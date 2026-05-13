---
title: Rebuild UEBA in Phoenix XDR
type: idea
tags: [idea, wiki]
proposer: "[[Aviad Cohen]]"
status: investigating
hypothesis: A rebuilt UEBA capability natively integrated into the [[Phoenix]] XDR platform can replace both the abandoned Level Blue USMA UBA component and Cybereason's stalled [[UEBA]] project, at lower cost than buying SentinelOne / IBM.
related_projects: ["[[UEBA]]", "[[UEBA (USMA)]]"]
last_updated: 2026-05-12
---

# Rebuild UEBA in Phoenix XDR

## Hypothesis

Both Level Blue (via the abandoned [[UEBA (USMA)]] component on [[USMA]]) and Cybereason (via the stalled [[UEBA]] POC under [[Guy Kapach]]) currently lack a working User & Entity Behavior Analytics capability. A unified rebuild inside [[Phoenix]] XDR — sharing platform infrastructure and avoiding a per-tenant UBA stack — is cheaper long-term than buying SentinelOne / IBM and gets a real UEBA capability back in the product without re-creating it inside the legacy USMA platform.

## Evidence

- [[UEBA (USMA)]] — Level Blue UEBA on [[USMA]] was abandoned ~2 years ago after AT&T DS team turnover; the abandoned model still generates noisy alarms and customer complaints ([[2026-05-12 — Aviad and Jose intro]]).
- Cybereason [[UEBA]] POC under [[Guy Kapach]] is Q2 Low priority with no current active owner after Guy was lost in layoffs.
- [[Jose Manuel Martin Rodriguez]] has working experience on the original USMA UBA implementation (anomalous logins, exfiltrations, lateral movements) — usable domain input.
- [[Aviad Cohen]] has 5 years at IBM Research on QRadar-side network anomaly detection — directly transferable background.
- [[Phoenix]] already centralises XDR telemetry across endpoints + external SIEM/cloud sources, providing a single platform surface for per-user baseline modelling that USMA and Cybereason Core never had jointly.

## Evaluation criteria

- Detection precision/recall on the canonical UBA scenarios (anomalous login, exfiltration, lateral movement) vs. the published SentinelOne / IBM UEBA baselines.
- Cost-to-rebuild (engineering months, infra burn on Phoenix) vs. SentinelOne / IBM annual licence cost.
- Phoenix-platform readiness — [[Phoenix]] is acknowledged as "still a long way from being fully functional" ([[2026-05-12 — Aviad and Jose intro]]); the rebuild plan must include a readiness gate.
- Re-usability of [[Identity Correlation]] work as the entity-resolution layer underneath UEBA baselines.

## Risks

- **Phoenix XDR maturity.** Phoenix is not yet fully functional as an XDR backend — building UEBA on top of an incomplete platform compounds delivery risk.
- **No active engineering bandwidth.** Both Cybereason Phoenix engineering and Level Blue engineering are at full capacity ([[2026-05-12 — Aviad and Jose intro]]); a UEBA rebuild has no obvious home today.
- **Build-vs-buy.** [[Jose Manuel Martin Rodriguez]] floated buying from SentinelOne / IBM as a viable alternative — the rebuild needs to beat that on both cost and detection quality.
- **Identity-correlation dependency.** Reliable per-user baselining depends on [[Identity Correlation]], itself an unsolved hard problem across DS-team projects.

## Next step

Joint scoping session between [[Aviad Cohen]] and [[Jose Manuel Martin Rodriguez]] to:
1. Quantify the cost / detection-quality bar for the buy alternative (SentinelOne, IBM).
2. Pin a Phoenix-readiness gate that defines "platform ready to host a UEBA capability".
3. Decide whether the current [[UEBA]] POC artefact (Guy Kapach's notebooks under `ueba_python`) is the right starting point or whether to redesign from Jose's USMA UBA experience.

## Open questions

- Is a unified Level Blue + Cybereason UEBA the right scope, or should the rebuild be Cybereason-only inside Phoenix first?
- Does the buy option (SentinelOne / IBM UEBA) include per-tenant deployment terms compatible with Level Blue's managed-customer footprint?
- How much of the abandoned [[UEBA (USMA)]] codebase / signal library is recoverable as input to the rebuild, or is it effectively a green-field design?
- Who owns the rebuild on the DS side once [[Guy Kapach]]'s former POC is reactivated — a new hire, an existing engineer reassigned, or co-led with Jose on the Level Blue side?
