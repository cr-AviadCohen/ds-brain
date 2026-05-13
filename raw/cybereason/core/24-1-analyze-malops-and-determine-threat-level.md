[and-components&language=en_US#malop-types-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-types-and-components&language=en_US#malop-types-and-components)


[components) topic to learn which of the following properties to](https://nest.cybereason.com/s/knowledge-base?article=24-1-malop-types-and-components&language=en_US#malop-types-and-components)

focus on based on MalOp type.


Start by looking at the general properties associated with the files

included in the MalOp:






|Investigation<br>Area|Description|
|---|---|
|File Name and<br>Attributes|Look at fle name and attributes. For**.exe**<br>fles, the Cybereason platform reports a<br>number of important details:<br>Process names and IDs running from a<br>fle<br>Creation and end times<br>Command line information used by the<br>process from this fle<br>Details about the image fle (for<br>processes)<br>Extension type of the fle<br>Path to the fle<br>Signature details<br>Product names and types, and the<br>company names for the fle<br>Suspicious data for any of these indicators<br>shows a possibly malicious fle worth<br>investigating further.|
|Suspicions and<br>evidence|Did the Cybereason platform associate any<br>evidence or suspicions with this fle?|
|Signature|Is the fle signed and by whom? Anomalies<br>in the signature can often be a sign of<br>potentially malicious behavior|
|File location|Is the fle in a suspicious folder, such as the<br>_/temp_, _AppData_, _ProgramData_ folders? If a<br>fle runs from locations such as these, this is<br>a suspicious indicator.|
|Reputation|What is the fle's reputation? Based on the<br>fle's reputation you may want to look<br>further.|



The file details in the following image from the Element Details
screen point to malicious activity because the file is unsigned and


running from the temp folder.


Every MalOp includes relevant network information in the

**Communication** tab of the MalOp. Investigate these properties to


see potentially malicious behavior on the network


When analyzing the network properties, ask yourself questions


such as:







|Investigation<br>Area|Description|
|---|---|
|Network<br>connections|Ask questions about the communication<br>and connections, including:<br>Are there network connections? Internal<br>or external connections?<br>How long are the connections?<br>Is there data transmitted through these<br>connections? How much?<br>What port type is used in these<br>connections?<br>What direction is the communication?<br>If you fnd unexpected answers to these<br>questions, you need to investigate further<br>into such connections.|
|Listening<br>connections|Is there a listening connection or port on a<br>process?|
|DNS requests|Investigate both resolved and unresolved<br>DNS requests. Make sure that the behavior<br>of these requests are expected or not.|
|Processes|What processes are performing the<br>connections? Should they be?|


For example, the details in the following image suggest suspicious


activity because a machine is connecting to port 4444, which is

the default port for Metasploit's meterpeter. In addition, we see


these two machine transferring data.


For each MalOp, investigate the modules included with the


processes running as part of the MalOp. The MalOp details report

the loaded modules associated with the malicious process.


However, to view details about the modules, you must use the

**Investigation** screen, either through the MalOp details or


independently.


When analyzing modules, ask yourself questions such as:







|Investigation<br>Area|Description|
|---|---|
|Module<br>properties|What are the properties of the module or<br>modules? Your Cybereason platform reports<br>a number of details, including:<br>Names and addresses<br>Header and allocated properties values<br>Whether the header is a malformed<br>executable header<br>Characteristics of the module<br>General fle details<br>Scan these properties to check if you fnd<br>suspicious indicators in the properties list.|
|Floating<br>modules|Is the module foating? If you answer**Yes**,<br>check the protection details for mismatches.|
|Processes|What processes are using these modules?<br>Should they be using them?|
|Intelligence|Is this a known module when you search for<br>it on the internet?|


In general, the more common the module, the less likely it is to be


malicious.


For each MalOp, the Cybereason platform collects a variety of


information about the processes involved in the associated

activities. The Malop Inbox reports the process details in the


**Processes** tab of the MalOp details.


When analyzing the process properties, ask question such as:






|Investigation<br>Area|Description|
|---|---|
|Process details|Scan the collected process details<br>including:<br>The fle associated with the process<br>The total time for the process<br>Start and end times for the process|
|Suspicions and<br>evidences|What suspicions and evidences are<br>associated with the process?|
|Process type|What type of process is it - an OS process?<br>3rd party process?<br>It is also a good idea to look at the product<br>type for the process.|
|Command line|What is the command line returned for the<br>process? Many malicious behaviors<br>originate from command line arguments so<br>be sure to check these closely.|
|Process<br>behaviors|Does the process create other ways to<br>persist itself, such as registry entries,<br>scheduled tasks, services, or child<br>processes? Does this process has a<br>suspicious parent process? Is it an injected<br>process?|



In addition, for all processes, you can view the Attack Tree to see


how the process fits with other processes in your environments.

[For details on the Attack Tree, see Hunt with the Attack Tree](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunt-with-the-attack-tree&language=en_US#hunt-with-the-attack-tree)


[(/s/knowledge-base?article=24-1-hunt-with-the-attack-](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunt-with-the-attack-tree&language=en_US#hunt-with-the-attack-tree)

[tree&language=en_US#hunt-with-the-attack-tree).](https://nest.cybereason.com/s/knowledge-base?article=24-1-hunt-with-the-attack-tree&language=en_US#hunt-with-the-attack-tree)


The process details in the following image point to suspicious

activity because, while the process claims to be from Microsoft, it


is not signed by Microsoft. Additionally, the process is running

from a temp folder and has an unknown reputation.


## Analyze the status of automatic

## protection actions

For Endpoint Protection MalOps generated by Cybereason's EPP

features, look at the **Protection type** column in the **Malops**


**management** screen to see how the Cybereason platform

endpoint protection features responded to the incident. The


following table includes status descriptions, which types of

malware are associated with each status, and suggested actions


to take.














|Protection<br>type status|Description|Malware<br>types|
|---|---|---|
|Disinfected|Malware was detected and the<br>malicious fle was disinfected.<br>In cases where it was not possible to<br>disinfect the fle, the fle is removed<br>from the machine.**Note:** in this case,<br>the fle is not quarantined, it is<br>completely removed from the machine.|Known|
|Failed to<br>disinfect|Malware was detected and prevented,<br>but Anti-Malware could not disinfect or<br>remove the fle.|Known|


|Protection<br>type status|Description|Malware<br>types|
|---|---|---|
|Detected|Malware was detected but no action<br>was taken to prevent it.|Known,<br>Unknown,<br>Fileless,<br>Ransomware|
|Prevented|Malware was detected and prevented.|Known,<br>Unknown,<br>Fileless,<br>Application<br>Control|
|Deleting on<br>restart|Malware was detected and prevented.<br>It will be removed upon restart.|Known|


|Protection<br>type status|Description|Malware<br>types|
|---|---|---|
|Quarantined|Malware was detected and the<br>malicious fle was quarantined.<br>Malware MalOps marked with the<br>'Quarantined' Auto response label<br>indicate that the Cybereason platform<br>has moved the malicious fle to a<br>different location to prevent it from<br>executing. Quarantined fles are<br>placed in the following folder location:<br>**Windows**:<br>C:\ProgramData\apv2\Quarantine<br>**Mac**: /usr/local/cybereason<br>**Linux**:<br>/opt/cybereason/sensor/Quarantine<br>Cybereason deletes quarantined fles<br>after 30 days. The cleanup is<br>scheduled to run daily (every 24 hours)<br>and on sensor startup.<br>Note<br>The Quarantined status is relevant<br>only for malware triggered by<br>Artifcial Intelligence analysis and<br>behavioral document protection.|Unknown,<br>Fileless,<br>Ransomware|


## Determine the threat level

After you investigate your MalOp, you need to consider all the

answers together to determine if the behavior is malicious and


requires further remediation.


When deciding how, or in what order, to address MalOps you have


deemed a threat to your organization, consider:

The significance of the **machines** involved in the suspicious


activities. Address machines that are more vital machines to

your organization first.


The significance of the **behavior** . Severe activities should be

address before other, less severe activities.


The significance of the **users** involved. Certain users may be

more compromised than others. For example, suspicious


activity on a CEO's computer or on a machine with sensitive



