---
title: Supply Chain Attack Detection
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[Infrastructure of Interest]]"]
related_systems: ["[[Behavior Clustering]]", "[[Argus Collector]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# Supply Chain Attack Detection

> Detection of malicious infrastructure that rides a legitimate distribution channel (compromised npm/pip package, CDN, vendor update) — visible as **exponentially growing fleet usage** of a previously unknown domain.

## What it is

Inside [[Infrastructure of Interest]] / [[Behavior Clustering]], the **exponential** cluster captures domains whose fleet-event count rises sharply over a short window — distinct from steady-state legitimate traffic (Google → *massive* cluster) and from one-off anomalies (→ *legitimate anomaly* cluster). Exponential growth with no benign provenance is a strong supply-chain-compromise signal.

## Why we care

- Supply-chain attacks defeat per-host endpoint logic because the malicious binary arrives via a trusted update channel — fleet-prevalence ML is one of the few defenses that scales.
- Hard to replicate externally: needs [[Argus Collector]] / [[USMA]] fleet telemetry (or [[Phoenix]] equivalent in future) to detect.
- Direct overlap with [[identity-correlation-as-unsolved-hard-problem]] — once a supply-chain compromise propagates, identity/asset correlation tells you the blast radius.

## Manifestations

- 2026-05-14 — [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]] — Jose Manuel named the *exponential* cluster as the supply-chain-attack signal inside Behavior Clustering.

## Open questions

- Minimum fleet size + customer count for the exponential signal to be reliable.
- Does the same detector translate cleanly to [[Phoenix]] telemetry?
- Coordination with [[Smart Asset Correlation]] blast-radius logic on confirmed supply-chain incidents.
