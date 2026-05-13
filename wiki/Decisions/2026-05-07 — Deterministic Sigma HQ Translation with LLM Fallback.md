---
title: Deterministic Sigma HQ Translation with LLM Fallback
type: decision
tags: [decision, wiki]
date: 2026-05-07
deciders: ["[[Itamar Hershko]]", "[[Santiago Cortes Diaz]]"]
status: accepted
related_projects: ["[[Owlint-Sigma]]"]
last_updated: 2026-05-11
---

# Deterministic Sigma HQ Translation with LLM Fallback — 2026-05-07

## Context

The Sigma Interoperability project needs to translate one Sigma rule into many SIEM dialects (Splunk, Sentinel, Elastic, Fusion, USMA, Phoenix, Core, Alert Logic). LLM-only translation is non-deterministic and expensive; pure deterministic translation lacks coverage when a platform mapping is missing. The 2026-05-07 brownbag formalised the chosen split.

## Decision

Primary translation engine is the official `Sigma HQ` Python package (deterministic; natively supports Splunk, Sentinel, Elastic, etc.) with a custom mapping built on top for Fusion. An LLM with RAG over platform-specific schema documentation is the fallback — invoked only when `Sigma HQ` fails or when a platform has no native mapping (e.g., USMA). A multi-layer LLM validation pass (syntax, field placement, metadata, applicability) with up to three retries self-corrects before finalising.

## Why

Deterministic translation gives cheaper, repeatable, auditable conversions for platforms that already have library support — which is most of them. Restricting the LLM to gap-filling and validation keeps token cost down, keeps output stable across runs, and concentrates LLM risk where it adds clear value (novel mappings, edge cases). The retry-bounded validation loop ensures we still publish only well-formed rules without unbounded LLM spend.

## Alternatives considered

- LLM-only translation across all platforms — rejected: non-deterministic, expensive, harder to audit.
- Pure deterministic with no LLM fallback — rejected: blocks coverage for platforms without `Sigma HQ` mappings (notably USMA) and makes the system brittle when Sigma HQ fails on an edge case.

## Consequences

- Per-platform translation modules inherit from a shared `BasePlatform` (syntax, field mapping, validation, repair loops).
- RAG corpora over platform docs (USMA operators, "mute" logic, Phoenix schemas, etc.) must be maintained as the LLM-fallback knowledge base.
- Langfuse observability is wired in so per-step validation outcomes and RAG embeddings can be inspected.
- The 3-retry cap on LLM self-correction bounds the failure-mode budget per rule.

## Open questions

- Should the similarity threshold (0.55) on the local Chroma dedup store be tuned per-platform once production data comes in?
- When LLM fallback is exercised, how is the result fed back to improve the deterministic mapping over time?
