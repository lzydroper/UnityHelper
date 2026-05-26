from __future__ import annotations

import argparse
import datetime as dt
from pathlib import Path

from common import load_config, read_jsonl, resolve_output_root, write_jsonl
from unity_doc_cleaner import extract_page, is_low_value_page


def clean_existing(config_path: str | Path) -> Path:
    config = load_config(config_path)
    output_root = resolve_output_root(config, config_path)
    raw_dir = output_root / "raw" / "unity_docs"
    source_path = raw_dir / "unity_docs.jsonl"
    clean_path = raw_dir / "unity_docs_clean.jsonl"
    rejected_path = raw_dir / "unity_docs_rejected.jsonl"
    html_dir = raw_dir / "html"
    min_effective_chars = int(config.get("unity_docs", {}).get("min_effective_chars", 140))
    preserve_image_refs = bool(config.get("unity_docs", {}).get("preserve_image_refs", True))

    cleaned = []
    rejected = []
    for row in read_jsonl(source_path):
        if row.get("status") != "ok":
            rejected.append({**row, "reject_reason": "fetch_error_or_non_ok"})
            continue

        html_path = html_dir / f"{row['id']}.html"
        if html_path.exists():
            title, content, headings = extract_page(
                row.get("url", ""),
                html_path.read_text(encoding="utf-8"),
                preserve_image_refs=preserve_image_refs,
            )
            row = {**row, "title": title, "content": content, "headings": headings[:12]}

        if is_low_value_page(row.get("url", ""), row.get("title", ""), row.get("content", ""), min_effective_chars):
            rejected.append({**row, "reject_reason": f"effective_content_below_{min_effective_chars}_chars"})
            continue

        cleaned.append({**row, "cleaned_at": dt.datetime.now(dt.UTC).isoformat()})

    write_jsonl(clean_path, cleaned)
    write_jsonl(rejected_path, rejected)
    print(f"Wrote {len(cleaned)} cleaned Unity docs to {clean_path}")
    print(f"Wrote {len(rejected)} rejected/low-value Unity docs to {rejected_path}")
    return clean_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Re-clean existing Unity docs from saved HTML without crawling again.")
    parser.add_argument("--config", required=True, help="Path to KnowledgeCrawler config JSON.")
    args = parser.parse_args()
    clean_existing(args.config)


if __name__ == "__main__":
    main()
