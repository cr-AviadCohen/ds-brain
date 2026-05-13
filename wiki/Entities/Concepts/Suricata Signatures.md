---
title: Suricata Signatures
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[UEBA (USMA)]]", "[[Hunter]]"]
related_systems: ["[[USMA]]"]
last_updated: 2026-05-12
---

# Suricata Signatures

> Open-source IDS/IPS rule format (Suricata project) — pattern-match signatures over network packets / flows that trigger alerts when traffic matches a known attack pattern.

## What it is

Suricata is an open-source network IDS/IPS/NSM engine (OISF). Its signature language is a single-line rule format with action, header (proto, src/dst, ports), and options (`msg`, `content`, `pcre`, `flow`, `sid`, `rev`, `classtype`, `reference`, `metadata`, etc.). Example shape:

```
alert tcp $HOME_NET any -> $EXTERNAL_NET $HTTP_PORTS (msg:"..."; flow:established,to_server; content:"..."; sid:1000001; rev:1;)
```

Sibling atomic format to [[Sigma Rule Format]] — Sigma targets SIEM detection over log events, Suricata targets in-line network traffic over the wire. Where Sigma is vendor-neutral and translates to many SIEM backends, Suricata is the rule format consumed directly by the Suricata engine (and by Snort with minor dialect adjustments).

## Why we care

- [[USMA]] correlation stack consumes Suricata signatures as one of its primary network-detection inputs.
- [[Jose Manuel Martin Rodriguez]] has spent ~10 years writing Suricata signatures for USMA — his domain expertise centres on this format.
- [[Hunter]] generates Suricata IDS rules via an agentic workflow — see [[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]].

## Manifestations

- 2026-05-12 — Catalogued from [[2026-05-12 — Aviad and Jose intro]] (Jose's 10-yr authorship history on USMA).
- 2026-04-30 — Hunter Suricata rule-generation agentic workflow — see [[2026-04-30 — Agentic Workflow for Hunter Suricata Rule Generation]].

## Open questions

- How translatable are USMA Suricata signatures to / from [[Sigma Rule Format]] given their different telemetry surfaces (network packets vs. log events)?
- Could Jose's 10-year Suricata corpus seed a training / few-shot prompt set for [[Hunter]]'s Suricata generation pipeline?
