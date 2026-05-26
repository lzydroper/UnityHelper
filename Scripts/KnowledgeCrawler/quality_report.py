from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from common import read_jsonl


def resolve_report_root(value: str) -> Path:
    root = Path(value)
    if root.is_absolute():
        return root

    cwd = Path.cwd().resolve()
    if cwd.name.lower() == "knowledgecrawler" and cwd.parent.name.lower() == "scripts":
        return cwd.parent.parent / root
    return cwd / root


def count_jsonl(path: Path) -> tuple[int, Counter[str]]:
    if not path.exists():
        return 0, Counter()
    counter: Counter[str] = Counter()
    total = 0
    for row in read_jsonl(path):
        total += 1
        counter[row.get("source", "unknown")] += 1
    return total, counter


def issue_comment_quality(path: Path) -> dict[str, object]:
    if not path.exists():
        return {
            "github_issues_with_selected_comments": 0,
            "selected_github_comments": 0,
            "avg_selected_comments_per_github_issue": 0,
        }
    github_total = 0
    with_selected = 0
    selected_total = 0
    relevance_scores: list[int] = []
    for row in read_jsonl(path):
        if row.get("source") != "github_issue":
            continue
        github_total += 1
        selected = row.get("selected_comments") or []
        selected_total += len(selected)
        if selected:
            with_selected += 1
        if isinstance(row.get("relevance_score"), int):
            relevance_scores.append(row["relevance_score"])
    avg = round(selected_total / github_total, 2) if github_total else 0
    avg_relevance = round(sum(relevance_scores) / len(relevance_scores), 2) if relevance_scores else 0
    return {
        "github_issues": github_total,
        "github_issues_with_selected_comments": with_selected,
        "selected_github_comments": selected_total,
        "avg_selected_comments_per_github_issue": avg,
        "avg_github_relevance_score": avg_relevance,
    }


def bundle_files(root: Path) -> list[dict[str, object]]:
    bundle_dir = processed_root_for(root) / "dify_bundle"
    if not bundle_dir.exists():
        return []
    rows = []
    for path in sorted(bundle_dir.glob("*.md")):
        size = path.stat().st_size
        rows.append(
            {
                "file": str(path),
                "size_mb": round(size / 1024 / 1024, 3),
                "under_15mb": size <= 15 * 1024 * 1024,
            }
        )
    return rows


def processed_root_for(root: Path) -> Path:
    clean_processed = root / "processed_clean"
    return clean_processed if clean_processed.exists() else root / "processed"


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize knowledge-base collection and Dify preparation counts.")
    parser.add_argument("--root", default="Data/KnowledgeBase", help="Knowledge-base output root.")
    args = parser.parse_args()

    root = resolve_report_root(args.root)
    unity_total, unity_sources = count_jsonl(root / "raw" / "unity_docs" / "unity_docs.jsonl")
    unity_clean_total, unity_clean_sources = count_jsonl(root / "raw" / "unity_docs" / "unity_docs_clean.jsonl")
    unity_rejected_total, _ = count_jsonl(root / "raw" / "unity_docs" / "unity_docs_rejected.jsonl")
    issue_total, issue_sources = count_jsonl(root / "raw" / "issues" / "issues.jsonl")
    issue_quality = issue_comment_quality(root / "raw" / "issues" / "issues.jsonl")
    processed_root = processed_root_for(root)
    chunk_total, chunk_sources = count_jsonl(processed_root / "manifest.jsonl")
    bundles = bundle_files(root)

    report = {
        "root": str(root),
        "processed_root": str(processed_root),
        "unity_pages": unity_total,
        "unity_clean_pages": unity_clean_total,
        "unity_rejected_pages": unity_rejected_total,
        "issues": issue_total,
        "issue_quality": issue_quality,
        "dify_chunks": chunk_total,
        "dify_bundle_files": bundles,
        "unity_sources": dict(unity_sources),
        "unity_clean_sources": dict(unity_clean_sources),
        "issue_sources": dict(issue_sources),
        "chunk_sources": dict(chunk_sources),
        "acceptance_targets": {
            "unity_pages": ">= 1500",
            "issues": ">= 200",
            "effective_dify_chunks": ">= 1000"
        }
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
