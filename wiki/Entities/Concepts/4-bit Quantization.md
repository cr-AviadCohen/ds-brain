---
title: 4-bit Quantization
type: concept
tags: [concept, wiki]
domain: ai-infra
related_projects: ["[[AIDRA]]", "[[SFT-PS]]"]
related_systems: ["[[Azure AI Foundry]]"]
last_updated: 2026-05-12
---

# 4-bit Quantization

> INT4 weight compression for LLM inference — typically implemented via
> BitsandBytes (NF4 / FP4) or GPTQ / AWQ schemes — trades a small
> quality loss for ~4× memory reduction.

## What it is

Quantize model weights from FP16/BF16 (16 bits) down to INT4 (4 bits)
representation, usually with per-channel or per-group scales. Common
flavors:
- **BitsandBytes NF4 / FP4** — quantize on load, dequantize on the fly during forward pass (good with [[LoRA]] — see "QLoRA").
- **GPTQ / AWQ** — calibrate quantization on a small dataset, ship a quantized checkpoint.

The result: a 7B parameter model that needed ~14 GB in FP16 fits in
~4 GB at INT4 — viable on a single consumer-grade GPU.

## Why we care

- [[AIDRA]] uses 4-bit quantization on its CodeLlama-7B inference path to fit within available GPU memory.
- [[SFT-PS]] (PowerShell SFT) — a candidate consumer of QLoRA (4-bit + [[LoRA]]) for cheap fine-tuning.

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.

## Open questions

- Which 4-bit scheme is the DS-team default (NF4 vs. GPTQ vs. AWQ)?
- Quality regression budget — what eval delta is acceptable when moving from FP16 to INT4 inference?
