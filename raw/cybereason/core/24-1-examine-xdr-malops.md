proprietary detection rules managed by the Cybereason Security


Research team. For example, if multiple events share a similar IP

address or user identity as the main performer of the event, the


MalOp detection engine might group these events together in a

step.


Some steps, when performed together in a sequence, can also be

grouped together if they share a similar indicator. For example, if


you have a suspicious login activity followed by a malicious

activity with data, these steps can be grouped together.


In addition, the engine analyzes steps and connections between

steps to determine if these steps are considered a MalOp, based


on a number of criteria:


Total events


Variety of suspicious names

Variety of data sources


Data source category

Total targeted users/hosts


Events severity

Sequences of activity that match known attack patterns


Accuracy of detections, including how many times and how

often these detections occur, as many repeated detections


may indicate a false positive


Specific sequences of events that meet specified levels around


the criteria above are then considered MalOps.


The engine also calculates the severity for the MalOp based on


the assessment of the criteria above. The engine assigns a status

for the MalOp of **New** or **Auto-resolved** if all events associated


with the MalOp were previously mitigated by the connected

vendor platforms/products.


The MalOp detection engine enables you to narrow millions of

events to a much smaller percentage of suspicious events, and


then to a very limited number of MalOps that are highly likely to be

malicious and require your attention.


When the Cybereason platform generates an XDR Malop, the

platform groups suspicious events together based on the MITRE


ATT&CK tactic/technique/sub-technique for the events. Each of

these groupings is considered a "step" in the XDR MalOo. In these


steps, you are able to see all the suspicious events, which helps

you determine if there is a larger pattern of behavior across your


organization by comparing numerous suspicious events in the

same context of the MalOp "step".


When analyzing suspicious events, the Cybereason platform

focuses on the performer and victim identities involved in the


suspicious events. These values may differ from the traditional

source and target values, as the identity data can include various


user accounts, not just machine-based information. In some


cases, such as during lateral movement attack stages, the initial


victim becomes the performer. This is just one scenario in which

the platform would trigger a MalOp.


XDR MalOps are separate from the EDR MalOps (AI Hunting and

Endpoint Protection) found on the **Malops management** screen,


and only reference data gathered from XDR integrations.


Watch this video on XDR MalOps:


In this topic:


View and understand XDR MalOps


Search for and filter XDR MalOps

Understand the MalOp summary and scope


View the steps and events in the MalOp

Analyze the indicators of behavior in the MalOp


View potential response actions for the MalOp

Add MalOp feedback


XDR MalOp examples

Known issues - XDR MalOps

## View and understand XDR MalOps


After the platform generates the MalOps, you should view the

MalOps and understand what is happening.


You view XDR MalOps in the **XDR Malops** tab of the **XDR** screen.

For each MalOp, in the MalOp grid, you can view the following:


|Column|Description|
|---|---|
|MalOp name|The name of the MalOp, generated from the<br>suspicious events that triggered it. Select<br>this value to open the**XDR Malops details**<br>screen.|
|Severity|The calculated severity of the MalOp, based<br>on the contributing suspicious events and<br>steps involved. Values include:<br>High<br>Medium<br>Low<br>Informational (usually automatically<br>resolved MalOps)<br>For more details, see Suspicious Events<br>Severity Scores (/s/knowledge-base?<br>article=24-1-suspicious-events-severity-<br>scores&language=en_US#suspicious-<br>events-severity-scores)|
|MalOp ID|Unique identifer for the MalOp|
|Creation time|Time the platform created the MalOp|
|Last event in|The last time of an event was associated<br>with the MalOp|
|First event in|The frst time an event was associated with<br>this Malop.|
|MalOp steps|The sequence of unique threats that led to<br>the creation of the XDR MalOp. Each step<br>that makes up an XDR MalOp represents a<br>unique threat. For example, if there are 15<br>suspicious events that represent a phishing<br>attempt, the Cybereason platform will<br>consider that 1 step in the overall attack<br>story.|
|Total<br>suspicious<br>events|The number of suspicious events that<br>contributed to this MalOp. Click the value to<br>open the**Suspicious events** tab, which will<br>be fltered to only include these events.|
|Description|A feld populated by the Cybereason<br>platform that contains additional information<br>about the MalOp that may aid in<br>remediation.<br>For some XDR MalOps, this feld may be<br>empty.|


|Column|Description|
|---|---|
|Status|The position journey in the investigation and<br>remediation process. Values include:<br>New (Default)<br>On Hold<br>Under Investigation<br>Resolved<br>Close irrelevant<br>Reopened<br>Auto resolved|
|Recommended<br>actions|The recommended response actions to take<br>for the indicators in the different steps of the<br>MalOp.|
|Response<br>status|If you have enabled Response actions in<br>selected integrations, the status of response<br>actions for the different steps in the MalOp.<br>The percentage indicates the total amount<br>of successful completion of response<br>actions. For example, if you have four<br>possible response actions you can perform<br>from Cybereason XDR, and only two of the<br>actions have been completed successfully,<br>the percentage is**50%**.|


## Search for and filter XDR MalOps

You can search for an XDR MalOp by name or MalOp. From the


search bar, select **MalOp name** or **MalOp id** from the drop down

menu, and start typing the name or MalOp ID. The search box will


automatically list valid results.


You can filter the items in the MalOps list by creation time,


investigation status, or severity. Click the filter icon to open or


collapse the filter menu.


As you search or filter the XDR MalOps, the XDR MalOps screen

updates the displayed MalOps accordingly.

## Understand the MalOp summary and


When you first view the XDR MalOp details, you want to quickly

gain an idea of the MalOp's basic details, including what


happened and the scope of the suspected attack.


In the XDR MalOp details, on the left side of the MalOp details,


you can view the overview details about the MalOp, including the

**Summary** tab and the **Response** tab.


In the **Summary** pane, you can view the basic MalOp details,

including:


MalOp **Summary** : A text summary of the events that

contributed to the MalOp, as well as MalOp metadata (MalOp


ID, severity, status, etc.)

MalOp **Scope** : A list of affected assets (machines and users),


the steps involved, and the data sources reporting the

suspicious events


## View the steps and events in the MalOp

As each XDR MalOp is created based on the likely connection of


multiple suspicious events in the same attack chain, as part of the

XDR MalOp details, you can view the associated suspicious


events that are associated with this MalOp.


You view the steps in the MalOp in the **Overview** tab:


You view the suspicious events for a MalOp in the **Suspicious**

**events** tab of the XDR MalOp details:


This tab contains the following parts:


**Suspicious events** list: The suspicious events list for the


suspicious events associated with the step. These details are

the same as the details displayed in the **Suspicious events**


screen.

Step selector: Once you have selected a step and have the


details card open, you can use the step selector drop down

list to move between steps:


[For details on how to analyze suspicious events, see Analyze](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-suspicious-events&language=en_US#analyze-suspicious-events)

[Suspicious Events (/s/knowledge-base?article=24-1-analyze-](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-suspicious-events&language=en_US#analyze-suspicious-events)


[suspicious-events&language=en_US#analyze-suspicious-events).](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-suspicious-events&language=en_US#analyze-suspicious-events)


In addition, you can view the indicators of correlation between


steps to better understand how steps in the MalOp are related:


The top correlation list shows those items that are related between


steps, as well the number of occurrences of these items.

## Analyze the indicators of behavior in the


In addition to understanding the scope and steps in a MalOp, you


also should view the indicators of behavior associated with a

MalOp. Analyzing these indicators will help you confirm whether


the MalOp represents actual malicious behavior or a false positive.


In the XDR MalOp details, the indicators of behavior display in the


**Detected elements** tab:


The Detected elements in the XDR MalOp include related


indicators that are not physical assets in your organization. These

elements may include:


Message

Attachment (File)


Links

Connection


Access (IP address)


For each detected indicator, you view relevant details to help you


determine the malicious nature of this indicator or not. Each

indicator in the Detected Elements tab list will have different


details, depending on the type of Element:


|Element|Displayed Indicators|
|---|---|
|Message|**Suspicious name:** The name of the event<br>to which this message is associated<br>**Action taken:** Any action taken by the<br>integrated platform for this message<br>**Subject:** The message subject<br>**Sender:** Email address of the message<br>sender<br>**Recipients:** Email addresses of recipients<br>of the message<br>**Links:** Links included in the message<br>**Attachments:** Total number of attachments<br>for this message|
|Attachments|**Suspicious name:** The name of the event<br>to which these attachments are associated<br>**Action taken:** An action taken by the<br>integrated platform for these attachment<br>fles<br>**File name:** The name of the attachment fle<br>**File sha256:** The SHA-256 fle hash value<br>for the attachment fle<br>**File size:** The size of the attachment fle|
|Links|**Suspicious name:** The name of the event<br>to which these links are associated<br>**Action taken:** Any action taken by the<br>integrated platform for this link<br>**URL:** The URL displayed in this link|
|Connection|**Suspicious name:** The name of the event<br>to which this connection is associated<br>**Action taken:** Any action taken by the<br>integrated platform for this connection<br>**Connection name:** The name of the<br>connection<br>**Domain name:** The domain name<br>associated with this connection<br>**Connection direction:** The direction for<br>this connection<br>**Protocol:** The protocol used for this<br>connection<br>**Target application:** The application target<br>for this connection|


|Element|Displayed Indicators|
|---|---|
|Login|**Suspicious name:** The name of the event<br>to which this access is associated<br>**Action taken:** Any action taken by the<br>integrated platform for this access address<br>**Source IP:** The source IP address for this<br>access<br>**Target resource:** The target for this<br>access<br>**Source location city:** The city for the IP<br>address associated with this login<br>**Source location country/region:** The<br>country/region for the IP address<br>associated with this login<br>**Auth details:** Authentication details<br>associated with this login|



The **Detected elements** tab displays up to 50 items per element.

If there are more than 50, the list will display the top 50 indicators.


In the list of the top 50 events, unmitigated events where no action

has been taken will be displayed before events where there is an


action taken.


If you would like to see all indicators, you can view these

indicators per suspicious event in the **Suspicious events** tab.


These indicators are displayed in the **Additional details** section of

the event details.


For the details, if the value of a specific field is a single value,

such as the sender email address for a Message, you will see the


value. If there are a collection of values, such as the number of

attachments for an email message, you will see the total number


of items.


You can filter the list by the MalOp step (just like in the


**Suspicious events** tab) or by the action taken to help you

address indicators where no action has been taken:


## View potential response actions for the

To help resolve the MalOp, you will need to take response actions.


You can perform these in your third-party integrated platforms or

directly from Cybereason XDR (for supported actions in supported


integrations).


In the XDR MalOp details, the recommended response actions are


displayed in the **Overview** section, in the **Response** tab.


Follow the recommendations on the specific items or perform


these actions from Cybereason XDR as needed. For details on

[how to perform XDR response, see Perform Response for XDR](https://nest.cybereason.com/s/knowledge-base?article=24-1-perform-response-for-xdr-malops&language=en_US#perform-response-for-xdr-malops)


[MalOps (/s/knowledge-base?article=24-1-perform-response-for-](https://nest.cybereason.com/s/knowledge-base?article=24-1-perform-response-for-xdr-malops&language=en_US#perform-response-for-xdr-malops)

[xdr-malops&language=en_US#perform-response-for-xdr-malops).](https://nest.cybereason.com/s/knowledge-base?article=24-1-perform-response-for-xdr-malops&language=en_US#perform-response-for-xdr-malops)

## Add MalOp feedback


To help the Cybereason Security Research team, for any MalOp,

you can provide feedback on the MalOp, including whether the


MalOp is a legitimately malicious MalOp or a false positive, the

accuracy of the events that were associated with the MalOp, and


what types of behaviors in your organization are found in the

MalOp.


The Cybereason Security research team takes this feedback to
further refine the out-of-the-box detection rules to help generate


the most accurate and meaningful MalOps for real-life security

needs.

## XDR MalOp examples


The following examples describe how you might use the **XDR**

**MalOps**, **XDR MalOp details**, and **Suspicious Events** screens to


investigate a potential attack.


|Example|Details|
|---|---|
|Example 1:<br>Cloud<br>account<br>takeover|The following XDR MalOp shows a**Cloud**<br>**account takeover** XDR MalOp.<br>In the MalOp details, you can see the steps in<br>the attack sequence.<br>**Step 1: Additional Cloud Roles**: A GCP user<br>gains owner permissions on their account.<br>This account manipulation allows the user to<br>create additional users, as seen in step 2.<br>**Step 2: Cloud Account**: The user adds a new<br>GCP account. This could be an attacker's<br>attempt to maintain persistence in the system.<br>**Step 3: Data Destruction**: Using the new<br>account, the attacker compromises GCP<br>resources by destroying data.<br>**Step 4: Clear Linux or Mac System Logs**:<br>The attacker attempts to evade detection by<br>clearing the audit log.<br>In the**Suspicious Events** tab, you can see<br>the 5 suspicious events that contributed to<br>this XDR MalOp:<br>Notice that although there are 5 events, the<br>Malop only contains 4 steps. This is because<br>the Cybereason platform recognizes that<br>certain separate events (such as**GCP new**<br>**user gained new permissions** and**Owner**<br>**permissions added to account**) represent<br>one action taken by the attacker. By hovering<br>over a step in the details screen, you can see<br>the specifc suspicious events that contribute<br>to the step.|


|Example|Details|
|---|---|
|Example 2:<br>Business<br>email<br>compromise|The following XDR Malop details screen<br>displays a**Business Email Compromise**<br>XDR Malop.<br>From the**Overview tab**, we can determine<br>that the following unique steps were taken:<br>**Step 1: Spearphishing Attachment**: The<br>email account**do_not_reply@capitol-**<br>**supply.com (mailto:do_not_reply@capitol-**<br>**supply.com)** attempts to gain initial access to<br>a system by sending targeted emails to select<br>company email accounts, including<br>**roberte@demo.loc**<br>**(mailto:roberte@demo.loc)**.<br>**Step 2: Valid Accounts**: The user**roberte**<br>reports fnding suspicious login activity on<br>their account.<br>In the**Suspicious events** tab of the MalOp<br>details you can see the 12 suspicious events<br>that contributed to this XDR MalOp:<br>The Cybereason platform identifes each<br>phishing attempt as belonging to a single<br>unique initial access attempt, and further<br>recognizes that a victim in the frst step<br>subsequently reported suspicious login<br>activity.|


|Example|Details|
|---|---|
|Example 3:<br>Data<br>Manipulation|The following XDR MalOp detected by the<br>XDR MalOp detection engine shows a**Data**<br>**manipulation** MalOP with malicious access to<br>a network and misuse of an organization's<br>data.<br>In the**Overview** tab of the MalOp details, you<br>can see the following steps in the MalOp:<br>**Step 1: Valid accounts login:** An attacker<br>targeted 6 different user identities to gain<br>access to the company's network through a<br>Microsoft program.<br>If you look at the**Suspicious events** tab for<br>this MalOp, you will see 22 different events, all<br>with the same IP address:<br>Note|


|Example|Details|
|---|---|
||Although this example does not show the<br>IP address of**10.10.10.10** for all events, if<br>you look at the**xdrqa+1** value and hover<br>over it, this column would also display the<br>IP address**10.10.10.10** in addition to the<br>**xdrqa** value.<br>**Step 2: Data manipulation:** Following the<br>access to the system, the MalOp detection<br>engine found the**resttest101012** identity<br>performed data destruction activities after it<br>gained access in the previous step.<br>Because the detection engine noticed the<br>same user identity in both steps, the steps are<br>connected together in the same attack<br>sequence.<br>If you look at the**Suspicious events** tab for<br>this step, you will see the IP address of<br>**10.10.10.10**:|



