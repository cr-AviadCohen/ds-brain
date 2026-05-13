---
title: DS Team Takes Over Spider Labs Orphaned Projects
type: decision
tags: [decision, wiki]
date: 2026-05-06
deciders: ["[[Inbar Dekel]]", "[[Santiago Cortes Diaz]]", "[[Aviad Cohen]]"]
status: accepted
related_projects: ["[[Martin News Chatbot]]"]
related_systems: ["[[Alert Logic]]"]
last_updated: 2026-05-13
---

# DS Team Takes Over Spider Labs Orphaned Projects — 2026-05-06

## Context

At the 2026-05-06 DS team / Santi handover, Spider Labs (Santi, Jose, Inigo) and the incoming AI/DS team (Inbar, Aviad, Itamar, Guy) reviewed three Spider Labs projects orphaned by Hessam's departure: a Martin News OSINT chatbot POC, the Themis domain-risk scoring model, and the Infrastructure of Interest (IOI) infrastructure-tracking pipeline.

## Decision

The DS team takes over all three orphaned Spider Labs projects: (1) the Martin News OSINT chatbot, (2) the Themis domain-risk model, and (3) the Infrastructure of Interest (IOI) pipeline. Sequencing is also decided in the same session: start with the Martin News OSINT chatbot as the "low-hanging fruit" first project, defer Themis's full retraining-pipeline automation to the longer-term roadmap, and prioritise replacing IOI's static numeric flag weights with a trained ML weighting model.

## Why

Hessam's departure left these projects without an owner, and Spider Labs needs continuity on internal threat-intel capability. The DS team has the ML/agent expertise to (a) re-host the Martin News chatbot on its own orchestrator if it chooses, (b) build a labelled-data-driven ML weighting model for IOI, and (c) eventually automate Themis retraining against OTX-derived ground truth. The phasing reflects effort/impact: the chatbot is the cheapest first win, IOI weighting is highest immediate value, Themis automation is the heaviest engineering lift and can wait.

## Alternatives considered

- Leave the projects with Spider Labs and hire a dedicated replacement for Hessam — not pursued; the DS team has bandwidth and ML depth that fits the work.
- Take only the chatbot and decline IOI/Themis — rejected: Santi flagged IOI weighting as a high-priority ask, and Themis is the long-term path to retiring the 8-year-old Papillion model.

## Consequences

- The DS team owns the Martin News chatbot first and can keep AWS Bedrock Agent Core or migrate to its own orchestrator.
- The DS team must build the missing MCP endpoints connecting the chatbot to the separate DB holding older TIPR/CVE/APT/ransomware data.
- IOI campaign-clustering work begins in collaboration with [[Jose Manuel Martin Rodriguez]].
- Themis automation is deferred but remains a tracked future commitment.
- The Martin News chatbot, Themis, IOI, TIPR/Tipper, Papillion, and Mather need to be seeded as wiki project pages so this decision and its follow-ups can be properly back-linked.

## Open questions

- Which orchestration target wins for the chatbot — AWS Bedrock Agent Core or the DS team's own multi-agent orchestrator?
- What labelled benign/malicious dataset will train the IOI weighting model — does an OTX-derived label set have sufficient coverage?
- How much of [[Jose Manuel Martin Rodriguez]]'s time can the DS team count on for IOI campaign-clustering knowledge transfer?
