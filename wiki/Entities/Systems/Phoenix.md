---
title: Phoenix
type: system
tags: [system, wiki]
owner: Cybereason
related_projects: ["[[Phoenix Review]]", "[[RCE-NG]]", "[[Malop-Worthy]]", "[[Risk Assessment]]", "[[IRCA]]", "[[AI Assistant]]"]
seeds:
  - raw/cybereason/phoenix/summary-phoenix-server.md
  - raw/cybereason/phoenix/summary-phoenix-agent.md
  - raw/data_science_drive/data-science-main.md
last_updated: 2026-05-13
---

# Phoenix

> Cybereason's cloud-hosted, multi-tenant EDR/XDR platform that ingests endpoint and external telemetry, detects threats in real time, and dispatches remediation commands back to agents.

## Owner / vendor

Cybereason — successor to the legacy Core platform.

## Integration surface

- Endpoint agents (Phoenix Agent / Sunbird) connect via HTTPS+mTLS to `sensor-gateway`.
- gRPC facades over storage for analyst-portal reads.
- MQTT (TLS) push channel for actions back to the endpoint.
- Apache Flink CEP rule evaluation; Sigma engine in `cep-service`.
- Protobuf shared schemas (`SingleEvent`, `Detection`, `Action`, `FullAgentInfo`).

## Data flow

Agents (Windows/Linux/macOS) → `sensor-gateway` → Redpanda/Kafka → `cep-service` (Sigma) → `correlation-service` → `detection-store` (Postgres) → analyst portal. In parallel, `clickhouse-ingester-v2` bulk-writes `raw-events` to ClickHouse for analytics; `xdr-worker-v2` (Temporal) pulls external SIEM/cloud telemetry.

## Current usage

Replaces the legacy Core backend. Core stored data graph-based in Transparency (RAM); Phoenix is multi-tenant, runs faster, works on local disk, and uses Redpanda (Kafka-compatible streaming) + ClickHouse (analytics DB). Data Science depends on Phoenix for: RCE-NG (correlation engine pivoting from old XDR to Phoenix), Malop-Worthy (input schema follows Phoenix detections), Risk Assessment (defining required schema fields).

## Known issues

- New schema differs from legacy XDR; downstream projects must remap.
- Benign vs detection separation at RCE input still open (cost and accuracy implications).

## Related entities

[[Phoenix Review]], [[RCE-NG]], [[Malop-Worthy]], [[Risk Assessment]], [[IRCA]], [[AI Assistant]], [[Core]]

Active ideas targeting Phoenix as deployment surface: [[Rebuild UEBA in Phoenix XDR]].

Both [[IRCA]] and [[AI Assistant]] are presently deferred — Phoenix engineering bandwidth is the gating constraint per [[2026-05-12 — Aviad and Jose intro]].

## Open questions

- Final detection-stage scheme into and out of RCE-NG.
- Migration path from AIAV (new sensor) onto Phoenix.
