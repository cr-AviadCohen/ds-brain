---
title: Infrastructure of Interest (SLR Brownbag)
type: meeting
tags: [meeting, wiki, slr, threat-intel]
date: 2026-05-14
duration: 43m 59s
series: SLR Brownbag Session Series
presenter: "[[Jose Manuel Martin Rodriguez]]"
host: "[[Santiago Cortes Diaz]]"
participants: ["[[Santiago Cortes Diaz]]", "[[Jose Manuel Martin Rodriguez]]", "[[Aviad Cohen]]", "[[Itamar Hershko]]", "[[Nikita Kazymirskyi]]", "[[Shabtay Barel]]"]
related_projects: ["[[Infrastructure of Interest]]", "[[Tipper]]"]
related_systems: ["[[Themis]]", "[[Campaign Assembler]]", "[[Behavior Clustering]]", "[[BestWhois Collector]]", "[[CertStream Collector]]", "[[Argus Collector]]", "[[URL System]]", "[[Tipper]]", "[[OTX]]", "[[USMA]]"]
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
last_updated: 2026-05-19
---

# Infrastructure of Interest (SLR Brownbag) — 2026-05-14

> [[Jose Manuel Martin Rodriguez]] deep-dive on [[Infrastructure of Interest]] (IOI): four-stage proactive threat-infra pipeline (collection → enrichment → ML flagging → dissemination + Campaign Assembler). 1.5M+ stored domain observations, 5K–40K daily intake, 200–800 high-confidence malicious domains pushed daily, avg **40–120 day lead time** vs. public attribution. [[Santiago Cortes Diaz]] framed IOI as the SLR team's proactive-research framework (replacing reactive/opportunistic workflows). [[Aviad Cohen]] offered DS team help on clustering. Tipper UI SSO rollout in progress.

## Pipeline (four stages)

1. **Collection** — 10–11 independent collectors (one dark ≠ pipeline break); ~30% noise filtered at whitelisting. Collectors include [[BestWhois Collector]], [[CertStream Collector]] (WIP, [[Alejandro Prada Nespral]]), Camry, OTX, Mute, phishing feeds, [[Argus Collector]] (USM telemetry via OpenSearch — exclusive moat). Observations retained (never overwritten) → time-series score evolution.
2. **Analysis & Enrichment** — internal: [[URL System]], passive DNS, historic WHOIS, HML (from [[Trustwave]] post-merger), Kape/Cuckoo sandbox. External: Shodan IP scans. ML: [[Themis]] multi-class (90+ features, 6-model ensemble + meta-learner), TLS-NLP binary classifier (independent of Themis), [[Behavior Clustering]] (K-means on fleet telemetry).
3. **Flagging & Scoring** — ~45 weighted suspiciousness flags → summed score → thresholds: high-confidence → [[OTX]] + USM customer detection; medium → OTX only; below → drop. Hard filters: Themis-benign excluded; >100 events OR >10 customers → too noisy, excluded.
4. **Dissemination + [[Campaign Assembler]]** — 5 pulse types (Phishing / C2 / Stealer / etc.) by collector profile+query tags. Campaign Assembler runs 5 clustering methodologies × 16 views; consensus ≥4 views → solid cluster. Output: 5 evidence dimensions + text templates (no LLM on hot path due to cost) + suggested investigation steps. 11-cluster taxonomy distinguishes analyst-ready vs. emerging vs. noise.

## Numbers

- 1.5M+ stored domain observations; 11 active collectors.
- 5K–40K daily intake, ~70% pass whitelist, **200–800 high-confidence/day**.
- **567** independently confirmed-malicious domains to date.
- Avg lead time **40–120 days**; max several months (e.g., 177 days vs. Recorded Future confirmation).
- 45-day Campaign Assembler bootstrap: 774 consensus clusters, 234 analyst-ready.

## Success stories

- Six-year Chinese iGaming affiliate fraud impersonating CN casino brands via thousands of rotating redirectors — seeded from three short `.cc` domains.
- SMS-thief malware via fake Google Store app targeting Brazil + India.
- Microsoft 365 credential phishing hub.
- Domain seen Sep 2025 → confirmed by [[Hunt.io]] Apr 2026; another seen Aug 2025 → confirmed by [[Recorded Future]] Feb 2026 (177-day lead).

## Strategic framing ([[Santiago Cortes Diaz]])

SLR + broader InfoSec community ≈ reactive (post-IR) or opportunistic (VT clicking). IOI = structured framework for **proactive research** grounded in [[Cybereason]] + [[LevelBlue]] fleet visibility — research output unique and hard for competitors to replicate. Surfaces via [[Tipper]] UI (analyst platform); complements MartineNews (sales/MVR overview — separate from [[Martin News Chatbot]]). Goal: any analyst opens Tipper, picks a campaign, within 2h either drops or develops a lead.

## Action items

- [ ] IT / [[LevelBlue]] — finalize Tipper SSO access for SLR + DS team.
- [ ] [[Jose Manuel Martin Rodriguez]] — onboard DS team to IOI once UI access lands; share clustering details for collaboration.
- [ ] [[Aviad Cohen]] / DS team — engage on Campaign Assembler clustering review + improvements when invited.
- [ ] [[Santiago Cortes Diaz]] — explore IOI applicability to [[Phoenix]] (offline).
- [ ] [[Alejandro Prada Nespral]] — finish [[CertStream Collector]] (in progress).

## Strategic implications

- DS-team collaboration surface opened on Campaign Assembler clustering — direct request from Jose.
- IOI + Tipper rollout overlaps with [[Owlint-Sigma]] Tipper-collaboration track ([[Itamar Hershko]]).
- Reinforces [[Tipper]] as the SLR analyst surface bundling both IOI and Sigma interop.
- AI/LLM opportunity flagged: Jose plans an LLM scoring layer to rank "which campaigns to investigate first" (kept off per-observation hot path due to cost).

## Open questions

- Applicability of IOI to [[Phoenix]] data plane — Santi flagged offline.
- DS-team scope on clustering — review only, or net-new methodologies?
- Tipper output schema / API contract DS code can pin against.
- Will the planned LLM campaign-ranking layer be a DS-team build or stay inside SLR?
- Sigma integration: Tipper UI will bundle Sigma solution (per [[2026-05-07 — Sigma Interoperability brownbag]]) alongside IOI — interaction model?
