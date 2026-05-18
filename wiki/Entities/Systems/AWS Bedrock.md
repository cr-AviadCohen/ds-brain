---
title: AWS Bedrock
type: system
tags: [system, wiki]
owner: vendor
vendor: AWS
integration_surface: [API]
related_projects: ["[[Hunter]]", "[[Martin News Chatbot]]"]
last_updated: 2026-05-18
---

# AWS Bedrock

> AWS's managed-LLM service plus the **Agent Core** runtime for agentic workflows — tool use, guardrails, knowledge-base retrieval. Production target for [[Hunter]] and the candidate target for [[Martin News Chatbot]].

## Owner / vendor

AWS (third-party). Consumed by the DS team via Level Blue / AlienVault AWS accounts.

## Integration surface

- Bedrock model invocation API (Anthropic, Amazon, Cohere, Mistral, Meta hosted).
- Bedrock Agent Core — declarative agent definition (tools, action groups, knowledge bases, guardrails).
- Bedrock Knowledge Bases — managed RAG retrieval over S3-backed content.
- AWS account constraint — an Agent Core agent must live in the same AWS account as the data it accesses (cross-account access is not supported in the simple path).

## Data flow

DS-team client → Bedrock Agent Core → (tools | knowledge base) → response. For [[Martin News Chatbot]] the knowledge base lives in the AlienVault OTX account alongside the agent.

## Current usage

- [[Hunter]] — production stack pattern (Bedrock + OpenSearch retrieval).
- [[Martin News Chatbot]] — current direction is the same Bedrock + KB + MCP pattern (Aviad pro-Bedrock); platform-choice decision deferred pending AWS-cost evaluation flagged by [[Jose Manuel Martin Rodriguez]].
- Operationally preferred by Aviad over hand-rolled Python orchestration — easier agent creation, native tool wiring, and built-in guardrails compared with the earlier QRadar POC he wrote from scratch at IBM.

## Known issues

- Cost — Jose flagged AWS expense + scoping limitations as a blocker for full Martin productionisation.
- Restrictive outside-in communication model — Jose's specific concern for Martin News.
- Single-account data-locality requirement forces awkward decisions around which AWS account owns a given knowledge base + agent.

## Related entities

- [[Hunter]] — production reference.
- [[Martin News Chatbot]] — candidate target.
- [[AWS SageMaker]] — sibling AWS-ML platform (different ergonomics — heavy framework, steeper curve).
- [[OTX]] — current home of the Martin News agent + KB.

## Open questions

- Is Bedrock + Agent Core the right production target for Martin News given the cost + outside-in limitations Jose flagged?
- FedRAMP / managed-LLM posture trade-off vs. a cheaper non-AWS Docker-based deployment.
- Cross-account workaround story for any future Level-Blue-wide agent that needs to read from multiple AWS accounts.
