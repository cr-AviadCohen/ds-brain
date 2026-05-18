---
title: Smart Asset Correlation knowledge transfer
type: meeting
tags: [meeting, wiki]
date: 2026-05-18
participants: ["[[Xin Tang]]", "[[Inbar Dekel]]", "[[Aviad Cohen]]", "[[Guy Kassorla]]", "[[Adria]]"]
related_projects: ["[[Smart Asset Correlation]]"]
related_decisions: ["[[2026-05-18 — Python for Smart Asset Correlation Service]]", "[[2026-05-18 — Pre-filter Rules Before ML on ClickHouse]]", "[[2026-05-18 — Over-merge Preferred over Under-merge]]"]
source: raw/meetings/meeting_2026.05.18 - Smart Asset Correlation.md
last_updated: 2026-05-18
---

# Smart Asset Correlation knowledge transfer — 2026-05-18

> Phoenix data engineer [[Xin Tang]] handed off the asset-correlation data model + database surface to the DS team. Phase 1 (exact-match merge) done by Xin; DS team owns Phase 2 / Mode 3 (behavioral inference) against [[ClickHouse]] → PostgreSQL/TB.

## Decisions

- [[2026-05-18 — Python for Smart Asset Correlation Service]] — async + DB-bound; no need for Rust.
- [[2026-05-18 — Pre-filter Rules Before ML on ClickHouse]] — ClickHouse single node carries up to 15 PB across ~2000 orgs; ML on raw dataset will OOM the cluster.
- [[2026-05-18 — Over-merge Preferred over Under-merge]] — false positives in correlation < false negatives, because under-merging breaks automated response (isolate machine, disable account).

## Action items

- [x] Open dedicated Slack channel — [[Aviad Cohen]] — completed during meeting
- [ ] Share Phoenix repos / Confluence / ClickHouse credentials — [[Xin Tang]] — drop in Slack channel
- [ ] Define behavioral filtering rules — DS team + [[Hen Ashkenazi]]'s team — bottleneck on domain-expert bandwidth
- [ ] Schedule weekly sync — [[Inbar Dekel]] / [[Adria]] — starts next week
- [ ] Authenticate into Dev ClickHouse + run successful test query — DS team — before next sync

## Discussion notes

**Data model — two layers.** Instance = raw record per vendor integration (AWS EC2, CrowdStrike EDR, Azure machine). Canonical = unified physical machine / user. Multiple instances → one canonical asset via matching logic (IPs, hostnames, device IDs).

**Two ingest paths.** Inventory data = direct vendor API pull (ground truth, never overwritten). Discovered data = parsed from raw behavioral events when no API exists. Inventory always wins on conflict.

**Architectural split.** Xin's Phase 1 = exact-key merge (deterministic). DS Phase 2 / Mode 3 = scheduled async service, queries [[ClickHouse]] for raw events, applies behavioral rules + ML, writes confidence-scored relations to PostgreSQL/TB (relational store for transactions). Independent of Phase 1 — work parallel.

**Database constraint.** ~2000 orgs × ~15 PB total on a single ClickHouse node. ML on raw dataset is non-viable. Mandatory: domain-specific SQL pre-filter rules to shrink payload before model invocation. Resource preservation is critical — over-aggressive queries crash the cluster.

**Environment.** Dev for raw ClickHouse events (fast iteration). Staging for portal stability work.

**Language.** Python OK — service is async + DB-bound; no latency floor that demands Rust.

**Asymmetric correlation cost.** Xin: over-merge > under-merge. If automated response can't see all instances of a compromised user, isolation/account-disable is incomplete and threat escapes.

**Domain knowledge bottleneck.** DS team lacks cyber domain background to author behavioral rules ("user logs into this machine often enough that they own it"). Need [[Hen Ashkenazi]]'s team or threat research — both currently at capacity. Project will stall if not resolved.

**Schema gap.** Aviad flagged that Xin's schemas don't strictly separate mandatory vs optional fields. Xin clarified: most fields optional except primary keys.

## Strategic implications

- Direct prerequisite for automated MDR response (isolate machine, disable compromised account).
- Enriches threat-detection queries across all vendor integrations — analysts can pivot from a new IOC (hostname, MAC) across the whole tenant simultaneously.
- Direct evidence for [[identity-correlation-as-unsolved-hard-problem]].

## Open questions

- Who authors the behavioral filtering rules — DS researchers, [[Hen Ashkenazi]]'s team, or threat-research crew? Currently unowned.
- Exact schema mapping between [[ClickHouse]] (events) and PostgreSQL/TB (relations) — review by [[Aviad Cohen]] post-access.
- [[Adria]] — last name not captured in transcript; confirm at first sync.
- "TB" PostgreSQL database — full name + schema not yet captured; populate when Xin shares links.
