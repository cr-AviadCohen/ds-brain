---
title: Themis
type: system
tags: [system, wiki, ml-classifier, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, classifier]
related_projects: ["[[Infrastructure of Interest]]"]
related_systems: ["[[Behavior Clustering]]", "[[Campaign Assembler]]"]
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
last_updated: 2026-05-19
---

# Themis

> Multi-class ML classifier inside [[Infrastructure of Interest]] that scores domain observations as **benign / gray-benign / gray-malicious / malicious**. 90+ features, 6-model ensemble (NN, RF, KNN, SVC, …) with a meta-learner. Output drives both scoring weights and the conservative hard-filter ("Themis benign → excluded from detection, even if other signals fire").

## Owner / vendor

Internal SLR Labs system under [[Jose Manuel Martin Rodriguez]]. Co-developed with the broader IOI pipeline.

## Integration surface

- Input: enriched domain observations (post-collection, post-whitelist).
- Output: 4-class verdict + per-feature contributions consumed by the [[Infrastructure of Interest]] flag-scoring stage.
- Independent of the TLS-NLP binary classifier — the two verdicts are deliberately decoupled so a confident TLS verdict can survive a Themis disagreement and vice versa.

## Data flow

Collector → whitelist → enrichment ([[URL System]], passive DNS, WHOIS, Shodan, sandbox) → Themis features (90+) → 6 base models → meta-learner → 4-class label → flag scoring → OTX/USM dissemination.

## Current usage

- Production verdict for every observation that survives whitelisting in [[Infrastructure of Interest]].
- Hard filter: Themis benign / gray-benign verdicts are excluded from customer detection regardless of other signals (conservative posture — protect customers from false positives).
- Themis-malicious flag carries weight 0.3 in the suspiciousness score.

## Known issues

- Single-head ownership ([[Jose Manuel Martin Rodriguez]]) — model + feature engineering live in one head.
- 6-model + meta-learner stack is opaque to analysts; per-flag explanations rely on the orthogonal flag-scoring layer rather than Themis-native interpretability.

## Related entities

- Projects: [[Infrastructure of Interest]].
- People: [[Jose Manuel Martin Rodriguez]] (owner).
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- Training-data sourcing + refresh cadence — how are new labels obtained for benign vs. malicious domains?
- Drift monitoring — is there a regression test set + Themis-vs-ground-truth dashboard?
- Why the 6-model ensemble (vs. a single boosted tree)? Pure recall reasons or interpretability hedge?
