# tier0-analysis-api-design.docx

# Tier 0 Analysis — API Integration Design Document

**Purpose:** This document describes how the sunrise-app-playbook service will integrate with the Tier 0 Analysis API. It is intended for the team that owns the analysis API so they can design and adjust their endpoints to work with the calling workflow.

## 1. Integration Overview

### What is calling the API?

A **Temporal workflow** (ExecuteActionWorkflow) running inside sunrise-app-playbook. The workflow is triggered when an analyst (or automation) requests AI-powered analysis of a security incident.

### Interaction pattern

The workflow uses a **submit → poll** pattern:

Playbook Workflow Tier 0 Analysis API

│ │

│ POST /analyze │

│ (incident JSON payload) │

├───────────────────────────────────────►│

│ │

│ { request\_id: "..." } │

│ ◄───────────────────────────────────── ┤

│ │

│ ┌─── wait interval ───┐ │

│ │ │ │

│ GET /status/{request\_id} │ │

├───────────────────────────────────────►│

│ │

│ { status: "processing" } │

│ ◄───────────────────────────────────── ┤

│ │ │ │

│ └─── wait interval ───┘ │

│ │

│ GET /status/{request\_id} │

├───────────────────────────────────────►│

│ │

│ { status: "completed", result: {...} }│

│ ◄───────────────────────────────────── ┤

│ │

### Caller behavior

| **Parameter** | **Default** | **Notes** |
| --- | --- | --- |
| Poll interval | 30 seconds | Configurable via TIER0\_POLL\_INTERVAL\_SECONDS |
| Max poll attempts | 60 | Configurable via TIER0\_MAX\_POLL\_ATTEMPTS (~30 min with 30s interval) |
| HTTP timeout per request | 30 seconds | Per-call timeout, not total |
| Retry on transient failure | Yes | Temporal retries on 5xx / network errors (up to 8 attempts with exponential backoff) |
| Non-retryable errors | 400, 401, 403, 422 | Client errors fail immediately without retry |

## 2. Authentication

Credentials are fetched from the Sunrise credential store using platform key **tier\_0\_analysis**.

The workflow expects the credential record to contain at minimum:

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| base\_url | string | **Required.** Root URL of the analysis API (e.g. https://tier0-analysis.internal.example.com/api/v1) |
| token | string | Pre-shared bearer token for Authorization: Bearer <token> header |

The workflow will send every request with:

Authorization: Bearer <token>

Content-Type: application/json

Accept: application/json



**Question for API team:** Is bearer token sufficient, or do you require OAuth2 client-credentials flow? The workflow supports both patterns. If OAuth2 is needed, we will also store client\_id, client\_secret, token\_url, and scope in the credential record.

## 3. API Endpoint: Submit Analysis

### POST {base\_url}/analyze

Submits an incident for AI analysis.

### Request body

The payload is a JSON object representing a complete incident with its associated alerts, evidence, and observed entities — all read from the Sunrise database.

{

// ── Incident metadata ──────────────────────────────────

"id": "INC-00098312", // Sunrise internal incident ID

"customer\_id": "cust\_7f3a2b", // Sunrise customer identifier

"case\_id": "CSE-00042197", // Parent case ID in Sunrise

"source\_id": "inc\_28374659", // Vendor's native incident ID

"integration\_name": "Acme Corp - Defender", // Name of the credential/integration

"status": "Active", // Sunrise normalized: Active | In Progress | Redirected | Resolved

"severity": "High", // Sunrise normalized: Informational | Low | Medium | High | Critical

"priority": "High", // Sunrise normalized: Low | Medium | High | Unknown

"classification": null, // True Positive | False Positive | Benign | Unknown | null

"determination": null, // Malware | Adv Persistent Threat | Phishing | Compromised Account | ... | null

"description": "Multi-stage attack involving credential access and lateral movement",

"analysis": null, // null until resolved by analyst/tier0

"suggested\_remediation": "Isolate affected endpoint, reset compromised credentials",

"source\_link": "https://security.microsoft.com/incidents/28374659",

"source\_status": "active", // Raw status string from vendor

"source\_assigned\_to": "analyst@acme.com",

"source\_priority": "High", // Raw priority string from vendor

// ── Timestamps (ISO 8601 UTC) ──────────────────────────

"source\_created\_at": "2026-03-06T14:22:08.000Z",

"source\_updated\_at": "2026-03-06T18:45:33.000Z",

"ingested\_at": "2026-03-06T14:25:11.000Z",

"last\_sync\_at": "2026-03-06T18:50:02.000Z",

"reopened\_at": null,

"closed\_at": null,

// ── Vendor-specific extras ─────────────────────────────

"additional\_details": { // JSONB — structure varies by vendor

"tags": ["MITRE:TA0006", "MITRE:TA0008"],

"assigned\_group": "SOC-Tier1"

},

// ── Alerts ─────────────────────────────────────────────

"alerts": [

{

"id": "ALR-00215478",

"incident\_id": "INC-00098312",

"source\_id": "da637920812812345\_-123456789",

"name": "Suspicious credential dumping activity",

"description": "A process attempted to access LSASS memory, consistent with credential harvesting tools",

"category": "CredentialAccess", // MITRE tactic category

"detection\_method": "EDR",

"detector\_ref": "MDE.CredentialDumping",

"product\_ref": "Microsoft Defender for Endpoint",

"mitre\_tactics": ["CredentialAccess"], // Array of MITRE tactic names

"mitre\_techniques": ["T1003.001"], // Array of MITRE technique IDs

"threat\_name": "Mimikatz",

"threat\_family": "HackTool:Win32/Mimikatz",

"source\_recommendations": "Isolate the device, investigate the user account",

"source\_link": null,

// Alert timestamps (ISO 8601 UTC)

"source\_created\_at": "2026-03-06T14:22:08.000Z",

"source\_updated\_at": "2026-03-06T14:22:08.000Z",

"generated\_at": "2026-03-06T14:20:55.000Z",

"first\_activity\_at": "2026-03-06T14:18:30.000Z",

"last\_activity\_at": "2026-03-06T14:20:50.000Z",

"closed\_at": null,

"additional\_details": null,

// ── Evidence items for this alert ──────────────────

"evidences": [

{

"id": "EVD-00412890",

"incident\_id": "INC-00098312",

"alert\_id": "ALR-00215478",

"roles": ["attacker"], // Role of this evidence in the alert

"role\_details": null, // Optional expanded role descriptions

"verdict": "Malicious", // Automated investigation verdict

"remediation\_status": "pending",

"remediation\_status\_detail": null,

"tags": ["credential-access", "lsass"],

"detail": { // JSONB — structure depends on evidence\_type

"evidence\_type": "process",

"process\_name": "mimikatz.exe",

"process\_id": 7284,

"parent\_process\_name": "cmd.exe",

"parent\_process\_id": 5120,

"file\_path": "C:\\Users\\jdoe\\AppData\\Local\\Temp\\mimikatz.exe",

"file\_hash\_sha256": "a1b2c3d4e5f6...",

"command\_line": "mimikatz.exe \"privilege::debug\" \"sekurlsa::logonpasswords\"",

"detection\_status": "detected"

}

},

{

"id": "EVD-00412891",

"incident\_id": "INC-00098312",

"alert\_id": "ALR-00215478",

"roles": ["contextual"],

"role\_details": null,

"verdict": null,

"remediation\_status": null,

"remediation\_status\_detail": null,

"tags": ["endpoint"],

"detail": {

"evidence\_type": "device",

"device\_name": "WORKSTATION-0451",

"device\_id": "abc123def456",

"os\_platform": "Windows11",

"health\_status": "Active",

"risk\_score": "High",

"ip\_address": "10.0.1.42",

"logged\_on\_users": ["ACME\\jdoe"]

}

},

{

"id": "EVD-00412892",

"incident\_id": "INC-00098312",

"alert\_id": "ALR-00215478",

"roles": ["target"],

"role\_details": null,

"verdict": null,

"remediation\_status": null,

"remediation\_status\_detail": null,

"tags": null,

"detail": {

"evidence\_type": "user",

"user\_account": {

"account\_name": "jdoe",

"user\_principal\_name": "jdoe@acme.com",

"domain\_name": "ACME"

}

}

}

]

},

{

"id": "ALR-00215479",

"incident\_id": "INC-00098312",

"source\_id": "da637920812899999\_-987654321",

"name": "Lateral movement using stolen credentials",

"description": "Anomalous SMB authentication from WORKSTATION-0451 to SERVER-DC01",

"category": "LateralMovement",

"detection\_method": "EDR",

"detector\_ref": "MDE.LateralMovement",

"product\_ref": "Microsoft Defender for Endpoint",

"mitre\_tactics": ["LateralMovement"],

"mitre\_techniques": ["T1021.002"],

"threat\_name": null,

"threat\_family": null,

"source\_recommendations": "Verify the legitimacy of the SMB session",

"source\_link": null,

"source\_created\_at": "2026-03-06T14:35:22.000Z",

"source\_updated\_at": "2026-03-06T14:35:22.000Z",

"generated\_at": "2026-03-06T14:34:10.000Z",

"first\_activity\_at": "2026-03-06T14:30:00.000Z",

"last\_activity\_at": "2026-03-06T14:33:55.000Z",

"closed\_at": null,

"additional\_details": null,

"evidences": [

{

"id": "EVD-00412893",

"incident\_id": "INC-00098312",

"alert\_id": "ALR-00215479",

"roles": ["attacker"],

"verdict": "Suspicious",

"remediation\_status": null,

"remediation\_status\_detail": null,

"tags": ["lateral-movement", "smb"],

"detail": {

"evidence\_type": "network",

"source\_address": "10.0.1.42",

"destination\_address": "10.0.0.5",

"destination\_port": 445,

"protocol": "SMB",

"destination\_device\_name": "SERVER-DC01"

}

}

]

}

],

// ── Observed entities (incident-level) ─────────────────

"entities": [

{

"id": "ENT-00078412",

"incident\_id": "INC-00098312",

"type": "User", // User | Host

"association": "Associated", // Associated | Targeted

"name": "jdoe@acme.com",

"alert\_ids": ["ALR-00215478"],

"detail": {

"evidence\_type": "user",

"user\_account": {

"account\_name": "jdoe",

"user\_principal\_name": "jdoe@acme.com",

"domain\_name": "ACME"

}

}

},

{

"id": "ENT-00078413",

"incident\_id": "INC-00098312",

"type": "Host",

"association": "Targeted",

"name": "WORKSTATION-0451",

"alert\_ids": ["ALR-00215478", "ALR-00215479"],

"detail": {

"evidence\_type": "device",

"device\_name": "WORKSTATION-0451",

"ip\_address": "10.0.1.42"

}

}

]

}

### Expected response — 202 Accepted

{

"request\_id": "uuid-or-opaque-string"

}



The request\_id is used by the caller for all subsequent polling.

## 4. API Endpoint: Poll Status

### GET {base\_url}/status/{request\_id}

Returns the current processing status of a submitted analysis.

### Expected responses

**While processing — 200 OK:**

{

"status": "processing"

}



**Question for API team:** Are there other intermediate statuses (e.g. queued, extracting, analyzing)? The workflow only checks for status == "completed" and status == "failed" — all other values are treated as "still in progress, keep polling."

**On completion — 200 OK:**

{

"status": "completed",

"result": {

// ... analysis output (see section 5 for storage constraints)

}

}



**On failure — 200 OK:**

{

"status": "failed",

"error": "Human-readable error description"

}



Using 200 with status: "failed" (rather than a 4xx/5xx) is preferred so the workflow can distinguish between "the analysis itself failed" vs. "the API is down" (which triggers Temporal retry).

## 5. Analysis Result — How It Will Be Stored

The contents of result from the completed poll response will be stored as an **AI Note** in the Sunrise database, linked to the incident's parent case.

### AI Note storage fields

| **DB column** | **Value set by workflow** | **Constraint** |
| --- | --- | --- |
| case\_id | Parent case of the incident | FK → cases.id (required) |
| type | "Summary" | One of: Summary, Recommendation, Report, Analyst Bot |
| automated | true | Boolean |
| prompt | Description of what was requested (optional) | TEXT, nullable |
| response | **json.dumps(result)** | TEXT, nullable — **this is where the full analysis output goes** |
| s3\_object | null (unless result is very large) | TEXT, nullable |

### Implications for the API team

1. **The result object is stored as a JSON text blob.** There is no schema enforcement on its structure from the DB side. You are free to return whatever structure is most useful.
2. **The response column is PostgreSQL TEXT** — no hard size limit, but very large payloads (>1 MB) should be discussed. If analysis produces large artifacts (e.g. full PCAP references, detailed timeline), consider referencing them via URL rather than inlining.
3. **The result will be displayed in the Sunrise UI** as an AI Note on the case/incident. If you include structured sections, a consistent schema would help the UI render them. Suggested structure (not required):

{

"summary": "Brief natural-language summary of findings",

"severity\_assessment": "Critical | High | Medium | Low | Informational",

"classification": "True Positive | False Positive | Benign | Undetermined",

"determination": "Malware | Phishing | Compromised Account | ...",

"confidence": 0.92,

"findings": [

{

"title": "Credential harvesting via Mimikatz",

"description": "...",

"mitre\_techniques": ["T1003.001"],

"severity": "Critical",

"affected\_assets": ["WORKSTATION-0451", "jdoe@acme.com"]

}

],

"recommended\_actions": [

"Isolate WORKSTATION-0451 immediately",

"Reset credentials for jdoe@acme.com",

"Scan SERVER-DC01 for signs of compromise"

],

"analysis\_metadata": {

"model\_version": "1.2.0",

"processing\_time\_seconds": 45,

"tokens\_used": 12500

}

}



## 6. Data Reference — Field Glossary

### Incident fields

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| id | string | Sunrise internal ID (format: INC-XXXXXXXX) |
| customer\_id | string | Tenant/customer identifier |
| case\_id | string | Parent case in Sunrise (format: CSE-XXXXXXXX) |
| source\_id | string | Vendor's native incident identifier |
| integration\_name | string | Name of the credential integration used to access the vendor |
| status | enum | Active | In Progress | Redirected | Resolved |
| severity | enum | Informational | Low | Medium | High | Critical |
| priority | enum | Low | Medium | High | Unknown |
| classification | string | null | True Positive | False Positive | Benign | Unknown |
| determination | string | null | Malware | Adv Persistent Threat | Phishing | Compromised Account | Multi Staged Attack | Unwanted Software | Security Personnel | Security Testing | Malicious User Activity | Not Malicious | Insufficient Data | Confirmed Activity | Business Application | Other | Unknown |
| description | string | null | Incident description |
| analysis | string | null | Previous analysis text (null if unanalyzed) |
| suggested\_remediation | string | null | Remediation suggestions from vendor/intel |
| source\_link | string | null | Deep link to incident in vendor console |
| additional\_details | object | null | JSONB — vendor-specific extras, no fixed schema |

### Alert fields

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| id | string | Sunrise internal ID (format: ALR-XXXXXXXX) |
| source\_id | string | Vendor's native alert identifier |
| name | string | Alert title / display name |
| description | string | null | Detailed alert description |
| category | string | null | MITRE ATT&CK tactic category |
| detection\_method | string | null | How the alert was detected (e.g. EDR, AV) |
| product\_ref | string | null | Product that generated the alert |
| mitre\_tactics | string[] | null | MITRE ATT&CK tactic names |
| mitre\_techniques | string[] | null | MITRE ATT&CK technique IDs (e.g. T1003.001) |
| threat\_name | string | null | Specific threat/malware name |
| threat\_family | string | null | Threat family/category |
| source\_recommendations | string | null | Vendor's recommended remediation |
| evidences | Evidence[] | Evidence items associated with this alert |

### Evidence fields

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| id | string | Sunrise internal ID (format: EVD-XXXXXXXX) |
| alert\_id | string | null | Alert this evidence belongs to |
| roles | string[] | null | Role in the alert: attacker, target, contextual, etc. |
| verdict | string | null | Automated investigation verdict: Malicious, Suspicious, Clean, etc. |
| remediation\_status | string | null | Current remediation status |
| tags | string[] | null | Custom tags |
| detail | object | null | JSONB — varies by evidence\_type (see below) |

### Evidence detail — common evidence\_type values

| **evidence\_type** | **Key fields in detail** |
| --- | --- |
| process | process\_name, process\_id, parent\_process\_name, parent\_process\_id, file\_path, file\_hash\_sha256, command\_line |
| file | file\_name, file\_path, file\_hash\_sha256, file\_hash\_sha1, file\_hash\_md5, file\_size |
| device | device\_name, device\_id, os\_platform, health\_status, risk\_score, ip\_address, logged\_on\_users |
| user | user\_account.account\_name, user\_account.user\_principal\_name, user\_account.domain\_name |
| network | source\_address, destination\_address, destination\_port, protocol, url, domain |
| ip | ip\_address, geo\_location, asn |
| registry | registry\_key, registry\_value\_name, registry\_value\_data |

**Note:** The detail field is a passthrough of vendor-normalized data. Its exact structure depends on the vendor (Defender, CrowdStrike, SentinelOne, etc.) and which evidence categories were populated during ingestion. Not all fields are guaranteed to be present.

### Observed Entity fields

| **Field** | **Type** | **Description** |
| --- | --- | --- |
| id | string | Sunrise internal ID (format: ENT-XXXXXXXX) |
| type | enum | User | Host |
| association | enum | Associated | Targeted |
| name | string | Display name of the entity |
| alert\_ids | string[] | null | Which alerts this entity is associated with |
| detail | object | null | Same JSONB structure as evidence detail |

## 7. Supported Vendors

Incidents may originate from any of these vendor integrations. The integration\_name field indicates which one.

| **Vendor** | **Notes** |
| --- | --- |
| Microsoft Defender for Endpoint | Most common. Rich evidence with process trees, device details |
| CrowdStrike Falcon | Detections as alerts. Evidence includes IOCs and process info |
| SentinelOne | Threats as incidents. Evidence includes process trees |
| Carbon Black (VMware) | Alerts with device and process context |
| Cybereason | MalOps as incidents. Evidence structure varies |
| Palo Alto Cortex XDR / XSIAM | Incidents with alert grouping |
| IBM QRadar | Offenses as incidents. AQL-based evidence |
| AT&T USM / AlienVault | Alarms as incidents |

The data is vendor-normalized before being sent, so field names are consistent. However, the depth and completeness of additional\_details and evidence detail varies by vendor.

## 8. Error Handling Expectations

| **Scenario** | **Expected API behavior** | **Workflow behavior** |
| --- | --- | --- |
| Valid request accepted | 202 with request\_id | Proceed to polling |
| Invalid/malformed payload | 400 with error message | Fail immediately (non-retryable) |
| Authentication failure | 401 or 403 | Fail immediately (non-retryable) |
| API server error | 500 / 502 / 503 | Retry with exponential backoff (up to 8 attempts) |
| Request ID not found on poll | 404 | Fail immediately |
| Analysis timed out on API side | 200 with status: "failed" | Workflow records failure, updates activity |
| Poll max attempts exceeded | N/A | Workflow times out after ~30 min, records timeout |

## 9. Payload Size Estimates

| **Incident complexity** | **Approx. alerts** | **Approx. evidence items** | **Est. payload size** |
| --- | --- | --- | --- |
| Simple (single alert) | 1 | 2–5 | 5–15 KB |
| Typical | 3–8 | 10–30 | 30–80 KB |
| Complex (multi-stage attack) | 10–25 | 50–150 | 100–500 KB |
| Very large (correlated campaign) | 25–100+ | 200+ | 500 KB – 2 MB |

**Question for API team:** Is there a max payload size your API can accept? If large incidents are a concern, we can truncate or paginate the evidence data, or send a reference ID and let you pull the data.

## 10. Open Questions for Discussion

1. **Endpoint paths** — Are POST /analyze and GET /status/{request\_id} the actual paths, or will they differ?
2. **Authentication** — Bearer token or OAuth2 client-credentials?
3. **Payload filtering** — Should we send the full incident data every time, or do you want a subset? Should we add include/exclude flags (similar to our existing EnrichIncidentRequest model)?
4. **Result schema** — Will the result object follow a fixed schema, or is it free-form? A fixed schema helps with UI rendering.
5. **Status values** — What are all possible status values the poll endpoint can return?
6. **Callback/webhook alternative** — Would you prefer to support a webhook callback instead of (or in addition to) polling? The workflow can support either pattern.
7. **Rate limiting** — Any rate limits we should respect? Multiple incidents could be submitted concurrently.
8. **Idempotency** — If we submit the same incident twice (e.g. due to retry), should the API deduplicate, or return a new request\_id?
9. **Large payload handling** — For very large incidents (>500 KB), should we truncate evidence, or is there a reference-based pull model?
10. **TTL / Expiry** — How long does a request\_id remain valid for polling? If the workflow restarts after a crash, can it resume polling an old request\_id?
