---
title: Microsoft
type: organization
tags: [organization, wiki]
kind: vendor
hq: Redmond, Washington, USA
website: https://www.microsoft.com/
last_updated: 2026-05-12
---

# Microsoft

> Cloud + AI infrastructure vendor; hosts the DS team's production LLM
> stack via [[Azure AI Foundry]] and is the owner of Sentinel — a
> recurring integration / interop target.

## What they do

Cloud platform (Azure), productivity software, and AI services. Owner
of OpenAI GPT model hosting via [[Azure AI Foundry]], Microsoft
Sentinel SIEM, Defender for Endpoint, and the broader Microsoft
Security portfolio.

## Relationship to DS team

Vendor. [[Azure AI Foundry]] is the team's primary LLM provider for
production agentic services (CR-AI deployments operated by
[[Shoshana Avni]] and [[Nitzan Milchin]]). Microsoft Sentinel is a
recurring integration target on the SIEM side — Sigma rule export
([[Owlint-Sigma]]) and XDR interop discussions reference Sentinel as a
peer target.

## Key people

(None tracked in this wiki yet.)

## Teams

(None — vendor relationship.)

## Systems

- [[Azure AI Foundry]] — managed LLM service, primary DS-team LLM provider

## Open questions

- Sentinel as a Sigma export target — is there a Level Blue customer footprint that would warrant first-class translation support in [[Owlint-Sigma]]?
- How much of [[Azure AI Foundry]] quota is shared across DS-team projects vs. siloed per workload?
