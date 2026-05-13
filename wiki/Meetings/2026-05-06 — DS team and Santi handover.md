---
title: DS team and Santi handover
type: meeting
tags: [meeting, wiki]
date: 2026-05-06
participants: ["[[Santiago Cortes Diaz]]", "[[Jose Manuel Martin Rodriguez]]", "[[Inigo Lopez-Barranco]]", "[[Inbar Dekel]]", "[[Aviad Cohen]]", "[[Itamar Hershko]]", "[[Guy Kassorla]]"]
related_projects: []
related_decisions: ["[[2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects]]", "[[2026-05-06 — 50-50 DS Bandwidth Split Phoenix and Spider Labs]]"]
source: raw/meetings/meeting_2026.05.06_DS_team_and_santi.txt
last_updated: 2026-05-11
---

# DS team and Santi handover — 2026-05-06

> Strategy + handover session between Spider Labs Threat Intelligence (Santi, Jose, Inigo) and the incoming AI/DS team (Inbar, Aviad, Itamar, Guy), taking over three orphaned projects after Hessam's departure: a Martin News OSINT chatbot, the Themis domain-risk model, and the IOI infrastructure-tracking pipeline.

## Decisions

- [[2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects]] — DS team takes over Martin News OSINT chatbot, Themis domain-risk model, and IOI pipeline; start with the chatbot, defer Themis automation, prioritise IOI ML weighting.
- [[2026-05-06 — 50-50 DS Bandwidth Split Phoenix and Spider Labs]] — approximate 50/50 split of DS-team bandwidth with at least one high-priority internal project always in motion.

## Action items

- [ ] Pick up the Martin News OSINT chatbot POC, decide whether to keep AWS Bedrock Agent Core or migrate to the team's own orchestrator — [[Itamar Hershko]], [[Aviad Cohen]]
- [ ] Build the missing MCP endpoints connecting the chatbot to the separate database holding older TIPR data, CVEs, APTs, and ransomware — DS team
- [ ] Design a trained ML weighting model to replace IOI's static numeric flags against the 1.2 publish threshold — DS team
- [ ] Implement a more mature, AI-driven clustering approach for IOI's daily ~20,000 domain observations (campaign assembler) — DS team, in collaboration with [[Jose Manuel Martin Rodriguez]]
- [ ] Plan a longer-term automated retraining pipeline for Themis benchmarked against OTX-pulse malicious-domain ground truth — DS team (deferred)

## Discussion notes

**Spider Labs context.** Santi framed Spider Labs as its own first customer for threat intelligence — building tooling to increase capability and speed, and to bridge silos between departments. Two main platforms anchor that work: **TIPR/TIPPER** (internal pipeline ingesting 50–70 reports/day, fuelling detection writing) and **Martin News** (external-facing portal that consumes TIPR data to surface customised intel to managed services, sales, and hunters).

**Project 1 — Martin News OSINT chatbot.** A POC built by the previous data scientist (Hessam, no current wiki page) answers analyst questions about trending threats, CVEs, vulnerabilities. Architecture: AWS Bedrock Agent Core runtime, Anthropic Haiku for routing, AWS Bedrock knowledge base (managed vector store / RAG) covering the last 3 months of TIPR news. For older data and CVE/APT/ransomware lookups, planned MCP endpoints to a separate DB exist but are not yet built. Persistent memory across sessions and "Lambda tools" (static Python functions) for actions like URL downloads are already wired in. The DS team can keep the AWS stack or migrate to their own orchestrated agent system. This was deemed the "low-hanging fruit" — first project on the DS-team plate.

**Project 2 — Themis (domain risk scoring).** Themis is a production stacking ensemble (XGBoost + neural networks + random forest) feeding a meta-learner, classifying domains as benign / gray benign / gray malicious / malicious. It was meant to replace an 8-year-old model (`Papillion`), but the legacy is still live because Themis occasionally flags well-known benign domains (e.g. Google) as malicious. Santi wants an automated retraining pipeline benchmarked against known-malicious OTX pulses so Themis can be refreshed every few months and fully retire Papillion. The DS team flagged this as a heavier engineering lift and recommended deferring it.

**Project 3 — Infrastructure of Interest (IOI).** IOI flags suspicious domains before they go active in campaigns, monitoring early signals like fresh `whois` registrations. Observations are enriched with ~50 boolean flags from systems like Themis and `Mather` (TLS-cert binary classifier). Today those flags are combined via static numeric weights — a score above 1.2 publishes the domain as a malicious IOC on OTX. Santi's high-priority ask is to replace those static values with a trained ML weighting model using labelled benign/malicious datasets. Separately, IOI processes ~20,000 domain observations daily, and Jose currently clusters them into "campaigns" using legacy methods over Shodan, DNS, and customer-observation features — Spider Labs wants a more mature, AI-driven clustering approach so the research team can prioritise the most impactful campaigns for PR-grade deep-dive research.

**Resource allocation.** Santi pushed for a guaranteed slice of DS-team time on internal TI research, citing the risk of being consumed entirely by platform PMs who are "always in a hurry". [[Inbar Dekel]] agreed to a roughly 50/50 split between [[Phoenix]] and Spider Labs internal projects, with elasticity for urgent platform needs.

## Open questions

- Which orchestration target wins for the chatbot — keep AWS Bedrock Agent Core, or migrate into the DS team's own multi-agent orchestrator?
- What labelled benign/malicious dataset will train the IOI weighting model — does an OTX-derived label set have sufficient coverage?
- How much of [[Jose Manuel Martin Rodriguez]]'s time can the DS team count on for IOI campaign-clustering knowledge transfer?
- Hessam (former DS team member) is referenced but has no Entities/People page — flagged.
- The internal projects `TIPR / Tipper`, `Martin News`, `Themis`, `Papillion`, `Mather`, and `Infrastructure of Interest` are not yet wiki project pages — flagged for follow-up project seeding.
