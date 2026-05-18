---
title: Smart Asset Correlation
type: project
tags: [project, wiki]
status: in-progress
lead: [[Itamar Hershko]]
team: ["[[Aviad Cohen]]", "[[Inbar Dekel]]", "[[Guy Kassorla]]"]
started: 2026-05-11
systems: ["[[Phoenix]]", "[[ClickHouse]]"]
related_decisions: ["[[2026-05-18 — Python for Smart Asset Correlation Service]]", "[[2026-05-18 — Pre-filter Rules Before ML on ClickHouse]]", "[[2026-05-18 — Over-merge Preferred over Under-merge]]"]
raw_path: raw/data_science_drive/data-science-projects.md
last_updated: 2026-05-18
---

# Smart Asset Correlation

> Phoenix-platform Data Science project — correlate assets (endpoints, users, identities, accounts) across telemetry and identity sources. Q2 High priority. Phoenix data lead: [[Xin Tang]]. Engineering contacts: [[Ortal Keizman]], [[Tonny Pham]]. Phoenix PM: [[Adria]]. Jira ENG-9970.

## Goal

Merge multi-vendor asset / identity records into single canonical entities so [[Phoenix]] automated response (isolate machine, disable account) operates on a complete view of a compromised actor. Direct counter to [[identity-correlation-as-unsolved-hard-problem]].

## Approach

Two-phase architecture (Xin Tang's framing, 2026-05-18):

**Phase 1 — exact-match merge (owned by Phoenix data eng, in progress under [[Xin Tang]]).** Deterministic merge across vendor integrations using primary keys (device IDs, hostnames, IPs returned by vendor APIs).

**Phase 2 / Mode 3 — behavioral inference (owned by DS team).** Scheduled async Python service that:

1. Queries raw events from [[ClickHouse]] (Phoenix analytics store).
2. Applies pre-filter SQL rules to shrink payload (mandatory — ClickHouse is single-node, ~15 PB across ~2000 orgs; raw ML scan will OOM).
3. Runs behavioral rules + ML to infer "user owns machine" / "users belong to same identity" relationships.
4. Writes confidence-scored relations to PostgreSQL/TB (relational store for transactions).

Phase 1 and Phase 2 run in parallel — no sequencing dependency.

### Data model

- **Instance layer.** Vendor-specific raw record (one per integration). Multiple instances per real-world asset.
- **Canonical layer.** Unified physical machine / user. Aggregates instances.
- **Inventory vs Discovered.** Inventory = direct vendor API pull (ground truth, never overwritten). Discovered = parsed from raw behavioral events. Inventory wins on conflict.

Confluence references:

- Main ADR: `cybereason.atlassian.net/wiki/x/coADlgc`
- Further details: `cybereason.atlassian.net/wiki/x/RID6jwc`

Jira ticket: ENG-9970.

## Status

In progress (Q2 High). Phase 1 ongoing under [[Xin Tang]]. DS Phase 2 / Mode 3 cleared to start in parallel as of 2026-05-18. Immediate next step: DS team authenticates into Dev ClickHouse and runs a successful test query.

## Decisions

- [[2026-05-18 — Python for Smart Asset Correlation Service]] — async + DB-bound profile; no latency floor demanding Rust.
- [[2026-05-18 — Pre-filter Rules Before ML on ClickHouse]] — domain-specific SQL pre-filters mandatory before ML invocation; ClickHouse is single-node + multi-PB.
- [[2026-05-18 — Over-merge Preferred over Under-merge]] — false positives < false negatives in correlation, because under-merging defeats automated response.

## Risks

- **ClickHouse overload.** Single-node DB across ~2000 orgs; poorly optimised queries will crash the cluster and block all Phoenix analytics.
- **Domain-knowledge bottleneck.** DS team can't author behavioral rules without cyber-domain support. [[Hen Ashkenazi]]'s team and threat research are both at capacity — project stalls if bandwidth doesn't materialise.
- **Schema looseness.** Most fields in Xin's schemas are optional (only PKs mandatory) — DS service must validate aggressively.
- **Cross-DB consistency.** ClickHouse (events) ↔ PostgreSQL/TB (relations) schema mapping not yet captured.

## Mentions

- 2026-05-11 — [[data-science-team-knowledge]] — Q2 High-priority project; lead [[Itamar Hershko]]; Phoenix platform; contacts [[Ortal Keizman]], [[Tonny Pham]]; Jira ENG-9970.
- 2026-05-18 — [[2026-05-18 — Smart Asset Correlation knowledge transfer]] — Xin Tang knowledge transfer; Phase 2 / Mode 3 scope locked for DS team; three architectural decisions taken; weekly sync to be scheduled.

## Open questions

- Who authors the behavioral filtering rules — DS researchers, [[Hen Ashkenazi]]'s team, or threat research?
- Exact schema mapping between [[ClickHouse]] and PostgreSQL/TB — pending DS access.
- Confidence-score calibration + threshold for writing back to PostgreSQL/TB.
- Cost / latency budget on Phoenix for the scheduled service.
- Cross-vendor identity source list (full catalogue not yet enumerated).
