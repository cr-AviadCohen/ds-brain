---
title: Aviad and Pawel intro
type: meeting
tags: [meeting, wiki]
date: 2026-04-30
participants: ["[[Aviad Cohen]]", "[[Pawel Knapczyk]]"]
related_projects: ["[[Hunter]]"]
related_decisions: ["[[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]]"]
related_systems: ["[[Alert Logic]]"]
source: raw/meetings/meeting_2026.04.30_aviad_pawel.txt
last_updated: 2026-05-12
---

# Aviad and Pawel intro — 2026-04-30

> Intro between Aviad and Pawel covering Pawel's MTR background, shared identity-management roadblocks for cross-vendor correlation, and concrete near-term collaboration opportunities on Hunter, IDS-signature automation, and the Alert Logic ML compliance pipeline.

## Decisions

- [[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]] — replace the single-prompt design with an agentic, validated workflow for Hunter-driven Suricata IDS rule generation.
- Plan to graft Pawel's tools (Hunter, IDS-signature generation) into Aviad's multi-agent orchestrator once VPN/access is unblocked. (intent, pending unblock)
- Recommend Cursor as the standard coding-assistant tool for Pawel's team (already heavy on [[Itamar Hershko]]'s side). (tooling recommendation)
- Treat the Alert Logic compliance ML pipeline as a candidate project for the DS team to take over or improve. (candidate, not yet committed)

## Action items

- [ ] Resolve VPN/access so Pawel's tools can integrate with Aviad's orchestrator — [[Pawel Knapczyk]]
- [ ] Share the multi-agent AI assistant architecture with Pawel — [[Aviad Cohen]]
- [ ] Aviad to attend Pawel's upcoming brownbag on the Alert Logic ML pipeline — [[Aviad Cohen]]
- [ ] Push Pawel's Cursor license through — [[Pawel Knapczyk]]
- [ ] Prototype an agentic, validated workflow for Hunter-driven Suricata IDS rule generation (instead of single-prompt) — [[Aviad Cohen]], [[Pawel Knapczyk]]

## Discussion notes

**Pawel's background.** 8 years at ESET on reverse engineering, generic malware detections, and early ML classification (~2014); Acronis on ransomware behavioural detection and ML feature-extraction over compiled C / obfuscation; ABB as a hands-on threat hunter dealing with IoT-pivot intrusions on factory networks; and 4 years at Trustwave leading the Managed Threat Research (MTR) team, including detection optimisation for Fusion (which had a fragile detection engine where badly ordered rules could crash the stack) and high-profile threat-intel write-ups on Sandworm wiper attacks against Ukrainian telecom/water infrastructure.

**Shared roadblock — identity management.** Pawel previously led an AI effort called "Correlate ML" that tried to correlate cross-vendor threat data over time using pivot fields (IPs, usernames). It stalled because there is no unified Identity Management across ~4,000 clients. Aviad strongly resonated — the same identity-resolution gap is currently blocking attack-story correlation on the [[Phoenix]] XDR project.

**Current AI projects on Pawel's side.** [[Hunter]] is an internal GenAI tool (Claude-based) used by analysts to query Fusion; main pain is prompt optimisation to keep the model from hallucinating IDs or faking VirusTotal calls. Pawel's team also drives [[Hunter]] via API to auto-generate Suricata IDS rules from vulnerability inputs like Nuclei templates — Aviad proposed replacing the single-prompt design with an agentic workflow that validates and double-checks LLM output before surfacing the signature.

**Tooling.** Pawel is currently using the Claude web UI and waiting on a Cursor license. Aviad recommended Cursor strongly, citing how [[Itamar Hershko]] uses it heavily to accelerate development.

**Next steps & opportunities.** Aviad proposed sharing the team's multi-agent assistant architecture so Claude can dynamically route Pawel's tasks to the right agents. Pawel invited Aviad to an upcoming brownbag on Alert Logic's ML pipeline for compliance log review — an autonomous pipeline that hasn't been tuned in over a year. There are higher-level discussions (involving [[Ziv Mador]] and [[Keith Ibarguen]]) about integrating that pipeline into [[Phoenix]], which could become a natural intake project for the DS team.

## Open questions

- What is the right scope and ownership boundary if the DS team takes over the Alert Logic ML pipeline integration into Phoenix?
- How quickly can VPN/access be resolved to enable the orchestrator hookup?
- "Correlate ML" is not currently a wiki project page — flagged for follow-up.
