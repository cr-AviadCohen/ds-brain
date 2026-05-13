"""Frontmatter check: every wiki/ page must have title, type, tags incl. 'wiki', last_updated."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import yaml

REQUIRED_KEYS = ("title", "type", "tags", "last_updated")


@dataclass(frozen=True)
class Violation:
    path: Path
    message: str


def _parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    block = text[3:end]
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def _is_archived(path: Path, root: Path) -> bool:
    rel = path.relative_to(root)
    return "📦 Archive" in rel.parts


def find_violations(root: Path) -> list[Violation]:
    violations: list[Violation] = []
    for md in root.rglob("*.md"):
        if _is_archived(md, root):
            continue
        if md.name == "README.md":
            continue  # folder guides have their own schema
        text = md.read_text(encoding="utf-8")
        fm = _parse_frontmatter(text)
        if fm is None:
            violations.append(Violation(md, "missing frontmatter"))
            continue
        for key in REQUIRED_KEYS:
            if key not in fm:
                violations.append(Violation(md, f"missing key: {key}"))
        tags = fm.get("tags", [])
        if not isinstance(tags, list) or "wiki" not in tags:
            violations.append(Violation(md, "missing wiki tag"))
    return violations
