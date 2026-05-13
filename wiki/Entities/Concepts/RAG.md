---
title: RAG
type: concept
tags: [concept, wiki]
domain: ml
related_projects: ["[[AI Assistant]]", "[[Owlint-Sigma]]", "[[OWLINT]]", "[[OwlBot]]", "[[Hunter]]", "[[Martin News Chatbot]]"]
related_systems: ["[[Azure AI Foundry]]"]
last_updated: 2026-05-12
---

# RAG

> Retrieval-Augmented Generation — embed a corpus, retrieve top-k
> relevant chunks at query time, and condition the LLM on them to
> ground its answer.

## What it is

Pipeline:
1. Chunk + embed a source corpus into a vector store.
2. At query time, embed the user query and retrieve top-k similar chunks.
3. Feed retrieved chunks into the LLM context window alongside the question.
4. (Optional) Rerank, filter, or chain multiple retrievals.

RAG is the default counter-measure when [[LLM Hallucination]] is the
dominant failure mode — grounding the model in retrieved evidence
reduces (but does not eliminate) ungrounded claims.

## Why we care

- [[AI Assistant]] grounds analyst questions on platform docs + telemetry.
- [[Owlint-Sigma]] retrieves similar Sigma rules + ATT&CK technique descriptions during rule generation.
- [[OWLINT]] retrieves prior CTI articles when triaging new threat-intel feeds.
- [[OwlBot]] is essentially a RAG layer over Notion.
- [[Hunter]] uses retrieval over rule + telemetry corpora.

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.
- 2026-05-12 — [[Martin News Chatbot]] POC uses knowledge base + MCP for retrieval — productionisation handed off to DS team in [[2026-05-12 — Aviad and Jose intro]].

## Open questions

- Shared embedding model + vector store across DS-team RAG projects (or per-project bespoke)?
- Eval methodology — how do we measure retrieval quality consistently?
