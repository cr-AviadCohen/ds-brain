---
title: MITRE
type: organization
tags: [organization, wiki]
kind: standards-body
hq: McLean, Virginia, USA
website: https://www.mitre.org/
last_updated: 2026-05-12
---

# MITRE

> Federally funded R&D non-profit; steward of the ATT&CK framework and
> the de-facto adversary-behavior taxonomy the DS team's detection +
> hunting work maps to.

## What they do

Operates federally funded research and development centers (FFRDCs) and
maintains foundational cybersecurity standards — most notably the
[[MITRE ATT&CK]] framework (adversary tactics + techniques knowledge
base), CVE (vulnerability ID system), CWE (weakness enumeration), and
the CAR (Cyber Analytics Repository) analytics library.

## Relationship to DS team

Standards body. ATT&CK technique IDs are the lingua franca for
detection content across [[Cybereason]] and [[LevelBlue]] — they show
up in [[Owlint-Sigma]] rule generation, [[Detection Engineering Hub]],
[[Hunter]] hunt definitions, [[AIDRA]] risk scoring, and the
[[Tipper]] threat-intel pipeline. STIX (an adjacent OASIS standard
that MITRE contributes to) governs the team's threat-intel exchange
schema — see [[STIX]].

## Key people

(None tracked in this wiki yet.)

## Teams

(None — non-profit standards body.)

## Systems

- [[MITRE ATT&CK]] — adversary tactic/technique knowledge base
- [[STIX]] — OASIS standard for threat-intel exchange (MITRE-contributed)

## Open questions

- Which ATT&CK sub-techniques are under-covered by current DS-team detection content (gap analysis backlog)?
- Should the team contribute back upstream (e.g. via ATT&CK Evaluations or CAR analytics) given the volume of Sigma rules being produced?
