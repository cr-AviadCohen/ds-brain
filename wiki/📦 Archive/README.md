---
title: 📦 Archive — Folder Guide
type: readme
created: 2026-05-05
updated: 2026-05-11
tags: [readme, folder-guide, archive]
---

# 📦 Archive/

Soft-deleted wiki notes. Populated by `/remove <path>` (default mode).

## Conventions

- Mirrors the original path: a note deleted from `Projects/AIDRA.md` lands at `📦 Archive/Projects/AIDRA.md`.
- Archived notes carry three extra frontmatter fields:
  ```yaml
  deleted: YYYY-MM-DD
  deleted_reason: "<rationale>"
  deleted_from: <original-relative-path>
  ```
- Archived notes are excluded from `/lint-wiki` and from `INDEX.md`.
- Use `git log --diff-filter=R --follow "📦 Archive/<path>"` to trace the original location.

## Restoring

```bash
git mv "📦 Archive/<path>" "<path>"
# strip deleted* frontmatter fields
# re-add INDEX.md entry
```

Then append `DELETE-RESTORE | <path> | <utc> |` to `Log/wiki-ops.md`.
