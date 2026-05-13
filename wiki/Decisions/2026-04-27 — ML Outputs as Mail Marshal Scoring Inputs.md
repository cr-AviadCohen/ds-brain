---
title: ML Outputs as Mail Marshal Scoring Inputs
type: decision
tags: [decision, wiki]
date: 2026-04-27
deciders: ["[[Aviad Cohen]]", "[[Phil Hay]]"]
status: accepted
related_projects: []
related_systems: ["[[Mail Marshal]]"]
last_updated: 2026-05-12
---

# ML Outputs as Mail Marshal Scoring Inputs — 2026-04-27

## Context

During the 2026-04-27 Aviad/Phil intro, Phil walked through how URL Deep, PageML, and Defense feed Mail Marshal. He was explicit that no ML model blocks email on its own — outputs are weighted scoring inputs (e.g., a confident URL Deep verdict contributes ~22 points toward a ~60-point conviction threshold), and structural rules plus threat indicators must also fire.

## Decision

Keep ML model output as weighted scoring inputs into Mail Marshal rather than autonomous block actions. Any future DS/ML collaboration on attachments or other surfaces will plug into this existing scoring system, not bypass it.

## Why

The weighted scoring architecture lets multiple weak signals combine into a high-confidence verdict without giving any single model autonomous authority to block customer mail. This bounds the blast radius of any one model's false positives and matches how Mail Marshal already integrates URL Deep, PageML, and Defense.

## Alternatives considered

- Autonomous ML block actions — rejected: a single false positive would impact customer mail flow directly with no compensating signal.

## Consequences

- DS-team work on Mail Marshal-adjacent ML must be evaluated against its marginal contribution to the scoring threshold, not as a stand-alone classifier.
- Threshold calibration and per-signal weight tuning remain the integration concern, not "should the model block?".
- Aligns with the broader pattern that ML outputs feed scoring/triage rather than terminal enforcement.

## Open questions

- How are signal weights re-tuned when a new model joins the scoring stack?
- How is calibration drift handled across the existing three production ML signals?
