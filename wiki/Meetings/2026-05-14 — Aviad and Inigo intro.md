---
title: Aviad and Inigo intro
type: meeting
tags: [meeting, wiki]
date: 2026-05-14
participants: ["[[Aviad Cohen]]", "[[Inigo Lopez-Barranco]]"]
related_projects: ["[[Martin News Chatbot]]"]
related_decisions: []
source: raw/meetings/meeting_2026.05.14_aviad_inigo.txt
last_updated: 2026-05-18
---

# Aviad and Inigo intro — 2026-05-14

> Intro + technical sync between [[Aviad Cohen]] and [[Inigo Lopez-Barranco]]: backgrounds, [[AlienVault]] → [[AT&T]] → [[LevelBlue]] infra history, AWS account maze, [[Martin News Chatbot]] / AWS Bedrock Agent Core direction, and the cross-merger org-map effort.

## Decisions

- (none — intro session)

## Action items

- [ ] Share consolidated org-map across the merged-team department once compiled — [[Aviad Cohen]] — TBD
- [ ] Unblock Level Blue Microsoft / Confluence / AWS access via IT ticket — [[Aviad Cohen]] — TBD

## Discussion notes

**Backgrounds.**
- Aviad — 13 yrs cybersecurity research (classic ML + GenAI). PhD in Software & Information Systems Engineering — malicious email detection, non-executable malware (PDFs, Office docs, images). Prior: IBM Research (network anomaly detection + AI assistant for QRadar SIEM). >1 yr at [[Cybereason]]; managed DS team during [[Inbar Dekel]]'s maternity leave before becoming Principal AI Architect.
- Inigo — Master's in physics + electronic engineering. ~12 yrs in embedded systems for trains (incl. high-assurance CCTV "black box" recorder built after the Madrid train bombings). Joined [[AlienVault]] in 2014 — plugins + ingestion mechanisms, then trained on Coursera and built early ML systems for the company.

**Company-history thread.**
- Inigo joined AlienVault → AT&T (2018 acquisition) → [[LevelBlue]] (2024 spinout). "Three companies, same job."
- Post-AT&T transition, the original OTX (Open Threat Exchange) team left. Inigo inherited the full backend sample + analysis stack; today he runs >100 microservices collecting / analyzing / storing threat data for projects like the malware trackers and "Infrastructure of Interest" (IOI).
- Staffing-shortage reality: Inigo's main focus is "keeping the lights on" rather than new-feature development.

**Cloud + EngOps.**
- ~90–95% of Inigo's systems run on AWS ECS clusters — architecture built by the old OTX team before Docker Swarm / Kubernetes were standard at the company.
- Because they operate on legacy infra separated from the main engineering org, Inigo's team handles their own EngOps.
- Long-term direction: migrate off proprietary AWS services (ECS, SQS) toward platform-agnostic managed services using Kubernetes + Kafka / [[Redpanda]]. Goal: stay aligned with broader engineering, AWS or OCI (Oracle Cloud).

**AWS Bedrock / SageMaker / [[Martin News Chatbot]].**
- Aviad described his current project: building the Martin News chatbot using [[AWS Bedrock]] + Agent Core. Preference for Agent Core because it enables easy agent creation, tool wiring, and guardrails without coding the orchestration from scratch in Python (which was the case for his earlier QRadar POC).
- Inigo has not used Bedrock Agent Core but shared SageMaker experience: AWS ML frameworks make deployment + versioning very easy in the long run, but the learning curve is steep, they impose strong workflow lock-in, and they are expensive. Pragmatic warning rather than a recommendation against.

**Access issues.**
- Aviad still waiting on full AWS + Confluence access. Level Blue Microsoft account is active but empty during the call; Confluence link from Inigo could not be opened. Pending IT ticket to wire permissions.

**AWS account map (Inigo's clarification).**
1. AlienVault ML Account — model development + training (contains the SageMaker pipelines).
2. AlienVault OTX Account — currently home of the Martin agent + knowledge base (AWS requires the agent and its data to live in the same account).
3. AlienVault Apps Account — runs the actual OTX platform. ("Naming scheme is to confuse the hackers.")

**Org-map / merger confusion.**
- Inigo's home team — Santi (Santiago Cortes Diaz), Jose Manuel Martin Rodriguez — originated at AlienVault.
- [[Phil Hay]], [[Pawel Knapczyk]], Carl come from [[Trustwave]].
- Other names are merging in from [[Alert Logic]].
- Aviad is compiling a consolidated org-map; Inigo strongly encouraged sharing it broadly — "everyone is currently feeling a bit lost."

## Open questions

- Which AWS account becomes the production home of the [[Martin News Chatbot]] once the DS team owns build (AlienVault OTX Account by inheritance, or a Level-Blue-side account)?
- Is migration of Inigo's >100-microservice ECS estate to K8s / Kafka a Level-Blue-engineering-led effort, or does it remain Inigo's team's responsibility?
- Are there DS-team-relevant data flows hidden in the AlienVault ML Account SageMaker pipelines (training data, model artifacts) worth surveying before they are re-platformed?
- Who is the IT ticket owner for Aviad's Level Blue Microsoft / Confluence / AWS access — and is there a Level-Blue-wide pattern other ex-Cybereason staff are hitting?
