---
title: Behavior Clustering
type: system
tags: [system, wiki, ml-clustering, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, fleet-telemetry]
related_projects: ["[[Infrastructure of Interest]]"]
related_systems: ["[[Argus Collector]]", "[[USMA]]"]
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
last_updated: 2026-05-19
---

# Behavior Clustering

> Unsupervised K-means clustering inside [[Infrastructure of Interest]] that maps [[USMA]] customer-telemetry observations into time-series behavior profiles. Tells the pipeline whether a domain behaves like Google (massive, drop) vs. like an exponential supply-chain campaign (escalate).

## Owner / vendor

Internal SLR Labs system. Built on top of [[Argus Collector]] OpenSearch hunts of [[USMA]] telemetry.

## Integration surface

- Input: per-domain fleet-event time series (frequency, host count, customer count, day-over-day delta).
- Output: cluster assignment used both as a flag (e.g., *exponential* → strong [[Supply Chain Attack Detection]] signal) and as a hard filter (*massive* → drop).

## Cluster profiles

- **massive** — Google-like ubiquitous traffic → discard (too noisy).
- **professional services** — recurring B2B usage → benign-leaning.
- **legitimate anomaly** — bursty but explainable → defer.
- **exponential** — rapidly increasing fleet observations → potential supply-chain compromise → escalate.
- (other clusters listed in raw source).

## Current usage

- Production stage of [[Infrastructure of Interest]] pre-flagging.
- Drives the hard "noisy" filter: >100 fleet events OR >10 distinct customers → exclude from detection.
- Source of the supply-chain-attack signal in the flag-scoring layer.

## Known issues

- Static K-means parameters — drift in fleet composition may shift cluster boundaries.
- Cluster labels are domain-expert curated; new behaviors require manual taxonomy updates.

## Related entities

- Projects: [[Infrastructure of Interest]].
- Systems: [[Argus Collector]] (telemetry source), [[USMA]] (fleet substrate).
- Concepts: [[Supply Chain Attack Detection]].
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- Cluster-count selection — elbow / silhouette / hand-picked?
- Refresh cadence for K-means re-fit.
- Is there a parallel pipeline for IP-level behavior (or is everything domain-keyed)?
