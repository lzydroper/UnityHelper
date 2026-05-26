from __future__ import annotations

import argparse
import datetime as dt
import math
import os
from pathlib import Path
from typing import Any

import requests
from tqdm import tqdm

from common import clean_text, load_config, polite_sleep, resolve_output_root, stable_id, write_jsonl


UNITY_RELEVANCE_TERMS = {
    "unity",
    "unity3d",
    "unityengine",
    "unityeditor",
    "monobehaviour",
    "gameobject",
    "scriptableobject",
    "prefab",
    "rigidbody",
    "collider",
    "scene",
    "inspector",
    "addressables",
    "inputsystem",
    "input system",
    "il2cpp",
    "urp",
    "hdrp",
    "shader",
    "cinemachine",
    "xr",
    "ar foundation",
    "ml-agents",
}

SOLUTION_TERMS = {
    "fix",
    "fixed",
    "solved",
    "resolved",
    "workaround",
    "solution",
    "try",
    "use",
    "set",
    "change",
    "update",
    "upgrade",
    "downgrade",
    "install",
    "remove",
    "delete",
    "caused by",
    "because",
    "root cause",
    "merged",
    "duplicate of",
    "closing",
}

LOW_VALUE_COMMENT_TERMS = {
    "+1",
    "same here",
    "same issue",
    "me too",
    "any update",
    "bump",
    "still happening",
    "still occurs",
    "confirmed",
}


def github_repo_name(item: dict[str, Any]) -> str:
    repo_url = item.get("repository_url", "")
    if "/repos/" in repo_url:
        return repo_url.split("/repos/", 1)[1]
    html_url = item.get("html_url", "")
    parts = html_url.split("/")
    if len(parts) >= 5:
        return f"{parts[3]}/{parts[4]}"
    return ""


def issue_relevance_score(item: dict[str, Any]) -> int:
    repo = github_repo_name(item).lower()
    labels = " ".join(label.get("name", "") for label in item.get("labels", []) if isinstance(label, dict))
    text = clean_text(f"{item.get('title', '')}\n{item.get('body', '')}\n{labels}\n{repo}").lower()
    score = 0
    if repo.startswith("unity-technologies/"):
        score += 3
    if any(term in text for term in UNITY_RELEVANCE_TERMS):
        score += 2
    score += min(3, sum(1 for term in UNITY_RELEVANCE_TERMS if term in text))
    if any(error in text for error in ["nullreferenceexception", "missingreferenceexception", "il2cpp", "shader error"]):
        score += 1
    return score


def reaction_count(comment: dict[str, Any]) -> int:
    reactions = comment.get("reactions") or {}
    if not isinstance(reactions, dict):
        return 0
    return sum(value for key, value in reactions.items() if key != "url" and isinstance(value, int))


def score_comment(comment: dict[str, Any]) -> int:
    body = clean_text(comment.get("body") or "")
    text = body.lower()
    if len(body) < 40:
        return -5

    score = 0
    author_association = str(comment.get("author_association", "")).upper()
    if author_association in {"OWNER", "MEMBER", "COLLABORATOR"}:
        score += 5
    if any(term in text for term in SOLUTION_TERMS):
        score += 4
    if "```" in body or "`" in body:
        score += 3
    if any(term in text for term in UNITY_RELEVANCE_TERMS):
        score += 2
    score += min(4, reaction_count(comment))
    if len(body) > 200:
        score += 1
    if any(term in text for term in LOW_VALUE_COMMENT_TERMS) and len(body) < 180:
        score -= 4
    return score


def select_solution_comments(comments: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    scored = [(score_comment(comment), index, comment) for index, comment in enumerate(comments)]
    useful = [(score, index, comment) for score, index, comment in scored if score > 0]
    useful.sort(key=lambda item: (-item[0], item[1]))
    selected = useful[:limit]
    selected.sort(key=lambda item: item[1])
    rows: list[dict[str, Any]] = []
    for score, _, comment in selected:
        user = comment.get("user") or {}
        rows.append(
            {
                "score": score,
                "author": user.get("login", ""),
                "author_association": comment.get("author_association", ""),
                "created_at": comment.get("created_at", ""),
                "url": comment.get("html_url", ""),
                "body": clean_text(comment.get("body") or ""),
                "reactions": reaction_count(comment),
            }
        )
    return rows


def fetch_github_comments(
    session: requests.Session,
    comments_url: str,
    headers: dict[str, str],
    total_comments: int,
    per_page: int,
    pages_mode: str,
) -> list[dict[str, Any]]:
    if not comments_url or total_comments <= 0:
        return []
    per_page = max(1, min(100, per_page))
    last_page = max(1, math.ceil(total_comments / per_page))
    if pages_mode == "all":
        pages = list(range(1, last_page + 1))
    else:
        pages = [1] if last_page == 1 else [1, last_page]

    comments: list[dict[str, Any]] = []
    seen_ids: set[int] = set()
    for page in pages:
        response = session.get(
            comments_url,
            headers=headers,
            params={"per_page": per_page, "page": page},
            timeout=30,
        )
        response.raise_for_status()
        for comment in response.json():
            comment_id = comment.get("id")
            if comment_id in seen_ids:
                continue
            seen_ids.add(comment_id)
            if clean_text(comment.get("body") or ""):
                comments.append(comment)
    return comments


def format_solution_comments(comments: list[dict[str, Any]]) -> str:
    blocks: list[str] = []
    for index, comment in enumerate(comments, start=1):
        header = (
            f"Comment {index}"
            f" | author: {comment.get('author', '')}"
            f" | association: {comment.get('author_association', '')}"
            f" | reactions: {comment.get('reactions', 0)}"
            f" | score: {comment.get('score', 0)}"
            f" | url: {comment.get('url', '')}"
        )
        blocks.append(f"{header}\n{comment.get('body', '')}")
    return "\n\n".join(blocks)


def normalize_github_issue(
    item: dict[str, Any],
    query: str,
    solution_comments: list[dict[str, Any]] | None = None,
    relevance_score: int = 0,
) -> dict[str, Any]:
    body = clean_text(item.get("body") or "")
    title = clean_text(item.get("title") or "")
    labels = [label.get("name", "") for label in item.get("labels", []) if isinstance(label, dict)]
    content_parts = [body]
    if solution_comments:
        content_parts.append("Selected solution comments:\n" + format_solution_comments(solution_comments))
    content = clean_text("\n\n".join(part for part in content_parts if part))
    return {
        "id": stable_id(item["html_url"], "gh_issue_"),
        "source": "github_issue",
        "source_type": "community_issue",
        "query": query,
        "url": item["html_url"],
        "repository": github_repo_name(item),
        "title": title,
        "content": content,
        "state": item.get("state", ""),
        "labels": labels,
        "comments": item.get("comments", 0),
        "selected_comments": solution_comments or [],
        "relevance_score": relevance_score,
        "score": item.get("score", 0),
        "created_at": item.get("created_at", ""),
        "updated_at": item.get("updated_at", ""),
        "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
    }


def collect_github(config: dict[str, Any], target_items: int, delay: float) -> list[dict[str, Any]]:
    gh_cfg = config["issues"]["github"]
    if not gh_cfg.get("enabled", True):
        return []

    token = os.environ.get(gh_cfg.get("token_env", "GITHUB_TOKEN"), "")
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "UnityDevAssistantCourseProject/1.0",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    session = requests.Session()
    max_pages = int(config["issues"].get("max_pages_per_query", 10))
    min_relevance_score = int(gh_cfg.get("min_relevance_score", 2))
    comment_fetch_per_page = int(gh_cfg.get("comment_fetch_per_page", 100))
    comment_pages = str(gh_cfg.get("comment_pages", "first_last"))
    solution_comment_limit = int(gh_cfg.get("solution_comment_limit", 6))

    for query in tqdm(gh_cfg["queries"], desc="GitHub issues"):
        page = 1
        while len(rows) < target_items and page <= max_pages:
            params = {
                "q": query,
                "sort": "comments",
                "order": "desc",
                "per_page": 100,
                "page": page,
            }
            response = session.get("https://api.github.com/search/issues", headers=headers, params=params, timeout=30)
            response.raise_for_status()
            items = response.json().get("items", [])
            if not items:
                break
            for item in items:
                if "pull_request" in item:
                    continue
                url = item.get("html_url", "")
                if not url or url in seen:
                    continue
                relevance_score = issue_relevance_score(item)
                if relevance_score < min_relevance_score:
                    continue
                seen.add(url)
                comments: list[dict[str, Any]] = []
                if item.get("comments", 0) > 0:
                    comments = fetch_github_comments(
                        session,
                        item.get("comments_url", ""),
                        headers,
                        int(item.get("comments", 0)),
                        comment_fetch_per_page,
                        comment_pages,
                    )
                    polite_sleep(delay)
                solution_comments = select_solution_comments(comments, solution_comment_limit)
                rows.append(normalize_github_issue(item, query, solution_comments, relevance_score))
                if len(rows) >= target_items:
                    break
            page += 1
            polite_sleep(delay)
    return rows


def fetch_stackexchange_answers(
    session: requests.Session,
    site: str,
    question_ids: list[int],
) -> dict[int, list[dict[str, Any]]]:
    if not question_ids:
        return {}
    ids = ";".join(str(question_id) for question_id in question_ids)
    response = session.get(
        f"https://api.stackexchange.com/2.3/questions/{ids}/answers",
        params={
            "order": "desc",
            "sort": "votes",
            "site": site,
            "filter": "withbody",
            "pagesize": 100,
        },
        timeout=30,
    )
    response.raise_for_status()
    grouped: dict[int, list[dict[str, Any]]] = {}
    for answer in response.json().get("items", []):
        grouped.setdefault(answer.get("question_id", 0), []).append(answer)
    for answers in grouped.values():
        answers.sort(key=lambda answer: (not answer.get("is_accepted", False), -int(answer.get("score", 0))))
    return grouped


def format_stackexchange_answers(answers: list[dict[str, Any]], limit: int = 3) -> str:
    blocks: list[str] = []
    for index, answer in enumerate(answers[:limit], start=1):
        owner = answer.get("owner") or {}
        header = (
            f"Answer {index}"
            f" | accepted: {answer.get('is_accepted', False)}"
            f" | score: {answer.get('score', 0)}"
            f" | author: {owner.get('display_name', '')}"
        )
        blocks.append(f"{header}\n{clean_text(answer.get('body', ''))}")
    return "\n\n".join(blocks)


def normalize_stackexchange_question(item: dict[str, Any], query: str, answers: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    title = clean_text(item.get("title", ""))
    body = clean_text(item.get("body", ""))
    content = body
    if answers:
        content = f"{body}\n\nSelected answers:\n{format_stackexchange_answers(answers)}"
    return {
        "id": stable_id(item["link"], "so_issue_"),
        "source": "stackoverflow",
        "source_type": "community_issue",
        "query": query,
        "url": item["link"],
        "title": title,
        "content": content,
        "tags": item.get("tags", []),
        "score": item.get("score", 0),
        "answer_count": item.get("answer_count", 0),
        "selected_answers": answers[:3] if answers else [],
        "is_answered": item.get("is_answered", False),
        "created_at": item.get("creation_date", 0),
        "updated_at": item.get("last_activity_date", 0),
        "fetched_at": dt.datetime.now(dt.UTC).isoformat(),
    }


def collect_stackexchange(config: dict[str, Any], target_items: int, delay: float) -> list[dict[str, Any]]:
    se_cfg = config["issues"]["stackexchange"]
    if not se_cfg.get("enabled", True):
        return []

    rows: list[dict[str, Any]] = []
    seen: set[str] = set()
    session = requests.Session()
    max_pages = int(config["issues"].get("max_pages_per_query", 10))

    for query in tqdm(se_cfg["queries"], desc="StackExchange issues"):
        page = 1
        while len(rows) < target_items and page <= max_pages:
            params = {
                "order": "desc",
                "sort": "votes",
                "site": se_cfg.get("site", "stackoverflow"),
                "tagged": se_cfg.get("tagged", "unity3d"),
                "q": query,
                "filter": "withbody",
                "pagesize": 100,
                "page": page,
            }
            response = session.get("https://api.stackexchange.com/2.3/search/advanced", params=params, timeout=30)
            response.raise_for_status()
            payload = response.json()
            items = payload.get("items", [])
            if not items:
                break
            answers_by_question = fetch_stackexchange_answers(
                session,
                se_cfg.get("site", "stackoverflow"),
                [item.get("question_id") for item in items if item.get("question_id")],
            )
            for item in items:
                url = item.get("link", "")
                if not url or url in seen:
                    continue
                seen.add(url)
                rows.append(normalize_stackexchange_question(item, query, answers_by_question.get(item.get("question_id"), [])))
                if len(rows) >= target_items:
                    break
            if not payload.get("has_more"):
                break
            page += 1
            polite_sleep(delay)
    return rows


def collect(config_path: str | Path) -> Path:
    config = load_config(config_path)
    output_root = resolve_output_root(config, config_path)
    out_path = output_root / "raw" / "issues" / "issues.jsonl"
    target_items = int(config["issues"].get("target_items", 220))
    delay = float(config["issues"].get("delay_seconds", 1.0))

    rows = collect_github(config, target_items, delay)
    if len(rows) < target_items:
        rows.extend(collect_stackexchange(config, target_items - len(rows), delay))

    deduped: list[dict[str, Any]] = []
    seen_urls: set[str] = set()
    for row in rows:
        if row["url"] in seen_urls:
            continue
        if len(f"{row.get('title', '')}\n{row.get('content', '')}") < 80:
            continue
        seen_urls.add(row["url"])
        deduped.append(row)
        if len(deduped) >= target_items:
            break

    write_jsonl(out_path, deduped)
    print(f"Wrote {len(deduped)} issue records to {out_path}")
    return out_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect high-frequency Unity GitHub and community issues.")
    parser.add_argument("--config", required=True, help="Path to KnowledgeCrawler config JSON.")
    args = parser.parse_args()
    collect(args.config)


if __name__ == "__main__":
    main()
