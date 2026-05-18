---
title: ClickHouse
type: system
tags: [system, wiki]
owner: ClickHouse Inc. (vendor / OSS)
vendor: ClickHouse Inc.
related_projects: ["[[Phoenix Review]]", "[[Smart Asset Correlation]]"]
seeds:
  - raw/data_science_drive/data-science-main.md
last_updated: 2026-05-11
---

# ClickHouse

> Columnar OLAP database — [[Phoenix]]'s analytics store for raw events. Cited as "the fastest DB for analytics" in the DS team's general-knowledge doc.

## Owner / vendor

ClickHouse Inc. — embedded inside [[Phoenix]].

## Integration surface

SQL.

## Data flow

`clickhouse-ingester-v2` bulk-writes `raw-events` from [[Redpanda]] → ClickHouse → analytics queries / Data Science jobs.

## Current usage

Phoenix analytics layer. Primary read surface for the [[Smart Asset Correlation]] DS service (Phase 2 / Mode 3 behavioral inference).

## Known issues

- **Single-node cluster** (per [[Xin Tang]], 2026-05-18) carrying ~15 PB across ~2000 organisations. Poorly-bounded queries crash the cluster — see [[2026-05-18 — Pre-filter Rules Before ML on ClickHouse]].
- Any ML-style workload against the raw dataset is non-viable; pre-filter SQL rules are mandatory before model invocation.

## Related entities

[[Phoenix]], [[Redpanda]]

## Open questions
