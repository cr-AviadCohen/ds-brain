---
title: CMD Classification
type: project
tags: [project, wiki]
status: active
lead: [[Aviad Cohen]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - CMD Classification/
last_updated: 2026-05-11
---

# CMD Classification

> Classify process command lines as benign/malicious at the endpoint using ML/AI — a difficult task because maliciousness depends on context that isn't always available.

## Goal

Start with Windows CMD/PowerShell process command lines; later extend to macOS (most beneficial for the product). Two scopes considered: process command lines (collected) vs interactive shell commands executed via cmd.exe (not collected). Initial focus is process command lines, with parent/grand-parent context where extractable.

## Approach

Collect data from GitHub (PowerShell), VirusTotal (.bat files), and customer data via Google BigQuery (`hunting_amer.triage_result`, `hunting_apac.triage_result`, `hunting_emea.triage_result`). Detailed keyword-driven feature-extraction configuration plus LLM-assisted labelling (LLM tags VirusTotal commands; Sigma rules also used to label). Modelling options under consideration: classical ML, fine-tuned LLM, RAG. Initial VT+GBQ experiment produced poor results — future work emphasises a curated validated dataset.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Context that's critical for decisions (parent process, grandparent, image paths, file company, internal name) is mostly not extractable today.
- Initial experiment results were poor.

## Mentions

(populated by /ingest)

## Open questions

- Scope of the classifier: process command lines only, or any shell/script commands?
- Best modelling approach (classical ML vs fine-tuned LLM vs RAG).
