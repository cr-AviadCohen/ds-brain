---
title: Pre-filter Rules Before ML on ClickHouse
type: decision
tags: [decision, wiki]
date: 2026-05-18
deciders: ["[[Xin Tang]]", "[[Aviad Cohen]]", "[[Inbar Dekel]]"]
status: accepted
related_projects: ["[[Smart Asset Correlation]]"]
last_updated: 2026-05-18
---

# Pre-filter Rules Before ML on ClickHouse — 2026-05-18

## Context

The [[Smart Asset Correlation]] Phase 2 / Mode 3 service must query [[ClickHouse]] — Phoenix's analytics store — to infer behavioral relationships between assets and users. ClickHouse holds up to ~15 PB of raw events across roughly 2,000 customer organisations, on a single node. Per [[Xin Tang]], naive ML-over-raw-events workloads will OOM the cluster and break all downstream Phoenix analytics.

## Decision

Every ML / scoring pass must be preceded by domain-specific SQL pre-filter rules that shrink the candidate event set before any model invocation. No ML runs on the raw dataset.

## Why

Resource preservation. The ClickHouse cluster is shared infrastructure with no headroom for unbounded scans. Pre-filter rules push selectivity into the database engine (column pruning, partition filtering, aggregation) where ClickHouse is fastest, leaving the ML layer to operate on a tractable candidate slice. Skipping this step risks a cluster-wide outage with blast radius far beyond the DS service.

## Alternatives considered

- **Stream directly to ML.** Rejected — guaranteed ClickHouse meltdown on ~15 PB.
- **Replicate slices to a separate analytics surface.** Not viable short-term — no second ClickHouse node, and the storage cost duplicates the entire fleet's history.
- **Schedule overnight bulk jobs.** Doesn't help — single-node still saturates; also delays freshness.

## Consequences

- DS service architecture must own a rule library (likely YAML or SQL templates).
- Rule authorship requires cyber-domain knowledge the DS team lacks — bottleneck on [[Hen Ashkenazi]]'s team or threat research, both currently at capacity.
- Each Phase 2 mode (user-owns-machine, asset-belongs-to-org, etc.) needs at least one validated pre-filter rule before its ML stage ships.
- Sets the architectural pattern for any future DS service that touches ClickHouse.

## Open questions

- Who authors the rules — DS researchers, [[Hen Ashkenazi]]'s team, or threat research?
- Rule storage format and versioning.
- Pre-filter rule validation harness — how do we know a rule is selective enough before it hits prod ClickHouse?
