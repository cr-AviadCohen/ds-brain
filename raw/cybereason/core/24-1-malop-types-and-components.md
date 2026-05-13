|Icon|MalOp<br>type|Description|
|---|---|---|
||**AI**<br>**Hunting**<br>**MalOps**|MalOps that represent threats that the<br>Cybereason Cross Machine Correlation<br>(CMC) engine or private and global threat<br>intelligence sources identifes.|


|Icon|MalOp<br>type|Description|
|---|---|---|
||**Endpoint**<br>**Protection**<br>**MalOps**|MalOps that were triggered by threats<br>detected or prevented on the endpoint,<br>including known malware, unknown<br>malware, and ransomware.<br>Note<br>Some MalOps detected by the<br>Cybereason platform's Anti-<br>Ransomware or Predictive Ransomware<br>Protection engines are identifed as**AI**<br>**Hunting** MalOps, not Endpoint<br>Protection MalOps.<br>The Cybereason platform generates<br>Endpoint Protection MalOps for multiple<br>types of malware, including:<br>**Known:** MalOps are generated from<br>known malware detected by signature-<br>based detection.<br>**Unknown:** MalOps are generated from<br>previously unknown malware detected<br>by artifcial intelligence.<br>**Fileless:** MalOps are generated from<br>malware not based on a fle, such as<br>PowerShell-based attacks.<br>**App Control** MalOps are generated<br>based on the prevention of<br>applications/processes marked for<br>prevention in the**Reputation** screen<br>(see Manage Reputations<br>(/s/knowledge-base?article=24-1-<br>manage-<br>reputations&language=en_US#manage-<br>reputations)).|

## MalOp states





When the Cybereason platform etects a MalOp, the Cybereason

platform immediately assigns a state to the MalOp. The MalOp


State represents how the MalOp is currently behaving in your

environment, and helps inform what response actions an analyst


should take. MalOps can have the following states in the **Malops**

**management** screen.


|Icon|State|Description|
|---|---|---|
|<br>(Red)|Active|Active MalOps are red and require<br>urgent response. A MalOp is active if<br>the malicious behavior is currently<br>active. This could mean that a<br>malicious fle is open, or a malicious<br>process is running.<br>For malware, the Cybereason platform<br>cannot know if the malicious item was<br>accessed, so the alert is considered<br>**Active** as long as it hasn't been<br>addressed.|
|<br>(Yellow)|Inactive|Inactive Malops are yellow and<br>indicate further response is<br>recommended. A MalOp is inactive if<br>the associated processes are not<br>active, but a risk still exists. For<br>example, if a fle is not currently<br>executing but could be malicious, an<br>analyst might want to at it to the<br>blocklist.|
|<br>(Green)|Resolved|Resolved MalOps are green and<br>indicate no further action is required. A<br>MalOp is considered resolved if one of<br>the following occurs:<br>The Cybereason platform<br>automatically prevents, disinfects,<br>or quarantines a malicious item.<br>An analyst manually resolves the<br>MalOp using the**Mark as**<br>**remediated/resolved** button in the<br>**Malops management** or**Malop**<br>**details** screen.|
|<br>(Grey)|Excluded|Excluded MalOps are grey and<br>indicate that the MalOp was addressed<br>and the 'Malop is benign - Exclude'<br>option was chosen during remediation.<br>Excluding a MalOp means the specifc<br>behaviors in the MalOps will not trigger<br>a MalOp in the future.|


MalOps contain the complete story of a cyber attack, including


affected machines, users, files, and more. These associated items

help the analyst not only understand what happened, but where


and to whom the malicious activity occurred.


Analysts can see a timeline of all associated activity for the


MalOp. The timeline includes all activity that the Cybereason

platform has associated with the MalOp, such as processes and


files.


The MalOp contains a list of suspicions that led to the MalOp


generation, and evidences that led to the creation of the

suspicion.


In addition, the Cybereason platform adds the following

information about a MalOp:


**Triggering item:** The process that caused the Cybereason

platform to create a MalOp.


**Detection type:** Category of activity that the Cybereason

platform recognized as the malicious behavior.


**Root cause:** The underlying reason why an activity is

considered malicious.


Within the MalOp, you can learn more about the associated
machines, users, files, processes, and so forth. You can view


collected details about these items and investigate specific items

in the Investigation screen.


In the **Malops management** screen, you can view all these

details:


Note


A single MalOp may have multiple root causes. The root cause

listed in the **Malops management** screen is the primary root


cause, or the one that requires the most attention.

## MalOp certainty levels


To help you better understand malicious behavior, the Cybereason


platform further classifies MalOps by **certainty levels** . Certainty

levels indicate the degree to which the Cybereason platform is


confident the behavior is a threat. Cybereason identifies the

following certainty levels, each of which contain different detection


types.


The following tables list the Cybereason MalOp detection types


and root causes organized by certainty level. The **Investigation**

column recommends properties to focus on when you investigate


a MalOp that has a certain detection type and root cause. For

[more details about investigating these properties, see Analyze](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)


[MalOps and Determine Threat Level (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)

[article=24-1-analyze-malops-and-determine-threat-](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)


[level&language=en_US#analyze-malops-and-determine-threat-](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)

[level).](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)

## Verified MalOps


Verified MalOps are verified by the Cybereason Security Research

team, meaning they demonstrate malicious activity and are likely a


threat to your system.


|Detection type|Col2|
|---|---|
|Blocklist (/s/knowledge-base?article=24-1-blocklist-<br>malops&language=en_US#blocklistdetections-appcontrolblocked)||
|Blocklist (/s/knowledge-base?article=24-1-blocklist-<br>malops&language=en_US#blocklistdetections-flehash)||
|Blocklist (/s/knowledge-base?article=24-1-blocklist-<br>malops&language=en_US#blocklistdetections-blocklistmodule)||
|Blocklist (/s/knowledge-base?article=24-1-blocklist-<br>malops&language=en_US#blocklistdetections-blocklistip)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-malwareaddress)||


|Detection type|Col2|
|---|---|
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-maliciousaddress)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-maliciousdomain)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-downloadmaliciousdo||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-dga)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-maliciousrclone)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-powershell)||
|||


|Detection type|Col2|
|---|---|
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-maliciousnetsupport)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-<br>maliciouspsexecfromscreenconnect)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-<br>maliciousfleintempfolderromscreenconnect)||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-screenconnectranmali||
|Command and Control (CNC) (/s/knowledge-base?article=24-1-comman<br>control-malops&language=en_US#c2cdetections-downloadexecute)||
|Credential theft (/s/knowledge-base?article=24-1-credential-theft-<br>malops&language=en_US#credentialtheft-attemptedcredentialtheft)||
|Credential theft (/s/knowledge-base?article=24-1-credential-theft-<br>malops&language=en_US#credentialtheft-maliciousaccesstontdsfle)||
|||


|Detection type|Col2|
|---|---|
|Credential theft (/s/knowledge-base?article=24-1-credential-theft-<br>malops&language=en_US#credentialtheft-maliciousaccesstontdssamres||
|Elevated access (/s/knowledge-base?article=24-1-elevated-access-<br>malops&language=en_US#elevatedaccess-detections)||
|Extension manipulation (/s/knowledge-base?article=24-1-extension-man<br>malops&language=en_US#extensionmanipulation-detections)||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#antimalwareArtifcialIntelligenceDetectedMal||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-blackcatransomware)||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-maliciousexecutable)||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-malicioustoolmodule)||
|||


|Detection type|Col2|
|---|---|
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-maliciousmodule)||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-malicioustool)||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-icedidmainbot)||
|Known malware (/s/knowledge-base?article=24-1-known-malware-<br>malops&language=en_US#knownmalware-antimalwaredetected)||
|CVE_2020_06_01 Attempted exploitation (/s/knowledge-base?article=24<br>process-malops-research&language=en_US#maliciousprocess-cve2020||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-disablecrservice)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-flelessmalware)||
|||


|Detection type|Col2|
|---|---|
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-javamalware)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-osprocesses)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-foatingmodule)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-packedprocess)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-maliciousfle)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-maliciouscommand)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-cobaltstrike)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-psempire)||
|||


|Detection type|Col2|
|---|---|
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-meterpreter)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-mimikatz)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-peddlecheap)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-malicioustool)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-rat)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-shellcodeinjection)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-slivershell)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-webshells)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-maliciousinstallutil)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-msmpengmismatch)||
|||


|Detection type|Col2|
|---|---|
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-<br>maliciousmsbuildexecutionfrommsoffce)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-maliciousnetcompiler)||
|Malicious process (/s/knowledge-base?article=24-1-malicious-process-<br>malops&language=en_US#maliciousprocess-maliciousmbuildprocessex||
|Persistence (/s/knowledge-base?article=24-1-persistence-<br>malops&language=en_US#persistencedetections)||
|Persistence (/s/knowledge-base?article=24-1-persistence-<br>malops&language=en_US#persistencedetections)||
|Process injection (/s/knowledge-base?article=24-1-process-injection-<br>malops&language=en_US#processinjection-detections)||
|||


|Detection type|Col2|
|---|---|
|Ransomware (/s/knowledge-base?article=24-1-ransomware-<br>malops&language=en_US#ransomware-detections)||
|Ransomware (/s/knowledge-base?article=24-1-ransomware-<br>malops&language=en_US#ransomware-detections)||
|Ransomware (/s/knowledge-base?article=24-1-ransomware-<br>malops&language=en_US#ransomware-detections)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-abnormalprocessactivity)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-androidtampering)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-apptampering)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-deviceconfgurations)||
|||


|Detection type|Col2|
|---|---|
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-devicejailbroken)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-elevatedprivileges)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-detectedmaliciousapp)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-malwareadware)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-malwareescalatedprivileges)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-malwareransom)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-mitm)||
|||


|Detection type|Col2|
|---|---|
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-mitmarp)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-mitmfakessl)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-mitmsslstrip)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-mitmicmp)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-flesystemmodifcation)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-roguewif)||
|||


|Detection type|Col2|
|---|---|
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-sideloadedapp)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-deceiveenduser)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-suspiciousiosapp)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-systemtampering)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-thirdpartyappstores)||
|Mobile (/s/knowledge-base?article=24-1-cybereason-mobile-<br>malops&language=en_US#mobile-untrustedprofle)||
|Research MalOps<br>Research MalOps are based on experimental rules that examine<br>new threat detection logic and which Cybereason evaluates over<br>time. Detections for these types of MalOps are turned off by<br>default because they have the potential to cause false positives<br>and have a certainty level that is dramatically lower than MalOps<br>classifed as Verifed. If you think you are not catching all the||


potentially malicious activity you want, or you have a strict


environment, contact customer support to turn on this feature and
see MalOps classified as Research.






|Detection type|Root<br>cause|
|---|---|
|Data transmission volume (/s/knowledge-base?<br>article=24-1-data-transmission-volume-<br>malops&language=en_US#datatransmission-<br>detections)|High<br>volume of<br>transmitted<br>data by<br>injected<br>process|
|Malicious process (/s/knowledge-base?article=24-1-<br>malicious-process-malops-<br>research&language=en_US#maliciousprocessresearch-<br>maliciouschildprocessfromoffce)|Malicious<br>creation of<br>a child<br>process by<br>Microsoft<br>Offce<br>process|
|Malicious process (/s/knowledge-base?article=24-1-<br>malicious-process-malops-<br>research&language=en_US#maliciousprocess-<br>cve2020)|The<br>process<br>attempted<br>to exploit a<br>known CVE|
|Malicious process (/s/knowledge-base?article=24-1-<br>malicious-process-malops-<br>research&language=en_US#maliciousprocess-<br>covertexecution)|Covert<br>process<br>execution|
|Phishing (/s/knowledge-base?article=24-1-phishing-<br>malops-research&language=en_US#phishing-<br>detections)|Malicious<br>execution<br>of shell<br>process|


|Detection type|Root<br>cause|
|---|---|
|Phishing (/s/knowledge-base?article=24-1-phishing-<br>malops-<br>research&language=en_US#maliciousdocument)|Malicious<br>document<br>detected|
|Reconnaissance (/s/knowledge-base?article=24-1-<br>reconnaissance-malops-<br>research&language=en_US#reconnaissance-<br>detections)|Process is<br>performing<br>suspicious<br>scanning<br>activities|
|Reconnaissance (/s/knowledge-base?article=24-1-<br>reconnaissance-malops-<br>research&language=en_US#reconnaissance-<br>detections)|Suspicious<br>scanning<br>activity by<br>an elevated<br>process|
|Credential Theft (/s/knowledge-base?article=24-1-<br>credential-theft-malops-<br>research&language=en_US#credentialtheftresearch-<br>abnormalprocessinvocation)|Abnormal<br>process<br>invocation<br>using<br>DCOM|
|Credential Theft (/s/knowledge-base?article=24-1-<br>credential-theft-malops-<br>research&language=en_US#credentialtheftresearch-<br>adintegration)|Active<br>Directory<br>Abuse|


|Detection type|Root<br>cause|
|---|---|
|Credential Theft (/s/knowledge-base?article=24-1-<br>credential-theft-malops-<br>research&language=en_US#credentialtheftresearch-<br>maliciousreadwritememoryaccess)|The<br>process<br>performed<br>a malicious<br>read/write<br>memory<br>access to a<br>sensitive<br>process|
|Persistence (/s/knowledge-base?article=24-1-<br>persistence-malops-<br>research&language=en_US#asyncrat-malware)|Async Rat<br>malware<br>detected|
|Persistence (/s/knowledge-base?article=24-1-<br>persistence-malops-<br>research&language=en_US#persistenceresearch-<br>loginlogouthooks)|User<br>login/logout<br>hook<br>detected|
|Elevated access (/s/knowledge-base?article=24-1-<br>elevated-access-malops-<br>research&language=en_US#elevatedaccessresearch-<br>detections)|Attempt to<br>disable<br>macOS<br>Gatekeeper|


|Detection type|Root cause|MalOp<br>triggered<br>when...|Invest|
|---|---|---|---|
|Potentially Unwanted Program<br>(PUP) (/s/knowledge-base?<br>article=24-1-potentially-<br>unwanted-programs-pup-<br>malops&language=en_US#pup-<br>detections)|Cybereason<br>Threat<br>Intelligence<br>identifed<br>an<br>Unwanted<br>Executable|Process<br>image fle<br>hash is<br>identifed as<br>a Potentially<br>Unwanted<br>Program by<br>Cybereason<br>Threat<br>Intelligence|Image<br>of the<br>proces|
|Potentially Unwanted Program<br>(PUP) (/s/knowledge-base?<br>article=24-1-potentially-<br>unwanted-programs-pup-<br>malops&language=en_US#pup-<br>detections)|Cybereason<br>Threat<br>Intelligence<br>identifed<br>an<br>Unwanted<br>Module|Process<br>loads a<br>module<br>identifed as<br>a Potentially<br>Unwanted<br>Program by<br>Cybereason<br>Threat<br>Intelligence|Loaded<br>module|





