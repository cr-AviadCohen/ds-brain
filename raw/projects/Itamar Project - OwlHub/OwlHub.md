# OwlHub

> 💡 OwlHub — The nest where your agents live, collaborate, and stay safe.
> Multi-agent orchestration hub for AI security frameworks.
> Version 0.1.0

---

### What is OwlHub?

OwlHub is a centralized orchestration platform for autonomous AI agents. It provides management, monitoring, safety guardrails, and collaboration infrastructure for AI agent projects like VOWL (vulnerability scanning), Aidra (code analysis), and Owlint (DFIR/YARA generation).

Git - https://github.com/cybereason-labs/itamar-h/tree/owlhub

### Key Capabilities

Agent Management
Register and track agents across projects
Real-time heartbeat monitoring
Kill switches (individual, project, global emergency)
Task assignment and tracking
Safety & Security
LLM proxy with secret scrubbing (11 patterns)
Prompt injection detection (6 attack types)
Response scanning (PII, exfiltration, prompt leaks)
YAML-based policy engine
Human-in-the-loop approval queue
Full audit trail
Cross-Project Collaboration
Redis Streams event bus (pub/sub)
Cross-project tool calling
Multi-step workflow engine
Event-driven automation
Observability
Token and cost tracking per model/project
Real-time WebSocket streams
Streamlit dashboard with dark theme
Rich CLI with live monitoring

---

### Platform Components

Component
	
Type
	
Stack
	
Purpose

owlhub-core
	
Backend API
	
FastAPI + SQLAlchemy + Redis
	
Multi-agent orchestration backend (70+ endpoints)

owlhub-cli
	
CLI
	
Typer + Rich
	
Terminal interface and platform launcher

owlhub-dashboard
	
Web UI
	
Streamlit + Plotly
	
Real-time monitoring and control dashboard

owlhub-sdk
	
Library
	
Python + httpx
	
Agent integration SDK with OpenAI drop-in

---

### Documentation Index

All documentation pages are organized below. Click any page to dive deeper.

Page
	
Covers

Architecture & Overview
	
System diagram, deployment options, project structure, database schema, tech stack

Core API — Endpoints Reference
	
All 70+ REST endpoints across 14 routers, WebSocket streams

Backend Services
	
10 service modules: event bus, workflow engine, safety, response scanner, metrics, etc.

Safety & Security
	
Secret scrubbing, injection detection, response scanning, policy engine, HITL, audit trail

CLI Reference
	
All 8 command modules, platform launcher, display utilities

Dashboard
	
8 UI pages, authentication, theme, monitoring, security command center

Python SDK
	
Client, OpenAI drop-in, decorators, client-side safety, manifests

Event Bus & Workflows
	
Redis Streams pub/sub, workflow engine, cross-project tool calling

Integration Examples
	
VOWL (vuln scanning), Aidra (code analysis), Owlint (DFIR/YARA)

Configuration & Deployment
	
Environment variables, Docker Compose, local setup, Nginx, migrations

Testing
	
10 test files, test infrastructure, running tests
- 📄 [Architecture & Overview](https://www.notion.so/Architecture-Overview-339ae23bae1d81019d30dceba7194db5?pvs=25)
- 📄 [Core API — Endpoints Reference](https://www.notion.so/Core-API-Endpoints-Reference-339ae23bae1d8154a438d1a454a37445?pvs=25)
- 📄 [Backend Services](https://www.notion.so/Backend-Services-339ae23bae1d81139c38c2672bbcb419?pvs=25)
- 📄 [Safety & Security](https://www.notion.so/Safety-Security-339ae23bae1d8127a127c8f19efc45eb?pvs=25)
- 📄 [CLI Reference](https://www.notion.so/CLI-Reference-339ae23bae1d816b8abfc819ae99fc03?pvs=25)
- 📄 [Dashboard](https://www.notion.so/Dashboard-339ae23bae1d81f6a8b3ef54e0fb690f?pvs=25)
- 📄 [Python SDK](https://www.notion.so/Python-SDK-339ae23bae1d81ac94cfe36ae4c5a6d7?pvs=25)
- 📄 [Event Bus & Workflows](https://www.notion.so/Event-Bus-Workflows-339ae23bae1d81888ee4fae68e4cf2ec?pvs=25)
- 📄 [Integration Examples](https://www.notion.so/Integration-Examples-339ae23bae1d81819b2cc824109e30f5?pvs=25)
- 📄 [Configuration & Deployment](https://www.notion.so/Configuration-Deployment-339ae23bae1d815aba1ed45d7cb2d42a?pvs=25)
- 📄 [Testing](https://www.notion.so/Testing-339ae23bae1d8144bc81cbca5b4e619e?pvs=25)

---

# Subpages Content

---

## Architecture & Overview

#### System Architecture

```
graph TB
    subgraph Clients
        CLI["OwlHub CLI"]
        DASH["Dashboard"]
        SDK["Python SDK"]
    end
    subgraph Core["OwlHub Core API - FastAPI port 8000"]
        REG["Project Registry"]
        LLM["LLM Proxy"]
        SAF["Safety Engine"]
        WF["Workflow Engine"]
        MET["Metrics"]
        MON["Monitor"]
        EVT["Event Bus"]
        COL["Collaboration"]
    end
    subgraph Storage
        DB["SQLite or PostgreSQL"]
        REDIS["Redis Streams"]
    end
    CLI --> Core
    DASH --> Core
    SDK --> Core
    Core --> DB
    EVT --> REDIS

Storage

OwlHub Core API - FastAPI port 8000

Clients

SQLite or PostgreSQL

Redis Streams

Project Registry

LLM Proxy

Safety Engine

Workflow Engine

Metrics

Monitor

Event Bus

Collaboration

OwlHub CLI

Dashboard

Python SDK

​
```

---

#### Deployment Options

Docker Compose (Recommended)
docker-compose up -d

​
Starts owlhub (port 8000) + redis (port 6379) with persistent volumes.
Local Development
docker run -d -p 6379:6379 redis:7-alpine
pip install -r requirements.txt
cd owlhub-core && alembic upgrade head && cd ..
bash start.sh

​
Starts API (8000), Dashboard (8510), Nginx (8500/8501).

---

#### Access Points

Service
	
URL

API Docs (Swagger)
	
http://localhost:8000/docs

Dashboard
	
http://localhost:8501

Health Check
	
GET /api/health

---

#### Project Structure

```
owlhub/
├── owlhub-core/           # FastAPI backend (14 routers, 70+ endpoints)
├── owlhub-cli/            # Typer + Rich CLI (8 command modules)
├── owlhub-dashboard/      # Streamlit UI (13 components)
├── owlhub-sdk/            # Python SDK (httpx-based)
├── examples/              # 3 integration examples
├── docs/                  # API reference + architecture
├── docker-compose.yaml
├── start.sh
└── requirements.txt

​
```

---

#### Database Schema (14 Tables)

Model
	
Purpose

Project
	
AI agent projects (name, api_key_hash, status, max_agents)

Agent
	
Individual agents (type, status, current_task, last_heartbeat)

Task
	
Agent work items (title, status, priority)

Tool
	
Callable functions (schema, exposed, requires_approval)

Event
	
Cross-project events (type, source, data)

Workflow / WorkflowRun
	
Multi-step automation and execution tracking

Metric
	
Token usage, cost, latency per model/agent

AuditLog
	
Security audit trail (action, flags, blocked)

SafetyAlert
	
Security findings (severity, type, resolved)

ApprovalQueue
	
Human-in-the-loop approvals (risk_level, expires_at)

Log
	
Application logs (level, message, context)

Package
	
Security modules (type, version, manifest)

Repo
	
GitHub repositories (url, status, last_scan)

---

#### Technology Stack

Layer
	
Technology

API
	
FastAPI + Uvicorn

ORM
	
SQLAlchemy (async) + Alembic

Database
	
SQLite (aiosqlite) or PostgreSQL

Message Bus
	
Redis 7 Streams

LLM Router
	
LiteLLM

CLI
	
Typer + Rich

Dashboard
	
Streamlit + Plotly

HTTP Client
	
httpx

Validation
	
Pydantic v2

Reverse Proxy
	
Nginx

---

## Core API — Endpoints Reference

#### API Overview

FastAPI backend on port 8000 with 70+ endpoints across 14 routers. All routes prefixed with /api/.

---

#### Projects (/api/projects)

Method
	
Endpoint
	
Description

POST
	
/api/projects/
	
Create project (returns API key)

GET
	
/api/projects/
	
List projects (paginated)

GET
	
/api/projects/{id}
	
Get project details

PUT
	
/api/projects/{id}
	
Update project

DELETE
	
/api/projects/{id}
	
Delete project

---

#### Agents (/api/agents)

Method
	
Endpoint
	
Description

POST
	
/api/agents/
	
Register agent

GET
	
/api/agents/
	
List agents (filter by project_id)

GET
	
/api/agents/{id}
	
Get agent details

PUT
	
/api/agents/{id}
	
Update agent

DELETE
	
/api/agents/{id}
	
Delete agent

POST
	
/api/agents/heartbeat
	
Agent heartbeat

POST
	
/api/agents/{id}/kill
	
Kill single agent

POST
	
/api/agents/kill-all/{project_id}
	
Kill all in project

POST
	
/api/agents/emergency-kill-all
	
Emergency global kill

---

#### LLM Proxy (/api/llm)

Method
	
Endpoint
	
Description

POST
	
/api/llm/generate
	
LLM call with full safety pipeline

POST
	
/api/llm/kill/{agent_id}
	
Kill agent via proxy

Safety pipeline: Secret scan (11 patterns) → Injection detect (6 patterns) → Policy check → LiteLLM route → Response scan (PII, exfil, leaks) → Metrics + Audit

---

#### Safety (/api/safety)

##### Audit Logs

Method
	
Endpoint
	
Description

POST
	
/api/safety/audit-logs
	
Create audit entry

GET
	
/api/safety/audit-logs
	
Query (filter: project, action, blocked)

##### Safety Alerts

Method
	
Endpoint
	
Description

POST
	
/api/safety/alerts
	
Create alert

GET
	
/api/safety/alerts
	
Query (filter: severity, type, resolved)

PUT
	
/api/safety/alerts/{id}
	
Update/resolve alert

##### Approval Queue

Method
	
Endpoint
	
Description

POST
	
/api/safety/approvals
	
Submit for approval

GET
	
/api/safety/approvals
	
List pending

GET
	
/api/safety/approvals/{id}
	
Get details

PUT
	
/api/safety/approvals/{id}
	
Approve or deny

##### Logs

Method
	
Endpoint
	
Description

POST
	
/api/safety/logs
	
Create log

GET
	
/api/safety/logs
	
Query (filter by level)

---

#### Workflows (/api/workflows)

Method
	
Endpoint
	
Description

POST
	
/api/workflows/
	
Create workflow

GET
	
/api/workflows/
	
List workflows

GET
	
/api/workflows/{id}
	
Get workflow

PUT
	
/api/workflows/{id}
	
Update workflow

DELETE
	
/api/workflows/{id}
	
Delete workflow

GET
	
/api/workflows/{id}/runs
	
List runs

POST
	
/api/workflows/{id}/trigger
	
Manual trigger

Step types: emit_event, call_tool, transform_data, wait_approval

---

#### Events (/api/events)

Method
	
Endpoint
	
Description

POST
	
/api/events/
	
Publish event

GET
	
/api/events/
	
Query (filter: type, source, time range)

---

#### Metrics (/api/metrics)

Method
	
Endpoint
	
Description

GET
	
/api/metrics/
	
List metrics

GET
	
/api/metrics/summary
	
Aggregated per project

GET
	
/api/metrics/tokens/by-model
	
Token usage by model

GET
	
/api/metrics/tokens/by-project
	
Token usage by project

---

#### Tools (/api/tools)

Method
	
Endpoint
	
Description

POST
	
/api/tools/
	
Register tool

GET
	
/api/tools/
	
List tools

GET
	
/api/tools/{id}
	
Get tool

PUT
	
/api/tools/{id}
	
Update tool

DELETE
	
/api/tools/{id}
	
Delete tool

POST
	
/api/tools/call
	
Cross-project tool call

---

#### Tasks (/api/tasks)

Method
	
Endpoint
	
Description

POST
	
/api/tasks/
	
Create task

GET
	
/api/tasks/
	
List (filter: agent_id, status)

GET
	
/api/tasks/{id}
	
Get task

PUT
	
/api/tasks/{id}
	
Update task

DELETE
	
/api/tasks/{id}
	
Delete task

---

#### WebSocket Streams (/api/ws)

Protocol
	
Endpoint
	
Description

WS
	
/api/ws/safety
	
Real-time safety alerts

WS
	
/api/ws/events
	
Real-time event stream

WS
	
/api/ws/logs
	
Real-time log stream

---

#### Other Routers

Router
	
Prefix
	
Description

Health
	
/api/health
	
Service status

Repositories
	
/api/repos
	
GitHub repo import/scanning

Packages
	
/api/packages
	
Security module registry

---

## Backend Services

#### Services Overview

The backend has 10 service modules in owlhub-core/owlhub/services/ implementing core business logic.

---

#### Event Bus (event_bus.py)

Redis Streams-based pub/sub for cross-project communication.
- publish(event_type, data, source_project, source_agent) — Publish via XADD
- subscribe(consumer_group, consumer_name) — Subscribe via XREADGROUP
- get_events(filters) — Query stored events
- get_stream_info() — Stream metadata and pending counts

Uses consumer groups for reliable, ordered delivery across projects.

---

#### Workflow Engine (workflow_engine.py)

Multi-step automation triggered by events.
- trigger_workflow(workflow_id, event) — Start a run
- _execute_steps(run, steps) — Sequential execution

Step types: emit_event, call_tool, transform_data, wait_approval

Output passes between steps. Default 3 retries per step. Tracks started_at, completed_at, error.

---

#### Safety Service (safety.py)

Policy-based safety checks from YAML config.
- load_policies() — Load from safety_policies.yaml
- get_safety_policy(project_id) — Merge default + project overrides
- check_safety(action, context) — Evaluate against policies

Policies define blocked paths, blocked patterns, approval requirements, and token rate limits.

---

#### Response Scanner (response_scanner.py)

Scans LLM outputs before returning to agents.

scan_response(text) detects: system prompt leaks, PII (SSN, passport, credit card, email), and data exfiltration attempts.

---

#### Collaboration (collaboration.py)

Cross-project tool calling with audit trails.
- register_tool_handler(name, handler) — Register callable
- call_tool(caller, target, tool, input) — Invoke with audit

---

#### Monitor (monitor.py)

Agent health via heartbeats. check_agent_health() identifies stale agents.

---

#### Metrics (metrics.py)

Token and cost tracking.
- record_metric(project, agent, type, model, tokens, cost, latency)
- aggregate_metrics(project_id) — Summarize per project

---

#### Other Services
- LLM Proxy (llm_proxy.py) — Routes calls through LiteLLM
- Registry (registry.py) — Project lookup and validation
- Package Registry (package_registry.py) — YAML-based security packages

---

#### Middleware

Middleware
	
Purpose
	
Details

auth.py
	
API key validation
	
Validates X-OwlHub-Key header

rate_limit.py
	
Token rate limiting
	
Per-project, default 100K tokens/min

logging.py
	
Request/response logging
	
Full audit trail

---

## Safety & Security

#### Overview

OwlHub provides defense-in-depth security for AI agent operations. Every LLM call, tool invocation, and agent action passes through multiple safety layers.

---

#### Security Pipeline

```
graph LR
    A["Agent Request"] --> B["Secret Scanner"]
    B --> C["Injection Detector"]
    C --> D["Policy Engine"]
    D --> E["Rate Limiter"]
    E --> F["LLM Provider"]
    F --> G["Response Scanner"]
    G --> H["Audit Logger"]
    H --> I["Agent Response"]

Agent Request

Secret Scanner

Injection Detector

Policy Engine

Rate Limiter

LLM Provider

Response Scanner

Audit Logger

Agent Response

​
```

---

#### Secret Scrubbing (11 Patterns)

All prompts are scanned before reaching the LLM. Detected secrets are blocked and logged.

Detected patterns include:
- AWS Access Keys and Secret Keys
- GitHub Tokens (ghp_, gho_, github_pat_)
- OpenAI and Anthropic API Keys
- Private Key material
- Slack Tokens
- Passwords and secrets in assignments

---

#### Prompt Injection Detection (6 Patterns)

Detects attempts to manipulate agent behavior:
1. Instruction Override — attempts to ignore previous instructions
1. Role Manipulation — "you are now" / "act as" attacks
1. Context Wipe — disregard previous context
1. Memory Wipe — forget instructions
1. Prompt Extraction — reveal system prompt attempts
1. Prompt Leak — "what is your prompt" queries

---

#### Response Scanner

Scans all LLM outputs before returning to agents:

<details><summary>System Prompt Leak Detection</summary>

</details>

<details><summary>PII Detection</summary>

</details>

<details><summary>Data Exfiltration Detection</summary>

</details>

---

#### Policy Engine

YAML-based safety policies with per-project overrides.

Policy fields:
- blocked_paths — File paths agents cannot access
- blocked_patterns — Regex patterns to block
- requires_approval — Actions needing human sign-off
- token_rate_limit — Max tokens per minute (default 100K)

---

#### Human-in-the-Loop (HITL)

Sensitive actions require human approval before execution.

Actions requiring approval:
- execute_shell — Running shell commands
- delete_resource — Deleting data or resources
- modify_safety_policy — Changing safety config

Approval workflow:
1. Agent submits action to approval queue
1. Action enters pending state with risk level
1. Human reviews in Dashboard or via API
1. Approve or deny with reason
1. Approval expires after timeout (default: 1 hour)

---

#### Audit Trail

Every action is logged with: project_id, agent_id, action_type, action_detail (JSON), safety_flags, blocked status, and timestamp.

---

#### Safety Alerts

Four severity levels: critical, high, medium, low

Alerts are generated when secrets are detected, injection is attempted, PII is found, rate limits are exceeded, or policies are violated.

Alerts can be viewed and resolved via the Dashboard Security Command Center or the API.

---

#### Rate Limiting
- Per-project token rate limiting
- Default: 100,000 tokens per minute
- Configurable via environment variable
- Tracked by middleware on every LLM proxy request

---

## CLI Reference

#### Overview

The OwlHub CLI is built with Typer and Rich for a polished terminal experience. It serves as both an interface to the API and the platform launcher.

```
pip install -r requirements.txt

​
```

---

#### Global Commands

Command
	
Description

owlhub
	
Launch the full platform (API + Dashboard + Nginx)

owlhub start
	
Start the platform

owlhub stop
	
Stop all running processes

owlhub version
	
Show CLI version (0.1.0)

---

#### Projects

```
owlhub projects list [--offset 0] [--limit 50]
owlhub projects status <name>
owlhub projects pause <name>
owlhub projects resume <name>

​
```

Manage AI agent projects: list, inspect, pause, and resume.

---

#### Agents

```
owlhub agents list [--project <name>]
owlhub agents watch
owlhub agents kill <agent_id>

​
```
- list — List agents, optionally filtered by project
- watch — Live-updating agent table (refreshes every 5s)
- kill — Terminate a specific agent

---

#### Safety

```
owlhub safety alerts [--severity critical|high|medium|low]
owlhub safety audit-logs
owlhub safety approvals

​
```

View safety alerts, audit logs, and pending approval requests.

---

#### Events

```
owlhub events stream
owlhub events history

​
```
- stream — Real-time event stream from Redis
- history — Query historical events

---

#### Workflows

```
owlhub workflows list
owlhub workflows trigger <workflow_id>

​
```

List and manually trigger workflows.

---

#### Metrics

```
owlhub metrics summary
owlhub metrics tokens

​
```
- summary — Aggregated metrics overview
- tokens — Token usage by model and project

---

#### Tools

```
owlhub tools list
owlhub tools call

​
```

List available tools and invoke cross-project tool calls.

---

#### Platform Launcher

When you run owlhub with no arguments, the launcher:
1. Kills any previous instances
1. Frees ports 8000, 8500, 8501, 8510
1. Starts backend API (uvicorn on port 8000)
1. Waits for API health check
1. Starts Streamlit dashboard (port 8510)
1. Starts Nginx reverse proxy (8500/8501 to 8510)
1. Auto-restarts dashboard on crash
1. Handles Ctrl+C with graceful cleanup

---

#### Display Utilities

The CLI uses Rich for formatted output:
- Color-coded status badges (green=active, red=error, yellow=idle, blue=info)
- Professional terminal tables
- Relative timestamps ("5m ago", "2h ago")
- Styled error/success/info messages

---

## Dashboard

#### Overview

The OwlHub Dashboard is a Streamlit web application with a professional dark theme, real-time monitoring, and 8 main pages. It runs on port 8510 internally, proxied via Nginx to ports 8500/8501.

Default login: admin / admin

---

#### Authentication System

SQLite-backed auth with session management.
- Database: data/users.db with users and sessions tables
- Roles: admin, user
- Session expiry: 480 minutes (8 hours, rolling)
- Session tokens: secrets.token_hex
- Functions: init_user_db(), create_session(), validate_session(), delete_session(), cleanup_expired_sessions()

---

#### Pages

##### 1. Dashboard (Overview)

564 lines — components/dashboard.py
- Project count, agent count, active tasks
- Recent metrics summary
- Token usage charts (Plotly)
- Cost breakdown by model
- System health indicators

##### 2. Projects

459 lines — components/projects.py
- Create, edit, delete projects
- View agent counts per project
- Project status management (active/paused)
- API key display

##### 3. Terminal

1019 lines — components/terminal.py
- Live terminal for command execution
- Stream logs in real-time
- Manage running agents and projects
- Green-on-black terminal styling

##### 4. Repositories

106 lines — components/repos.py
- GitHub repository import
- Repository scanning status
- Clone and scan workflows

##### 5. Packages

69 lines — components/packages.py
- Browse security modules and templates
- Install/configure packages
- View package manifests

##### 6. Monitoring

806 lines — components/monitoring.py
- Real-time agent status dashboard
- Heartbeat tracking with staleness detection
- Agent task details and progress
- Kill switches (individual agent, project-wide, emergency global)
- Agent type filtering

##### 7. Security Command Center

907 lines — components/security.py
- Risk posture gauge visualization
- Recent safety alerts with severity badges
- Audit log viewer with filtering
- Approval queue management (approve/deny actions)
- Human-in-the-loop controls
- Alert resolution workflow

##### 8. Settings

115 lines — components/settings.py
- User account settings
- Environment variable configuration
- Platform preferences

---

#### Supporting Modules

Module
	
Lines
	
Purpose

api_client.py
	
212
	
HTTP client wrapper for OwlHub API

auth.py
	
303
	
Authentication system

rbac.py
	
12
	
Role-based access control helper

shared_utils.py
	
41
	
Shared utility functions

---

#### Theme & Styling

274 lines of custom CSS with:
- Primary: red (#e94560)
- Secondary: dark blue (#0f3460)
- Backgrounds: black (#0e1117), dark gray (#1a1a2e), card blue (#16213e)
- Text: light gray (#e0e0e0), secondary (#a0a0b0)
- Status badges: green (active), red (error), yellow (pending), blue (info)
- Terminal: green text on black background
- Metric cards: gradient backgrounds with white values

---

#### Navigation

Sidebar with 8 pages:
1. Dashboard — Metrics overview
1. Projects — Manage projects
1. Terminal — Live command execution
1. Repositories — GitHub imports
1. Packages — Security modules
1. Monitoring — Agent status
1. Security — Safety control center
1. Settings — Configuration

---

## Python SDK

#### Overview

The OwlHub SDK (owlhub-sdk/) is a Python library that makes it easy for agents to integrate with the OwlHub platform. It provides an HTTP client, decorators for agent tracking, an OpenAI-compatible drop-in replacement, and client-side safety checks.

Install: pip install httpx (the only dependency)

---

#### Configuration (config.py)

```
from owlhub_sdk import OwlHubConfig

config = OwlHubConfig(
    api_url="http://localhost:8000",   # or OWLHUB_API_URL env
    api_key="your-project-key",         # or OWLHUB_API_KEY env
    project_id="your-project-id"        # or OWLHUB_PROJECT_ID env
)

​
```

---

#### HTTP Client (client.py)

Low-level async HTTP client using httpx.

```
from owlhub_sdk import OwlHubClient

client = OwlHubClient(config)
response = await client.generate(
    prompt="Analyze this code",
    model="claude-sonnet-4-20250514",
    system_prompt="You are a security analyst",
    max_tokens=2000,
    temperature=0.7
)
print(response.content)
await client.close()

​
```

---

#### OpenAI Drop-in Replacement (openai_compat.py)

Replace the official OpenAI client with OwlHub's secured proxy — zero code changes needed.

```
from owlhub_sdk import OpenAI

client = OpenAI(api_url, api_key, project_id)
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)

​
```

All calls go through OwlHub's safety pipeline (secret scanning, injection detection, response scanning).

---

#### Decorators (decorators.py)

##### @track_agent

Automatically logs agent lifecycle (start, completion, error) with execution time.

```
from owlhub_sdk import track_agent

@track_agent(name="scanner", hub=client)
async def scan_repo(repo_path: str) -> list:
    # Your agent logic here
    return vulnerabilities

​
```

##### @expose_tool

Marks a function as callable from other projects via the cross-project tool system.

```
from owlhub_sdk import expose_tool

@expose_tool(name="scan_repo", description="Scan a git repo")
async def scan_repo_tool(repo_path: str) -> list:
    return await scan_repo(repo_path)

​
```

---

#### Client-Side Safety (safety.py)

```
from owlhub_sdk.safety import scan_for_secrets, check_prompt_safety

# Scan text for embedded secrets
findings = scan_for_secrets(text)

# Check if a prompt is safe to send
safe, reason = check_prompt_safety(prompt)

​
```

---

#### Manifest Loader (manifest.py)

Load and validate YAML agent manifests.

```
from owlhub_sdk.manifest import load_manifest, validate_manifest

config = load_manifest("agent.yaml")
errors = validate_manifest(config)

​
```

Manifests can define: agents, tools, event subscriptions, and safety policies.

---

#### Events (events.py) and Interceptors (interceptors.py)
- Events — Subscribe to and handle cross-project events
- Interceptors — Request/response hooks for advanced use cases (logging, transformation, etc.)

---

## Event Bus & Workflows

#### Event Bus

OwlHub uses Redis Streams (XADD/XREADGROUP) as the event bus for cross-project communication.

##### How It Works
1. Publishing: Any project can publish events via POST /api/events/ or event_bus.publish()
1. Subscribing: Projects subscribe to event types using consumer groups
1. Delivery: Redis Streams ensure ordered, reliable delivery with acknowledgment
1. Storage: Events are persisted in both Redis (real-time) and the database (history)

##### Event Structure

Field
	
Description

event_type
	
Event category (e.g., "vulnerability.discovered")

source_project
	
Which project emitted the event

source_agent
	
Which agent emitted the event

data
	
JSON payload with event details

consumed_by
	
Which projects have consumed this event

created_at
	
Timestamp

##### Common Event Types
- vulnerability.discovered — VOWL found a vulnerability
- analysis.complete — Aidra finished code analysis
- vulnerability.patched — A patch was applied
- report.collected — Owlint collected a DFIR report
- rule.generated — YARA/Sigma rules were generated
- intel.enriched — Threat intelligence was added
- scan.completed — A scan finished

---

#### Workflow Engine

Automate multi-step processes triggered by events.

##### Workflow Definition

Field
	
Description

name
	
Workflow name

trigger_event
	
Event type that triggers execution

trigger_filter
	
JSON filter to match specific events

steps
	
Ordered list of step definitions

enabled
	
Whether the workflow is active

##### Step Types

<details><summary>emit_event</summary>

</details>

<details><summary>call_tool</summary>

</details>

<details><summary>transform_data</summary>

</details>

<details><summary>wait_approval</summary>

</details>

##### Execution Model
1. Event matches a workflow's trigger_event and trigger_filter
1. A WorkflowRun is created with status "running"
1. Steps execute sequentially — each step's output feeds the next
1. Failed steps retry up to 3 times
1. On completion, status becomes "completed" with timestamp
1. On failure, status becomes "failed" with error details

##### API Endpoints

Method
	
Endpoint
	
Description

POST
	
/api/workflows/
	
Create workflow

GET
	
/api/workflows/
	
List workflows

GET
	
/api/workflows/{id}
	
Get details

PUT
	
/api/workflows/{id}
	
Update

DELETE
	
/api/workflows/{id}
	
Delete

GET
	
/api/workflows/{id}/runs
	
List runs

POST
	
/api/workflows/{id}/trigger
	
Manual trigger

---

#### Cross-Project Tool Calling

Projects can expose tools for other projects to call.

##### How It Works
1. Register: A project registers a tool via POST /api/tools/ with name, schema, and exposed=true
1. Discover: Other projects find tools via GET /api/tools/?exposed=true
1. Call: Projects invoke via POST /api/tools/call with caller, target, tool name, and input
1. Audit: Every call is logged to the audit trail

##### Tool Properties

Field
	
Description

name
	
Tool identifier

description
	
What the tool does

input_schema
	
JSON Schema for input validation

output_schema
	
JSON Schema for output

exposed
	
Whether other projects can call it

requires_approval
	
Whether calls need human approval

call_count
	
Total invocations tracked

---

## Integration Examples

#### Overview

OwlHub ships with 3 integration examples in examples/ showing how real AI agent projects connect to the platform. These demonstrate event-driven collaboration between projects.

---

#### VOWL — Vulnerability Scanning

File: examples/vowl_integration.py (117 lines)

VOWL is a vulnerability scanning agent that discovers, analyzes, and patches security issues in code repositories.

##### Agents
- scanner — Scans repos for vulnerabilities, emits vulnerability.discovered and scan.completed events
- patcher — Generates patches via LLM, requests human approval for critical vulnerabilities

##### Key Features
- Uses @track_agent for automatic lifecycle logging
- Emits events that trigger Aidra's code analysis
- Requests HITL approval before patching critical vulnerabilities
- Listens for analysis.complete events from Aidra to enhance patching
- Exposes scan_repo as a cross-project tool

##### Event Flow

```
graph LR
    A["VOWL Scanner"] -->|"vulnerability.discovered"| B["Event Bus"]
    B -->|"triggers"| C["Aidra Analyzer"]
    C -->|"analysis.complete"| B
    B -->|"triggers"| D["VOWL Patcher"]
    D -->|"vulnerability.patched"| B

VOWL Scanner

Event Bus

Aidra Analyzer

VOWL Patcher

vulnerability.discovered

triggers

analysis.complete

triggers

vulnerability.patched

​
```

---

#### Aidra — Code Analysis

File: examples/aidra_integration.py (77 lines)

Aidra performs deep code analysis using LLMs, producing security risk scores and detailed findings.

##### Agents
- analyzer — Routes LLM calls through OwlHub proxy for secured analysis

##### Key Features
- Listens for vulnerability.discovered events from VOWL
- Analyzes code files using Claude through the LLM proxy
- Produces risk scores and structured findings
- Emits analysis.complete for downstream consumers
- Exposes analyze_code as a cross-project tool

---

#### Owlint — DFIR & YARA Generation

File: examples/owlint_integration.py (102 lines)

Owlint collects DFIR reports, extracts IOCs (Indicators of Compromise), and generates detection rules.

##### Agents
- collector — Parses DFIR reports, extracts IOCs (IPs, hashes, domains)
- generator — Uses LLM to generate YARA and Sigma detection rules

##### Key Features
- Extracts IOCs: IP addresses, file hashes, malicious domains
- Generates both YARA and Sigma rules via LLM
- Listens for vulnerability.discovered to enrich with threat intelligence
- Emits report.collected, rule.generated, and intel.enriched events
- Exposes search_threat_intel as a cross-project tool

---

#### Cross-Project Collaboration Flow

All three projects work together through the event bus:

```
graph TB
    subgraph VOWL
        VS["Scanner"]
        VP["Patcher"]
    end
    subgraph Aidra
        AA["Analyzer"]
    end
    subgraph Owlint
        OC["Collector"]
        OG["Generator"]
    end
    subgraph OwlHub["OwlHub Core"]
        EB["Event Bus"]
        LP["LLM Proxy"]
        ST["Safety"]
    end
    VS -->|"vulnerability.discovered"| EB
    EB -->|"triggers"| AA
    EB -->|"triggers"| OC
    AA -->|"analysis.complete"| EB
    EB -->|"enriches"| VP
    OC --> OG
    OG -->|"rule.generated"| EB
    VS --> LP
    AA --> LP
    OG --> LP
    LP --> ST

OwlHub Core

Owlint

Aidra

VOWL

Event Bus

LLM Proxy

Safety

Collector

Generator

Analyzer

Scanner

Patcher

vulnerability.discovered

triggers

triggers

analysis.complete

enriches

rule.generated

​
```

---

#### SDK Patterns Used

All examples demonstrate these SDK patterns:

Pattern
	
Usage

@track_agent(name, hub)
	
Automatic agent lifecycle tracking

client.llm_generate()
	
Secured LLM calls through proxy

client.emit_event()
	
Cross-project event publishing

@client.on_event()
	
Event subscription and handling

client.request_approval()
	
Human-in-the-loop for critical actions

@client.expose_tool()
	
Cross-project tool exposure

client.log()
	
Centralized logging

---

## Configuration & Deployment

#### Environment Variables

Variable
	
Default
	
Purpose

DATABASE_URL
	
sqlite+aiosqlite:///./data/owlhub.db
	
Database connection string

REDIS_URL
	
redis://localhost:6379/0
	
Redis event bus

OWLHUB_ADMIN_KEY
	
admin-dev-key
	
Admin authentication key

OWLHUB_SECRET_KEY
	
change-me-in-production
	
Signing secret

LITELLM_API_BASE
	
(unset)
	
LLM provider endpoint

LITELLM_MASTER_KEY
	
(unset)
	
LLM provider key

LOG_LEVEL
	
INFO
	
Logging verbosity

MAX_TOKENS_PER_MINUTE
	
100000
	
Token rate limit

APPROVAL_TIMEOUT_SECONDS
	
3600
	
HITL approval timeout

Copy .env.example to .env and customize.

---

#### Docker Compose

```
services:
  owlhub:
    build: ./owlhub-core
    ports:
      - "8000:8000"
    volumes:
      - owlhub-data:/app/data
    depends_on:
      - redis
  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    volumes:
      - redis-data:/data

​
```

Start with docker-compose up -d

---

#### Local Setup Steps
1. Start Redis

```
docker run -d -p 6379:6379 redis:7-alpine

​
```
1. Install dependencies

```
pip install -r requirements.txt

​
```
1. Initialize database

```
cd owlhub-core && alembic upgrade head && cd ..

​
```
1. Configure environment

```
cp .env.example .env
# Edit .env with your settings

​
```
1. Launch platform

```
bash start.sh
# Or use the CLI:
owlhub

​
```

---

#### start.sh Launcher (142 lines)

The launcher script handles the full startup sequence:
1. Kills previous instances (nginx, API, dashboard)
1. Frees ports 8000, 8500, 8501, 8510
1. Starts uvicorn API server (port 8000)
1. Waits for health check to pass
1. Starts Streamlit dashboard (port 8510)
1. Configures and starts Nginx reverse proxy
1. Auto-restarts dashboard on crash
1. Graceful shutdown on Ctrl+C

---

#### Nginx Configuration

Reverse proxy setup:
- Port 8500 proxies to Streamlit (8510)
- Port 8501 proxies to Streamlit (8510)
- Handles WebSocket upgrades for real-time features

---

#### Database Migrations

Using Alembic (owlhub-core/alembic/):
- Single initial migration creates all 14 tables + 13 indexes
- Run: cd owlhub-core && alembic upgrade head
- Supports SQLite (dev) and PostgreSQL (production)

---

#### Dependencies

##### Core Backend
- fastapi, uvicorn, sqlalchemy (async), aiosqlite, alembic
- pydantic, pydantic-settings, redis, litellm
- httpx, websockets, pyyaml

##### CLI
- typer, rich, httpx

##### Dashboard
- streamlit, plotly, requests

##### SDK
- httpx

##### Dev/Testing
- pytest, pytest-asyncio, pytest-cov, fakeredis

---

## Testing

#### Test Suite Overview

OwlHub has 10 test files in owlhub-core/tests/ covering all major components.

```
cd owlhub-core
pytest tests/ -v

​
```

---

#### Test Files

Test File
	
What It Tests

conftest.py
	
Pytest fixtures, async event loop setup, test DB

test_projects.py
	
Project CRUD: create, list, get, update, delete

test_agents.py
	
Agent registration, heartbeat, kill switches

test_safety.py
	
Secret scanning, injection detection, policy checks

test_safety_crud.py
	
Safety model CRUD: audit logs, alerts, approvals

test_llm_proxy.py
	
LLM routing, safety pipeline, metrics recording

test_events.py
	
Event creation, querying, filtering

test_workflows.py
	
Workflow definition, triggering, step execution

test_tasks.py
	
Task CRUD, status updates, filtering

---

#### Test Infrastructure
- Framework: pytest + pytest-asyncio
- Database: In-memory SQLite for fast, isolated tests
- Redis: fakeredis for event bus testing without real Redis
- Coverage: pytest-cov for coverage reporting
- Async: Full async/await test support

---

#### Running Tests

```
# All tests
pytest tests/ -v

# Specific test file
pytest tests/test_safety.py -v

# With coverage
pytest tests/ --cov=owlhub --cov-report=html

# Only async tests
pytest tests/ -v -k "async"

​
```

---

#### Test Dependencies

```
pytest>=7.4.0
pytest-asyncio>=0.23.0
pytest-cov>=4.1.0
fakeredis[lua]>=2.20.0

​
```
