---
title: Hunter
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: ["[[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]]"]
related_projects: ["[[Martin News Chatbot]]"]
raw_path: raw/projects/Project - Hunter/
last_updated: 2026-05-11
---

# Hunter

> Internal AI-powered hunting interface backed by AWS Bedrock and OpenSearch, currently read-only, used for SOC investigations across customer data.

## Goal

Provide GTO/SpiderLabs analysts with an AI-assisted hunting interface over the customer data already held in AWS OpenSearch (one cluster for raw data, one for findings/incidents). Read-only from the beginning. Sufficient for internal usage today; expansion to broader (customer-facing) usage is a future discussion that requires stronger backend-enforced access controls.

## Approach

LLM stack: AWS Bedrock (FedRAMP-authorised) — chosen because the team is "all in" on AWS and customer data is already hosted there. Web UI: Open WebUI with a custom MCP plug-in / OpenSearch connector that issues queries and returns results to Hunter. Security groups already align analyst groups (GTO, SpiderLabs) with the customer data they're entitled to. Backend (not the AI prompt) must enforce access for any future broader rollout because prompt-level controls are easily bypassed.

## Status

active — seeded from raw 2026-05-11.

## Decisions

- [[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]] — replace single-prompt Suricata IDS rule generation with a validated agentic workflow.

## Risks

- Prompt-level access controls are not a sufficient enforcement boundary for broader rollout; backend enforcement is required.
- Data-privacy posture relies on Bedrock not training on customer data.

## Mentions

- 2026-05-12 — [[2026-05-12 — Aviad and Jose intro]] — Hunter's AWS Bedrock pattern referenced as the likely template for [[Martin News Chatbot]] productionisation ([[Guy Kassorla]] exploring Martin News APIs + Bedrock).

## Open questions

- Conditions and architecture for moving from internal-only to broader (customer-facing) usage.
