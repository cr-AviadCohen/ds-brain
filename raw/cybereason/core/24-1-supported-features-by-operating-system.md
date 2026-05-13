|Feature|Category|Windows|Mac|Linux|
|---|---|---|---|---|
|Anti-Malware|Signature-<br>based<br>analysis|✓|✓|✓|
|Anti-Malware|Artifcial<br>Intelligence<br>analysis|✓<br>Not<br>supported<br>on<br>endpoints<br>with CSV<br>(Cluster<br>Shared<br>Volume) fle<br>systems|||
|Anti-Malware|Scheduled<br>scans<br>(full/quick)|✓|✓|✓|


|Feature|Category|Windows|Mac|Linux|
|---|---|---|---|---|
|Anti-Malware|On-fle<br>access<br>scans|✓|✓|✓|
|Anti-<br>Ransomware|Anti-<br>Ransomware|✓|||
|Application<br>Control|Application<br>Control|✓<br>Not<br>supported<br>on<br>endpoints<br>with CSV<br>(Cluster<br>Shared<br>Volume) fle<br>systems|||
|Application<br>Control|SHA-1/SHA-<br>256 hash-<br>based<br>prevention|✓|||
|Behavioral<br>document<br>protection|Rule-based<br>behavioral<br>document<br>protection|✓|||
|Behavioral<br>document<br>protection|AI-based<br>behavioral<br>document<br>protection|✓|||
|Behavioral<br>execution<br>prevention|Behavioral<br>execution<br>prevention<br>rules|✓|||
|Behavioral<br>execution<br>prevention|Variant<br>payload<br>protection|✓<br>Windows<br>10 RS2 and<br>later|||
|Behavioral<br>execution<br>prevention|Variant fle<br>prevention|✓|||


|Feature|Category|Windows|Mac|Linux|
|---|---|---|---|---|
|Endpoint<br>Controls|Device<br>Control|✓|✓<br>USB<br>Devices<br>only|✓|
|Endpoint<br>Controls|Personal<br>frewall<br>control|✓||✓|
|Endpoint<br>controls|Full disk<br>encryption<br>visibility|✓|||
|Exploit<br>Protection|Exploit<br>Protection|✓<br>If you are<br>using a<br>version of<br>Windows<br>that does<br>not include<br>Exploit<br>Guard<br>(versions<br>earlier than<br>Windows<br>10 Fall<br>Creators<br>Update or<br>RS3), EMET<br>5.5 is<br>required for<br>Exploit<br>protection<br>to work. If<br>EMET is not<br>installed,<br>we<br>recommend<br>to upgrade<br>to the latest<br>Windows<br>version,<br>because<br>Windows<br>no longer<br>offcially<br>supports<br>EMET.|||


|Feature|Category|Windows|Mac|Linux|
|---|---|---|---|---|
|Fileless<br>protection|Fileless<br>protection|✓|||
|Fileless<br>protection|Anti-Malware<br>Scan<br>Interface<br>(AMSI)-<br>based<br>protection|✓<br>Windows<br>10 and later|||
|Predictive<br>Ransomware<br>Protection|Predictive<br>Ransomware<br>Protection|✓|||














|Feature|Category|Windows|macOS|Linux|
|---|---|---|---|---|
|Active<br>Directory|Active<br>Directory<br>data|✓|||
|Connection|Long-lived<br>connection|✓|✓|✓<br>On Linux<br>sensors,<br>this<br>connection<br>type does<br>not include<br>rx/tx bytes.|
||||||


|Feature|Category|Windows|macOS|Linux|
|---|---|---|---|---|
|Connection|Short-lived<br>connection|✓|✓|✓<br>Not<br>supported<br>on SLES<br>12, Debian<br>8/9, or<br>Amazon<br>Linux AMI<br>2017.03.|
|Connection|TCP|✓|✓|✓|
|Connection|UDP|✓|||
|Domain<br>request<br>and<br>response|Domain<br>request and<br>response<br>details|✓||✓<br>For Linux<br>sensors,<br>domain<br>request<br>and<br>response<br>requires<br>libpcap<br>version 1.0<br>or higher,<br>and Linux<br>kernel<br>version<br>2.6.32-358<br>or higher.|
|Drivers|Drivers<br>installed on<br>machine|✓|✓|✓<br>Not<br>supported<br>on SLES<br>12, Debian<br>8/9,<br>Amazon<br>Linux AMI<br>2017.03.|
|File|Download<br>source info||✓||
|File|MD5, SHA-<br>1, and<br>SHA-256<br>fle hashes|✓|✓|✓|


|Feature|Category|Windows|macOS|Linux|
|---|---|---|---|---|
|File|Icon<br>collection|✓|✓||
|File|Metadata<br>for non-exe<br>fles|✓|||
|File|File<br>properties|✓|✓|✓|
|File|File<br>signatures|✓|✓|✓|
|File events|File events|✓<br>Not<br>recommended<br>for use on<br>server<br>machines.|||
|Hosts fle|Host fle<br>details|✓|||
|Logon<br>session|Logon<br>session<br>details|✓|✓|✓|
|Machine|Machine<br>information|✓|✓|✓|
|Modules|Floating<br>modules|✓|||
|Modules|Long-lived<br>modules|✓|||
|Modules|Short-lived<br>modules|✓|||
|Mount<br>Point|Mount point<br>details|✓|✓|✓|
|Network<br>interface|Network<br>interface<br>details|✓|✓|✓|
|Process|Process<br>aggregation|||✓|
||||||


|Feature|Category|Windows|macOS|Linux|
|---|---|---|---|---|
|Process|Code<br>Injection|✓|||
|Process|Long-lived<br>processes|✓|✓|✓|
|Process|Short-lived<br>processes|✓|✓|✓|
|Proxy|Proxies<br>confgured<br>on machine|✓|✓||
|Registry|Registry<br>entries|✓|||
|Registry<br>Events|Registry<br>event<br>details|✓|||
|Remote<br>Logon<br>Sessions|Remote<br>logon<br>session<br>details|✓|✓|✓|
|Scheduled<br>Task|Scheduled<br>task details|✓|✓<br>Scheduled<br>tasks are<br>displayed<br>as part of<br>services.||
|Services|Service<br>details and<br>properties|✓|✓|✓<br>Services<br>are not<br>collected<br>on Ubuntu<br>14.|
|User|User<br>account<br>details|✓|||
|WMI<br>activity|WMI activity<br>details|✓|||
||||||


|Feature|Category|Col3|Windows|Col5|macOS|Col7|Linux|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|WMI<br>persistent<br>objects|WMI<br>persistent<br>object<br>details|WMI<br>persistent<br>object<br>details|✓|✓||||||
|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|Response features<br>With response features, the Cybereason platform identifes a<br>threat, and then you specify an action for the Cybereason platform<br>to take. For example, you might instruct the Cybereason platform<br>to isolate a machine or kill a process.<br>The Cybereason platform's response actions fall into multiple<br>categories:<br>**MalOp response:** Using the capabilities of the Cybereason<br>platform's EDR module, these actions enable you to address<br>threats immediately. When the Cybereason platform detects a<br>potentially malicious operation, the platform generates a<br>MalOp. In the MalOp, you view, understand, and analyze the<br>activities associated with the MalOp and respond accordingly<br>to stop potential problems.<br>**Digital Forensics and Incident Response (DFIR):** Using the<br>Cybereason platform's DFIR module, you can supplemenet<br>the native response abilities of the Cybereason platform.<br>These features help you automatically deploy and run incident<br>response and forensic data ingestion tools using the<br>Cybereason platform.<br>The Cybereason platform supports the following features in the<br>operating systems detailed below:|
|**Feature**|**Feature**|**Category**|**Category**|**Windows**|**Windows**|**Mac**|**Mac**|**Linu**||
|DFIR|DFIR|Manage incident<br>response (IR) tools|Manage incident<br>response (IR) tools|✓|✓|||✓||
|DFIR|DFIR|Browse fles from<br>the Element Details<br>screen|Browse fles from<br>the Element Details<br>screen|✓|✓|||||
|DFIR|DFIR|Download fles from<br>the Element Details<br>screen|Download fles from<br>the Element Details<br>screen|✓|✓|✓|✓|✓||
|||||||||||


|Feature|Category|Windows|Mac|Linu|Col6|
|---|---|---|---|---|---|
|DFIR|Live File search|✓|✓<br>Not enabled<br>by default|✓<br>(vers<br>23.2.<br>and l||
|DFIR|Live File search with<br>YARA rules|✓|✓|✓||
|Machine<br>isolation|Isolate machine|✓|✓|✓<br>Not<br>supp<br>on SL||
|Machine<br>isolation|Customize the<br>queue period|✓|✓|✓||
|Machine<br>isolation|Machine isolation<br>exception rules|✓|✓|✓||
|Machine<br>isolation|Machine isolation<br>exception rules for<br>IP range|✓|✓|✓||
|Remediation<br>actions|Kill process|✓|✓|✓||
|Remediation<br>actions|Quarantine fle|✓|✓<br>Not<br>supported<br>for DMG<br>fles and<br>fles<br>downloaded<br>from the<br>Internet on<br>OSX<br>operating<br>systems.|✓||
|||||||


|Feature|Category|Windows|Mac|Linu|Col6|
|---|---|---|---|---|---|
|Remediation<br>actions|Unquarantine fle|✓||||
|Remediation<br>actions|Add unquarantine<br>fle to allowlist|✓||||
|Remediation<br>actions|Download<br>quarantined fle|✓||||
|Remediation<br>actions|Remove registry<br>entries|✓||||
|Remediation<br>actions|Suspend/unsuspend<br>ransomware|✓||||
|Remediation<br>actions|Prevent a fle's<br>execution|✓||||
|Remote<br>Shell|Restricted mode|✓|✓|✓||
|Remote<br>Shell|Unrestricted mode|✓|✓|✓||
|Remote<br>Shell|Sensor group<br>access|✓|✓|✓||
|Sensor platform features<br>The Cybereason platform supports the following sensor features<br>on the operating systems listed below:|Sensor platform features<br>The Cybereason platform supports the following sensor features<br>on the operating systems listed below:|Sensor platform features<br>The Cybereason platform supports the following sensor features<br>on the operating systems listed below:|Sensor platform features<br>The Cybereason platform supports the following sensor features<br>on the operating systems listed below:|Sensor platform features<br>The Cybereason platform supports the following sensor features<br>on the operating systems listed below:||


|Feature|Windows|macOS|Linux|
|---|---|---|---|
|Data<br>collection<br>continues<br>when the<br>sensor is<br>disconnected|✓|✓|✓|
|Decommission<br>sensors|✓|✓|✓|
|Digital signing<br>for the sensor<br>fle|✓|✓|✓|
|eBPF<br>framework for<br>process<br>collection|||✓|
|ESF<br>framework for<br>process<br>collection||✓||
|Endpoint<br>Management<br>Channel|✓|✓<br>(Authenticated<br>URL feature:<br>Big Sur and<br>higher)|✓|
|Exclusion<br>obfuscation in<br>logs|✓|✓|✓|
|Scaled sensor<br>upgrade<br>process|✓|||
|Process<br>collection from<br>the drive|✓|||
|Proxy<br>connection for<br>sensor - auto-<br>detect proxy|✓|✓|✓|


|Feature|Windows|macOS|Linux|
|---|---|---|---|
|Proxy<br>connection for<br>sensor -<br>manual<br>assignment|✓|✓|✓|
|Proxy<br>connection for<br>sensor - use<br>PAC or server|✓|✓||
|Quarantine fle<br>cleanup|✓|✓||
|Registration<br>server for<br>sensor<br>assignment to<br>Detection<br>servers|✓|✓|✓|
|Restart sensor|✓|✓|✓|
|Sensor binary<br>fles with the<br>Sectigo<br>certifcate|✓|||
|Sensor works<br>in Safe mode|✓|✓|✓|
|Sensor<br>installation for<br>sensor groups|✓|✓|✓|
|Sensor<br>tampering<br>protection|✓|||
|Start/stop<br>sensor|✓|✓|✓|
|Uninstall<br>sensors from<br>the**Sensors**<br>screen|✓|✓|✓|
|Uninstall<br>password|✓<br>Not on<br>Windows 8|||


|Feature|Windows|macOS|Linux|
|---|---|---|---|
|Uninstall<br>sensors from<br>fle|✓|||
|Upgrade<br>sensor|✓|✓|✓|
|Upgrade<br>sensor -<br>prerequisite<br>checks|✓|||





