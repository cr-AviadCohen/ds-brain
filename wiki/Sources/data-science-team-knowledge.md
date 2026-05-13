---
title: DS Team — General Knowledge & Projects Notion Doc
type: source
tags: [source, wiki, source_type/deck]
authors: [Data Science Team]
year: 2026
raw_path: raw/data_science_drive/data-science-main.md
last_updated: 2026-05-11
---

# DS Team — General Knowledge & Projects Notion Doc

> Internal DS-team Notion-style doc that bundles a stack overview (sensor + backend + XDR + Azure AI) with the Q2 project tracker.

## Summary

- **Sensor stack:** [[Core]] (legacy, graph-based, RAM-resident Transparency, expensive) vs new [[AIAV]] (event-based, cheaper, not yet deployed — gated on full [[Phoenix]] rollout).
- **Detection engines on Core sensor:** VFP, VPP, BEP, PRP, NGAV, BDP, BDP-AI, Fileless (PowerShell / .NET / VBScript / JavaScript), legacy canary-based Anti-Ransomware, BitDefender AV engine.
- **Backend:** Core = Transparency (in-RAM graph DB) + Perspective (orchestrates Transparency + UI + API). [[Phoenix]] is multi-tenant, disk-based, faster, built on [[Redpanda]] (Kafka-compatible streaming) and [[ClickHouse]] (analytics DB).
- **XDR backends:** [[Chronicle]] on GCP (full feature suite incl. IDM, costly) and [[Observe]] on Snowflake/AWS (limited, missing IDM). New direction: XDR over [[Phoenix]] via [[XIS]] to ingest 3rd-party logs into the Phoenix schema.
- **Azure AI:** subscription `CR-AI` (`7663b00e-8f86-4f1f-a4ac-9bb724c220f7`). Access requests via [[Shoshana Avni]]. Model deploys via [[Nitzan Milchin]] (and Shoshana). Israel integrator: Aztek (`asaf@aztek.co.il`). Quota-increase justification template captured for repeat use.
- **Internal system:** [[Sage]] = daily VirusTotal downloader.
- **Q2 project tracker** lists every active DS workstream with status, platform (Core / Phoenix / Agnostic), owner, contact, priority, Jira ticket, comments. Engineering contact [[Ortal Keizman]] covers most Phoenix-bound projects. Priority sign-off is "TBD with [[Ziv Mador]]".

## Why we care

This doc is the team's internal cheat-sheet — single page that defines what the DS team works on, who owns each workstream, what platform each runs on, and how the platform itself fits together. Most Entity pages here (Systems, Projects, People) draw their context fields from this source.

## Cited from

(Append-only. Wikilink per citing page.)

- [[Core]]
- [[Phoenix]]
- [[Azure AI Foundry]]
- [[Sage]]
- [[AIAV]]
- [[Chronicle]]
- [[Redpanda]]
- [[ClickHouse]]
- [[XIS]]
- [[Fusion 2]]
- [[Rules Quality]]
- [[Smart Asset Correlation]]
- [[XDR Correlation for Phoenix]]
- [[META]]
- [[NGAV]]
- [[AI Assistant]]
- [[IRCA]]
- [[AIDRA]]
- [[UEBA]]
- [[Incident Investigation (for Fusion 2)]]
- [[Owlint-Sigma]]
- [[Active Focus]]

## Open questions

- Q2 priority list — sign-off from [[Ziv Mador]] still pending per the tracker.
- Several projects flagged "To Be Defined" (Rules Quality, Smart Asset Correlation, XDR Correlation for Phoenix, Incident Investigation for Fusion 2) — scoping work outstanding.

#source #data-science #cybereason
