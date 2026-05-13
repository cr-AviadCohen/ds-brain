---
title: Wiki Ops Log
type: log
tags: [log, wiki]
direction: prepend (newest on top)
append_only: true
last_updated: 2026-05-13
---

> **Append-only, prepend-order log.** New entries go directly below this
> preamble (newest on top). Never edit or delete past entries — they are
> the historical record. Same convention applies to `wiki/Log/pulse.md`.

## [2026-05-13] lint | inline-code lint fix + 12 cross-refs + 15 new concept/system/research pages
- tools/lint baseline: 4 → 3 (1 stale-link fixed via schema change, not content edit). 3 remaining orphans (INDEX/pulse/wiki-ops) are structural-by-design.
- schema fix: tools/lint/check_stale_links.py now strips inline-code spans (single + double backticks) before scanning so that `[[name]]` quoted in log entries no longer registers as stale-link. Test for prior behavior inverted; double-backtick case added. 12/12 lint tests pass.
- LLM checks (5 parallel Explore audits): contradictions 0; stale claims 0; orphaned concepts 15 (all seeded — see below); missing cross-refs 15 (12 applied, 2 already correct, 1 false-positive); data gaps 12 (deferred — research pass only).
- cross-ref backfills (12):
  - wiki/Entities/Teams/Spider Labs.md (related_projects + body → [[Martin News Chatbot]])
  - wiki/Entities/Projects/IRCA.md (systems → [[Phoenix]])
  - wiki/Entities/Systems/Phoenix.md (related_projects + Related-entities body → [[IRCA]], [[AI Assistant]])
  - wiki/Entities/Projects/AI Assistant.md (systems → [[Phoenix]])
  - wiki/Entities/Projects/Detection Engineering Hub.md (related_projects → [[Owlint-Sigma]])
  - wiki/Entities/Projects/Owlint-Sigma.md (related_projects → [[Detection Engineering Hub]])
  - wiki/Entities/Projects/AIDRA.md (related_teams → [[Labs]])
  - wiki/Decisions/2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects.md (related_projects → [[Martin News Chatbot]])
  - wiki/Entities/Projects/RCE-NG.md (related_projects → [[XDR Correlation for Phoenix]])
  - wiki/Entities/Projects/UEBA (USMA).md (related_ideas → [[Rebuild UEBA in Phoenix XDR]])
  - wiki/Entities/Projects/XDR Correlation for Phoenix.md (related_teams → [[Phoenix Team]])
  - wiki/Entities/Teams/Data Science Team.md (related_teams → [[Spider Labs]])
  - wiki/Meetings/2026-05-07 — Sigma Interoperability brownbag.md (related_projects → [[Detection Engineering Hub]])
  - wiki/Entities/Projects/Incident Investigation (for Fusion 2).md (related_teams → [[Fusion 2 Team]])
- orphaned-concept seeds (15 new pages, all referenced from INDEX.md):
  - wiki/Entities/Concepts/Command and Control.md
  - wiki/Entities/Concepts/Remote Access Trojan.md
  - wiki/Entities/Concepts/Persistence.md
  - wiki/Entities/Concepts/Local Security Authority.md
  - wiki/Entities/Systems/Event Tracing for Windows.md
  - wiki/Entities/Systems/Antimalware Scan Interface.md
  - wiki/Entities/Concepts/Windows Management Instrumentation.md
  - wiki/Research/Digital Forensics and Incident Response.md (first Research page)
  - wiki/Entities/Concepts/Code Obfuscation.md
  - wiki/Entities/Concepts/Remote Desktop Protocol.md
  - wiki/Entities/Concepts/Master Boot Record.md
  - wiki/Entities/Concepts/Credential Theft.md
  - wiki/Entities/Systems/Active Directory.md
  - wiki/Entities/Concepts/Privilege Escalation.md
  - wiki/Entities/Concepts/Lateral Movement.md
- wiki/INDEX.md (11 new Concept entries + 3 new System entries + 1 new Research entry + last_updated bump)
- data gaps deferred (12 suggested external searches — Tipper owner/schema/SLA, Alert Logic ML scope/transfer feasibility, Phoenix UEBA arch, USMA→Phoenix timeline, Sigma 2.0 adoption, Sage scope, Langfuse deployment, RAG shared-stack, Anthropic prod policy).

## [2026-05-12] lint | deterministic clean + 6 cross-ref backfills
- tools/lint/run_all baseline: 4 → 3 (1 stale-link fixed; 3 remaining orphans are structural pages INDEX/pulse/wiki-ops by design).
- wiki/Entities/Projects/DS Brain.md (literal `[[wikilinks]]` placeholder in inline code replaced with "Obsidian-style wikilinks" to drop spurious stale-link)
- LLM checks (5 parallel Explore audits): contradictions 0, stale claims 0, orphaned concepts 9 (deferred — net-new pages), missing cross-refs 10 (top 5 applied below), data gaps 10 (deferred — separate research pass).
- wiki/Entities/Teams/Data Science Team.md (related_projects + [[DS Brain]])
- wiki/Entities/Systems/Phoenix.md (Related entities + [[Rebuild UEBA in Phoenix XDR]])
- wiki/Entities/Projects/UEBA.md (frontmatter related_ideas → [[Rebuild UEBA in Phoenix XDR]])
- wiki/Meetings/2026-05-12 — Aviad and Jose intro.md (frontmatter related_ideas → [[Rebuild UEBA in Phoenix XDR]])
- wiki/Entities/Projects/Martin News Chatbot.md (frontmatter related_projects → [[Hunter]])
- wiki/Entities/Projects/Hunter.md (frontmatter related_projects → [[Martin News Chatbot]])

## [2026-05-12] ingest | Aviad and Guy DS Brain architecture
- wiki/Meetings/2026-05-12 — Aviad and Guy DS Brain architecture.md (new)
- wiki/Sources/2026-05-12 — Aviad and Guy DS Brain architecture.md (new — source one-pager for the meeting-summary input)
- wiki/Entities/Projects/DS Brain.md (new — first project page for the brain itself, meta workstream)
- wiki/Decisions/2026-05-12 — Unified Branch over Split for DS Brain.md (new)
- wiki/Decisions/2026-05-12 — Local Claude Write-Only to INBOX.md (new)
- wiki/Decisions/2026-05-12 — Server VM as Sole Ingest Authority.md (new)
- wiki/Entities/People/Aviad Cohen.md (Mentions + related_projects → [[DS Brain]])
- wiki/Entities/People/Guy Kassorla.md (Mentions + related_projects → [[DS Brain]]; **role: Data Engineer → Data Scientist** per user)
- wiki/Entities/People/Inbar Dekel.md (Mentions + related_projects → [[DS Brain]])
- wiki/Entities/People/Itamar Hershko.md (Mentions + related_projects → [[DS Brain]])
- wiki/Entities/People/Jose Manuel Martin Rodriguez.md (Mentions — Martin News collaborator no-git workflow flagged)
- wiki/Entities/Projects/Martin News Chatbot.md (Mentions + Risks — collaborator no-git workflow)
- wiki/Entities/Locations/Tel-Aviv.md (Guy role → Data Scientist)
- wiki/Entities/Teams/Data Science Team.md (Guy role → Data Scientist)
- wiki/Entities/Teams/Engineering.md (Guy role → Data Scientist)
- wiki/🔥 Hot Notes/Brain Architecture.md (new Topology section — local vs server roles for the team-wide rollout)
- wiki/INDEX.md (Guy role updated; new entries: DS Brain project, Aviad+Guy meeting, 3 decisions, 1 source bullet)
Files moved:
- INBOX/project Data Science Brain → raw/meetings/meeting_summary_2026.05.12_aviad_guy_ds_brain.md

## [2026-05-12] split | UEBA — disambiguate Cybereason project / USMA project / concept
- wiki/Entities/Concepts/UEBA (concept).md (new — abstract concept page; filename disambiguated to avoid stem collision with Projects/UEBA.md)
- wiki/Entities/Projects/UEBA (USMA).md (new — Jose's historical Level Blue / USMA Unsupervised UBA project)
- wiki/Entities/Projects/UEBA.md (clarified — now explicitly Cybereason; cross-link to [[UEBA (USMA)]] sibling and [[UEBA (concept)]] umbrella)
- wiki/Entities/Systems/USMA.md (5 wikilink retargets — USMA-context UEBA refs → [[UEBA (USMA)]])
- wiki/Entities/People/Jose Manuel Martin Rodriguez.md (frontmatter related_projects → [[UEBA (USMA)]])
- wiki/Meetings/2026-05-12 — Aviad and Jose intro.md (frontmatter + body — Jose's USMA history → [[UEBA (USMA)]]; Cybereason POC reference disambiguated)
- wiki/Ideas/Rebuild UEBA in Phoenix XDR.md (both projects mentioned explicitly; frontmatter related_projects)
- wiki/Entities/Concepts/Identity Correlation.md (USMA-context UEBA mention → [[UEBA (USMA)]])
- wiki/Entities/Concepts/Suricata Signatures.md (stale UEBA frontmatter ref → [[UEBA (USMA)]] — Suricata→UBA tie is USMA-stack-specific)
- wiki/INDEX.md (2 new bullets: [[UEBA (USMA)]] under Projects, [[UEBA (concept)]] under Concepts)

## [2026-05-12] ingest | Aviad and Jose intro (Spider Labs handover follow-up)
- wiki/Meetings/2026-05-12 — Aviad and Jose intro.md (new)
- wiki/Entities/Projects/Martin News Chatbot.md (new)
- wiki/Entities/Systems/USMA.md (new)
- wiki/Entities/Organizations/AlienVault.md (new)
- wiki/Entities/Concepts/Suricata Signatures.md (new)
- wiki/Ideas/Rebuild UEBA in Phoenix XDR.md (new)
- wiki/Entities/People/Aviad Cohen.md (Mentions)
- wiki/Entities/People/Jose Manuel Martin Rodriguez.md (Mentions + Background refined)
- wiki/Entities/Projects/UEBA.md (Mentions + Tensions block on ownership crisis)
- wiki/Entities/Projects/AI Assistant.md (Mentions — blocker)
- wiki/Entities/Projects/IRCA.md (Mentions — blocker)
- wiki/Entities/Projects/Hunter.md (Mentions — Bedrock context)
- wiki/Entities/Concepts/RAG.md (Manifestations)
- wiki/Entities/Concepts/Identity Correlation.md (Manifestations)
- wiki/Connections/training-data-plumbing-as-real-ml-bottleneck.md (instance added)
- wiki/Entities/Organizations/AT&T.md (AlienVault lineage note)
- wiki/INDEX.md (6 new bullets across Projects, Systems, Organizations, Concepts, Ideas, Meetings)
Files moved:
- INBOX/meeting_2026.05.12_aviad_jose.txt → raw/meetings/meeting_2026.05.12_aviad_jose.txt

## [2026-05-12] lint | seed Entities/Organizations + Teams + Concepts
- wiki/Entities/Organizations/* (6 new: Trustwave, AT&T, Anthropic, LangChain Inc., Microsoft, MITRE)
- wiki/Entities/Teams/* (8 new: Data Science Team, Engineering, Security Research, SOC, Labs, Spider Labs, Phoenix Team, Fusion 2 Team)
- wiki/Entities/Concepts/* (8 new: LoRA, Prompt Injection, RAG, Sigma Rule Format, Identity Correlation, Multi-Agent Orchestration, LLM Hallucination, 4-bit Quantization)
- wiki/INDEX.md (3 new sections)

## [2026-05-12] lint | round 2 — AA+BB+CC+EE
- wiki/Entities/Projects/AI Assistant.md (lead → Guy Kassorla; systems backfilled)
- wiki/Entities/Projects/IRCA.md (lead → Guy Kassorla)
- wiki/Entities/Projects/UEBA.md (lead → Guy Kapach per user)
- wiki/Entities/Projects/Owlint-Sigma.md (systems backfilled)
- wiki/Entities/Projects/OWLINT.md (systems backfilled)
- wiki/Entities/Projects/AIDRA.md (systems backfilled)
- wiki/Entities/Systems/Palo Alto.md (new)
- wiki/Entities/Systems/ServiceNow.md (new)
- wiki/Entities/Systems/Velociraptor.md (new)
- wiki/Entities/Systems/STIX.md (new)
- wiki/Entities/Systems/Alert Logic.md (related_decisions added)
- wiki/Decisions/2026-05-06 — DS Team Takes Over Spider Labs Orphaned Projects.md (related_systems added)
- wiki/Meetings/2026-04-30 — Aviad and Pawel intro.md (related_systems added)
- wiki/INDEX.md (4 new System bullets)

## [2026-05-12] lint | D+E: add 6 Systems (orphan-concept resolution)
- wiki/Entities/Systems/Langfuse.md (new)
- wiki/Entities/Systems/LangGraph.md (new)
- wiki/Entities/Systems/Cursor.md (new)
- wiki/Entities/Systems/Alert Logic.md (new)
- wiki/Entities/Systems/Tipper.md (new)
- wiki/Entities/Systems/BDP.md (new)
- wiki/INDEX.md (Entities/Systems section — 6 new bullets inserted alphabetically)

## [2026-05-12] lint | tools: skip fenced spans in stale-link check
- tools/lint/check_stale_links.py (function rewritten + fenced-span stripper)
- tools/lint/tests/test_stale_links.py (3 new tests; 5/5 pass)
- baseline: total 35 → 3 (32 false-positive stale-links eliminated)

## [2026-05-12] lint | cross-ref backfill (A+B+C)
- wiki/Entities/Systems/Mail Marshal.md (new)
- wiki/Entities/People/*.md (Mentions backfilled from Meeting participants — 9 people)
- wiki/Entities/People/Aviad Cohen.md (related_projects populated)
- wiki/Entities/People/Phil Hay.md (related_projects checked — no project lead/team match, stays empty)
- wiki/Entities/People/Santiago Cortes Diaz.md (related_projects checked — no project lead/team match, stays empty)
- wiki/Meetings/2026-04-27 — Aviad and Phil intro.md (related_systems added)
- wiki/Decisions/2026-04-27 — Email Attachments as First ML Collaboration Target.md (related_systems added)
- wiki/Decisions/2026-04-27 — ML Outputs as Mail Marshal Scoring Inputs.md (related_systems added)

## [2026-05-11] ingest | DS Team — General Knowledge & Projects Notion Doc
- wiki/Sources/data-science-team-knowledge.md (new)
- wiki/Entities/People/Ortal Keizman.md (new)
- wiki/Entities/People/Tonny Pham.md (new)
- wiki/Entities/People/Hila Karmi.md (new)
- wiki/Entities/People/Atchuta Meka.md (new)
- wiki/Entities/People/Nitzan Milchin.md (new)
- wiki/Entities/People/Shoshana Avni.md (new)
- wiki/Entities/People/Guy Kapach.md (new)
- wiki/Entities/Systems/AIAV.md (new)
- wiki/Entities/Systems/Chronicle.md (new)
- wiki/Entities/Systems/Redpanda.md (new)
- wiki/Entities/Systems/ClickHouse.md (new)
- wiki/Entities/Systems/XIS.md (new)
- wiki/Entities/Systems/Fusion 2.md (new)
- wiki/Entities/Projects/Rules Quality.md (new)
- wiki/Entities/Projects/Smart Asset Correlation.md (new)
- wiki/Entities/Projects/XDR Correlation for Phoenix.md (new)
- wiki/Entities/People/Itamar Hershko.md (Mentions + related_projects)
- wiki/Entities/People/Guy Kassorla.md (Mentions + related_projects)
- wiki/Entities/People/Hen Ashkenazi.md (Mentions + related_projects)
- wiki/Entities/People/Ziv Mador.md (Mentions)
- wiki/Entities/Systems/Core.md (seeds path retargeted INBOX → raw/data_science_drive)
- wiki/Entities/Systems/Phoenix.md (seeds path retargeted INBOX → raw/data_science_drive)
- wiki/Entities/Systems/Azure AI Foundry.md (seeds path retargeted INBOX → raw/data_science_drive)
- wiki/Entities/Systems/Sage.md (seeds path retargeted INBOX → raw/data_science_drive)
- wiki/Entities/Projects/META.md (Phoenix variant + Mentions)
- wiki/Entities/Projects/NGAV.md (Phoenix variant + Mentions)
- wiki/Entities/Projects/AI Assistant.md (Phoenix variant + Mentions)
- wiki/Entities/Projects/IRCA.md (Mentions)
- wiki/Entities/Projects/AIDRA.md (Mentions)
- wiki/Entities/Projects/UEBA.md (Mentions)
- wiki/Entities/Projects/Incident Investigation (for Fusion 2).md (Mentions)
- wiki/Entities/Projects/Owlint-Sigma.md (Tipper section + Mentions)
- wiki/🔥 Hot Notes/Active Focus.md (Q2 priorities populated)
- wiki/INDEX.md (new entries + index refresh)
- wiki/Log/pulse.md (direction flipped to prepend; convention note added)
- wiki/Log/wiki-ops.md (append-only preamble + `append_only: true` frontmatter)
- CLAUDE.md (log rule extended to cover pulse.md)
- .claude/commands/braindump.md (Append → Prepend wording)
Files moved:
- INBOX/converted/data-science-main.md → raw/data_science_drive/data-science-main.md
- INBOX/converted/data-science-projects.md → raw/data_science_drive/data-science-projects.md

## [2026-05-11] bootstrap | initial wiki content
- wiki/Entities/People/* (50 new)
- wiki/Entities/Projects/* (28 new)
- wiki/Entities/Systems/* (11 new)
- wiki/Meetings/* (6 new)
- wiki/Decisions/* (7 extracted)
- wiki/Connections/* (4 extracted)
- wiki/Log/INDEX.md (new)
- wiki/🔥 Hot Notes/Brain Architecture.md (new)
- wiki/Log/wiki-ops.md (new)
- wiki/Log/pulse.md (new)
