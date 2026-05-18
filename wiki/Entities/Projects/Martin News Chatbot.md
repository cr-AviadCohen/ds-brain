---
title: Martin News Chatbot
type: project
tags: [project, wiki]
status: active
lead: [[Guy Kassorla]]
team: ["[[Guy Kassorla]]", "[[Aviad Cohen]]", "[[Jose Manuel Martin Rodriguez]]"]
started: 2026-05-12
systems: []
related_decisions: ["[[2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects]]"]
related_projects: ["[[Hunter]]"]
raw_path: null
last_updated: 2026-05-18
---

# Martin News Chatbot

> Productionise the Martin News AI chatbot — a knowledge-base + MCP-backed assistant — into a full production application consumed company-wide by NDR, threat hunters, and researchers.

## Goal

Take Jose's basic POC (knowledge base + MCP) and turn it into a full, production-ready AI chatbot over Martin News content, deployed for cross-company use by the NDR team, threat hunters, and researchers. Replaces ad-hoc browsing / searching of Martin News with a conversational retrieval interface.

## Approach

DS team owns platform choice (handed off explicitly by Jose). Current direction: [[Guy Kassorla]] to explore the Martin News APIs + [[AWS Bedrock]] Agent Core (same stack pattern as [[Hunter]]). Aviad's reasoning for Bedrock Agent Core: easy agent creation, native tool wiring, built-in guardrails — no need to hand-roll the orchestration in Python (which was the case for his earlier IBM QRadar POC). POC architecture is knowledge-base + MCP; production target adds [[RAG]] over Martin News content plus the agent surface needed for cross-departmental use. Productionisation work blocked on the same Phoenix-engineering bandwidth limitation that gates [[AI Assistant]] and [[IRCA]] is not expected here because the deployment lives outside Phoenix.

AWS account layout (per [[Inigo Lopez-Barranco]], 2026-05-14): the Martin agent + its knowledge base currently live in the **AlienVault OTX Account** because AWS requires the Agent Core agent and its data to be in the same account. Training pipelines (SageMaker) sit in the **AlienVault ML Account**; the actual [[OTX]] platform runs in the **AlienVault Apps Account**.

## Status

active — seeded 2026-05-12 from [[2026-05-12 — Aviad and Jose intro]]. Hand-off from Spider Labs / Level Blue research to DS team is part of the broader orphan-project sweep recorded in [[2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects]]. POC exists on Jose's side; production build not yet started.

## Decisions

- DS team owns platform-choice decision (AWS vs. non-AWS) — to be locked after AWS scoping / cost evaluation.

## Risks

- AWS-cost + scoping limitations could make AWS Bedrock the wrong production target (Jose flagged restrictive outside-in communication model).
- Non-AWS deployments are cheaper to interconnect but lose the FedRAMP / managed-LLM posture that AWS Bedrock provides for sibling DS projects ([[Hunter]]).
- Cross-customer-data exposure risk if a non-isolated deployment ends up serving NDR, hunters, and sales from a shared instance — needs access-control story before broader rollout.
- Collaborator team currently works inside AWS Workspaces and exchanges code as zip downloads — no git, no branching, no PR review history. Material risk for any production hand-off that requires auditable version control. Source: [[2026-05-12 — Aviad and Guy DS Brain architecture]].

## Mentions

- 2026-05-12 — [[2026-05-12 — Aviad and Jose intro]] — Jose handed productionisation to Aviad's team; [[Guy Kassorla]] exploring APIs + AWS Bedrock; platform choice deferred pending AWS evaluation.
- 2026-05-12 — [[2026-05-12 — Aviad and Guy DS Brain architecture]] — Aviad flagged that the collaborator team works in AWS Workspaces and exchanges code as zip files (no git) — material risk for any production hand-off requiring version-control discipline.
- 2026-05-14 — [[2026-05-14 — Aviad and Inigo intro]] — Aviad confirmed [[AWS Bedrock]] Agent Core direction; Inigo (no Bedrock experience) flagged [[AWS SageMaker]] cost + lock-in risk as a general AWS-ML caution; AWS account map clarified (agent + KB in AlienVault OTX Account).

## Tensions

- **AWS strategy.** [[Aviad Cohen]] pro-AWS for production (robustness, parity with [[Hunter]]); [[Jose Manuel Martin Rodriguez]] anti-AWS (high cost + restrictive scoped environment that makes outside-in communication difficult). Resolved: DS team owns platform choice; will evaluate AWS limitations before deciding.

## Open questions

- Final platform choice — AWS Bedrock vs. a cheaper non-AWS Docker-based deployment?
- Where does this project share infra with [[Hunter]] (both target Bedrock + retrieval over a content corpus) vs. diverge?
- Who on the Level Blue side becomes the day-to-day product owner once DS team owns build?
- What SLAs / availability are required for cross-company use (NDR / threat hunters / researchers all at once)?
