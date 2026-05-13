# Risk Assessment .xlsx

## Unified Schema for EDR.Next
| Parent Property Name | Property Name | Property Type | Is Repeated | Property Display Name | Description | Example Value | Enum Values | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -- | detections | Detection | repeated | NaN | The security detections found in the event | -- | NaN | NaN |
| -- | dynamic\_data | Dynamic Data | NaN | NaN | any additional data that does not fit the schema | NaN | NaN | NaN |
| -- | email | Email | NaN | NaN | The event email details | -- | NaN | NaN |
| -- | enrichment | Enrichment | NaN | NaN | XDR enrichments | -- | NaN | NaN |
| -- | metadata | Metadata | NaN | NaN | The event metadata details | -- | NaN | NaN |
| -- | network | Network | NaN | NaN | The event network details | -- | NaN | NaN |
| -- | principal | Noun | NaN | NaN | The event principal details | -- | NaN | NaN |
| -- | target | Noun | repeated | NaN | The event target details | -- | NaN | NaN |
| Asset | domain | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Asset | id | String | NaN | NaN | vendor specific unique identifier | NaN | NaN | NaN |
| Asset | ip\_address | IP Address | NaN | NaN | NaN | -- | NaN | NaN |
| Asset | mac | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Asset | name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Asset | os\_name | String | NaN | NaN | NaN | windows 10 | NaN | NaN |
| Asset | os\_platform\_architerture | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Asset | os\_type | Enum | NaN | NaN | NaN | WINDOWS | WINDOWS, MAC, LINUX, IOS, UNKNOWN | NaN |
| Asset | sensor\_id | String | NaN | NaN | NaN | -- | NaN | NaN |
| Asset | type | Enum | NaN | NaN | NaN | NaN | HOST, VIRTUAL\_MACHINE, MOBILE, IOT, UNKNOWN | must be populated if we have any asset information |
| Asset | uuid | String | NaN | NaN | Unique identifier assigned by Cybereason | NaN | NaN | NaN |
| AttackDetails | sub\_tecnique\_id | String | NaN | NaN | ATT&CK sub technique id | T1562.001 | NaN | NaN |
| AttackDetails | sub\_tecnique\_name | String | NaN | NaN | ATT&CK technique name | Disable or Modify Tools | NaN | NaN |
| AttackDetails | tactic\_id | String | NaN | NaN | ATT&CK tactic id | TA0005 | NaN | NaN |
| AttackDetails | tactic\_name | String | NaN | NaN | ATT&CK tactic name | Defense Evasion | NaN | NaN |
| AttackDetails | technique\_id | String | NaN | NaN | ATT&CK technique id | T1562 | NaN | NaN |
| AttackDetails | technique\_name | String | NaN | NaN | ATT&CK technique name | Impair Defense | NaN | NaN |
| AttackDetails | version | String | NaN | NaN | ATT&CK framework version | 12.1 | NaN | NaN |
| AttackEntity (XDR) | asset | Asset | NaN | NaN | The VP asset | -- | NaN | NaN |
| AttackEntity (XDR) | email\_address | String | NaN | NaN | The VP email address | NaN | NaN | NaN |
| AttackEntity (XDR) | url\_domain | UrlDomain | NaN | NaN | The VP domain | -- | NaN | NaN |
| AttackEntity (XDR) | user | User | NaN | NaN | The VP user | -- | NaN | NaN |
| Detection | attack\_details | AttackDetails | repeated | NaN | ATT&CK classification details | -- | NaN | NaN |
| Detection | category | String | NaN | NaN | A catogorization of the detection | Reconnaissance | NaN | NaN |
| Detection | id | String | NaN | NaN | A vendor-specific ID for a threat. | 187987870-321-98712837 | NaN | NaN |
| Detection | indicator\_type | Enum | NaN | NaN | The type of indicator that triggered the detection | PROCESS | FILE, PROCESS, DOMAIN, USER | NaN |
| Detection | method | String | NaN | NaN | The methos that detected the event | signature, fingerprint | NaN | NaN |
| Detection | name | String | NaN | NaN | A vendor-assigned classification common across multiple customers | Host Sweep | NaN | NaN |
| Detection | reason | String | NaN | NaN | The reason this event had occured | user password was wrong | NaN | NaN |
| Detection | rule | Rule | NaN | NaN | The information regurding the rules related to the event | -- | NaN | NaN |
| Detection | vulnerability\_cve | String | NaN | NaN | CVE of the vulnerabulity related to the detection | CVE-2023-28322 | NaN | NaN |
| DNS | dns\_query\_uuid | String | NaN | NaN | NaN | NaN | NaN | EDR |
| DNS | is\_resolved | Boolean | NaN | NaN | NaN | True | NaN | NaN |
| DNS | record\_type | Enum | NaN | NaN | The DNS record type | AAAA | A, AAAA, CNAME, NS, MX | NaN |
| DNS | resolver | IP Address | NaN | NaN | The DNS resolver IP address | -- | NaN | NaN |
| DNS | result | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Dynamic Data | NaN | Dynamic Data | NaN | NaN | contains any custom data that did not fit any field in the schema | NaN | NaN | for fields "field1","field2" and values "value1", "values2" add:\nadditional {\n    "field1" : "value1",\n    "field2" : "value2"\n} |
| Email | attachments | File | repeated | NaN | The email attached files | -- | NaN | NaN |
| Email | links | UrlDomain | repeated | NaN | The email attached URLs | -- | NaN | NaN |
| Email | message\_id | String | NaN | NaN | The email unique identifier | <CAOsPkSfLB1v0RCLDxyS9Mc4c=mN6n3T-Qw@mail.gmail.com> | NaN | NaN |
| Email | recipients | String | repeated | NaN | The email recipients | pete36@cybereason.com | NaN | NaN |
| Email | sender | String | NaN | NaN | The email sender | ella73@cybereason.com | NaN | NaN |
| Email | subject | String | NaN | NaN | The email subject | Upgrade your style with personalized Adams t-shirts | NaN | NaN |
| Enrichment (XDR) | alert\_name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Enrichment (XDR) | is\_alert | Boolean | NaN | NaN | NaN | NaN | NaN | NaN |
| Enrichment (XDR) | mitre | AttackDetails | NaN | NaN | NaN | -- | NaN | NaN |
| Enrichment (XDR) | performer | AttackEntity | NaN | NaN | NaN | -- | NaN | NaN |
| Enrichment (XDR) | rule\_mode | Enum | NaN | NaN | NaN | NaN | ALERT, TRAP, RESEARCH | NaN |
| Enrichment (XDR) | rule\_name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Enrichment (XDR) | rule\_type | Enum | NaN | NaN | NaN | NaN | ATOMIC, AGGREGATION, CORELLATION | NaN |
| Enrichment (XDR) | victims | AttackEntity | repeated | NaN | NaN | -- | NaN | NaN |
| File | company\_name | String | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | NaN |
| File | description | String | NaN | NaN | NaN | NaN | NaN | NaN |
| File | embedded\_content | String | repeated | NaN | NaN | NaN | NaN | NaN |
| File | entropy | ? | NaN | NaN | NaN | NaN | NaN | NaN |
| File | file\_version | String | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | id | String | NaN | NaN | The unique identifier of the file, as defined by the vendor | 1700-6faa-8331-0a22 | NaN | NaN |
| File | imp\_hash | String | NaN | NaN | NaN | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| File | is\_downloaded\_from\_internet | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | is\_pe\_file | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | last\_access\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | NaN |
| File | legal\_copywrite | String | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | md5 | String | NaN | NaN | The MD5 identifier of the file | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| File | old\_path | String | NaN | NaN | In case of a change of path, this field populate the value of the previous path | NaN | NaN | NaN |
| File | original\_name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| File | owner | User | NaN | NaN | NaN | NaN | NaN | NaN |
| File | path | String | NaN | NaN | The full path of the file | NaN | NaN | NaN |
| File | product\_name | String | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | product\_version | String | NaN | NaN | NaN | NaN | NaN | EDR only? |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | NaN |
| File | rich\_pe\_header | String | NaN | NaN | NaN | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | The SHA1 identifier of the file | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN |
| File | sha256 | String | NaN | NaN | The SHA256 identifier of the file | NaN | NaN | NaN |
| File | signature\_info | SignatureInfo | NaN | NaN | The signiture details | -- | NaN | NaN |
| File | tlsh | String | NaN | NaN | The TLSH identifier of the file | NaN | NaN | NaN |
| File | content\_type | String | NaN | NaN | NaN | PE | NaN | NaN |
| File | uuid | String | NaN | NaN | Unique identifier assigned by Cybereason | NaN | NaN | NaN |
| Group | id | String | NaN | NaN | The unique identifier of the group | 3245-9878-ff-900 | NaN | NaN |
| Group | name | String | NaN | NaN | The name of the group | admin-users | NaN | NaN |
| Group | permmisions | Permission | repeated | NaN | The group's permissions details | -- | ? | NaN |
| HTTP | browser | String | NaN | NaN | The HTTP browser | CHROME | NaN | NaN |
| HTTP | method | String | NaN | NaN | The HTTP request method | GET | NaN | NaN |
| HTTP | referral\_url\t | String | NaN | NaN | The URL for the HTTP referer | NaN | NaN | NaN |
| HTTP | response\_code | Int | NaN | NaN | The response status code | 200 | NaN | NaN |
| HTTP | user\_agent | String | NaN | NaN | The HTTP user agent | Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36 | NaN | NaN |
| IP Address | address | String | NaN | NaN | Thr IP address | 10.101.1.1 | NaN | NaN |
| IP Address | is\_internal | boolean | NaN | NaN | Inticates if the IP address is internal or external | True | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | NaN |
| IP Address | type | Enum | NaN | NaN | The format type of the IP address | IPV6 | IPV4, IPV6, UKNOWN | NaN |
| Metadata | action | Enum | NaN | NaN | The action taken as provided by the vendor. | ALLOW | ALLOW, BLOCK, FAIL, QUARENTINE, UNKNOWN | NaN |
| Metadata | action\_details | String | NaN | NaN | The unnormelized action taken as provided by the vendor. | Permitted | NaN | NaN |
| Metadata | categories | String | repeated | NaN | Any additional categorization related to the event (use only if all other "categorization" fields are used) | NaN | NaN | NaN |
| Metadata | code | String | NaN | NaN | Numeral represantation of the event type | 170001 | NaN | NaN |
| Metadata | description | String | NaN | NaN | A human-readable unparsable description of the event. | Domain was blocked by dns botnet C&C | NaN | NaN |
| Metadata | engine | String | NaN | NaN | The product engine that descoverd the detection | Behavioral Execution Prevention | NaN | NaN |
| Metadata | event\_id | String | NaN | NaN | The unique event ID as provided by the vendor | fdd3bf0d-1bfa-4919-8a45-f1a311d56753 | NaN | NaN |
| Metadata | event\_subtype | String | NaN | NaN | A product-specific event subtype | Suspicious Activity | NaN | NaN |
| Metadata | event\_type | String | NaN | NaN | A short, descriptive, human-readable, product-specific event name or type | Security | NaN | NaN |
| Metadata | parser\_label | String | NaN | NaN | The label for the Cybereason parser, as defined by integration team | FORTINET\_FORTIGATE | NaN | internal |
| Metadata | parser\_version | String | NaN | NaN | The version for the Cybereason parser, as defined by integration team | 1.4.0 | NaN | internal |
| Metadata | product\_category | String | NaN | NaN | The category of the product, as defined by Cybereason | Cloud | NaN | internal |
| Metadata | product\_name | String | NaN | NaN | The name of the product | Defender for Endpoint | NaN | NaN |
| Metadata | product\_url | String | NaN | NaN | A URL that takes the user to the source product console for this event. | https://security.microsoft.com/?hash=/threatexplorer?messageParams=11b32a86-ce41-495c-fea9-08dad0803938,11b32a86-ce41-495c-fea9 | NaN | NaN |
| Metadata | product\_version | String | NaN | NaN | The version of the product | 16.3 | NaN | NaN |
| Metadata | severity | Enum | NaN | NaN | The event severity as provided by the vendor. | HIGH | CRITICAL, ERROR, HIGH, MEDIUM, LOW, INFORMATIONAL, UNKNOWN | NaN |
| Metadata | severity\_details | String | NaN | NaN | The unnormelized event severity as provided by the vendor. | high | NaN | NaN |
| Metadata | timestamp | Timestamp | NaN | NaN | The timestamp when the event was generated. | NaN | NaN | NaN |
| Metadata | type | Enum | NaN | NaN | The Cybereason normelized event type | PROCESS\_CREATION | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=6674958#gid=6674958 | NaN |
| Metadata | uuid | String | NaN | NaN | The unique event ID as provided by Cybereason | NaN | NaN | NaN |
| Metadata | vendor\_name | String | NaN | NaN | The name of the vendor | Microsoft | NaN | NaN |
| Module | address | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Module | file | File | NaN | NaN | The file details of the module | -- | NaN | NaN |
| Module | name | String | NaN | NaN | The name of the module | NaN | NaN | NaN |
| Module | uuid | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Network | application\_protocol | Enum | NaN | NaN | The application protocol of the connection, normalized | SMTP | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=1306388957#gid=1306388957 | NaN |
| Network | application\_protocol\_details | String | NaN | NaN | The application protocol of the connection | smtp | NaN | NaN |
| Network | conn\_end\_time | Timestamp | NaN | NaN | the time the connection has ended | NaN | NaN | NaN |
| Network | conn\_start\_time | Timestamp | NaN | NaN | the time the connection has started | NaN | NaN | NaN |
| Network | conn\_first\_seen | Timestamp | NaN | NaN | NaN | NaN | NaN | NaN |
| Network | conn\_flags | String | repeated | NaN | The flags of the connection | NaN | NaN | NaN |
| Network | conn\_state | Enum | NaN | NaN | The state of the connection | OPEN | OPEN, CLOSED, UNKNOWN | NaN |
| Network | direction | Enum | NaN | NaN | The direction of the connection | INBOUND | OUTBOUND, INBOUND, UNKNOWN | NaN |
| Network | dns | DNS | NaN | NaN | the DNS details of the connection | -- | NaN | NaN |
| Network | http | HTTP | NaN | NaN | the HTTP details of the connection | -- | NaN | NaN |
| Network | icmp\_code | Enum | NaN | NaN | NaN | True | 0-15 | NaN |
| Network | icmp\_type | Enum | NaN | NaN | NaN | 8 | 0-255 | NaN |
| Network | transport\_protocol | Enum | NaN | NaN | The ip protocol of the connection | TCP | TCP, UDP, ICMP, UNKNOWN | NaN |
| Network | session\_id | String | NaN | NaN | The unique identifier of the session | 13444109 | NaN | NaN |
| NetworkInterface | address | IP Address | NaN | NaN | NaN | NaN | NaN | NaN |
| NetworkInterface | description | String | NaN | NaN | NaN | NaN | NaN | NaN |
| NetworkInterface | dhcp\_server | IP Address | NaN | NaN | IP address details about the DHCP server | -- | NaN | EDR only? |
| NetworkInterface | dns\_server | IP Address | NaN | NaN | IP address details about the DNS server | -- | NaN | EDR only? |
| NetworkInterface | gateway\_server | IP Address | NaN | NaN | IP address details about the gateway server | -- | NaN | EDR only? |
| NetworkInterface | id | String | NaN | NaN | The unique identifier of the network interface | NaN | NaN | NaN |
| NetworkInterface | mac | String | NaN | NaN | The mac address of the network interface | NaN | NaN | NaN |
| NetworkInterface | name | String | NaN | NaN | The name of the network interface | NaN | NaN | NaN |
| Noun | asset | Asset | NaN | NaN | The assosiated asset information | -- | NaN | NaN |
| Noun | bytes | Int | NaN | NaN | The transmitted\received bytes of the connection | 2341 | NaN | NaN |
| Noun | file | File | NaN | NaN | The assosiated file information | -- | NaN | NaN |
| Noun | group | Group | NaN | NaN | The assosiated group information | -- | NaN | NaN |
| Noun | nat\_ip | IP Address | NaN | NaN | The NAT IP address | -- | NaN | NaN |
| Noun | nat\_port | Int | NaN | NaN | The NAT port | 21152 | NaN | NaN |
| Noun | network\_interface | NetworkInterface | NaN | NaN | The assosiated network interface information | -- | NaN | NaN |
| Noun | packets | Int | NaN | NaN | The transmitted\received packets of the connection | 1889 | NaN | NaN |
| Noun | port | Int | NaN | NaN | The port of the connection | 445 | NaN | NaN |
| Noun | process | Process | NaN | NaN | The assosiated process information | -- | NaN | NaN |
| Noun | registry | Registry | NaN | NaN | The assosiated registry information | -- | NaN | NaN |
| Noun | resource | Resource | NaN | NaN | The assosiated resource information | -- | NaN | NaN |
| Noun | url | UrlDomain | NaN | NaN | The assosiated URL domain information | -- | NaN | NaN |
| Noun | user | User | NaN | NaN | The assosiated user information | -- | NaN | NaN |
| Permission | description | String | NaN | NaN | Human-readable description of the permissiom | Ability to update detect rules | NaN | NaN |
| Permission | id | String | NaN | NaN | The unique identifier of the permission | 133 | NaN | NaN |
| Permission | name | String | NaN | NaN | The name of the permission | chronicle.analyst.updateRule | NaN | NaN |
| Process | command\_line | String | NaN | NaN | The command line command that created the process. | NaN | NaN | NaN |
| Process | create\_flags | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | file | File | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | hooked\_functions | String | repeated | NaN | NaN | NaN | NaN | EDR only? |
| Process | integrity | Enum | NaN | NaN | NaN | NaN | MEDIUM, HIGH | NaN |
| Process | is\_created\_before\_probe\_started | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| Process | is\_created\_suspended | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| Process | is\_debugged | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| Process | is\_hidden | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| Process | is\_sandbox | Boolean | NaN | NaN | NaN | NaN | NaN | EDR only? |
| Process | modified\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | loaded\_modules | Module | repeated | NaN | The details about the related modules | -- | NaN | NaN |
| Process | logon\_session | string | NaN | NaN | Link to related logon ssesion (EDR) | NaN | NaN | NaN |
| Process | parameter\_flags | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | parent | Process | NaN | NaN | Information about the parent process. | -- | NaN | NaN |
| Process | pid | String | NaN | NaN | The process ID. | NaN | NaN | NaN |
| Process | rpc\_initiating\_process\_id | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | session\_id | Int | NaN | NaN | NaN | True | NaN | NaN |
| Process | stderr | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | stdin | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | stdout | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | sxs\_flags | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | threads | Thread | repeated | NaN | NaN | NaN | NaN | NaN |
| Process | tree\_id | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | user\_uuid | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | uuid | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | window\_starting\_height | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | window\_starting\_position\_horizontal | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | window\_starting\_position\_vertical | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | window\_starting\_width | Int | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | window\_station | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Registry | data\_type | Enum | NaN | NaN | NaN | REG\_SZ | REG\_BINARY, REG\_DWORD, REG\_DWORD\_LITTLE\_ENDIAN, REG\_DWORD\_BIG\_ENDIAN, REG\_EXPAND\_SZ, REG\_LINK\nREG\_MULTI\_SZ, REG\_NONE, REG\_QWORD, REG\_QWORD\_LITTLE\_ENDIAN, REG\_SZ | NaN |
| Registry | is\_clsid | boolean | NaN | NaN | NaN | False | NaN | NaN |
| Registry | owner | User | NaN | NaN | NaN | NaN | NaN | NaN |
| Registry | path | String | NaN | NaN | Registry key associated with an application or system component | HKCU\Environment... | NaN | NaN |
| Registry | data | String | NaN | NaN | Data associated with a registry value | %USERPROFILE%\Local Settings\Temp | NaN | NaN |
| Registry | value | String | NaN | NaN | Name of the registry value associated with an application or system component | TEMP | NaN | NaN |
| Resource | id | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | name | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | parent | Resource | NaN | NaN | NaN | -- | NaN | NaN |
| Resource | subtype | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | type | Enum | NaN | NaN | NaN | TABLE | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=1023176768#gid=1023176768 | NaN |
| Resource | type\_details | String | NaN | NaN | NaN | BigQuery Table | NaN | NaN |
| Rule | id | String | NaN | NaN | A vendor-specific ID and name for a rule | 5d2b44d0-5ef6-40f5-a704-47d61d3babbe | NaN | NaN |
| Rule | name | String | NaN | NaN | Name of the security rule | BlockInboundToOracle | NaN | NaN |
| Rule | ruleset | Rule | NaN | NaN | The ruleset details | -- | NaN | NaN |
| Rule | type | String | NaN | NaN | The type of security rule. | signature | NaN | NaN |
| Rule | version | String | NaN | NaN | Version of the security rule | v1.1 | NaN | NaN |
| SignatureInfo | hash | String | NaN | NaN | NaN | NaN | NaN | NaN |
| SignatureInfo | is\_signature\_fail | Boolean | NaN | NaN | NaN | NaN | NaN | NaN |
| SignatureInfo | is\_signature\_verified | Boolean | NaN | NaN | Indicated if the file signiture is verified | False | NaN | NaN |
| SignatureInfo | is\_signed | Boolean | NaN | NaN | Indicated if the file is signed | True | NaN | NaN |
| SignatureInfo | is\_verify\_fail | Boolean | NaN | NaN | NaN | NaN | NaN | NaN |
| SignatureInfo | reason\_verify\_fail | String | NaN | NaN | NaN | NaN | NaN | NaN |
| SignatureInfo | signer | String | NaN | NaN | The name of the file signer | Microsoft | NaN | NaN |
| Thread | token\_type | String | NaN | NaN | NaN | NaN | NaN | NaN |
| Thread | call\_stack\_modules | Module | repeated | NaN | NaN | NaN | NaN | NaN |
| UrlDomain | domain\_name | String | NaN | NaN | The domain of the URL | login-outlook-midstream.com | NaN | NaN |
| UrlDomain | is\_internal | Boolean | NaN | NaN | Inticates if the domain is internal or external | False | NaN | NaN |
| UrlDomain | reputation | Enum | NaN | NaN | The domain reputation previded by the Vendor (Cybereason) | BENIGN | BENIGN, MALICIOUS, NEUTRAL | NaN |
| UrlDomain | url\_path | String | NaN | NaN | The URL full path | https://login-outlook-midstream.com/hummus.co.jp | NaN | NaN |
| UrlDomain | uuid | String | NaN | NaN | Unique identifier assigned by Cyberason | NaN | NaN | NaN |
| User | display\_name | String | NaN | NaN | The display name of the user | Avi Ron | NaN | NaN |
| User | domain | String | NaN | NaN | The domain the user belongs to | cybereason.com | NaN | NaN |
| User | email\_addresses | String | repeated | NaN | The email addresses related to the user | avi.ron@cybereason.com | NaN | NaN |
| User | id | String | NaN | NaN | The vendor specific unique identifier of the user | ff22-2144-f55a-1004 | NaN | NaN |
| User | permmisions | Permission | repeated | NaN | The permissions of the user | -- | NaN | NaN |
| User | username | String | NaN | NaN | The name of the user | avi.ron@cybereason.com | NaN | NaN |
| User | uuid | String | NaN | NaN | Unique identifier assigned by Cyberason | NaN | NaN | NaN |

## Risk Assessment relevant fields
| CONDITIONS FIELDS | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Unnamed: 9 | Unnamed: 10 | Unnamed: 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Parent Property Name | Property Name | Property Type | Is Repeated | Property Display Name | Example Value | Enum Values | Notes | field path | NaN | NaN | NaN |
| Metadata | engine | String | NaN | NaN | Behavioral Execution Prevention | AIAV\nAnti-ransomware\nAnti-stealer\nApp control\nBehavioral execution prevention\nCloudAV\nExploit protection\nGeneric Shellcode Detection (GSD)\nHash based execution block\nProcess integrity\nScript protection\nSecret scanner\nVariant payload prevention\n | NaN | metadata.engine | NaN | NaN | NaN |
| Metadata | action | Enum | NaN | NaN | ALLOW | ALLOW, BLOCK, FAIL, QUARENTINE, UNKNOWN | NaN | metadata.action | NaN | NaN | NaN |
| Asset | type | Enum | NaN | NaN | NaN | HOST, VIRTUAL\_MACHINE, MOBILE, IOT, UNKNOWN | must be populated if we have any asset information | principal.asset.type, target.asset.type | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| IDENTITIES | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| Parent Property Name | Property Name | Property Type | Is Repeated | Property Display Name | Example Value | Enum Values | Notes | field path | NaN | NaN | severity |
| -- | metadata | Metadata | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | Timestemp |
| Metadata | engine | String | NaN | NaN | Behavioral Execution Prevention | NaN | NaN | metadata.engine | NaN | NaN | NaN |
| Metadata | event\_id | String | NaN | NaN | fdd3bf0d-1bfa-4919-8a45-f1a311d56753 | NaN | NaN | metadata.event\_id | NaN | NaN | NaN |
| Metadata | event\_subtype | String | NaN | NaN | Suspicious Activity | NaN | NaN | metadata.event\_subtype | NaN | NaN | NaN |
| Metadata | event\_type | String | NaN | NaN | Security | NaN | NaN | metadata.event\_type | NaN | NaN | NaN |
| Metadata | severity | Enum | NaN | NaN | HIGH | CRITICAL, ERROR, HIGH, MEDIUM, LOW, INFORMATIONAL, UNKNOWN | NaN | metadata.severity | NaN | NaN | NaN |
| Metadata | severity\_details | String | NaN | NaN | high | NaN | NaN | metadata.severity\_details | NaN | NaN | NaN |
| metadata.type | timestamp | Timestamp | NaN | NaN | NaN | NaN | NaN | metadata.timestamp | NaN | NaN | NaN |
| Metadata | type | Enum | NaN | NaN | PROCESS\_CREATION | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=6674958#gid=6674958 | NaN | metadata.type | NaN | NaN | NaN |
| Metadata | uuid | String | NaN | NaN | NaN | NaN | NaN | metadata.uuid | NaN | NaN | NaN |
| -- | principal | Noun | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Noun | asset | Asset | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Asset | domain | String | NaN | NaN | NaN | NaN | NaN | principal.asset.domain | NaN | NaN | NaN |
| Asset | id | String | NaN | NaN | NaN | NaN | NaN | principal.asset.id | NaN | NaN | NaN |
| Asset | ip\_address | IP Address | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | principal.asset.ip\_address.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | principal.asset.ip\_address.reputation | NaN | NaN | NaN |
| Asset | name | String | NaN | NaN | NaN | NaN | NaN | principal.asset.name | NaN | NaN | NaN |
| Asset | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.asset.uuid | NaN | NaN | NaN |
| Noun | file | File | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.file.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | principal.file.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | principal.file.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | principal.file.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | principal.file.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | principal.file.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | principal.file.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.file.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | principal.file.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.file.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | principal.file.reputation | NaN | NaN | NaN |
| Noun | group | Group | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Group | id | String | NaN | NaN | 3245-9878-ff-900 | NaN | NaN | principal.group.id | NaN | NaN | NaN |
| Group | name | String | NaN | NaN | admin-users | NaN | NaN | principal.group.name | NaN | NaN | NaN |
| Noun | nat\_ip | IP Address | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | principal.nat\_ip.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | principal.nat\_ip.reputation | NaN | NaN | NaN |
| Noun | network\_interface | NetworkInterface | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| NetworkInterface | address | IP Address | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | principal.NetworkInterface.address.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | principal.NetworkInterface.address.reputation | NaN | NaN | NaN |
| NetworkInterface | dhcp\_server | IP Address | NaN | NaN | -- | NaN | EDR only? | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | principal.NetworkInterface.dhcp\_server.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | principal.NetworkInterface.dhcp\_server.reputation | NaN | NaN | NaN |
| NetworkInterface | dns\_server | IP Address | NaN | NaN | -- | NaN | EDR only? | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | principal.NetworkInterface.dns\_server.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | principal.NetworkInterface.dns\_server.reputation | NaN | NaN | NaN |
| NetworkInterface | gateway\_server | IP Address | NaN | NaN | -- | NaN | EDR only? | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | principal.NetworkInterface.gateway\_server.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | principal.NetworkInterface.gateway\_server.reputation | NaN | NaN | NaN |
| NetworkInterface | id | String | NaN | NaN | NaN | NaN | NaN | principal.NetworkInterface.id | NaN | NaN | NaN |
| NetworkInterface | name | String | NaN | NaN | NaN | NaN | NaN | principal.NetworkInterface.name | NaN | NaN | NaN |
| Noun | process | Process | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.creation\_time | NaN | NaN | NaN |
| Process | integrity | Enum | NaN | NaN | NaN | NaN | MEDIUM, HIGH | principal.process.integrity | NaN | NaN | NaN |
| Process | file | File | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.file.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | principal.process.file.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | principal.process.file.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | principal.process.file.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | principal.process.file.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | principal.process.file.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | principal.process.file.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.process.file.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | principal.process.file.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.file.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | principal.process.file.reputation | NaN | NaN | NaN |
| Process | modified\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.modified\_time | NaN | NaN | NaN |
| Process | pid | String | NaN | NaN | NaN | NaN | NaN | principal.process.pid | NaN | NaN | NaN |
| Process | user\_uuid | String | NaN | NaN | NaN | NaN | NaN | principal.process.user\_uuid | NaN | NaN | NaN |
| Process | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.process.uuid | NaN | NaN | NaN |
| Process | parent | Process | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.parent.creation\_time | NaN | NaN | NaN |
| Process | integrity | Enum | NaN | NaN | NaN | NaN | MEDIUM, HIGH | principal.process.parent.integrity | NaN | NaN | NaN |
| Process | file | File | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | principal.process.parent.file.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | principal.process.parent.file.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | principal.process.parent.file.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.parent.file.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | principal.process.parent.file.reputation | NaN | NaN | NaN |
| Process | modified\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | principal.process.parent.modified\_time | NaN | NaN | NaN |
| Process | pid | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.pid | NaN | NaN | NaN |
| Process | user\_uuid | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.user\_uuid | NaN | NaN | NaN |
| Process | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.process.parent.uuid | NaN | NaN | NaN |
| Noun | registry | Registry | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Registry | owner | User | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| User | display\_name | String | NaN | NaN | Avi Ron | NaN | NaN | principal.registry.owner.display\_name | NaN | NaN | NaN |
| User | domain | String | NaN | NaN | cybereason.com | NaN | NaN | principal.registry.owner.domain | NaN | NaN | NaN |
| User | email\_addresses | String | repeated | NaN | avi.ron@cybereason.com | NaN | NaN | principal.registry.owner.email\_addresses | NaN | NaN | NaN |
| User | id | String | NaN | NaN | ff22-2144-f55a-1004 | NaN | NaN | principal.registry.owner.id | NaN | NaN | NaN |
| User | username | String | NaN | NaN | avi.ron@cybereason.com | NaN | NaN | principal.registry.owner.username | NaN | NaN | NaN |
| User | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.registry.owner.uuid | NaN | NaN | NaN |
| User | permmisions | Permission | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Permission | description | String | NaN | NaN | Ability to update detect rules | NaN | NaN | principal.registry.owner.permmisions.description | NaN | NaN | NaN |
| Permission | id | String | NaN | NaN | 133 | NaN | NaN | principal.registry.owner.permmisions.id | NaN | NaN | NaN |
| Permission | name | String | NaN | NaN | chronicle.analyst.updateRule | NaN | NaN | principal.registry.owner.permmisions.name | NaN | NaN | NaN |
| Noun | resource | Resource | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | id | String | NaN | NaN | NaN | NaN | NaN | principal.resource.id | NaN | NaN | NaN |
| Resource | name | String | NaN | NaN | NaN | NaN | NaN | principal.resource.name | NaN | NaN | NaN |
| Resource | type | Enum | NaN | NaN | NaN | TABLE | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=1023176768#gid=1023176768 | principal.resource.type | NaN | NaN | NaN |
| Resource | parent | Resource | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | id | String | NaN | NaN | NaN | NaN | NaN | principal.resource.parent.id | NaN | NaN | NaN |
| Resource | name | String | NaN | NaN | NaN | NaN | NaN | principal.resource.parent.name | NaN | NaN | NaN |
| Resource | type | Enum | NaN | NaN | NaN | TABLE | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=1023176768#gid=1023176768 | principal.resource.parent.type | NaN | NaN | NaN |
| Noun | url | UrlDomain | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| UrlDomain | domain\_name | String | NaN | NaN | login-outlook-midstream.com | NaN | NaN | principal.url.domain\_name | NaN | NaN | NaN |
| UrlDomain | url\_path | String | NaN | NaN | https://login-outlook-midstream.com/hummus.co.jp | NaN | NaN | principal.url.url\_path | NaN | NaN | NaN |
| UrlDomain | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.url.uuid | NaN | NaN | NaN |
| UrlDomain | reputation | Enum | NaN | NaN | BENIGN | BENIGN, MALICIOUS, NEUTRAL | NaN | principal.url.reputation | NaN | NaN | NaN |
| Noun | user | User | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| User | display\_name | String | NaN | NaN | Avi Ron | NaN | NaN | principal.user.display\_name | NaN | NaN | NaN |
| User | domain | String | NaN | NaN | cybereason.com | NaN | NaN | principal.user.domain | NaN | NaN | NaN |
| User | email\_addresses | String | repeated | NaN | avi.ron@cybereason.com | NaN | NaN | principal.user.email\_address | NaN | NaN | NaN |
| User | id | String | NaN | NaN | ff22-2144-f55a-1004 | NaN | NaN | principal.user.id | NaN | NaN | NaN |
| User | username | String | NaN | NaN | avi.ron@cybereason.com | NaN | NaN | principal.usename | NaN | NaN | NaN |
| User | uuid | String | NaN | NaN | NaN | NaN | NaN | principal.user.uuid | NaN | NaN | NaN |
| User | permmisions | Permission | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Permission | description | String | NaN | NaN | Ability to update detect rules | NaN | NaN | principal.user.permmisions.description | NaN | NaN | NaN |
| Permission | id | String | NaN | NaN | 133 | NaN | NaN | principal.user.permmisions.id | NaN | NaN | NaN |
| Permission | name | String | NaN | NaN | chronicle.analyst.updateRule | NaN | NaN | principal.user.permmisions.name | NaN | NaN | NaN |
| -- | target | Noun | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Noun | asset | Asset | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Asset | domain | String | NaN | NaN | NaN | NaN | NaN | target.asset.domain | NaN | NaN | NaN |
| Asset | id | String | NaN | NaN | NaN | NaN | NaN | target.asset.id | NaN | NaN | NaN |
| Asset | ip\_address | IP Address | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | target.asset.ip\_address.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | target.asset.ip\_address.reputation | NaN | NaN | NaN |
| Asset | name | String | NaN | NaN | NaN | NaN | NaN | target.asset.name | NaN | NaN | NaN |
| Asset | uuid | String | NaN | NaN | NaN | NaN | NaN | target.asset.uuid | NaN | NaN | NaN |
| Noun | file | File | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.file.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | target.file.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | target.file.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | target.file.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | target.file.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | target.file.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | target.file.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | target.file.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | target.file.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.file.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | target.file.reputation | NaN | NaN | NaN |
| Noun | group | Group | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Group | id | String | NaN | NaN | 3245-9878-ff-900 | NaN | NaN | target.group.id | NaN | NaN | NaN |
| Group | name | String | NaN | NaN | admin-users | NaN | NaN | target.group.name | NaN | NaN | NaN |
| Noun | nat\_ip | IP Address | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | target.nat\_ip.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | target.nat\_ip.reputation | NaN | NaN | NaN |
| Noun | network\_interface | NetworkInterface | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| NetworkInterface | address | IP Address | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | target.NetworkInterface.address.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | target.NetworkInterface.address.reputation | NaN | NaN | NaN |
| NetworkInterface | dhcp\_server | IP Address | NaN | NaN | -- | NaN | EDR only? | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | target.NetworkInterface.dhcp\_server.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | target.NetworkInterface.dhcp\_server.reputation | NaN | NaN | NaN |
| NetworkInterface | dns\_server | IP Address | NaN | NaN | -- | NaN | EDR only? | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | target.NetworkInterface.dns\_server.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | target.NetworkInterface.dns\_server.reputation | NaN | NaN | NaN |
| NetworkInterface | gateway\_server | IP Address | NaN | NaN | -- | NaN | EDR only? | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | target.NetworkInterface.gateway\_server.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | target.NetworkInterface.gateway\_server.reputation | NaN | NaN | NaN |
| NetworkInterface | id | String | NaN | NaN | NaN | NaN | NaN | target.NetworkInterface.id | NaN | NaN | NaN |
| NetworkInterface | name | String | NaN | NaN | NaN | NaN | NaN | target.NetworkInterface.name | NaN | NaN | NaN |
| Noun | process | Process | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.creation\_time | NaN | NaN | NaN |
| Process | integrity | Enum | NaN | NaN | NaN | NaN | MEDIUM, HIGH | target.process.integrity | NaN | NaN | NaN |
| Process | file | File | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.file.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | target.process.file.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | target.process.file.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | target.process.file.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | target.process.file.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | target.process.file.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | target.process.file.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | target.process.file.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | target.process.file.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.file.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | target.process.file.reputation | NaN | NaN | NaN |
| Process | modified\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.modified\_time | NaN | NaN | NaN |
| Process | pid | String | NaN | NaN | NaN | NaN | NaN | target.process.pid | NaN | NaN | NaN |
| Process | user\_uuid | String | NaN | NaN | NaN | NaN | NaN | target.process.user\_uuid | NaN | NaN | NaN |
| Process | uuid | String | NaN | NaN | NaN | NaN | NaN | target.process.uuid | NaN | NaN | NaN |
| Process | parent | Process | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Process | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.parent.creation\_time | NaN | NaN | NaN |
| Process | integrity | Enum | NaN | NaN | NaN | NaN | MEDIUM, HIGH | target.process.parent.integrity | NaN | NaN | NaN |
| Process | file | File | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | target.process.parent.file.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | target.process.parent.file.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | target.process.parent.file.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.parent.file.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | target.process.parent.file.reputation | NaN | NaN | NaN |
| Process | modified\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | target.process.parent.modified\_time | NaN | NaN | NaN |
| Process | pid | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.pid | NaN | NaN | NaN |
| Process | user\_uuid | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.user\_uuid | NaN | NaN | NaN |
| Process | uuid | String | NaN | NaN | NaN | NaN | NaN | target.process.parent.uuid | NaN | NaN | NaN |
| Noun | registry | Registry | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Registry | owner | User | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| User | display\_name | String | NaN | NaN | Avi Ron | NaN | NaN | target.registry.owner.display\_name | NaN | NaN | NaN |
| User | domain | String | NaN | NaN | cybereason.com | NaN | NaN | target.registry.owner.domain | NaN | NaN | NaN |
| User | email\_addresses | String | repeated | NaN | avi.ron@cybereason.com | NaN | NaN | target.registry.owner.email\_addresses | NaN | NaN | NaN |
| User | id | String | NaN | NaN | ff22-2144-f55a-1004 | NaN | NaN | target.registry.owner.id | NaN | NaN | NaN |
| User | username | String | NaN | NaN | avi.ron@cybereason.com | NaN | NaN | target.registry.owner.username | NaN | NaN | NaN |
| User | uuid | String | NaN | NaN | NaN | NaN | NaN | target.registry.owner.uuid | NaN | NaN | NaN |
| User | permmisions | Permission | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Permission | description | String | NaN | NaN | Ability to update detect rules | NaN | NaN | target.registry.owner.permmisions.description | NaN | NaN | NaN |
| Permission | id | String | NaN | NaN | 133 | NaN | NaN | target.registry.owner.permmisions.id | NaN | NaN | NaN |
| Permission | name | String | NaN | NaN | chronicle.analyst.updateRule | NaN | NaN | target.registry.owner.permmisions.name | NaN | NaN | NaN |
| Noun | resource | Resource | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | id | String | NaN | NaN | NaN | NaN | NaN | target.resource.id | NaN | NaN | NaN |
| Resource | name | String | NaN | NaN | NaN | NaN | NaN | target.resource.name | NaN | NaN | NaN |
| Resource | type | Enum | NaN | NaN | NaN | TABLE | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=1023176768#gid=1023176768 | target.resource.type | NaN | NaN | NaN |
| Resource | parent | Resource | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Resource | id | String | NaN | NaN | NaN | NaN | NaN | target.resource.parent.id | NaN | NaN | NaN |
| Resource | name | String | NaN | NaN | NaN | NaN | NaN | target.resource.parent.name | NaN | NaN | NaN |
| Resource | type | Enum | NaN | NaN | NaN | TABLE | https://docs.google.com/spreadsheets/d/1a8chTWpVdHBWSUjJ0a9JuXfWTpv7eE9C22kCP8\_6jxU/edit?gid=1023176768#gid=1023176768 | target.resource.parent.type | NaN | NaN | NaN |
| Noun | url | UrlDomain | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| UrlDomain | domain\_name | String | NaN | NaN | login-outlook-midstream.com | NaN | NaN | target.url.domain\_name | NaN | NaN | NaN |
| UrlDomain | url\_path | String | NaN | NaN | https://login-outlook-midstream.com/hummus.co.jp | NaN | NaN | target.url.url\_path | NaN | NaN | NaN |
| UrlDomain | uuid | String | NaN | NaN | NaN | NaN | NaN | target.url.uuid | NaN | NaN | NaN |
| UrlDomain | reputation | Enum | NaN | NaN | BENIGN | BENIGN, MALICIOUS, NEUTRAL | NaN | target.url.reputation | NaN | NaN | NaN |
| Noun | user | User | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| User | display\_name | String | NaN | NaN | Avi Ron | NaN | NaN | target.use.display\_name | NaN | NaN | NaN |
| User | domain | String | NaN | NaN | cybereason.com | NaN | NaN | target.use.domain | NaN | NaN | NaN |
| User | email\_addresses | String | repeated | NaN | avi.ron@cybereason.com | NaN | NaN | target.use.email\_address | NaN | NaN | NaN |
| User | id | String | NaN | NaN | ff22-2144-f55a-1004 | NaN | NaN | target.user.id | NaN | NaN | NaN |
| User | username | String | NaN | NaN | avi.ron@cybereason.com | NaN | NaN | target.usename | NaN | NaN | NaN |
| User | uuid | String | NaN | NaN | NaN | NaN | NaN | target.user.uuid | NaN | NaN | NaN |
| User | permmisions | Permission | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Permission | description | String | NaN | NaN | Ability to update detect rules | NaN | NaN | target.user.permmisions.description | NaN | NaN | NaN |
| Permission | id | String | NaN | NaN | 133 | NaN | NaN | target.user.permmisions.id | NaN | NaN | NaN |
| Permission | name | String | NaN | NaN | chronicle.analyst.updateRule | NaN | NaN | target.user.permmisions.name | NaN | NaN | NaN |
| -- | network | Network | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Network | conn\_end\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | network.conn\_end\_time | NaN | NaN | NaN |
| Network | conn\_start\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | network.conn\_start\_time | NaN | NaN | NaN |
| Network | conn\_first\_seen | Timestamp | NaN | NaN | NaN | NaN | NaN | network.conn\_first\_seen | NaN | NaN | NaN |
| Network | dns | DNS | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| DNS | dns\_query\_uuid | String | NaN | NaN | NaN | NaN | EDR | network.dns\_query\_uuid | NaN | NaN | NaN |
| DNS | resolver | IP Address | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| IP Address | address | String | NaN | NaN | 10.101.1.1 | NaN | NaN | network.dns.resolver.address | NaN | NaN | NaN |
| IP Address | reputation | Enum | NaN | NaN | The IP address reputation previded by the Vendor | BENIGN | BENIGN, MALICIOUS, NEUTRAL | network.dns.resolver.reputation | NaN | NaN | NaN |
| Network | session\_id | String | NaN | NaN | The unique identifier of the session | 13444109 | NaN | network.session\_id | NaN | NaN | NaN |
| -- | email | Email | NaN | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| Email | attachments | File | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| File | creation\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | email.attachment.creation\_time | NaN | NaN | NaN |
| File | id | String | NaN | NaN | 1700-6faa-8331-0a22 | NaN | NaN | email.attachment.id | NaN | NaN | NaN |
| File | md5 | String | NaN | NaN | 938c2cc0dcc05f2b68c4287040cfcf71 | NaN | NaN | email.attachment.md5 | NaN | NaN | NaN |
| File | name | String | NaN | NaN | NaN | NaN | NaN | email.attachment.name | NaN | NaN | NaN |
| File | sha1 | String | NaN | NaN | 2fd4e1c67a2d28fced849ee1bb76e7391b93eb12 | NaN | NaN | email.attachment.sha1 | NaN | NaN | NaN |
| File | sha256 | String | NaN | NaN | NaN | NaN | NaN | email.attachment.sha256 | NaN | NaN | NaN |
| File | tlsh | String | NaN | NaN | NaN | NaN | NaN | email.attachment.tlsh | NaN | NaN | NaN |
| File | uuid | String | NaN | NaN | NaN | NaN | NaN | email.attachment.uuid | NaN | NaN | NaN |
| File | internal\_name | String | NaN | NaN | NaN | NaN | NaN | email.attachment.internal\_name | NaN | NaN | NaN |
| File | modification\_time | Timestamp | NaN | NaN | NaN | NaN | NaN | email.attachment.modification\_time | NaN | NaN | NaN |
| File | reputation | Enum | NaN | NaN | The reputation of the file | MALICIOUS | BENIGN, MALICIOUS, NEUTRAL | email.attachment.reputation | NaN | NaN | NaN |
| Email | links | UrlDomain | repeated | NaN | -- | NaN | NaN | NaN | NaN | NaN | NaN |
| UrlDomain | domain\_name | String | NaN | NaN | login-outlook-midstream.com | NaN | NaN | email.links.domain\_name | NaN | NaN | NaN |
| UrlDomain | url\_path | String | NaN | NaN | https://login-outlook-midstream.com/hummus.co.jp | NaN | NaN | email.links.url\_path | NaN | NaN | NaN |
| UrlDomain | uuid | String | NaN | NaN | NaN | NaN | NaN | email.links.uuid | NaN | NaN | NaN |
| UrlDomain | reputation | Enum | NaN | NaN | BENIGN | BENIGN, MALICIOUS, NEUTRAL | NaN | email.links.reputation | NaN | NaN | NaN |
| Email | recipients | String | repeated | NaN | pete36@cybereason.com | NaN | NaN | email.recipients | NaN | NaN | NaN |
| Email | sender | String | NaN | NaN | ella73@cybereason.com | NaN | NaN | email.sender | NaN | NaN | NaN |
| Email | message\_id | String | NaN | NaN | The email unique identifier | <CAOsPkSfLB1v0RCLDxyS9Mc4c=mN6n3T-Qw@mail.gmail.com> | NaN | email.message\_id | NaN | NaN | NaN |
| -- | detections | Detection | repeated | NaN | The security detections found in the event | -- | NaN | NaN | NaN | NaN | NaN |
| Detection | vulnerability\_cve | String | NaN | NaN | CVE of the vulnerabulity related to the detection | CVE-2023-28322 | NaN | detections.vulnerability\_cve | NaN | NaN | NaN |

## FIELDS PATH
| metadata | principal | target | network | email | Detection |
| --- | --- | --- | --- | --- | --- |
| metadata.engine | principal.asset.domain | target.asset.domain | network.conn\_end\_time | email.attachment.creation\_time | detections.vulnerability\_cve |
| metadata.action | principal.asset.id | target.asset.id | network.conn\_start\_time | email.attachment.id | NaN |
| metadata.event\_id | principal.asset.type | target.asset.type | network.conn\_first\_seen | email.attachment.md5 | NaN |
| metadata.event\_subtype | principal.asset.ip\_address.address | target.asset.ip\_address.address | network.dns\_query\_uuid | email.attachment.name | NaN |
| metadata.event\_type | principal.asset.ip\_address.reputation | target.asset.ip\_address.reputation | network.dns.resolver.address | email.attachment.sha1 | NaN |
| metadata.severity | principal.asset.name | target.asset.name | network.dns.resolver.reputation | email.attachment.sha256 | NaN |
| metadata.severity\_details | principal.asset.uuid | target.asset.uuid | network.session\_id | email.attachment.tlsh | NaN |
| metadata.timestamp | principal.file.creation\_time | target.file.creation\_time | NaN | email.attachment.uuid | NaN |
| metadata.type | principal.file.id | target.file.id | NaN | email.attachment..internal\_name | NaN |
| metadata.uuid | principal.file.md5 | target.file.md5 | NaN | email.attachment.modification\_time | NaN |
| NaN | principal.file.name | target.file.name | NaN | email.attachment.reputation | NaN |
| NaN | principal.file.sha1 | target.file.sha1 | NaN | email.links.domain\_name | NaN |
| NaN | principal.file.sha256 | target.file.sha256 | NaN | email.links.url\_path | NaN |
| NaN | principal.file.tlsh | target.file.tlsh | NaN | email.links.uuid | NaN |
| NaN | principal.file.uuid | target.file.uuid | NaN | email.links.reputation | NaN |
| NaN | principal.file.internal\_name | target.file.internal\_name | NaN | email.message\_id | NaN |
| NaN | principal.file.modification\_time | target.file.modification\_time | NaN | email.recipients | NaN |
| NaN | principal.file.reputation | target.file.reputation | NaN | email.sender | NaN |
| NaN | principal.group.id | target.group.id | NaN | NaN | NaN |
| NaN | principal.group.name | target.group.name | NaN | NaN | NaN |
| NaN | principal.nat\_ip.address | target.nat\_ip.address | NaN | NaN | NaN |
| NaN | principal.nat\_ip.reputation | target.nat\_ip.reputation | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.address.address | target.NetworkInterface.address.address | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.address.reputation | target.NetworkInterface.address.reputation | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.dhcp\_server.address | target.NetworkInterface.dhcp\_server.address | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.dhcp\_server.reputation | target.NetworkInterface.dhcp\_server.reputation | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.dns\_server.address | target.NetworkInterface.dns\_server.address | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.dns\_server.reputation | target.NetworkInterface.dns\_server.reputation | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.gateway\_server.address | target.NetworkInterface.gateway\_server.address | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.gateway\_server.reputation | target.NetworkInterface.gateway\_server.reputation | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.id | target.NetworkInterface.id | NaN | NaN | NaN |
| NaN | principal.NetworkInterface.name | target.NetworkInterface.name | NaN | NaN | NaN |
| NaN | principal.process.creation\_time | target.process.creation\_time | NaN | NaN | NaN |
| NaN | principal.process.integrity | target.process.integrity | NaN | NaN | NaN |
| NaN | principal.process.file.creation\_time | target.process.file.creation\_time | NaN | NaN | NaN |
| NaN | principal.process.file.id | target.process.file.id | NaN | NaN | NaN |
| NaN | principal.process.file.md5 | target.process.file.md5 | NaN | NaN | NaN |
| NaN | principal.process.file.name | target.process.file.name | NaN | NaN | NaN |
| NaN | principal.process.file.sha1 | target.process.file.sha1 | NaN | NaN | NaN |
| NaN | principal.process.file.sha256 | target.process.file.sha256 | NaN | NaN | NaN |
| NaN | principal.process.file.tlsh | target.process.file.tlsh | NaN | NaN | NaN |
| NaN | principal.process.file.uuid | target.process.file.uuid | NaN | NaN | NaN |
| NaN | principal.process.file.internal\_name | target.process.file.internal\_name | NaN | NaN | NaN |
| NaN | principal.process.file.modification\_time | target.process.file.modification\_time | NaN | NaN | NaN |
| NaN | principal.process.file.reputation | target.process.file.reputation | NaN | NaN | NaN |
| NaN | principal.process.modified\_time | target.process.modified\_time | NaN | NaN | NaN |
| NaN | principal.process.pid | target.process.pid | NaN | NaN | NaN |
| NaN | principal.process.user\_uuid | target.process.user\_uuid | NaN | NaN | NaN |
| NaN | principal.process.uuid | target.process.uuid | NaN | NaN | NaN |
| NaN | principal.process.parent.creation\_time | target.process.parent.creation\_time | NaN | NaN | NaN |
| NaN | principal.process.parent.integrity | target.process.parent.integrity | NaN | NaN | NaN |
| NaN | principal.process.parent.file.creation\_time | target.process.parent.file.creation\_time | NaN | NaN | NaN |
| NaN | principal.process.parent.file.id | target.process.parent.file.id | NaN | NaN | NaN |
| NaN | principal.process.parent.file.md5 | target.process.parent.file.md5 | NaN | NaN | NaN |
| NaN | principal.process.parent.file.name | target.process.parent.file.name | NaN | NaN | NaN |
| NaN | principal.process.parent.file.sha1 | target.process.parent.file.sha1 | NaN | NaN | NaN |
| NaN | principal.process.parent.file.sha256 | target.process.parent.file.sha256 | NaN | NaN | NaN |
| NaN | principal.process.parent.file.tlsh | target.process.parent.file.tlsh | NaN | NaN | NaN |
| NaN | principal.process.parent.file.uuid | target.process.parent.file.uuid | NaN | NaN | NaN |
| NaN | principal.process.parent.file.internal\_name | target.process.parent.file.internal\_name | NaN | NaN | NaN |
| NaN | principal.process.parent.file.modification\_time | target.process.parent.file.modification\_time | NaN | NaN | NaN |
| NaN | principal.process.parent.file.reputation | target.process.parent.file.reputation | NaN | NaN | NaN |
| NaN | principal.process.parent.modified\_time | target.process.parent.modified\_time | NaN | NaN | NaN |
| NaN | principal.process.parent.pid | target.process.parent.pid | NaN | NaN | NaN |
| NaN | principal.process.parent.user\_uuid | target.process.parent.user\_uuid | NaN | NaN | NaN |
| NaN | principal.process.parent.uuid | target.process.parent.uuid | NaN | NaN | NaN |
| NaN | principal.registry.owner.display\_name | target.registry.owner.display\_name | NaN | NaN | NaN |
| NaN | principal.registry.owner.domain | target.registry.owner.domain | NaN | NaN | NaN |
| NaN | principal.registry.owner.email\_addresses | target.registry.owner.email\_addresses | NaN | NaN | NaN |
| NaN | principal.registry.owner.id | target.registry.owner.id | NaN | NaN | NaN |
| NaN | principal.registry.owner.username | target.registry.owner.username | NaN | NaN | NaN |
| NaN | principal.registry.owner.uuid | target.registry.owner.uuid | NaN | NaN | NaN |
| NaN | principal.registry.owner.permmisions.description | target.registry.owner.permmisions.description | NaN | NaN | NaN |
| NaN | principal.registry.owner.permmisions.id | target.registry.owner.permmisions.id | NaN | NaN | NaN |
| NaN | principal.registry.owner.permmisions.name | target.registry.owner.permmisions.name | NaN | NaN | NaN |
| NaN | principal.resource.id | target.resource.id | NaN | NaN | NaN |
| NaN | principal.resource.name | target.resource.name | NaN | NaN | NaN |
| NaN | principal.resource.type | target.resource.type | NaN | NaN | NaN |
| NaN | principal.resource.parent.id | target.resource.parent.id | NaN | NaN | NaN |
| NaN | principal.resource.parent.name | target.resource.parent.name | NaN | NaN | NaN |
| NaN | principal.resource.parent.type | target.resource.parent.type | NaN | NaN | NaN |
| NaN | principal.url.domain\_name | target.url.domain\_name | NaN | NaN | NaN |
| NaN | principal.url.url\_path | target.url.url\_path | NaN | NaN | NaN |
| NaN | principal.url.uuid | target.url.uuid | NaN | NaN | NaN |
| NaN | principal.url.reputation | target.url.reputation | NaN | NaN | NaN |
| NaN | principal.user.display\_name | target.user.display\_name | NaN | NaN | NaN |
| NaN | principal.user.domain | target.user.domain | NaN | NaN | NaN |
| NaN | principal.user.email\_address | target.user.email\_address | NaN | NaN | NaN |
| NaN | principal.user.id | target.user.id | NaN | NaN | NaN |
| NaN | principal.usename | target.usename | NaN | NaN | NaN |
| NaN | principal.user.uuid | target.user.uuid | NaN | NaN | NaN |
| NaN | principal.user.permmisions.description | target.user.permmisions.description | NaN | NaN | NaN |
| NaN | principal.user.permmisions.id | target.user.permmisions.id | NaN | NaN | NaN |
| NaN | principal.user.permmisions.name | target.user.permmisions.name | NaN | NaN | NaN |

## correlation- FIELDS PATH
| metadata | principal | target | network | email |
| --- | --- | --- | --- | --- |
| metadata.event\_id | principal.asset.domain | target.asset.domain | network.conn\_end\_time | email.attachment.creation\_time |
| metadata.event\_subtype | principal.asset.type | target.asset.type | network.conn\_start\_time | email.attachment.sha256 |
| metadata.event\_type | principal.asset.ip\_address.address | target.asset.ip\_address.address | network.conn\_first\_seen | email.attachment.tlsh |
| metadata.severity | principal.asset.name | target.asset.name | network.dns\_query\_uuid | email.attachment.uuid |
| metadata.severity\_details | principal.asset.uuid | target.asset.uuid | network.dns.resolver.address | email.attachment..internal\_name |
| metadata.timestamp | principal.file.creation\_time | target.file.creation\_time | network.dns.resolver.reputation | email.attachment.reputation |
| metadata.type | principal.file.sha256 | target.file.sha256 | network.session\_id | email.links.domain\_name |
| metadata.uuid | principal.file.tlsh | target.file.tlsh | NaN | email.links.url\_path |
| NaN | principal.file.uuid | target.file.uuid | NaN | email.links.uuid |
| NaN | principal.file.internal\_name | target.file.internal\_name | NaN | email.links.reputation |
| NaN | principal.group.name | target.group.name | NaN | email.message\_id |
| NaN | principal.nat\_ip.address | target.nat\_ip.address | NaN | email.recipients |
| NaN | principal.NetworkInterface.address.address | target.NetworkInterface.address.address | NaN | email.sender |
| NaN | principal.NetworkInterface.id | target.NetworkInterface.id | NaN | NaN |
| NaN | principal.NetworkInterface.name | target.NetworkInterface.name | NaN | NaN |
| NaN | principal.process.creation\_time | target.process.creation\_time | NaN | NaN |
| NaN | principal.process.file.creation\_time | target.process.file.creation\_time | NaN | NaN |
| NaN | principal.process.file.sha256 | target.process.file.sha256 | NaN | NaN |
| NaN | principal.process.file.tlsh | target.process.file.tlsh | NaN | NaN |
| NaN | principal.process.file.uuid | target.process.file.uuid | NaN | NaN |
| NaN | principal.process.file.internal\_name | target.process.file.internal\_name | NaN | NaN |
| NaN | principal.process.pid | target.process.pid | NaN | NaN |
| NaN | principal.process.user\_uuid | target.process.user\_uuid | NaN | NaN |
| NaN | principal.process.uuid | target.process.uuid | NaN | NaN |
| NaN | principal.process.parent.creation\_time | target.process.parent.creation\_time | NaN | NaN |
| NaN | principal.process.parent.file.sha256 | target.process.parent.file.sha256 | NaN | NaN |
| NaN | principal.process.parent.file.tlsh | target.process.parent.file.tlsh | NaN | NaN |
| NaN | principal.process.parent.file.uuid | target.process.parent.file.uuid | NaN | NaN |
| NaN | principal.process.parent.file.internal\_name | target.process.parent.file.internal\_name | NaN | NaN |
| NaN | principal.process.parent.pid | target.process.parent.pid | NaN | NaN |
| NaN | principal.process.parent.user\_uuid | target.process.parent.user\_uuid | NaN | NaN |
| NaN | principal.process.parent.uuid | target.process.parent.uuid | NaN | NaN |
| NaN | principal.registry.owner.domain | target.registry.owner.domain | NaN | NaN |
| NaN | principal.registry.owner.email\_addresses | target.registry.owner.email\_addresses | NaN | NaN |
| NaN | principal.registry.owner.username | target.registry.owner.username | NaN | NaN |
| NaN | principal.registry.owner.uuid | target.registry.owner.uuid | NaN | NaN |
| NaN | principal.url.domain\_name | target.url.domain\_name | NaN | NaN |
| NaN | principal.url.url\_path | target.url.url\_path | NaN | NaN |
| NaN | principal.url.uuid | target.url.uuid | NaN | NaN |
| NaN | principal.url.reputation | target.url.reputation | NaN | NaN |
| NaN | principal.user.domain | target.user.domain | NaN | NaN |
| NaN | principal.user.email\_address | target.user.email\_address | NaN | NaN |
| NaN | principal.usename | target.usename | NaN | NaN |
| NaN | principal.user.uuid | target.user.uuid | NaN | NaN |

## network.application_protocol en
| AFP |
| --- |
| AMQP |
| APPC |
| ATOM |
| BEEP |
| BIT\_TORRENT |
| BITCOIN |
| CFDP |
| CIP |
| COAP |
| COTP |
| DCERPC |
| DDS |
| DEVICE\_NET |
| DHCP |
| DICOM |
| DNP3 |
| DNS |
| E\_DONKEY |
| ENRP |
| FAST\_TRACK |
| FINGER |
| FREENET |
| FTAM |
| GOOSE |
| GOPHER |
| GRPC |
| H323 |
| HL7 |
| HTTP |
| HTTPS |
| IEC104 |
| IRCP |
| KADEMLIA |
| KRB5 |
| LDAP |
| LPD |
| MIME |
| MMS |
| MODBUS |
| MQTT |
| NETCONF |
| NFS |
| NIS |
| NNTP |
| NTCIP |
| NTP |
| OSCAR |
| PNRP |
| PTP |
| QUIC |
| RDP |
| RELP |
| RIP |
| RLOGIN |
| RPC |
| RTMP |
| RTP |
| RTPS |
| RTSP |
| SAP |
| SDP |
| SIP |
| SLP |
| SMB |
| SMTP |
| SNMP |
| SNTP |
| SSH |
| SSMS |
| STYX |
| SV |
| TCAP |
| TDS |
| TOR |
| TSP |
| UNKNOWN |
| VTP |
| WEB\_DAV |
| WHOIS |
| X400 |
| X500 |
| XMPP |

## metadat.event_type enum list
| EMAIL\_TRANSACTION |
| --- |
| EMAIL\_DETECTION? |
| EMAIL\_UNCATEGORIZED |
| FILE\_COPY |
| FILE\_CREATION |
| FILE\_DELETION |
| FILE\_DETECTION |
| FILE\_MODIFICATION |
| FILE\_MOVE |
| FILE\_OPEN |
| FILE\_READ |
| FILE\_SCAN |
| FILE\_SYNC |
| FILE\_UNCATEGORIZED |
| GENERIC\_EVENT |
| GROUP\_CREATION |
| GROUP\_DELETION |
| GROUP\_MODIFICATION |
| GROUP\_UNCATEGORIZED |
| MUTEX\_CREATION |
| MUTEX\_UNCATEGORIZED |
| NETWORK\_CONNECTION |
| NETWORK\_DETECTION |
| NETWORK\_UNCATEGORIZED |
| NETWORK\_HOST\_SCAN |
| NETWORK\_VULN\_SCAN |
| PROCESS\_CREATION |
| PROCESS\_DETECTION |
| PROCESS\_INJECTION |
| PROCESS\_MODULE\_LOAD |
| PROCESS\_OPEN |
| PROCESS\_SCAN |
| PROCESS\_TERMINATION |
| PROCESS\_UNCATEGORIZED |
| REGISTRY\_CREATION |
| REGISTRY\_DELETION |
| REGISTRY\_DETECTION |
| REGISTRY\_MODIFICATION |
| REGISTRY\_UNCATEGORIZED |
| RESOURCE\_CREATION |
| RESOURCE\_DELETION |
| RESOURCE\_DETECTION |
| RESOURCE\_PERMISSIONS\_CHANGE |
| RESOURCE\_READ |
| RESOURCE\_WRITE |
| RESOURCE\_UNCATEGORIZED |
| SCHEDULED\_TASK\_CREATION |
| SCHEDULED\_TASK\_DELETION |
| SCHEDULED\_TASK\_DISABLE |
| SCHEDULED\_TASK\_ENABLE |
| SCHEDULED\_TASK\_MODIFICATION |
| SCHEDULED\_TASK\_UNCATEGORIZED |
| SERVICE\_CREATION |
| SERVICE\_DELETION |
| SERVICE\_MODIFICATION |
| SERVICE\_START |
| SERVICE\_STOP |
| SERVICE\_UNSPECIFIED |
| SETTING\_CREATION |
| SETTING\_DELETION |
| SETTING\_MODIFICATION |
| SETTING\_UNCATEGORIZED |
| STATUS\_HEARTBEAT |
| STATUS\_SHUTDOWN |
| STATUS\_STARTUP |
| STATUS\_UNCATEGORIZED |
| STATUS\_UPDATE |
| SYSTEM\_AUDIT\_LOG\_UNCATEGORIZED |
| SYSTEM\_AUDIT\_LOG\_WIPE |
| USER\_CHANGE\_PASSWORD |
| USER\_CHANGE\_PERMISSIONS |
| USER\_COMMUNICATION |
| USER\_CREATION |
| USER\_DELETION |
| USER\_DETECTION |
| USER\_LOGIN |
| USER\_LOGOUT |
| USER\_UNCATEGORIZED |

## resource.type enum list
| APPLICATION |
| --- |
| BACKEND\_SERVICE |
| CLOUD\_PROJECT |
| CLUSTER |
| CONTAINER |
| DATABASE |
| DATASET |
| FUNCTION |
| LOAD\_BALANCER |
| MAILBOX\_FOLDER |
| MUTEX |
| PIPE |
| POD |
| REPOSITORY |
| SENSOR |
| SETTING |
| SNAPSHOT |
| STORAGE\_BUCKET |
| STORAGE\_OBJECT |
| SUBNET |
| TABLE |
| TASK |
| UNSPECIFIED |
| VOLUME |
| VPC\_NETWORK |
