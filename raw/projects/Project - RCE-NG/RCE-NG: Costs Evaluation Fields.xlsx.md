# RCE-NG: Costs Evaluation Fields.xlsx

## General
| customer | num of endpoints | total number of integration | the integration | total events per month may | detection alerts per month may | detection alerts per day on avg | the number of  potential correlation in 24 h | potential group (events) max size  per 24 h | potential group (events) avg size | tokens per event | prompt size tokens (MAX) | INPUT tokens per average potenital group | estimated OUPUT tokens per single potential group | [GPT-4o] $ cost per 1M INPUT tokens | [GPT-4o] $ cost per 1M OUTPUT tokens | [GPT-5] $ cost per 1M INPUT tokens | [GPT-5] $ cost per 1M OUTPUT tokens | [GPT-4o] cost per single correlation group | [GPT-5] cost per single correlation group | [GPT-4o] cost per avg correlation groups in 24h - Single Customer | [GPT-5] cost per avg correlation groups in 24h - Single Customer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ccbji1 | 16363 | 8.0 | Cisco Umbrella\nCybereason MTD\nCisco ASA\nMicrosoft Graph API Alerts\nAzure AD Directory Audit\nOffice 365\nMicrosoft SharePoint\nAWS Cloudtrail | 6.360272e+09 | 540218 | 18007.26667 | 50 | 419.0 | 58.0 | 250.0 | 550.0 | 15050.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.07925 | 0.020813 | 3.96250 | 1.040625 |
| aeonfanta | 1946 | 5.0 | FortiGate\nPalo Alto Networks Firewall\nWorkspace Activities\nWorkspace Alerts\nCybereason MTD | 3.475974e+09 | 25481 | 849.366667 | 6 | 321.0 | 142.0 | 250.0 | 550.0 | 36050.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.18425 | 0.047063 | 1.10550 | 0.282375 |
| misumi-group | 12601 | 1.0 | CATO Networks | 1.329882e+09 | 102514 | 3417.133333 | 10 | 120.0 | 17.0 | 250.0 | 550.0 | 4800.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.02800 | 0.008000 | 0.28000 | 0.080000 |
| taiyo-sec-global | 2950 | 8.0 | Windows Event\nCisco Umbrella\nCisco Meraki\nMicrosoft Graph API Alerts\nFortiGate\nMicrosoft SharePoint\nOffice 365\nAzure AD Directory Audit | 1.218303e+09 | 8450 | 281.666667 | 19 | 30.0 | 6.0 | 250.0 | 550.0 | 2050.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01425 | 0.004562 | 0.27075 | 0.086688 |
| yorozu | 2627 | 1.0 | FortiGate | 8.930971e+08 | 367 | 12.233333 | 1 | 4.0 | 4.0 | 250.0 | 550.0 | 1550.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01175 | 0.003938 | 0.01175 | 0.003938 |
| satake | 1858 | 1.0 | FortiGate | 5.760025e+08 | 302 | 10.066667 | 3 | 4.0 | 3.0 | 250.0 | 550.0 | 1300.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01050 | 0.003625 | 0.03150 | 0.010875 |
| tfr | NaN | 8.0 | Azure AD Directory Audit\nOffice 365 \nMicrosoft SharePoint\nFortiGate\nZScaler\nPalo Alto Networks Firewall\nWindows Event\nMicrosoft Graph API Alerts | 5.381329e+08 | 2408 | 80.266667 | 7 | 12.0 | 6.0 | 250.0 | 550.0 | 2050.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01425 | 0.004562 | 0.09975 | 0.031938 |
| tsuchiya | 2103 | 1.0 | FortiGate | 3.859943e+08 | 3711 | 123.7 | 10 | 73.0 | 17.0 | 250.0 | 550.0 | 4800.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.02800 | 0.008000 | 0.28000 | 0.080000 |
| pasconet | 1526 | 5.0 | Cisco Meraki\nAWS Cloudtrail\nWorkspace Activities\nWorkspace Alerts\nCisco Umbrella | 4.173467e+07 | 1784 | 59.466667 | 3 | 24.0 | 10.0 | 250.0 | 550.0 | 3050.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01925 | 0.005812 | 0.05775 | 0.017438 |
| openhouse | 5835 | 1.0 | AWS Cloudtrail | 7.203820e+06 | 5276 | 175.866667 | 2 | 7.0 | 5.0 | 250.0 | 550.0 | 1800.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01300 | 0.004250 | 0.02600 | 0.008500 |
| sws | 35624 | 2.0 | Palo Alto Networks Firewall\nNetwork Security Platform | 8.042050e+05 | 204316 | 6810.533333 | 52 | 781.0 | 58.0 | 250.0 | 550.0 | 15050.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.07925 | 0.020813 | 4.12100 | 1.082250 |
| toa | 392 | 3.0 | Cybereason MTD\nWorkspace Activities \nWorkspace Alerts\n | 1.656040e+05 | 704 | 23.466667 | 18 | 4.0 | 3.0 | 250.0 | 550.0 | 1300.0 | 200 | 5 | 20.00 | 1.25 | 10.0 | 0.01050 | 0.003625 | 0.18900 | 0.065250 |
| NaN | NaN | 44.0 | NaN | 1.482757e+10 | 895531 | 29851.03333 | 181 | 1799.0 | NaN | NaN | NaN | NaN | NaN | 60 | 240.00 | NaN | NaN | 0.49225 | 0.135063 | 10.43550 | 2.789875 |
| NaN | https://lookerstudio.google.com/u/0/reporting/44b8a202-4ee1-473a-9c82-023db280cc4e/page/T3cWC | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | GPT 4 | GPT 5 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | W/O any optimization/filter gate 24h | 14694.17116 | 4031.75519 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | OpenAI Costs | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | OpenAI Tokenizer | [GPT-4o] $ cost per 1M INPUT tokens | 5.00 | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | [GPT-5] $ cost per 1M INPUT tokens | 1.25 | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | [GPT-4o] $ cost per 1M OUTPUT tokens | 20.00 | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | [GPT-5] $ cost per 1M OUTPUT tokens | 10.00 | NaN | NaN | NaN | NaN | NaN | NaN |

## events per month
| customerIdentifier | count |
| --- | --- |
| aeonfanta | 3475974093 |
| anx24 | 1858817 |
| ccbji1 | 6360271899 |
| customer-daiichi | 109144819 |
| fuchu-edu | 183521049 |
| gifucityedu | 18372033 |
| hagiwara | 1159688 |
| hli-g | 321824444 |
| htec | 113313909 |
| igits-sv001yt | 114615621 |
| iijglobal-lab | 41814948 |
| infra-2022 | 105888817 |
| japan-xdr-prod-test11 | 31771 |
| japan-xdr-prod-test12 | 31728 |
| japanet | 1803347342 |
| jmu | 2131485904 |
| jp-xdr-uat | 45326 |
| juro0153 | 212620403 |
| jwacredr | 3787549724 |
| kyfo12 | 61529677 |
| misumi-group | 1329882136 |
| naisnet | 677714615 |
| necf-nfr | 11487 |
| nesic-nfr | 57398 |
| nipro | 228992502 |
| ns1566 | 32000149 |
| openhouse | 7203820 |
| pasconet | 41734673 |
| peach | 13611416 |
| satake | 576002511 |
| sb-xdr-uat | 5007 |
| scsk-xdr-poc-jp1 | 151248 |
| secdso2003 | 26938 |
| shimagin | 29995563 |
| soltechwest1 | 2405 |
| sws | 804205 |
| szgp | 646187703 |
| taiyo-sec-global | 1218302784 |
| tden-cr-nfr | 92726 |
| tfr | 538132865 |
| toa | 165604 |
| tokai-kyowa | 33693669 |
| tsuchiya | 385994333 |
| valqua-japan | 208099135 |
| xdr-handson-demo | 31700 |
| xdr-handson-jp | 33767 |
| yorozu | 893097092 |
| NaN | NaN |
| NaN | NaN |
| query | statsby\n  count(),\n  group\_by(\n    customerIdentifier\n  ) |

## detections per month
| customer\_id | event\_count |
| --- | --- |
| 661ccfd9b126238d1fb0813f | 567 |
| aeonfanta | 25481 |
| airdo | 8 |
| anx24 | 101 |
| apac-sdr-demo | 2 |
| ccbji1 | 540218 |
| crjse-sdr-poc | 242 |
| crkk-cs3 | 105 |
| crkktc-23-1-441 | 73 |
| customer-daiichi | 58 |
| diffeve | 6 |
| fuchu-edu | 176 |
| gifucityedu | 2636 |
| hagiwara | 821 |
| hli-g | 1656 |
| htec | 562 |
| igits-sv001yt | 124 |
| iijglobal-lab | 39850 |
| infra-2022 | 63 |
| japanet | 7173 |
| jmu | 656 |
| jp-xdr-uat | 3261 |
| juro0153 | 396 |
| jwacredr | 4748 |
| kanakan | 8 |
| kfpc | 7 |
| kyfo12 | 13 |
| marudai | 34 |
| mecnfr | 3 |
| misumi-group | 102514 |
| naisnet | 12 |
| necf-nfr | 61 |
| nesic-nfr | 2 |
| nipro | 338189 |
| ns1566 | 24 |
| openhouse | 5276 |
| pasconet | 1784 |
| peach | 97 |
| pt-systema-nfr | 2189 |
| qa-232460 | 34 |
| satake | 302 |
| scsk-xdr-poc-jp1 | 523 |
| secdso2003 | 18 |
| shimagin | 10 |
| soltechwest1 | 24 |
| sws | 204316 |
| szgp | 181714 |
| tachun | 20 |
| taiyo-sec-global | NaN |
| takuma | 547 |
| tden-cr-nfr | 4 |
| tfr | 2408 |
| toa | 704 |
| tokai-kyowa | 11 |
| towayakuhin | 2 |
| tsuchiya | 3711 |
| valqua-japan | 4420 |
| vup-education123 | 8 |
| xdr-handson-jp | 35 |
| ykkkorea | 410 |
| yorozu | 367 |
| NaN | NaN |
| Query | SELECT \n  s.customer\_id,\n  COUNT(\*) AS event\_count\nFROM sa.alert AS a\nJOIN sa.suspicious\_event AS s ON a.id = s.alert\_id\nWHERE detection\_time BETWEEN '2025-05-01 00:00:00' AND '2025-06-01 00:00:00' \n  AND event->>'tactic' IS NOT NULL\nGROUP BY s.customer\_id; |

## Integrations
| Customer | Region | Integration | Integration Type | Vendor | Product | Status |
| --- | --- | --- | --- | --- | --- | --- |
| aeonfanta | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| aeonfanta | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| aeonfanta | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| aeonfanta | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| anx24 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| anx24 | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| anx24 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| anx24 | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| ccbji1 | APAC | CISCO Umbrella API - Proxy | PULLER | Cisco | Cisco Umbrella | READY |
| ccbji1 | APAC | CISCO Umbrella API - Intrusion | PULLER | Cisco | Cisco Umbrella | READY |
| ccbji1 | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| ccbji1 | APAC | CISCO Umbrella API - Firewall | PULLER | Cisco | Cisco Umbrella | READY |
| ccbji1 | APAC | CISCO Umbrella API - DNS | PULLER | Cisco | Cisco Umbrella | READY |
| ccbji1 | APAC | Cisco ASA Firewall TCP | PUSHER | Cisco | Cisco ASA | READY |
| ccbji1 | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| ccbji1 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| ccbji1 | APAC | AWS CloudTrail | PULLER | AWS | AWS Cloudtrail | READY |
| crjse-sdr-poc | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| crjse-sdr-poc | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| crjse-sdr-poc | APAC | Lanscope Endpoint Manager | PUSHER | Lanscope | Endpoint Manager | READY |
| crjse-sdr-poc | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| crjse-sdr-poc | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| crkk-cs3 | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| crkk-cs3 | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| crkk-cs3 | APAC | Windows AD | PUSHER | Microsoft | Microsoft AD | READY |
| customer-daiichi | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| fuchu-edu | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| gifucityedu | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| gifucityedu | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| gifucityedu | APAC | Box Enterprise Events | PULLER | Box | Box Content Management | READY |
| gifucityedu | APAC | Palo Alto Cortex Data Lake - Syslog | PUSHER | Palo Alto | Cortex Data Lake | READY |
| hagiwara | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| hagiwara | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| hagiwara | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| hagiwara | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| hagiwara | APAC | Box Enterprise Events | PULLER | Box | Box Content Management | READY |
| hagiwara | APAC | Hennge One | PULLER | Hennge | One | READY |
| hagiwara | APAC | CATO Networks SASE Cloud | PULLER | CATO Networks | SASE Cloud | READY |
| hli-g | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| hli-g | APAC | CISCO Meraki | PUSHER | Cisco | Cisco Meraki | READY |
| htec | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| htec | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| htec | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| igits-sv001yt | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| igits-sv001yt | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| igits-sv001yt | APAC | CISCO Meraki | PUSHER | Cisco | Cisco Meraki | READY |
| iijglobal-lab | APAC | Zscaler ZPA AppProtection | PUSHER | ZScaler | ZScaler ZPA | READY |
| iijglobal-lab | APAC | Zscaler ZPA Audit Logs | PUSHER | ZScaler | ZScaler ZPA | READY |
| iijglobal-lab | APAC | Zscaler ZPA Browser Access | PUSHER | ZScaler | ZScaler ZPA | READY |
| iijglobal-lab | APAC | Zscaler ZPA User Activity | PUSHER | ZScaler | ZScaler ZPA | READY |
| iijglobal-lab | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| iijglobal-lab | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| iijglobal-lab | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| iijglobal-lab | APAC | Palo Alto Cortex Data Lake - Syslog | PUSHER | Palo Alto | Cortex Data Lake | READY |
| iijglobal-lab | APAC | CATO Networks SASE Cloud | PULLER | CATO Networks | SASE Cloud | READY |
| iijglobal-lab | APAC | CATO Networks SASE Cloud | PULLER | CATO Networks | SASE Cloud | READY |
| infra-2022 | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| japan-xdr-prod-test11 | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| japan-xdr-prod-test12 | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| japanet | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| jmu | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| jmu | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| jmu | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| jp-xdr-uat | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| jp-xdr-uat | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| jp-xdr-uat | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| jp-xdr-uat | APAC | Windows AD | PUSHER | Microsoft | Microsoft AD | READY |
| jp-xdr-uat | APAC | CISCO Meraki | PUSHER | Cisco | Cisco Meraki | READY |
| jp-xdr-uat | APAC | Okta Identity and Audit | PULLER | Okta | Okta, Okta User Context, Okta Device Context | READY |
| jp-xdr-uat | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| jp-xdr-uat | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| jp-xdr-uat | APAC | Cisco ASA Firewall TCP | PUSHER | Cisco | Cisco ASA | READY |
| jp-xdr-uat | APAC | Cisco ASA Firewall | PUSHER | Cisco | Cisco ASA | READY |
| jp-xdr-uat | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| jp-xdr-uat | APAC | Zscaler ZPA AppProtection | PUSHER | ZScaler | ZScaler ZPA | READY |
| jp-xdr-uat | APAC | Sysdig Secure | PUSHER | Sysdig | Sysdig Secure | PENDING\_DELETE\_APPROVAL |
| jp-xdr-uat | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| jp-xdr-uat | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| jp-xdr-uat | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| jp-xdr-uat | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| jp-xdr-uat | APAC | Microsoft Defender for Endpoint Alerts | PULLER | Microsoft | Microsoft Defender for Endpoint | READY |
| jp-xdr-uat | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| jp-xdr-uat | APAC | Watchguard FireboxV | PUSHER | Watchguard | FireboxV | READY |
| jp-xdr-uat | APAC | Azure Monitor Activity Logs | PULLER | Microsoft | Azure Monitor | ERROR |
| jp-xdr-uat | APAC | Sysdig Secure | PUSHER | Sysdig | Sysdig Secure | READY |
| jp-xdr-uat | APAC | Azure AD Signin Logs | PULLER | Microsoft | Azure AD | ERROR |
| jp-xdr-uat | APAC | Trellix IPS | PUSHER | Trellix | Network Security Platform | READY |
| jp-xdr-uat | APAC | Sysdig Secure | PUSHER | Sysdig | Sysdig Secure | READY |
| juro0153 | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| juro0153 | APAC | Zscaler ZIA Web | PUSHER | ZScaler | Zscaler | READY |
| juro0153 | APAC | Zscaler ZIA Firewall | PUSHER | ZScaler | ZScaler NGFW | READY |
| juro0153 | APAC | Zscaler ZIA SaaS Security Activity | PUSHER | ZScaler | Zscaler CASB | READY |
| juro0153 | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| juro0153 | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| juro0153 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| jwacredr | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| kyfo12 | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | PENDING\_REGISTRATION |
| kyfo12 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| kyfo12 | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| kyfo12 | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| mediatech | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| misumi-group | APAC | CATO Networks SASE Cloud | PULLER | CATO Networks | SASE Cloud | READY |
| naisnet | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| naisnet | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| necf-nfr | APAC | Box Enterprise Events | PULLER | Box | Box Content Management | ERROR |
| necf-nfr | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| necf-nfr | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| necf-nfr | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| necf-nfr | APAC | Azure Monitor Activity Logs | PULLER | Microsoft | Azure Monitor | READY |
| necf-nfr | APAC | Azure Monitor Activity Logs | PULLER | Microsoft | Azure Monitor | READY |
| nesic-nfr | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| nesic-nfr | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| nesic-nfr | APAC | CATO Networks SASE Cloud | PULLER | CATO Networks | SASE Cloud | READY |
| nesic-nfr | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| nipro | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| nipro | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| nipro | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| nipro | APAC | Cisco ASA Firewall | PUSHER | Cisco | Cisco ASA | READY |
| ns1566 | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| openhouse | APAC | AWS CloudTrail | PULLER | AWS | AWS Cloudtrail | READY |
| pasconet | APAC | CISCO Meraki | PUSHER | Cisco | Cisco Meraki | READY |
| pasconet | APAC | AWS CloudTrail | PULLER | AWS | AWS Cloudtrail | READY |
| pasconet | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| pasconet | APAC | Cisco Umbrella | PULLER | Cisco | Cisco Umbrella Audit, Cisco Umbrella DNS, Cisco Umbrella Web Proxy | ERROR |
| peach | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| satake | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| sb-xdr-uat | APAC | Zscaler ZIA Firewall | PUSHER | ZScaler | ZScaler NGFW | READY |
| sb-xdr-uat | APAC | Zscaler ZIA SaaS Security Activity | PUSHER | ZScaler | Zscaler CASB | READY |
| sb-xdr-uat | APAC | Zscaler ZIA Web | PUSHER | ZScaler | Zscaler | READY |
| sb-xdr-uat | APAC | Zscaler ZPA User Activity | PUSHER | ZScaler | ZScaler ZPA | READY |
| sb-xdr-uat | APAC | Zscaler ZPA Browser Access | PUSHER | ZScaler | ZScaler ZPA | READY |
| sb-xdr-uat | APAC | Zscaler ZPA AppProtection | PUSHER | ZScaler | ZScaler ZPA | READY |
| sb-xdr-uat | APAC | Zscaler ZPA Audit Logs | PUSHER | ZScaler | ZScaler ZPA | READY |
| sb-xdr-uat | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| sb-xdr-uat | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| scsk-xdr-poc-jp1 | APAC | Netskope SSE | PULLER | Netskope | Netskope SSE | READY |
| scsk-xdr-poc-jp1 | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| scsk-xdr-poc-jp1 | APAC | Box Enterprise Events | PULLER | Box | Box Content Management | ERROR |
| secdso2003 | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| secdso2003 | APAC | Zimperium Threat Events | PUSHER | Zimperium | Zimperium | READY |
| secdso2003 | APAC | Windows AD | PUSHER | Microsoft | Microsoft AD | READY |
| secdso2003 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| shimagin | APAC | Zscaler ZIA SaaS Security Activity | PUSHER | ZScaler | Zscaler CASB | READY |
| shimagin | APAC | Zscaler ZPA AppProtection | PUSHER | ZScaler | ZScaler ZPA | READY |
| shimagin | APAC | Zscaler ZPA Audit Logs | PUSHER | ZScaler | ZScaler ZPA | READY |
| shimagin | APAC | Zscaler ZPA Browser Access | PUSHER | ZScaler | ZScaler ZPA | READY |
| shimagin | APAC | Zscaler ZPA User Activity | PUSHER | ZScaler | ZScaler ZPA | READY |
| shimagin | APAC | Zscaler ZIA Web | PUSHER | ZScaler | Zscaler | READY |
| shimagin | APAC | Zscaler ZIA Firewall | PUSHER | ZScaler | ZScaler NGFW | READY |
| soltechwest1 | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| soltechwest1 | APAC | CATO Networks SASE Cloud | PULLER | CATO Networks | SASE Cloud | READY |
| soltechwest1 | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| soltechwest1 | APAC | Azure AD Signin Logs | PULLER | Microsoft | Azure AD | ERROR |
| soltechwest1 | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| soltechwest1 | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| sws | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| sws | APAC | Trellix IPS | PUSHER | Trellix | Network Security Platform | READY |
| szgp | APAC | Palo Alto Cortex Data Lake - Syslog | PUSHER | Palo Alto | Cortex Data Lake | READY |
| szgp | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| taiyo-sec-global | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| taiyo-sec-global | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| taiyo-sec-global | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| taiyo-sec-global | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| taiyo-sec-global | APAC | CISCO Meraki | PUSHER | Cisco | Cisco Meraki | READY |
| taiyo-sec-global | APAC | CISCO Umbrella API - DNS | PULLER | Cisco | Cisco Umbrella | READY |
| taiyo-sec-global | APAC | CISCO Umbrella API - Firewall | PULLER | Cisco | Cisco Umbrella | READY |
| taiyo-sec-global | APAC | CISCO Umbrella API - Intrusion | PULLER | Cisco | Cisco Umbrella | READY |
| taiyo-sec-global | APAC | CISCO Umbrella API - Proxy | PULLER | Cisco | Cisco Umbrella | READY |
| tden-cr-nfr | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| tden-cr-nfr | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| tden-cr-nfr | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| tfr | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| tfr | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| tfr | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| tfr | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| tfr | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| tfr | APAC | Zscaler ZIA Firewall | PUSHER | ZScaler | ZScaler NGFW | READY |
| tfr | APAC | Zscaler ZIA SaaS Security Activity | PUSHER | ZScaler | Zscaler CASB | READY |
| tfr | APAC | Zscaler ZIA Web | PUSHER | ZScaler | Zscaler | READY |
| tfr | APAC | Zscaler ZPA AppProtection | PUSHER | ZScaler | ZScaler ZPA | READY |
| tfr | APAC | Zscaler ZPA Audit Logs | PUSHER | ZScaler | ZScaler ZPA | READY |
| tfr | APAC | Zscaler ZPA Browser Access | PUSHER | ZScaler | ZScaler ZPA | READY |
| tfr | APAC | Zscaler ZPA User Activity | PUSHER | ZScaler | ZScaler ZPA | READY |
| toa | APAC | Cybereason MTD | PUSHER | Cybereason | Cybereason MTD | READY |
| toa | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| tokai-kyowa | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| tsuchiya | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| valqua-japan | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| xdr-handson-demo | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| xdr-handson-demo | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| xdr-handson-jp | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | READY |
| xdr-handson-jp | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | READY |
| xdr-handson-jp | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| xdr-japan-test | APAC | Windows AD | PUSHER | Microsoft | Microsoft AD | READY |
| xdr-japan-test | APAC | Okta Identity and Audit | PULLER | Okta | Okta, Okta Device Context, Okta User Context | READY |
| xdr-japan-test | APAC | JAMF Threat Event Stream | PUSHER | JAMF | JAMF Threat Events | READY |
| xdr-japan-test | APAC | JAMF Network Traffic | PUSHER | JAMF | JAMF Network Traffic | READY |
| xdr-japan-test | APAC | Zscaler Cloud NSS For Web | PUSHER | ZScaler | Zscaler | READY |
| xdr-japan-test | APAC | Zscaler Cloud NSS For Firewall | PUSHER | ZScaler | ZScaler NGFW | READY |
| xdr-japan-test | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| xdr-japan-test | APAC | Zscaler ZIA SaaS Security Activity | PUSHER | ZScaler | Zscaler CASB | READY |
| xdr-japan-test | APAC | Lacework Alerts | PUSHER | Lacework | Lacework Cloud Security | READY |
| xdr-japan-test | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |
| xdr-japan-test | APAC | Zimperium User Activity | PUSHER | Zimperium | Zimperium | READY |
| xdr-japan-test | APAC | Zimperium Threat Events | PUSHER | Zimperium | Zimperium | READY |
| xdr-japan-test | APAC | CISCO Meraki | PUSHER | Cisco | Cisco Meraki | READY |
| xdr-japan-test | APAC | Zscaler ZPA User Activity | PUSHER | ZScaler | ZScaler ZPA | READY |
| xdr-japan-test | APAC | Cisco ASA Firewall | PUSHER | Cisco | Cisco ASA | READY |
| xdr-japan-test | APAC | Cisco AMP | PUSHER | Cisco | Cisco AMP | READY |
| xdr-japan-test | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| xdr-japan-test | APAC | CISCO Meraki socket | PUSHER | Cisco | Cisco Meraki | READY |
| xdr-japan-test | APAC | kuki | PUSHER | Cisco | Cisco Meraki | READY |
| xdr-japan-test | APAC | Palo Alto Cortex Data Lake - Syslog | PUSHER | Palo Alto | Cortex Data Lake | READY |
| xdr-japan-test | APAC | OneLogin SSO | PUSHER | One Identity | OneLogin SSO | READY |
| xdr-japan-test | APAC | Slack Enterprise Audit | PULLER | Slack | Slack Audit | READY |
| xdr-japan-test | APAC | Slack Enterprise Audit | PULLER | Slack | Slack Audit | READY |
| xdr-japan-test | APAC | Windows Events | PUSHER | Microsoft | Windows Event | READY |
| xdr-japan-test | APAC | do not use - Sysdig Secure test | PUSHER | Sysdig | Sysdig Secure | READY |
| xdr-japan-test | APAC | Cisco ASA Firewall | PUSHER | Cisco | Cisco ASA | READY |
| xdr-japan-test | APAC | Google Workspace and Alerts Center | PULLER | Google | Workspace Activities, Workspace Alerts | READY |
| xdr-japan-test | APAC | Cisco ASA Firewall TCP | PUSHER | Cisco | Cisco ASA | READY |
| xdr-japan-test | APAC | Sysdig Secure | PUSHER | Sysdig | Sysdig Secure | READY |
| xdr-japan-test | APAC | Hennge One | PULLER | Hennge | One | ERROR |
| xdr-japan-test | APAC | Rapid7 InsightVM | PULLER | Rapid7 | Rapid7 Insight | READY |
| xdr-japan-test | APAC | M365 and Azure AD Audit | PULLER | Azure, Microsoft 365, Microsoft | Azure AD Directory Audit, Office 365, Microsoft SharePoint | PENDING\_DELETE\_APPROVAL |
| xdr-japan-test | APAC | Azure AD Identity and Risk Detections | PULLER | Microsoft | Microsoft Graph API Alerts | PENDING\_DELETE\_APPROVAL |
| xdr-japan-test | APAC | Qualys VMDR | PULLER | Qualys | VMDR | READY |
| xdr-japan-test | APAC | Dropbox Team Audit Logs - token | PULLER | Dropbox | Dropbox | READY |
| xdr-japan-test | APAC | Palo Alto Firewall | PUSHER | Palo Alto | Palo Alto Networks Firewall | READY |
| yorozu | APAC | Fortigate Firewall | PUSHER | Fortinet | FortiGate | READY |

## events per data source
| customerIdentifier | product | count |
| --- | --- | --- |
| aeonfanta | cybereason mtd | 174 |
| aeonfanta | palo alto networks firewall | 3471057698 |
| aeonfanta | workspace activities | 4916221 |
| anx24 | azure ad directory audit | 64741 |
| anx24 | azure active directory audit | 102571 |
| anx24 | microsoft sharepoint | 809935 |
| anx24 | office 365 | 881570 |
| ccbji1 | cisco umbrella | 4784029169 |
| ccbji1 | microsoft graph api alerts | 371 |
| ccbji1 | cybereason mtd | 16120 |
| ccbji1 | azure active directory audit | 10360725 |
| ccbji1 | azure ad directory audit | 8769139 |
| ccbji1 | microsoft sharepoint | 82129694 |
| ccbji1 | aws cloudtrail | 17943194 |
| ccbji1 | office 365 | 47371842 |
| ccbji1 | cisco asa | 1409651645 |
| customer-daiichi | fortigate | 109144819 |
| fuchu-edu | fortigate | 183521049 |
| gifucityedu | cortex data lake | 2107543 |
| gifucityedu | microsoft sharepoint | 15442508 |
| gifucityedu | office 365 | 47741 |
| gifucityedu | azure active directory audit | 579069 |
| gifucityedu | azure ad directory audit | 194420 |
| gifucityedu | box content management | 734 |
| gifucityedu | microsoft graph api alerts | 18 |
| hagiwara | microsoft sharepoint | 245132 |
| hagiwara | office 365 | 795310 |
| hagiwara | box content management | 11823 |
| hagiwara | sase cloud | 118 |
| hagiwara | azure active directory audit | 84701 |
| hagiwara | azure ad directory audit | 16796 |
| hagiwara | one | 5808 |
| hli-g | fortigate | 321824444 |
| htec | microsoft sharepoint | 1032271 |
| htec | office 365 | 316393 |
| htec | microsoft graph api alerts | 2 |
| htec | azure active directory audit | 91149 |
| htec | azure ad directory audit | 61413 |
| htec | fortigate | 111812681 |
| igits-sv001yt | fortigate | 114615621 |
| iijglobal-lab | azure active directory audit | 12466 |
| iijglobal-lab | microsoft graph api alerts | 3 |
| iijglobal-lab | azure ad directory audit | 5170 |
| iijglobal-lab | office 365 | 8319 |
| iijglobal-lab | palo alto networks firewall | 41749885 |
| iijglobal-lab | microsoft sharepoint | 39105 |
| infra-2022 | fortigate | 105888817 |
| japan-xdr-prod-test11 | workspace activities | 31771 |
| japan-xdr-prod-test12 | workspace activities | 31728 |
| japanet | fortigate | 1803347342 |
| jmu | windows event | 2114517499 |
| jmu | microsoft graph api alerts | 3 |
| jmu | azure active directory audit | 265514 |
| jmu | azure ad directory audit | 516100 |
| jmu | office 365 | 7304774 |
| jmu | microsoft sharepoint | 8882014 |
| jp-xdr-uat | workspace activities | 31706 |
| jp-xdr-uat | cybereason mtd | 765 |
| jp-xdr-uat | azure ad directory audit | 373 |
| jp-xdr-uat | okta user context | 1054 |
| jp-xdr-uat | microsoft sharepoint | 11 |
| jp-xdr-uat | sysdig secure | 8820 |
| jp-xdr-uat | fortigate | 346 |
| jp-xdr-uat | okta | 551 |
| jp-xdr-uat | microsoft graph api alerts | 1 |
| jp-xdr-uat | azure active directory audit | 287 |
| jp-xdr-uat | office 365 | 1412 |
| juro0153 | workspace activities | 9086611 |
| juro0153 | workspace alerts | 3 |
| juro0153 | zscaler ngfw | 63471366 |
| juro0153 | zscaler | 140062423 |
| jwacredr | fortigate | 3787549724 |
| kyfo12 | microsoft sharepoint | 74956 |
| kyfo12 | office 365 | 668815 |
| kyfo12 | azure ad directory audit | 20710 |
| kyfo12 | windows event | 6453228 |
| kyfo12 | fortigate | 54298041 |
| kyfo12 | azure active directory audit | 13927 |
| misumi-group | sase cloud | 1329882136 |
| naisnet | microsoft sharepoint | 239712 |
| naisnet | fortigate | 677188101 |
| naisnet | azure ad directory audit | 119137 |
| naisnet | azure active directory audit | 25982 |
| naisnet | office 365 | 141683 |
| necf-nfr | azure monitor | 4467 |
| necf-nfr | microsoft sharepoint | 661 |
| necf-nfr | azure ad directory audit | 1473 |
| necf-nfr | office 365 | 3961 |
| necf-nfr | azure active directory audit | 925 |
| nesic-nfr | office 365 | 990 |
| nesic-nfr | sase cloud | 52913 |
| nesic-nfr | azure active directory audit | 2726 |
| nesic-nfr | azure ad directory audit | 332 |
| nesic-nfr | microsoft sharepoint | 437 |
| nipro | fortigate | 188829916 |
| nipro | palo alto networks firewall | 40159543 |
| nipro | cisco asa | 3043 |
| ns1566 | workspace activities | 32000143 |
| ns1566 | workspace alerts | 6 |
| openhouse | aws cloudtrail | 7203820 |
| pasconet | cisco umbrella audit | 1417 |
| pasconet | cisco meraki | 253 |
| pasconet | aws cloudtrail | 8034870 |
| pasconet | workspace alerts | 1388 |
| pasconet | workspace activities | 33696745 |
| peach | workspace activities | 13611336 |
| peach | workspace alerts | 80 |
| satake | fortigate | 576002511 |
| sb-xdr-uat | azure active directory audit | 888 |
| sb-xdr-uat | office 365 | 3819 |
| sb-xdr-uat | azure ad directory audit | 244 |
| sb-xdr-uat | microsoft sharepoint | 56 |
| scsk-xdr-poc-jp1 | netskope sse | 52346 |
| scsk-xdr-poc-jp1 | workspace activities | 98902 |
| secdso2003 | office 365 | 3460 |
| secdso2003 | azure active directory audit | 20669 |
| secdso2003 | cybereason mtd | 691 |
| secdso2003 | zimperium | 126 |
| secdso2003 | azure ad directory audit | 1855 |
| secdso2003 | microsoft sharepoint | 137 |
| shimagin | zscaler zpa | 849294 |
| shimagin | zscaler ngfw | 17810 |
| shimagin | zscaler | 29128459 |
| soltechwest1 | cybereason mtd | 321 |
| soltechwest1 | microsoft graph api alerts | 1 |
| soltechwest1 | microsoft sharepoint | 11 |
| soltechwest1 | office 365 | 1412 |
| soltechwest1 | azure ad directory audit | 373 |
| soltechwest1 | azure active directory audit | 287 |
| sws | network security platform | 804205 |
| szgp | cortex data lake | 646187703 |
| taiyo-sec-global | office 365 | 4708330 |
| taiyo-sec-global | microsoft sharepoint | 7670968 |
| taiyo-sec-global | azure ad directory audit | 471975 |
| taiyo-sec-global | windows event | 525190 |
| taiyo-sec-global | cisco umbrella | 894035730 |
| taiyo-sec-global | microsoft graph api alerts | 4 |
| taiyo-sec-global | azure active directory audit | 441145 |
| taiyo-sec-global | fortigate | 310448709 |
| taiyo-sec-global | cisco meraki | 733 |
| tden-cr-nfr | windows event | 87445 |
| tden-cr-nfr | workspace activities | 5281 |
| tfr | zscaler casb | 1 |
| tfr | microsoft sharepoint | 13402691 |
| tfr | office 365 | 2748409 |
| tfr | fortigate | 225291096 |
| tfr | azure ad directory audit | 653945 |
| tfr | microsoft graph api alerts | 71 |
| tfr | azure active directory audit | 1703686 |
| tfr | windows event | 61794508 |
| tfr | zscaler | 145323071 |
| tfr | zscaler ngfw | 5183708 |
| tfr | zscaler zpa | 82031679 |
| toa | workspace activities | 164412 |
| toa | cybereason mtd | 1191 |
| toa | workspace alerts | 1 |
| tokai-kyowa | fortigate | 33693669 |
| tsuchiya | fortigate | 385994333 |
| valqua-japan | fortigate | 208099135 |
| xdr-handson-demo | workspace activities | 31700 |
| xdr-handson-jp | azure active directory audit | 287 |
| xdr-handson-jp | microsoft sharepoint | 11 |
| xdr-handson-jp | office 365 | 1412 |
| xdr-handson-jp | azure ad directory audit | 373 |
| xdr-handson-jp | workspace activities | 31684 |
| yorozu | fortigate | 893097092 |

## Sheet7
| product |
| --- |
| aws cloudtrail |
| azure active directory audit |
| azure monitor |
| box content management |
| cisco asa |
| cisco meraki |
| cisco umbrella |
| cisco umbrella audit |
| cortex data lake |
| cybereason mtd |
| fortigate |
| microsoft graph api alerts |
| microsoft sharepoint |
| netskope sse |
| network security platform |
| office 365 |
| okta |
| okta user context |
| one |
| palo alto networks firewall |
| sase cloud |
| sysdig secure |
| windows event |
| workspace activities |
| workspace alerts |
| zimperium |
| zscaler |
| zscaler casb |
| zscaler ngfw |
| zscaler zpa |
