# Sunrise Platform — Technical Answers for Vendor Questions

**Source**: Vendor questionnaire received March 2026
**Audience**: External vendor / partner
**Purpose**: Answer technical questions about Sunrise platform capabilities based on the current codebase
**Date**: March 2026

---

## 1. Do you have an IDM solution?

**Yes.** Sunrise implements a comprehensive, multi-protocol Identity Management solution.

### Supported Authentication Protocols

| Protocol | Implementation | Location |
|----------|---------------|----------|
| **SAML 2.0** | Full SSO with SP/IdP configuration, x509 certificate validation, NameID extraction | `sunrise-lambda-gateway` — `lib/saml2.py` |
| **OpenID Connect (OIDC)** | OAuth 2.0 authorization code flow with HMAC-HS256 JWT tokens, UserInfo endpoint | `sunrise-lambda-gateway` — `int_devo_oidc.py` |
| **Portal-native auth** | Username/password with multi-factor authentication (email, SMS, TOTP/authenticator app) | `sunrise-lambda-gateway` — `int_portal_login.py` |

### Key Capabilities

- **Multi-tenant SSO management**: Per-customer SAML configuration via REST API (`sunrise-app-accountmgmt` — `api/v1/accountmgmts/sso.py`)
- **Multi-factor authentication**: Email, SMS, and TOTP/authenticator app
- **Role-based access control (RBAC)** with internal and external role hierarchies:
  - **External roles**: `Accounts.User`, `Accounts.Admin`, `General.API`, `MTDR.Analyst`, `MTDR.Auditor`, `MTDR.Responder`
  - **Internal roles**: `Internal.Admin`, `Internal.Impersonate`, `Operations.Analyst`, `Operations.Lead`, `Operations.Manager`
  - **Service roles**: `Configs.API`, `Metadata.API`
- **Session management**: Token-based sessions with configurable TTLs (e.g., 8-hour portal tokens, 30-minute sessions), cross-tab synchronization, inactivity timeout with warning
- **Additional flows**: Password reset, user registration with email/phone verification, admin impersonation, mobile app authentication
- **Credential management service** (`sunrise-app-credential`): Stores and manages API credentials, access keys, and integration secrets

### Data Storage

- **Redis** for session state, SSO configuration cache, and token management
- **PostgreSQL** for persistent user accounts, SSO configurations, and credential storage
- SSO data models defined in `sunrise-model` — `schema/model/sso.py` (supports `SsoMode.SAML` and `SsoMode.OIDC`)

---

## 2. Sunrise DB Schemas

### 2.1 Incident Schema

**Table**: `incidents`
**Model**: `sunrise-model/tw/sunrise/core/schema/model/incident.py`

#### Enums

| Enum | Values |
|------|--------|
| `IncidentStatus` | Active, In Progress, Redirected, Resolved |
| `IncidentSeverity` | Informational, Low, Medium, High, Critical |
| `IncidentPriority` | Low, Medium, High, Unknown |
| `IncidentClassification` | True Positive, False Positive, Benign, Unknown |
| `IncidentDetermination` | Adv Persistent Threat, Malware, Security Personnel, Security Testing, Unwanted Software, Multi Staged Attack, Compromised Account, Phishing, Malicious User Activity, Not Malicious, Insufficient Data, Confirmed Activity, Business Application, Other, Unknown |

#### Fields

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `id` | String | NO | Auto-generated reference ID with `IN` prefix |
| `case_id` | String | NO | FK → `cases.id` |
| `source_id` | Text | NO | Unique identifier from source vendor system |
| `source_redirected_id` | Text | YES | Vendor incident ID this was merged into |
| `source_assigned_to` | Text | YES | Owner on source system |
| `merged_to_incident_id` | String | YES | Sunrise incident ID merged into |
| `integration_name` | Text | NO | Credential integration name used to access source |
| `last_sync_at` | DateTime | NO | Last sync with source system |
| `ingested_at` | DateTime | NO | When Sunrise received the incident |
| `source_created_at` | DateTime | NO | Creation time on source system |
| `source_updated_at` | DateTime | NO | Last update on source system |
| `reopened_at` | DateTime | YES | When reopened |
| `closed_at` | DateTime | YES | When resolved/closed |
| `closed_by` | Text | YES | User ID who closed |
| `description` | Text | YES | Incident description |
| `analysis` | Text | YES | Tier0/Analyst analysis |
| `suggested_remediation` | Text | YES | Remediation suggestions |
| `status` | Enum(IncidentStatus) | NO | Current status |
| `source_status` | Text | YES | Unaltered status from source |
| `severity` | Enum(IncidentSeverity) | NO | Impact severity |
| `priority` | Enum(IncidentPriority) | NO | Priority level |
| `source_priority` | Text | YES | Original priority from source |
| `classification` | Text | YES | Classification on resolution |
| `determination` | Text | YES | Determination on resolution |
| `source_link` | Text | YES | Web URL to incident on source system |
| `additional_details` | JSONB | YES | Additional vendor-specific details |
| `created_at` | DateTime | NO | Record creation time |
| `created_by` | Text | NO | User who created |
| `updated_at` | DateTime | NO | Last update time |
| `updated_by` | Text | YES | User who updated |
| `customer_id` | Text | NO | Customer/tenant identifier |
| `region` | Enum | NO | Region: ams, emea, aus, gov, global |

#### Relationships

| Relationship | Target | Cardinality | Behavior |
|-------------|--------|-------------|----------|
| `alerts` | Alert | 1:Many | Cascade delete |
| `evidences` | Evidence | 1:Many | Cascade delete |
| `entities` | ObservedEntity | 1:Many | Cascade delete |
| `case` | Case | Many:1 | — |

---

### 2.2 Alert Schema

**Table**: `alerts`
**Model**: `sunrise-model/tw/sunrise/core/schema/model/alert.py`

#### Fields

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `id` | String | NO | Auto-generated reference ID with `AL` prefix |
| `incident_id` | String | NO | FK → `incidents.id` |
| `source_id` | Text | NO | Alert identifier on source system |
| `last_sync_at` | DateTime | NO | Last sync with source system |
| `generated_at` | DateTime | NO | When source created alert |
| `closed_at` | DateTime | YES | When source resolved/closed |
| `source_created_at` | DateTime | NO | Creation time on source system |
| `source_updated_at` | DateTime | NO | Last update on source system |
| `first_activity_at` | DateTime | YES | Earliest associated activity |
| `last_activity_at` | DateTime | YES | Latest associated activity |
| `name` | Text | NO | Alert name |
| `description` | Text | YES | Alert description |
| `category` | Text | YES | Kill-chain category (MITRE ATT&CK aligned) |
| `source_policy_ref` | Text | YES | Policy ID/name on source |
| `detection_method` | Text | YES | Detection technology/sensor |
| `detector_ref` | Text | YES | Detector name/ID that triggered |
| `product_ref` | Text | YES | Product name that published this alert |
| `mitre_tactics` | Array[String] | YES | MITRE ATT&CK tactics |
| `mitre_techniques` | Array[String] | YES | MITRE ATT&CK techniques |
| `threat_name` | Text | YES | Threat/malware name |
| `threat_family` | Text | YES | Threat/malware family |
| `source_recommendations` | Text | YES | Remediation actions from source |
| `source_link` | Text | YES | Web URL to alert on source system |
| `additional_details` | JSONB | YES | Additional vendor-specific details |
| `created_at` | DateTime | NO | Record creation time |
| `created_by` | Text | NO | User who created |
| `updated_at` | DateTime | NO | Last update time |
| `updated_by` | Text | YES | User who updated |
| `customer_id` | Text | NO | Customer/tenant identifier |
| `region` | Enum | NO | Region: ams, emea, aus, gov, global |

#### Relationships

| Relationship | Target | Cardinality | Behavior |
|-------------|--------|-------------|----------|
| `incident` | Incident | Many:1 | Eager loaded |
| `events` | CachedEvent | 1:Many | Cascade delete, eager loaded |
| `evidences` | Evidence | 1:Many | Eager loaded, filtered by alert_id |

---

### 2.3 Evidence Schema

**Table**: `evidences`
**Model**: `sunrise-model/tw/sunrise/core/schema/model/evidence.py`

#### Fields

| Field | Type | Nullable | Description |
|-------|------|----------|-------------|
| `id` | String | NO | Auto-generated reference ID with `EV` prefix |
| `incident_id` | String | NO | FK → `incidents.id` |
| `alert_id` | String | YES | FK → `alerts.id` (optional — evidence can be incident-level) |
| `roles` | Array[String] | YES | Role(s) entity represents in alert |
| `role_details` | Array[String] | YES | Detailed role descriptions |
| `remediation_status` | Text | YES | Status of remediation action |
| `remediation_status_detail` | Text | YES | Details about remediation status |
| `verdict` | Text | YES | Decision from automated investigation |
| `tags` | Array[String] | YES | Custom tags for evidence |
| `detail` | JSONB | YES | All other evidence key/value pairs from source |
| `created_at` | DateTime | NO | Record creation time |
| `created_by` | Text | NO | User who created |
| `updated_at` | DateTime | NO | Last update time |
| `updated_by` | Text | YES | User who updated |
| `customer_id` | Text | NO | Customer/tenant identifier |
| `region` | Enum | NO | Region: ams, emea, aus, gov, global |

#### Relationships

| Relationship | Target | Cardinality | Behavior |
|-------------|--------|-------------|----------|
| `incident` | Incident | Many:1 | — |
| `alert` | Alert | Many:1 | Eager loaded (optional) |

---

## 3. Are there alerts based on a mix of alerts from different vendors?

### About the `product_ref` field

The `product_ref` field on each alert stores the **vendor product name** that generated the alert. It is populated during ingestion from each vendor's normalized data. The values per vendor are:

| Vendor | `product_ref` Value | Source |
|--------|---------------------|--------|
| Microsoft Defender | Dynamic — extracted from API response `vendorInformation.productName` (e.g., "Microsoft Defender for Endpoint", "Microsoft Defender for Identity") | `defender/incidents.py` |
| CrowdStrike | `"CrowdStrike Falcon"` | `crowdstrike/incidents.py` |
| SentinelOne | `"Singularity"` | `sentinelone/incidents.py` |
| Cybereason | `"Cybereason EDR"` | `cybereason/incidents.py` |
| Cortex XDR | `"Cortex XDR"` | `cortex/incidents.py` |
| Cortex XSIAM | `"Cortex XSIAM"` | `cortex_xsiam/incidents.py` |
| Carbon Black | `"Carbon Black Cloud"` | `carbonblack/incidents.py` |
| IBM QRadar | `"IBM QRadar SIEM"` | `qradar/incidents.py` |
| USM Anywhere | Dynamic — from alarm data, defaults to `"USM Anywhere"` | `usm/incidents.py` |

### Current behavior: Incidents are vendor-isolated

In the current architecture, **incidents are ingested per-vendor independently**. Each incident record is tied to a single `integration_name` (the credential/vendor integration used to fetch it) and a `source_id` (the vendor's incident identifier).

- The Temporal workflow orchestrates ingestion from each vendor separately.
- Alerts within a single incident all come from the **same vendor** because the incident itself originates from that vendor's system.
- There is **no automatic cross-vendor correlation** that merges alerts from different vendors into a single Sunrise incident.

### Mixed-vendor scenario within Microsoft Defender

The one case where `product_ref` varies within a single incident is **Microsoft Defender**, where the value is dynamic. A single Defender incident can contain alerts from different Microsoft products (e.g., "Microsoft Defender for Endpoint", "Microsoft Defender for Identity", "Microsoft Defender for Office 365"). These are all under the Microsoft umbrella but represent different detection products.

### Incident merging support

The data model does support **explicit merging** of incidents via:
- `merged_to_incident_id` — tracks when two Sunrise incidents are manually consolidated
- `source_redirected_id` — tracks when the vendor itself merges incidents on their side

This merging mechanism could produce an incident with alerts originating from different integrations, but it requires manual or rule-based action rather than automatic cross-vendor correlation.

---

## 4. Do you have an API the Agent could use to retrieve additional data for the AI analysis?

**Yes.** Sunrise exposes a comprehensive set of REST APIs across multiple services that an AI agent can use to retrieve data for analysis. Below are the most relevant endpoints grouped by use case.

### 4.1 Incident & Alert Data (Case Management Service)

**Base path**: `/case`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/v1/incident/{incident_id}` | Fetch full incident details |
| `POST` | `/v1/incident/find` | Search incidents by JSON query (paginated) |
| `GET` | `/v1/alert/{alert_id}` | Fetch full alert details |
| `POST` | `/v1/alert/find` | Search alerts by JSON query (paginated) |
| `GET` | `/v1/evidence/{evidence_id}` | Fetch evidence details |
| `POST` | `/v1/evidence/find` | Search evidence by JSON query (paginated) |
| `GET` | `/v1/observed-entity/{id}` | Fetch observed entity details |
| `POST` | `/v1/observed-entity/find` | Search observed entities (paginated) |
| `GET` | `/v1/cached-event/{event_id}` | Fetch cached event details |
| `POST` | `/v1/cached-event/find` | Search cached events (paginated) |
| `GET` | `/v1/case/{case_id}` | Fetch case details |
| `POST` | `/v1/case/find` | Search cases by JSON query (paginated) |

### 4.2 AI Notes (Case Management Service)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/v1/ai-note/case/{case_id}/create-ai-note` | Create AI analysis notes for a case |
| `GET` | `/v1/ai-note/{ai_note_id}` | Fetch existing AI note |
| `POST` | `/v1/ai-note/find` | Search AI notes (paginated) |

### 4.3 Deep Enrichment from Vendor APIs (Playbook/Connector Service)

These endpoints reach back into vendor systems for live, detailed data:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/enrich-incident` | Deep enrichment: endpoint details, evidence/artifacts, process chains, IOCs, network activity, user context |
| `POST` | `/incidents-alerts` | Fetch incidents and alerts by creation time (paginated, filterable) |
| `POST` | `/incidents-alerts-updates` | Fetch incidents and alerts by modification time (incremental sync) |
| `POST` | `/list-machines` | List enrolled endpoints with health status, risk score, OS, IP, tags |
| `POST` | `/get-machine-detail` | Detailed endpoint information for a single machine |

**Supported vendors for enrichment**: CrowdStrike, Microsoft Defender, SentinelOne, Cybereason, Cortex XDR, Cortex XSIAM, Carbon Black, QRadar, USM Anywhere

### 4.4 Entity Context (Entity Service)

**Base path**: `/entity`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/{customer_id}/{region}/host/{host_name}` | Fetch host entity details and relationships |
| `GET` | `/{customer_id}/{region}/user/{user_name}` | Fetch user entity details and relationships |
| `GET` | `/{customer_id}/{region}/query/{associated_field}/{field}/{value}` | Query entity associations |

### 4.5 Search Service

**Base path**: `/search`

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/v1/search/results/{search_id}/scroll` | Scroll through search results |
| `GET` | `/v1/search/results/{search_id}/status` | Get search execution status |
| `GET` | `/v1/search/data_dictionary` | Fetch data dictionary for field definitions |
| `GET` | `/v1/search/query/{search_id}` | Retrieve saved queries |

### 4.6 Response Actions (Playbook/Connector Service)

An AI agent with appropriate authorization could also trigger response actions:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/isolate` | Isolate endpoint from network |
| `POST` | `/unisolate` | Release endpoint from isolation |
| `POST` | `/kill-process` | Terminate a running process |
| `POST` | `/quarantine-file` | Quarantine a file |
| `POST` | `/run-script` | Execute a script or scan |
| `POST` | `/disable-user` | Disable a user account |
| `POST` | `/enable-user` | Enable a user account |
| `POST` | `/reset-user-password` | Reset user password |
| `POST` | `/revoke-user-sessions` | Revoke all user sessions |

### 4.7 Activity & Collaboration

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/v1/activity/find` | Search activity logs (paginated) |
| `GET` | `/{customer_id}/chat/{chat_id}/history` | Fetch investigation chat history |
| `GET` | `/{customer_id}/context` | Fetch customer context |

### 4.8 Metrics

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/metrics/query` | Instant metric query |
| `POST` | `/metrics/query-range` | Range metric query |

### Summary

The most valuable endpoints for an AI agent performing security analysis are:

1. **`/enrich-incident`** — provides the richest single-call context (endpoint details, process chains, IOCs, network activity, user context)
2. **`/v1/incident/find` + `/v1/alert/find` + `/v1/evidence/find`** — structured queries across the case data model
3. **Entity service** (`/host/{name}`, `/user/{name}`) — for affected system and user context
4. **Search service** — for ad-hoc queries across all indexed data
5. **`/v1/ai-note/find`** — to read prior AI analysis on the same case

All endpoints support pagination and JSON-based filtering, making them suitable for programmatic consumption by an AI agent.
