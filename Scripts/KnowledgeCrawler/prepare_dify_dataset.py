from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
from pathlib import Path
from typing import Any, Iterable

from common import clean_text, ensure_dir, load_config, read_jsonl, resolve_output_root, safe_filename, stable_id, write_jsonl


DATASETS = {"all", "unity_docs", "issues", "lua_docs"}
UNITY_SOURCE_MODES = {"auto", "full", "incremental"}


def split_paragraphs(text: str) -> list[str]:
    parts = [part.strip() for part in text.split("\n") if part.strip()]
    return parts


def chunk_text(text: str, size: int, overlap: int, min_chars: int) -> list[str]:
    paragraphs = split_paragraphs(text)
    chunks: list[str] = []
    current = ""
    for paragraph in paragraphs:
        candidate = f"{current}\n\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= size:
            current = candidate
            continue
        if len(current) >= min_chars:
            chunks.append(current)
            current = current[-overlap:] if overlap > 0 else ""
        if len(paragraph) > size:
            start = 0
            while start < len(paragraph):
                piece = paragraph[start : start + size]
                if len(piece) >= min_chars:
                    chunks.append(piece)
                start += max(1, size - overlap)
            current = ""
        else:
            current = paragraph
    if len(current) >= min_chars:
        chunks.append(current)
    return chunks


def frontmatter(metadata: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in metadata.items():
        if isinstance(value, list):
            value = ", ".join(str(item) for item in value)
        text = str(value).replace("\n", " ").replace('"', "'")
        lines.append(f'{key}: "{text}"')
    lines.append("---")
    return "\n".join(lines)


def source_markdown(row: dict[str, Any]) -> str:
    title = clean_text(row.get("title", "")) or row.get("url", "")
    url = row.get("url", "")
    content = clean_text(row.get("content", ""))
    source = row.get("source", "")
    section = row.get("section", "")
    framework = row.get("framework", "")
    heading = f"# {title}".strip()
    meta_lines = [
        f"- Source: {source}",
        f"- Section: {section}" if section else "",
        f"- Framework: {framework}" if framework else "",
        f"- URL: {url}",
    ]
    meta = "\n".join(line for line in meta_lines if line)
    return f"{heading}\n\n{meta}\n\n{content}".strip()


def bundle_name(row: dict[str, Any]) -> str:
    source = row.get("source", "")
    if source == "unity_docs":
        crawl_batch = str(row.get("crawl_batch", ""))
        if crawl_batch.startswith("unity_docs_incremental_"):
            return crawl_batch.replace("unity_docs", "unity_official_docs", 1)
        return "unity_official_docs"
    if source in {"github_issue", "stackoverflow"}:
        return "unity_issues_cases"
    if source == "lua_docs":
        return "unity_lua_hot_update"
    return str(source or "misc")


class BundleWriter:
    def __init__(self, bundle_dir: Path, max_bytes: int) -> None:
        self.bundle_dir = ensure_dir(bundle_dir)
        self.max_bytes = max_bytes
        self.parts: dict[str, int] = {}
        self.bytes_used: dict[str, int] = {}
        self.files: dict[str, dict[str, Any]] = {}
        self.touched: set[Path] = set()

    def _path(self, name: str) -> Path:
        part = self.parts.setdefault(name, 1)
        if name.startswith("unity_official_docs_incremental_"):
            return self.bundle_dir / f"{name}_{part:03d}.md"
        return self.bundle_dir / f"{name}_bundle_{part:03d}.md"

    def add(self, name: str, document: str, row: dict[str, Any]) -> None:
        block = (
            "\n\n---\n\n"
            f"<!-- source={row.get('source', '')}; title={row.get('title', '')}; url={row.get('url', '')} -->\n\n"
            f"{document.strip()}\n"
        )
        block_bytes = len(block.encode("utf-8"))
        current_bytes = self.bytes_used.get(name, 0)
        if current_bytes > 0 and current_bytes + block_bytes > self.max_bytes:
            self.parts[name] = self.parts.get(name, 1) + 1
            self.bytes_used[name] = 0
            current_bytes = 0

        path = self._path(name)
        header = ""
        if path not in self.touched:
            header = f"# {name}\n\nThis file is a Dify upload bundle generated from local JSONL sources.\n"
            path.write_text(header, encoding="utf-8", newline="\n")
            self.touched.add(path)

        with path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(block)

        used = current_bytes + len(header.encode("utf-8")) + block_bytes
        self.bytes_used[name] = used
        key = str(path)
        self.files[key] = {
            "file": key,
            "bundle": name,
            "part": self.parts[name],
            "bytes": used,
            "size_mb": round(used / 1024 / 1024, 3),
        }

    def manifest_rows(self) -> list[dict[str, Any]]:
        return sorted(self.files.values(), key=lambda row: row["file"])


def unity_full_source_path(output_root: Path) -> Path:
    unity_clean = output_root / "raw" / "unity_docs" / "unity_docs_clean.jsonl"
    unity_raw = output_root / "raw" / "unity_docs" / "unity_docs.jsonl"
    return unity_clean if unity_clean.exists() else unity_raw


def unity_incremental_source_paths(output_root: Path) -> list[Path]:
    raw_dir = output_root / "raw" / "unity_docs"
    clean_paths = sorted(raw_dir.glob("unity_docs_incremental_*_clean.jsonl"))
    if clean_paths:
        return clean_paths
    return sorted(
        path
        for path in raw_dir.glob("unity_docs_incremental_*.jsonl")
        if not path.name.endswith(("_clean.jsonl", "_rejected.jsonl"))
    )


def selected_source_paths(output_root: Path, dataset: str, unity_source_mode: str) -> list[Path]:
    paths: list[Path] = []
    if dataset in {"all", "unity_docs"}:
        if dataset == "all" or unity_source_mode == "full":
            paths.append(unity_full_source_path(output_root))
        else:
            incremental_paths = unity_incremental_source_paths(output_root)
            if incremental_paths:
                paths.extend(incremental_paths)
            elif unity_source_mode == "auto":
                paths.append(unity_full_source_path(output_root))

    if dataset in {"all", "issues"}:
        paths.append(output_root / "raw" / "issues" / "issues.jsonl")

    if dataset in {"all", "lua_docs"}:
        paths.append(output_root / "raw" / "lua_docs" / "lua_docs.jsonl")

    return paths


def iter_source_rows(output_root: Path, dataset: str, unity_source_mode: str) -> Iterable[dict[str, Any]]:
    for path in selected_source_paths(output_root, dataset, unity_source_mode):
        if path.exists():
            yield from read_jsonl(path)


def processed_root_for(output_root: Path) -> Path:
    clean_source = output_root / "raw" / "unity_docs" / "unity_docs_clean.jsonl"
    return output_root / ("processed_clean" if clean_source.exists() else "processed")


def manifest_suffix(dataset: str) -> str:
    return "" if dataset == "all" else f"_{dataset}"


def prepare(config_path: str | Path, dataset: str = "all", unity_source_mode: str = "auto") -> Path:
    if dataset not in DATASETS:
        raise ValueError(f"Unsupported dataset: {dataset}")
    if unity_source_mode not in UNITY_SOURCE_MODES:
        raise ValueError(f"Unsupported Unity source mode: {unity_source_mode}")

    config = load_config(config_path)
    output_root = resolve_output_root(config, config_path)
    prep_cfg = config.get("dify_prepare", {})
    size = int(prep_cfg.get("chunk_size_chars", 1800))
    overlap = int(prep_cfg.get("chunk_overlap_chars", 180))
    min_chars = int(prep_cfg.get("min_chunk_chars", 220))
    bundle_max_bytes = int(float(prep_cfg.get("bundle_max_mb", 14.5)) * 1024 * 1024)

    processed_root = ensure_dir(processed_root_for(output_root))
    import_dir = ensure_dir(processed_root / "dify_import")
    bundle_dir = ensure_dir(processed_root / "dify_bundle")
    suffix = manifest_suffix(dataset)
    manifest_jsonl = processed_root / f"manifest{suffix}.jsonl"
    manifest_csv = processed_root / f"manifest{suffix}.csv"
    bundle_manifest_jsonl = processed_root / f"bundle_manifest{suffix}.jsonl"

    manifest_rows: list[dict[str, Any]] = []
    bundle_writer = BundleWriter(bundle_dir, bundle_max_bytes)
    for row in iter_source_rows(output_root, dataset, unity_source_mode):
        if row.get("status") not in {None, "", "ok"}:
            continue
        markdown = source_markdown(row)
        bundle_writer.add(bundle_name(row), markdown, row)
        chunks = chunk_text(markdown, size=size, overlap=overlap, min_chars=min_chars)
        for index, chunk in enumerate(chunks, start=1):
            chunk_id = stable_id(f"{row.get('id')}:{index}", "chunk_")
            metadata = {
                "chunk_id": chunk_id,
                "source_id": row.get("id", ""),
                "source": row.get("source", ""),
                "source_type": row.get("source_type", ""),
                "section": row.get("section", ""),
                "framework": row.get("framework", ""),
                "title": row.get("title", ""),
                "url": row.get("url", ""),
                "crawl_batch": row.get("crawl_batch", ""),
                "chunk_index": index,
                "prepared_at": dt.datetime.now(dt.UTC).isoformat(),
            }
            file_name = safe_filename(f"{metadata['source']}_{chunk_id}", ".md")
            file_path = import_dir / file_name
            file_path.write_text(f"{frontmatter(metadata)}\n\n{chunk}\n", encoding="utf-8", newline="\n")
            manifest = dict(metadata)
            manifest["file"] = str(file_path.as_posix())
            manifest["chars"] = len(chunk)
            manifest_rows.append(manifest)

    ensure_dir(manifest_jsonl.parent)
    write_jsonl(manifest_jsonl, manifest_rows)
    bundle_rows = bundle_writer.manifest_rows()
    write_jsonl(bundle_manifest_jsonl, bundle_rows)
    with manifest_csv.open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames = [
            "chunk_id",
            "source_id",
            "source",
            "source_type",
            "section",
            "framework",
            "title",
            "url",
            "crawl_batch",
            "chunk_index",
            "file",
            "chars",
            "prepared_at",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in manifest_rows:
            writer.writerow({key: row.get(key, "") for key in fieldnames})

    print(
        json.dumps(
            {
                "dataset": dataset,
                "unity_source_mode": unity_source_mode,
                "chunks": len(manifest_rows),
                "processed_root": str(processed_root),
                "chunk_import_dir": str(import_dir),
                "bundle_import_dir": str(bundle_dir),
                "bundles": bundle_rows,
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return import_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Prepare cleaned Markdown chunks for Dify dataset import.")
    parser.add_argument("--config", required=True, help="Path to KnowledgeCrawler config JSON.")
    parser.add_argument(
        "--dataset",
        choices=sorted(DATASETS),
        default="all",
        help="Dataset direction to prepare. Defaults to all for backward compatibility.",
    )
    parser.add_argument(
        "--unity-source-mode",
        choices=sorted(UNITY_SOURCE_MODES),
        default="auto",
        help="Use full or incremental Unity docs when --dataset unity_docs. Auto prefers incremental files.",
    )
    args = parser.parse_args()
    prepare(args.config, dataset=args.dataset, unity_source_mode=args.unity_source_mode)


if __name__ == "__main__":
    main()
