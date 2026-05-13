---
title: Event Tracing for Windows
type: system
tags: [system, wiki]
owner: Microsoft
vendor: Microsoft
integration_surface: [kernel-providers, user-mode-consumers]
related_projects: ["[[NGAV]]", "[[Phoenix Review]]"]
last_updated: 2026-05-13
---

# Event Tracing for Windows

> Kernel + user-mode tracing facility ("ETW") that emits high-volume structured events from Windows OS components and applications — Cybereason's primary low-level Windows telemetry source.

## Owner / vendor

Microsoft (built-in to Windows since 2000).

## Integration surface

- **Providers** — kernel and user-mode components publish events to ETW sessions (Microsoft-Windows-Threat-Intelligence, Microsoft-Windows-Kernel-Process, Microsoft-Windows-PowerShell, AMSI, etc.).
- **Consumers** — EDR agents subscribe to provider GUIDs and ingest the event stream in real time.
- **Sessions** — `logman`, ETW APIs, or kernel-driver consumers can register without writing to disk.

## Data flow

Provider → Session buffer (kernel) → Real-time consumer (Cybereason sensor) → Sensor pipeline → [[Phoenix]] / [[Core]] backend.

## Current usage

[[NGAV]] and the Cybereason sensor read ETW for process / thread / image-load / DLL / registry / network telemetry, plus the Threat-Intelligence provider (TI-ETW) for AMSI / [[Local Security Authority]] / [[Antimalware Scan Interface]] events. [[Phoenix Review]] noted ETW provider coverage and disable-vector gaps in the Phoenix Agent.

## Known issues

- ETW providers can be silently disabled by privileged attackers (ETWTI bypass / patching `EtwEventWrite`); detection requires kernel-driver heart-beat or provider-ID monitoring.
- Event volume is high enough that providers must be aggressively filtered server-side.

## Related entities

[[NGAV]], [[Phoenix]], [[Core]], [[Antimalware Scan Interface]], [[Local Security Authority]]

## Open questions

- Coverage map of which ETW providers the Phoenix Agent currently subscribes to vs the Core sensor.
