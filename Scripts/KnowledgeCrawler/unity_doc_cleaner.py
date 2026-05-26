from __future__ import annotations

import re
from pathlib import PurePosixPath
from urllib.parse import urljoin
from urllib.parse import urlparse

from bs4 import BeautifulSoup

from common import clean_text


DROP_SELECTORS = [
    "script",
    "style",
    "noscript",
    "nav",
    "header",
    "footer",
    ".header-wrapper",
    ".toolbar",
    ".sidebar-wrap",
    ".suggest",
    ".suggest-wrap",
    ".scrollToFeedback",
    ".footer-wrapper",
    ".feedback",
    ".cookie",
    ".nextprev",
    ".otherversionscontent",
    ".lang-list",
    ".mobileLogo",
    "#onetrust-banner-sdk",
    "#ot-sdk-btn-container",
]

CONTENT_SELECTORS = [
    "#content-wrap .content-block > .content",
    "#content-wrap .content-block .content",
    "#content-wrap",
    "main",
    "article",
    "#content",
    ".content",
    "body",
]

DROP_LINE_EXACT = {
    "Leave feedback",
    "Suggest a change",
    "Success!",
    "Submission failed",
    "Close",
    "Your name",
    "Your email",
    "Suggestion",
    "*",
    "Submit suggestion",
    "Cancel",
    "Tutorials",
    "Community Answers",
    "Knowledge Base",
    "Forums",
    "Asset Store",
    "Terms of use",
    "Legal",
    "Privacy Policy",
    "Cookies",
    "Do Not Sell or Share My Personal Information",
    "Your Privacy Choices (Cookie Settings)",
}

DROP_LINE_PREFIXES = (
    "Thank you for helping us improve the quality of Unity Documentation.",
    "Although we cannot accept all submissions",
    "For some reason your suggested change could not be submitted.",
    "Is something described here not working as you expect it to?",
    "Please check with the Issue Tracker",
    "Copyright ©",
    "Built from job ID",
    "Built on:",
)

SECTION_LABELS = {
    "Description",
    "Declaration",
    "Parameters",
    "Returns",
    "Examples",
    "Additional resources",
    "Properties",
    "Public Methods",
    "Static Methods",
    "Inherited Members",
}


def title_from_soup(url: str, soup: BeautifulSoup) -> str:
    title_node = soup.find("h1") or soup.find("title")
    if title_node:
        title = clean_text(title_node.get_text(" "))
        title = re.sub(r"^Unity\s*-\s*Scripting API:\s*", "", title)
        return title.strip()
    return url


def content_node(soup: BeautifulSoup):
    for selector in CONTENT_SELECTORS:
        node = soup.select_one(selector)
        if node:
            return node
    return soup


def image_label(src: str, alt: str) -> str:
    if alt:
        return alt
    name = PurePosixPath(urlparse(src).path).name
    return name or "Unity documentation image"


def replace_images_with_markdown(content, base_url: str) -> None:
    for img in content.find_all("img"):
        src = img.get("src", "").strip()
        if not src:
            img.decompose()
            continue
        if any(token in src for token in ["StaticFiles", "favicons", "icons/"]):
            img.decompose()
            continue
        absolute = urljoin(base_url, src)
        alt = clean_text(img.get("alt", "") or img.get("title", ""))
        label = image_label(absolute, alt)
        img.replace_with(f"\n![{label}]({absolute})\n")


def clean_unity_lines(text: str) -> str:
    lines = [line.strip() for line in text.splitlines()]
    kept: list[str] = []
    skip_known_issue_tail = False
    for line in lines:
        if not line:
            continue
        if line in DROP_LINE_EXACT:
            continue
        if any(line.startswith(prefix) for prefix in DROP_LINE_PREFIXES):
            skip_known_issue_tail = True
            continue
        if skip_known_issue_tail:
            if line.startswith("Copyright ©") or line in DROP_LINE_EXACT:
                continue
            if line in {"Known Issue", "issuetracker.unity3d.com", "."}:
                continue
            skip_known_issue_tail = False
        kept.append(line)
    return clean_text("\n".join(kept))


def extract_page(url: str, html: str, preserve_image_refs: bool = True) -> tuple[str, str, list[str]]:
    soup = BeautifulSoup(html, "html.parser")
    for selector in DROP_SELECTORS:
        for node in soup.select(selector):
            node.decompose()

    title = title_from_soup(url, soup)
    content = content_node(soup)

    if preserve_image_refs:
        replace_images_with_markdown(content, url)

    for code in content.find_all("pre"):
        code_text = clean_text(code.get_text("\n"))
        if code_text:
            code.string = f"\n```csharp\n{code_text}\n```\n"

    headings = [clean_text(h.get_text(" ")) for h in content.find_all(["h1", "h2", "h3"])]
    headings = [heading for heading in headings if heading and heading not in DROP_LINE_EXACT]
    body = clean_unity_lines(content.get_text("\n"))
    return title, body, headings


def effective_text(content: str, title: str = "") -> str:
    title_norm = clean_text(title).replace(" ", "")
    meaningful: list[str] = []
    for line in content.splitlines():
        line = line.strip()
        if not line or line in SECTION_LABELS:
            continue
        if title_norm and line.replace(" ", "") == title_norm:
            continue
        meaningful.append(line)
    return clean_text("\n".join(meaningful))


def is_low_value_page(url: str, title: str, content: str, min_effective_chars: int = 140) -> bool:
    parsed = urlparse(url)
    if "/ScriptReference/" not in parsed.path:
        return len(effective_text(content, title)) < min_effective_chars

    meaningful = effective_text(content, title)
    if len(meaningful) >= min_effective_chars:
        return False

    has_api_signal = any(label in content for label in ["Declaration", "Parameters", "Returns", "Examples"])
    has_code = "```" in content or "public " in content or "static " in content
    return not (has_api_signal or has_code)
