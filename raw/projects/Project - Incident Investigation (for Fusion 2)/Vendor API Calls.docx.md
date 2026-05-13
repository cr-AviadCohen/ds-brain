# Vendor API Calls.docx

**Vendor API Calls & Capability Matrix**

| **Vendor** | **API Calls for Enrichment** | **Processes** | **IOCs** | **Network** | **Timeline** | **Users** |
| --- | --- | --- | --- | --- | --- | --- |
| **CrowdStrike** | POST /incidents/entities/incidents/GET/v1 + POST /alerts/entities/alerts/v2 + POST /devices/entities/devices/v2 | behaviors[].process\_name, command\_line, parent\_details | behaviors[].sha256, device IPs | Limited | Behavior timestamps | behaviors[].user\_name |
| **Defender** | GET /security/incidents/{id} + GET /security/alerts\_v2 (evidence[] embedded) + GET /api/machines/{id} | processEvidence: processId, commandLine, imageFile | fileEvidence.sha256, ipEvidence, urlEvidence | ipEvidence with countryCode | Alert activity timestamps | userEvidence.userAccount |
| **Carbon Black** | POST /api/alerts/v7/.../alerts/\_search + observation search | process\_name, process\_sha256, parent\_name, cmdline | process\_sha256 | Observation netconn\_\* | Alert timestamps | device\_username |
| **SentinelOne** | GET /threats?ids={id} + GET /threats/{id}/timeline + GET /agents?ids={id} | threatInfo.processName, filePath | sha256, sha1, md5, indicators[] | Limited | **/timeline endpoint (richest)** | agent lastLoggedInUserName |
| **Cortex XDR** | POST /public\_api/v1/incidents/get\_incident\_extra\_data **(single call, richest)** | key\_artifacts[].process | file\_artifacts[] SHA-256, network\_artifacts[] IPs/domains | network\_artifacts[] with ports/protocols | Alert detection\_timestamp | Alert user fields |
| **Cortex XSIAM** | POST /incidents/get\_incidents + POST /alerts/get\_alerts\_multi\_events | Event-level process data | Event-level hashes, IPs | Event-level network data | Event timestamps | Event user fields |
| **QRadar** | GET /siem/offenses/{id} + resolve source\_address\_ids + dest\_address\_ids + optional AQL | No (SIEM) | Source/dest IPs | Yes (src/dst pairs) | AQL events (expensive) | offense\_source |
| **Cybereason** | POST /rest/crimes/unified with malopGuid | rootCauseElements[] | Element hashes, IPs | Connection elements | Element timestamps | User elements |
| **USM** | GET /investigations/{uuid} with embedded alarms | No (SIEM) | Event source/dest | Event src/dst addresses | Alarm timestamps | Event fields |
