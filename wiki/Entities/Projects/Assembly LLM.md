---
title: Assembly LLM
type: project
tags: [project, wiki]
status: active
team: [[Aviad Cohen]]
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - Assembly LLM/
last_updated: 2026-05-11
---

# Assembly LLM

> Disassemble executables into assembly blocks and functions, generate pseudocode, tag each function with its purpose, and ultimately construct the "complete story" of the executable from its function-call flow.

## Goal

Use LLMs over Ghidra-derived disassembly to identify security-related implementations (attack methods, capabilities) and label each function's purpose (e.g., "reads hosts file", "accesses cookie files"). End goal: reconstruct the executable's full behavioural narrative from its call graph and per-function tags.

## Approach

Pipeline: Ghidra (treated as an agent, run headlessly) extracts functions and API calls as C code → splitter breaks them down → prompts route them to specialised LLM agents → writer/reporter compiles results. Designed generically so users can request various outputs from Ghidra. Local model loading on remote GPU (OCI server) via HuggingFace Transformers; also exploring Ollama and LMStudio. Models under consideration include `gemma-3-270m`/`gemma-3n-E4B` and `gpt-oss-20b`. Codebase under `cybereason-labs/assembly-llm`.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Project name ("Assembly LLM") is considered confusing; a renaming was discussed but not yet decided.

## Mentions

(populated by /ingest)

## Open questions

- Final project name.
- Packing/unpacking support for additional script obfuscation formats.
