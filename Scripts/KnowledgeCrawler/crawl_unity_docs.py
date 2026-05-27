from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import Counter, deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from common import append_jsonl, ensure_dir, load_config, polite_sleep, read_jsonl, resolve_output_root, stable_id, write_jsonl
from unity_doc_cleaner import extract_page, is_low_value_page


def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""
    if not parsed.path or parsed.path.endswith("/"):
        path = parsed.path + "index.html"
    else:
        path = parsed.path
    return parsed._replace(path=path, query="").geturl()


def is_allowed(url: str, domains: set[str], prefixes: list[str]) -> bool:
    parsed = urlparse(url)
    if parsed.netloc not in domains:
        return False
    if not parsed.path.endswith(".html"):
        return False
    return any(parsed.path.startswith(prefix) for prefix in prefixes)


def section_from_url(url: str) -> str:
    return "ScriptReference" if "/ScriptReference/" in url else "Manual"


def section_base_url(seed_url: str) -> str:
    parsed = urlparse(seed_url)
    path = parsed.path
    for marker in ["/Manual/", "/ScriptReference/"]:
        if marker in path:
            prefix = path.split(marker)[0] + marker
            return parsed._replace(path=prefix, query="").geturl()
    return seed_url


def extract_toc_links(seed_url: str, html: str, session: requests.Session, headers: dict[str, str]) -> set[str]:
    soup = BeautifulSoup(html, "html.parser")
    script_urls: list[str] = []
    for script in soup.find_all("script", src=True):
        src = script.get("src", "")
        if "docdata/" in src and src.endswith(".js"):
            script_urls.append(urljoin(seed_url, src))
    script_urls.extend(
        [
            urljoin(section_base_url(seed_url), "docdata/toc.js"),
            urljoin(section_base_url(seed_url), "docdata/global_toc.js"),
        ]
    )

    links: set[str] = set()
    base = section_base_url(seed_url)
    for script_url in dict.fromkeys(script_urls):
        try:
            response = session.get(script_url, headers=headers, timeout=25)
            response.raise_for_status()
        except requests.RequestException:
            continue
        for href in re.findall(r"""["']([^"']+\.html(?:#[^"']*)?)["']""", response.text):
            if href.startswith(("http://", "https://", "/")) or href.startswith("../"):
                candidate = urljoin(script_url, href)
            else:
                candidate = urljoin(base, href)
            normalized = normalize_url(candidate)
            if normalized:
                links.add(normalized)
    return links


def iter_links(base_url: str, html: str, domains: set[str], prefixes: list[str]) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []
    for anchor in soup.find_all("a", href=True):
        href = anchor.get("href", "")
        normalized = normalize_url(urljoin(base_url, href))
        if normalized and is_allowed(normalized, domains, prefixes):
            links.append(normalized)
    return links


def read_existing_rows(path: Path) -> list[dict[str, object]]:
    if not path.exists():
        return []
    return list(read_jsonl(path))


def ok_url_set(rows: list[dict[str, object]]) -> set[str]:
    return {str(row.get("url", "")) for row in rows if row.get("url") and row.get("status") == "ok"}


def section_counts(rows: list[dict[str, object]]) -> Counter[str]:
    counter: Counter[str] = Counter()
    for row in rows:
        if row.get("status") == "ok":
            counter[str(row.get("section", ""))] += 1
    return counter


def normalize_section_targets(raw_targets: object) -> dict[str, int]:
    if not isinstance(raw_targets, dict):
        return {}
    targets: dict[str, int] = {}
    for key, value in raw_targets.items():
        try:
            targets[str(key)] = int(value)
        except (TypeError, ValueError):
            continue
    return targets


def section_target_reached(section: str, counts: Counter[str], targets: dict[str, int]) -> bool:
    target = targets.get(section)
    return target is not None and counts[section] >= target


def replace_rows_by_url(
    existing_rows: list[dict[str, object]],
    refreshed_rows: list[dict[str, object]],
    new_rows: list[dict[str, object]],
) -> list[dict[str, object]]:
    refreshed_by_url = {str(row.get("url", "")): row for row in refreshed_rows if row.get("url")}
    merged: list[dict[str, object]] = []
    for row in existing_rows:
        url = str(row.get("url", ""))
        merged.append(refreshed_by_url.pop(url, row))
    merged.extend(refreshed_by_url.values())
    merged.extend(new_rows)
    return merged


def next_incremental_batch(raw_dir: Path) -> tuple[str, Path]:
    date_code = dt.datetime.now().strftime("%y%m%d")
    base = f"unity_docs_incremental_{date_code}"
    base_path = raw_dir / f"{base}.jsonl"
    if not base_path.exists():
        return base, base_path
    for index in range(2, 1000):
        batch_id = f"{base}_{index:03d}"
        path = raw_dir / f"{batch_id}.jsonl"
        if not path.exists():
            return batch_id, path
    raise RuntimeError(f"Unable to allocate incremental Unity docs batch under {raw_dir}")


def crawl(
    config_path: str | Path,
    incremental: bool = False,
    max_new_pages: int | None = None,
    refresh_existing: bool = False,
) -> Path:
    config = load_config(config_path)
    unity_cfg = config["unity_docs"]
    output_root = resolve_output_root(config, config_path)
    raw_dir = ensure_dir(output_root / "raw" / "unity_docs")
    html_dir = ensure_dir(raw_dir / "html")
    jsonl_path = raw_dir / "unity_docs.jsonl"

    domains = set(unity_cfg["allowed_domains"])
    prefixes = list(unity_cfg["allowed_path_prefixes"])
    max_pages = int(unity_cfg.get("max_pages", 1600))
    section_targets = normalize_section_targets(unity_cfg.get("section_targets", {}))
    min_effective_chars = int(unity_cfg.get("min_effective_chars", 140))
    use_toc = bool(unity_cfg.get("use_toc", True))
    preserve_image_refs = bool(unity_cfg.get("preserve_image_refs", True))
    delay = float(unity_cfg.get("delay_seconds", 0.6))
    headers = {"User-Agent": unity_cfg.get("user_agent", "UnityDevAssistantCourseProject/1.0")}

    seed_urls = [normalize_url(seed) for seed in unity_cfg["seeds"]]
    queue = deque(seed_urls)
    seen: set[str] = set()
    queued: set[str] = set(seed_urls)
    docs: list[dict[str, object]] = []
    refreshed_docs: list[dict[str, object]] = []
    session = requests.Session()
    existing_rows = read_existing_rows(jsonl_path) if incremental else []
    existing_ok_urls = ok_url_set(existing_rows)
    existing_count = len([row for row in existing_rows if row.get("status") == "ok"]) if incremental else 0
    counts = section_counts(existing_rows)
    batch_id, incremental_path = next_incremental_batch(raw_dir)

    if incremental and max_new_pages == 0:
        print("No Unity documentation records requested because --max-new-pages is 0.")
        return jsonl_path

    def queue_cached_links(url: str) -> None:
        html_path = html_dir / f"{stable_id(url, 'unity_')}.html"
        if not html_path.exists():
            return
        html = html_path.read_text(encoding="utf-8")
        for link in iter_links(url, html, domains, prefixes):
            if link not in seen and link not in queued:
                queue.append(link)
                queued.add(link)

    if use_toc:
        for seed in seed_urls:
            if not seed or not is_allowed(seed, domains, prefixes):
                continue
            try:
                response = session.get(seed, headers=headers, timeout=25)
                response.raise_for_status()
            except requests.RequestException:
                continue
            for link in extract_toc_links(seed, response.text, session, headers):
                if link not in queued and is_allowed(link, domains, prefixes):
                    queue.append(link)
                    queued.add(link)
            polite_sleep(delay)

    total_limit = max(0, max_pages - existing_count) if incremental else max_pages
    if max_new_pages is not None:
        total_limit = min(total_limit, max(0, max_new_pages))

    with tqdm(total=total_limit, desc="Unity docs") as bar:
        while queue and len(docs) < total_limit:
            url = queue.popleft()
            if not url or url in seen or not is_allowed(url, domains, prefixes):
                continue
            if incremental and not refresh_existing and url in existing_ok_urls:
                seen.add(url)
                queue_cached_links(url)
                continue
            section = section_from_url(url)
            if section_target_reached(section, counts, section_targets):
                seen.add(url)
                continue
            seen.add(url)

            try:
                response = session.get(url, headers=headers, timeout=25)
                response.raise_for_status()
            except requests.RequestException as exc:
                doc: dict[str, object] = {
                    "id": stable_id(url, "unity_error_"),
                    "source": "unity_docs",
                    "url": url,
                    "status": "fetch_error",
                    "error": str(exc),
                    "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
                }
                if incremental:
                    doc["crawl_batch"] = batch_id
                docs.append(doc)
                bar.update(1)
                polite_sleep(delay)
                continue

            html = response.text
            page_id = stable_id(url, "unity_")
            (html_dir / f"{page_id}.html").write_text(html, encoding="utf-8")
            title, body, headings = extract_page(url, html, preserve_image_refs=preserve_image_refs)
            doc = {
                "id": page_id,
                "source": "unity_docs",
                "source_type": "official_documentation",
                "section": section,
                "url": url,
                "title": title,
                "headings": headings[:12],
                "content": body,
                "language": "csharp" if section == "ScriptReference" else "",
                "status": "ok",
                "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
            }
            if incremental:
                doc["crawl_batch"] = batch_id
            if len(body) >= 120 and not is_low_value_page(url, title, body, min_effective_chars):
                if incremental and refresh_existing and url in existing_ok_urls:
                    doc["refreshed_at"] = dt.datetime.now(dt.UTC).isoformat()
                    refreshed_docs.append(doc)
                else:
                    docs.append(doc)
                    counts[section] += 1
                bar.update(1)

            for link in iter_links(url, html, domains, prefixes):
                if link not in seen and link not in queued:
                    queue.append(link)
                    queued.add(link)
            polite_sleep(delay)

    if incremental:
        if refresh_existing:
            write_jsonl(jsonl_path, replace_rows_by_url(existing_rows, refreshed_docs, docs))
        else:
            for doc in docs:
                append_jsonl(jsonl_path, doc)
        if docs:
            write_jsonl(incremental_path, docs)
            print(f"Wrote {len(docs)} incremental Unity documentation records to {incremental_path}")
        if refreshed_docs:
            print(f"Refreshed {len(refreshed_docs)} existing Unity documentation records in {jsonl_path}")
    else:
        write_jsonl(jsonl_path, docs)
    total_written = len(docs) + (len(refreshed_docs) if refresh_existing else 0)
    print(f"Wrote {total_written} Unity documentation records to {jsonl_path}")
    return jsonl_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl Unity official Manual and Scripting API pages.")
    parser.add_argument("--config", required=True, help="Path to KnowledgeCrawler config JSON.")
    parser.add_argument("--incremental", action="store_true", help="Append only newly discovered Unity docs.")
    parser.add_argument("--max-new-pages", type=int, default=None, help="Maximum number of new pages for this run.")
    parser.add_argument(
        "--refresh-existing",
        action="store_true",
        help="When used with --incremental, refresh already known URLs instead of skipping them.",
    )
    args = parser.parse_args()
    crawl(
        args.config,
        incremental=args.incremental,
        max_new_pages=args.max_new_pages,
        refresh_existing=args.refresh_existing,
    )


if __name__ == "__main__":
    main()
