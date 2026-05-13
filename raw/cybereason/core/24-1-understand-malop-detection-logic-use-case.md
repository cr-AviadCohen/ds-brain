## PowerShell suspicion logic explained

The Malicious use of PowerShell suspicion may include (for


example) the following three evidences:


The Malicious use of PowerShell suspicion the following three


evidences:






|Obfuscated<br>PowerShell<br>command<br>evidence|This evidence indicates that the process<br>in question is a PowerShell process,<br>and the PowerShell command line uses<br>obfuscation techniques.|
|---|---|
|**Malicious**<br>**PowerShell**<br>**framework**|This evidence indicates that the process<br>is a PowerShell process, and is found to<br>be a malicious PowerShell framework.|
|**PowerShell**<br>**executed by Word**<br>**process**|This evidence indicates that the process<br>is a PowerShell process and the parent<br>process is Microsoft Word.|


## How does this detection logic help me?

First, all AI Hunting MalOps require multiple conditions. Any


individual threat requires additional detections (such as certain

suspicions and evidence), so that a MalOp shows a pattern of


behavior, not just an isolated malicious incident. In this example,

the **Malicious use of PowerShell Malop** may include four


different suspicions, including the **Malicious use of PowerShell**

suspicion and three additional suspicions.


Second, suspicions and evidence are usually also multi-faceted,

and are based on events and properties. In this example, the


**Malicious use of PowerShell** suspicion may include three

different evidences:


**Obfuscated PowerShell command evidence:**

**Malicious PowerShell framework:**


**PowerShell executed by Word process:**


Because suspicions and evidence are based on events and


properties, some suspicions and evidence are not necessarily

malicious and must be analyzed further. Because these


suspicions and evidence involve a smaller number of events that



