# Tier 0 Analysis — API Integration Design Document

> **Purpose:** This document describes how the `sunrise-app-playbook` service will integrate with the Tier 0 Analysis API. It is intended for the team that owns the analysis API so they can design and adjust their endpoints to work with the calling workflow.

---

## 1. Integration Overview

### What is calling the API?

A **Temporal workflow** (`ExecuteActionWorkflow`) running inside `sunrise-app-playbook`. The workflow is triggered when an analyst (or automation) requests AI-powered analysis of a security incident.

### Interaction pattern

The workflow uses a **submit → poll** pattern:

```
Playbook Workflow                        Tier 0 Analysis API
       │                                        │
       │  POST /analyze                         │
       │  (incident JSON payload)               │
       ├───────────────────────────────────────►│
       │                                        │
       │  { request_id: "..." }                 │
       │ ◄───────────────────────────────────── ┤
       │                                        │
       │         ┌─── wait interval ───┐        │
       │         │                     │        │
       │  GET /status/{request_id}     │        │
       ├───────────────────────────────────────►│
       │                                        │
       │  { status: "processing" }              │
       │ ◄───────────────────────────────────── ┤
       │         │                     │        │
       │         └─── wait interval ───┘        │
       │                                        │
       │  GET /status/{request_id}              │
       ├───────────────────────────────────────►│
       │                                        │
       │  { status: "completed", result: {...} }│
       │ ◄───────────────────────────────────── ┤
       │                                        │
```

### Caller behavior

| Parameter | Default | Notes |
|-----------|---------|-------|
| Poll interval | 30 seconds | Configurable via `TIER0_POLL_INTERVAL_SECONDS` |
| Max poll attempts | 60 | Configurable via `TIER0_MAX_POLL_ATTEMPTS` (~30 min with 30s interval) |
| HTTP timeout per request | 30 seconds | Per-call timeout, not total |
| Retry on transient failure | Yes | Temporal retries on 5xx / network errors (up to 8 attempts with exponential backoff) |
| Non-retryable errors | 400, 401, 403, 422 | Client errors fail immediately without retry |

---

## 2. Authentication

Credentials are fetched from the Sunrise credential store using platform key **`tier_0_analysis`**.

The workflow expects the credential record to contain at minimum:

| Field | Type | Description |
|-------|------|-------------|
| `base_url` | string | **Required.** Root URL of the analysis API (e.g. `https://tier0-analysis.internal.example.com/api/v1`) |
| `token` | string | Pre-shared bearer token for `Authorization: Bearer <token>` header |

The workflow will send every request with:

```
Authorization: Bearer <token>
Content-Type: application/json
Accept: application/json
```

> **Question for API team:** Is bearer token sufficient, or do you require OAuth2 client-credentials flow? The workflow supports both patterns. If OAuth2 is needed, we will also store `client_id`, `client_secret`, `token_url`, and `scope` in the credential record.

---

## 3. API Endpoint: Submit Analysis

### `POST {base_url}/analyze`

Submits an incident for AI analysis.

### Request body

The payload is a JSON object representing a complete incident with its associated alerts, evidence, and observed entities — all read from the Sunrise database.

```jsonc
{
  // ── Incident metadata ──────────────────────────────────
  "id": "INC-00098312",                          // Sunrise internal incident ID
  "customer_id": "cust_7f3a2b",                  // Sunrise customer identifier
  "case_id": "CSE-00042197",                      // Parent case ID in Sunrise
  "source_id": "inc_28374659",                    // Vendor's native incident ID
  "integration_name": "Acme Corp - Defender",     // Name of the credential/integration
  "status": "Active",                             // Sunrise normalized: Active | In Progress | Redirected | Resolved
  "severity": "High",                             // Sunrise normalized: Informational | Low | Medium | High | Critical
  "priority": "High",                             // Sunrise normalized: Low | Medium | High | Unknown
  "classification": null,                         // True Positive | False Positive | Benign | Unknown | null
  "determination": null,                          // Malware | Adv Persistent Threat | Phishing | Compromised Account | ... | null
  "description": "Multi-stage attack involving credential access and lateral movement",
  "analysis": null,                               // null until resolved by analyst/tier0
  "suggested_remediation": "Isolate affected endpoint, reset compromised credentials",
  "source_link": "https://security.microsoft.com/incidents/28374659",
  "source_status": "active",                      // Raw status string from vendor
  "source_assigned_to": "analyst@acme.com",
  "source_priority": "High",                      // Raw priority string from vendor

  // ── Timestamps (ISO 8601 UTC) ──────────────────────────
  "source_created_at": "2026-03-06T14:22:08.000Z",
  "source_updated_at": "2026-03-06T18:45:33.000Z",
  "ingested_at": "2026-03-06T14:25:11.000Z",
  "last_sync_at": "2026-03-06T18:50:02.000Z",
  "reopened_at": null,
  "closed_at": null,

  // ── Vendor-specific extras ─────────────────────────────
  "additional_details": {                         // JSONB — structure varies by vendor
    "tags": ["MITRE:TA0006", "MITRE:TA0008"],
    "assigned_group": "SOC-Tier1"
  },

  // ── Alerts ─────────────────────────────────────────────
  "alerts": [
    {
      "id": "ALR-00215478",
      "incident_id": "INC-00098312",
      "source_id": "da637920812812345_-123456789",
      "name": "Suspicious credential dumping activity",
      "description": "A process attempted to access LSASS memory, consistent with credential harvesting tools",
      "category": "CredentialAccess",             // MITRE tactic category
      "detection_method": "EDR",
      "detector_ref": "MDE.CredentialDumping",
      "product_ref": "Microsoft Defender for Endpoint",
      "mitre_tactics": ["CredentialAccess"],       // Array of MITRE tactic names
      "mitre_techniques": ["T1003.001"],           // Array of MITRE technique IDs
      "threat_name": "Mimikatz",
      "threat_family": "HackTool:Win32/Mimikatz",
      "source_recommendations": "Isolate the device, investigate the user account",
      "source_link": null,

      // Alert timestamps (ISO 8601 UTC)
      "source_created_at": "2026-03-06T14:22:08.000Z",
      "source_updated_at": "2026-03-06T14:22:08.000Z",
      "generated_at": "2026-03-06T14:20:55.000Z",
      "first_activity_at": "2026-03-06T14:18:30.000Z",
      "last_activity_at": "2026-03-06T14:20:50.000Z",
      "closed_at": null,

      "additional_details": null,

      // ── Evidence items for this alert ──────────────────
      "evidences": [
        {
          "id": "EVD-00412890",
          "incident_id": "INC-00098312",
          "alert_id": "ALR-00215478",
          "roles": ["attacker"],                  // Role of this evidence in the alert
          "role_details": null,                   // Optional expanded role descriptions
          "verdict": "Malicious",                 // Automated investigation verdict
          "remediation_status": "pending",
          "remediation_status_detail": null,
          "tags": ["credential-access", "lsass"],
          "detail": {                             // JSONB — structure depends on evidence_type
            "evidence_type": "process",
            "process_name": "mimikatz.exe",
            "process_id": 7284,
            "parent_process_name": "cmd.exe",
            "parent_process_id": 5120,
            "file_path": "C:\\Users\\jdoe\\AppData\\Local\\Temp\\mimikatz.exe",
            "file_hash_sha256": "a1b2c3d4e5f6...",
            "command_line": "mimikatz.exe \"privilege::debug\" \"sekurlsa::logonpasswords\"",
            "detection_status": "detected"
          }
        },
        {
          "id": "EVD-00412891",
          "incident_id": "INC-00098312",
          "alert_id": "ALR-00215478",
          "roles": ["contextual"],
          "role_details": null,
          "verdict": null,
          "remediation_status": null,
          "remediation_status_detail": null,
          "tags": ["endpoint"],
          "detail": {
            "evidence_type": "device",
            "device_name": "WORKSTATION-0451",
            "device_id": "abc123def456",
            "os_platform": "Windows11",
            "health_status": "Active",
            "risk_score": "High",
            "ip_address": "10.0.1.42",
            "logged_on_users": ["ACME\\jdoe"]
          }
        },
        {
          "id": "EVD-00412892",
          "incident_id": "INC-00098312",
          "alert_id": "ALR-00215478",
          "roles": ["target"],
          "role_details": null,
          "verdict": null,
          "remediation_status": null,
          "remediation_status_detail": null,
          "tags": null,
          "detail": {
            "evidence_type": "user",
            "user_account": {
              "account_name": "jdoe",
              "user_principal_name": "jdoe@acme.com",
              "domain_name": "ACME"
            }
          }
        }
      ]
    },
    {
      "id": "ALR-00215479",
      "incident_id": "INC-00098312",
      "source_id": "da637920812899999_-987654321",
      "name": "Lateral movement using stolen credentials",
      "description": "Anomalous SMB authentication from WORKSTATION-0451 to SERVER-DC01",
      "category": "LateralMovement",
      "detection_method": "EDR",
      "detector_ref": "MDE.LateralMovement",
      "product_ref": "Microsoft Defender for Endpoint",
      "mitre_tactics": ["LateralMovement"],
      "mitre_techniques": ["T1021.002"],
      "threat_name": null,
      "threat_family": null,
      "source_recommendations": "Verify the legitimacy of the SMB session",
      "source_link": null,
      "source_created_at": "2026-03-06T14:35:22.000Z",
      "source_updated_at": "2026-03-06T14:35:22.000Z",
      "generated_at": "2026-03-06T14:34:10.000Z",
      "first_activity_at": "2026-03-06T14:30:00.000Z",
      "last_activity_at": "2026-03-06T14:33:55.000Z",
      "closed_at": null,
      "additional_details": null,
      "evidences": [
        {
          "id": "EVD-00412893",
          "incident_id": "INC-00098312",
          "alert_id": "ALR-00215479",
          "roles": ["attacker"],
          "verdict": "Suspicious",
          "remediation_status": null,
          "remediation_status_detail": null,
          "tags": ["lateral-movement", "smb"],
          "detail": {
            "evidence_type": "network",
            "source_address": "10.0.1.42",
            "destination_address": "10.0.0.5",
            "destination_port": 445,
            "protocol": "SMB",
            "destination_device_name": "SERVER-DC01"
          }
        }
      ]
    }
  ],

  // ── Observed entities (incident-level) ─────────────────
  "entities": [
    {
      "id": "ENT-00078412",
      "incident_id": "INC-00098312",
      "type": "User",                             // User | Host
      "association": "Associated",                 // Associated | Targeted
      "name": "jdoe@acme.com",
      "alert_ids": ["ALR-00215478"],
      "detail": {
        "evidence_type": "user",
        "user_account": {
          "account_name": "jdoe",
          "user_principal_name": "jdoe@acme.com",
          "domain_name": "ACME"
        }
      }
    },
    {
      "id": "ENT-00078413",
      "incident_id": "INC-00098312",
      "type": "Host",
      "association": "Targeted",
      "name": "WORKSTATION-0451",
      "alert_ids": ["ALR-00215478", "ALR-00215479"],
      "detail": {
        "evidence_type": "device",
        "device_name": "WORKSTATION-0451",
        "ip_address": "10.0.1.42"
      }
    }
  ]
}
```

### Expected response — `202 Accepted`

```json
{
  "request_id": "uuid-or-opaque-string"
}
```

The `request_id` is used by the caller for all subsequent polling.

---

## 4. API Endpoint: Poll Status

### `GET {base_url}/status/{request_id}`

Returns the current processing status of a submitted analysis.

### Expected responses

**While processing — `200 OK`:**

```json
{
  "status": "processing"
}
```

> **Question for API team:** Are there other intermediate statuses (e.g. `queued`, `extracting`, `analyzing`)? The workflow only checks for `status == "completed"` and `status == "failed"` — all other values are treated as "still in progress, keep polling."

**On completion — `200 OK`:**

```json
{
  "status": "completed",
  "result": {
    // ... analysis output (see section 5 for storage constraints)
  }
}
```

**On failure — `200 OK`:**

```json
{
  "status": "failed",
  "error": "Human-readable error description"
}
```

> Using `200` with `status: "failed"` (rather than a 4xx/5xx) is preferred so the workflow can distinguish between "the analysis itself failed" vs. "the API is down" (which triggers Temporal retry).

---

## 5. Analysis Result — How It Will Be Stored

The contents of `result` from the completed poll response will be stored as an **AI Note** in the Sunrise database, linked to the incident's parent case.

### AI Note storage fields

| DB column | Value set by workflow | Constraint |
|-----------|----------------------|------------|
| `case_id` | Parent case of the incident | FK → `cases.id` (required) |
| `type` | `"Summary"` | One of: `Summary`, `Recommendation`, `Report`, `Analyst Bot` |
| `automated` | `true` | Boolean |
| `prompt` | Description of what was requested (optional) | TEXT, nullable |
| `response` | **`json.dumps(result)`** | TEXT, nullable — **this is where the full analysis output goes** |
| `s3_object` | null (unless result is very large) | TEXT, nullable |

### Implications for the API team

1. **The `result` object is stored as a JSON text blob.** There is no schema enforcement on its structure from the DB side. You are free to return whatever structure is most useful.

2. **The `response` column is PostgreSQL `TEXT`** — no hard size limit, but very large payloads (>1 MB) should be discussed. If analysis produces large artifacts (e.g. full PCAP references, detailed timeline), consider referencing them via URL rather than inlining.

3. **The result will be displayed in the Sunrise UI** as an AI Note on the case/incident. If you include structured sections, a consistent schema would help the UI render them. Suggested structure (not required):

```json
{
  "summary": "Brief natural-language summary of findings",
  "severity_assessment": "Critical | High | Medium | Low | Informational",
  "classification": "True Positive | False Positive | Benign | Undetermined",
  "determination": "Malware | Phishing | Compromised Account | ...",
  "confidence": 0.92,
  "findings": [
    {
      "title": "Credential harvesting via Mimikatz",
      "description": "...",
      "mitre_techniques": ["T1003.001"],
      "severity": "Critical",
      "affected_assets": ["WORKSTATION-0451", "jdoe@acme.com"]
    }
  ],
  "recommended_actions": [
    "Isolate WORKSTATION-0451 immediately",
    "Reset credentials for jdoe@acme.com",
    "Scan SERVER-DC01 for signs of compromise"
  ],
  "analysis_metadata": {
    "model_version": "1.2.0",
    "processing_time_seconds": 45,
    "tokens_used": 12500
  }
}
```

---

## 6. Data Reference — Field Glossary

### Incident fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Sunrise internal ID (format: `INC-XXXXXXXX`) |
| `customer_id` | string | Tenant/customer identifier |
| `case_id` | string | Parent case in Sunrise (format: `CSE-XXXXXXXX`) |
| `source_id` | string | Vendor's native incident identifier |
| `integration_name` | string | Name of the credential integration used to access the vendor |
| `status` | enum | `Active` \| `In Progress` \| `Redirected` \| `Resolved` |
| `severity` | enum | `Informational` \| `Low` \| `Medium` \| `High` \| `Critical` |
| `priority` | enum | `Low` \| `Medium` \| `High` \| `Unknown` |
| `classification` | string \| null | `True Positive` \| `False Positive` \| `Benign` \| `Unknown` |
| `determination` | string \| null | `Malware` \| `Adv Persistent Threat` \| `Phishing` \| `Compromised Account` \| `Multi Staged Attack` \| `Unwanted Software` \| `Security Personnel` \| `Security Testing` \| `Malicious User Activity` \| `Not Malicious` \| `Insufficient Data` \| `Confirmed Activity` \| `Business Application` \| `Other` \| `Unknown` |
| `description` | string \| null | Incident description |
| `analysis` | string \| null | Previous analysis text (null if unanalyzed) |
| `suggested_remediation` | string \| null | Remediation suggestions from vendor/intel |
| `source_link` | string \| null | Deep link to incident in vendor console |
| `additional_details` | object \| null | JSONB — vendor-specific extras, no fixed schema |

### Alert fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Sunrise internal ID (format: `ALR-XXXXXXXX`) |
| `source_id` | string | Vendor's native alert identifier |
| `name` | string | Alert title / display name |
| `description` | string \| null | Detailed alert description |
| `category` | string \| null | MITRE ATT&CK tactic category |
| `detection_method` | string \| null | How the alert was detected (e.g. `EDR`, `AV`) |
| `product_ref` | string \| null | Product that generated the alert |
| `mitre_tactics` | string[] \| null | MITRE ATT&CK tactic names |
| `mitre_techniques` | string[] \| null | MITRE ATT&CK technique IDs (e.g. `T1003.001`) |
| `threat_name` | string \| null | Specific threat/malware name |
| `threat_family` | string \| null | Threat family/category |
| `source_recommendations` | string \| null | Vendor's recommended remediation |
| `evidences` | Evidence[] | Evidence items associated with this alert |

### Evidence fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Sunrise internal ID (format: `EVD-XXXXXXXX`) |
| `alert_id` | string \| null | Alert this evidence belongs to |
| `roles` | string[] \| null | Role in the alert: `attacker`, `target`, `contextual`, etc. |
| `verdict` | string \| null | Automated investigation verdict: `Malicious`, `Suspicious`, `Clean`, etc. |
| `remediation_status` | string \| null | Current remediation status |
| `tags` | string[] \| null | Custom tags |
| `detail` | object \| null | JSONB — varies by `evidence_type` (see below) |

### Evidence `detail` — common `evidence_type` values

| `evidence_type` | Key fields in `detail` |
|-----------------|----------------------|
| `process` | `process_name`, `process_id`, `parent_process_name`, `parent_process_id`, `file_path`, `file_hash_sha256`, `command_line` |
| `file` | `file_name`, `file_path`, `file_hash_sha256`, `file_hash_sha1`, `file_hash_md5`, `file_size` |
| `device` | `device_name`, `device_id`, `os_platform`, `health_status`, `risk_score`, `ip_address`, `logged_on_users` |
| `user` | `user_account.account_name`, `user_account.user_principal_name`, `user_account.domain_name` |
| `network` | `source_address`, `destination_address`, `destination_port`, `protocol`, `url`, `domain` |
| `ip` | `ip_address`, `geo_location`, `asn` |
| `registry` | `registry_key`, `registry_value_name`, `registry_value_data` |

> **Note:** The `detail` field is a passthrough of vendor-normalized data. Its exact structure depends on the vendor (Defender, CrowdStrike, SentinelOne, etc.) and which evidence categories were populated during ingestion. Not all fields are guaranteed to be present.

### Observed Entity fields

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Sunrise internal ID (format: `ENT-XXXXXXXX`) |
| `type` | enum | `User` \| `Host` |
| `association` | enum | `Associated` \| `Targeted` |
| `name` | string | Display name of the entity |
| `alert_ids` | string[] \| null | Which alerts this entity is associated with |
| `detail` | object \| null | Same JSONB structure as evidence detail |

---

## 7. Supported Vendors

Incidents may originate from any of these vendor integrations. The `integration_name` field indicates which one.

| Vendor | Notes |
|--------|-------|
| Microsoft Defender for Endpoint | Most common. Rich evidence with process trees, device details |
| CrowdStrike Falcon | Detections as alerts. Evidence includes IOCs and process info |
| SentinelOne | Threats as incidents. Evidence includes process trees |
| Carbon Black (VMware) | Alerts with device and process context |
| Cybereason | MalOps as incidents. Evidence structure varies |
| Palo Alto Cortex XDR / XSIAM | Incidents with alert grouping |
| IBM QRadar | Offenses as incidents. AQL-based evidence |
| AT&T USM / AlienVault | Alarms as incidents |

The data is vendor-normalized before being sent, so field names are consistent. However, the depth and completeness of `additional_details` and evidence `detail` varies by vendor.

---

## 8. Error Handling Expectations

| Scenario | Expected API behavior | Workflow behavior |
|----------|----------------------|-------------------|
| Valid request accepted | `202` with `request_id` | Proceed to polling |
| Invalid/malformed payload | `400` with error message | Fail immediately (non-retryable) |
| Authentication failure | `401` or `403` | Fail immediately (non-retryable) |
| API server error | `500` / `502` / `503` | Retry with exponential backoff (up to 8 attempts) |
| Request ID not found on poll | `404` | Fail immediately |
| Analysis timed out on API side | `200` with `status: "failed"` | Workflow records failure, updates activity |
| Poll max attempts exceeded | N/A | Workflow times out after ~30 min, records timeout |

---

## 9. Payload Size Estimates

| Incident complexity | Approx. alerts | Approx. evidence items | Est. payload size |
|--------------------|----|------|-----------|
| Simple (single alert) | 1 | 2–5 | 5–15 KB |
| Typical | 3–8 | 10–30 | 30–80 KB |
| Complex (multi-stage attack) | 10–25 | 50–150 | 100–500 KB |
| Very large (correlated campaign) | 25–100+ | 200+ | 500 KB – 2 MB |

> **Question for API team:** Is there a max payload size your API can accept? If large incidents are a concern, we can truncate or paginate the evidence data, or send a reference ID and let you pull the data.

---

## 10. Open Questions for Discussion

1. **Endpoint paths** — Are `POST /analyze` and `GET /status/{request_id}` the actual paths, or will they differ?

2. **Authentication** — Bearer token or OAuth2 client-credentials?

3. **Payload filtering** — Should we send the full incident data every time, or do you want a subset? Should we add include/exclude flags (similar to our existing `EnrichIncidentRequest` model)?

4. **Result schema** — Will the `result` object follow a fixed schema, or is it free-form? A fixed schema helps with UI rendering.

5. **Status values** — What are all possible `status` values the poll endpoint can return?

6. **Callback/webhook alternative** — Would you prefer to support a webhook callback instead of (or in addition to) polling? The workflow can support either pattern.

7. **Rate limiting** — Any rate limits we should respect? Multiple incidents could be submitted concurrently.

8. **Idempotency** — If we submit the same incident twice (e.g. due to retry), should the API deduplicate, or return a new `request_id`?

9. **Large payload handling** — For very large incidents (>500 KB), should we truncate evidence, or is there a reference-based pull model?

10. **TTL / Expiry** — How long does a `request_id` remain valid for polling? If the workflow restarts after a crash, can it resume polling an old `request_id`?
