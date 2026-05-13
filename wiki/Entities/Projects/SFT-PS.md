---
title: SFT-PS
type: project
tags: [project, wiki]
status: active
lead: [[Aviad Cohen]]
team: []
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - SFT-PS/
last_updated: 2026-05-11
---

# SFT-PS

> Supervised Fine-Tuning for PowerShell — fine-tune an LLM for PowerShell classification and code analysis.

## Goal

Produce an LLM-based classifier tuned to PowerShell that improves on stock-LLM accuracy for security-relevant PS classification and analysis tasks.

## Approach

Supervised fine-tuning experiments using LLaMA-Factory, on a mix of cloud machines: GCP VMs (data preparation VM, `jupyter-planet-shani` for training) and OCI Data Science projects (us-phoenix-1). Main experiment notebook: `cybereason-labs/research_notebooks/llm-train/llm_train/src/powershell/sft_classification.ipynb`.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

(populated as identified)

## Mentions

(populated by /ingest)

## Open questions
