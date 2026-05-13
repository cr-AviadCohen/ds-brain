"""Run all wiki lint checks with thread-pool fan-out."""
from __future__ import annotations

import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from rich.console import Console

from lint.check_frontmatter import find_violations
from lint.check_orphans import find_orphans
from lint.check_stale_links import find_stale_links


def main() -> int:
    repo_root = Path(__file__).resolve().parents[2]
    wiki = repo_root / "wiki"
    console = Console()

    with ThreadPoolExecutor(max_workers=3) as pool:
        f_fronts = pool.submit(find_violations, wiki)
        f_orphs = pool.submit(find_orphans, wiki)
        f_stale = pool.submit(find_stale_links, wiki)

    fronts = f_fronts.result()
    orphs = f_orphs.result()
    stale = f_stale.result()

    console.rule("frontmatter")
    for v in fronts:
        console.print(f"  {v.path.relative_to(repo_root)} — {v.message}")
    console.rule("orphans")
    for p in orphs:
        console.print(f"  {p.relative_to(repo_root)}")
    console.rule("stale links")
    for s in stale:
        console.print(f"  {s.source.relative_to(repo_root)} → [[{s.target}]]")

    total = len(fronts) + len(orphs) + len(stale)
    console.rule()
    console.print(
        f"frontmatter: {len(fronts)}  orphans: {len(orphs)}  stale: {len(stale)}  total: {total}"
    )
    return 0 if total == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
