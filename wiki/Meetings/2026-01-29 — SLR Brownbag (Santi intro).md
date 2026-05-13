---
title: SLR Brownbag — Santi intro
type: meeting
tags: [meeting, wiki]
date: 2026-01-29
participants: ["[[Santiago Cortes Diaz]]"]
related_projects: ["[[AIDRA]]", "[[Owlint-Sigma]]"]
related_decisions: []
source: raw/meetings/meeting_2026-01-29_Santi
last_updated: 2026-05-11
---

# SLR Brownbag — Santi intro — 2026-01-29

> Kick-off SLR Labs introduction inside the newly formed Level Blue org — Santi walks the wider group through SLR's structure, tooling, intelligence pipeline, and the strategic shift from tracking APT actors to tracking payloads.

## Decisions

- Adopt cross-functional brownbag series as the primary channel for breaking silos between AT&T Cybersecurity, Trustwave, SpiderLabs, and Alert Logic.
- Continue shifting threat tracking focus from APT actors to payload infrastructure (Cobalt Strike, info stealers, initial access brokers) given the SMB-heavy customer base.
- Provision Premium OTX access to all Level Blue members so internal teams can consume private pulses.
- Launch a weekly Threat Intel Summit to unify the threat-intel processes across the four/five legacy companies now inside Level Blue.

## Action items

- [ ] Provision OTX Premium accounts for cross-org members — [[Santiago Cortes Diaz]]
- [ ] Schedule follow-up brownbag deep dive on the IDRA / AIDRA AI/LLM malware analysis module — [[Santiago Cortes Diaz]]
- [ ] Schedule follow-up brownbag from the legacy Trustwave MDR AI research team — [[Santiago Cortes Diaz]]

## Discussion notes

**SLR Labs structure.** Santi framed SLR Labs (origin: AlienVault) as three pillars: Detection Engineering for USM Anywhere, Threat Intelligence Group, and an Engineering & Data Science group that runs the backend pipelines feeding OTX (Open Threat Exchange).

**Intelligence pipeline scale.** The team translates OSINT reports into OTX "Pulses" and Jira detection tickets, exchanges ~50,000 malware samples/day with Hybrid Analysis, Any.Run, and Emerging Threats (using a Cuckoo/Cape fork extended for Linux and IoT), and processes ~300,000 daily Whois records plus passive DNS, malicious URLs, and TLS certificates.

**USM Anywhere & detection philosophy.** USM Anywhere correlates events across ~800 integrations and surfaces TTPs rather than atomic alerts. To control alert fatigue, alarms split into "Contextual" (enrichment-only) vs "Investigation Leads" (analyst-actionable). Detections follow a strict "Test as Code" philosophy with peer review before dissemination.

**Proprietary tooling.** Santi walked through several internal capabilities: **Tipper** (LLM pipeline for OSINT triage, dedup, and semi-automated OTX pulse / Jira ticket creation), **Martin News** (internal knowledge DB for threat briefings and leadership-facing PDFs), **Sauron** (Whois + DNS + IP geo correlation for malicious infrastructure), and an OTX domain scoring stack moving from `Rat feeder` to a new model called **Themis**.

**Strategic shift — payloads over actors.** Because SLR customers are mostly SMBs (rarely targeted by state actors), the team now tracks payload infrastructure. Monitoring infra that supports Cobalt Strike beacons, info stealers, and initial-access brokers gives earlier kill-chain visibility, often before the actual campaign launches.

**In-flight initiatives.** Infrastructure of Interest (IoI) — fleet-wide IOC herd-immunity flow; CVE management combining CVSS with exploit availability and ransomware-usage signals; Behavioral clustering of malicious infra; and a conceptual YARA memory-hunting effort that targets Java-based malware via on-device caches to dodge cloud bandwidth costs.

## Open questions

- How will OTX Premium provisioning be staged across the merged org?
- What is the governance model for the new weekly Threat Intel Summit?
- Will the legacy Trustwave MDR AI research stack be integrated with SLR's stack, kept separate, or consolidated under Level Blue?
- Note: a presenter referenced only as "Se" (host) could not be resolved to an existing People page — left without wikilink.
