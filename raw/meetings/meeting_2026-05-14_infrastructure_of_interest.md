---
title: "Meeting — Infrastructure of Interest (SLR Brownbag)"
type: meeting
date: 2026-05-14
duration: 43m 59s
series: SLR Brownbag Session Series
recorded: true
presenter: Jose Manuel Martin Rodriguez
host: Santiago Cortes Diaz
attendees:
  - Santiago Cortes Diaz
  - Jose Manuel Martin Rodriguez
  - Aviad Cohen
  - Itamar Hershko
  - Nikita Kazymirskyi
  - Shabtay Barel
tags:
  - meeting
  - inbox
  - slr
  - threat-intel
  - infrastructure-of-interest
  - tipper
---

# Meetings Summary

The May 14, 2026, SLR team meeting featured a deep-dive presentation by Jose Manuel Martin Rodriguez on a new proactive threat detection project called **Infrastructure of Interest (IoI)**. The session, introduced by Santiago Cortes Diaz (Santi), outlined a system designed to identify, analyze, and track suspicious infrastructure long before adversaries actually deploy it in malicious campaigns.

### **Core Concept and Scale of the IoI Project**
The primary goal of the IoI project is to step ahead of attackers by evaluating a massive pool of domain observations to infer if they will be used maliciously in the future. By cross-referencing internal telemetry with third-party data, the team can create early warning protections and provide highly contextualized intelligence. 

The scale of the project is massive. The system currently stores over **1.5 million domain observations** and takes in between 5,000 to 40,000 new domains daily. After a whitelisting process that filters out about 30% of the noise, roughly 70% of the domains proceed to analysis, resulting in 200 to 800 high-confidence malicious domains being pushed to customers daily. On average, this system allows the team to detect and block campaigns **40 to 120 days** before other vendors or the broader InfoSec community classify them as malicious.

### **The Four-Stage IOI Pipeline**

**1. Data Collection**
The system relies on 10 to 11 independent collectors that gather data daily or weekly. If one goes dark, the rest continue to operate. 
*   Collectors track various sources, including new domain registrations (Best Ruiz), certificates (Set Stream), phishing feeds, community inputs (Camry, OTX), and importantly, customer telemetry via OpenSearch hunting queries (Argus). 
*   The system intentionally retains observations instead of overwriting them, allowing analysts to track the historical evolution and score of a domain over time to determine if it is truly malicious or a false positive. 
*   Specific modules help filter noise, such as fuzzy matching for typosquatting, semantic similarity matching using embeddings for known brand impersonation (e.g., spotting fake Outlook or Instagram domains), and entropy filters to catch domain generation algorithms (DGAs).

**2. Analysis and Enrichment**
Once collected, domains are enriched using multiple internal and external databases.
*   **Internal Tools:** The team uses proprietary solutions like their own URL scanning system, historical Whois records, passive DNS databases, and the recently integrated HML from Trustwave.
*   **External Integration:** They leverage Shodan to scan associated IP addresses for open ports, banners, and TLS records. If a domain is linked to malware, the file is analyzed via a custom Cuckoo/Cape Sandbox solution equipped with YARA and network signatures.

**3. Machine Learning and Behavioral Filtering**
The system employs advanced machine learning to classify threats and avoid false positives:
*   **Themis:** A multi-class ML classifier that evaluates over 90 features using six distinct models (e.g., neural networks, random forests, KNN, SVC) and a meta-learner to classify domains as benign, gray benign, gray malicious, or malicious.
*   **TLS NLP Model:** An independent binary classifier that analyzes the natural language of TLS certificate features.
*   **Behavioral Clustering:** An unsupervised K-means clustering solution that maps USM customer telemetry into time series. It groups observations to determine if a domain behaves legitimately across the fleet (like Google) or exponentially (indicating a potential supply chain attack).
*   *Strict Guardrails:* To protect customers, if Themis marks a domain as benign, or if a domain appears in more than 100 events or across more than 10 different customers, it is considered too noisy/legitimate and is strictly blocked from becoming a detection rule.

**4. Flagging, Scoring, and Dissemination**
Observations that pass the analysis are evaluated against approximately **45 specific suspiciousness flags** (e.g., recent Whois creation, high entropy, self-signed certificates), each carrying a distinct numerical weight. 
*   The final score is the sum of these weights. If the score exceeds a "high confidence" threshold, the domain is pushed to the USM platform to actively protect customers. 
*   If it falls into a "medium confidence" tier, it is only pushed to the Open Threat Exchange (OTX). 
*   Indicators are categorized into five distinct "pulses" (e.g., Phishing, C2, Stealer) to give analysts immediate context.

### **The Campaign Assembler**
Jose also introduced a new advanced feature called the Campaign Assembler, which groups disparate domain observations into cohesive, investigation-ready campaigns. 
*   It utilizes five distinct clustering methodologies (such as Hash bucketing, weighted Jaccard, and latent community graph detection) operating across 16 different analytical views.
*   A "solid cluster" is formed only when at least four of the 16 views agree.
*   These clusters are simplified into **five dimensions of evidence** accompanied by text-based templates (to save on AI costs) and suggested investigation steps so human analysts can easily understand the threat narrative.
*   The system categorizes clusters into 11 types, clearly highlighting which ones are "analyst ready" (e.g., forensic matches, external attribution) versus those that are just noise or need more time to emerge.

### **Success Stories**
Jose showcased several real-world threats uncovered by the IOI system:
*   A massive, six-year-long Chinese affiliate fraud and iGaming operation that impersonated casino brands using thousands of rotating domains and redirectors.
*   An SMS thief malware distributed via a fake Google Store application targeting users in Brazil and India.
*   A complex credential phishing hub targeting Microsoft Office 365.

### **Strategic Vision and Next Steps**
Following the technical breakdown, Santi contextualized the project's strategic value for the SLR team. Traditionally, threat intelligence is either reactive (responding to an incident) or opportunistic (stumbling upon something on VirusTotal). The IoI system, integrated into the team's overarching "Tipper" platform, provides a structured framework for **proactive hunting**. Because the system relies heavily on the company's exclusive fleet telemetry, the resulting research and PR reports will be unique and difficult for competitors to replicate. 

The meeting concluded with Nikita Kazymirskyi requesting access to the system. Jose and Santi confirmed that IT is currently configuring SSO access, and the entire team will soon be able to utilize both the IoI platform and the Sigma interoperability tool (presented in the previous meeting) via the Tipper UI. Additionally, Aviad Cohen offered the AI team's assistance to help Jose refine the clustering algorithms in the future.

# Infrastructure of Interest (IOI) — SLR Brownbag

## TL;DR

SLR project to proactively identify, contextualize, and score suspicious internet infrastructure (domains/IPs/certs) **before** adversary campaigns go live. Funnels 5K–40K daily domain observations through 10+ collectors → enrichment + ML flagging → OTX/USM dissemination → campaign assembler. Avg lead time **40–120 days** ahead of public attribution; 567 domains independently confirmed malicious to date. Goal: give every SLR analyst a framework for **proactive** research grounded in Cybereason/LevelBlue's own visibility, replacing reactive/opportunistic workflows. Surfaced via Tipper UI (access rollout in progress).

## Why It Matters

- Early warning: customers blocked weeks/months before competitors flag.
- Contextualizes 3rd-party intel (avoid blind trust in vendor feeds).
- Leverages fleet prevalence as ground truth.
- Spots campaign profiles: growing / stable / supply-chain / DGA bursts.
- Research advantage exclusive to our telemetry — hard for others to replicate.

## Pipeline Overview

Four stages:

1. **Collection** — 10+ independent collectors, each tagged with profile/query for traceability. ~30% dropped at whitelisting before analysis.
2. **Analysis & Enrichment** — ML models + internal/external data sources.
3. **Flagging & Scoring** — ~45 weighted flags → maliciousness score → thresholds for USM / OTX-only / drop.
4. **Dissemination + Campaign Assembler** — pulses to OTX, high-confidence to USM; clustering builds investigation objects.

## Numbers

- **1.5M+** domain observations stored.
- **11** active collectors (Alejandro adding another).
- **40+** suspiciousness flags.
- **567** confirmed-malicious domains (independent confirmation).
- Daily intake: 5K–40K observations; ~70% pass whitelist; **200–800** high-confidence domains/day to OTX/USM.
- Lead time vs. public attribution: avg **40–120 days**, max several months.

## Collectors

All independent (one going dark ≠ pipeline break). Apply profile/query tags + whitelisting API mid-flow.

| Collector | Source | Purpose |
|---|---|---|
| **BestWhois** | New domain registrations (3×/week) | Earliest possible signal |
| **CertStream** (Alejandro, WIP) | New TLS certs | Cert-driven discovery |
| **Camry** | 3rd party | External intel |
| **OTX** | Community pulses | Crowd-sourced |
| **Mute** | Newly added | 3rd-party feed |
| **Phishing feeds** | Various | Phishing-specific |
| **Argus** | USM customer telemetry (OpenSearch queries weekly) | Fleet visibility — exclusive moat |

### BestWhois detail (3 sub-modules)

- **Fuzzy Jaro-Winkler** — typosquats of any length.
- **Semantic similarity** — embedding model vs. known-brand list (catches lookalikes like `gmial.*`, `blackhorizon.online`).
- **Entropy + suspicious TLD filter** — catches DGA bursts (random same-length domains, weird TLDs, registered in bursts).

### Observation model

Domains stored as **observations**, never overwritten. Yields time series of how a domain's score evolves → distinguishes legit/FP from persistently malicious.

## Analysis & Enrichment

### Internal

- **URL System** — internal URL-scan equivalent.
- **Passive DNS** historical DB.
- **Historic WHOIS** DB.
- **HML** (TrustWave post-merger).
- **Kape Sandbox / Cuckoo** — for malware files seen on related IPs (YARA + network sigs).

### External

- **Shodan** — scan IPs from A + TXT + other DNS records; track banners, open ports, TLS, apps.

### ML Models

- **Themis** — multi-class classifier (benign / gray-benign / gray-malicious / malicious). 90+ features. Ensemble of 6 models (NN, RF, KNN, SVC, …) → meta-learner weights features.
- **TLS NLP classifier** — binary, NLP over certificate fields. **Independent of Themis** → independent verdict.
- **Behavior (K-means, unsupervised)** — clusters customer-telemetry observations into time-series profiles. Clusters incl. *massive* (Google etc. → discard), *professional services*, *legitimate anomaly*, *exponential* (← supply-chain signal), etc.

### Hard filters (conservative posture)

- Themis says benign/gray-benign → excluded from detection (still stored).
- Domain seen on >100 fleet events OR >10 customers → noisy → excluded.
- Rationale: protect customers from FPs.

## Flag Scoring

~45 flags, each with weight. Final score = sum. Thresholds:

- **High confidence** → OTX **+ USM** (customer detection).
- **Medium** → OTX only.
- **Below** → drop.

Example flag weights:
- WHOIS recent creation: low.
- High entropy / has-pulse-related: 0.2.
- Themis malicious / very-high TLS score: 0.3.
- Multi-high-score, HTML-match, etc.: higher.

## Dissemination

- 5 OTX pulses by profile (Phishing / C2 / Stealer / etc.) — driven by collector's profile+query tags so analysts get context.
- **Only high-confidence → USM.**
- Pulses retained 3 months; rolled off if no new sightings (suspicious infra usually sticks → repeated observations).

## Campaign Assembler

Clusters observations into **investigation-ready campaign objects**.

### 5 clustering views (run in parallel, 16 total view variants)

- **Hash bucketing** — same payload / same MD5 of sorted ports / same cert.
- **Weighted Jaccard** — weighted vector overlap (old-school).
- **Time-window bursts** — 48h coordination signal.
- **Latent community detection** — graph-based, fills gaps.
- (+ one more)

**Consensus rule:** ≥4 of 16 views must agree → solid cluster.

### Output: 5 evidence dimensions

Text-template explanations (not LLM — cost-prohibitive at scale) covering forensic payload, external attribution, content morphology, shared infra, behavior. Suggested investigation steps included.

### Bootstrap stats (45-day sample)

- 774 clusters meeting consensus.
- 234 analyst-ready campaigns (out of 11 cluster-type taxonomy).
- ~0.6 of observations actually funnel into a cluster.

### Cluster taxonomy (11 types)

- **Analyst-ready**: direct attribution, strong coordination (48h burst), forensic (3rd-party reported — Country, Mute, phishing feeds).
- **Emerging legitimate**: monitor, defer.
- **Noise**: discard.

## Success Stories (selected)

- Domain spotted Sep 2025 → confirmed malicious by **Hunt.io** Apr 2026.
- Domain in system Aug 2025 → confirmed by **Recorded Future** Feb 2026 → **177-day lead time**.

### Live investigations from IOI seeds

- **6-yr Chinese iGaming affiliate fraud** — impersonating CN casino brands, thousands of rotating redirectors. Started from 3 short `.cc` domains → first + second-stage payloads recovered.
- **SMS thief** — distributed via fake Google Store app, targeting Brazil + India. First-stage recovered. Attribution WIP.
- **Microsoft 365 phishing hub** — credential phishing kit served across domain set. Seeded from IOI observations.

## Strategic Framing (Santiago)

- SLR + broader InfoSec community = reactive (post-incident IR + report) or opportunistic (VT clicking).
- IOI offers a **framework** for proactive research grounded in our visibility.
- Surfaces via **Tipper** (analyst platform) — complements **MartineNews** (sales/MVR overview).
- Goal: any analyst can open Tipper, pick a campaign, and within 2h either drop it or develop a lead.
- Future: coordination layer so analysts don't duplicate research.

## Open Questions / Follow-ups

- **Applicability to Phoenix?** — Santiago flagged for offline discussion. [[Phoenix]]
- **Tipper access rollout** — IT/LevelBlue SSO ongoing; team-wide access pending.
- **DS team collaboration** — Jose requested DS help improving clustering. Aviad: "We'll be glad to help." → DS engagement track to open.
- **AI in campaign assembler** — Jose plans to add LLM scoring for "which campaigns to investigate first" (kept off the per-observation hot path due to cost).
- **Sigma integration** — Tipper UI will bundle Sigma solution alongside IOI.

## Action Items

- [ ] **IT/LevelBlue** — finalize Tipper SSO access for SLR + DS dept.
- [ ] **Jose** — onboard DS team once UI access lands; share clustering details for collaboration.
- [ ] **DS team (Aviad et al.)** — engage on clustering review / improvements when invited.
- [ ] **Santiago** — explore IOI applicability to Phoenix.
- [ ] **Alejandro** — finish new collector (in progress).

## Entities to Promote on Ingest

- Project: [[Infrastructure of Interest]] (IOI)
- Project: [[Tipper]]
- Project: [[MartineNews]]
- System: [[Themis]] (multi-class domain classifier)
- System: [[Behavior Clustering]] (K-means on fleet telemetry)
- System: [[Campaign Assembler]]
- System: [[BestWhois Collector]]
- System: [[CertStream Collector]]
- System: [[Argus Collector]]
- System: [[URL System]] (internal)
- Concept: [[Typosquatting Detection]]
- Concept: [[DGA Detection]]
- Concept: [[Supply Chain Attack Detection]]
- Org: [[Hunt.io]], [[Recorded Future]], [[TrustWave]], [[LevelBlue]], [[Cybereason]]
- People: [[Jose Manuel Martin Rodriguez]], [[Santiago Cortes Diaz]], [[Alejandro]] (collector WIP), [[Itamar Hershko]], [[Nikita Kazymirskyi]], [[Shabtay Barel]]
