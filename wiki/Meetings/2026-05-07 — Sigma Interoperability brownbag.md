---
title: Sigma Interoperability brownbag
type: meeting
tags: [meeting, wiki]
date: 2026-05-07
participants: ["[[Ziv Mador]]", "[[Itamar Hershko]]", "[[Santiago Cortes Diaz]]", "[[Pawel Knapczyk]]"]
related_projects: ["[[Owlint-Sigma]]", "[[Detection Engineering Hub]]"]
related_decisions: ["[[2026-05-07 — Sigma as Common Detection Language]]", "[[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]]"]
source: raw/meetings/meeting_2026-05-07_BrownBag_Sigma Interoperability Tipper - Itamar
last_updated: 2026-05-13
---

# Sigma Interoperability brownbag — 2026-05-07

> SLR Brownbag presenting the Sigma Interoperability project — a unified pipeline that uses Sigma as a common detection language across Fusion, USM Anywhere, Phoenix, Core, and Alert Logic, plugged into the Tipper intel pipeline with deterministic translation + LLM fallback + RAG-based dedup.

## Decisions

- [[2026-05-07 — Sigma as Common Detection Language]] — Sigma is the common detection language across all Level Blue SIEMs (Fusion, USM Anywhere, [[Phoenix]], Core, Alert Logic); operated across three tracks (automated pipeline from Tipper, community rule adaptation, bi-directional SIEM-to-SIEM migration via Sigma as IR).
- [[2026-05-07 — Deterministic Sigma HQ Translation with LLM Fallback]] — prefer deterministic translation via the `Sigma HQ` Python package; LLM fallback only when conversion fails or when a platform mapping is missing.
- System currently generates high-quality templates for analysts to fine-tune, not end-to-end auto-deployed production rules. (operating principle)

## Action items

- [ ] Deploy the source code on the AWS server [[Pawel Knapczyk]] has prepared for live API handshakes and production-traffic testing — [[Pawel Knapczyk]], [[Itamar Hershko]]
- [ ] Schedule the next brownbag on the Infrastructure of Interest (IOI) project — [[Ziv Mador]]

## Discussion notes

**The problem.** Level Blue now spans multiple SIEM/MDR platforms — Fusion, USM Anywhere (USMA), [[Phoenix]], Core, and Alert Logic. Before this project, each team independently read the same intel reports and wrote platform-specific detections by hand. The Sigma Interoperability project replaces that duplication with one detection opportunity that auto-translates into each platform's native syntax.

**Tipper pipeline.** Sigma Interop sits inside the broader **Tipper** pipeline. Tipper monitors ~200 sources via RSS and Google APIs for campaigns and IOCs, accepts manual submissions, and is planned to ingest DFIR reports and fleet telemetry. ML/LLMs extract TTPs and produce "detection opportunities" formulated as Sigma proposals. Outputs flow to two destinations: **Tipper (internal)** to speed SLR detection QA, and **Martin News (company-wide)** so sales can answer customer coverage questions and threat hunters can pull hunting queries for Splunk, SentinelOne, etc. via systems like Inigo.

**Three tracks.** Track 1 (automated): raw threat reports + Tipper detection logic in, auto-generated Sigma rule out, translated to each SIEM before the next analyst shift. Track 2 (adaptation): ingests pre-existing Sigma rules from VirusTotal / community forums, validates, and re-translates to required formats. Track 3 (migration): bi-directional translation — a user can take a Splunk query, lift it back into Sigma, then push down into Fusion.

**Translation + AI fallback.** Primary engine is a local deployment of the official **`Sigma HQ`** Python package (natively supports Splunk, Sentinel, Elastic, …), with a custom mapping built on top for Fusion. When `Sigma HQ` fails or when a platform has no native mapping (e.g. USMA), an LLM with RAG over platform-specific schema documentation (USMA operators, "mute" logic, etc.) produces the translation.

**Validation, QA, and dedup.** A local Chroma vector store deduplicates: if a new rule has a similarity score above 0.55 against existing rules, the system flags it. A multi-layer LLM validation pass checks syntax, field placement, metadata, and platform applicability, looping up to three retries to self-correct before finalising. Langfuse provides observability into agent runs, RAG embeddings, and per-step validation outcomes.

**Strategy — templates, not full automation.** Santi was clear that the system generates high-quality templates rather than pushing directly to production. The target is to compress a 3-to-5-hour manual detection-engineering task to ~5 minutes by handing the analyst a ready-to-tune template plus source context. Once an analyst perfects a rule on one platform (e.g. [[Phoenix]]), the system replicates that expertise across all others.

**Closing context.** Ziv closed by noting how recently four separate entities with proprietary detection languages had been disconnected — this tool combined Tipper (Santi's team), Sigma mapping (Pawel's team), Phoenix schemas (Way's contribution), and AI automation (Itamar's team) into one shared resource. Next brownbag will cover IOI.

## Open questions

- What is the rollout sequencing once the AWS deployment is live — which platform mapping does production traffic flow into first?
- Should the similarity threshold (0.55) be tuned per-platform once production data comes in?
- A contributor referenced only as "Way" (Phoenix schemas) could not be resolved to an existing People page — left without wikilink.
- `Tipper`, `Martin News`, `Inigo`, `Fusion`, `USM Anywhere`, and `Alert Logic` are not yet wiki project / system pages — flagged for follow-up.
