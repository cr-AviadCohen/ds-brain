---
description: Run a wiki health check — deterministic checks then LLM checks
argument-hint: (no args)
---

Lint the wiki per `CLAUDE.md` § Operations.

## Step 1 — deterministic checks

From the vault root:

```bash
cd tools && uv run python -m lint.run_all
```

The Python script fans frontmatter / orphans / stale-links across a thread
pool internally. Report what it found. Fix every issue (or flag what can't
be auto-fixed) before Step 2.

## Step 2 — LLM checks (parallel subagents)

Dispatch the five checks below as **separate subagents in a SINGLE
message** so they run concurrently (`superpowers:dispatching-parallel-agents`).
Each subagent reads `wiki/INDEX.md` plus the relevant subset of pages,
returns a numbered findings list with file paths and exact quotes, and does
**not** write.

1. **Contradictions** — claim X on page A, claim ¬X on page B, no
   `## Tensions` block.
2. **Stale claims** — page `last_updated` is old AND newer `raw/` notes
   supersede info.
3. **Orphaned concepts** — recurring in `raw/` but no `wiki/Research/` or
   `wiki/Entities/*` page exists.
4. **Missing cross-references** — entities that should link to each other
   but don't.
5. **Data gaps** — areas where an external source would clarify (suggest
   the search; don't run it).

Pick `subagent_type: Explore` for each — read-only audits. Brief each one
with: which check it owns, the wiki layout it should scan, the exact
report format. Collate the five reports into one numbered list. **Do NOT
make edits yet.**

## Step 3 — apply approved fixes

After review:
- Apply only the fixes approved. Independent file edits batch in a SINGLE
  message (parallel `Edit` calls).
- For >5 changes, batch into commits per category.
- Prepend `## [YYYY-MM-DD] lint | <summary>` to `wiki/Log/wiki-ops.md` with
  counts of issues found and fixed.
- Stage all touched files (including `wiki/Log/wiki-ops.md`), commit
  `lint | <summary>`, push to `origin/unified`.

If no fixes were applied (clean run), do not write to `wiki/Log/wiki-ops.md`
and do not commit. Just report the clean status.
