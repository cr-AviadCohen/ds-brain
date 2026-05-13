# Project - RCE-NG for Fusion 2.docx

our questions

LB syntax:

**Incidents** (correlations made how?) **->**

**Alerts** (created via a set of rules on top of the vendors alerts for one or more evidences) **->**

**Evidences** (Tier 1, suspicious by the vendor)

* Do you have an IDM solution? IDM is necessary for the quality of the AI analysis.
* Please describe and attach the Sunrize DB schema for:
  + Incident
  + Alert
  + Evidence
* How are the Incidents (correlations) being made?

What are they based on?

* In the example you shared with us in the api design file, both of the alerts had the value "Microsoft Defender for Endpoint" for "product\_ref" field.

Are there alerts based on a mix of alerts from different vendors?

* Do you have an API the Agent could use to retrieve additional data for the AI analysis?

request json example

{

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

```

response json example

questions we should answer

* Is bearer token sufficient, or do you require OAuth2 client-credentials flow? The workflow supports both patterns. If OAuth2 is needed, we will also store `client\_id`, `client\_secret`, `token\_url`, and `scope` in the credential record.
* Are there other intermediate statuses (e.g. `queued`, `extracting`, `analyzing`)? The workflow only checks for `status == "completed"` and `status == "failed"` — all other values are treated as "still in progress, keep polling."

open questions

1. \*\*Endpoint paths\*\* — Are `POST /analyze` and `GET /status/{request\_id}` the actual paths, or will they differ?

2. \*\*Authentication\*\* — Bearer token or OAuth2 client-credentials?

3. \*\*Payload filtering\*\* — Should we send the full incident data every time, or do you want a subset? Should we add include/exclude flags (similar to our existing `EnrichIncidentRequest` model)?

4. \*\*Result schema\*\* — Will the `result` object follow a fixed schema, or is it free-form? A fixed schema helps with UI rendering.

5. \*\*Status values\*\* — What are all possible `status` values the poll endpoint can return?

6. \*\*Callback/webhook alternative\*\* — Would you prefer to support a webhook callback instead of (or in addition to) polling? The workflow can support either pattern.

7. \*\*Rate limiting\*\* — Any rate limits we should respect? Multiple incidents could be submitted concurrently.

8. \*\*Idempotency\*\* — If we submit the same incident twice (e.g. due to retry), should the API deduplicate, or return a new `request\_id`?

9. \*\*Large payload handling\*\* — For very large incidents (>500 KB), should we truncate evidence, or is there a reference-based pull model?

10. \*\*TTL / Expiry\*\* — How long does a `request\_id` remain valid for polling? If the workflow restarts after a crash, can it resume polling an old `request\_id`?
