---
name: ds-brain
description: Use this skill whenever the user wants to query, search, or read the Data Science team's shared second brain (the Obsidian-style wiki at the ds-brain repo), OR wants to add information into it — notes, meeting summaries, insights, raw materials, decisions, references, links, action items, or follow-ups. Triggers on phrases like "search the brain", "what do we know about", "summarize what the brain says", "save this to the brain", "push this to the brain", "add to the brain", "store in the DS brain", "drop this in the inbox", "remember this for the team", "what's connected to this project/person", "find previous decisions about", and similar. Also triggers on any request to retrieve team context for ongoing work, traverse links between notes, or stash conversation insights so the team can find them later. Both reads and writes go through the GitHub MCP (`@modelcontextprotocol/server-github`) against `cybereason-labs/ds-brain` on branch `unified`. Reads use `search_code` and `get_file_contents`; writes use `create_or_update_file` into the repo's INBOX/ folder. No local clone needed; no Obsidian dependency. Each team member uses their own fine-grained Personal Access Token so commits carry their own GitHub identity. MCP-required — if the GitHub MCP is missing, walks the user through one-time install rather than silently falling back to filesystem or local git. Never touches wiki/, raw/, .claude/, scripts/, or any other structural file directly — the central server-side ingest pipeline owns all knowledge restructuring. Also triggers on first-time setup intents ("install git mcp", "install github mcp", "set up the brain", "onboard me to the DS brain", "how do I configure this", "the brain isn't working") — in those cases, walk the user through references/setup.md.
---

# Data Science Brain

## What this skill is

The Data Science team maintains a shared **second brain** — an Obsidian-compatible Markdown vault following Andrej Karpathy's wiki-LLM pattern. It lives in the GitHub repo `cybereason-labs/ds-brain` on branch `unified`. It is a single source of truth for: who is on the team, what projects are active, what we decided, what we researched, who we work with, what we learned in meetings, and what raw material backs all of that up.

The brain is **multi-author** and has a strict separation of concerns:

| Layer | What lives there | Who writes |
|-------|------------------|-----------|
| `raw/` | Source-of-truth artifacts (decks, transcripts, docs) | Immutable. Hooks block edits. |
| `wiki/` | Synthesized notes, entities, decisions, research | A central server-side Claude process |
| `INBOX/` | Unprocessed material waiting to be ingested | **This is the only layer this skill writes to.** |
| Schema (`CLAUDE.md`, `.claude/`, `scripts/`, `tools/`) | Conventions, hooks, commands, lint | Maintainers only |

The central server-side process (`/ingest`, `/lint`, etc., run from a maintainer's machine) is responsible for pulling new INBOX files, transforming them into wiki notes, resolving links, and maintaining structure. Local team members never run that pipeline — they only feed material into INBOX and read the resulting wiki.

This skill enables exactly two operations: **read** the brain, and **drop material into INBOX**. Everything else is forbidden.

## When this skill should fire

Default to firing whenever the user mentions, references, or asks about:

- "the brain", "DS brain", "data science brain", "team brain", "our wiki", "the vault"
- A team member's name, a project name, a customer/vendor name, or a research topic that the user clearly wants context on rather than a generic answer
- Storing, saving, capturing, or remembering something for later that has team-knowledge value
- A meeting they just had, a decision they just made, an idea they want to file
- Searching, traversing, or "what's connected to" questions about people / projects / decisions
- Anything where the natural follow-up is "should I look in the wiki?" — the answer is yes, look in the wiki

If you're under 50% sure the user wants the brain, ask one short clarifying question before reading or writing. If you're over 50% sure, just do it.

## Tools you will use

This skill is **GitHub-MCP-only**. No filesystem, no Bash, no Obsidian dependency. Both reads and writes go through the same MCP. If the GitHub MCP is missing, the skill cannot operate — guide the user through installation first, then resume.

### Required MCP

| MCP | Used for | Without it |
|-----|----------|-----------|
| `github` (`@modelcontextprotocol/server-github`) | Search, read, and write notes on the remote repo via GitHub API | Skill halts |

Check availability by inspecting the tool list for `mcp__github__*` tools. If that family is absent in the current session, the skill is blocked.

### Gate before operating

Before answering a read request or starting a write request, confirm the GitHub MCP is connected.

- **No `github` MCP:** stop. Tell the user: "The GitHub MCP isn't connected in this session, so I can't reach the brain. I'll walk you through the one-time install (about 5 minutes) — ready?" If yes, read `references/setup.md` and execute the steps with the user (you run the `claude mcp add` commands; the user generates **their own** fine-grained Personal Access Token — never share a team-wide one).
- **User declines install:** acknowledge, do not proceed. The skill does not silently fall back. Tell them the skill needs the MCP and they can return when ready.

### GitHub MCP — reads

Every read goes through the GitHub MCP against `owner=cybereason-labs`, `repo=ds-brain`, `ref=unified`.

Primary tools:

- `mcp__github__search_code` — keyword / phrase / symbol search across the repo. Use the `q` query syntax with `repo:cybereason-labs/ds-brain` to scope. Add `path:wiki/` to bias toward synthesized notes, or `path:raw/` only when the user explicitly asked for raw evidence. Examples:
  - `q: "Tipper" repo:cybereason-labs/ds-brain path:wiki/`
  - `q: "LoRA fine-tune" repo:cybereason-labs/ds-brain path:wiki/Entities/Projects/`
  - `q: filename:Tipper.md repo:cybereason-labs/ds-brain`
- `mcp__github__get_file_contents` — read a specific file or list a directory. For directory listing, pass `path` pointing at the folder (e.g., `wiki/Entities/People`) and the API returns the directory tree. For file reads, pass the full path (e.g., `wiki/Entities/Projects/Tipper.md`). Always pass `ref: unified`.
- `mcp__github__list_commits` — only when the user explicitly asks for history of a note.

Wikilink traversal: GitHub search does not resolve `[[Other Note]]` for you. Extract the link target from the note text, map it to a likely path (`wiki/Entities/People/<Name>.md`, `wiki/Entities/Projects/<Name>.md`, etc.), and fetch with `get_file_contents`. If the first guess 404s, fall back to `search_code` with `filename:<Name>.md`.

Note: GitHub's code search has a ~1-minute index lag for very recent commits and ignores files >384 KB. For freshly written content or large transcripts, fall back to a directory listing + targeted `get_file_contents`.

### GitHub MCP — writes

Writes target `cybereason-labs/ds-brain` on branch `unified` (confirm if the user says otherwise).

Preferred tool: `mcp__github__create_or_update_file` — one call creates the file and the commit in one shot.

Required arguments:
- `owner`: `cybereason-labs`
- `repo`: `ds-brain`
- `branch`: `unified`
- `path`: `INBOX/YYYY-MM-DD-<kebab-slug>.md`
- `content`: the full Markdown body (frontmatter + content)
- `message`: `inbox | <subject>` — matches the brain's existing commit-message convention
- `sha`: omit when creating a new file; required only when updating an existing one

Multiple-file writes (rare for this skill): use `mcp__github__push_files` to batch into a single commit.

**No `git push`, no local clone churn.** Every write is an atomic API commit. The skill's commits will appear on GitHub authored by the PAT owner, which means each team member's commits carry their own GitHub identity — preserving audit trail.

Use **fewest-side-effects** behavior on writes: one file per commit, scoped to `INBOX/`. Don't touch other paths. Don't open PRs unless the user explicitly asks for review-gated INBOX. Don't force-update. Confirm the API returned 200/201 and surface the resulting commit SHA before telling the user "done."

### Setup walkthrough on demand

If the user explicitly asks ("install github mcp", "install git mcp", "set up the brain", "how do I configure this"), read `references/setup.md` and walk them through it without waiting for an operation to fail.

## Brain structure quick reference

The wiki layer is organized like this — use it to plan a query and to map wikilinks to file paths:

```
wiki/
├── INDEX.md                      ← structural map of every page
├── Entities/
│   ├── People/                   ← teammates, stakeholders, vendors
│   ├── Teams/                    ← sub-units (DS Team, SLR, Spider Labs, …)
│   ├── Organizations/            ← companies, customers, standards bodies
│   ├── Projects/                 ← active DS projects
│   ├── Systems/                  ← products / components we integrate with
│   ├── Concepts/                 ← atomic ideas, techniques (LoRA, Sigma, …)
│   └── Locations/                ← geo / office locations
├── Meetings/                     ← distilled meeting outcomes
├── Decisions/                    ← DS-leadership ADRs
├── Ideas/                        ← hypotheses + evidence
├── Research/                     ← deeper ML/AI/security research notes
├── Sources/                      ← one-pagers for external sources
├── Syntheses/                    ← curated LLM answers worth keeping
├── Connections/                  ← cross-domain patterns
├── 🔥 Hot Notes/                 ← active focus (≤7 entries)
├── 🗺️ Maps/                      ← .canvas / .base visual maps
├── 📦 Archive/                   ← soft-deleted notes
├── Memories/                     ← durable team know-how
└── Log/
    ├── wiki-ops.md               ← audit trail (prepend, newest-on-top)
    └── pulse.md                  ← daily ops notes
```

Wikilinks look like `[[Inbar Dekel]]` or `[[Tipper]]`. To follow a wikilink, map `[[<Name>]]` to the most likely path under `wiki/Entities/<Folder>/<Name>.md` and fetch via `get_file_contents`; if it 404s, run `search_code` with `filename:<Name>.md repo:cybereason-labs/ds-brain`.

Frontmatter on every wiki page carries `wiki` in the `tags` array as the layer marker.

## Query workflow

When the user asks a question that wants brain context:

1. **Decide the entry point.** If the user named a person/project/concept, jump straight to the likely path under `wiki/Entities/.../<Name>.md` with `get_file_contents`. If they asked an open question or "what do we know about X," start with `search_code`. If they want structural navigation ("what's in research"), fetch `wiki/INDEX.md`.

2. **Search.** Use `mcp__github__search_code` with `repo:cybereason-labs/ds-brain` and a `path:wiki/` scope unless the user explicitly asked for raw source material. Add more specific subfolder scopes (`path:wiki/Entities/Projects/`, `path:wiki/Decisions/`) to narrow.

3. **Read the candidate notes.** Pull frontmatter + the relevant section via `get_file_contents`. If a note links to `[[Other Note]]` clearly relevant to the question, follow the link by guessing the path and fetching.

4. **Compose the answer.** Stay grounded — every non-trivial claim should cite a wiki page (and the underlying `raw/` source when the user asked for evidence). Quote sparingly. If the brain doesn't contain enough to answer, say so explicitly rather than inventing.

5. **Surface the "Open questions" section** of any entity / decision / research note you read — those are deliberate signals from prior synthesis cycles about what's still unknown.

6. **Don't run lint, ingest, or any other slash command** unless the user explicitly asks. The brain has its own rhythm.

### Read-only golden rule

When reading, prefer `wiki/` for synthesized knowledge and `raw/` only for evidence the user asked to verify. If both exist, cite the wiki note and link to the raw source — this matches the brain's own citation convention.

## Write-to-INBOX workflow

When the user wants to save something to the brain:

1. **Compose a clean Markdown note.** Match the right template (see `references/inbox-templates.md`) — meeting, insight, raw material, decision draft, reference/link, or generic free-form. If unsure, use the generic template; the server-side ingest will route it.

2. **Required frontmatter.** Every INBOX file carries at minimum:

   ```yaml
   ---
   title: <short descriptive title>
   created_at: 2026-05-14
   created_by: <user email or name>
   source_type: <meeting | insight | raw | link | decision-draft | wiki-update-request | free-form>
   status: inbox
   tags: [inbox]
   ---
   ```

   Optional but valuable:
   ```yaml
   related_people: ["[[Inbar Dekel]]", "[[Aviad Cohen]]"]
   related_projects: ["[[Tipper]]"]
   meeting_date: 2026-05-14
   participants: ["[[Inbar Dekel]]", "[[Maor Gabay]]"]
   ```

3. **Filename convention.** `INBOX/YYYY-MM-DD-<kebab-slug>.md`. The date is the date of the *event* (meeting date, insight date), not necessarily today. The slug is short and descriptive.

   Example: `INBOX/2026-05-14-tipper-rollout-retro.md`

4. **Save under `INBOX/`.** Never under `wiki/`, `raw/`, or anywhere else. INBOX is the only sanctioned write destination.

5. **Write via GitHub MCP — single API call, no local clone.** Use `mcp__github__create_or_update_file` with:

   ```
   owner:   cybereason-labs
   repo:    ds-brain
   branch:  unified
   path:    INBOX/2026-05-14-tipper-rollout-retro.md
   content: <full markdown — frontmatter + body>
   message: "inbox | tipper rollout retro 2026-05-14"
   ```

   The commit message follows the brain's existing convention: `inbox | <subject>` (lowercase op, pipe, subject). Omit `sha` when creating; supply it only when updating an existing file.

6. **Do not run `/ingest`.** Ingestion is a server-side maintainer operation.

7. **Confirm to the user.** Tell them the filename and the resulting commit SHA returned by the API. Note that the server-side pipeline will pick it up.

### Saving a conversation insight

When the user says "save this conversation" or "remember this for the team," you have to do the synthesis:

- Read the recent conversation context
- Identify: the **insight or decision**, the **assumptions** behind it, the **open questions** that remain, the **action items** if any
- Preserve enough surrounding context that someone reading it cold next week can understand what we were discussing and why
- Attribute speakers if multiple people were involved (e.g., a meeting summary)

Do not just dump the entire chat transcript. Distill it.

## Safety constraints (hard rules)

These are non-negotiable. The skill enforces a write boundary so the central ingest pipeline stays the single source of truth.

| Path | Read | Write |
|------|------|-------|
| `INBOX/` | ✓ | ✓ |
| `wiki/` | ✓ | ✗ |
| `raw/` | ✓ | ✗ (and PreToolUse hook will block) |
| `.claude/`, `scripts/`, `tools/`, `hooks/` | ✓ | ✗ |
| `CLAUDE.md`, `AGENTS.md`, top-level schema files | ✓ | ✗ |
| `.obsidian/` | ✓ | ✗ |

If the user asks you to **update a wiki note**, do not edit it. Create an INBOX *update-request* note describing what they want changed (see template). The server-side ingest decides whether and how to apply it.

If the user asks you to **delete or rewrite brain content**, create an INBOX *delete-request* note (or update-request) — never run `/remove` or directly modify wiki content yourself.

If the user explicitly says they are a maintainer and wants to bypass these rules, decline politely and explain that maintainer operations happen via the server-side pipeline, not this skill. (If they really need direct edit access, they should drop this skill and use the standard `/ingest`, `/lint`, `/remove` commands directly.)

## Examples

### Example 1 — Query about a project

**User:** "What do we know about the Tipper rollout?"

**Behavior:**
1. `mcp__github__search_code` with `q: "Tipper" repo:cybereason-labs/ds-brain path:wiki/`.
2. `mcp__github__get_file_contents` for `wiki/Entities/Projects/Tipper.md` on `ref: unified`. Read its frontmatter + status + linked decisions and meetings.
3. Follow wikilinks: fetch `wiki/Decisions/Tipper alert routing 2026-04-22.md` (guessed from `[[Decision: Tipper alert routing 2026-04-22]]`); if 404, fall back to `search_code` with `filename:"Tipper alert routing*" repo:cybereason-labs/ds-brain`.
4. Answer concisely with citations: "Per [[Tipper]] (last updated 2026-05-08), rollout is in pilot with [[Cybereason]] EDR fleet. [[Decision: Tipper alert routing 2026-04-22]] set the threshold at 0.7. Open questions: false-positive rate on Windows endpoints (flagged in the project note)."

### Example 2 — Save a meeting summary

**User:** "Save this meeting to the brain — we just decided to move the LoRA fine-tune to next quarter because the eval harness isn't ready."

**Behavior:**
1. Compose `INBOX/2026-05-14-lora-finetune-deferral.md` using the meeting template.
2. Frontmatter: `source_type: meeting`, `meeting_date: 2026-05-14`, `participants:` from conversation context, `related_projects: ["[[LoRA Fine-Tune]]"]`, `tags: [inbox, decision, q3-planning]`.
3. Body captures the decision, the reason (eval harness not ready), open questions (what defines "ready"), action items.
4. Single API write via `mcp__github__create_or_update_file` (owner=`cybereason-labs`, repo=`ds-brain`, branch=`unified`, path=`INBOX/2026-05-14-lora-finetune-deferral.md`, message=`inbox | lora finetune deferral 2026-05-14`).
5. Confirm: "Saved to `INBOX/2026-05-14-lora-finetune-deferral.md` on `unified` as commit `<sha>`. The server-side ingest will pick it up on the next cycle."

### Example 3 — Wiki update request

**User:** "Update the Aviad Cohen page — his title is now Principal AI Architect, not Senior."

**Behavior:**
1. Do *not* edit `wiki/Entities/People/Aviad Cohen.md`.
2. Create `INBOX/2026-05-14-aviad-cohen-title-update.md` with `source_type: wiki-update-request`.
3. Body: "Requested change to [[Aviad Cohen]]: update `title` from 'Senior AI Architect' to 'Principal AI Architect'. Reason: promotion effective 2026-05."
4. One API commit via `mcp__github__create_or_update_file` with message `inbox | aviad cohen title update`.
5. Confirm to user: filed the update request as commit `<sha>`; server-side ingest will apply it.

### Example 4 — Add a reference link

**User:** "Drop this Karpathy gist in the brain — https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f"

**Behavior:**
1. Compose `INBOX/2026-05-14-karpathy-wiki-llm-gist.md` with `source_type: link`.
2. Frontmatter includes the URL and `tags: [inbox, reference, llm, wiki-pattern]`.
3. Body: short note on what the link is and why it's worth filing. Optionally include the actual content if it's small and the user wanted it captured.
4. One API commit via `mcp__github__create_or_update_file` with message `inbox | karpathy wiki-llm gist`.

### Example 5 — Ambiguous request

**User:** "Save this."

**Behavior:** Ambiguous — ask one short clarifying question. "Want me to drop this into the DS brain INBOX? If yes, what should I title it — is this a meeting note, an insight, or something else?" Then proceed.

## Error handling

| Situation | What to do |
|-----------|-----------|
| GitHub MCP not connected | Halt. Walk the user through `references/setup.md` (PAT generation + `claude mcp add github ...`). Resume after Claude Code restart. |
| Search returns nothing for a recent commit | GitHub code-search index lags ~1 minute and skips files >384 KB. Retry after a beat, or fall back to a directory listing via `get_file_contents` on the parent folder and a targeted file fetch. |
| `get_file_contents` returns 404 on a guessed wikilink path | Fall back to `search_code` with `filename:<Name>.md repo:cybereason-labs/ds-brain`. If still nothing, tell the user the note doesn't exist; offer to file an INBOX request. |
| GitHub API write fails — `401 Unauthorized` | PAT is invalid, expired, or revoked. Point the user at the PAT regeneration steps in `references/setup.md`. Do not retry. |
| GitHub API write fails — `403 Forbidden` | PAT lacks `Contents: Read and write` on this repo, or the user isn't a collaborator on `cybereason-labs/ds-brain`. Show the exact response. Point at PAT scope section of `references/setup.md` or ask the maintainer to add them as a collaborator. |
| GitHub API write fails — `404 Not Found` | Repo path / branch wrong. Verify owner = `cybereason-labs`, repo = `ds-brain`, branch exists (typically `unified`). |
| GitHub API write fails — `409 Conflict` / stale SHA | Someone else updated the same file while you were composing. Re-fetch with `mcp__github__get_file_contents`, get the new `sha`, retry the write. Don't force. |
| GitHub API write fails — `422 Unprocessable Entity` | Usually means the file content failed branch-protection rules (e.g., required PR review). Show the error. Offer to use `mcp__github__create_pull_request` workflow instead of direct commit. |
| GitHub API rate limit hit | Show remaining quota from response headers. Tell user to wait until reset window or use a PAT with higher limits. Do not retry. |
| User asks to write outside INBOX | Decline, explain the constraint, offer to file an update-request note instead. |
| User declines to install the GitHub MCP | Acknowledge. Do not proceed. The skill is MCP-required; reading or writing the vault any other way would create inconsistent behavior across the team. |

## Operational checklist

Before claiming a write operation is done, verify:

- [ ] File path starts with `INBOX/` and matches `YYYY-MM-DD-<slug>.md` convention
- [ ] Frontmatter has `title`, `created_at`, `created_by`, `source_type`, `status: inbox`, `tags` (with `inbox`)
- [ ] Body distills the content — not a raw dump
- [ ] `mcp__github__create_or_update_file` call targeted `owner=cybereason-labs`, `repo=ds-brain`, `branch=unified`
- [ ] Commit message matches `inbox | <subject>` format
- [ ] API response returned a commit SHA (you saw it)
- [ ] User told the filename + commit SHA, and that the server-side ingest will process it

Before claiming a read operation is done, verify:

- [ ] You actually opened the relevant note(s) via `get_file_contents`, not just a search hit snippet
- [ ] You cited the wiki page(s) you drew from
- [ ] You noted uncertainty if the brain didn't have enough evidence
- [ ] You didn't invent facts to fill gaps

## Reference files

- `references/inbox-templates.md` — Markdown templates for every `source_type` (meeting, insight, raw, link, decision-draft, wiki-update-request, free-form)
- `references/setup.md` — One-time GitHub MCP install (PAT generation + `claude mcp add github ...`)
