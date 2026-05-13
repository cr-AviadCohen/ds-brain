---
title: INBOX — Folder Guide
type: readme
created: 2026-05-11
updated: 2026-05-11
tags: [readme, folder-guide]
---

# INBOX/

Queue for newly-added external sources (clipped articles, transcripts dropped
by hand, PDFs, slack exports) awaiting ingest.

- INBOX/ sits **outside** `raw/`. Claude reads files here, may add summary
  frontmatter, but never edits body content. The PreToolUse guard
  (`scripts/hooks/guard_immutable.py`) enforces this.
- `/ingest` moves the source out of INBOX/ into the agreed `raw/<tab>/`
  destination using `git mv` so history is preserved.
- The SessionStart hook (`.claude/hooks/inbox-check.sh`) auto-injects a
  reminder when this folder has unprocessed files.
