---
title: Aviad and Phil intro
type: meeting
tags: [meeting, wiki]
date: 2026-04-27
participants: ["[[Aviad Cohen]]", "[[Phil Hay]]"]
related_projects: []
related_systems: ["[[Mail Marshal]]"]
related_decisions: ["[[2026-04-27 — Email Attachments as First ML Collaboration Target]]", "[[2026-04-27 — ML Outputs as Mail Marshal Scoring Inputs]]"]
source: raw/meetings/meeting_2026.04.27_aviad_phil.txt
last_updated: 2026-05-12
---

# Aviad and Phil intro — 2026-04-27

> Intro session between Aviad and Phil to scope potential ML/data-science collaboration around Mail Marshal phishing detection; landed on email attachments as the most likely first project.

## Decisions

- [[2026-04-27 — Email Attachments as First ML Collaboration Target]] — treat email attachments (currently rule-handled) as the most promising candidate first project for ML collaboration.
- [[2026-04-27 — ML Outputs as Mail Marshal Scoring Inputs]] — keep ML output as weighted scoring inputs into Mail Marshal rather than autonomous block actions; existing scoring model is the right integration surface.

## Action items

- [ ] Plan an in-depth follow-up technical session covering URL Deep, PageML, and Defense internals — [[Aviad Cohen]], [[Phil Hay]]
- [ ] Scope a data-provisioning and check-in plan before committing to any attachment-ML collaboration — [[Phil Hay]]

## Discussion notes

**Phil's team in scope.** Phil's group owns Mail Marshal, threat research, manual malware analysis, and security updates. Three production ML systems have been built over the last 5–6 years.

**Three core ML systems.** *URL Deep* is a deep learning model that tokenises URL strings and predicts "phishiness"; training data is sourced from intercepted phishing emails, Phishtank, and APWG. *PageML* is a traditional ML model that crawls URLs (following redirects), extracts ~120 HTML/URL features, and layers a Regex/Yara rules engine for FP mitigation — it consumes URL Deep's score as a feature and is overdue for a feature-set refresh. *Defense* is a structural-email model that scores headers and body to target attacker email-generation infrastructure rather than chasing content.

**Scoring model, not autonomous blocking.** Phil emphasised that no ML model blocks on its own — outputs feed a weighted scoring system inside Mail Marshal (example: a confident URL Deep verdict contributes ~22 points toward a ~60-point conviction threshold). Structural rules and threat indicators must also fire.

**Operational pain points.** The hardest part is not modelling but training-data plumbing: labelling, refreshing, evaluating "good vs bad" data, and proving a candidate model is better than the live one. The threat landscape has also moved from malicious attachments to phishing-link campaigns embedded in benign-looking PDFs or compromised SharePoint sites. Attachments are still handled effectively by rules + Yara + AV layers, including aggressive nested-unpacking.

**Team and collaboration.** Phil's core team: [[Lloyd Macrohon]] as ML glue between research and code, with [[Rodel Mendrez]], [[Karla Agregado]], and [[John Kevin Adriano]] each owning data and model upkeep for URL Deep, PageML, and Defense respectively. Phil is open to consulting with a research-oriented DS for fresh directions, but flagged that any project requires careful planning, data provisioning, and recurring check-ins.

## Open questions

- What dataset, label process, and ground-truth pipeline would be required to build an attachment ML model on top of Mail Marshal's existing unpacking layer?
- Mail Marshal as a system does not yet have a wiki page — flagged for follow-up project seeding.
- The internal `URL Deep`, `PageML`, and `Defense` models are not yet wiki projects — flagged for follow-up.
