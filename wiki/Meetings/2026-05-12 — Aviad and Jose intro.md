---
title: Aviad and Jose intro
type: meeting
tags: [meeting, wiki]
date: 2026-05-12
participants: ["[[Aviad Cohen]]", "[[Jose Manuel Martin Rodriguez]]"]
related_projects: ["[[Martin News Chatbot]]", "[[UEBA]]", "[[UEBA (USMA)]]", "[[AI Assistant]]", "[[IRCA]]", "[[Hunter]]"]
related_systems: ["[[USMA]]"]
related_decisions: []
related_ideas: ["[[Rebuild UEBA in Phoenix XDR]]"]
source: raw/meetings/meeting_2026.05.12_aviad_jose.txt
last_updated: 2026-05-12
---

# Aviad and Jose intro — 2026-05-12

> Intro session between Aviad (AI Architect) and Jose (10-yr Level Blue / ex-AlienVault domain expert) covering backgrounds, the Martin News Chatbot productionisation hand-off, the abandoned UEBA capability at Level Blue, and the shared engineering-bandwidth bottleneck.

## Decisions

- DS team owns platform choice for [[Martin News Chatbot]] productionisation — Aviad's team will evaluate AWS limitations before deciding (Jose anti-AWS, Aviad pro-AWS for production; explicit hand-off of platform ownership to DS).

## Action items

- [ ] Explore Martin News APIs and AWS Bedrock for the [[Martin News Chatbot]] production build — [[Guy Kassorla]]
- [ ] Evaluate AWS scoping / cost limitations vs. alternatives before locking platform choice — [[Aviad Cohen]]
- [ ] Scope a future collaboration on rebuilding UEBA inside [[Phoenix]] XDR (vs. buy from SentinelOne / IBM) — [[Aviad Cohen]], [[Jose Manuel Martin Rodriguez]]

## Discussion notes

**Backgrounds.** Aviad — 13 years of cybersecurity-research ML/AI; PhD in malicious-email / non-executable-attachment detection; 5 years at IBM Research on network anomaly detection + a QRadar AI assistant; now [[Aviad Cohen|Principal AI Architect at Cybereason]]; led the DS team for 7 months covering [[Inbar Dekel]]'s maternity leave. Left IBM Research over frustration with academic-style work that never reached production — strong bias toward shipping impact over papers. Jose — 5-yr Telecoms Engineering degree (Spain) + MSc Cybersecurity; started in software at Telefonica; ten years with the company through three rebrands ([[AlienVault]] → [[AT&T]] → [[LevelBlue]]) writing correlation rules and [[Suricata Signatures|Suricata signatures]] for the [[USMA]] (Unified Security Management) platform. Recently positioned as a domain expert building datasets and translating cybersecurity concepts for pure data scientists who lacked security background.

**Martin News Chatbot — productionisation hand-off.** Jose has a basic POC using a knowledge base + MCP; needs Aviad's team to turn it into a full production application consumed by NDR, threat hunters, and researchers across the company. Aviad noted that [[Guy Kassorla]] is preparing to explore Martin News APIs + AWS Bedrock — same direction [[Hunter]] already took. AWS preference is a tension: Jose dislikes AWS for cost and the overly-scoped "outside-in" communication model, prefers cheaper non-AWS deployments that interconnect more easily; gave Aviad's team complete ownership of platform choice. Aviad pushed back that Docker is fine for POC but a robust platform like AWS is usually needed for production, and committed to evaluating AWS limitations carefully before deciding.

**UEBA at Level Blue is dead.** Jose previously worked on an unsupervised-ML UBA solution inside [[USMA]] for anomalous-login / exfiltration / lateral-movement detection — captured as [[UEBA (USMA)]]. Project was completely abandoned roughly two years ago after severe turnover (loss of the AT&T DS team, then subsequent newly-hired DS leaving). The abandoned system still emits noisy alarms and generates customer complaints. Jose wants to rebuild or buy (SentinelOne, IBM). Aviad noted his side also lost a key UEBA engineer ([[Guy Kapach]]) in recent layoffs — the Cybereason [[UEBA]] POC. Aviad proposed rebuilding UEBA inside the [[Phoenix]] XDR platform as a candidate future collaboration but flagged that XDR is still a long way from fully functional — captured as [[Rebuild UEBA in Phoenix XDR]].

**Engineering-bandwidth bottleneck on both sides.** Aviad's [[AI Assistant]] and [[IRCA]] are currently blocked because [[Phoenix]] engineering is at full capacity and can't integrate them. Mirror image on the Level Blue side: massive layoffs in Level Blue engineering, remaining staff strictly focused on maintaining the legacy [[USMA]] platform until the [[Phoenix]] migration completes, so they cannot help with new AI deployments either.

**Three target scopes for AI work (Jose).** Tools for end-customers (heavy engineering cost), internal tools for the team's own research (lowest friction), internal tools for sibling departments — MDR, hunters, sales. Aviad echoed a strong preference for projects with highly-visible upper-management impact (esp. [[Ziv Mador]]) to prove the AI team's business value.

## Open questions

- AWS vs. non-AWS — what concrete scoping and cost evaluations does the [[Martin News Chatbot]] team need to run before committing?
- Rebuild [[UEBA]] inside [[Phoenix]] XDR vs. buy from SentinelOne / IBM — what budget / timeline horizon does each option imply?
- Can [[Phoenix]] engineering capacity ever unblock [[AI Assistant]] + [[IRCA]] without a new staffing decision, or do these projects need an alternative integration surface?
- What is the right shape of a recurring Aviad ↔ Jose sync given the overlap on UEBA, Martin News, and domain-expert dataset support?
