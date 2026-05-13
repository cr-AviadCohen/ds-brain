# AI Assistant - Agent - UI.xlsx

## Routers
| Tool | key | page | url\_template | permissions | version | page\_explanation | notes | Navigation Prompt | WORKED |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| UI\_Tool\_EPP\_Overview | epp\_overview | EPP Overview | /#/EPP-overview | NaN | NaN | Central dashboard summarizing detections MalOps affected users/hosts and key metrics. Visual widgets show MalOps by status severity MITRE tactics resolution trends IOCs and machine status. | Filters available:- Time range (Last 24h 7d 30d custom)- Detection Engines- OS Type. Export option provided. see on EPP Overview sheet | Display all MalOps statistics and key metrics in the environment | V |
| UI\_Tool\_MalOp\_Management | malop\_managemant | MalOps Management | /#/malop-management?time=AllTime-from:-7200000,to:1757365199233 | NaN | NaN | Displays all malops detected in the environment. | NaN | List all security incidents and malops detected in the environment | V |
| UI\_Tool\_Malware\_Alerts | malware\_alerts | Malware Alerts | /#/malware/feed | NaN | NaN | Displays all malware alerts detected in the environment. Lists files flagged as malware affected machines detection time and status. | Tabs: All Known Unknown Fileless App Control. Filters: Status (All/Detected/etc.) Sort (All time / Recent). Export: CSV export option available. | Find all malware alerts and flagged files in the environment | V |
| UI\_Tool\_Security\_Mobile\_Policy | security\_mobile\_policy | Mobile Security Policy | /#/security-profile/mobile-policy | NaN | NaN | Manages mobile security policy for devices. Provides links to Cybereason Mobile resources. | Mostly informational with link to "The Nest" for mobile details. | Configure the mobile security policy settings | V |
| UI\_Tool\_Security\_Reputations | security\_reputations | Reputations | /#/security-profile/reputations-list | NaN | NaN | Manage custom and global reputation lists for files/domains. Allows adding items uploading CSV and searching. | Tabs: Custom Reputation List Global Reputation Search. Buttons: Add Item Upload CSV Download Template. | Manage all file and domain reputation lists | V |
| UI\_Tool\_Security\_Reputations\_Search | security\_reputations\_search | Reputations search | /#/security-profile/reputations-search | NaN | NaN | Search for the reputation of a File hash, Domain or IP address that was previously uploaded, or manually marked. | NaN | Look up reputation status for specific file hashes, domains, or IP addresses | V |
| UI\_Tool\_Security\_Behavior\_Allow | security\_behavior\_allow | Behavioral Allowlisting | /#/security-profile/behavioral-allowlist | NaN | NaN | Create rules that prevent MalOps from being triggered under specific behaviors. | Tabs: Enabled Disabled Archived. Option to create new rules. | Create behavioral allowlisting rules to prevent false positives | V |
| UI\_Tool\_Security\_Custom\_Rules | security\_custom\_rules | Custom Detection Rules | /#/security-profile/custom-detection-rules | NaN | NaN | Create and manage custom detection rules with user-defined logic. | Option to add new rules. | Set up custom detection rules and logic | V |
| UI\_Tool\_Security\_Isolation\_Ex | security\_isolation\_ex | Machine Isolation Exceptions | /#/security-profile/machine-isolation | NaN | NaN | Manage exceptions for isolated machines (allowing communication by IP or port). | Search by IP/Range add exception export CSV. Columns: IP/Range Port(s) Direction Last Updated Last Updated By. | Configure communication exceptions for isolated machines | V |
| UI\_Tool\_Device\_Control | device\_control | Device Control | /#/device-control | NaN | NaN | Manage and monitor external device usage and control policies. | Filters: Time range (e.g. Last 7 days). Export option available. | Monitor external device usage and control policies | V |
| UI\_Tool\_System\_Dashboard | system\_dashboard | System – Dashboard | /#/system/dashboard | System Admin | NaN | Overview of sensors and machines by status OS type and version. | Widgets: Sensor status activity trend OS versions. | Check sensor deployment status and system health metrics | V |
| UI\_Tool\_System\_Overview | system\_overview | System – Overview | /#/system | System Admin | NaN | General system overview including server details services and sensor status. | Displays sensor status last restart/update and service health (Data Threat intel). | View general system health and service status | V |
| UI\_Tool\_System\_Sensors | system\_sensors | System – Sensors | /#/system/sensors | System Admin | NaN | Lists all deployed sensors with detailed attributes and filters. | Filters: Sensor status Data collection OS Outdated/Updated App Control mode Anti-Ransomware mode. Columns: Machine FQDN Sensor version Last seen etc. | List all deployed sensors with their detailed status | V |
| UI\_Tool\_System\_Sensor\_Actions | system\_sensor\_actions | System – Sensor Actions | /#/system/sensor-actions | System Admin | NaN | Displays logs of sensor actions performed on machines. | Columns: Action Status Action Type Machine Name Error Error Message Warning IP Initiated At. | Review the history of sensor actions and activities | V |
| UI\_Tool\_System\_Policies | system\_policies | System – Policies Management | /#/system/policies | System Admin | NaN | Manage and configure sensor policies. | Create/Edit policies. Includes Default and Legacy policies. | Configure sensor policies and settings | V |
| UI\_Tool\_System\_Servers | system\_servers | System – Detection Servers | /#/system/servers | System Admin | NaN | Manage detection servers and sites. | Options: Add detection server Manage sites. Shows server info: name IP port sensors. | Manage detection servers and infrastructure | V |
| UI\_Tool\_System\_Groups | system\_groups | System – Groups | /#/system/groups | System Admin | NaN | Manage sensor assignment groups (automatic and manual). | Allows creating groups shows group name sensors assignment logic creation time. | Organize sensors into groups and assignments | V |
| UI\_Tool\_Users\_Mgmt | users\_mgmt | Users Management | /#/u/users?roles={roles}&sort={} | User Admin | NaN | Manage user accounts roles and permissions. | Lists users roles TFA status notifications. Filters by role (analyst/admin). | Set up user accounts, roles, and permissions | V |
| UI\_Tool\_Settings | settings | Settings | /#/settings | System Admin | NaN | Configure system-wide settings like registration SMTP authentication password policy and notifications. | Tabs: Registration Service SMTP server Notification Authentication Password Policy Stale & Archived Sensors. | Configure system-wide settings and parameters | V |
| UI\_Tool\_MalOp\_Details | malop\_details | MalOp Details | /#/malop/{malop\_guid} | NaN | NaN | Detailed view of individual MalOp showing attack progression evidence and affected elements. | Tabs: Overview Process Tree Evidence Affected Elements. Actions: Remediate Isolate Export. | Open detailed information about this specific security incident AAAA07t0p4ZsnYnS | V |
| UI\_Tool\_Detection\_MalOp\_Details | detection\_malop\_details | Detection MalOp Details | /#/detection-malop/{malop\_guid} | NaN | NaN | Detailed view of individual detection MalOp showing attack progression evidence and affected elements. | Tabs: Overview Process Tree Evidence Affected Elements. Actions: Remediate Isolate Export. | View detailed information about this detection-based security incident AAAA1gXqeBBIcCso | V |
| UI\_Tool\_Reports\_Dashboard | reports\_dashboard | Reports Dashboard | /#/reports | NaN | NaN | Executive and operational reporting interface. | Pre-built reports custom report builder scheduled reports dashboard widgets. | Generate executive reports and operational metrics | V |
| UI\_Tool\_IR\_Tools | ir\_tools | \nIR Tools | /#/dfir | Responder L2 | 21.2.221 and later. | Manage Incident Response and Forensic Data Ingestion Tools | NaN | i want to see all the ir tools | V |
| UI\_Tool\_Vulnerability\_Management | vulnerability\_management | vulnerability management | #/vulnerability-management | NaN | 24.1.380 | With the Vulnerability Management API, you can retrieve details on vulnerabilities on machines or applications found on machines in your environment. | NaN | view  vulnerabilities on machines | V |
| UI\_Tool\_File\_Search | file\_search | file search | #/fileSearch/ | Responder L1/L2 or Local Responder | NaN | \nPerforms a search request for a specific file on the file systems of machines in your organizations with sensors installed. You can search all directories on a specific machine, specific folders, or use YARA rules to find a specific file. | NaN | search request for a specific file on the file systems | V |

## investigation screen
| elements bubbles options fields: | {object}.investigation.VisualQuery.configurationModel | Unnamed: 2 |
| --- | --- | --- |
| elements filter: | {object}.investigation.GridFilters.configurationModel | NaN |
| NaN | NaN | NaN |
| NaN | NaN | NaN |
| filters | urls examples | NaN |
| maches word | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:)nn%22 | NaN |
| contains | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:@nn%22 | NaN |
| is | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:%3Dnn%22 | NaN |
| doesnt match word | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:\_nn%22 | NaN |
| doesnt contain | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:!nn%22 | NaN |
| is not | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:%2Bnn%22 | NaN |
| or in the condition | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22elementDisplayName:)22%7C21%22 | NaN |
| NaN | NaN | NaN |
| equal | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3D8%22 | NaN |
| doesnt equal | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%2B8%22 | NaN |
| less than | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3C8%22 | NaN |
| grater than | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3E8%22 | NaN |
| is between | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:-8%7CNaN%22 | NaN |
| NaN | NaN | NaN |
| bytes | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3D8%22 | NaN |
| KB | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3D8000%22 | NaN |
| MB | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3D8000000%22 | NaN |
| GB | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22totalDiskSpace:%3D8000000000%22 | NaN |
| NaN | NaN | NaN |
| True | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22vulnerableIosEvidence:true%22 | NaN |
| False | https://eli-sal.cybereason.net/#/s/search?queryString=0%3C-Machine%22vulnerableIosEvidence:false%22 | NaN |
| NaN | NaN | NaN |
| NaN | NaN | NaN |
| question | worked? | link |
| i want to see all the processes fron the last month that associated with the machine that the name contains bb or gg | V | https://eli-sal.cybereason.net/#/s/search?queryString=1%3C-@1755426634428-1758018634428@Process-%3EownerMachine%22elementDisplayName:@bb%7Cgg%22 |

## EPP Overview
| page | fillters | parameters | link | explaintaions | notes |
| --- | --- | --- | --- | --- | --- |
| EPP Overview | time range | (Last 24 hours, Last week, Last 30 days, Last 3 month, Last year, All Time) | /#/EPP-overview | filters the dashboard according spesific time range | the url doesnt cahnge |
| NaN | Select Detection Engines | (AI Hunting , AI-based Anti-Malware, Application Control, Behavioral execution prevention, Fileless Protection, Mobile, Sensor Tampering protection, Variant File Prevention, Variant Payload P,rotection, Anti Malware, Behavioral Document Protection, Anti Ransomware, Exploit Protection) | /#/EPP-overview | filters the dashboard according the selected detection engines | the url doesnt cahnge |
| NaN | Select OS Type | (Windows, MacOS, Linux) | /#/EPP-overview | filters the dashboard according the selected os type | the url doesnt cahnge |

## malop management
| page | fillters | parameters | link | explaintaions | notes | Specific MalOp Management Navigation Prompts | worked? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MalOps Management | Time Range | All Time, Last 3 Months, Last Month, Last Week, Last 24 Hours, Custom Range | /#/malop-management?time=LastThreeMonths&from:1749330000000&to:1757365199569 | Filters MalOps by detection time period | Custom ranges use Unix timestamps. Affects performance with large time spans | Filter MalOps to show only "Last 24 Hours" time range | V |
| MalOps Management | Investigation Status | New, Re-opened, Under Investigation, On Hold, Closed, Escalated | /#/malop-management?filter=malop-investigationStatus:Pending,Reopened,UnderInvestigation,OnHold,Closed,TODO | Filters MalOps by investigation workflow status | New status indicates MalOps requiring initial analysis | Filter MalOps to show only "New" investigation status | V |
| MalOps Management | State | Active, Inactive, Resolved, Excluded | /#/malop-management?filter=malop-status:Active,Remediated,Closed,Excluded | Filters MalOps by current state | Active MalOps require immediate attention and response | Filter MalOps to show only "Active" state | V |
| MalOps Management | Detection Engine | AI Hunting, Anti-Malware, AI-based Anti-Malware, Fileless Protection, Anti-Ransomware, Behavioral Document Protection, Mobile, Exploit Protection, Application Control, Behavioral Execution Prevention, Variant Payload Prevention, Variant File Prevention, Sensor Tampering Protection | /#/malop-management?time=AllTime-from:-7200000,to:1757365199562&filter=malop-detectionEngines:EDR,AntiVirus,StaticAnalysis,Script,Ransomware,Document,Mobile,AntiExploit,ApplicationControl,RulesEngine,VariantPayloadProtection,VariantFileProtection,TamperingProtection | Filters MalOps by the detection engine that triggered the alert | Shows which protection mechanism detected the threat | Filter MalOps to show only "AI Hunting" detection engine | V |
| MalOps Management | Priority | High, Medium, Low | /#/malop-management?filter=malop-priority:HIGH,MEDIUM,LOW | Filters MalOps by priority level | High priority MalOps should be addressed first in incident response | Filter MalOps to show only "High" priority | V |
| MalOps Management | Protection Type | Detected, Prevented, Quarantined, Disinfected, Failed, Failed to quarantine, Failed to prevent, Deleting on restart, Mitigated | /#/malop-management?time=AllTime-from:-7200000,to:1757365199680&filter=malop-decisionStatuses:dds\_detected,dds\_prevented,dds\_qurantined,dds\_disinfected,dds\_failure,dds\_failed\_to\_quarantine,dds\_failed\_to\_prevent,dds\_delete\_after\_reboot,dds\_mitigated | Filters MalOps by protection action taken | Shows effectiveness of automated response measures | Filter MalOps to show only "Prevented" protection type | V |
| MalOps Management | MITRE Tactic | Collection, Command and Control, Credential Access, Defense Evasion, Discovery, Execution, Exfiltration, Impact, Initial Access, Lateral Movement, Persistence, Privilege Escalation, Reconnaissance, Resource Development | /#/malop-management?time=AllTime-from:-7200000,to:1757365199764&filter=malop-mitreTactics:Collection,Command%20and%20Control,Credential%20Access,Defense%20Evasion,Discovery,Execution,Exfiltration,Impact,Initial%20Access,Lateral%20Movement,Persistence,Privilege%20Escalation,Reconnaissance,Resource%20Development | Filters MalOps by MITRE ATT&CK framework tactic | Maps incidents to standardized attack lifecycle phases | Filter MalOps to show only "Command and Control" MITRE tactic | V |
| MalOps Management | IoC Type | File, Process, Module, Domain Name, IP Address, User | /#/malop-management?time=AllTime-from:-7200000,to:1757365199636&filter=malop-iocs:File,Process,Module,DomainName,IpAddress,User | Filters MalOps by type of Indicator of Compromise | Identifies the primary IoC category for investigation focus | Filter MalOps to show only "File" IoC type | V |
| MalOps Management | Detection Type | Exclude PUP (Potentially Unwanted Program) | /#/malop-management?time=AllTime-from:-7200000,to:1757365199167&filter=malop-detectionType:pup | Excludes potentially unwanted programs from results | Filters out low-priority software detections to focus on threats | Exclude "PUP" from MalOps detection type | V |
| MalOps Management | MalOp Type | EDR (Endpoint Detection and Response), NGAV (Next-Generation Antivirus) | /#/malop-management?time=AllTime-from:-7200000,to:1757365199123&filter=malop-type:EDR,EPP | Filters MalOps by detection technology type | Distinguishes between behavior-based (EDR) and signature-based (NGAV) detections | Filter MalOps to show only "EDR" MalOp type | V |
| MalOps Management | Severity | High, Medium, Low | /#/malop-management?filter=malop-severity:High,Medium,Low | Filters MalOps by threat severity level | High severity indicates critical threats requiring immediate response | Filter MalOps to show only "High" severity | V |
| MalOps Management | Machine Status | Online, Isolated, Offline | /#/malop-management?filter=machine-status:Connected,Isolated,Offline | Filters MalOps by affected machine connectivity status | Isolated machines indicate active containment measures in progress | Filter MalOps to show only "Isolated" machine status | V |
| MalOps Management | OS Type | Windows, Linux, MacOS | /#/malop-management?filter=machine-osType:WINDOWS,LINUX,OSX | Filters MalOps by affected machine operating system | Helps identify OS-specific attack patterns and vulnerabilities | Filter MalOps to show only "Windows" OS type | V |
| MalOps Management | User Privileges | Administrator, Domain user, Local system | /#/malop-management?filter=user-privileges:admin,domainUser,localSystem | Filters MalOps by affected user permission levels | Administrator compromises are highest priority security incidents | Filter MalOps to show only "Administrator" user privileges | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Advanced Specific Filter Combinations: | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "Last Week" AND "Under Investigation" status | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "High" priority AND "Active" state | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "Anti-Ransomware" detection engine AND "Quarantined" protection type | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "Lateral Movement" MITRE tactic AND "Process" IoC type | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "NGAV" MalOp type AND "Medium" severity | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "Online" machine status AND "Linux" OS type | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "Domain user" privileges AND "Closed" investigation status | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter MalOps to show "Last Month" AND "Behavioral Document Protection" detection engine | V |

## Malware alerts
| page | filter | parameters | link | explanation | notes | Navigation Prompt | worked? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Malware Alerts | Status Filter | All, Done, Excluded, Detected, Prevented, Disinfected, Deleting on restart, Quarantined | /#/malware/feed?status=Detected | Filters malware alerts by detection/remediation status | Status dropdown shows current protection action taken on detected malware | Single Filter Prompts: | NaN |
| NaN | Time Range Sort | All time, Last 24 hours, Last 48 hours, Last 7 days, Last month | /#/malware/feed?filters=type%3D,FilelessMalware;timestamp,FromTimeOp,86400000 | Filters malware alerts by detection time period | Time range affects which alerts are displayed in the feed | Filter malware alerts to show only "Detected" status | V |
| NaN | Search | Free text search across alert details | /#/malware/feed?search={query} | Searches within malware alert names, file names, machine names, and other alert details | Search field allows filtering by specific indicators or machine names | Filter malware alerts to show only "Prevented" status | V |
| NaN | Malware Classification | Malware Alerts | /#/malware/feed | Displays all malware alerts detected in the environment. Lists files flagged as malware affected machines detection time and status. | NaN | Filter malware alerts to show only "Quarantined" status | V |
| NaN | NaN | Known Malware Alerts | /#/malware/feed?filters=type,%3D,KnownMalware | Displays all the known malware alerts detected in the environment. Lists files flagged as malware affected machines detection time and status. | NaN | Filter malware alerts to show only "Disinfected" status | V |
| NaN | NaN | Unknown Malware Alerts | /#/malware/feed?filters=type,%3D,UnknownMalware | Displays all the unknown malware alerts detected in the environment. Lists files flagged as malware affected machines detection time and status. | NaN | Filter malware alerts to show only "Done" status | V |
| NaN | NaN | Fileless Malware Alerts | /#/malware/feed?filters=type,%3D,FilelessMalware | Displays all the fileless malware alerts detected in the environment. Lists files flagged as malware affected machines detection time and status. | NaN | Filter malware alerts to show only "Excluded" status | V |
| NaN | NaN | App Control Malware Alerts | /#/malware/feed?filters=type,%3D,ApplicationControlMalware | Displays all the app control malware alerts detected in the environment. Lists files flagged as malware affected machines detection time and status. | NaN | Filter malware alerts to show only "Deleting on restart" status | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter malware alerts to show "Last 24 hours" time range | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter malware alerts to show "Last 48 hours" time range | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter malware alerts to show "Last 7 days" time range | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter malware alerts to show "Last month" time range | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Show only "Known Malware" alerts | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Show only "Unknown Malware" alerts | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Show only "Fileless Malware" alerts | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Show only "App Control Malware" alerts | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Search malware alerts for specific file name or machine name  bb-win11-23h2 | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Advanced Combination Filter Prompts: | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter malware alerts to show "Quarantined" status AND "Last 24 hours" time range | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Filter malware alerts to show "Prevented" status AND "Last 7 days" time range | V |
| NaN | NaN | NaN | NaN | NaN | NaN | Show "Known Malware" alerts with "Detected" status from "Last 48 hours" | V |
