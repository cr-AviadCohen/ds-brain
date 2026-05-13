|MalOp<br>types|Details|
|---|---|
|For all<br>MalOps|If the Cybereason platform generates a<br>MalOp multiple times because of<br>scheduled scans, the platform groups the<br>instances into a single MalOp. In this case,<br>the Cybereason platform notes the time that<br>the platform frst detected the MalOp, the<br>time the platform most recently detected<br>the MalOp, and the number of instances of<br>the MalOp.<br>The item stems from a source found in a<br>previously generated MalOp.<br>The item satisfes more than one root<br>cause.|
|For AI Hunt<br>MalOps|If the root cause Element is File, the<br>Cybereason platform aggregates by fle hash<br>except in the following cases:<br>If the fle is classifed as a potentially<br>unwanted program (PUP), the Cybereason<br>platform aggregates by company.<br>If the fle is signed, and has an internal<br>name, company name, and product name,<br>the Cybereason platform aggregates by<br>those elements (all values per element have<br>to be identical in this case).|
|For<br>Endpoint<br>Protection<br>MalOps|If the Cybereason platform Anti-Malware<br>feature identifes the item, the Cybereason<br>platform groups the malicious fles into one<br>MalOp by fle hash value.<br>If Cybereason's Anti-Malware feature<br>identifes the item as a PowerShell process,<br>the Cybereason platform groups the<br>MalOps by the root cause, such as the<br>domain, URL, or script pattern.|



If the Cybereason platform encounters a malicious element or

activity whose root cause triggered a MalOp in the past, the


Cybereason platform adds the new item's details to the existing

MalOp, including any new root causes, instead of generating a


new MalOp.


You can view detailed information about each instance of the


malicious element or activity in the **Malop Details** screen.


If the root cause has not triggered a MalOp in the past, the


Cybereason platform creates a new MalOp.


PowerShell is a general purpose tool that can be used to facilitate


a lot of different actions, including a lot of different MalOps.


Unlike other MalOps, the Cybereason platform groups PowerShell


MalOps, identified by the **Malicious activity by PowerShell or**

**.NET process** name for the MalOp, by the machine in the user's


network on which the malicious PowerShell process is running.

Since PowerShell is a general purpose tool used to facilitate many


different actions (some of which are legitimate), combining

PowerShell MalOps by normal grouping methods could create


MalOps with many potentially unrelated threats. By grouping by

machine, each **Malicious Use of Powershell** MalOp is much


more likely to contain threats that are connected to each other.


Grouped MalOps display in both the **Malops management** and


**Malop details** screen:






|View|Details|
|---|---|
|From the<br>Malops<br>management<br>screen|The**Malops management** screen shows one<br>row per MalOp, even if the grouping<br>functionality was applied.<br>In grid view, the root causes are listed in the<br>**Detection description** column, separated by<br>a comma. In card view, the root causes are<br>listed in the**Subject** column in red above the<br>malicious behavior.|


|View|Details|
|---|---|
|From the<br>Malop details<br>screen|The**Malop details** screen lists the multiple<br>root causes (if applicable) under the name of<br>the fle or process that triggered the Malop.<br>Details about each root cause can be found<br>on the left side of the Malop details screen.<br>If a MalOp was reopened, an**Only new**<br>**activity** check box appears at the top of the<br>screen. Select this checkbox to view details<br>for only the events that occurred since the<br>MalOp was reopened. Because only new<br>events are displayed, you may not see all the<br>tabs at the bottom of the MalOp details<br>screen. For example, if there are no new<br>processes, the processes tab will not be<br>displayed.<br>You can investigate the primary root cause<br>from the**Investigate** drop down menu.|



