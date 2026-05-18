---
title: AWS SageMaker
type: system
tags: [system, wiki]
owner: vendor
vendor: AWS
integration_surface: [API]
related_projects: []
last_updated: 2026-05-18
---

# AWS SageMaker

> AWS's managed ML platform — training, deployment, model registry, pipelines. Historically used by [[Inigo Lopez-Barranco]]'s team in the AlienVault ML Account for [[OTX]]-related training workflows.

## Owner / vendor

AWS (third-party).

## Integration surface

SageMaker pipelines, training jobs, model registry, hosted endpoints. Within the Level Blue estate, SageMaker workloads live in the AlienVault ML Account.

## Data flow

Training data (AlienVault Apps / OTX accounts) → SageMaker pipelines in AlienVault ML Account → model artifacts → deployment endpoints.

## Current usage

- Inigo's team has historical SageMaker pipelines for [[OTX]]-side ML workloads.
- Not currently part of the DS team's production stack — [[Hunter]] + [[Martin News Chatbot]] target [[AWS Bedrock]] instead.

## Known issues

Per Inigo's experience (2026-05-14 intro):
- Steep learning curve.
- Forces you to surrender significant freedom to AWS-specific workflows.
- Highly expensive at production scale.
- Long-run upside: very smooth deployment + versioning once you've fully invested in the framework.

## Related entities

- [[AWS Bedrock]] — newer agent-oriented AWS-ML platform; preferred by the DS team for Hunter / Martin News.
- [[OTX]] — historical workload home.
- [[Inigo Lopez-Barranco]] — historical SageMaker user.

## Open questions

- Are any of Inigo's SageMaker pipelines worth surveying before they're re-platformed onto K8s + Kafka?
- Could SageMaker become the right host for any future DS-team training-heavy workload (e.g. [[SFT-PS]], [[Assembly LLM]] fine-tunes) instead of Azure / on-prem GPU?
