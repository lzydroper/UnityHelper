from __future__ import annotations

import argparse
import datetime as dt
import re
from collections import deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from common import clean_text, ensure_dir, load_config, polite_sleep, resolve_output_root, stable_id, write_jsonl
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


def crawl(config_path: str | Path) -> Path:
    config = load_config(config_path)
    unity_cfg = config["unity_docs"]
    output_root = resolve_output_root(config, config_path)
    raw_dir = ensure_dir(output_root / "raw" / "unity_docs")
    html_dir = ensure_dir(raw_dir / "html")
    jsonl_path = raw_dir / "unity_docs.jsonl"

    domains = set(unity_cfg["allowed_domains"])
    prefixes = list(unity_cfg["allowed_path_prefixes"])
    max_pages = int(unity_cfg.get("max_pages", 1600))
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
    session = requests.Session()

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

    with tqdm(total=max_pages, desc="Unity docs") as bar:
        while queue and len(docs) < max_pages:
            url = queue.popleft()
            if not url or url in seen or not is_allowed(url, domains, prefixes):
                continue
            seen.add(url)

            try:
                response = session.get(url, headers=headers, timeout=25)
                response.raise_for_status()
            except requests.RequestException as exc:
                docs.append(
                    {
                        "id": stable_id(url, "unity_error_"),
                        "source": "unity_docs",
                        "url": url,
                        "status": "fetch_error",
                        "error": str(exc),
                        "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
                    }
                )
                bar.update(1)
                polite_sleep(delay)
                continue

            html = response.text
            page_id = stable_id(url, "unity_")
            (html_dir / f"{page_id}.html").write_text(html, encoding="utf-8")
            title, body, headings = extract_page(url, html, preserve_image_refs=preserve_image_refs)
            section = section_from_url(url)
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
            if len(body) >= 120 and not is_low_value_page(url, title, body, min_effective_chars):
                docs.append(doc)
                bar.update(1)

            for link in iter_links(url, html, domains, prefixes):
                if link not in seen and link not in queued:
                    queue.append(link)
                    queued.add(link)
            polite_sleep(delay)

    write_jsonl(jsonl_path, docs)
    print(f"Wrote {len(docs)} Unity documentation records to {jsonl_path}")
    return jsonl_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl Unity official Manual and Scripting API pages.")
    parser.add_argument("--config", required=True, help="Path to KnowledgeCrawler config JSON.")
    args = parser.parse_args()
    crawl(args.config)


if __name__ == "__main__":
    main()
