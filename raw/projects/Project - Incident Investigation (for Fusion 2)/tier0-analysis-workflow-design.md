# Tier 0 Analysis Workflow — Design & Assumptions

> **Purpose:** Documents the internal workflow design for the `tier_0_analysis` action within `sunrise-app-playbook`, including the Temporal activity sequence, file changes, data flow, and all assumptions made during planning.

---

## 1. Workflow Sequence

The `tier_0_analysis` action is a new branch inside the existing `ExecuteActionWorkflow`. It is triggered when `detail["action"] == "tier_0_analysis"`.

```
┌────────────────────────────────────────────────────────┐
│            ExecuteActionWorkflow.run()                 │
│          detail["action"] == "tier_0_analysis"         │
│                                                        │
│  try:                                                  │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  Activity 1: extract_incident_data       [sync + DB]   │
│  ────────────────────────────────────────────────────  │
│  Inputs:  customer_id, incident_id                     │
│  ────────────────────────────────────────────────────  │
│  • Uses IncidentController.get_by_id(incident_id)      │
│  • SQLAlchemy eager-loads related data:                │
│      incident.alerts[*]                                │
│        └─ alert.evidences[*]                           │
│      incident.evidences[*]                             │
│      incident.entities[*]                              │
│  • Serializes the full object graph to JSON-safe dict  │
│  • Extracts incident.case_id (needed in Step 4)        │
│  ────────────────────────────────────────────────────  │
│  Returns: { "incident_data": {...}, "case_id": "..." } │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  Activity 2: enqueue_ai_analysis         [sync + HTTP] │
│  ────────────────────────────────────────────────────  │
│  Inputs:  customer_id, incident_data                   │
│  ────────────────────────────────────────────────────  │
│  • Fetches credentials from credential store:          │
│      fetch_credentials_sync(platform="tier_0_analysis")│
│  • Extracts base_url and auth token from credentials   │
│  • HTTP POST → {base_url}/analyze                      │
│      Body: incident_data JSON                          │
│      Auth: Bearer token                                │
│  ────────────────────────────────────────────────────  │
│  Returns: { "request_id": "..." }                      │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
                ┌────────────────┐
                │   Poll Loop    │
                │  (in workflow) │
                └────────┬───────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  Activity 3: poll_ai_analysis            [sync + HTTP] │
│  ────────────────────────────────────────────────────  │
│  Inputs:  customer_id, request_id                      │
│  ────────────────────────────────────────────────────  │
│  • Fetches credentials (same pattern as Step 2)        │
│  • HTTP GET → {base_url}/status/{request_id}           │
│  ────────────────────────────────────────────────────  │
│  Returns: { "status": "...", "result": {...} | null }  │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
               ┌─────────────────┐
               │ status check    │
               ├─────────────────┤
               │ "completed"  ───┼──► continue to Step 4
               │ "failed"    ────┼──► raise ApplicationError (non_retryable)
               │ other       ────┼──► workflow.sleep(30s), re-poll
               │ max attempts ───┼──► raise ApplicationError (non_retryable)
               └─────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  Activity 4: store_ai_note               [sync + DB]   │
│  ────────────────────────────────────────────────────  │
│  Inputs:  customer_id, case_id, incident_id,           │
│           analysis_result                              │
│  ────────────────────────────────────────────────────  │
│  • Builds controllers via _build_controllers() pattern │
│  • Creates AINoteCreate:                               │
│      case_id     = case_id (from Step 1)               │
│      type        = "Summary"                           │
│      automated   = True                                │
│      response    = json.dumps(analysis_result)         │
│  • AINoteController.create_ai_note_no_commit(...)      │
│  ────────────────────────────────────────────────────  │
│  Returns: { "ai_note_id": "..." }                      │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
┌────────────────────────────────────────────────────────┐
│  (success) update_activity_result    [existing, async] │
│  ────────────────────────────────────────────────────  │
│  Inputs:  activity_id, dispatch_result                 │
│  ────────────────────────────────────────────────────  │
│  • POST → ACTIVITY_SERVICE_BASE_URL/activity/{id}      │
│  • Already exists in ExecuteActionActivity             │
│  ────────────────────────────────────────────────────  │
│  Returns: activity service response                    │
└────────────────────────┬───────────────────────────────┘
                         │
                         ▼
                  ┌──────────────┐
                  │   Workflow   │
                  │  completes   │
                  └──────────────┘

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─

  FAILURE PATH (any exception from steps 1–4):

  except Exception as exc:
      │
      ▼
  ┌──────────────────────────────────────────────────────┐
  │  Best-effort: update_activity_result                 │
  │  POST → ACTIVITY_SERVICE_BASE_URL/activity/{id}      │
  │  Body: { "status": "failed", "error": str(exc) }     │
  │  ──────────────────────────────────────────────────  │
  │  Wrapped in its own try/except:                      │
  │  • Success → error recorded in activity service      │
  │  • Failure → log warning, continue                   │
  └──────────────────────┬───────────────────────────────┘
                         │
                    raise exc  ← re-raise original
                         │
                         ▼
                  ┌──────────────┐
                  │   Workflow   │
                  │   FAILED     │
                  └──────────────┘
```

---

## 2. Data Flow

```
                Sunrise DB                Credential Store
                    │                            │
       ┌────────────┘                            │
       │ read incident +                         │
       │ alerts + evidence                       │
       │ + entities                              │
       ▼                                         │
  ┌───────────────┐    ┌─────────────┐           │
  │ incident_data │───►│  Tier 0 AI  │◄──────────┘
  │    (JSON)     │    │  Analysis   │  credentials for
  └───────────────┘    │   API       │  tier_0_analysis
                       └──────┬──────┘
                              │
                       request_id
                              │
                       ┌──────┴──────┐
                       │  poll loop  │
                       └──────┬──────┘
                              │
                       analysis result
                              │
                   ┌──────────┴──────────┐
                   ▼                     ▼
             ┌──────────┐        ┌──────────────┐
             │ AI Note  │        │   Activity   │
             │  (DB)    │        │   Service    │
             └──────────┘        └──────────────┘
```

---

## 3. Files to Create

| File | Purpose |
|------|---------|
| `tw/sunrise/app/playbook/temporal/activities/tier0_analysis_activity.py` | New activity class with 4 activities: `extract_incident_data`, `enqueue_ai_analysis`, `poll_ai_analysis`, `store_ai_note` |
| `tw/sunrise/app/playbook/temporal/payload/tier0_analysis.py` | Dataclass for workflow args (`Tier0AnalysisArgs`) |

## 4. Files to Modify

| File | Change |
|------|--------|
| `tw/sunrise/app/playbook/temporal/workflows/execute_action_workflow.py` | Add `tier_0_analysis` branch in `run()` with 5-step sequence |
| `tw/sunrise/app/playbook/connectors/models.py` | Add `Tier0AnalysisRequest` model, register in `ActionSpecificRequest` union and `_ACTION_REQUEST_CLASSES` |
| `tw/sunrise/app/playbook/config/config.py` | Add `TIER0_POLL_INTERVAL_SECONDS` and `TIER0_MAX_POLL_ATTEMPTS` settings |

---

## 5. Assumptions

### 5.1 Incident Data Source

| Assumption | Rationale |
|------------|-----------|
| Incident data is read from the **Sunrise DB**, not fetched live from the vendor API | User decision. The incident and its alerts/evidence have already been ingested by the `FetchIncidentsAndAlertsActivity` ingestion pipeline. Reading from DB avoids redundant vendor API calls, credential scope concerns, and latency. |
| The incident referenced by `incident_id` already exists in the DB at workflow execution time | The workflow is triggered after ingestion. If the incident doesn't exist, the `extract_incident_data` activity will fail with a not-found error. |
| SQLAlchemy eager-loading (`selectin`) on `Incident.alerts`, `Alert.evidences`, `Incident.evidences`, and `Incident.entities` will load the full object graph in a single `get_by_id` call | This matches the model definitions in `sunrise-model` which declare these relationships with `lazy="selectin"`. |

### 5.2 Credential Store

| Assumption | Rationale |
|------------|-----------|
| AI analysis credentials are stored under platform key **`tier_0_analysis`** | User decision. This is the key passed to `fetch_credentials_sync()`. |
| The credential record contains at minimum `base_url` (API root URL) and `token` (bearer token) | Standard pattern for the credential store. The `VendorCredentials` model already supports this shape. |
| The same credentials are used for both the submit and poll endpoints | Both endpoints live under the same `base_url` and use the same auth. |

### 5.3 AI Analysis API Contract

| Assumption | Rationale |
|------------|-----------|
| The API uses a **submit → poll** pattern (not synchronous or webhook-based) | User requirement: "enqueue the json... assume this will give us a request-id to be used for polling status." |
| Submit endpoint accepts the full incident JSON as the POST body | The entire incident graph (with alerts, evidence, entities) is sent in a single request. The API team may request filtering — see open questions. |
| Submit endpoint returns a `request_id` field in the response | User requirement. |
| Poll endpoint returns a `status` field; `"completed"` means done with a `result` object | Assumed based on standard async API patterns. Exact status values TBD with API team. |
| Poll endpoint returns `"failed"` status on analysis failure (not an HTTP error code) | Distinguishes "analysis failed" from "API is down" — the latter triggers Temporal retry. |

### 5.4 Polling Behavior

| Assumption | Default | Rationale |
|------------|---------|-----------|
| Poll interval is **30 seconds** | `TIER0_POLL_INTERVAL_SECONDS = 30` | Balance between responsiveness and API load. Configurable. |
| Max **60 poll attempts** before timeout | `TIER0_MAX_POLL_ATTEMPTS = 60` | ~30 minutes total with 30s interval. Security analysis should complete well within this window. |
| Polling is done via **Temporal workflow timer + activity calls**, not blocking inside an activity | — | Temporal best practice. A long-blocking activity would prevent heartbeat and obscure progress. The workflow timer is durable across worker restarts. |
| The workflow raises an error if max poll attempts exceeded | — | The activity service records the failure. Can be retried manually. |

### 5.5 AI Note Storage

| Assumption | Rationale |
|------------|-----------|
| The analysis result is stored as an `AINote` in the DB using **direct DB access via controllers** (not via HTTP endpoint) | User decision. Follows the `persist_enrichment_evidence` pattern in `FetchIncidentsAndAlertsActivity`. |
| The AI note is linked via `case_id` obtained from the incident record | `AINote.case_id` is a FK to `cases.id`. The incident's `case_id` is captured during the extraction step. |
| The AI note type is `"Summary"` (`AINoteType.SUMMARY`) | Most appropriate for an automated analysis summary. Can be changed to `"Report"` or `"Analyst Bot"` if preferred. |
| `automated = True` | This is a machine-initiated analysis, not an analyst-driven interaction. |
| The full analysis result is stored as `json.dumps(result)` in the `response` column | The `response` column is PostgreSQL `TEXT` with no size limit enforced. |
| `prompt` field is set to a descriptive string (e.g. `"Automated tier-0 analysis for incident {incident_id}"`) or left null | Optional — helps with traceability. |
| `session_id` is null | There is no chained analyst session — this is a one-shot automated analysis. |

### 5.6 Activity Class Design

| Assumption | Rationale |
|------------|-----------|
| All 4 new activities are **synchronous** | DB activities require `@with_sync_db_session` (sync only). HTTP activities use `httpx.Client` (sync) for consistency within the same class. |
| The activity class constructor takes `http_sync_session`, `config`, `sunrise_resource` | Matches `FetchIncidentsAndAlertsActivity` pattern. All three are available in the worker's `dependencies` dict, so auto-registration works without changes to `worker.py`. |
| No changes to `worker.py` or `temporal_bootstrap.py` are needed | The `import_temporal_objects()` scanner auto-discovers activity classes by walking the `temporal/activities/` directory and matching constructor params to the dependencies dict. |
| Activities in the new file will be automatically registered by the existing worker bootstrap | Verified by reading `temporal_bootstrap.py` — it scans all `.py` files in the activities package. |

### 5.7 Workflow Integration

| Assumption | Rationale |
|------------|-----------|
| The `tier_0_analysis` action is added as a new conditional branch in `ExecuteActionWorkflow.run()`, alongside the existing `enrich_incident` branch | User requirement: "use the existing workflow execute_action_workflow." |
| The `ExecuteActionArgs` dataclass is sufficient — `detail` dict carries `action`, `incident_id`, `vendor`, etc. | Existing pattern. The workflow reads `detail["action"]` and `detail["incident_id"]`. No new payload dataclass is strictly required, but we create `Tier0AnalysisArgs` for type clarity if a dedicated entry point is added later. |
| The existing `update_activity_result` activity (from `ExecuteActionActivity`) is reused for Step 5 | Already registered and used by the workflow for all action types. |
| The workflow uses `get_common_activity_config()` for all activity calls (same timeouts, retry policy) | Consistent with how the workflow handles other actions. The 10-minute start-to-close timeout is sufficient for individual activities (DB reads and HTTP calls). The polling loop itself is managed by the workflow, not constrained by a single activity timeout. |

### 5.8 Request Model

| Assumption | Rationale |
|------------|-----------|
| A new `Tier0AnalysisRequest` model extends `ActionRequest` with `action: Literal["tier_0_analysis"]` and `incident_id: str` | Follows the existing `ActionSpecificRequest` union pattern (e.g. `IsolateRequest`, `KillProcessRequest`). |
| `Tier0AnalysisRequest` is added to the `ActionSpecificRequest` union type and `_ACTION_REQUEST_CLASSES` map | Enables `build_action_request("tier_0_analysis", ...)` to work. |
| The `vendor` field on `Tier0AnalysisRequest` identifies the source vendor of the incident, not the AI analysis service | The vendor is informational — it tells the analysis service which vendor the data came from. Credentials for the AI service are fetched separately using platform `tier_0_analysis`. |

### 5.9 Error Handling

| Assumption | Rationale |
|------------|-----------|
| HTTP 4xx responses from the AI analysis API are non-retryable | Client errors (bad request, auth failure) won't succeed on retry. These match the existing `TEMPORAL_ACTIVITY_RETRY_NON_RETRYABLE_ERROR_TYPES` pattern. |
| HTTP 5xx and network errors trigger Temporal activity retry | Transient failures. Temporal's retry policy handles backoff (up to 8 attempts, 5s initial, 300s max interval). |
| If the analysis API returns `status: "failed"`, the workflow raises an `ApplicationError` | Distinguishes from infrastructure failures. The activity record is updated with the failure before the workflow exits. |
| If `extract_incident_data` fails because the incident doesn't exist, the workflow fails without retry | A missing incident is a data issue, not a transient error. |
| All exceptions from dispatch are caught by a workflow-level `try/except` | Ensures `update_activity_result` is called with `{"status": "failed", "error": ...}` before re-raising. The error-path recording is best-effort (wrapped in its own `try/except`) so it cannot mask the original error. |
| The error-path `update_activity_result` uses the standard activity retry policy | Up to 8 attempts with exponential backoff to maximize the chance of recording the failure. |

### 5.10 Security

| Assumption | Rationale |
|------------|-----------|
| Credentials never appear in Temporal workflow event history | Credentials are fetched inside activities (not passed as workflow args). This matches the existing security boundary in `ExecuteActionActivity._fetch_credentials()`. |
| The incident data sent to the AI analysis API may contain PII (usernames, IPs, hostnames) | The AI analysis service is an internal service within the trust boundary. If external, data sanitization would need to be added. |

---

## 6. Reused Components

| Component | Location | How it's reused |
|-----------|----------|-----------------|
| `fetch_credentials_sync()` | `temporal/shared_utils.py` | Fetch AI analysis credentials from credential store |
| `@with_sync_db_session` | `helper/decorator.py` | DB session management for sync activities |
| `get_common_activity_config()` | `helper/temporal_config.py` | Standard timeout/retry config for all activity calls |
| `ExecuteInRegion` | `sunrise-core` | Multi-region DB access wrapper |
| `UserDetails` + `RepositoryFactory` + `ServiceResources` | `sunrise-core` | Controller instantiation pattern |
| `IncidentController` | `sunrise-core` | Read incident from DB |
| `AINoteController` | `sunrise-core` | Create AI note in DB |
| `AINoteCreate` | `sunrise-core` | Pydantic request model for AI note creation |
| `AINoteType` | `sunrise-model` | Enum for AI note types (`Summary`) |
| `CaseType` | `sunrise-model` | Enum for case types (`INCIDENT`) |
| `update_activity_result` | `temporal/activities/execute_action_activity.py` | Existing activity to update activity service |
| `import_temporal_objects()` | `helper/temporal_bootstrap.py` | Auto-discovers and registers the new activity class |

---

## 7. Configuration Additions

Added to `config/config.py`:

| Setting | Type | Default | Description |
|---------|------|---------|-------------|
| `TIER0_POLL_INTERVAL_SECONDS` | `int` | `30` | Seconds between poll attempts in the workflow loop |
| `TIER0_MAX_POLL_ATTEMPTS` | `int` | `60` | Maximum number of poll attempts before the workflow times out |

---

## 8. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| Large incident payloads (>1 MB) may exceed AI API limits | Submit fails with 413 | Truncate evidence or negotiate max size with API team |
| AI analysis takes longer than 30 min | Workflow times out | Increase `TIER0_MAX_POLL_ATTEMPTS` or interval. Workflow failure is recorded; can be retried. |
| Credential store doesn't have `tier_0_analysis` entry for a customer | Activity fails on credential fetch | Fail fast with clear error. Requires ops setup before feature is used. |
| Incident has no alerts/evidence (edge case) | Analysis may be low quality | Send anyway — the AI service should handle sparse data gracefully |
| Concurrent tier_0_analysis workflows for the same incident | Duplicate AI notes created | Acceptable for now — idempotency can be added later with a check-before-create pattern |
| Worker restart during poll loop | — | No risk — Temporal replays the workflow from event history. The workflow timer is durable. `request_id` is stored in workflow state. |
