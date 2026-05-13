"""Stale-link check: wikilinks pointing to a target that doesn't exist as a .md stem.

Wikilinks inside fenced code blocks (``` or ~~~) AND inline-code spans
(single or double backticks) are ignored — those are template/example
placeholders, not real references. This matters for log entries that
quote literal `[[name]]` syntax when documenting wikilink changes.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
FENCE_RE = re.compile(r"^(\s*)(```|~~~)", re.MULTILINE)
INLINE_CODE_RE = re.compile(r"(`+)(?!`)(.+?)(?<!`)\1(?!`)")


@dataclass(frozen=True)
class StaleLink:
    source: Path
    target: str


def _strip_fenced_blocks(text: str) -> str:
    """Replace lines inside ``` or ~~~ fences with blank lines.

    Preserves line numbers so reported positions remain meaningful (not
    currently used, but cheap insurance). A fence line opens; the next
    matching fence (or EOF) closes.
    """
    lines = text.split("\n")
    out: list[str] = []
    in_fence = False
    fence_marker: str | None = None
    for line in lines:
        stripped = line.lstrip()
        if not in_fence:
            if stripped.startswith("```") or stripped.startswith("~~~"):
                in_fence = True
                fence_marker = stripped[:3]
                out.append("")
                continue
            out.append(line)
        else:
            if stripped.startswith(fence_marker or "```"):
                in_fence = False
                fence_marker = None
                out.append("")
                continue
            out.append("")
    return "\n".join(out)


def _strip_inline_code(text: str) -> str:
    """Replace inline-code spans with same-length spaces.

    Preserves line numbering so reported positions remain meaningful.
    Runs after fence-stripping so fenced contents are already blanked.
    """
    return INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), text)


def find_stale_links(root: Path) -> list[StaleLink]:
    stems = {p.stem for p in root.rglob("*.md")}
    stale: list[StaleLink] = []
    for p in root.rglob("*.md"):
        if "📦 Archive" in p.relative_to(root).parts:
            continue
        text = _strip_inline_code(_strip_fenced_blocks(p.read_text(encoding="utf-8")))
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if target not in stems:
                stale.append(StaleLink(p, target))
    return stale
