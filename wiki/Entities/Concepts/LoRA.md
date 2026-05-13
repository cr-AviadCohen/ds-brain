---
title: LoRA
type: concept
tags: [concept, wiki]
domain: ai-infra
related_projects: ["[[AIDRA]]", "[[SFT-PS]]"]
related_systems: ["[[Azure AI Foundry]]"]
last_updated: 2026-05-12
---

# LoRA

> Low-Rank Adaptation — a parameter-efficient fine-tuning method that
> trains a pair of small low-rank matrices instead of the full model
> weights (Hu et al., 2021).

## What it is

Instead of updating all weights `W` during fine-tuning, LoRA freezes
`W` and learns a low-rank update `ΔW = B·A` where `A` and `B` are
small matrices (rank `r` typically 4-64). At inference the adapter can
be merged or kept separate. Drastically reduces trainable parameters
(often 1000×) and enables per-task adapter swapping.

## Why we care

- [[AIDRA]] uses LoRA for fine-tuning CodeLlama-7B variants.
- [[SFT-PS]] (Supervised Fine-Tuning for PowerShell) is a candidate
  LoRA target — fine-tune an LLM for PowerShell classification.
- Cheap to train + ship; enables multiple task-specific adapters atop
  a single base model on [[Azure AI Foundry]].

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.

## Open questions

- Do we standardize on a rank `r` and target modules (q_proj/v_proj only vs. all-linear) across DS-team fine-tunes?
- QLoRA (LoRA + [[4-bit Quantization]]) vs. plain LoRA — which is the default for [[AIDRA]] inference?
