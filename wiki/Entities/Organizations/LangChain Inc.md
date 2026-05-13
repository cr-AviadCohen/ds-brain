---
title: LangChain Inc.
type: organization
tags: [organization, wiki]
kind: vendor
hq: San Francisco, California, USA
website: https://www.langchain.com/
last_updated: 2026-05-12
---

# LangChain Inc.

> Vendor / open-source steward behind [[LangGraph]] (the DS team's
> primary agent-orchestration framework) and adjacent observability
> tooling.

## What they do

Originator of the LangChain Python / JS libraries, the [[LangGraph]]
state-machine DAG framework, the LangSmith observability product, and
ongoing open-source agent tooling. They also commercialize hosted
versions of these frameworks for enterprise customers.

## Relationship to DS team

Vendor / OSS dependency. [[LangGraph]] is the de-facto orchestration
runtime for DS-team agent projects ([[AI Assistant]], [[AIDRA]],
[[Pixel Agents]], [[OwlHub]]). [[Langfuse]] (separate company,
adjacent ecosystem) provides the team's observability layer; LangSmith
is the closest commercial alternative.

## Key people

(None tracked in this wiki yet.)

## Teams

(None — vendor relationship.)

## Systems

- [[LangGraph]] — state-machine DAG framework, the agent runtime baseline

## Open questions

- Should the DS team migrate observability from [[Langfuse]] to LangSmith for tighter integration with [[LangGraph]]?
- Is there an enterprise LangGraph offering (hosted runtime) under evaluation by [[LevelBlue]] procurement?
