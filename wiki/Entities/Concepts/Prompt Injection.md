---
title: Prompt Injection
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[AI Assistant]]", "[[Hunter]]", "[[OwlBot]]", "[[AIDRA]]"]
related_systems: ["[[Azure AI Foundry]]"]
last_updated: 2026-05-12
---

# Prompt Injection

> An attack class where adversarial user input (or retrieved content)
> overrides or subverts the model's system prompt / instructions.

## What it is

The LLM-era equivalent of injection attacks: untrusted text consumed
by an LLM is interpreted as instructions rather than data. Two main
flavors —
- **Direct** — the user types instructions designed to override the system prompt ("ignore previous, do X").
- **Indirect** — adversarial instructions are embedded in retrieved documents, tool outputs, or web pages that the LLM later ingests.

Mitigation is a moving target: input/output filtering, separation of
instructions from data, structured tool I/O, and least-privilege tool
scopes.

## Why we care

Every DS-team agentic project has prompt-injection in its threat model:
- [[AI Assistant]] — analysts can paste arbitrary text into the chat.
- [[Hunter]] — hunts ingest event content, including attacker-controlled fields.
- [[OwlBot]] — Notion content can be authored by anyone in the org.
- [[AIDRA]] — multi-agent system passes outputs between agents; one compromised step can poison downstream.

## Manifestations

- 2026-05-12 — Catalogued during Concepts seed.

## Open questions

- Do we have a shared red-team / eval harness for prompt injection across DS-team agents?
- Tool-call gating policy: which tools require human-in-the-loop vs. autonomous invocation?
