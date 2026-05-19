---
title: Tipper
type: system
tags: [system, wiki]
owner: Level Blue (Trustwave SpiderLabs heritage)
vendor: Level Blue
integration_surface: [threat-intel-pipeline, notification-feed]
related_projects: ["[[Owlint-Sigma]]", "[[OWLINT]]", "[[AIDRA]]", "[[Infrastructure of Interest]]"]
last_updated: 2026-05-19
---

# Tipper

> Level Blue's (formerly Trustwave SpiderLabs) AI-powered threat-intelligence pipeline — produces early signals on new threats, variants, and threat actors. The downstream collaboration target for the DS team's Owlint-Sigma rule-generation work.

## Owner / vendor

Originated inside Trustwave SpiderLabs; now part of Level Blue post the 2025 Trustwave acquisition.

## Integration surface

- Threat-intel pipeline ingesting public + proprietary sources.
- Outputs intel pulses / signals consumable by downstream detection-engineering workflows.
- Trigger surface — Owlint-Sigma consumes Tipper events to auto-generate Sigma rules and reverse-translate SIEM queries.

## Data flow

Threat intel sources → Tipper pipeline → classified signals / DFIR pulses → (new) [[Owlint-Sigma]] auto-generates validated Sigma rules + SIEM-query translations → downstream SIEM consumption.

Per the Sigma Interoperability brownbag (2026-05-07): "Tipper already gives us early visibility into new threats, variants, and threat actors. The opportunity is to make that intelligence actionable, not let it stop at a notification."

## Current usage

- Internal Level Blue / Trustwave SpiderLabs operations.
- Collaboration target for [[Owlint-Sigma]] (Itamar Hershko lead) — Tipper signals automatically trigger Sigma rule emission and SIEM translation, no manual handoff.
- Referenced by [[OWLINT]] proposal and [[AIDRA]] presentations as upstream intel source.
- **Analyst UI surface for [[Infrastructure of Interest]]** — Tipper UI bundles IOI campaign objects (from [[Campaign Assembler]]) alongside the Sigma interop tool. SSO rollout to SLR + DS team in progress (per 2026-05-14 brownbag).

## Known issues

(none documented yet — manual triage volume was the motivating gap)

## Related entities

- Projects: [[Owlint-Sigma]] (primary downstream consumer), [[OWLINT]], [[AIDRA]].
- People: [[Itamar Hershko]] (Owlint-Sigma lead).
- Meetings: [[2026-05-07 — Sigma Interoperability brownbag]].

## Open questions

- Authoritative Tipper owner / contact inside Level Blue post-acquisition.
- Tipper output schema — is there a stable contract Owlint-Sigma can pin against?
- SLA on Tipper-to-rule latency target (minutes? hours?).
- Rights / licensing of Tipper-derived Sigma rules — internal-only or sharable to community Sigma repos?
