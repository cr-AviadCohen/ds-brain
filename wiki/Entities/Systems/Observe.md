---
title: Observe
type: system
tags: [system, wiki]
owner: Observe Inc (vendor)
vendor: Observe Inc
related_projects: ["[[UEBA]]", "[[IRCA Cloud]]"]
seeds:
  - INBOX/converted/data-science-main.md
  - raw/projects/Project - UEBA/Project UEBA.docx.md
  - raw/projects/Project - IRCA Cloud/Project IRCA Cloud.docx.md
last_updated: 2026-05-11
---

# Observe

> Observe-on-Snowflake (on AWS) — one of Cybereason's two current XDR data lakes (the other being Chronicle on GCP). Used by Data Science as the primary multi-vendor telemetry source for UEBA and IRCA Cloud.

## Owner / vendor

Observe Inc — running on Snowflake on AWS.

## Integration surface

- Per-region Observe workspaces: APAC (`131377279880.ap-1.observeinc.com`), EU (`111638659092.eu-1.observeinc.com`), US (`121530154444.observeinc.com`).
- Opal filters for selecting subsets of data.
- Unified Data Model (UDM) format for events.

## Data flow

Multi-vendor telemetry (Fortinet FortiGate Firewall, AWS CloudTrail, Cisco Firewall, MS Office 365, MS Azure Identity, etc.) → Observe → UDM-formatted events queried per-region by DS pipelines.

## Current usage

- [[UEBA]]: 30-day Fortinet FortiGate firewall data across 500 users, 4-hour intervals.
- [[IRCA Cloud]]: cloud event source via UDM-formatted feed; consumed after Opal filtering to manage volume.

## Known issues

- Limited support compared to Chronicle on GCP — missing crucial features such as IDM.
- Cost / feasibility uncertainty for some feature-extraction approaches inside Observe.

## Related entities

[[UEBA]], [[IRCA Cloud]], [[Snowflake]]

## Open questions

- Cost feasibility of richer per-user feature extraction in Observe.
- Migration path to Phoenix-based XDR (which would replace today's Observe/Chronicle XDR).
