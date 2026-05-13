---
description: Two-pass removal of a topic (raw note, wiki page, or both) with reference cleanup; soft-deletes into 📦 Archive/ by default
argument-hint: <topic — file path, entity/concept name, or theme>
---

Remove **$ARGUMENTS** from the wiki per `CLAUDE.md` § Operations.

The topic could be a single `raw/` note, a single wiki page, or a
multi-page topic spanning both layers.

If editing a single page would suffice, **say so and stop** — removal is
the heavier hammer.

## PASS 1 — list, don't write

**Run discovery in parallel.** In a SINGLE message, batch the searches —
each is independent:
- `grep -rn "[[<topic>]]"` across `raw/` and `wiki/` for direct wikilinks.
- `grep -rn` for alias forms (`[[<topic>|...]]`, `[[<topic>#...]]`).
- `grep -rn` for `sources:` / `derived_from:` frontmatter pointers.
- `grep -n` against `wiki/INDEX.md` and `wiki/Log/wiki-ops.md` for
  mentions.
- `find` for sibling files that share the topic name.

Produce a single markdown report with these sections (totals at the top):

1. **Files to soft-delete (move to 📦 Archive/)** — exact paths.
2. **Files with stale wikilinks to fix.**
3. **`wiki/INDEX.md` entries** that reference the topic.
4. **`sources:` / `derived_from:` frontmatter entries** to clean.
5. **`wiki/Log/wiki-ops.md` mentions** (NOT edited — log is prepend-only).

**Do not write or move anything. Wait for approval before PASS 2.**

## PASS 2 — execute (only after approval)

1. For each file in PASS 1 step 1, soft-delete by `git mv` into the
   matching `📦 Archive/` sub-path (e.g.
   `wiki/Entities/Projects/Tipper.md` →
   `wiki/📦 Archive/Entities/Projects/Tipper.md`). Stamp three frontmatter
   fields on the archived note: `deleted: YYYY-MM-DD`,
   `deleted_reason: "..."`, `deleted_from: <original-relative-path>`.
2. **For each file with a stale wikilink, edit in parallel — batch every
   `Edit` call into a SINGLE message.** Independent files have no ordering
   dependency.
   - In a list → remove the bullet entirely.
   - In body prose → replace with link's display text in plain (no
     brackets); rewrite the sentence cleanly. Surface ambiguous cases.
3. Update `wiki/INDEX.md` to remove the archived entries.
4. Update `sources:` / `derived_from:` frontmatter — drop the entry; flag
   pages that now have zero sources.
5. Prepend to `wiki/Log/wiki-ops.md`:
   ```
   ## [YYYY-MM-DD] removal | <topic>
   - files archived: ...
   - files modified: ...
   - reason: <one paragraph in the user's words>
   ```
6. Run `cd tools && uv run python -m lint.run_all` and report. Fix
   anything dangling.
7. Stage all touched files, commit `removal | <topic>`, push to
   `origin/unified`.
8. Final report: total archived, total modified, lint status, commit SHA +
   push result.

## Hard rules

- `wiki/Log/wiki-ops.md` is prepend-only (newest on top). Past entries
  mentioning the removed topic stay — that's the historical record.
- Removals touching >5 files always go through PASS 1 review.
- PASS 1 discovery and PASS 2 reference-fixing must batch tool calls in a
  single message.
- Auto-commit + push is mandatory after PASS 2 lint passes.
