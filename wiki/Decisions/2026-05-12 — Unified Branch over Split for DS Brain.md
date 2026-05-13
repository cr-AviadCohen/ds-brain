---
title: Unified Branch over Split for DS Brain
type: decision
tags: [decision, wiki]
date: 2026-05-12
deciders: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
status: accepted
related_projects: ["[[DS Brain]]"]
last_updated: 2026-05-12
---

# Unified Branch over Split for DS Brain — 2026-05-12

## Context

For the team-wide rollout of the [[DS Brain]] (see [[2026-05-12 — Aviad and Guy DS Brain architecture]]), Aviad initially proposed a split repository where local clients clone only the data folders (`INBOX/`, `raw/`, `wiki/`) while the server holds the full repo including `.claude/`, `CLAUDE.md`, `tools/`, `scripts/`. Motivation: physically hide the schema layer from local Claude instances and prevent them from accidentally modifying the system's own architecture.

## Decision

Adopt a **single unified git branch** (the existing `unified` branch) for all four DS team members. Schema-layer protection is enforced by a robust Skill / system-prompt boundary applied to local Claude instances — see [[2026-05-12 — Local Claude Write-Only to INBOX]] — rather than by branch-level folder hiding.

## Why

In-meeting arbitration (via Claude) confirmed that git does not natively support auto-syncing folder subsets across branches — implementing the split would require ongoing `git subtree` plumbing or custom scripts, both of which add operational complexity and a permanent additional failure mode. Trading that complexity for a prompt-level boundary is cheaper, easier to audit, easier to extend, and aligned with the existing append-only / hook-based protection model already in use for `raw/`.

## Alternatives considered

- **Split branches with manual / `git subtree` sync** — rejected: high maintenance, conflict-prone, and the schema-layer-hiding goal is achievable at the Skill layer at lower cost.
- **Local sparse-checkout of `wiki/` only** — not discussed in depth in this session; carries similar tooling burden to the split-branch option and breaks Obsidian's expectation of a single vault root.

## Consequences

- All four team members work off the `unified` branch with the same view of the repo (including the schema layer).
- The local-Claude boundary must be implemented as a robust Skill / system prompt and ideally backed by an extended `scripts/hooks/guard_immutable.py` covering `wiki/` writes from non-server agents.
- Schema-layer change-control becomes a process question rather than a structural one — must be addressed before the team grows beyond four.
- Tooling sprawl avoided: no `git subtree`, no folder-subset sync scripts, no parallel CI for two branches.

## Open questions

- How is the boundary Skill version-pinned against the repo so that a stale local copy can't bypass an updated rule set?
- Should the `guard_immutable.py` hook be extended to make `wiki/` write-only-for-server, mirroring the prompt-level rule?
- How is schema-layer drift (`CLAUDE.md`, `.claude/commands/*.md`) reviewed when any local Claude can technically read it?
