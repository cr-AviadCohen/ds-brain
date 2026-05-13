Each event contains the name of the event reported from your

connected integration platform, as well as other selected details


about the event.


You can customize what event information to display in each row.


Click the and select the relevant columns:






|Column|Description|
|---|---|
|Suspicious<br>name|The event name reported in the integrated<br>vendor platform or product.|
|Severity|Threat level as reported by the data source.<br>Values include:<br>Informational<br>Low<br>Medium<br>High<br>Critical<br>Note<br>Presently, Suspicious events do not use the<br>**Critical** severity level. This level is reserved<br>for activities and assets that are critical to an<br>organization.|
|Data<br>source|The connected platform/product that generated<br>the suspicious event alert.|
|Detection<br>time|The time the suspicious event occurred as<br>reported by the data source.<br>The format for the date is**dd Month yyyy h:mm**<br>**timezone**|
|Source<br>identity|The entity/item that initiated the suspicious<br>activity or behavior reported in the event.<br>Values include:<br>Email<br>User<br>Hostname<br>IP|


|Column|Description|
|---|---|
|Target<br>identity|The entity/item that was the target of the<br>suspicious activity or behavior reported in the<br>event.<br>Values include:<br>Email<br>User<br>Hostname<br>IP|


|Column|Description|
|---|---|
|Action<br>taken|The Cybereason platform value for the action<br>taken by the security tool in the data source that<br>reported the suspicious event.<br>Values include:<br>Allow<br>Block<br>Alert<br>Allow with modifcation<br>Delete<br>Fail<br>Quarantine<br>Unknown<br>These values correspond with different values in<br>the various integrations. To see the vendor or<br>product-specifc action that was taken by your<br>integrated platform, in the**Additional details**<br>section of the event details, fnd the**Vendor**<br>**action** feld:<br>**Examples:**<br>1. In a Suspicious event from Microsoft 365, if<br>Microsoft 365 took the action**MoveToJmf**,<br>Cybereason XDR reports this as<br>**ALLOW_WITH_MODIFICATION**.<br>2. In a Suspicious event from Fortinet Fortigate,<br>if Fortinet Fortigate took the actions such as<br>**accept**, **allow**, or**passthrough**,<br>Cybereason XDR reports this as**ALLOW**.<br>3. In a Suspicious event from Okta, Okta took<br>the action**FAILURE** ,**DENY**, or<br>**DEFERRED**, Cybereason XDR reports this<br>as**BLOCK**.|
|MITRE<br>ATT&CK|A MITRE ATT&CK tactic, technique, or sub-<br>technique that characterizes the item or behavior<br>that triggered the alert.|


|Column|Description|
|---|---|
|Status|Status of the event set by you or another analyst.<br>Values include:<br>Pending (default)<br>Archived<br>Escalated|
|Suspicious<br>UUID|The individual event's unique identifer within the<br>Cybereason platform.|
|Event ID|The event ID for the event reported by the data<br>source that reported the event.|
|Suspicious<br>code|The identifer of a specifc alert name, which<br>usually exists in policy-based solutions that<br>report the policy/rule name and its id.|
|Related<br>MalOp|A link to the XDR Malop(s) associated with this<br>suspicious event. Click the value to open the<br>**XDR Malops** tab, which will be fltered to only<br>include the selected Malop.|


## View suspicious events from your

## Cybereason platform

Note


The ability to view suspicious events from your Cybereason

platform is not generally available. Contact your Customer


Success Manager to gain access to this feature.


In addition to events ingested from your connected integrations,


you also have the ability to view detected events from your

Cybereason platform. These events are equivalent to detections


related to Endpoint Protection and AI Auto Hunting MalOps.


Events from your Cybereason platform are automatically exported


from the Cross Machine Platform engine's data and ingested by

Cybereason XDR. Once Cybereason XDR parses these events,


the events are displayed in the **Suspicious events** screen.


Events from your Cybereason platform contain the following:


|Column|Description|
|---|---|
|Alert name|The name for the event in your<br>Cybereason platform.|
|Data source|The source for the alert.<br>For events related to Endpoint Protection<br>MalOps, this value is**Cybereason**<br>**NGAV**. For AI Hunting MalOps, the value<br>is**Cybereason EDR**.|
|Detection time|The time the suspicious event was frst<br>detected by the Cybereason platform.<br>The format for the date is is**dd MM yyyy**<br>**hh:mm timezone**.|
|Severity|Threat level of the event. Values include:<br>Informational<br>Low<br>Medium<br>High<br>Critical<br>Note<br>Presently, Suspicious events do not<br>use the**Critical** severity level. This<br>level is reserved for activities and<br>assets that are critical to an<br>organization.|
|Source identity|The asset the initiated the suspicious<br>activity or behavior reported in the event.<br>This value is the machine on which the<br>event occurred.|


|Column|Description|
|---|---|
|Action taken<br>Detection<br>status/protection<br>type|Action taken by the Cybereason<br>platform.<br>If you are viewing the**Detection**<br>**status/protection type** feld, possible<br>values include:<br>Collected<br>Deleting on restart<br>Detected<br>Disinfected<br>Failed to disinfect<br>Failed to prevent<br>Failed to quarantine<br>Mitigated<br>Prevented<br>Quarantined<br>Unknown<br>Detected<br>Allowlist<br>If you are viewing the**Action taken** feld,<br>possible values include:<br>Allow<br>Block<br>Alert<br>Allow with modifcaton<br>Delete<br>Fail<br>Quarantine<br>Unknown|
|MITRE ATT&CK|A MITRE ATT&CK tactic, technique, or<br>sub-technique that characterizes the<br>item or behavior that triggered the alert.|
|Type|The type of event.|
|Status|The status for the event set by you or<br>one of the analysts on your team.|
|Suspicious UUID|The event ID used by the Cybereason<br>platform for the event.|


|Column|Description|
|---|---|
|Detection Type|The type of item to which the event is<br>related. Possible values include:<br>Module type<br>Signature type<br>File type<br>Domain type<br>Details JSON<br>Fingerprint|
|Vendor detection<br>type|The detection engine the Cybereason<br>platform used to detect the event.<br>Possible values include:<br>Exploit Protection<br>Application Control<br>Anti-Malware<br>Behavioral Document Protection<br>AI Hunting<br>Mobile<br>Anti-Ransomware<br>Behavioral execution prevention<br>Fileless protection<br>AI-based Anti-Malware<br>Sensor Tampering Protection<br>Variant File Protection<br>Variant Payload Protection|
|Machine details|Detials on the event on the machine,<br>including:<br>Source (machine) hostname<br>Source (machine) OS type and OS<br>version<br>Source (machine) asset id (pylum<br>ID)|
|File details|Details on the fle associated with the<br>event, including:<br>File name<br>Path to the fle<br>File hashes (MD5 and SHA-256)<br>File size|


|Column|Description|
|---|---|
|Process details|Detials on the process associated with<br>the event, including:<br>Process name<br>Process ID and GUID<br>Command line for the process<br>Parent process for the process<br>Parent process GUID|
|User details|Details for the user associated with the<br>event, including:<br>User name/domain<br>User privilege levels|
|Vendor action|The action taken by the Cybereason<br>platform for this event.|
|Vendor category|The related suspicious raised by the<br>Cybereason platform for this event.|

## Search and filter suspicious events

The filter and search capabilities allow you to quickly focus on

alerts of interest to you and your team.

## Search for events


Use the search bar at the top of the **Suspicious Events** screen to
search for events by one of the following fields:


Alert name

MITRE ATT&CK technique or tactic


Source identity

Target identity


When you select the search box, the platform displays a list of

possible values on which to search.


Subsequent searches add to the existing search criteria, as shown

in the following image. To remove a search criteria, click the **X** in


the relevant filter bubble.


## Filter events

To filter which events display on the **Suspicious Events** screen,


click the filter icon and select one or more filters to apply.


Filter options include:


Time (Today or last 7, 14, 30, or 90 days)

Status


Severity

Action taken


Data source


Note


Filters do not affect how events are generated or detected.

Filters only affect how events are displayed.

## Investigate the associated MITRE tactic


The Cybereason platform enriches each suspicious event with a

tactic, technique, or sub-technique from the MITRE ATT&CK


matrix. This relationship allows analysts to:

Gain visibility into MITRE threat trends at a specific point in


time

Focus on specific threat categories across vendors


Further investigate threat tactics and mitigations as presented

by MITRE


Select an item in the MITRE ATT&CK column to view more

information about the MITRE tactic, technique, or sub-technique


[on the MITRE ATT&CK (https://attack.mitre.org) website.](https://attack.mitre.org/)

## Investigate a specific suspicious event


To further investigate a specific suspicious event, select the event


name from the list of events to open the event details pane. The

details pane contains more information about the event.


## Set suspicious event status

As you analyze each suspicious event, you can update the status

to ensure that other analysts in your organization understand its


place in the workflow.


Use any of the following status values to update a suspicious


event:


**Pending** : Events are pending if a status has not been set


**Archived** : Archive an alert if it is not relevant to your

organization or requires tuning


**Escalated** : Escalate an alert if it requires more investigation


To change the status of an suspicious event, do one of the


following:


For individual suspicions, click the three vertical dots on the


right end of the suspicious event entry and select a status to

apply to the event.


For one or more suspicions, select the checkbox next to the

suspicious event entry or entries, click the **Set Status** button


on the top right of the screen, and select a status to apply to

the selected events.

## - Known issues Suspicious events


When you filter results, the system retrieves all matching

items, but only displays up to 10K on the **Suspicious Events**


screen. The results number listed above the items in the

**Suspicious Events** screen, as well as the numbers next to


the filter options, reflect the _total_ number of results, which

could be greater than 10K.


When filtering suspicious events, if you use the autocomplete

functionality to enter a search string, the Suspicious events


screen will return all events, regardless of the time filter you

selected.


In the table with the list of suspicious events, if you resize a

column to the minimum size, no characters will display in the


minimized size to show there is a value in that column.

When copying values from the Severity or Action columns, the


value is not copied with the exact case for the value as it was

displayed in the screen. For example, the value **Alert** is


copied as **ALERT** .


On the Suspicious events screen, it is possible to hide all


columns in the Suspicious events list.

For environments in Japanese, the values for the **Creation**


**time** for any suspicious events are not translated into

Japanese.



