from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path

from common import ensure_dir, read_jsonl


CATEGORIES: dict[str, list[str]] = {
    "空引用与对象生命周期": [
        "nullreferenceexception",
        "missingreferenceexception",
        "object reference not set",
        "destroyed",
        "getcomponent",
    ],
    "编译与命名空间": [
        "cs0246",
        "namespace",
        "assembly",
        "compiler error",
        "could not be found",
    ],
    "构建与IL2CPP": [
        "il2cpp",
        "build failed",
        "gradle",
        "android build",
        "ios build",
    ],
    "包管理": [
        "package manager",
        "manifest.json",
        "upm",
        "dependency",
        "packages-lock",
    ],
    "输入系统": [
        "input system",
        "inputsystem",
        "input.getaxis",
        "inputaction",
        "controls",
    ],
    "Addressables与资源加载": [
        "addressables",
        "assetbundle",
        "loadasset",
        "resource",
        "remote catalog",
    ],
    "Shader与渲染": [
        "shader",
        "pink material",
        "urp",
        "hdrp",
        "render pipeline",
    ],
    "API弃用与版本迁移": [
        "obsolete",
        "deprecated",
        "upgrade",
        "migration",
        "unity 6",
        "unity 2022",
    ],
}


def classify(text: str) -> str:
    lowered = text.lower()
    scores: Counter[str] = Counter()
    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in lowered:
                scores[category] += 1
    return scores.most_common(1)[0][0] if scores else "其他"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a simple category report for collected Unity issues.")
    parser.add_argument("--input", default="Data/KnowledgeBase/raw/issues/issues.jsonl", help="Path to issues JSONL.")
    parser.add_argument("--output-dir", default="Data/KnowledgeBase/reports", help="Report output directory.")
    args = parser.parse_args()

    input_path = Path(args.input)
    output_dir = ensure_dir(args.output_dir)
    counts: Counter[str] = Counter()
    rows: list[dict[str, object]] = []

    for row in read_jsonl(input_path):
        text = "\n".join(
            [
                str(row.get("title", "")),
                str(row.get("content", "")),
                " ".join(str(label) for label in row.get("labels", [])),
                str(row.get("query", "")),
            ]
        )
        category = classify(text)
        counts[category] += 1
        rows.append(
            {
                "category": category,
                "source": row.get("source", ""),
                "title": row.get("title", ""),
                "url": row.get("url", ""),
            }
        )

    summary = {
        "total": sum(counts.values()),
        "categories": dict(counts.most_common()),
    }
    (output_dir / "issue_category_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    with (output_dir / "issue_category_details.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["category", "source", "title", "url"])
        writer.writeheader()
        writer.writerows(rows)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
