---
title: DS Brain
type: project
tags: [project, wiki, meta]
status: active
lead: [[Aviad Cohen]]
team: ["[[Aviad Cohen]]", "[[Guy Kassorla]]", "[[Itamar Hershko]]", "[[Inbar Dekel]]"]
started: 2026-05-11
target_ship: TBD
systems: ["[[Cursor]]"]
related_decisions: ["[[2026-05-12 — Unified Branch over Split for DS Brain]]", "[[2026-05-12 — Local Claude Write-Only to INBOX]]", "[[2026-05-12 — Server VM as Sole Ingest Authority]]"]
raw_path: null
last_updated: 2026-05-12
---

# DS Brain

> Team-wide AI knowledge base for the Data Science team — an Obsidian-compatible Markdown vault implementing Andrej Karpathy's wiki-LLM pattern, with a server-side ingest Claude and local Claude clients constrained to read-from-`wiki/` / write-only-to-`INBOX/`.

## Goal

Convert Aviad's working local prototype (this repo) into a shared brain for the four-person DS team ([[Aviad Cohen]], [[Guy Kassorla]], [[Itamar Hershko]], [[Inbar Dekel]]) so any member's local Claude can answer questions backed by the team's full corpus — people, projects, meetings, decisions, research, sources — without manual context priming. A new project (e.g. [[Martin News Chatbot]]) immediately inherits relevant institutional context: who owns what, prior decisions, adjacent systems.

## Approach

Three layers per Karpathy:

- **Raw** (`raw/`, `INBOX/`) — append-only, human-authored.
- **Wiki** (`wiki/`) — Claude-synthesised, Markdown + YAML frontmatter + Obsidian-style wikilinks.
- **Schema** (`CLAUDE.md`, `.claude/`, `tools/`, `server/`) — co-evolved governance and commands (`/ingest`, `/query`, `/lint`, `/remove`, `/braindump`, `/auto-ingest`, `/auto-lint`).

Topology for team rollout (decided 2026-05-12):

- Single **unified** git branch for all users (no split, no sparse checkout) — see [[2026-05-12 — Unified Branch over Split for DS Brain]].
- A shared **Ubuntu VM** hosts the server-side ingest Claude that polls git on a short interval, processes `INBOX/` into `raw/` + `wiki/`, commits + pushes back to `origin/unified`, and runs `/lint` on a daily schedule — see [[2026-05-12 — Server VM as Sole Ingest Authority]].
- **Local clients** run [[Cursor]] / Obsidian + Claude via MCP, constrained by a Skill / system-prompt boundary that pins them to **read `wiki/`, write only `INBOX/`** — see [[2026-05-12 — Local Claude Write-Only to INBOX]].

## Status

active — local prototype fully functional on Aviad's machine (this repo on the `unified` branch). Team-wide rollout pending: server VM not yet built; boundary Skill for local Claudes not yet authored; second + third users ([[Itamar Hershko]], [[Inbar Dekel]]) not yet onboarded. Build pairing session blocked on Aviad's upcoming presentation + 1:1 with [[Inbar Dekel]].

## Decisions

- Unified git branch over split branches — [[2026-05-12 — Unified Branch over Split for DS Brain]].
- Local Claude write-only to `INBOX/`, never `raw/` or `wiki/` — [[2026-05-12 — Local Claude Write-Only to INBOX]].
- Shared Ubuntu VM is the sole authority for ingest + lint — [[2026-05-12 — Server VM as Sole Ingest Authority]].

## Risks

- **Sync conflicts** if the local boundary Skill is bypassed and a local Claude writes directly to `wiki/`. Mitigation: prompt-level boundary plus the existing `.claude/hooks/guard_immutable.py` filesystem guard; ideally extend the guard to cover `wiki/` writes from non-server agents.
- **Server VM single point of failure** for ingest + lint — outage stalls the corpus update flow without blocking local queries (git state is still readable).
- **Schema co-evolution** under multiple authors — `.claude/`, `CLAUDE.md`, `tools/` are powerful surfaces; uncoordinated edits could break commands or invariants. Needs a change-control discipline.
- **Concurrent `INBOX/` writes** from multiple local clients need a serialisation story on the server (queue order, single-flight ingest loop, or per-file lock).
- **Trust-boundary drift** — Skill prompt is not a hard sandbox; a sufficiently determined local Claude could still emit a `Write` against `wiki/`. The filesystem-guard backstop matters.

## Mentions

- 2026-05-12 — [[2026-05-12 — Aviad and Guy DS Brain architecture]] — first whole-team architecture working session; locked unified-branch + local-write-only-to-`INBOX/` + server-as-sole-ingest-authority.

## Open questions

- What polling cadence and serialisation strategy does the server use for `INBOX/` → `raw/` → `wiki/` + lint?
- Should the local-Claude boundary be enforced only by the Skill prompt, or also by an extended filesystem / pre-commit guard?
- How is schema-layer (`.claude/`, `CLAUDE.md`) change-control governed once 4+ humans + ≥2 Claude instances co-author?
- Does this project get promoted onto [[Active Focus]] or live entirely as a meta workstream alongside the platform Q2 projects?
- Where does the server VM live (cloud, internal infra, on-prem)? Who funds it?
- What is the failure-surfacing path for server-side ingest errors — Slack, GitHub commit status, `pulse.md`?
