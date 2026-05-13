---
title: Sigma as Common Detection Language Across Level Blue SIEMs
type: decision
tags: [decision, wiki]
date: 2026-05-07
deciders: ["[[Ziv Mador]]", "[[Santiago Cortes Diaz]]", "[[Itamar Hershko]]", "[[Pawel Knapczyk]]"]
status: accepted
related_projects: ["[[Owlint-Sigma]]"]
last_updated: 2026-05-11
---

# Sigma as Common Detection Language Across Level Blue SIEMs — 2026-05-07

## Context

Level Blue now spans multiple SIEM/MDR platforms — Fusion, USM Anywhere, [[Phoenix]], Core, and Alert Logic. Before the Sigma Interoperability project, each team independently read the same intel reports and hand-wrote platform-specific detections. The 2026-05-07 brownbag (Itamar presenting, with Ziv, Santi, and Pawel in the room) formalised the position that Sigma serves as the unified intermediate representation across these platforms.

## Decision

Sigma is the common detection language across all Level Blue SIEMs (Fusion, USM Anywhere, [[Phoenix]], Core, Alert Logic). The Sigma Interoperability project operates across three tracks: (1) automated pipeline from Tipper that produces Sigma rules from raw intel, (2) adaptation of pre-existing community Sigma rules from VirusTotal / forums, and (3) bi-directional SIEM-to-SIEM migration using Sigma as the intermediate representation.

## Why

Standardising on Sigma collapses N×M duplication (N teams × M platforms) to N detection opportunities expressed once and translated per platform. It also unlocks community Sigma reuse and enables a single analyst to perfect a rule on one platform (e.g., [[Phoenix]]) and have it replicate everywhere else. Without a common IR, every Level Blue SIEM acquisition would require re-paying the per-platform detection cost.

## Alternatives considered

- Keep platform-specific authoring per team — rejected: that is the status quo whose duplication cost prompted the project.
- Adopt a vendor-specific lingua franca (e.g., Splunk SPL as canonical) — implicit rejection: would not generalise bi-directionally across non-Splunk SIEMs and tie Level Blue to one vendor's syntax.

## Consequences

- All new detection content originates as Sigma; per-platform syntax is generated downstream.
- Tipper outputs flow to two destinations (Tipper internal and Martin News company-wide) where consumers can pull Sigma or the translated SIEM-native query.
- The system must maintain per-platform translation modules and validation; Fusion in particular requires a custom mapping built on top of Sigma HQ.
- Future Level Blue SIEM acquisitions inherit the Sigma pivot rather than adding another bespoke output target.

## Open questions

- How is the canonical Sigma source-of-truth versioned and reviewed as the community Sigma rule set evolves?
- What is the rollout sequencing once the AWS deployment is live — which platform mapping ingests production traffic first?
