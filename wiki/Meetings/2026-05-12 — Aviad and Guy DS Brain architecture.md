---
title: Aviad and Guy DS Brain architecture
type: meeting
tags: [meeting, wiki]
date: 2026-05-12
participants: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
related_projects: ["[[DS Brain]]", "[[Martin News Chatbot]]"]
related_systems: ["[[Cursor]]"]
related_decisions: ["[[2026-05-12 — Unified Branch over Split for DS Brain]]", "[[2026-05-12 — Local Claude Write-Only to INBOX]]", "[[2026-05-12 — Server VM as Sole Ingest Authority]]"]
source: raw/meetings/meeting_summary_2026.05.12_aviad_guy_ds_brain.md
last_updated: 2026-05-12
---

# Aviad and Guy DS Brain architecture — 2026-05-12

> Working session between [[Aviad Cohen]] and [[Guy Kassorla]] to design the rollout of the [[DS Brain]] from Aviad's local prototype into a team-wide system for the four-person DS team ([[Aviad Cohen]], [[Guy Kassorla]], [[Itamar Hershko]], [[Inbar Dekel]]).

## Decisions

- Use a single unified git branch for the [[DS Brain]] (rejecting Aviad's split-branch proposal). Schema-layer protection enforced via a robust Skill / system-prompt boundary on local Claude rather than physical folder hiding. See [[2026-05-12 — Unified Branch over Split for DS Brain]].
- Local Claude instances may **read the wiki and write only to `INBOX/`** — never write directly to `raw/` or `wiki/`. See [[2026-05-12 — Local Claude Write-Only to INBOX]].
- A shared Ubuntu server VM is the **sole entity authorised to ingest from `INBOX/` into `raw/` and `wiki/`**, polling git on a short interval and running daily `/lint`. See [[2026-05-12 — Server VM as Sole Ingest Authority]].

## Action items

- [ ] Stand up the shared Ubuntu VM and configure git-pull + periodic ingest + daily lint triggers — [[Aviad Cohen]] (pairing with [[Guy Kassorla]] post-presentation + [[Inbar Dekel]] 1:1)
- [ ] Author the local-Claude Skill / system-prompt boundary that pins reads to `wiki/` and writes to `INBOX/` only — [[Aviad Cohen]] + [[Guy Kassorla]]
- [ ] Onboard [[Itamar Hershko]] and [[Inbar Dekel]] as second + third users once the boundary Skill is verified — [[Aviad Cohen]]

## Discussion notes

**Current local prototype.** Aviad runs a fully working local instance of the [[DS Brain]] backed by Claude. Single git repo. Three layers: a raw material folder (`raw/`, `INBOX/`), a processed wiki (`wiki/`) of Obsidian Markdown files with YAML frontmatter + double-bracket wikilinks (e.g. linking an [[Inbar Dekel]] note as manager of the [[Data Science Team]] note), and a schema layer (`.claude/`, `CLAUDE.md`) defining commands `/ingest`, `/query`, `/lint`. Pipeline: drop into `INBOX/` → Claude moves to `raw/` → Claude synthesises into `wiki/` → periodic `/lint` catches contradictions and broken links.

**Goal — team brain.** Promote the local prototype into a global brain for the four DS team members so any member's local Claude can pull full company / team / project context (e.g. for [[Martin News Chatbot]]) without manual context priming. New project members starting an unfamiliar workstream gain immediate access to who-knows-what, prior decisions, and adjacent projects.

**Server-vs-client split.** Shared Ubuntu VM hosts the server-side ingest Claude that pulls git periodically, processes `INBOX/` into `raw/` + `wiki/`, commits + pushes, and runs daily `/lint`. Team members connect locally via [[Cursor]] / Obsidian + MCP and rely on the same git repo as the source of truth. Local Claude is read-only on `wiki/`.

**Collision problem.** If every local Claude has full write access to git via Obsidian, two local Claudes could write to `wiki/` simultaneously or skip the ingest pipeline entirely — producing sync conflicts and bypassing the lint / synthesis steps that keep the corpus coherent. Mitigation: a hard read/write boundary on local Claudes (`wiki/` read-only, `INBOX/` write-only). The server VM is the sole writer to `raw/` and `wiki/`.

**Branching debate — unified won.** Aviad initially wanted a split repo where local clients clone only the data folders (`INBOX/`, `raw/`, `wiki/`) and the server holds the full repo including `.claude/`, `CLAUDE.md`, `tools/`, `scripts/`. Motivation: physically hide the schema layer from local Claude so it cannot accidentally modify the system's own architecture. Guy pushed back on operational complexity — maintaining split branches that sync only specific folders is overly complex. In-meeting Aviad asked Claude whether git natively supports folder-subset auto-sync across branches; Claude confirmed it does not (would require `git subtree` or custom scripts), effectively proving Guy's point. Aviad conceded; they aligned on a unified branch plus a strict boundary Skill on local Claude.

**Tone.** Aviad explicitly thanked Guy for arguing — noted that constructive pushback is the best way to refine complex architectural designs.

**Next steps.** Physical pairing session at the office to build the server VM + boundary Skill. Blocked on Aviad's upcoming presentation and a 1:1 with [[Inbar Dekel]].

**Aside — [[Martin News Chatbot]] collaborator workflow.** Aviad flagged that the team currently collaborating on [[Martin News Chatbot]] (Jose's side / Level Blue research) does not use git — they work directly inside AWS Workspaces and exchange code as zip downloads. Material risk for any production hand-off that involves version-control discipline.

## Open questions

- What polling / trigger cadence does the server VM use for git-pull → ingest → lint, and how does it serialise concurrent `INBOX/` writes from multiple local clients?
- What enforces the local-Claude boundary at runtime — purely the Skill prompt, or also a filesystem / git pre-commit guard analogous to the existing `scripts/hooks/guard_immutable.py`?
- How is conflict resolved if two team members simultaneously drop overlapping or contradicting material into `INBOX/`?
- How is the schema layer (`.claude/`, `CLAUDE.md`, `tools/`, `scripts/`) versioned and reviewed when the team grows beyond four people, or when local Claudes themselves want to evolve it?
- Does the [[Martin News Chatbot]] collaborator team's lack of git workflow block the production hand-off, or does a different exchange format suffice?
