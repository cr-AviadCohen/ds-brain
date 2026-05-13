---
title: Aviad and Santi intro
type: meeting
tags: [meeting, wiki]
date: 2026-04-30
participants: ["[[Aviad Cohen]]", "[[Santiago Cortes Diaz]]"]
related_projects: ["[[Owlint-Sigma]]"]
related_decisions: []
source: raw/meetings/meeting_2026.04.30_aviad_santi.txt
last_updated: 2026-05-11
---

# Aviad and Santi intro — 2026-04-30

> First 1:1 between Aviad and Santi to align on ML/GenAI in threat intelligence — landed on a follow-up broader session next week with Inbar's team and Jose, anchored on Santi's three core projects (Sigma Pipeline, Tipper, Infrastructure of Interest).

## Decisions

- Schedule a broader cross-team session next week with [[Inbar Dekel]]'s team and [[Jose Manuel Martin Rodriguez]] — 20 minutes of high-level overview + 20 minutes deep dive into the Infrastructure of Interest data.
- Endorse the working principle that PMs define business problems, not technical solutions, and reserve dedicated engineering bandwidth for internal capability improvements independent of product roadmaps.

## Action items

- [ ] Schedule the broader follow-up with Inbar's team and Jose — [[Santiago Cortes Diaz]], [[Aviad Cohen]] — due 2026-05-06
- [ ] Prepare a 20-min overview of Sigma Pipeline, Tipper, and Infrastructure of Interest for the broader session — [[Santiago Cortes Diaz]]
- [ ] Prepare a 20-min IOI data deep dive for the broader session — [[Jose Manuel Martin Rodriguez]]

## Discussion notes

**Working philosophy.** Santi pushed a clear PM/engineering separation: PMs frame the business problem, engineers choose the technical solution. He used the "mirrors in slow elevators" and "pencil-vs-anti-gravity-pen" metaphors to argue for simple, creative solutions over complex engineering. He also advocated for protecting a fixed engineering bandwidth for internal capability work that is fully insulated from PM-driven product deadlines.

**Santi's three core projects.** The team (with main DS analyst [[Jose Manuel Martin Rodriguez]]) is advancing three initiatives. The *Sigma Pipeline* extracts attacker TTPs from threat reports/blogs and translates them into generic Sigma rules that can be re-targeted to any SIEM (e.g. [[Phoenix]]). *Tipper* is an LLM-powered knowledge DB and chatbot on Bedrock that auto-ingests public reports and extracts IPs, vulnerabilities, ransomware tags, etc. *Infrastructure of Interest (IOI)* monitors suspicious domains using ~60 features (age, AV alarms, etc.) and adds a dynamic "behavioral exposure" signal — unique customer/asset interactions per rolling 6-hour window — which is particularly good at catching supply-chain attacks (e.g. legitimate software being weaponised in an update path).

**Personal / spiritual conversation.** A significant portion of the meeting was personal: shared sorrow over the Israel/Iran conflicts and the historical trauma of the Spanish Civil War; strong common ground on yoga and meditation; Aviad shared his "Law of One" / "service to others" framing and recent psychedelic experiences, and floated the idea of guided meditations at work as a way to surface solutions to complex technical problems via the subconscious.

**Outcome.** Concrete next step is a cross-team session structured as 20 minutes of project overview followed by 20 minutes of IOI data deep dive, designed to onboard [[Inbar Dekel]]'s DS team into Santi's threat-intel project portfolio.

## Open questions

- How much of [[Inbar Dekel]]'s team's bandwidth will be earmarked for Santi's internal projects vs platform/product work? (Likely answered in the follow-up session.)
- The internal projects `Tipper`, `Sigma Pipeline`, and `Infrastructure of Interest` (Mather, Themis sub-systems) are not yet wiki project pages — flagged for follow-up project seeding.
