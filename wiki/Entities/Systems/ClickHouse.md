---
title: ClickHouse
type: system
tags: [system, wiki]
owner: ClickHouse Inc. (vendor / OSS)
vendor: ClickHouse Inc.
related_projects: ["[[Phoenix Review]]"]
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

Phoenix analytics layer.

## Known issues

(stub)

## Related entities

[[Phoenix]], [[Redpanda]]

## Open questions
