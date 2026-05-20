---
title: Log — Folder Guide
type: readme
created: 2026-05-11
updated: 2026-05-11
tags: [readme, folder-guide]
---

# Log/

Two files, never split into per-day pages. (`INDEX.md` lives at the vault
root `wiki/INDEX.md`, not here — it's the entry point for structural
navigation, not an operational log.)

| File | Purpose | Update cadence | Append direction |
| --- | --- | --- | --- |
| `wiki-ops.md` | Audit trail of operations | Every `/ingest`, `/auto-ingest`, `/query` (filed), `/lint`, `/auto-lint`, `/remove` | Prepend below the `---` preamble separator |
| `pulse.md` | One-line-per-day operational notes (VM health, cron status, anomalies) | Daily cron tick | Append at bottom |

### `wiki-ops.md` entry shape

```
## [YYYY-MM-DD] <op> | <subject>
- wiki/<path>.md (new|updated|archived)
Files moved:
- INBOX/<old> → raw/<tab>/<new>
```
