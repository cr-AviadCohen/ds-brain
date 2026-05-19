---
title: 2026-05-14 — Infrastructure of Interest (SLR Brownbag)
type: source
tags: [source, wiki, source_type/meeting]
authors: ["[[Jose Manuel Martin Rodriguez]]", "[[Santiago Cortes Diaz]]"]
year: 2026
date: 2026-05-14
url: null
raw_path: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
last_updated: 2026-05-19
---

# 2026-05-14 — Infrastructure of Interest (SLR Brownbag)

> SLR Brownbag deep-dive by [[Jose Manuel Martin Rodriguez]] on the [[Infrastructure of Interest]] (IOI) proactive threat-infra pipeline. Hosted by [[Santiago Cortes Diaz]]. Pre-summarized note shipped with the raw transcript artifact.

## Summary

- Four-stage IOI pipeline: collection (10–11 collectors) → analysis/enrichment (internal + Shodan + 3 ML models) → flagging/scoring (~45 weighted flags) → dissemination + [[Campaign Assembler]].
- Scale: 1.5M+ stored observations, 5K–40K daily intake, 200–800 high-confidence malicious domains pushed daily, avg 40–120 day lead time vs. public attribution.
- ML stack: [[Themis]] (multi-class, 6-model ensemble + meta-learner), TLS-NLP binary classifier, [[Behavior Clustering]] (K-means on customer telemetry).
- Campaign Assembler: 5 clustering methodologies × 16 views, consensus ≥4 → solid cluster, 11-type taxonomy, 234 analyst-ready clusters in 45-day bootstrap.
- Strategic: [[Tipper]] UI bundles IOI + Sigma interop for SLR analysts. SSO rollout pending. DS team invited to help on clustering.

## Why we care

First canonical DS-brain record of the IOI architecture, scoring system, and Campaign Assembler. Direct collaboration ask from Jose to DS team on clustering — feeds the SLR/Spider Labs side of the 50/50 DS bandwidth split ([[2026-05-06 — 50-50 DS Bandwidth Split Phoenix and Spider Labs]]). Also names the new collectors / systems ([[BestWhois Collector]], [[CertStream Collector]], [[Argus Collector]], [[URL System]]) and the third-party confirmation orgs ([[Hunt.io]], [[Recorded Future]]).

## Cited from

- [[Infrastructure of Interest]]
- [[Tipper]]
- [[Themis]]
- [[Campaign Assembler]]
- [[Behavior Clustering]]
- [[BestWhois Collector]]
- [[CertStream Collector]]
- [[Argus Collector]]
- [[URL System]]
- [[Typosquatting Detection]]
- [[DGA Detection]]
- [[Supply Chain Attack Detection]]
- [[Hunt.io]]
- [[Recorded Future]]
- [[Jose Manuel Martin Rodriguez]]
- [[Santiago Cortes Diaz]]
- [[Aviad Cohen]]
- [[Itamar Hershko]]
- [[Nikita Kazymirskyi]]
- [[Shabtay Barel]]
- [[Alejandro Prada Nespral]]

## Open questions

- Exact list of all 11 collectors (source names 7 explicitly; "Mute" identity unclear — possibly a 3rd-party feed brand to confirm).
- 16-view breakdown for Campaign Assembler — only 5 methodologies named, 11 view variants unenumerated.
- Numerical weights per flag (only example weights given; full table not in this source).
