"""Orphan check: any wiki page with zero inbound wikilinks from another wiki page."""
from __future__ import annotations

import re
from pathlib import Path

LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")


def _wiki_md_files(root: Path) -> list[Path]:
    return [
        p
        for p in root.rglob("*.md")
        if "📦 Archive" not in p.relative_to(root).parts
        and p.name != "README.md"
    ]


def find_orphans(root: Path) -> list[Path]:
    files = _wiki_md_files(root)
    by_stem = {p.stem: p for p in files}
    referenced: set[str] = set()
    for p in files:
        for m in LINK_RE.finditer(p.read_text(encoding="utf-8")):
            referenced.add(m.group(1).strip())
    return sorted(p for stem, p in by_stem.items() if stem not in referenced)
