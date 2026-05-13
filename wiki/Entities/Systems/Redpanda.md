---
title: Redpanda
type: system
tags: [system, wiki]
owner: Redpanda Data (vendor)
vendor: Redpanda Data
related_projects: ["[[Phoenix Review]]"]
seeds:
  - raw/data_science_drive/data-science-main.md
last_updated: 2026-05-11
---

# Redpanda

> Kafka-compatible, fast, scalable streaming-data platform. [[Phoenix]]'s primary event bus — replaces the in-memory Transparency graph used by [[Core]].

## Owner / vendor

Redpanda Data (vendor) — embedded inside [[Phoenix]].

## Integration surface

Kafka-protocol producers / consumers.

## Data flow

`sensor-gateway` → Redpanda → `cep-service` (Sigma) → downstream Phoenix services.

## Current usage

Phoenix event backbone.

## Known issues

(stub)

## Related entities

[[Phoenix]], [[ClickHouse]]

## Open questions
