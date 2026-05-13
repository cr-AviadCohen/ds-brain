|Component|Description|Process Name|Col4|
|---|---|---|---|
|ActiveConsole|Establishes and maintains a<br>continuous connection with the<br>Detection server.|ActiveConsole.exe||
|ActiveProbe|Performs all Cybereason<br>platform collection and detection<br>activities on the endpoint and<br>feeds EDR with data on what<br>occurs on the machine, and<br>responds to requests from the<br>server.|PylumLoader.exe,<br>minionhost.exe||
|Anti-Malware<br>Driver|The Anti-Malware driver is<br>automatically installed as a<br>kernel driver when the Anti-<br>Malware Signatures feature is<br>enabled, in order to monitor fles<br>and processes that interact with<br>flesystem artifacts.|N/A||
|Anti-Malware<br>Driver<br>subcomponent|This service is part of the Anti-<br>Malware Signatures mode<br>operations.|N/A||
|Anti-Malware<br>Service|The Anti-Malware service<br>determines the logic of each<br>scan (see How does signature<br>analysis determine if a fle is<br>malicious? (/s/knowledge-base?<br>article=24-1-signature-based-<br>analysis&language=en_US#how-<br>does-signature-analysis-<br>determine-if-a-fle-is-malicious)).<br>The service is installed in the<br>user space when the Anti-<br>Malware > Signatures feature is<br>enabled.|AmSvc.exe||
|Anti-<br>Ransomware<br>Service|The Anti-Ransomware service<br>manages ransomware detection<br>and prevention on the endpoint,<br>including the deployment and<br>tracking of canary fles (where<br>applicable), and the suspension<br>of ransomware processes.|CrsSvc.exe||
|crav|Used by Windows machines to<br>enable the Cybereason Anti-<br>Malware protection to run with<br>Windows.|crav.exe||
|||||


|Component|Description|Process Name|Col4|
|---|---|---|---|
|cybereasonav|Used by Windows machines to<br>enable the Cybereason Anti-<br>Malware protection to run with<br>Windows.|cybereasonav.exe||
|Execution<br>Prevention<br>Driver|The Execution Prevention driver<br>is automatically installed as a<br>kernel driver when the<br>Application Control or Artifcial<br>intelligence Analysis features are<br>enabled, in order to block<br>execution of malicious fles and<br>processes.|N/A||
|Execution<br>Prevention<br>Service|The Execution Prevention service<br>calls the Artifcial Intelligence<br>scanner and the Application<br>Control scanner to determine if<br>the fle can be opened safely.|ExecutionPreventi||
|EDR|EDR collects data on endpoint<br>fles, processes and other<br>security-related events. EDR<br>sends this data to the Detection<br>server for analysis and detection<br>of advanced attacks. All sensor<br>services send reports and<br>communication to the sensor's<br>EDR component, which sends<br>these alerts to the Cybereason<br>UI via the Detection server.|minionhost.exe||
|Nnx|Manages Fileless Protection,<br>Behavioral Execution protection,<br>Predictive Ransomware<br>protection, and Variant File<br>Protection. If all of these features<br>are disabled, this process does<br>not run. If any one of the three<br>protection engines is enabled,<br>this process will still run.|Nnx.exe||
|PowerShell<br>Protection|PowerShell protection detects<br>and prevents malicious<br>PowerShell commands.|N/A||
|||||


|Component|Description|Process Name|Col4|
|---|---|---|---|
|Protected<br>service|Threat Intel service which allows<br>the Cybereason platform to<br>consume ETW (Event Tracing for<br>Windows) events to detect<br>credential Theft MalOps.|CrEX3.exe||
|PylumLoader|Launches and monitors the<br>sensor.|PylumLoader.exe||
|Remote Shell<br>Service<br>(Optional)|Remote Shell enables security<br>personnel to perform incident<br>response directly on the<br>machine. This service is disabled<br>by default.|ActiveCLIAgent.ex||
|SigCheck|Used for verifying our fle<br>signatures using Microsoft<br>technology.|sigcheck.exe||
|Update|The Update component retrieves<br>updates from the NGAV Global<br>or Local Update server.<br>Automatic updates occur every<br>15 minutes by default.|N/A||
|User Agent|The Cybereason icon appears<br>on the end user's System Tray by<br>default (it can be disabled if<br>necessary).|CrAmTray.exe||
|WSC Interface|Reports Anti-Malware Signatures<br>mode actions to the Windows<br>Security Center (WSC). The WSC<br>then reports to Windows that the<br>Anti-Malware > Signatures<br>feature is online and displays<br>status messages in WSC, for<br>example:**Cybereason Anti-**<br>**Malware is protecting**.|WscIfSvc.exe||
|On Windows, the sensor services run as localsystem (SYSTEM).<br>The icon (cramtray.exe) runs as the user account.<br>Mac sensor processes<br>Sensors on macOS machines have different components<br>depending on whether your enable the**Anti-Malware >**<br>**Signatures mode** for your Mac sensors:|On Windows, the sensor services run as localsystem (SYSTEM).<br>The icon (cramtray.exe) runs as the user account.<br>Mac sensor processes<br>Sensors on macOS machines have different components<br>depending on whether your enable the**Anti-Malware >**<br>**Signatures mode** for your Mac sensors:|On Windows, the sensor services run as localsystem (SYSTEM).<br>The icon (cramtray.exe) runs as the user account.<br>Mac sensor processes<br>Sensors on macOS machines have different components<br>depending on whether your enable the**Anti-Malware >**<br>**Signatures mode** for your Mac sensors:||


|Process Name|Description|
|---|---|
|**CybereasonActiveConsole**|Responsible for sensor<br>communication, status,<br>reporting, and management<br>actions.|
|**CybereasonSensor**|Performs all Cybereason<br>platform collection and<br>detection activities on the<br>endpoint. This process runs<br>as a service in the user<br>space, by the root user.|
|In versions before macOS 11<br>(Big Sur):**CybereasonAVKext**<br>In macOS version 11 (Big Sur)<br>and later:**CybereasonAv**|Performs all activities related<br>to Anti-Malware Signatures<br>mode, if enabled.|


## Linux sensor processes

Sensors on Linux machines have different components depending

on whether your enable the **Anti-Malware > Signatures mode** for


your Linux sensors:







|Process Name|Description|
|---|---|
|cybereason-<br>activeconsole|Responsible for sensor communication,<br>status, reporting, and management actions.|
|cybereason-<br>sensor|Performs all Cybereason collection and<br>detection activities on the endpoint. This<br>process runs as a service in the user<br>space, by the**cybereason** user.|
|cbram|Performs all activities related to Anti-<br>Malware Signatures mode, if enabled.|

## Sensor security and password

The Cybereason platform secures itself using the following

methods:


All communication between the sensor and the Registration

and Detection servers occurs over TLS.


Data in transit is transmitted over TLS, based on two-way


authentication between server and client and based on

certificate verification that employs a 2048-bit RSA key set,


and SHA256 hashing algorithm.

Only machine administrators can install or uninstall sensors on


endpoints across your organization.

You can generate a special passkey to uninstall sensors that


prevents the uninstallation of the sensor without the passkey.





