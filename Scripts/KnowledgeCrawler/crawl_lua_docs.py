from __future__ import annotations

import argparse
import datetime as dt
from collections import Counter, deque
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from common import clean_text, ensure_dir, load_config, polite_sleep, resolve_output_root, stable_id, write_jsonl


DROP_SELECTORS = [
    "script",
    "style",
    "noscript",
    "nav",
    "header",
    "footer",
    ".Header",
    ".footer",
    ".js-header-wrapper",
    ".Layout-sidebar",
    ".breadcrumb",
    ".toc",
    ".wy-nav-side",
    ".wy-side-nav-search",
]

CONTENT_SELECTORS = [
    "article.markdown-body",
    ".markdown-body",
    ".document",
    ".rst-content",
    "main",
    "article",
    "body",
]

BLOCKED_GITHUB_PATH_PARTS = {
    "/_edit",
    "/_history",
    "/_new",
    "/actions",
    "/branches",
    "/commits",
    "/compare",
    "/forks",
    "/issues",
    "/labels",
    "/milestones",
    "/network",
    "/projects",
    "/pulls",
    "/pulse",
    "/releases",
    "/security",
    "/stargazers",
    "/tags",
    "/watchers",
}

ALLOWED_GITHUB_EXACT_PATHS = {
    "/Tencent/xLua",
    "/topameng/tolua",
    "/topameng/tolua/wiki",
}

ALLOWED_GITHUB_PATH_PREFIXES = (
    "/Tencent/xLua/blob/master/Assets/XLua/Doc",
    "/Tencent/xLua/blob/master/docs",
    "/Tencent/xLua/blob/master/README",
    "/Tencent/xLua/tree/master/Assets/XLua/Doc",
    "/Tencent/xLua/tree/master/docs",
    "/Tencent/xLua/tree/master/General",
    "/topameng/tolua/blob/master/Assets/ToLua/Examples",
    "/topameng/tolua/blob/master/README",
    "/topameng/tolua/wiki/",
)


def normalize_url(url: str) -> str:
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""
    path = parsed.path or "/"
    return parsed._replace(path=path, query="").geturl()


def is_allowed(url: str, prefixes: list[str], domains: set[str]) -> bool:
    parsed = urlparse(url)
    if parsed.netloc not in domains:
        return False
    if parsed.netloc == "github.com":
        if any(part in parsed.path for part in BLOCKED_GITHUB_PATH_PARTS):
            return False
        if parsed.path not in ALLOWED_GITHUB_EXACT_PATHS and not parsed.path.startswith(ALLOWED_GITHUB_PATH_PREFIXES):
            return False
    return any(url.startswith(prefix) for prefix in prefixes)


def content_node(soup: BeautifulSoup):
    for selector in CONTENT_SELECTORS:
        node = soup.select_one(selector)
        if node:
            return node
    return soup


def extract_page(url: str, html: str) -> tuple[str, str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    for selector in DROP_SELECTORS:
        for node in soup.select(selector):
            node.decompose()

    node = content_node(soup)
    title_node = node.find("h1") or soup.find("h1") or soup.find("title")
    title = clean_text(title_node.get_text(" ")) if title_node else url

    for pre in node.find_all("pre"):
        code_text = clean_text(pre.get_text("\n"))
        if code_text:
            pre.string = f"\n```\n{code_text}\n```\n"

    headings = [clean_text(h.get_text(" ")) for h in node.find_all(["h1", "h2", "h3"])]
    headings = [heading for heading in headings if heading]
    body = clean_text(node.get_text("\n"))
    return title, body, headings[:12]


def iter_links(base_url: str, html: str, prefixes: list[str], domains: set[str]) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links: list[str] = []
    for anchor in soup.find_all("a", href=True):
        href = anchor.get("href", "")
        normalized = normalize_url(urljoin(base_url, href))
        if normalized and is_allowed(normalized, prefixes, domains):
            links.append(normalized)
    return links


def normalize_seed(raw_seed: object) -> dict[str, str]:
    if isinstance(raw_seed, str):
        return {"url": normalize_url(raw_seed), "framework": "", "section": ""}
    if isinstance(raw_seed, dict):
        return {
            "url": normalize_url(str(raw_seed.get("url", ""))),
            "framework": str(raw_seed.get("framework", "")),
            "section": str(raw_seed.get("section", "")),
        }
    return {"url": "", "framework": "", "section": ""}


def normalize_framework_targets(raw_targets: object) -> dict[str, int]:
    if not isinstance(raw_targets, dict):
        return {}
    targets: dict[str, int] = {}
    for key, value in raw_targets.items():
        try:
            targets[str(key)] = int(value)
        except (TypeError, ValueError):
            continue
    return targets


def framework_target_reached(framework: str, counts: Counter[str], targets: dict[str, int]) -> bool:
    target = targets.get(framework)
    return target is not None and counts[framework] >= target


def crawl(config_path: str | Path) -> Path:
    config = load_config(config_path)
    lua_cfg = config.get("lua_docs", {})
    output_root = resolve_output_root(config, config_path)
    raw_dir = ensure_dir(output_root / "raw" / "lua_docs")
    html_dir = ensure_dir(raw_dir / "html")
    jsonl_path = raw_dir / "lua_docs.jsonl"

    seeds = [normalize_seed(seed) for seed in lua_cfg.get("seeds", [])]
    seed_by_url = {seed["url"]: seed for seed in seeds if seed["url"]}
    domains = set(lua_cfg.get("allowed_domains", []))
    allowed_prefixes = [normalize_url(prefix) for prefix in lua_cfg.get("allowed_url_prefixes", [])]
    max_pages = int(lua_cfg.get("max_pages", 40))
    framework_targets = normalize_framework_targets(lua_cfg.get("framework_targets", {}))
    min_effective_chars = int(lua_cfg.get("min_effective_chars", 120))
    delay = float(lua_cfg.get("delay_seconds", 0.6))
    headers = {"User-Agent": lua_cfg.get("user_agent", "UnityDevAssistantCourseProject/1.0")}

    queue = deque(seed_by_url)
    queued = set(seed_by_url)
    seen: set[str] = set()
    docs: list[dict[str, object]] = []
    framework_counts: Counter[str] = Counter()
    session = requests.Session()

    with tqdm(total=max_pages, desc="Lua docs") as bar:
        while queue and len(docs) < max_pages:
            url = queue.popleft()
            if not url or url in seen or not is_allowed(url, allowed_prefixes, domains):
                continue
            seen.add(url)

            seed_meta = seed_by_url.get(url, {})
            framework = seed_meta.get("framework", "")
            section = seed_meta.get("section", "")
            if framework and framework_target_reached(framework, framework_counts, framework_targets):
                continue

            try:
                response = session.get(url, headers=headers, timeout=25)
                response.raise_for_status()
            except requests.RequestException as exc:
                docs.append(
                    {
                        "id": stable_id(url, "lua_error_"),
                        "source": "lua_docs",
                        "source_type": "lua_hot_update_documentation",
                        "framework": framework,
                        "section": section,
                        "url": url,
                        "status": "fetch_error",
                        "error": str(exc),
                        "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
                    }
                )
                framework_counts[framework] += 1
                bar.update(1)
                polite_sleep(delay)
                continue

            html = response.text
            page_id = stable_id(url, "lua_")
            (html_dir / f"{page_id}.html").write_text(html, encoding="utf-8")
            title, body, headings = extract_page(url, html)

            if len(body) >= min_effective_chars:
                docs.append(
                    {
                        "id": page_id,
                        "source": "lua_docs",
                        "source_type": "lua_hot_update_documentation",
                        "framework": framework,
                        "section": section or framework,
                        "url": url,
                        "title": title,
                        "headings": headings,
                        "content": body,
                        "language": "lua",
                        "status": "ok",
                        "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
                    }
                )
                framework_counts[framework] += 1
                bar.update(1)

            for link in iter_links(url, html, allowed_prefixes, domains):
                if link not in seen and link not in queued:
                    queue.append(link)
                    queued.add(link)
                    if framework or section:
                        seed_by_url.setdefault(link, {"url": link, "framework": framework, "section": section})
            polite_sleep(delay)

    write_jsonl(jsonl_path, docs)
    print(f"Wrote {len(docs)} Lua documentation records to {jsonl_path}")
    return jsonl_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl xLua and toLua documentation pages.")
    parser.add_argument("--config", required=True, help="Path to KnowledgeCrawler config JSON.")
    args = parser.parse_args()
    crawl(args.config)


if __name__ == "__main__":
    main()
