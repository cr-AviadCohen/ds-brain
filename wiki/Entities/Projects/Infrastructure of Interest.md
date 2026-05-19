---
title: Infrastructure of Interest
type: project
tags: [project, wiki, slr, threat-intel]
status: active
lead: "[[Jose Manuel Martin Rodriguez]]"
team: ["[[Santiago Cortes Diaz]]", "[[Alejandro Prada Nespral]]"]
org: "[[Labs]]"
parent_org: "[[LevelBlue]]"
started: pre-2025
systems: ["[[Themis]]", "[[Behavior Clustering]]", "[[Campaign Assembler]]", "[[BestWhois Collector]]", "[[CertStream Collector]]", "[[Argus Collector]]", "[[URL System]]", "[[OTX]]", "[[USMA]]", "[[Tipper]]"]
related_projects: ["[[Tipper]]", "[[Owlint-Sigma]]"]
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
last_updated: 2026-05-19
---

# Infrastructure of Interest (IOI)

> SLR Labs proactive threat-infrastructure pipeline. Identifies, contextualizes, and scores suspicious domains / IPs / TLS certificates **before** adversary campaigns go live. Surfaces high-confidence indicators to [[OTX]] + USM customer detection and bundles them into investigation-ready campaign objects via [[Campaign Assembler]]. Average lead time **40–120 days** ahead of public attribution.

## Goal

Give every SLR analyst a structured framework for **proactive research** grounded in [[Cybereason]] / [[LevelBlue]] fleet telemetry — replacing reactive (post-incident) or opportunistic ([[VirusTotal]]-clicking) workflows. Output: early customer protections + threat-intel reports that competitors cannot replicate because they lack equivalent visibility.

## Approach

Four-stage pipeline:

1. **Collection** — 10–11 independent collectors (one dark ≠ pipeline break); ~30% noise dropped at whitelisting. Each observation tagged with collector profile + query for traceability. Observations retained (never overwritten) — yields a time-series of how a domain's score evolves.
2. **Analysis & Enrichment** — internal: [[URL System]], passive DNS, historic WHOIS, HML ([[Trustwave]]), Kape/Cuckoo sandbox (YARA + network sigs). External: Shodan (open ports, banners, TLS). ML: [[Themis]] multi-class + TLS-NLP binary classifier + [[Behavior Clustering]] K-means.
3. **Flagging & Scoring** — ~45 suspiciousness flags, each weighted (WHOIS-recent low, high-entropy 0.2, Themis-malicious 0.3, multi-high-score HTML-match higher). Sum = score. High-confidence → OTX + USM; medium → OTX only; below → drop. Hard filters: Themis-benign excluded; >100 events OR >10 customers → too noisy, excluded.
4. **Dissemination + Campaign Assembler** — 5 OTX pulse types by profile (Phishing / C2 / Stealer / etc.). [[Campaign Assembler]] runs 5 clustering methodologies × 16 views; consensus ≥4 → solid cluster; output is 5 evidence dimensions + text templates + suggested investigation steps; 11-type taxonomy separates analyst-ready from noise.

## Status

active — operating in production with 1.5M+ stored observations and 567 independently confirmed-malicious domains. New collector ([[CertStream Collector]]) in progress under [[Alejandro Prada Nespral]]. Tipper SSO rollout to SLR + DS team in progress.

## Numbers

- 1.5M+ stored domain observations; 11 active collectors; ~45 weighted flags.
- 5K–40K daily intake, ~70% pass whitelist, 200–800 high-confidence/day to OTX/USM.
- 567 independently confirmed malicious domains to date.
- Lead time vs. public attribution: avg 40–120 days, max several months (177-day record).
- Campaign Assembler 45-day bootstrap: 774 consensus clusters, 234 analyst-ready, ~0.6 observation-to-cluster funnel.

## Collectors

| Collector | Source | Purpose |
|---|---|---|
| [[BestWhois Collector]] | New domain registrations (3×/week) | Earliest possible signal |
| [[CertStream Collector]] | New TLS certs (WIP, [[Alejandro Prada Nespral]]) | Cert-driven discovery |
| [[Argus Collector]] | USM customer telemetry via OpenSearch (weekly) | Fleet visibility — exclusive moat |
| Camry | 3rd party | External intel |
| OTX (community) | Community pulses | Crowd-sourced |
| Mute | Newly added | 3rd-party feed |
| Phishing feeds | Various | Phishing-specific |

## ML models

- [[Themis]] — multi-class (benign / gray-benign / gray-malicious / malicious); 90+ features; ensemble of 6 models (NN, RF, KNN, SVC, …) + meta-learner.
- **TLS-NLP classifier** — binary, NLP over TLS certificate fields; independent of Themis → independent verdict.
- [[Behavior Clustering]] — K-means on USM customer telemetry; clusters incl. *massive* (Google etc. → discard), *professional services*, *legitimate anomaly*, *exponential* (← [[Supply Chain Attack Detection]] signal).

## Hard filters (conservative posture)

- Themis says benign / gray-benign → excluded from detection (still stored).
- Domain on >100 fleet events OR >10 customers → too noisy → excluded.
- Rationale: protect customers from false positives even at cost of recall.

## Dissemination

- 5 OTX pulses by profile (Phishing / C2 / Stealer / etc.) — driven by collector profile+query tags so analysts get immediate context.
- Only high-confidence → USM customer detection.
- Pulses retained 3 months; rolled off if no new sightings (suspicious infra usually persists).

## Success stories

- 6-year Chinese iGaming affiliate fraud — impersonating CN casino brands via thousands of rotating redirectors; seeded from three short `.cc` domains; first + second-stage payloads recovered.
- SMS-thief — fake Google Store app targeting Brazil + India; first-stage recovered; attribution WIP.
- Microsoft 365 credential phishing hub — kit served across domain set; seeded from IOI observations.
- Lead-time wins: [[Hunt.io]] confirmed an IOI-flagged domain 7 months later; [[Recorded Future]] confirmed another after 177 days.

## DS-team collaboration

[[Jose Manuel Martin Rodriguez]] requested DS team help refining [[Campaign Assembler]] clustering. [[Aviad Cohen]] agreed (2026-05-14). LLM campaign-ranking layer planned but kept off per-observation hot path due to cost — candidate DS scope. See [[2026-05-06 — 50-50 DS Bandwidth Split Phoenix and Spider Labs]].

## Risks

- Tipper UI SSO rollout to SLR + DS team still pending — analyst access blocker.
- Domain-knowledge dependency on Jose: rule weights + flag definitions concentrate domain expertise in one head.
- LLM cost discipline: any AI augmentation must stay off the per-observation hot path.

## Related entities

- People: [[Jose Manuel Martin Rodriguez]] (lead), [[Santiago Cortes Diaz]] (strategy), [[Alejandro Prada Nespral]] (CertStream WIP), [[Aviad Cohen]] (DS collaboration), [[Itamar Hershko]] (Owlint-Sigma overlap).
- Systems: [[Tipper]] (analyst surface), [[OTX]] (pulse target), [[USMA]] (telemetry source via [[Argus Collector]]).
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- Applicability to [[Phoenix]] data plane — flagged for offline discussion.
- Full enumeration of the 16 Campaign Assembler views (only 5 methodologies named).
- Mute collector — exact upstream vendor / feed identity.
- DS-team Campaign Assembler scope: clustering review only, or net-new methodologies?
- LLM campaign-ranking layer ownership: SLR or DS?
- Sigma interoperability surface inside Tipper alongside IOI — interaction model when both are live.
