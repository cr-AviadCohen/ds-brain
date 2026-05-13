[view-malops-with-the-data-platform-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)


[architecture&language=en_US#view-malops-with-the-data-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)

[platform-architecture) topic instead.](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)


The above screenshot calls out the six main parts of the **Malops**

**management** screen:


1. Malops management dashboard
2. Search and filter options


3. Quick filters

4. View options


5. MalOps list

[6. Response options (see Remediate MalOps (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)


[base?article=24-1-remediate-](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)

[malops&language=en_US#remediate-malops))](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)

## View the Malops management


The dashboard in the **Malops management** screen presents

important information about the environment in a graphical, easy


to read format.


The dashboard widgets update based on the time frame you


select in the time frame filter.


Dashboard widgets include:






|MalOps<br>view|Description|
|---|---|
|**Active**<br>**MalOps**|Shows the number of active and total MalOps<br>in your organization as a ratio.|
|**MalOps by**<br>**detection**<br>**module**|Shows the number of AI Hunt MalOps, or<br>MalOps that the Cybereason platform Cross<br>Machine Correlation Engine created, as well as<br>the number of Endpoint Protection MalOps, or<br>MalOps that the Cybereason platform NGAV<br>features created. This box also shows the<br>connection status of Cybereason's threat<br>intelligence services.|
|**Machines**<br>**overview**|Information about the number of online, offine,<br>infected, and clean machines. Infected<br>machines have at least one active MalOp.<br>Clean machines have no active MalOps.|


|MalOps<br>view|Description|
|---|---|
|**MalOps**<br>**trend over**<br>**past week**|A graph showing the trend of MalOp creation<br>over the past week.|


## Search for MalOps

Using the search field, you can enter free text to search for

MalOps by a custom value.


The Cybereason platform returns MalOps that contain your search

term anywhere in their metadata. For example, a search for


'admin' will return MalOps that have affected users with 'admin' in

their username, as well as MalOps that have affected machines


with 'admin' in their name.

## Filter Malops


You can filter MalOps by time frame or by a variety of MalOp

characteristics.


Select the time frame drop-down menu to limit results to MalOps

triggered today, last week, last month, last three months, last year,


or all time.


Select the Filters button to toggle the filter menu. You can filter by


MalOp state, Detection module, Priority, OS type, machine status,

user privileges, or labels.


The numbers next to the filters represent the number of MalOps
that have that property. As you add more filters, the numbers next


to the other filters update.


The quick filters allow you to filter by:


AI hunting MalOps only

Escalated Malops (MalOps that a lower-level analyst has


escalated)


Active MalOps

## Change how MalOps are displayed


Next to the **View** label, choose between the **Grid view** and **Card**

**view** . The only difference between the two views is in how the


Malop information is presented in the **Subject** column, as

described below.








|View|Description|Suitable for|
|---|---|---|
|Grid|Displays a brief description of<br>the Malop, including the<br>triggering item and a matching<br>icon (e.g., Firefox logo for Firefox<br>processes)|Actively working<br>with Malops, such<br>as assigning<br>priority, escalating,<br>or responding.|
|Card|Displays information about the<br>Malop, including the triggering<br>item, primary root cause, and<br>detection type. This view also<br>displays different infographics<br>depending on the subject's<br>behavior (see the following<br>table).|Quickly assessing<br>threats.|



If you select the **Card view**, you are able to see additional

information. The following table describes the infographics that


are visible when the Subject column card view is active.






|Behavior|Graphic|Graphic Description|
|---|---|---|
|Command and<br>control||Network icon on a server<br>connection to the target<br>machine.|
|Reconnaissance||Process icon with radar<br>image connected to<br>target machine.|
|Injection||Process icon with code<br>pointing to an additional<br>process connected to the<br>target machine.|


|Behavior|Graphic|Graphic Description|
|---|---|---|
|Persistence||Process icon pointing to<br>an anchor connected to<br>the target machine.|
|Ransomware||Ransomware icon<br>connected to locked fles<br>connected to the target<br>machine.|
|Lateral<br>movement||Process icon with an<br>arrow branching to<br>multiple machines<br>connected to the initial<br>target machine.|
|Credential theft||Process icon pointing to a<br>badge connected to the<br>target machine.|
|Known malware||Process icon with a shield<br>connected to target<br>machine.|

## Select a Sensor Group





Users with the Local Analyst L1 and L2 role can view MalOps


associated with the sensors in the sensor groups the user has

permissions for.


To select which sensor group MalOps to view, check the relevant

boxes in the sensor group drop-down menu on the right, above


the list of Malops.


For more information on local analysts and sensor grouping, see

[Manage Sensor Groups (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)


[manage-sensor-groups&language=en_US#manage-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)

[groups).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)


## Select data to view

Use the column icon on the upper right of the results to customize


which columns to view.


Column options include:








|Column<br>name|Description|Values|
|---|---|---|
|State<br>(icon)|The type<br>and state of<br>the Malop|MalOp type:<br>AI Hunting MalOp<br>Endpoint Protection MalOp<br>MalOp states:<br>Active (red)<br>Inactive (orange)<br>Resolved (green)<br>Excluded (grey)<br>For more information, see Malop Types<br>and Components (/s/knowledge-base?<br>article=24-1-malop-types-and-<br>components&language=en_US#malop-<br>types-and-components).|
|Subject|Brief<br>description<br>of the item<br>involved in<br>the MalOp|Grid view:<br>Triggering item<br>Item type (icon)<br>Card view:<br>Detection type<br>Triggering item<br>Item type (icon)<br>Threat engine|


|Column<br>name|Description|Values|
|---|---|---|
|Resolved<br>by|Populated if<br>the MalOp<br>was<br>resolved.|One of the following:<br>Cybereason: The Cybereason<br>platform automatically prevented,<br>disinfected, or quarantined a<br>malicious item.<br>Analyst username: An analyst An<br>analyst manually resolves the<br>MalOp using the 'Mark as<br>remediated/resolved' button in the<br>**Malops management** or**Malop**<br>**details** screen.|
|Affected<br>machines|Machines<br>associated<br>with the<br>MalOp|Machine name, or machine count if<br>more than one machine is involved|
|OS type<br>(icon)|Machine<br>types<br>associated<br>with the<br>MalOp|Windows<br>Linux<br>MacOS|
|Affected<br>users|Users<br>associated<br>with the<br>MalOp|User name, or user count if more than<br>one user is involved|
|User<br>privileges<br>(icon)|Type of<br>users<br>associated<br>with the<br>MalOp|Administrator<br>Domain user<br>Local system|


|Column<br>name|Description|Values|
|---|---|---|
|Detection<br>description|The type of<br>behavior<br>that<br>triggered<br>the Malop|A basic description of the root cause<br>behavior that led to the Cybereason<br>platform creating the MalOp. This<br>description is different than the full<br>description that is available in the<br>overview section of the MalOp details<br>for the MalOp.<br>For Endpoint Protection Malops:<br>Known malware<br>Unknown malware detected by<br>Artifcial Intelligence<br>Exploit attempt (detected by<br>Exploit Protection)<br>Malicious payload loaded to<br>memory (detected by Fileless<br>Protection)<br>Process identifed by Behavioral<br>Execution Prevention<br>.NET application used to execute<br>malicious command (detected by<br>Fileless Protection)<br>PowerShell used to execute<br>suspicious download commands<br>(detected by Fileless Protection)<br>PowerShell used to download fle<br>from malicious site (detected by<br>Fileless Protection)<br>Malicious foating module loaded to<br>.NET application (detected by<br>Fileless Protection)<br>Document detected to contain<br>malicious code (detected by<br>Behavioral Document Protection)<br>Malware detected by Variant File<br>Prevention<br>Application marked for prevention<br>attempted to execute a process<br>For AI Hunting MalOps, see the list of<br>MalOp types in the MalOp Types topic.|
|Detection<br>modules|Which<br>Cybereason<br>component<br>detected the<br>malicious<br>behavior|AI Hunting<br>Anti-Malware<br>AI-based Anti-Malware<br>PowerShell and .NET protection<br>Anti-Ransomware|


|Column<br>name|Description|Values|
|---|---|---|
|Auto<br>response|The<br>Cybereason<br>platform<br>NGAV<br>automatic<br>response to<br>the Endpoint<br>Protection<br>MalOp.|Disinfected<br>Failed to disinfect<br>Detected<br>Prevented<br>Done<br>Excluded<br>Deleting on restart<br>Quarantined|
|Start time|The time the<br>MalOp was<br>triggered|Month day, year at hh:mm:ss AM/PM<br>timezone (ex. September 25, 2019 at<br>01:22:45 PM GMT-5)|
|Update<br>time|The last time<br>the MalOp<br>was<br>updated|Month day, year at hh:mm:ss AM/PM<br>timezone|
|Escalation|Whether or<br>not the<br>MalOp is<br>currently<br>escalated|Escalate button or 'x' button to de-<br>escalate|
|Severity|The severity<br>of the threat<br>as<br>determined<br>by<br>Cybereason.|High<br>Medium<br>Low|
|Priority|The priority<br>setting for<br>the MalOp|High<br>Medium<br>Low|
|Labels|Custom<br>labels|Label name|

## Group results

To organize your view of MalOps by machine, detection type, and

label, select a **Group by** option from the upper right of the Malops


list. The left-most button removes the grouping selection. Each

MalOp remains on an individual line and a banner is visible above


each group.



