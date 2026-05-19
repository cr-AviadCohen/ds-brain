---
title: CertStream Collector
type: system
tags: [system, wiki, collector, threat-intel]
owner: "[[Labs]]"
vendor: internal (Level Blue / SLR)
integration_surface: [ioi-pipeline, tls-certificates]
related_projects: ["[[Infrastructure of Interest]]"]
last_updated: 2026-05-19
source: raw/meetings/meeting_2026-05-14_infrastructure_of_interest.md
---

# CertStream Collector

> New TLS-certificate collector inside [[Infrastructure of Interest]] — currently in development by [[Alejandro Prada Nespral]]. Will tap the Certificate Transparency stream to discover suspicious infrastructure at TLS-issuance time, often before the domain is ever resolved by a victim.

## Owner / vendor

Internal SLR Labs collector under [[Alejandro Prada Nespral]] (work-in-progress at 2026-05-14).

## Integration surface

- Input: Certificate Transparency log stream (new TLS certs issued by public CAs).
- Output: candidate observations tagged with cert metadata (issuer, SANs, validity) feeding the IOI whitelist + enrichment + Themis + TLS-NLP classifier pipeline.

## Current usage

- Not yet live in production at 2026-05-14; under active development.
- Will add cert-issuance lead signal alongside the existing WHOIS-registration ([[BestWhois Collector]]) lead signal.

## Related entities

- Projects: [[Infrastructure of Interest]].
- People: [[Alejandro Prada Nespral]] (builder).
- Meetings: [[2026-05-14 — Infrastructure of Interest (SLR Brownbag)]].

## Open questions

- CT log source(s) — Google Argon / Cloudflare Nimbus / aggregated SaaS feed?
- Throughput target — CT volumes dwarf WHOIS; whitelist + enrichment downstream must scale.
- Will the TLS-NLP classifier consume CertStream observations natively or via a separate path?
