If you are using an environment without the newer Data

Platform architecture, your **Malops management** screen may


[look different than what is described here. Visit the View](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops&language=en_US#view-malops)

[Malops (/s/knowledge-base?article=24-1-view-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops&language=en_US#view-malops)


[malops&language=en_US#view-malops) topic instead.](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops&language=en_US#view-malops)


The above screenshot calls out the six main parts of the Malops


management screen:


1. View overall statistics from the Malops management


dashboard

2. Search for MalOps in your environment


3. Filter MalOps by specific characteristics

4. Change how MalOps appear on the **Malops management**


screen

5. View details about each MalOp


[6. Respond to MalOps (see Understand Threat Activity](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-threat-activity&language=en_US#understand-threat-activity)


[(/s/knowledge-base?article=24-1-understand-threat-](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-threat-activity&language=en_US#understand-threat-activity)


[activity&language=en_US#understand-threat-activity))](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-threat-activity&language=en_US#understand-threat-activity)

## View the Malops management


The dashboard in the **Malops management** screen presents


important information about the environment in a graphical, easy

to read format.


Regardless of your filters, the dashboard on top of the MalOp

Management table shows the data based on the **Last One Year**


time filter.


Dashboard widgets include:






|MalOps<br>view|Description|
|---|---|
|**Active**<br>**MalOps**|Shows the number of active and total MalOps<br>in your organization as a ratio.|
|**MalOps by**<br>**detection**<br>**module**|Shows the number of AI Hunt MalOps, or<br>MalOps that the Cybereason platform Cross<br>Machine Correlation Engine created, as well as<br>the number of Endpoint Protection MalOps, or<br>MalOps that the Cybereason platform NGAV<br>features created. This box also shows the<br>connection status of Cybereason's threat<br>intelligence services.|


|MalOps<br>view|Description|
|---|---|
|**Machines**<br>**overview**|Information about the number of online, offine,<br>infected, and clean machines. Infected<br>machines have at least one active MalOp.<br>Clean machines have no active MalOps.|
|**MalOps**<br>**trend over**<br>**past week**|A graph showing the trend of MalOp creation<br>over the past week.|



You can minimize the dashboard to view more MalOps in the grid:

## Search for MalOps


Using the search feature, you can select a MalOp characteristic


(Element) and enter free text to search for MalOps whose selected

characteristic contains your text.


You can search by a MalOp's associated:


Subject


MalOp name

Label


Root cause hash

MalOp GUID


Machine name

User Name


For example, a search for **admin** with **Machines** selected will

return all Malops that have affected machines with **admin** in the


name, but will not return MalOps where **admin** only appears

elsewhere, such as within an affected user's username.

## Filter Malops


Select the filter icon to open the filter menu. You can filter by:


|Filter|Example|
|---|---|
|Time range|The time the MalOp was created. You can<br>select**All time**, **Today**, **Last week**, **Last**<br>**month**, **Last three months**, **Last year**, or a<br>custom time range.<br>Note<br>When you flter by a time range, the<br>Malops management screen updates<br>the MalOps in the list, but not the<br>dashboard widgets.|
|MalOp<br>investigation<br>status||
|MalOp state|The state of the MalOp that the Cybereason<br>platform assigns for the MalOp.|
|Detection<br>engine|The engine that detected a MalOp.|


|Filter|Example|
|---|---|
|Detection type|Filter by Potentially Unwanted Programs<br>(PUP) (versions 23.2.20 and later).|
|MalOp priority|The priority an analyst assigned for a<br>MalOp.|
|MalOp severity|The severity of the MalOp assigned by an<br>analyst. You can flter by**High**, **Medium**, or<br>**Low**.|
|MalOp labels|Any custom labels applied to a MalOp.|
|MalOp type|(Versions 23.2.126 and later) The type of<br>MalOp. You can flter by**EDR** (AI Hunting)<br>or**NGAV** (Endpoint Protection MalOps).|
|Machine status|The status of the machines on which the<br>activity represented in a MalOp occurred.|


|Filter|Example|
|---|---|
|OS type|The type of operating system (Windows,<br>macOS, or Linux) for the machines<br>associated with a MalOp.|
|Protection type|The automatic protection action taken by the<br>sensor for the activity represented in a<br>MalOp.|
|User privileges|The privilege level for the users associated<br>with the MalOp.|


Applied filters display above the results, which enables you to


remove one of the filters while viewing the results.


Click **Clear filters** to remove the current filters:


For a description of the different values used in the filters, see the


section below on **Select data to view** .


## Change how Malops are displayed

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

## Select a sensor group





If you enable sensor grouping, analysts with the Local Analyst L1


and L2 role can view MalOps associated with the sensors in the

sensor groups the user has permissions for.


To select which sensor group MalOps to view, check the relevant

boxes in the sensor group drop-down menu on the right, above


the list of MalOps.


For more information on local analysts and sensor grouping, see

[Manage Sensor Groups (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)


[manage-sensor-groups&language=en_US#manage-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)

[groups).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)


|Column<br>name|Description|
|---|---|
|State (icon)|The type<br>and state of<br>the MalOp|
|Subject|Brief<br>description<br>of the item<br>involved in<br>the MalOp|
|Group (for<br>environments<br>with sensor<br>grouping<br>enabled)|The names<br>of the<br>groups to<br>which the<br>machines<br>associated<br>with the<br>MalOp<br>belong.|


|Column<br>name|Description|
|---|---|
|Resolved by|Populated if<br>the MalOp<br>was<br>resolved.|
|Affected<br>machines|Machines<br>associated<br>with the<br>MalOp|
|OS type<br>(icon)|Machine<br>types<br>associated<br>with the<br>MalOp|
|Affected<br>users|Users<br>associated<br>with the<br>MalOp|
|User<br>privileges<br>(icon)|Type of<br>users<br>associated<br>with the<br>MalOp|


|Column<br>name|Description|
|---|---|
|Detection<br>description|The type of<br>behavior<br>that<br>triggered<br>the MalOp|


|Column<br>name|Description|
|---|---|
|Detection<br>modules|Which<br>Cybereason<br>component<br>detected the<br>malicious<br>behavior|
|Start time|The time the<br>MalOp was<br>triggered|
|Update time|The last time<br>the MalOp<br>was<br>updated|
|Escalation|Whether or<br>not the<br>MalOp is<br>currently<br>escalated|
|Severity|The severity<br>of the threat<br>as<br>determined<br>by<br>Cybereason.|
|Priority|The priority<br>setting for<br>the MalOp|
|Labels|Custom<br>labels|


|Column<br>name|Description|Values|
|---|---|---|
|Protection<br>type|The type of<br>automatic<br>prevention<br>action taken<br>by the<br>sensor on<br>the<br>machines<br>associated<br>with the<br>MalOp.|Any of the following values:<br>Detected: The sensor detected the<br>activity but did not prevent the<br>execution of the activity.<br>Prevented: The sensor prevented<br>the activity<br>Quarantined: The sensor<br>quarantined the fle associated with<br>the MalOp.<br>Disinfected: The sensor removed<br>the fle associated with the MalOp<br>from the machine.<br>Failed: The sensor failed to remove<br>the fle associated with the MalOp<br>from the machine.<br>Failed to quarantine: The sensor<br>failed to quarantine a fle<br>associated with the MalOp.<br>Failed to prevent: The sensor failed<br>to stop the execution of the activity<br>that caused the MalOp.<br>Deleting on restart: The sensor will<br>remove the fle after a machine<br>restart.<br>Mitigated: (Mobile MalOps only)<br>The sensor already took actions to<br>mitigate the threat associated with<br>the MalOp.|



As needed, you can sort the columns accordingly to help you

view the MalOps in a more meaningful way.





