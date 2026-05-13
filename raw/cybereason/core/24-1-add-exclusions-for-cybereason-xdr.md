For **Event** -based exclusions, you specify one or more of the


following:


Note


You can select values that have already been used or

enter your own value.






|Item|Description|
|---|---|
|**Source**<br>**identity**|The source identity in the event reported<br>from the third-party connected data<br>source.|
|**Target**<br>**identity**|The target identity in the event reported<br>from the third-party connected data<br>source.|
|**Suspicious**<br>**event name**|The name of the suspicious event.<br>For a full list of suspicious events reported<br>for each integration, see the**Use Cases**<br>tab in the relevant integration page.|
|**MITRE**<br>**ATT&CK**<br>**technique**|The MITRE ATT&CK tactic/technique/sub-<br>technique reported with each suspicious<br>event. YOu use this if you want to exclude<br>all events tagged with a particular tactic,<br>technique, or sub-technique, regardless<br>of the data source or specifc event.|
|**Data source**|The third-party connected data source for<br>an integration. You can use this property if<br>you want to exclude all events from a<br>particular data source.|
|**User agent**|The user agent information. You can use<br>this property if you want to exclude all<br>events from a particular user agent<br>version.|


For **Artifact** -based exclusions, you specify one or more of the


following, depending on the type of artifact:


















|Artifact type|Items to specify|
|---|---|
|IP address|IP address|
|Domain|Source host name<br>Source User IDs<br>Source Asset Names<br>Source IP Name<br>Target User IDs<br>Target Asset Names<br>Target Host Name<br>Target IP Name|
|Hash|File hash value|
|File name|Source File Name<br>Target File Name<br>Process File Name|
|Email|Source Email Address<br>Target Email Address|
|Message|Email IDs<br>Source Emails<br>Target Emails<br>Subjects<br>Target Host Name<br>Source User IDs|


|Artifact type|Items to specify|
|---|---|
|User logins|User name|


6. Optionally, enter a description for the exclusion.


7. To see the events that would have previously been excluded


for event-based exclusion, click **Run preview**


8. Click **Save** .


Your exclusion is added with the list of exclusions in the

**Exclusions** tab and takes effect immediately.

## Add an exclusion from the Suspicious

## Events screen


In the course of your analysis and triage of reported suspicious
events, if you find a specific suspicious event that is not relevant,


you can automatically create the exclusion based on the event

directly from the Suspicious Events screen.


**To add an exclusion from the Suspicious Events screen,**

**follow these steps:**


1. In the **Suspicious Events** screen, select the event to exclude.

2. Above the events grid, click **Create as exclusion** .


The Cybereason platform opens the **Create New Exclusion**
**Rule** dialog with the relevant criteria already filled:


Edit these fields as needed.

3. Click **Save** .





