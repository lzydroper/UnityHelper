from __future__ import annotations

import hashlib
import json
import re
import time
from pathlib import Path
from typing import Any, Iterable


WHITESPACE_RE = re.compile(r"[ \t\r\f\v]+")
BLANK_LINE_RE = re.compile(r"\n{3,}")


def load_config(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as f:
        return json.load(f)


def resolve_output_root(config: dict[str, Any], config_path: str | Path) -> Path:
    root = Path(config.get("output_root", "Data/KnowledgeBase"))
    if root.is_absolute():
        return root

    config_dir = Path(config_path).resolve().parent
    if config_dir.name.lower() == "knowledgecrawler" and config_dir.parent.name.lower() == "scripts":
        return config_dir.parent.parent / root
    return config_dir / root


def ensure_dir(path: str | Path) -> Path:
    out = Path(path)
    out.mkdir(parents=True, exist_ok=True)
    return out


def stable_id(value: str, prefix: str = "") -> str:
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:16]
    return f"{prefix}{digest}" if prefix else digest


def clean_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = WHITESPACE_RE.sub(" ", text)
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(line for line in lines if line)
    return BLANK_LINE_RE.sub("\n\n", text).strip()


def write_jsonl(path: str | Path, rows: Iterable[dict[str, Any]]) -> int:
    count = 0
    out = Path(path)
    ensure_dir(out.parent)
    with out.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
            count += 1
    return count


def append_jsonl(path: str | Path, row: dict[str, Any]) -> None:
    out = Path(path)
    ensure_dir(out.parent)
    with out.open("a", encoding="utf-8", newline="\n") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: str | Path) -> Iterable[dict[str, Any]]:
    with Path(path).open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                yield json.loads(line)


def polite_sleep(seconds: float) -> None:
    if seconds > 0:
        time.sleep(seconds)


def safe_filename(value: str, suffix: str = ".md") -> str:
    name = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")
    return f"{name[:120]}{suffix}"
