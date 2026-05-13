---
title: Code Obfuscation
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[AIDRA]]", "[[NGAV]]", "[[SFT-PS]]", "[[Assembly LLM]]"]
related_systems: ["[[Antimalware Scan Interface]]"]
last_updated: 2026-05-13
---

# Code Obfuscation

> Transformations applied to a malicious payload — encoding, packing, string-splitting, control-flow flattening, polymorphism — designed to defeat static signatures while preserving runtime behaviour.

## What it is

Two big buckets. **Script-level obfuscation**: PowerShell base64 + `IEX`, `-EncodedCommand`, char-array concatenation, alias substitution, invoke-expression chains; JavaScript packer output; Office-macro VBA char-code obfuscation. **Binary-level obfuscation**: runtime packers (UPX, Themida, VMProtect), opaque predicates, mixed-mode native + .NET loaders, syscall stub randomisation. Defenders use deobfuscation engines, AMSI hooks at the execution boundary, and runtime-only behavioural signals.

## Why we care

- [[AIDRA]]'s Deobfuscation agent is one of the seven specialised agents — string + control-flow recovery on PowerShell.
- [[SFT-PS]] fine-tunes an LLM for classifying obfuscated PowerShell against the same target classes [[AIDRA]] reasons over.
- [[NGAV]] fileless-protection logic relies on [[Antimalware Scan Interface]] to see post-deobfuscation buffers PowerShell would otherwise hide.
- [[Assembly LLM]] tackles the binary-side counterpart — recover semantics from packed/obfuscated PE machine code.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Shared obfuscation-taxonomy across [[AIDRA]], [[SFT-PS]], and [[Assembly LLM]] — labels currently diverge.
