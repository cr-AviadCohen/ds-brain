---
description: Fully autonomous ingest of an INBOX file — no approval gates, no clarifying questions. Designed for headless invocation via `claude -p` from systemd/launchd.
argument-hint: <path-to-source-file-in-INBOX-or-raw>
---

Autonomously ingest `$ARGUMENTS` into the wiki per `CLAUDE.md` § Operations.

**This command runs without a human in the loop.** It is invoked by
`scripts/systemd/inbox-ingest.sh` (Ubuntu VM) or
`scripts/cron/inbox-ingest.sh` (macOS) after `git pull` lands new files in
`INBOX/`. There is no one to answer questions. Proceed straight through all
phases and commit + push on completion.

## Preconditions (fail fast if violated)

If any of these is false, log the reason and exit non-zero **without
modifying any file**:

- `$ARGUMENTS` is non-empty and points to a real file under `INBOX/` or
  `raw/`.
- Current branch is `unified`.
- Working tree is clean apart from `$ARGUMENTS` itself (an untracked or
  newly-pulled file is expected and OK; unrelated dirty files are not).
- The file is not `INBOX/README.md` and not a dotfile.

## Workflow

1. **Read the source fully.** No skimming. For `.docx` / `.xlsx`, first run
   `python3 tools/convert/docx_to_md.py <path>` (or `xlsx_to_md.py`) to
   produce a Markdown sidecar in the same directory; ingest both.

2. **Decide silently.** Do not stop to report or ask. Resolve every
   decision using the rules below; if any rule cannot be applied, route the
   file to `wiki/Sources/` with a `## Open questions` block flagging the
   ambiguity for the next human pass — never block the run.

   **Autonomous tie-break rules:**
   - **Destination tab.** Transcript / meeting notes → `raw/meetings/`.
     Project deck / design doc → `raw/projects/Project - <name>/` (use the
     existing project folder whose name has highest token overlap with the
     filename or document title; if no project page has >50% overlap, fall
     back to `raw/data_science_drive/` and flag in Open questions).
     External brief / vendor one-pager → leave in `INBOX/` and write a
     `wiki/Sources/<slug>.md` only (don't auto-classify into `raw/`).
     People-only notes → `raw/people/` is **immutable to Claude**; never
     create new files there. Capture the people via wiki entity pages
     instead.
   - **People / Org / Project / System / Concept extraction.** Any
     proper-noun mentioned ≥2 times or appearing in a heading becomes a
     wiki entity touch (append to `## Mentions` if the page exists; create
     a minimal stub per the folder's README if not). Single passing
     mentions do not earn a page; list them in the source's `##
     Open questions` instead.
   - **Decisions vs Ideas.** A statement framed as "we will / we decided /
     adopted / rejected" → `wiki/Decisions/`. A statement framed as "we
     should / could / what if / hypothesis" → `wiki/Ideas/`.
   - **Synthesis-worthy?** If the source restates known wiki content with
     no new claims, do not create a `wiki/Syntheses/` page — only update
     `## Mentions` on existing entity pages.
   - **Contradictions with existing wiki pages.** Do NOT overwrite. Append
     a `## Open questions` bullet on the affected wiki page citing both
     the existing claim and the new one with their sources, and leave the
     existing claim in place.

3. **Execute — parallelise independent work.**

   **Phase A — discovery (parallel reads).** In a SINGLE message, batch
   `Read` calls for every existing target page (entity pages, related
   project page, any same-day meeting page). Files are independent.

   **Phase B — page work (parallel writes).** Each Entity / Decision /
   Idea / Research / Source page is an independent file. In a SINGLE
   message, batch the `Edit` / `Write` calls:
   - For each Person / Project / System / Org / Concept: append to
     `## Mentions` if the page exists, else create per the folder's
     README template. Never touch `raw/people/` bodies.
   - For each Decision: write `wiki/Decisions/YYYY-MM-DD — <slug>.md` and
     add a bullet to `## Decisions` on the related Project page.
   - For each Idea: write `wiki/Ideas/<slug>.md`.
   - For external sources: write `wiki/Sources/<slug>.md`.
   - For meetings: create `wiki/Meetings/YYYY-MM-DD — <topic>.md`.

   Do NOT spawn subagents in headless mode — keep the work in this single
   `claude -p` invocation so failures are captured in one log stream.

   **Phase C — shared-file updates (sequential):**
   - Update `wiki/INDEX.md` (new pages + revised one-line summaries).
   - **Move source file(s) out of `INBOX/` into the agreed `raw/<tab>/`
     destination using `git mv`.** Update `sources:` frontmatter on every
     wiki page just written to reference the new path.
   - Prepend to `wiki/Log/wiki-ops.md` (newest on top, below the `---`
     preamble separator):

     ```
     ## [YYYY-MM-DD] auto-ingest | <source title>
     - wiki/Sources/<slug>.md (new)
     - wiki/Entities/People/<name>.md (updated)
     - wiki/Entities/Projects/<name>.md (updated)
     Files moved:
     - INBOX/<old> → raw/<tab>/<new>
     Open questions logged: <count>
     ```

   **Phase D — commit + push:** Stage all touched files (including
   `wiki/Log/wiki-ops.md` and the moved source), commit
   `auto-ingest | <source title>`, `git push` to `origin/unified`. If push
   is rejected because remote moved, run `git pull --ff-only origin
   unified` once and retry the push. If the retry also fails, exit
   non-zero — leave the local commit in place; the next 5-min pull cycle
   plus the inbox-ingest backstop will reconcile.

4. **Final report (to stdout, for the journal):**
   - One line per wiki page created / modified.
   - One line per file moved (old → new).
   - Commit SHA and push result.
   - Count of `## Open questions` bullets added across all touched pages.
   - Single line `auto-ingest: ok` or `auto-ingest: degraded — <reason>`.

   `degraded` is fine — it means the file was filed, but a human should
   look at the Open questions on the next session. `degraded` is **not**
   an error; exit 0. Only exit non-zero on preconditions failure, parse
   failure, push retry failure, or any tool error.

## Hard rules

- **Never edit a `raw/` note's body.** The PreToolUse guard
  (`scripts/hooks/guard_immutable.py`) enforces this; if you hit it, the
  ingest is wrong — back out the touched file from the staging set and
  exit non-zero rather than committing partial state.
- **No clarifying questions.** There is no one to answer. Use the
  autonomous tie-break rules and the Open-questions block as the escape
  valve.
- **No subagent dispatch.** Single `claude -p` process, single log
  stream.
- Wikilinks only (`[[Name]]`).
- Every wiki page must include `wiki` in its `tags` array.
- Phase A and Phase B must batch tool calls in a single message.
- Auto-commit + push is mandatory. `wiki/Log/wiki-ops.md` must always be
  in the commit. The commit op token is `auto-ingest` (not `ingest`) so
  the audit trail distinguishes human-driven from autonomous runs.
- If the run cannot complete, **leave the source file in `INBOX/`** so
  the next path-trigger fires again (or so a human can pick it up).
  Never delete the source on failure.

## What this command is NOT

- It is not `/ingest`. Use `/ingest` interactively when a human is
  available to approve destination + decisions.
- It does not bulk-process the whole INBOX. The caller
  (`scripts/systemd/inbox-ingest.sh`) iterates one file at a time and
  invokes this command per file, so each commit corresponds to one
  source.
