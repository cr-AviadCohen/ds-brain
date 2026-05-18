---
title: OTX
type: system
tags: [system, wiki]
owner: "[[LevelBlue]]"
vendor: "[[LevelBlue]]"
integration_surface: [API]
related_projects: []
last_updated: 2026-05-18
---

# OTX

> Open Threat Exchange — crowd-sourced threat-intelligence feed originally built by [[AlienVault]], inherited via [[AT&T]] and now operated by [[LevelBlue]]. Live at https://otx.alienvault.com/.

## Owner / vendor

[[LevelBlue]] — inherited via [[AT&T]] acquisition of [[AlienVault]] (2018) and the 2024 cybersecurity-arm spinout.

## Integration surface

Public REST API + community feed (pulses, indicators, malware-family entries). Backend: AWS-hosted ECS-based microservice estate (>100 services) — collection, analysis, storage of threat data; sibling projects include malware trackers and "Infrastructure of Interest" (IOI).

## Data flow

Community contributors → OTX pulses → AlienVault Apps Account (platform) → AlienVault OTX Account (agent + knowledge base, incl. the [[Martin News Chatbot]] POC) → AlienVault ML Account (training pipelines on SageMaker).

## Current usage

- Backend home of the [[Martin News Chatbot]] AWS-Bedrock agent + its knowledge base — AWS requires the agent and its underlying data to live in the same account.
- Owner team — [[Inigo Lopez-Barranco]] inherited the full estate post-[[AT&T]] transition when the original OTX team left; today the operating focus is "keep the lights on" rather than new-feature development.
- Long-term direction: re-platform off proprietary AWS (ECS / SQS) onto Kubernetes + Kafka / [[Redpanda]] to align with broader Level Blue / Cybereason engineering.

## Known issues

- Tech-debt + staffing risk — single-owner backend (>100 microservices) maintained by a team focused on availability, not new features.
- ECS / SQS lock-in delays platform-agnostic re-architecture.
- Account-structure complexity (ML / OTX / Apps accounts) makes data-locality reasoning awkward for any new agentic workload.

## Related entities

- [[AlienVault]] — original vendor.
- [[AT&T]] — historical parent.
- [[LevelBlue]] — current operator.
- [[Inigo Lopez-Barranco]] — current owner of OTX backend systems.
- [[Martin News Chatbot]] — agent + KB currently hosted inside the AlienVault OTX account.

## Open questions

- Is OTX a candidate platform for cross-Level-Blue threat-intel sharing (e.g. into [[Tipper]] or [[Owlint-Sigma]] workflows)?
- Are the >100 microservices documented anywhere, or is the architecture tribal knowledge?
- What's the timeline / owner for the K8s + Kafka / [[Redpanda]] re-platform?
