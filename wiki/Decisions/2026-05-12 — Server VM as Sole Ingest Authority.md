---
title: Server VM as Sole Ingest Authority
type: decision
tags: [decision, wiki]
date: 2026-05-12
deciders: ["[[Aviad Cohen]]", "[[Guy Kassorla]]"]
status: accepted
related_projects: ["[[DS Brain]]"]
last_updated: 2026-05-12
---

# Server VM as Sole Ingest Authority — 2026-05-12

## Context

In the team-wide topology for [[DS Brain]] (see [[2026-05-12 — Aviad and Guy DS Brain architecture]]), multiple humans drop material into `INBOX/` and multiple local Claude instances query `wiki/`. The pipeline that turns `INBOX/` items into `raw/` + `wiki/` entries (`/ingest`) and the periodic consistency pass (`/lint`) need a single authority — otherwise concurrent or partial runs could corrupt the corpus.

## Decision

A shared **Ubuntu VM** hosts the server-side ingest Claude. The VM polls git on a short interval, processes any new `INBOX/` items into `raw/` + `wiki/`, commits + pushes back to `origin/unified`, and runs `/lint` on a daily schedule. **No other agent is permitted to mutate `raw/` or `wiki/`** — local clients are constrained to read `wiki/` and write only to `INBOX/` ([[2026-05-12 — Local Claude Write-Only to INBOX]]).

## Why

Centralising ingest gives one authoritative process for synthesis, wikilink resolution, frontmatter compliance, and lint reconciliation. Avoids the failure mode where a local Claude partially ingests a source (e.g. creates the Source page but forgets to update People mentions). Concentrates Claude API spend and operational telemetry in one place. Aligns the brain's operational model with its existing single-author invariant (the `unified` branch, the `wiki-ops.md` audit trail) — the server is the "human" the existing log convention already assumes.

## Alternatives considered

- **Distributed ingest** — each local Claude can run `/ingest` against the shared repo. Rejected: high collision risk and inconsistent synthesis quality across users.
- **Manual ingest only** — humans always trigger `/ingest` from their workstation. Rejected: defeats the goal of an always-fresh team brain and reintroduces single-user dependence.
- **GitHub Actions runner instead of a long-lived VM** — not discussed in depth; viable alternative, may be revisited if VM operational burden is high.

## Consequences

- Server VM is a single point of failure for ingest and lint (but **not** for queries — local Claudes can still read whatever state git has).
- Need a deployment story: provisioning, secrets (Anthropic API key), git auth (deploy key vs PAT), monitoring, restart-on-crash.
- Need a serialisation story for concurrent `INBOX/` arrivals (queue order or single-flight ingest loop with a per-run lock).
- Daily `/lint` cadence is now a server cron, not an ad-hoc human action — must be observable; existing `wiki-ops.md` commit trail is the default surface.
- Server-side Claude becomes a privileged identity in git history — auditability of "who wrote what" still holds because the original `INBOX/` drop is recorded.

## Open questions

- Where does the VM live (cloud account, internal infra, on-prem)? Who owns the bill?
- What polling interval balances freshness vs. Claude API cost and git-traffic noise?
- How are server-side ingest failures surfaced to the team (Slack, GitHub commit status, `pulse.md` entry)?
- Is there a manual override path (e.g. an `/ingest` invoked locally with an explicit "server-mode" credential) for hot-fixes when the VM is down?
- How is the server Claude version-pinned, and how is its prompt/skill bundle reviewed when it changes?
