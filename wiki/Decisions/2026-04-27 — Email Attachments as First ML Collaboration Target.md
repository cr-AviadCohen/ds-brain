---
title: Email Attachments as First ML Collaboration Target
type: decision
tags: [decision, wiki]
date: 2026-04-27
deciders: ["[[Aviad Cohen]]", "[[Phil Hay]]"]
status: accepted
related_projects: []
related_systems: ["[[Mail Marshal]]"]
last_updated: 2026-05-12
---

# Email Attachments as First ML Collaboration Target — 2026-04-27

## Context

Aviad and Phil scoped potential ML/data-science collaboration in their 2026-04-27 intro. Phil's group already ships three production ML systems on Mail Marshal (URL Deep, PageML, Defense), and the threat landscape has shifted from malicious attachments toward phishing-link campaigns embedded in PDFs and compromised SharePoint sites.

## Decision

Treat email attachments — currently handled by rules + Yara + AV layers, including aggressive nested unpacking — as the most promising candidate first project for a future ML collaboration between Aviad's DS team and Phil's group.

## Why

Attachments still benefit from rule-based handling but represent a clear, bounded surface where a research-oriented data scientist can layer ML on top of existing unpacking, with measurable comparison against the current pipeline. URL Deep / PageML / Defense are already mature production systems, so they are less attractive as first collaboration targets than a slightly less crowded surface.

## Alternatives considered

- A fresh angle on URL Deep, PageML, or Defense — declined because those models are already in production and would compete with active owners ([[Rodel Mendrez]], [[Karla Agregado]], [[John Kevin Adriano]]).

## Consequences

- The DS team should expect to scope a data-provisioning and label-pipeline plan before committing to attachment-ML work.
- Any candidate model must clear "is it better than the live rule + Yara + AV stack?" as the success bar.
- An in-depth follow-up technical session covering URL Deep, PageML, and Defense internals is still planned to inform the collaboration.

## Open questions

- What dataset, label process, and ground-truth pipeline would be required to build an attachment ML model on top of Mail Marshal's existing unpacking layer?
- Will Mail Marshal, URL Deep, PageML, and Defense be seeded as wiki project/system pages before the collaboration starts?
