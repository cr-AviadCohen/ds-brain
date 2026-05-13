---
description: Ingest a source from INBOX/ (or any raw/ note) into the wiki layer
argument-hint: <path-to-source-or-empty-to-pick-from-INBOX>
---

Ingest `$ARGUMENTS` into the wiki per `CLAUDE.md` § Operations.

If `$ARGUMENTS` is empty, list what's currently in `INBOX/` and ask which file(s)
to ingest.

## Workflow

1. **Read the source fully.** No skimming. For `.docx` / `.xlsx`, first run
   `python3 tools/convert/docx_to_md.py <path>` (or `xlsx_to_md.py`) to
   produce a Markdown sidecar in the same directory; ingest both.

2. **Stop and report key takeaways.** Before writing or moving anything:
   - Summarise what the source actually says.
   - Propose a destination tab under `raw/<tab>/` for the file(s) (e.g.
     transcript → `raw/meetings/`, project deck → `raw/projects/Project -
     <name>/`).
   - List the People / Projects / Systems / Decisions / Ideas / Research
     pages you plan to touch.
   - Flag any contradictions you spotted with existing wiki pages.
   - Ask clarifying questions if intent is ambiguous.

   **Wait for go-ahead before continuing.**

3. **After approval, execute — parallelise independent work.**

   **Phase A — discovery (parallel reads).** In a SINGLE message, batch
   `Read` calls for every existing target page. Files are independent.

   **Phase B — page work (parallel writes).** Each Entity / Decision / Idea
   / Research / Source page is an independent file. In a SINGLE message,
   batch the `Edit` / `Write` calls:
   - For each Person/Project/System: append to `## Mentions` if the page
     exists, else create per the folder's README template.
   - For each Decision impacted: add to `## Decisions` on the related
     Project page.
   - For external sources: write `wiki/Sources/<slug>.md`.
   - For meetings: create `wiki/Meetings/YYYY-MM-DD — <topic>.md`.

   Use `superpowers:dispatching-parallel-agents` when a single page needs
   heavy net-new prose.

   **Phase C — shared-file updates (sequential):**
   - Update `wiki/INDEX.md` (new pages + revised one-line summaries).
   - **Move source file(s) out of `INBOX/` into the agreed `raw/<tab>/`
     destination using `git mv`.** Update `sources:` frontmatter on every
     wiki page just written to reference the new path.
   - Prepend to `wiki/Log/wiki-ops.md` (newest on top, below the `---`
     preamble separator):
     ```
     ## [YYYY-MM-DD] ingest | <source title>
     - wiki/Sources/<slug>.md (new)
     - wiki/Entities/People/<name>.md (updated)
     - wiki/Entities/Projects/<name>.md (updated)
     Files moved:
     - INBOX/<old> → raw/<tab>/<new>
     ```

   **Phase D — commit + push:** Stage all touched files (including
   `wiki/Log/wiki-ops.md` and the moved source), commit
   `ingest | <source title>`, `git push` to `origin/unified`.

4. **Final report:** pages created / modified, files moved, commit SHA +
   push result, anything flagged for human review.

## Hard rules

- Never edit a user-authored `raw/` note's body.
- Wikilinks only (`[[Name]]`).
- Every wiki page must include `wiki` in its `tags` array.
- Phase A and Phase B must batch tool calls in a single message.
- Auto-commit + push is mandatory. `wiki/Log/wiki-ops.md` must always be in
  the commit.
