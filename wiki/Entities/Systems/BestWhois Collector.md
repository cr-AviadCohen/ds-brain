---
title: BestWhois Collector
type: system
tags: [system, wiki, collector, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, domain-registration]
related_projects: ["[[Infrastructure of Interest]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# BestWhois Collector

> Earliest-signal collector inside [[Infrastructure of Interest]]. Ingests **new domain registrations** 3×/week and runs three filter sub-modules to surface candidates worth full analysis.

## Owner / vendor

Internal SLR Labs collector — part of the IOI pipeline.

## Sub-modules

- **Fuzzy Jaro-Winkler** — string-edit-distance match against a known-brand list. Catches typosquats of any length — see [[Typosquatting Detection]].
- **Semantic similarity** — embedding-model match against known brands (catches lookalikes like `gmial.*`, `blackhorizon.online` that fuzzy misses).
- **Entropy + suspicious-TLD filter** — high-entropy random-looking labels + suspicious TLDs, especially when registered in bursts → DGA candidates ([[DGA Detection]]).

## Integration surface

- Input: WHOIS feed of new domain registrations (3× weekly).
- Output: candidate observations tagged with sub-module provenance, fed into the IOI whitelist + enrichment + Themis pipeline.

## Current usage

- One of the 10–11 independent IOI collectors (loss of any single collector ≠ pipeline break).
- Provides the earliest-possible signal in the pipeline (pre-resolution, pre-deployment).

## Related entities

- Projects: [[Infrastructure of Interest]].
- Concepts: [[Typosquatting Detection]], [[DGA Detection]].
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- WHOIS source vendor / feed — single source or aggregator?
- Brand-list maintenance cadence + ownership.
- Embedding model used for semantic similarity (in-house vs. off-the-shelf).
