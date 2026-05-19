---
title: Argus Collector
type: system
tags: [system, wiki, collector, fleet-telemetry, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, usm-customer-telemetry]
related_projects: ["[[Infrastructure of Interest]]"]
related_systems: ["[[USMA]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# Argus Collector

> Fleet-telemetry collector inside [[Infrastructure of Interest]]. Runs **OpenSearch hunting queries against [[USMA]] customer telemetry on a weekly cadence**. Exclusive moat — competitors cannot replicate this signal because they lack equivalent fleet visibility.

## Owner / vendor

Internal SLR Labs collector — taps the [[USMA]] OpenSearch backend.

## Integration surface

- Input: OpenSearch queries over [[USMA]] customer telemetry (weekly).
- Output: per-domain fleet observations (frequency, host count, customer count) feeding both the IOI flag-scoring stage and the [[Behavior Clustering]] K-means time-series.

## Strategic role

- Source of the "fleet prevalence" signal used as ground truth across IOI.
- Powers the conservative noisy-filter rule (>100 fleet events OR >10 customers → exclude from detection).
- Drives [[Behavior Clustering]] cluster assignment (massive / professional services / legitimate anomaly / exponential / …).
- The **moat** that makes IOI research output difficult for competitors to replicate.

## Current usage

- Production collector in [[Infrastructure of Interest]].
- Weekly cadence — slower than registration/cert streams but irreplaceable for telemetry grounding.

## Related entities

- Projects: [[Infrastructure of Interest]].
- Systems: [[USMA]] (substrate), [[Behavior Clustering]] (downstream consumer).
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- Will Argus extend to [[Phoenix]] fleet telemetry once XDR consolidation matures?
- Hunt-query catalogue — who curates queries and how often are they refreshed?
- Latency floor of weekly cadence — is there appetite for daily/hourly Argus?
