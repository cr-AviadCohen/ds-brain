---
title: Azure AI Foundry
type: system
tags: [system, wiki]
owner: Microsoft (vendor)
vendor: Microsoft
related_projects: ["[[AI Assistant]]", "[[IRCA]]", "[[OWLINT]]", "[[Owlint-Sigma]]", "[[MCP]]"]
seeds:
  - raw/data_science_drive/data-science-main.md
  - raw/projects/Project - AI Assistant/AI Assistant - Gate 1 - Research Impact & Feasibility.docx.md
  - raw/projects/Project - IRCA/IRCA - Gate 1 - Research Impact & Feasibility.docx.md
last_updated: 2026-05-11
---

# Azure AI Foundry

> Microsoft Azure's managed LLM service — the team's primary LLM provider for production-grade GenAI projects (Cybereason subscription `CR-AI`).

## Owner / vendor

Microsoft Azure — subscription "CR-AI" (`7663b00e-8f86-4f1f-a4ac-9bb724c220f7`). Israel integrator: Aztek (`asaf@aztek.co.il`). Personal-access requests go through Shoshana Avni; model deployments through Nitzan Milchin (and Shoshana Avni).

## Integration surface

- OpenAI-compatible API endpoints for chat completions, embeddings, etc.
- Azure Content Filtering layer.
- Quota management (the team has filed quota-increase requests because tens of thousands of LLM requests per research run was taking weeks).

## Data flow

DS projects authenticate via Azure key/endpoint → LLM requests routed to deployed models (GPT-5, GPT-5.2, GPT-5.4 for AI Assistant; GPT-5 for IRCA; GPT-4o historically for MCP / RCE-NG). Content filters can block prompts/responses.

## Current usage

- [[AI Assistant]]: orchestrator and per-agent LLMs (GPT-5.2 / GPT-5.4 with lighter alternatives).
- [[IRCA]]: GPT-5 for threat assessment, narrative, and MITRE mapping.
- [[OWLINT]] and [[Owlint-Sigma]]: optional LLM provider for rule generation.
- [[MCP]]: GPT-4o (with the 450K-tokens-per-minute limit being a known bottleneck).

## Known issues

- Per-minute token limits (e.g., 450K TPM on GPT-4o) easily hit by API responses that exceed 80K tokens.
- Content filters can block legitimate security-research prompts; PoC UIs sometimes have a separate content-filter-safe path.

## Related entities

[[AI Assistant]], [[IRCA]], [[OWLINT]], [[Owlint-Sigma]], [[MCP]]

## Open questions

- Whether to move some high-volume workloads to local LLMs (already done for AIDRA, which runs on OCI GPU machines).
