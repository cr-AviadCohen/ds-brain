---
description: Fully autonomous wiki lint — no approval gates, no clarifying questions. Designed for headless invocation via `claude -p` from `server/jobs/auto_lint.py`.
argument-hint: (no args)
---

Autonomously lint the wiki per `CLAUDE.md` § Operations.

**This command runs without a human in the loop.** It is invoked weekly
by `server/jobs/auto_lint.py` (the Ubuntu VM auto-lint daemon) inside a
freshly created bot branch named `auto-lint/<UTC-timestamp>-<short-sha>`.
The Python wrapper handles branching, push, PR creation, and auto-merge.
There is no one to answer questions. **Commit on completion. Do NOT push
or open a PR — the wrapper does that after inspecting the diff against
blast-radius caps.**

## Preconditions (fail fast if violated)

If any of these is false, log the reason and exit non-zero **without
modifying any file**:

- Current branch starts with `auto-lint/` (the wrapper's bot branch). If
  the branch is `unified` you are being invoked outside the daemon —
  refuse and exit non-zero.
- Working tree is clean.

## Workflow

1. **Deterministic checks (Step 1 of `/lint`).**

   ```bash
   cd tools && uv run python -m lint.run_all
   ```

   Parse the output. The Python lint reports frontmatter problems,
   orphans, stale links. For each finding apply the corresponding
   automatic fix where the fix is **unambiguous** (e.g. add a missing
   required frontmatter key, normalise a known-broken wikilink target).
   For ambiguous findings (e.g. orphan page that may need promotion or
   archival) — **do not edit**; append a bullet to `wiki/Log/pulse.md`
   under a `## Lint findings <YYYY-MM-DD>` section instead.

2. **LLM checks — inline, no subagents.**

   In headless mode subagent dispatch is forbidden (single `claude -p`
   process, single log stream). Run the five checks sequentially in this
   session:

   1. **Contradictions** — claim X on page A, claim ¬X on page B, no
      `## Tensions` block.
   2. **Stale claims** — page `last_updated` is old AND newer `raw/`
      notes supersede info.
   3. **Orphaned concepts** — recurring in `raw/` but no
      `wiki/Research/` or `wiki/Entities/*` page exists.
   4. **Missing cross-references** — entities that should link to each
      other but don't.
   5. **Data gaps** — areas where an external source would clarify.

   For each check, read `wiki/INDEX.md` + the relevant subset of pages,
   produce a numbered findings list with file paths and exact quotes.
   Aggregate the five lists.

3. **Decide silently which findings to act on.**

   **Autonomous fix-vs-flag rules:**
   - **High-confidence, unambiguous fix → apply.** Examples:
     - Missing required frontmatter key with an obvious default.
     - Wikilink target rename where the new name is unambiguous (only
       one page matches by token overlap).
     - Adding a missing `## Open questions` section to a wiki page that
       needs one.
     - Adding a missing bidirectional wikilink when both pages
       unambiguously reference each other in prose.
   - **Anything contested, semantic, or destructive → DO NOT edit.**
     Examples:
     - Contradictions between pages (claim X vs ¬X). Flag in pulse.md.
     - Stale claims (someone needs to decide if the new info supersedes
       the old).
     - Orphan promotion / archival decisions.
     - Renaming a page (changes wikilinks site-wide).
   - **When in doubt, flag — don't fix.** A human reviewing the PR can
     unflag and merge; a bad auto-fix is harder to undo.

4. **Execute — batch independent edits in single messages.**

   **Phase A — apply approved fixes.** In a SINGLE message, batch all
   `Edit` / `Write` calls for the unambiguous fixes. Independent files,
   parallel execution.

   **Phase B — flag the rest.** Append the unfixed findings to
   `wiki/Log/pulse.md` as:

   ```
   ## Lint findings YYYY-MM-DD
   ### Contradictions
   - [[Page A]] claims X, [[Page B]] claims ¬X — needs reconciliation.
   ### Stale claims
   - [[Page]] last_updated 2024-XX; raw/<…> from 2026 contradicts.
   ### Orphans
   - "<concept>" mentioned in N raw notes but no wiki page.
   ### Missing cross-references
   - [[A]] ↔ [[B]] should reference each other.
   ### Data gaps
   - <topic> — suggest external source: <description>.
   ```

   No findings in a category → omit the subheading.

   **Phase C — wiki-ops log.** Prepend to `wiki/Log/wiki-ops.md` under
   the `---` preamble:

   ```
   ## [YYYY-MM-DD] auto-lint | <N> issues found, <M> auto-fixed, <K> flagged
   - Deterministic: <count_det_findings> findings, <count_det_fixed> auto-fixed
   - LLM: <count_llm_findings> findings, <count_llm_fixed> auto-fixed
   - Flagged in pulse.md: <K>
   ```

   **Phase D — commit only (NO push, NO PR):**
   - Stage all touched files (including `wiki/Log/wiki-ops.md` and
     `wiki/Log/pulse.md`).
   - `git commit -m "auto-lint | <N> issues, <M> auto-fixed, <K> flagged"`.
   - **Do NOT `git push`.** **Do NOT open a PR.** The wrapper handles
     push + `gh pr create` + auto-merge after inspecting the diff
     against blast-radius caps.

   If no edits were made and no findings were flagged (clean run), do
   NOT write to `wiki/Log/wiki-ops.md`, do NOT commit. Exit 0 with the
   final-report line `auto-lint: clean`. The wrapper detects the empty
   diff and skips PR creation.

5. **Final report (to stdout, for the journal):**

   - One line per fix applied.
   - One line summarising flagged findings per category.
   - Local commit SHA (or `(no commit)` for a clean run).
   - Single line `auto-lint: ok` (fixes applied or findings flagged),
     `auto-lint: clean` (nothing to do), or
     `auto-lint: degraded — <reason>` (partial work; details inline).

## Hard rules

- **Never edit a `raw/` note's body.** The PreToolUse guard enforces
  this; if you hit it, back out and exit non-zero.
- **No clarifying questions.** Use the fix-vs-flag rules above.
- **No subagent dispatch.** Single `claude -p` process.
- **No `git push`.** The wrapper owns push + PR + merge.
- **Conservative bias.** When in doubt, flag in pulse.md rather than
  edit. The PR review is the safety net, but auto-merge happens when
  caps pass — better to leave a finding flagged than to auto-fix wrongly.
- Wikilinks only (`[[Name]]`) in any new content.
- Every newly-created wiki page must carry `wiki` in `tags` and
  `provenance: auto-lint` in frontmatter.
- The commit op token is `auto-lint` (not `lint`) so the audit trail
  distinguishes autonomous from human-driven runs.

## What this command is NOT

- It is not `/lint`. Use `/lint` interactively when a human is available
  to approve fixes and consider ambiguous findings.
- It does not promote orphans, archive stale pages, or resolve
  contradictions — those need human judgement.
