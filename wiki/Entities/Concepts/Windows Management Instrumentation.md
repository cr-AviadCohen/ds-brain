---
title: Windows Management Instrumentation
type: concept
tags: [concept, wiki]
domain: security
related_projects: ["[[AI Assistant]]", "[[Hunter]]", "[[NGAV]]"]
related_systems: ["[[Active Directory]]"]
last_updated: 2026-05-13
---

# Windows Management Instrumentation

> Windows management API ("WMI") with namespaces, classes, and an event-subscription engine — a built-in admin tool that doubles as an attacker's [[Persistence]] and [[Lateral Movement]] channel.

## What it is

WMI exposes system state (processes, services, hardware) via WQL queries and supports permanent event-subscription consumers (`__EventFilter` / `CommandLineEventConsumer`). Attackers use `wmic` / PowerShell's `Get-CimInstance` for recon, and `Win32_Process.Create` over DCOM/WinRM for remote execution without dropping a binary. Detection relies on registry/MOF auditing, ETW provider `Microsoft-Windows-WMI-Activity`, and process-tree heuristics.

## Why we care

- [[NGAV]] behavioural rules score `wmic` + WMI-event-subscription creations as persistence + execution evidence.
- [[Hunter]] hunting queries pivot on WMI lateral-movement patterns surfacing in customer telemetry.
- [[AI Assistant]] analyst flows must reason over WMI-driven attack steps without losing the per-host process tree.
- WMI Event Subscriptions are a classic invisible [[Persistence]] mechanism that survives reboots.

## Manifestations

- 2026-05-13 — Catalogued during /lint orphan-concept seed.

## Open questions

- Coverage of `Microsoft-Windows-WMI-Activity` ETW events in Phoenix Agent vs Core sensor.
