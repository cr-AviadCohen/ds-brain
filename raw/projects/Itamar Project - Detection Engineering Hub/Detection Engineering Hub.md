# Detection Engineering Hub

Welcome to the Detection Engineering Hub
Documentation Index

---

### Welcome to the Detection Engineering Hub

This is the central documentation hub for the Detection Engineering Hub platform — a unified system for managing the complete lifecycle of detection rule content. It replaces scattered scripts, manual workflows, and tribal knowledge with a structured, auditable process.

Git - https://github.com/cybereason-labs/itamar-h/tree/Detection-Engineering-HUB

> 🎯 Mission: Upload, organize, validate, test, and publish detection rules with full audit trails across multiple engines and formats.

👥
Target Users
SOC Teams, Threat Intel Analysts, Detection Engineers
🔧
Tech Stack
FastAPI + Streamlit + PostgreSQL + Docker + Helm

---

### Documentation Index

All sub-pages below provide detailed documentation for every aspect of the platform:

Section
	
Description

Architecture Overview
	
System architecture, tech stack, deployment modes, and project structure

Detection Engines & Rule Formats
	
BEP, Fileless, VPP, VFP engines and supported rule formats (YARA, Sigma, JSON, BOSS)

API Reference
	
Complete REST API documentation — all endpoints, parameters, and responses

Release Workflow
	
End-to-end release lifecycle: upload, parse, validate, publish, confirm

Streamlit UI Guide
	
All frontend pages, features, navigation, and design system

Authentication & Authorization
	
JWT auth, 6 role levels, RBAC, and audit logging

Integrations
	
VirusTotal Retrohunt, Confluence KB, Jira Epics, Jupyter Notebooks

Admiral Rule Storage
	
Dynamic filesystem-based rule package storage and management

Database Schema
	
All models, tables, enums, indexes, and relationships

Deployment Guide
	
POC, Docker Compose, and Kubernetes Helm deployment options

CI/CD Pipeline
	
GitHub Actions workflows, testing, security scanning, Helm linting

Configuration Reference
	
Environment variables, .env setup, MCP servers, and settings

Backend Services Reference
	
All service layer functions: parser, validator, diff, commit, verification, Jira, VT, Confluence, Jupyter

Streamlit Frontend Internals
	
Design system, page renderers, session state, helper functions, CSS variables, dependencies
- 📄 [Architecture Overview](https://www.notion.so/Architecture-Overview-339ae23bae1d81bf96a3c42fec9a1da8?pvs=25)
- 📄 [Detection Engines & Rule Formats](https://www.notion.so/Detection-Engines-Rule-Formats-339ae23bae1d8150b728ca9b144c4448?pvs=25)
- 📄 [API Reference](https://www.notion.so/API-Reference-339ae23bae1d819b8d9cd8996cfb00ee?pvs=25)
- 📄 [Release Workflow](https://www.notion.so/Release-Workflow-339ae23bae1d81648061fd36c7575595?pvs=25)
- 📄 [Streamlit UI Guide](https://www.notion.so/Streamlit-UI-Guide-339ae23bae1d81a49f16e03523873eaa?pvs=25)
- 📄 [Authentication & Authorization](https://www.notion.so/Authentication-Authorization-339ae23bae1d81ab8bced35aa9107607?pvs=25)
- 📄 [Integrations](https://www.notion.so/Integrations-339ae23bae1d815e9828fed46874d636?pvs=25)
- 📄 [Admiral Rule Storage](https://www.notion.so/Admiral-Rule-Storage-339ae23bae1d81d3b4f0e1f4091953db?pvs=25)
- 📄 [Database Schema](https://www.notion.so/Database-Schema-339ae23bae1d81fea05ae8232fccafe7?pvs=25)
- 📄 [Deployment Guide](https://www.notion.so/Deployment-Guide-339ae23bae1d818d8cd5c64f5aafa8f9?pvs=25)
- 📄 [CI/CD Pipeline](https://www.notion.so/CI-CD-Pipeline-339ae23bae1d81db9837ddd0f3a77830?pvs=25)
- 📄 [Configuration Reference](https://www.notion.so/Configuration-Reference-339ae23bae1d8161aa20f64bbbf6586b?pvs=25)
- 📄 [Backend Services Reference](https://www.notion.so/Backend-Services-Reference-339ae23bae1d81509b2fdbda88417132?pvs=25)
- 📄 [Streamlit Frontend Internals](https://www.notion.so/Streamlit-Frontend-Internals-339ae23bae1d81ca8d7ce24f93a6791f?pvs=25)

---

# Subpages Content

---

## Architecture Overview

#### System Architecture

The Detection Engineering Hub follows a layered architecture with multiple deployment modes and UI options.

##### High-Level Diagram

```
graph TD
	A["Streamlit UI (Port 9510/8501)"] --> C["FastAPI Backend (Port 9000/8000)"]
	B["Next.js Frontend (Port 3000)"] --> C
	C --> D["PostgreSQL / SQLite"]
	C --> E["Remote JupyterLab"]
	C --> F["VirusTotal API"]
	C --> G["Confluence API"]
	C --> H["Jira API"]
	C --> I["Admiral Storage (Filesystem)"]

Streamlit UI (Port 9510/8501)

FastAPI Backend (Port 9000/8000)

Next.js Frontend (Port 3000)

PostgreSQL / SQLite

Remote JupyterLab

VirusTotal API

Confluence API

Jira API

Admiral Storage (Filesystem)

​
```

---

#### Tech Stack

Layer
	
Technology
	
Version

Backend API
	
FastAPI + Uvicorn
	
0.115.6

Primary UI
	
Streamlit
	
>= 1.38.0

Secondary UI
	
Next.js (React)
	
Optional, disabled by default

ORM
	
SQLAlchemy
	
2.0.36

Database
	
PostgreSQL 16 (prod) / SQLite (POC)
	
16 Alpine

Validation
	
Pydantic
	
2.10.4

YARA Parsing
	
Plyara
	
2.2.5

Sigma Parsing
	
PyYAML
	
6.0.2

Notebook Execution
	
Papermill + Jupyter Client
	
2.6.0 / 8.6.3

Charts
	
Plotly
	
>= 5.20.0

Auth
	
python-jose (JWT) + bcrypt
	
3.3.0 / 4.2.1

HTTP Client
	
httpx
	
0.28.1

Containerization
	
Docker + Docker Compose
	
-

Orchestration
	
Kubernetes via Helm
	
Chart 0.1.0

---

#### Project Structure

```
Detection_Engeneering_Hub/
├── backend/
│   ├── app/
│   │   ├── api/routes/         # 16 API route modules
│   │   ├── core/               # config, database, auth
│   │   ├── models/             # SQLAlchemy ORM models
│   │   ├── schemas/            # Pydantic request/response schemas
│   │   ├── services/           # Business logic (parser, validator, VT)
│   │   └── main.py             # FastAPI app initialization
│   ├── tests/                  # 121 pytest tests
│   ├── seed.py                 # Demo data seeder
│   ├── requirements.txt
│   └── Dockerfile
├── frontend_streamlit/
│   ├── app.py                  # Main Streamlit app (~10,000 lines)
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/                   # Next.js (optional)
├── helm/detection-hub/         # Kubernetes Helm chart
├── .github/workflows/          # CI/CD pipelines
├── docker-compose.yml
├── run-poc.sh                  # POC launcher script
└── .mcp.json                   # MCP server configs

​
```

---

#### FastAPI Application Setup (main.py)

The FastAPI app is initialized with:
- Title: settings.APP_NAME ("Detection Engineering Hub")
- Version: 0.1.0
- CORS Middleware: Reads CORS_ORIGINS env, supports STREAMLIT_ORIGIN and FRONTEND_ORIGIN overrides, defaults to localhost:3000, localhost:8500, localhost:8501, localhost:8502, localhost:9510

##### Router Mount Table

Prefix
	
Module
	
Description

/health
	
health.router
	
Liveness probe (no prefix)

/api/auth
	
auth.router
	
Login, register, me

/api/upload
	
upload.router
	
File parsing

/api/releases
	
releases.router
	
Release CRUD and publish

/api/compare
	
compare.router
	
Release comparison

/api/history
	
history.router
	
Release history + audit log

/api/statistics
	
statistics.router
	
Analytics endpoints

/api/confluence
	
confluence.router
	
Knowledge base

/api/validation
	
validation.router
	
Rule syntax validation

/api/virustotal
	
virustotal.router
	
Retrohunt integration

/api/admin
	
admin.router
	
Engine/repo management

/api/engines
	
engines.router
	
Public engine listing

/api/notebook
	
notebook.router
	
Local notebook execution

/api/notebook/remote
	
notebook_remote.router
	
Remote Jupyter execution

/api/admiral
	
admiral.router
	
File storage operations

---

#### Core Dependencies (Python)

Package
	
Version
	
Purpose

fastapi
	
0.115.6
	
Web framework

uvicorn[standard]
	
0.34.0
	
ASGI server

sqlalchemy
	
2.0.36
	
ORM

alembic
	
1.14.1
	
Database migrations

psycopg2-binary
	
2.9.10
	
PostgreSQL driver

pydantic
	
2.10.4
	
Data validation

pydantic-settings
	
2.7.1
	
Config from .env

python-multipart
	
0.0.20
	
File upload support

httpx
	
0.28.1
	
Async HTTP client

bcrypt
	
4.2.1
	
Password hashing

python-jose[cryptography]
	
3.3.0
	
JWT tokens

plyara
	
2.2.5
	
YARA parsing

pyyaml
	
6.0.2
	
Sigma/YAML parsing

markdownify
	
0.13.1
	
HTML to Markdown

papermill
	
2.6.0
	
Notebook execution

nbconvert
	
7.16.4
	
Notebook conversion

nbformat
	
>= 5.10.0
	
Notebook format handling

jupyter-client
	
8.6.3
	
Jupyter kernel communication

ipykernel
	
6.29.5
	
IPython kernel

websockets
	
>= 12.0
	
WebSocket support

websocket-client
	
>= 1.6.0
	
WS client for Jupyter

plotly
	
>= 5.20.0
	
Interactive charts

pandas
	
>= 2.1.0
	
Data processing

pyzipper
	
>= 0.3.6
	
ZIP file handling

streamlit
	
>= 1.38.0
	
Primary UI framework

pytest
	
8.3.4
	
Testing framework

pytest-asyncio
	
0.24.0
	
Async test support

---

#### Three Deployment Modes

> 💡 POC (Proof of Concept) — SQLite, single process, run-poc.sh. Ports: 9000 (API), 9510 (UI)

> 💡 Docker Compose — PostgreSQL + multi-container stack. Ports: 5432 (DB), 8000 (API), 8501 (Streamlit), 3000 (Next.js)

> 💡 Kubernetes (Helm) — Production-ready with Helm chart templates, ingress, secrets, and replicas

---

## Detection Engines & Rule Formats

#### Detection Engines

The Hub supports four core detection engines, each targeting different threat categories and supporting specific rule formats.

Engine
	
Full Name
	
Supported Formats
	
Purpose

BEP
	
Behavioral Endpoint Protection
	
Sigma
	
Behavioral detection via log-based correlation rules

Fileless
	
Fileless Detection
	
YARA, .NET
	
Fileless threat detection with notebook automation

VPP
	
Variant Payload Prevention
	
YARA, BOSS
	
Payload variant detection and prevention

VFP
	
Variant File Protection
	
YARA
	
File-based variant threat detection

---

#### Rule Formats

##### YARA Rules

Parsed using the plyara library. Extracts rule name, tags, metadata, and string counts.

Required Metadata Fields:
- id — Unique rule identifier
- score — Severity score (0–100)
- author — Rule author
- tags — Classification tags
- stability — One of: verified, experimental, stable, deprecated, test
- mitre — MITRE ATT&CK reference
- date — Creation/modification date
- description — What the rule detects

##### Sigma Rules

Parsed using PyYAML. Supports multi-document YAML files.

Required Fields:
- title, id, author, description, date
- logsource — Must have both category AND product
- detection — Detection logic block
- level — One of: low, medium, high, critical, informational
- tags — Must match MITRE ATT&CK format: attack.tNNNN or attack.taNNNN

##### JSON Rules

Accepts array of rules or object with "rules" key. Extracts name, id, title from each rule object. Full metadata preserved as JSON.

##### BOSS Rules

Treated as opaque units — one file equals one rule. No internal parsing, basic text validation only.

##### Supplemental Content

Shipped alongside rules but not parsed as detection logic:
- .ps1, .psm1, .psd1 (PowerShell scripts)
- .txt, .xml, .csv, .md, .bat, .sh

---

#### Syntax Validation

The Hub provides instant syntax validation for pasted rules:

> 💡 YARA Validation: Checks required metadata fields, score range (0–100), stability values, and structural syntax via plyara.

> 💡 Sigma Validation: Checks required fields, logsource structure, detection block presence, level values, and MITRE tag format.

Validation is available both via API (POST /api/validation/validate) and the Streamlit UI Syntax Validation page.

---

## API Reference

#### Complete REST API Documentation

The FastAPI backend exposes a comprehensive REST API. All endpoints (except health and auth) require JWT Bearer token authentication.

Base URL: http://localhost:8000 (Docker) or http://localhost:9000 (POC)

---

#### Authentication

Method
	
Endpoint
	
Description

POST
	
/api/auth/login
	
Login with username/password, returns JWT token

POST
	
/api/auth/register
	
Create new user account

GET
	
/api/auth/me
	
Get current authenticated user info

---

#### Release Management

Method
	
Endpoint
	
Description

POST
	
/api/releases/prepare
	
Upload rules, parse, generate commit msg, save as pending. Validates 10MB/file, 50MB total. Computes diff, proposes semantic version, generates AI summary.

GET
	
/api/releases/{release_id}
	
Fetch full release details with all rules

GET
	
/api/releases/
	
List all releases (paginated)

POST
	
/api/releases/{release_id}/confirm
	
Confirm publish with commit hash → marks as PUBLISHED, triggers Jira Epic

GET
	
/api/releases/{release_id}/commit-message
	
Get suggested commit text

GET
	
/api/releases/{release_id}/git-instructions
	
Get manual git steps

---

#### Release Comparison & History

Method
	
Endpoint
	
Description

GET
	
/api/compare/{release_a_id}/{release_b_id}
	
Side-by-side diff of two releases (added, removed, modified rules)

GET
	
/api/history/releases
	
6+ months of releases, filterable by engine/type

GET
	
/api/history/audit
	
Complete audit log of all actions

---

#### File Upload & Parsing

Method
	
Endpoint
	
Description

POST
	
/api/upload/parse
	
Parse a single file and extract rules

POST
	
/api/upload/parse-multiple
	
Parse multiple files with combined results

---

#### Rule Validation

Method
	
Endpoint
	
Description

POST
	
/api/validation/validate
	
Paste rule content → instant syntax check. Auto-detects YARA vs Sigma format.

---

#### VirusTotal Retrohunt

Method
	
Endpoint
	
Description

POST
	
/api/virustotal/retrohunt
	
Submit YARA rule to VirusTotal retrohunt

GET
	
/api/virustotal/retrohunt
	
List all retrohunt jobs

GET
	
/api/virustotal/retrohunt/{job_id}
	
Check job status

GET
	
/api/virustotal/retrohunt/{job_id}/matches
	
Browse/filter file matches with pagination

Supports X-VT-Api-Key header for per-request API keys. Falls back to demo mode with mock data if no key configured.

---

#### Confluence Knowledge Base

Method
	
Endpoint
	
Description

GET
	
/api/confluence/pages
	
List preset documentation pages

GET
	
/api/confluence/search
	
Search Confluence by query string

GET
	
/api/confluence/page/{page_id}
	
Fetch full page content (HTML → Markdown)

POST
	
/api/confluence/credentials
	
Save Confluence Cloud credentials to .env

---

#### Statistics & Analytics

Method
	
Endpoint
	
Description

GET
	
/api/statistics/overview
	
Release velocity, total rules, engine count

GET
	
/api/statistics/rules-over-time
	
Time-series chart data (12–60 months)

GET
	
/api/statistics/by-format
	
Rules breakdown by format (JSON/YARA/Sigma/BOSS)

GET
	
/api/statistics/by-type
	
Sprint vs hot_fix breakdown

GET
	
/api/statistics/by-status
	
Draft/pending/published/failed counts

GET
	
/api/statistics/by-engine
	
Releases per engine (30–365 day range)

GET
	
/api/statistics/contributors
	
Top rule creators leaderboard

---

#### Local Notebook Execution

Method
	
Endpoint
	
Description

POST
	
/api/notebook/run
	
Upload .ipynb  • rule files + supplemental ZIPs + env_vars JSON. Executes via Papermill in background thread. Returns {run_id, status: "running"}.

GET
	
/api/notebook/run/{run_id}/poll
	
Poll output lines since ?after=N. Returns {lines, next_after, done, status, exit_code}.

GET
	
/api/notebook/run/{run_id}/status
	
Quick status: {run_id, status, done, lines_count, exit_code}.

> ⚙️ In-memory store _RUNS[run_id] tracks: status, output lines, done flag, error, exit_code. Live watcher polls output notebook every 3s. Temp dir cleaned 5 min after completion. Timeout: 7200s.

---

#### Remote Jupyter Execution

Method
	
Endpoint
	
Description

POST
	
/api/notebook/remote/test-connection
	
Test JupyterLab auth + optional notebook access. Returns {ok, error, diag}.

POST
	
/api/notebook/remote/clear-hub-packages
	
Clear hub_packages directory on remote server. Returns {ok, removed_count, removed_names}.

POST
	
/api/notebook/remote/prepare-and-launch
	
Upload packages, inject env vars + PowerShell functions into cells, clear outputs, save notebook, return JupyterLab URL with cell fragment.

POST
	
/api/notebook/remote/list-outcome
	
List outcome files from notebook execution directory.

POST
	
/api/notebook/remote/download-outcome
	
Download outcome files as ZIP (StreamingResponse).

POST
	
/api/notebook/remote/approve-outcome
	
Approve outcome for staging. Returns {staging_id, staging_dir, files, draft_pr}.

POST
	
/api/notebook/remote/fetch-results
	
Fetch cell-by-cell results. Detects kernel busy state, polls for updates. Returns {ok, cells, summary, kernel_busy}.

POST
	
/api/notebook/remote/session
	
Create full Jupyter session: auth, upload notebook + zips, start kernel, connect WebSocket. Returns {session_id, cells, kernel_id}.

> 🔌 Remote execution uses JupyterRemoteClient (REST + session cookies + XSRF) and KernelConnection (WebSocket Jupyter wire protocol). Sessions stored in _SESSIONS[session_id].

---

#### Admiral Storage

Method
	
Endpoint
	
Description

POST
	
/api/admiral/mkdir
	
Create directory hierarchy

GET
	
/api/admiral/browse
	
List directory contents

POST
	
/api/admiral/upload
	
Upload JSON files or ZIP archives

GET
	
/api/admiral/download-file
	
Download single file

GET
	
/api/admiral/download-dir
	
Download directory as ZIP

POST
	
/api/admiral/move
	
Move file/directory

GET
	
/api/admiral/all-dirs
	
Recursive directory listing

DELETE
	
/api/admiral/rm
	
Delete file or directory

---

#### Admin & System

Method
	
Endpoint
	
Description

GET
	
/health
	
Liveness probe (no auth required)

GET
	
/api/engines
	
List all engines (any authenticated user)

GET
	
/api/admin/engines
	
List engines (admin only)

POST
	
/api/admin/engines
	
Create new engine (admin only)

GET
	
/api/admin/repositories
	
List repositories (admin only)

POST
	
/api/admin/repositories
	
Create repository (admin only)

---

#### Error Codes

Code
	
Meaning

400
	
Bad request (validation error, file size exceeded)

401
	
Unauthorized (missing or invalid JWT)

403
	
Forbidden (insufficient role permissions)

404
	
Resource not found

413
	
Payload too large (10MB/file, 50MB total)

#### Pagination

All list endpoints support limit (max 100–500) and offset parameters. Time-based endpoints accept months (1–60) for range filtering.

---

#### Role Requirements by Endpoint

Endpoint Group
	
Required Roles

/api/releases/prepare, /confirm
	
RESEARCHER, RELEASE_MANAGER, ADMIN

/api/releases/{id}, /commit-message, /git-instructions
	
RESEARCHER, RELEASE_MANAGER, MANAGER, VIEWER, ADMIN

/api/virustotal/*
	
RESEARCHER, RELEASE_MANAGER, ADMIN

/api/confluence/credentials
	
ADMIN, MANAGER, RELEASE_MANAGER, RESEARCHER

/api/admin/*
	
ADMIN only

All other endpoints
	
Any authenticated user

---

#### Request/Response Models (Pydantic Schemas)

<details><summary>Authentication Schemas</summary>

</details>

<details><summary>Release Schemas</summary>

</details>

<details><summary>Upload & Validation Schemas</summary>

</details>

<details><summary>Diff & Version Schemas</summary>

</details>

<details><summary>Commit & Verification Schemas</summary>

</details>

<details><summary>Compare & History Schemas</summary>

</details>

<details><summary>VirusTotal Schemas</summary>

</details>

<details><summary>Engine & Repository Schemas</summary>

</details>

---

## Release Workflow

#### End-to-End Release Lifecycle

The Detection Engineering Hub manages the full release lifecycle for detection rules. A critical design principle: the Hub does NOT execute git operations — users manually run git commands and paste commit hashes for verification.

---

#### Workflow Diagram

```
flowchart TD
	A["Upload Rule Files"] --> B["Parse & Extract Rules"]
	B --> C["Validate Syntax"]
	C --> D["Prepare Release"]
	D --> E["Generate Commit Message"]
	E --> F["User Runs Git Commands Manually"]
	F --> G["User Pastes Commit Hash"]
	G --> H["Confirm Publish"]
	H --> I["Status: PUBLISHED"]
	I --> J["Jira Epic Created (Optional)"]

Upload Rule Files

Parse & Extract Rules

Validate Syntax

Prepare Release

Generate Commit Message

User Runs Git Commands Manually

User Pastes Commit Hash

Confirm Publish

Status: PUBLISHED

Jira Epic Created (Optional)

​
```

---

#### Step-by-Step Process

##### Step 1: Upload & Parse
- User uploads rule files (JSON, YARA, Sigma, BOSS) via Streamlit UI or API
- Hub parses each file, extracts individual rules, and detects format
- Returns list of rules with any validation errors or warnings
- Supports supplemental content (PowerShell scripts, configs)

##### Step 2: Prepare Release

POST /api/releases/prepare with files + engine + release type
- Computes diff against previous release for the same engine
- Proposes semantic version (e.g., 1.0.0 → 1.1.0 for sprint, 1.0.1 for hotfix)
- Generates commit message template
- Generates git instructions (text only — no execution)
- Creates deterministic AI summary from structured data
- Saves release as status = pending_publish

##### Step 3: Manual Git Operations

The Hub provides copy-paste instructions. The user runs them locally:

```
git checkout main
git pull origin main
git add <files>
git commit -m "<generated message>"
git push origin main

​
```

User then copies the resulting commit hash.

##### Step 4: Confirm Publish

POST /api/releases/{id}/confirm with the commit hash
- Hub verifies hash format (7–64 hex characters)
- Sets status = published
- Creates Jira Epic if Jira credentials are configured
- Regenerates AI summary with published state
- Full audit log entry recorded

---

#### Why Manual Git?

> 💡 Security & Auditability: Preventing unauthorized commits, allowing human verification, preserving version control auditability, and supporting multi-approval workflows.

---

#### Release Types

Type
	
Version Bump
	
Use Case

Sprint
	
Minor (1.0.0 → 1.1.0)
	
Regular scheduled releases with multiple rules

Hot Fix
	
Patch (1.0.0 → 1.0.1)
	
Urgent out-of-cycle fixes for critical detections

---

#### Release Statuses

Status
	
Meaning

draft
	
Initial state, rules uploaded but not finalized

pending_publish
	
Release prepared, awaiting manual git commit and hash confirmation

published
	
Commit hash confirmed, release is live

failed
	
Release process encountered an error

---

#### Diff & Comparison

Every release computes a diff against the previous release for the same engine:
- Added rules — New rules not in the previous release
- Removed rules — Rules that existed before but are no longer present
- Modified rules — Rules with the same name but different content hash

Users can also compare any two releases side-by-side via GET /api/compare/{a}/{b}.

---

#### AI Summaries

Release summaries are deterministic (no LLM calls in production):
- Generated from structured data: version, status, rule count, change breakdown, formats
- Regenerated when release status changes
- Includes: total rules, added/modified/removed counts, engine, type, and version info

---

## Streamlit UI Guide

#### Primary User Interface

The Streamlit frontend is the main user-facing console for the Detection Engineering Hub (~10,000 lines of code). It features a professional design system with sidebar navigation and role-based page filtering.

---

#### Design System

Element
	
Value

Body Font
	
Inter

Code Font
	
JetBrains Mono

Theme
	
Professional Grey + Purple accents

Layout
	
Responsive grid with badges, status indicators

---

#### Pages

##### Login
- JWT token exchange with backend
- Session persistence via Streamlit session state
- Role displayed after login

##### Dashboard
- Pending publishes count
- Recent activity feed
- Quick statistics overview
- Role-based widget visibility

##### New Release (Multi-Step Wizard)

> 💡 A guided wizard that walks users through the entire release process:
> Upload — Drag & drop rule files
> Parse — Auto-detect format and extract rules
> Validate — Check syntax and metadata requirements
> Select Engine — Choose target detection engine
> Configure — Set release type and parameters
> Publish — Review diff, get git instructions, confirm

##### Release Detail
- Full rule list with content preview
- Diff visualization against previous release
- Copy-paste commit instructions
- Jira Epic link (if created)
- Export to JSON/CSV

##### History
- Searchable archive of 6+ months of releases
- Filter by engine, release type, status
- Relative timestamps ("3 hours ago")

##### Compare
- Side-by-side diff of any two releases
- Added/removed/modified rule breakdown
- Content hash comparison

##### Statistics
- Rules Over Time — Time-series line chart
- By Format — Pie/bar chart (JSON/YARA/Sigma/BOSS)
- By Engine — Activity heatmap per engine
- By Type — Sprint vs hot_fix breakdown
- By Status — Draft/pending/published/failed counts
- Contributors — Top rule creators leaderboard
- All charts powered by Plotly with configurable time ranges (1–60 months)

##### Syntax Validation
- Paste any YARA or Sigma rule
- Instant syntax check with detailed error/warning output
- Auto-detects format

##### VT Retrohunt
- Submit YARA rules to VirusTotal
- Track job progress in real-time
- Browse matching files with statistics
- Filter matches by tags
- Pagination for large result sets

##### Knowledge Base
- Inline Confluence documentation browser
- Full-text search across pages
- Markdown rendering of Confluence content

##### Admin Panel
- Manage detection engines (create, list)
- Manage repositories (create, list)
- User management
- Only visible to Admin role

---

#### Key UI Features
- Relative timestamps — "3 hours ago" instead of raw dates
- Markdown rendering — Rule content displayed with syntax highlighting
- ZIP extraction — Upload ZIP files, preview extracted rules
- Live notebook monitoring — Cell-by-cell output during execution
- Multi-step wizard — Progress tracking through release flow
- Export — Download releases as JSON or CSV
- Badges — Status, type, and change indicators throughout

---

## Authentication & Authorization

#### JWT Authentication System

The Hub uses JSON Web Token (JWT) Bearer authentication with role-based access control (RBAC).

---

#### Auth Flow

```
sequenceDiagram
	participant U as User
	participant S as Streamlit UI
	participant A as FastAPI Backend
	participant D as Database

	U->>S: Enter username/password
	S->>A: POST /api/auth/login
	A->>D: Verify bcrypt hash
	D-->>A: User record
	A-->>S: JWT token (user_id, username, role)
	S-->>U: Logged in, session stored
	U->>S: Navigate to page
	S->>A: GET /api/... (Authorization: Bearer token)
	A->>A: Validate JWT, check role
	A-->>S: Response data

Database
FastAPI Backend
Streamlit UI
User
Database
FastAPI Backend
Streamlit UI
User
Enter username/password
POST /api/auth/login
Verify bcrypt hash
User record
JWT token (user_id, username, role)
Logged in, session stored
Navigate to page
GET /api/... (Authorization: Bearer token)
Validate JWT, check role
Response data
​
```

---

#### JWT Configuration

Setting
	
Default
	
Env Variable

Algorithm
	
HS256
	
JWT_ALGORITHM

Expiration
	
480 minutes (8 hours)
	
JWT_EXPIRE_MINUTES

Secret Key
	
Must be overridden in production
	
JWT_SECRET_KEY

---

#### Role-Based Access Control (6 Levels)

Role
	
Permissions

Admin
	
Full access: users, engines, repositories, releases, all operations

Release Manager
	
Create releases, publish, manage engines

Researcher
	
Create releases, run notebooks, access VT Retrohunt

Manager
	
Read-only + Retrohunt + statistics

TAM
	
Statistics, history, knowledge base only (omits sensitive git data)

Viewer
	
Dashboard + read-only browsing only

---

#### Audit Logging

Every significant action is logged to the audit_logs table:

Action
	
Details Captured

user_login
	
IP address, user agent, role

release_prepared
	
Engine, version, rule count, type

jira_epic_attempted
	
Release ID, success/failure, Jira key

confluence_credentials_saved
	
Timestamp, user

admiral_upload
	
Package name, storage path, file count

Audit logs are queryable via GET /api/history/audit and indexed by created_at, entity_type + entity_id, and action.

---

#### Auth Service Functions (services/auth.py)

Function
	
Signature
	
Description

hash_password
	
(password: str) -> str
	
bcrypt.hashpw + gensalt

verify_password
	
(plain: str, hashed: str) -> bool
	
bcrypt.checkpw comparison

create_access_token
	
(user_id, username, role) -> str
	
JWT encode with payload {sub, username, role, exp}

decode_access_token
	
(token: str) -> dict | None
	
JWT decode, validate sub field, returns None on error

authenticate_user
	
(db, username, password) -> User | None
	
Query user by username, verify password, check is_active

get_user_by_id
	
(db, user_id) -> User | None
	
Query active user by ID

---

#### Auth Dependencies (core/auth.py)
- security = HTTPBearer() — FastAPI security scheme
- get_current_user(credentials, db) -> User — Extracts Bearer token, decodes JWT, fetches user, raises HTTP 401 on failure
- require_role(*allowed_roles: UserRole) — Dependency factory. Returns role_checker(user) that raises HTTP 403 if user.role not in allowed roles.

---

#### Login Implementation Details

The POST /api/auth/login endpoint:
1. Calls authenticate_user(db, username, password)
1. Creates JWT via create_access_token(user_id, username, role)
1. Captures client IP from X-Forwarded-For header (proxy) or request.client.host
1. Logs user_login audit action with: method, ip, user_agent, role
1. Returns TokenResponse with access_token and token_type="bearer"

---

#### Registration

POST /api/auth/register:
- Validates username uniqueness (400 if taken)
- Validates email uniqueness (400 if taken)
- Hashes password via bcrypt
- Default role: VIEWER (configurable in request)
- Logs user_registered audit action

---

#### Commit Verification System

When confirming a release publish, the verification service provides an extensible commit verification pipeline:

Enums:
- VerificationMethod: FORMAT_ONLY, PROVIDER_CONFIRMED, PROVIDER_UNAVAILABLE, PROVIDER_MISMATCH
- VerificationOutcome: ACCEPTED_FORMAT, ACCEPTED_PROVIDER, REJECTED_MISMATCH, REJECTED_VALIDATION, REJECTED_STATE

Provider Architecture:
- GitProviderAdapter (abstract base) — interface for verify_commit_exists(hash, repo_url)
- StubGitProvider (default) — returns {exists: None, provider: "stub"}, format-only validation
- Swappable via set_provider() for GitHub/GitLab integration

Verification Flow:
1. Validate commit hash format (regex ^[0-9a-f]{7,64}$)
1. Validate confirmed_by name (>= 2 chars)
1. Check release exists and is in PENDING_PUBLISH state
1. Check no existing confirmation (idempotency guard)
1. Call provider verify_commit_exists()
1. Create PublishConfirmation record
1. Update Release.status to PUBLISHED
1. Log 3 audit entries: commit_hash_submitted, verification_completed, publish_confirmed

---

## Integrations

#### External Service Integrations

The Detection Engineering Hub integrates with several external services to extend its capabilities.

---

#### VirusTotal Retrohunt

> 💡 Submit YARA rules to VirusTotal's retrohunt engine and browse matching malware samples.

How It Works:
1. User pastes a YARA rule in the Streamlit UI or submits via API
1. Hub sends the rule to VirusTotal's retrohunt API
1. Job is tracked with real-time status polling
1. Results include matching files with metadata, tags, and statistics
1. Matches can be filtered and paginated

API Key Options:
- Global: Set VIRUSTOTAL_API_KEY in .env
- Per-request: Pass via X-VT-Api-Key header (users bring their own quota)
- Demo mode: Returns mock data via _demo_jobs() and _demo_matches() hardcoded functions when no API key is configured

Service Functions (services/virustotal.py):
- submit_retrohunt(rules, corpus="main", api_key?) -> dict — POST /intelligence/retrohunt_jobs
- list_retrohunt_jobs(api_key?) -> dict — Handles 401 (auth), 403 (no premium)
- get_retrohunt_job(job_id, api_key?) -> dict — Returns {id, status, num_matches, progress}
- get_retrohunt_matches(job_id, tags?, limit?, cursor?, api_key?) -> dict — CSV tag filter support

Base URL: https://www.virustotal.com/api/v3

Request model: SubmitRetrohuntRequest(content: str [10-1M chars], corpus: "main" | "goodware")

---

#### Jira Integration

> 💡 Automatic Jira Epic creation when a release is confirmed/published.

Flow:
- After POST /api/releases/{id}/confirm succeeds
- Hub creates a Jira Epic with title: [Detection] Sprint Release v1.0.0
- Epic includes commit hash, rule count, engine, and version
- Audit logged as jira_epic_attempted
- Stub mode if credentials not configured (no error, just skipped)
- Severity: SEV-3 (hardcoded constant)

Service Functions (services/jira.py):
- build_epic_title(version, release_type) -> str — "[Detection] Sprint Release v{version}"
- build_epic_description(version, release_type, rule_count, commit_hash, confirmed_by) -> str
- create_jira_epic(...) -> dict — Returns {success, stub, epic_key, epic_url, epic_title, severity, message}

Configuration:

```
JIRA_BASE_URL=https://your-org.atlassian.net
JIRA_API_TOKEN=<token>
JIRA_USER_EMAIL=<email>
JIRA_PROJECT_KEY=DET

​
```

---

#### Confluence Knowledge Base

> 💡 Browse and search Confluence documentation inline within the Hub UI.

Features:
- List preset documentation pages
- Full-text search across Confluence spaces
- Fetch full page content with HTML-to-Markdown conversion (via markdownify)
- Inline rendering in Streamlit
- Credentials stored in backend .env (not hardcoded)
- Auto-detects Atlassian Cloud (.atlassian.net → /wiki/rest/api) vs Server (/rest/api)

Preset Categories: release, jira, fp, training, sensor, infra (each with keyword filters)

Service Functions (services/confluence.py):
- _html_to_markdown(html) — Converts Confluence Storage Format HTML via markdownify
- list_preset_pages() — Returns categories, verifies credentials with ping search
- search_pages(q) — CQL: type = page AND (title ~ "..." OR text ~ "...") ORDER BY lastModified DESC
- get_page_content(page_id) — GET /content/{id} with expand=body.storage,version,space

Configuration:

```
CONFLUENCE_BASE_URL=https://your-org.atlassian.com/wiki
CONFLUENCE_API_TOKEN=<token>
CONFLUENCE_USER_EMAIL=<email>

​
```

---

#### Jupyter Notebook Execution

The Hub supports both local and remote notebook execution for detection rule automation.

##### Local Execution

> 💡 Run .ipynb notebooks locally via Papermill with rule file injection.
- Upload notebook + rule files
- Papermill executes the notebook with injected environment variables
- Cell-by-cell output streamed in real-time via polling
- In-memory execution store tracks run state
- Timeout: 7200 seconds (2 hours)

##### Remote Execution

> 💡 Connect to a remote JupyterLab server for execution without local compute.
- Password-based authentication with session cookies
- XSRF token management for security
- Upload rules + hub_env_config.json to remote server
- Inject PowerShell function lists into notebook cells
- Execute via Jupyter kernel using WebSocket wire protocol
- Stream output back to Hub via polling
- Supports URL path prefixes (e.g., /securityresearch-20221115)

PowerShell Injection (services/notebook_inject.py):
- inject_powershell_functions_cell(nb, text, target_cell_id?) — patches notebook JSON in-place
- Searches cells by: target_cell_id → DEFAULT_POWERSHELL_CELL_ID → pattern match
- Constants: DEFAULT_POWERSHELL_CELL_ID = "ab5d9228-...", FILELESS_POWERSHELL_HEADING_FRAGMENT = "Additional-lists-(like-alex)"

JupyterRemoteClient (services/jupyter_remote.py):
- REST + session cookies + XSRF tokens via httpx
- Methods: authenticate(), upload_file(), start_kernel(), start_session_for_notebook(), wait_kernel_ready(), save_notebook(), read_notebook(), clear_hub_packages_dir()

KernelConnection (WebSocket):
- Thread-safe persistent WebSocket using Jupyter wire protocol
- execute(code, on_output?, timeout=7200) — sends execute_request, waits for execute_reply + status idle
- connect(timeout=30, retries=3) with 3s sleep between retries

---

#### MCP Servers

The project includes MCP (Model Context Protocol) server configurations in .mcp.json:

Server
	
Purpose

Stitch
	
UI/Design generation via Google APIs

Nano-banana
	
Image generation via Gemini

21st-dev Magic
	
Component library integration

Playwright
	
Browser automation and testing

Notion
	
Workspace documentation and task management

---

## Admiral Rule Storage

#### Dynamic Filesystem-Based Rule Storage

Admiral is a file storage system built into the Hub for managing detection rule packages outside of version control. It provides a directory-based browser with upload, download, and organization features.

---

#### Why Admiral?

> 💡 Not all rules belong in git. Admiral provides a staging area for rule packages that need flexible organization, quick sharing, or pre-release storage without polluting version control history.

---

#### Storage Layout

```
storage/admiral/
├── {directory}/
│   ├── {project}/
│   │   ├── rule_1.json
│   │   ├── rule_2.json
│   │   └── rule_3.yar
│   └── {another_project}/
│       └── rules.zip
└── {another_directory}/
    └── ...

​
```

Configurable root via ADMIRAL_STORAGE_ROOT env variable (default: storage/admiral).

---

#### Features

##### Directory Management
- Create directories — POST /api/admiral/mkdir with sanitized names
- Browse contents — GET /api/admiral/browse lists files and subdirectories
- Recursive listing — GET /api/admiral/all-dirs for directory picker UIs
- Move — POST /api/admiral/move relocates files/dirs to new locations
- Delete — DELETE /api/admiral/rm with safe path traversal checks

##### File Operations
- Upload — POST /api/admiral/upload accepts JSON files or ZIP archives
- Download file — GET /api/admiral/download-file for single files
- Download directory — GET /api/admiral/download-dir packages entire directory as ZIP

##### Security
- All path inputs are sanitized to prevent directory traversal attacks
- Names are cleaned of special characters
- Database audit trail for all uploads

---

#### Streamlit UI

The Admiral page in Streamlit provides:
- Breadcrumb navigation through directory tree
- Folder picker dropdowns for upload targets and move destinations
- Drag-and-drop uploads for JSON and ZIP files
- Row actions for individual file operations (download, move, delete)
- Bulk download of entire directories as ZIP archives

---

## Database Schema

#### Data Models & Relationships

The Hub uses SQLAlchemy ORM with support for both PostgreSQL (production) and SQLite (POC mode).

---

#### Entity Relationship Diagram

```
erDiagram
	User ||--o{ Release : creates
	Engine ||--o{ Release : belongs_to
	Engine ||--o{ Repository : has
	Release ||--|{ ReleaseItem : contains
	Release ||--o| PublishConfirmation : confirmed_by
	Release }o--|| AuditLog : generates
	AdmiralPackage }o--|| AuditLog : generates

User

Release

Engine

Repository

ReleaseItem

PublishConfirmation

AuditLog

AdmiralPackage

creates

belongs_to

has

contains

confirmed_by

generates

generates

​
```

---

#### Tables

##### users

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

username
	
String (unique)
	
Login identifier

email
	
String (unique)
	
User email

hashed_password
	
String
	
bcrypt hash

role
	
Enum(UserRole)
	
One of 6 role levels

is_active
	
Boolean
	
Account enabled/disabled

created_at
	
DateTime
	
Auto-set

##### engines

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

name
	
String (unique)
	
Engine name (BEP, Fileless, VPP, VFP)

description
	
Text
	
Engine description

supported_formats
	
JSON
	
List of supported rule formats

created_at
	
DateTime
	
Auto-set

##### repositories

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

name
	
String (unique)
	
Repository name

url
	
String
	
Git URL

engine_id
	
FK (nullable)
	
Associated engine

default_branch
	
String
	
Default git branch name

created_at
	
DateTime
	
Auto-set

Relationship: engine → Engine (many-to-one)

##### releases

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

version
	
String
	
Semantic version (e.g., 1.2.0)

release_type
	
Enum(ReleaseType)
	
sprint or hot_fix

status
	
Enum(ReleaseStatus)
	
draft/pending_publish/published/failed

engine_id
	
FK (nullable)
	
Target engine

repository_id
	
FK (nullable)
	
Target repository

created_by
	
FK (nullable)
	
Creator username

description
	
Text
	
Release description

package_metadata
	
JSON
	
File metadata from upload

suggested_commit_message
	
Text
	
Generated commit message

git_instructions
	
Text
	
Manual git steps text

ai_summary
	
Text
	
Deterministic summary (no LLM)

jira_epic_key
	
String (nullable)
	
e.g., DET-123

jira_epic_url
	
String (nullable)
	
Full Jira URL

jira_epic_title
	
String (nullable)
	
Epic title text

created_at
	
DateTime (indexed)
	
Auto-set

updated_at
	
DateTime
	
Last modification

Relationships: items → ReleaseItem[] (back_populates), publish_confirmation → PublishConfirmation (uselist=False)

##### release_items

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

release_id
	
FK (cascade delete)
	
Parent release

rule_name
	
String (indexed)
	
Name of the rule

rule_format
	
Enum(RuleFormat)
	
json/yara/sigma/boss/dotnet

file_path
	
String
	
Original filename

content_hash
	
String
	
SHA256 (first 16 chars) for diff

change_type
	
String
	
added / modified / removed

selected
	
Boolean
	
Whether rule was selected for release

rule_metadata
	
JSON
	
Full rule metadata

created_at
	
DateTime
	
Auto-set

##### publish_confirmations

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

release_id
	
FK (cascade, unique)
	
One confirmation per release

commit_hash
	
String (indexed)
	
7-64 hex chars (CHECK constraint)

confirmed_by
	
String
	
Username who confirmed

verified
	
Boolean
	
Provider verification result

verification_details
	
JSON
	
Method, provider, outcome

confirmed_at
	
DateTime
	
Confirmation timestamp

##### audit_logs

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

action
	
String (indexed)
	
Action name (e.g., release_prepared)

entity_type
	
String
	
Type of entity (release, user, etc.)

entity_id
	
String
	
ID of affected entity

actor
	
String
	
Who performed the action

details
	
JSON
	
Additional context data

created_at
	
DateTime (indexed)
	
Auto-set

##### admiral_packages

Column
	
Type
	
Notes

id
	
Integer (PK)
	
Auto-increment

name
	
String (indexed)
	
Package name

storage_path
	
String (unique)
	
Filesystem path

file_count
	
Integer
	
Number of files in package

total_size_bytes
	
Integer
	
Total package size

file_manifest
	
JSON
	
List of files with metadata

uploaded_by
	
String
	
Username of uploader

notes
	
Text
	
Optional notes

created_at
	
DateTime (indexed)
	
Upload timestamp

---

#### Enums

Enum
	
Values

UserRole
	
viewer, researcher, manager, release_manager, tam, admin

ReleaseType
	
sprint, hot_fix

ReleaseStatus
	
draft, pending_publish, published, failed

RuleFormat
	
json, yara, sigma, boss, dotnet

---

#### Key Indexes
- releases.status, releases.created_at, releases.engine_id + status
- release_items.release_id, release_items.rule_name
- publish_confirmations.commit_hash
- audit_logs.created_at, audit_logs.entity_type + entity_id, audit_logs.action
- admiral_packages.name, admiral_packages.created_at

#### Cascade Rules
- Delete Release → cascades to ReleaseItem and PublishConfirmation
- Foreign keys to Engine, Repository, User support nullable references

---

#### Database Setup

SQLAlchemy Configuration (core/database.py):
- engine: Created via create_engine(settings.DATABASE_URL) with SQLite check_same_thread=False
- SessionLocal: sessionmaker(autocommit=False, autoflush=False)
- Base: DeclarativeBase for all models
- get_db(): Generator dependency yielding DB sessions (FastAPI Depends pattern)

Seed Data (seed.py) creates:
- 4 demo users: admin/admin123 (ADMIN), researcher/researcher123 (RESEARCHER), viewer/viewer123 (VIEWER), tam_user/tam123 (TAM)
- 4 engines: BEP (sigma), Fileless (yara, dotnet), VPP (yara, boss), VFP (yara)
- 3 repositories: Security-Content-Variant (VFP), Security-Content-PCP (BEP), Security-Content-Fileless (Fileless)
- 3 demo releases: v1.0.0 (PUBLISHED, 30d ago), v1.1.0 (PUBLISHED, 14d ago), v1.1.1 (PENDING_PUBLISH, 3h ago)
- 7 demo rules: detect_powershell_download, detect_mimikatz_usage, detect_lateral_movement, detect_dns_tunneling, detect_credential_dump, detect_ransomware_behavior, detect_c2_beaconing
- Audit log entries for all release prepare/publish actions

---

## Deployment Guide

#### Three Deployment Options

The Detection Engineering Hub supports three deployment modes, from lightweight local development to production Kubernetes.

---

#### Option 1: POC (Proof of Concept)

> 🧪 Best for: Quick demos, local development, single-user testing. No external database required.

Setup:

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd backend && python seed.py && cd ..
./run-poc.sh

​
```
- Database: SQLite (poc.db file)
- API: http://localhost:9000
- Streamlit UI: http://localhost:9510
- Single process, no Docker required

What run-poc.sh does:
1. Checks if poc.db exists; if not, runs python seed.py (creates tables + 4 demo users + 4 engines + 3 repos + 3 releases)
1. Starts backend: uvicorn app.main:app --port 9000 --reload
1. Starts Streamlit: streamlit run app.py --server.port 9510 --server.headless true

Demo Credentials:

Username
	
Password
	
Role

admin
	
admin123
	
ADMIN (full access)

researcher
	
researcher123
	
RESEARCHER (prepare & confirm)

viewer
	
viewer123
	
VIEWER (read only)

tam_user
	
tam123
	
TAM (limited view)

---

#### Option 2: Docker Compose

> 🐳 Best for: Team environments, integration testing, staging.

```
docker compose up --build

​
```

Service
	
Port
	
Notes

PostgreSQL 16
	
5432
	
Persistent volume

Backend API
	
8000
	
FastAPI + Uvicorn

Streamlit UI
	
8501
	
Primary UI

Next.js Frontend
	
3000
	
Optional, disabled by default

---

#### Option 3: Kubernetes (Helm)

> ☸️ Best for: Production deployments, multi-replica scaling, enterprise environments.

```
helm lint helm/detection-hub
helm install detection-hub helm/detection-hub -f values.yaml

​
```

Helm Chart Features:
- Chart version 0.1.0, appVersion 0.1.0
- External PostgreSQL or Bitnami subchart toggle
- Configurable replicas per service
- Custom image repositories + tags

Key values.yaml Settings:

Path
	
Default
	
Description

backend.image.repository
	
ghcr.io/cybereason-labs/detection-hub-backend
	
Backend image

backend.replicaCount
	
1
	
Backend replicas

backend.port
	
8000
	
Backend service port

streamlit.image.repository
	
ghcr.io/cybereason-labs/detection-hub-streamlit
	
Streamlit image

streamlit.port
	
8501
	
Streamlit service port

frontend.enabled
	
false
	
Next.js frontend toggle

postgresql.enabled
	
true
	
Bitnami PostgreSQL subchart

postgresql.auth.password
	
"changeme"
	
DB password (override in prod)

ingress.enabled
	
false
	
Ingress toggle

Helm Templates:
- _helpers.tpl — Name/fullname helpers, database URL builder, secret name
- backend-deployment.yaml — Liveness: GET /health (15s initial, 20s period). Readiness: GET /health (5s initial, 10s period)
- streamlit-deployment.yaml — Health check: GET /_stcore/health. Liveness (10s/30s), Readiness (5s/10s)
- secret.yaml — DATABASE_URL + JWT_SECRET_KEY
- ingress.yaml — Routes: /api → backend, /app → frontend, / → streamlit. TLS support.

---

#### Container Images

Published to ghcr.io:
- detection-hub-backend (from backend/Dockerfile)
- detection-hub-frontend (from frontend/Dockerfile)
- detection-hub-streamlit (from frontend_streamlit/Dockerfile)

Tagged with git SHA + latest.

---

#### Docker Compose Environment Variables

Service
	
Key Variables

db
	
POSTGRES_USER=postgres, POSTGRES_PASSWORD=postgres, POSTGRES_DB=detection_hub

backend
	
DATABASE_URL=postgresql://postgres:postgres@db:5432/detection_hub, SEED_ON_START=true

frontend
	
NEXT_PUBLIC_API_URL=http://localhost:8000

streamlit
	
BACKEND_API_URL=http://backend:8000

Volume: pgdata:/var/lib/postgresql/data (persistent PostgreSQL data)

Health Check (db): pg_isready -U postgres (5s interval, 3s timeout, 5 retries)

---

#### Dockerfiles

##### Backend

```
FROM python:3.11-slim
WORKDIR /app
EXPOSE 8000
ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

​
```

##### Streamlit

```
FROM python:3.11-slim
WORKDIR /app
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

​
```

The Streamlit Dockerfile also copies adv_fileless_automation-test.ipynb as /app/adv_fileless_automation.ipynb for the Fileless engine notebook automation.

---

## CI/CD Pipeline

#### GitHub Actions Workflow

Defined in .github/workflows/ci.yml. Triggers on pushes to main or Detection-Engineering-HUB branch, and all pull requests.

---

#### Pipeline Diagram

```
flowchart LR
	A["backend-test"] --> C["docker-build"]
	B["frontend-lint"] --> C
	C --> D["security-scan"]
	E["helm-lint"]

backend-test

docker-build

frontend-lint

security-scan

helm-lint

​
```

---

#### Jobs

##### 1. Backend Tests
- Runner: Ubuntu latest, Python 3.11
- Installs backend/requirements-dev.txt
- Runs pytest backend/tests/ -x -q (121 tests, stop on first failure)

##### 2. Frontend Lint
- Runner: Ubuntu latest, Node 18
- npm ci → npm run lint → npm run build

##### 3. Docker Build
- Depends on: backend-test + frontend-lint
- Builds 3 images: backend, frontend, streamlit
- Pushes to ghcr.io with SHA + latest tags (main branch only)

##### 4. Security Scan
- Runs after docker-build (push events only)
- pip-audit on backend, npm audit on frontend
- Non-blocking (warnings allowed)

##### 5. Helm Lint
- Independent, runs in parallel
- Lints chart syntax + template rendering test

---

#### Testing Framework
- Framework: pytest 8.3.4
- Location: backend/tests/
- Count: 121 test cases
- Async support: pytest-asyncio 0.24.0
- Dev deps: backend/requirements-dev.txt extends requirements.txt with: pytest, pytest-asyncio
- HTTP test client: httpx 0.28.1 (for async test client)

---

#### Docker Build Matrix

Image
	
Context
	
Dockerfile
	
Registry

detection-hub-backend
	
./backend
	
backend/Dockerfile
	
ghcr.io

detection-hub-frontend
	
./frontend
	
frontend/Dockerfile
	
ghcr.io

detection-hub-streamlit
	
. (root)
	
frontend_streamlit/Dockerfile
	
ghcr.io

Tag strategy: {git-sha} + latest on main branch pushes only. PRs build but don't push.

Caching: Uses GitHub Actions cache for Docker layers.

---

#### Trigger Conditions

Event
	
Branches
	
Jobs Run

Push
	
main, Detection-Engineering-HUB
	
All 5 jobs (backend-test, frontend-lint, docker-build, security-scan, helm-lint)

Pull Request
	
main, Detection-Engineering-HUB
	
backend-test, frontend-lint, docker-build (no push), helm-lint

---

#### Security Scanning Details
- pip-audit: Checks backend/requirements.txt against known vulnerability databases. Non-blocking (warnings allowed).
- npm audit: Checks frontend/ dependencies, omitting dev dependencies. Non-blocking.
- Only runs on push events (not on PRs) after docker-build succeeds.

---

## Configuration Reference

#### Environment Variables

All configuration via .env file (see .env.example template).

---

#### Core Settings

Variable
	
Default
	
Description

DATABASE_URL
	
sqlite:///./poc.db
	
DB connection string. Use postgresql:// for production.

JWT_SECRET_KEY
	
Weak default
	
MUST override in production. Signs JWT tokens.

JWT_ALGORITHM
	
HS256
	
JWT signing algorithm

JWT_EXPIRE_MINUTES
	
480
	
Token expiration (default 8 hours)

---

#### Jira (Optional)

Variable
	
Description

JIRA_BASE_URL
	
e.g., https://your-org.atlassian.net

JIRA_API_TOKEN
	
API token for authentication

JIRA_USER_EMAIL
	
Email for the API token

JIRA_PROJECT_KEY
	
Project key (e.g., DET)

Stub mode if not configured (no errors, just skipped).

---

#### Confluence (Optional)

Variable
	
Description

CONFLUENCE_BASE_URL
	
e.g., https://your-org.atlassian.com/wiki

CONFLUENCE_API_TOKEN
	
API token for authentication

CONFLUENCE_USER_EMAIL
	
Email for the API token

Can also be saved at runtime via POST /api/confluence/credentials.

---

#### VirusTotal (Optional)

Variable
	
Description

VIRUSTOTAL_API_KEY
	
Global key. Per-request keys via X-VT-Api-Key header also supported.

Demo mode with mock data when not configured.

---

#### Admiral Storage

Variable
	
Default
	
Description

ADMIRAL_STORAGE_ROOT
	
storage/admiral
	
Root directory for file storage

---

#### Other

Variable
	
Default
	
Description

GIT_VERIFY_ENABLED
	
false
	
Experimental git commit hash verification

---

#### Seed Data

Run python backend/seed.py to populate:
- 4 detection engines (BEP, Fileless, VPP, VFP)
- Demo repositories pointing to GitHub
- Default admin user for testing

---

#### Key Design Decisions

<details><summary>Why no git operations in the Hub?</summary>

</details>

<details><summary>Why deterministic AI summaries?</summary>

</details>

<details><summary>Why per-request VT API keys?</summary>

</details>

<details><summary>Why filesystem storage for Admiral?</summary>

</details>

<details><summary>Why 6 role levels?</summary>

</details>

---

## Backend Services Reference

#### Service Layer Architecture

All business logic lives in backend/app/services/. Route handlers delegate to these services for parsing, validation, diffing, verification, and external API integration.

---

#### Authentication Service (services/auth.py)

Function
	
Signature
	
Description

hash_password
	
(password: str) -> str
	
bcrypt hash with gensalt

verify_password
	
(plain: str, hashed: str) -> bool
	
bcrypt.checkpw comparison

create_access_token
	
(user_id: int, username: str, role: str) -> str
	
JWT encode with {sub, username, role, exp}. Expiry from JWT_EXPIRE_MINUTES.

decode_access_token
	
(token: str) -> dict | None
	
JWT decode, validate sub field. Returns None on JWTError.

authenticate_user
	
(db, username, password) -> User | None
	
Query user, verify password, check is_active.

get_user_by_id
	
(db, user_id: int) -> User | None
	
Query active user by ID.

Auth Dependencies (core/auth.py):
- security: HTTPBearer instance
- get_current_user(credentials, db) -> User: Extracts/validates JWT Bearer token, raises 401
- require_role(*allowed_roles): Dependency factory returning role_checker that raises 403

---

#### Parser Service (services/parser.py)

Parses uploaded rule files into structured data.

Function
	
Signature
	
Description

detect_format
	
(filename: str) -> RuleFormat | None
	
Detect by extension: .json, .yar/.yara, .boss/.bossig, .yml/.yaml

is_supplemental_content_filename
	
(filename: str) -> bool
	
Check suffix against: .ps1, .psm1, .psd1, .txt, .xml, .csv, .md, .bat, .sh

parse_json_package
	
(content, filename) -> dict
	
Supports list, {rules: []}, or single object. Extracts name/id/title, content_hash (sha256[:16]).

parse_yara_package
	
(content, filename) -> dict
	
Uses plyara library. Extracts rule_name, tags, metadata, strings_count.

parse_sigma_package
	
(content, filename) -> dict
	
Uses yaml.safe_load_all for multi-document. Extracts title, id, status, level, logsource, author.

parse_boss_package
	
(content, filename) -> dict
	
Opaque unit: one file = one rule. Hashes entire content.

parse_package
	
(content, filename, fmt?) -> dict
	
Auto-detects format, delegates to specific parser.

Return format for all parsers:

```
{filename, format, rules_found, rules: [{rule_name, file_path, content_hash, metadata}], validation_errors, validation_warnings}

​
```

---

#### Rule Validator Service (services/rule_validator.py)

Strict syntax validation for YARA and Sigma rules.

##### YARA Validation Constants
- Required metadata: id, score, author, tags, stability, description
- Required alias groups: [date, creation_date], [mitre_tags, mitre]
- Recommended metadata: classification
- Score range: 0–100
- Stability values: verified, experimental, stable, deprecated, test
- ID format: UUID v4
- Date format: YYYY-MM-DD or DD/MM/YYYY or YYYY/MM/DD

##### Sigma Validation Constants
- Required fields: title, id, author, description, date, logsource, detection, level
- Logsource required: both category AND product
- Level values: informational, low, medium, high, critical
- Tags pattern: attack.tNNNN or attack.taNNNN (MITRE ATT&CK)
- Detection must have: selection* keys + condition

##### Data Classes
- ValidationIssue(message: str, field: str | None, line: int | None)
- ValidationResult(format: str, valid: bool, errors: list, warnings: list)

##### Functions
- _detect_format(content) -> "yara" | "sigma" | "unknown" — rule + { for YARA, YAML + title/detection for Sigma
- _validate_yara(content) -> ValidationResult — full plyara parse + metadata validation
- _validate_sigma(content) -> ValidationResult — YAML parse + field/structure validation
- validate_rule(content) -> ValidationResult — main entry point

---

#### Version Service (services/version.py)

Function
	
Signature
	
Description

get_latest_version
	
(db, engine_id?) -> str | None
	
Query latest Release.version ordered by created_at desc

parse_version
	
(version: str) -> (int, int, int)
	
Parse semver via regex v?(\d+)\.(\d+)\.(\d+), defaults (0,0,0)

propose_version
	
(db, release_type, engine_id?) -> dict
	
Sprint: minor bump (1.0.0 → 1.1.0). Hot_fix: patch bump (1.1.0 → 1.1.1). First: 1.0.0.

---

#### Diff Service (services/diff.py)

compute_diff(db, new_rules: list[dict], engine_id?) -> dict
- Finds latest PUBLISHED release for the engine
- Builds lookup dicts by rule_name
- Compares content_hash to detect modifications
- Returns: {previous_version, entries: [{rule_name, change_type, details}], summary}
- First release: all rules marked "added"

---

#### Commit Service (services/commit.py)

NEVER executes git commands — only generates text.
- generate_commit_message(version, release_type, rule_count, added, modified, removed, description?) -> str
- generate_git_instructions(version, release_type, commit_message, repository_name?, branch="main") -> list[str]

---

#### Verification Service (services/verification.py)

Commit hash verification with pluggable git provider.

##### Enums
- VerificationMethod: FORMAT_ONLY, PROVIDER_CONFIRMED, PROVIDER_UNAVAILABLE, PROVIDER_MISMATCH
- VerificationOutcome: ACCEPTED_FORMAT, ACCEPTED_PROVIDER, REJECTED_MISMATCH, REJECTED_VALIDATION, REJECTED_STATE

##### Architecture
- GitProviderAdapter (abstract): verify_commit_exists(hash, repo_url) -> {exists, details}
- StubGitProvider (default): Always returns {exists: None, provider: "stub"}
- Global: _provider = StubGitProvider() with get_provider() / set_provider()

##### Functions
- validate_commit_hash(hash) -> (bool, str) — regex ^[0-9a-f]{7,64}$
- validate_confirmed_by(name) -> (bool, str) — must be >= 2 chars
- verify_and_confirm(db, release_id, commit_hash, confirmed_by) -> dict — validates inputs, checks PENDING_PUBLISH state, creates PublishConfirmation, updates status to PUBLISHED, logs 3 audit entries (commit_hash_submitted, verification_completed, publish_confirmed)

---

#### Jira Service (services/jira.py)
- JIRA_SEVERITY = "SEV-3"
- build_epic_title(version, release_type) -> str — "[Detection] Sprint Release v{version}"
- build_epic_description(version, release_type, rule_count, commit_hash, confirmed_by) -> str
- create_jira_epic(...) -> dict — Stub mode when JIRA_API_TOKEN not set. Returns {success, stub, epic_key, epic_url, epic_title, severity, message}.

---

#### AI Summary Service (services/ai_summary.py)

generate_release_summary(version, release_type, status, rule_count, added, modified, removed, formats?, jira_epic_key?, commit_hash?, confirmed_by?) -> str

Deterministic (no LLM calls). Returns markdown with ## Release Summary heading. Published state includes commit + confirmed_by; pending state shows awaiting message.

---

#### Audit Service (services/audit.py)

log_action(db, action, entity_type?, entity_id?, actor?, details?) -> AuditLog

Adds to session without committing (caller controls transaction).

---

#### Statistics Service (services/statistics.py)

All functions accept db: Session + time range parameters.

Function
	
Returns

get_overview(db, months=12)
	
{total_releases, total_rules, contributors_count, published_releases}

get_rules_over_time(db, months=12)
	
[{period: "YYYY-MM", count}] for published rules

get_by_format(db, months=12)
	
[{format, count}]

get_by_type(db, months=12)
	
[{type, count}]

get_by_status(db, months=12)
	
[{status, count}]

get_by_engine(db, days=30)
	
[{engine, count}] (includes "Unassigned")

get_contributors(db, months=12, limit=20)
	
[{created_by, count, last_activity}]

---

#### Confluence Service (services/confluence.py)

Auto-detects Atlassian Cloud (.atlassian.net → /wiki/rest/api) vs Server (/rest/api).

Preset Categories: release, jira, fp, training, sensor, infra (each with keywords)

Function
	
Description

_is_configured()
	
Check BASE_URL, API_TOKEN, USER_EMAIL all set

_auth_headers()
	
Basic auth from email:token base64-encoded

_html_to_markdown(html)
	
Convert Confluence Storage Format HTML to Markdown via markdownify

list_preset_pages()
	
Returns preset categories, verifies credentials with ping search

search_pages(q)
	
CQL search: type = page AND (title ~ ... OR text ~ ...)

get_page_content(page_id)
	
GET /content/{id} with expand=body.storage,version,space. Returns markdown.

---

#### VirusTotal Service (services/virustotal.py)

Base URL: https://www.virustotal.com/api/v3

Function
	
Description

submit_retrohunt(rules, corpus, api_key?)
	
POST /intelligence/retrohunt_jobs. Returns {configured, job, error}.

list_retrohunt_jobs(api_key?)
	
GET retrohunt jobs. Handles 401 (auth), 403 (no premium).

get_retrohunt_job(job_id, api_key?)
	
GET specific job with {id, status, num_matches, progress}.

get_retrohunt_matches(job_id, tags?, limit?, cursor?, api_key?)
	
GET matching files. Parses CSV tags filter. Returns {matches, cursor}.

Demo functions _demo_jobs() and _demo_matches() return hardcoded mock data when not configured.

---

#### Notebook Inject Service (services/notebook_inject.py)

PowerShell function injection for Fileless automation notebooks.

Constants:
- DEFAULT_POWERSHELL_CELL_ID = "ab5d9228-9b35-497d-b348-9cb0f315633d"
- FILELESS_POWERSHELL_HEADING_FRAGMENT = "Additional-lists-(like-alex)"

Function
	
Description

parse_powershell_function_names(text)
	
Split by newline, trim, lowercase

build_powershell_cell_source(names)
	
Generate cell code with list assignment + print

inject_powershell_functions_cell(nb, text, target_cell_id?)
	
Patch notebook JSON in-place. Search: target_id → default_id → pattern match. Returns (nb, metadata).

lab_url_with_powershell_fragment(lab_url, injection)
	
Append #cell-id or #heading fragment to JupyterLab URL

---

#### Jupyter Remote Service (services/jupyter_remote.py)

##### Class: JupyterRemoteClient

REST API client with password auth → session cookies.

Method
	
Description

authenticate()
	
POST /login, store XSRF token + cookies. Raises PermissionError on 401/403.

check_status()
	
GET /api/status

upload_file(path, content)
	
PUT /api/contents/{path} with base64 content

create_directory(path)
	
PUT /api/contents/{path} type: directory

start_kernel(name?)
	
POST /api/kernels, returns kernel_id

start_session_for_notebook(path, kernel?)
	
POST /api/sessions, returns (kernel_id, session_id)

wait_kernel_ready(kernel_id, timeout=120)
	
Poll until execution_state is idle. Raises TimeoutError.

shutdown_kernel(kernel_id)
	
DELETE /api/kernels/{id}

save_notebook(path, nb_content)
	
PUT /api/contents/{path} type: notebook

read_notebook(path)
	
Returns (notebook_dict, nb_bytes, filename, last_modified)

clear_hub_packages_dir(path)
	
Remove all items, returns (count, names)

kernel_ws_url(kernel_id)
	
Build ws:///wss:// URL for /api/kernels/{id}/channels

##### Class: KernelConnection

Thread-safe persistent WebSocket to Jupyter kernel.
- connect(timeout=30, retries=3) — websocket-client handshake with auth
- execute(code, on_output?, timeout=7200) — sends execute_request, waits for execute_reply + status idle, calls on_output callback per output
- close() — closes WebSocket

##### Wire Protocol Helpers
- make_execute_request(msg_id, session_id, code) — Jupyter execute_request message
- parse_output_message(msg) — Parse iopub: stream, execute_result, display_data, error

---

## Streamlit Frontend Internals

#### Technical Deep Dive

The Streamlit frontend (frontend_streamlit/app.py) is a ~10,000 line single-file application that serves as the primary user interface.

---

#### Design System

##### CSS Variables

Variable
	
Value
	
Usage

--purple-accent
	
#7C3AED
	
Primary accent, buttons, links

--purple-soft
	
#8B5CF6
	
Hover states, lighter accents

--green-accent
	
#16A34A
	
Success states, published badges

--amber-accent
	
#D97706
	
Warning states

--orange-accent
	
#EA580C
	
Warning variant

--red-accent
	
#DC2626
	
Error states, failed badges

--bg-void
	
#F0F1F3
	
Page background

--bg-base
	
#EDEEF0
	
Card backgrounds

--text-primary
	
#1A202C
	
Primary text

--text-secondary
	
#3F4E63
	
Secondary text

##### Streamlit Theme (.streamlit/config.toml)

```
primaryColor = "#7C3AED"
backgroundColor = "#F0F1F3"
secondaryBackgroundColor = "#FFFFFF"
textColor = "#1E293B"
font = "sans serif"

​
```

##### SVG Icons

Built-in SVG constants: ICON_SHIELD, ICON_CHECK, ICON_ALERT, ICON_CLOCK, ICON_GIT, ICON_TERMINAL, ICON_PACKAGE, ICON_LOCK

---

#### Page Renderers

Each page is a standalone function that renders the full page content.

Function
	
Page
	
Key Features

login_page()
	
Login
	
JWT token exchange, session persistence

dashboard_page()
	
Dashboard
	
Pending publishes, recent activity, quick stats

upload_page()
	
New Release
	
Multi-step wizard: pick engine → upload → parse → validate → configure → publish

release_detail_page()
	
Release Detail
	
Full rule list, diff, commit instructions, Jira epic link, export

history_page()
	
History
	
Searchable 6+ month archive, filterable by engine/type

compare_page()
	
Compare
	
Side-by-side diff of any two releases

statistics_page()
	
Statistics
	
Plotly charts: trends, formats, engines, contributors

validation_page()
	
Syntax Validation
	
Paste YARA/Sigma rules, instant syntax check

virustotal_page()
	
VT Retrohunt
	
Submit YARA, track jobs, browse matches

confluence_page()
	
Knowledge Base
	
Inline Confluence browser, full-text search

admiral_page()
	
Admiral Storage
	
Directory browser, upload, download, move, delete

admin_page()
	
Admin
	
Engine/repository/user management

---

#### Session State Variables

Streamlit uses st.session_state for persistence across reruns.

Variable
	
Type
	
Purpose

token
	
str
	
JWT authentication token

username
	
str
	
Current user's username

role
	
str
	
Current user's role

email
	
str
	
Current user's email

page
	
str
	
Current page/route name

release_step
	
str
	
Upload wizard step (pick_engine, upload_rules, etc.)

release_engine_group
	
dict
	
Selected engine configuration

parse_result
	
dict
	
Parsed rules from file upload

fileless_config
	
dict
	
Fileless engine automation config

fl_nb_override_mode
	
bool
	
Notebook override toggle

_prepared_version
	
str
	
Last prepared release version

_just_prepared
	
bool
	
Toast notification flag

fl_vt_test_result
	
dict
	
VirusTotal test results

_jupyter_test_ok
	
bool
	
Remote notebook test success

_jupyter_test_err
	
str
	
Remote notebook test error

_jupyter_test_diag
	
dict
	
Remote notebook diagnostic info

compare_result
	
dict
	
Compare view state

_cmp_cache_key
	
str
	
Compare cache key

bep_show_guide
	
bool
	
BEP guide visibility toggle

---

#### Helper Functions

##### Display & Formatting

Function
	
Purpose

inject_css()
	
Inject custom design CSS into Streamlit

status_badge(status, release)
	
Colored HTML badge for release status

type_badge(rt)
	
Release type badge (Sprint/Hot Fix)

change_sym(ct)
	
Change type symbol (+/-/~)

fmt_date(iso)
	
Format ISO date string

relative_time(iso)
	
"2 days ago", "3 hours ago", etc.

verification_label(conf)
	
Verification status display label

audit_event_style(action)
	
Style audit log entries by action type

build_stepper(steps)
	
Step progress indicator UI

workflow_stepper(status, release)
	
Release workflow progress

cmd_panel(label, lang, content)
	
Code command panel with copy button

svg_icon(name, size, color, extra_style)
	
Render SVG icon inline

page_header(title, subtitle)
	
Page header with title and subtitle

##### Business Logic

Function
	
Purpose

derive_jira_status(rel)
	
Extract Jira integration status from release

derive_verification_status(rel)
	
Derive verification method and status tuple

_get_engines()
	
Fetch all engines from backend API

_group_engines(engines)
	
Group engines by category for UI display

##### Sigma/BEP Rule Helpers

Function
	
Purpose

_cr_prefix(sigma_field)
	
Extract CR prefix from Sigma field name

_clean_sigma_value(raw, field_base)
	
Clean Sigma field value for display

_extract_sigma_selections(sigma_content)
	
Extract all Sigma detection selections

_build_necroowl_name(title)
	
Build NecroOwl rule name from title

_build_ui_url_path(terms)
	
Build UI rule path for NecroOwl

_render_necroowl_guide()
	
Render BEP NecroOwl detection guide

##### Jupyter/Notebook

Function
	
Purpose

_render_jupyter_fetch_results_card(vfr, key)
	
Render notebook execution results card

_merge_jupyter_fetch_payload(prev, new)
	
Merge incremental fetch results

##### API Client

Function
	
Purpose

get_headers()
	
Get auth headers with JWT token

api_get(path, **kw)
	
GET request to backend with auth

api_post(path, **kw)
	
POST request to backend with auth

api_post_json(path, data)
	
POST JSON body with auth

nav_to(page, **extra)
	
Navigate to a different page

---

#### Streamlit Dependencies

Package
	
Version
	
Purpose

streamlit
	
>= 1.38.0
	
UI framework

requests
	
>= 2.31.0
	
HTTP client for API calls

plotly
	
>= 5.20.0
	
Interactive charts (Plotly.js)

pandas
	
>= 2.1.0
	
Data processing for statistics

pyyaml
	
6.0.2
	
Sigma rule parsing in frontend

plyara
	
2.2.5
	
YARA rule parsing in frontend

pyzipper
	
>= 0.3.6
	
ZIP file handling

markdownify
	
0.13.1
	
HTML to Markdown conversion

---

#### Docker Configuration

```
FROM python:3.11-slim
EXPOSE 8501
HEALTHCHECK: curl --fail http://localhost:8501/_stcore/health
CMD: streamlit run app.py --server.port=8501 --server.address=0.0.0.0 --server.headless=true

​
```

Also copies adv_fileless_automation-test.ipynb as /app/adv_fileless_automation.ipynb for the fileless engine notebook automation feature.
