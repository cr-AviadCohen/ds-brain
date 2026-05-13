|Investigation<br>status|Set by user|Set by platform|
|---|---|---|
|New|When you want to move<br>MalOp back to pending<br>status.|When the MalOp<br>frst appears in<br>the**Malops**<br>**management**<br>screen.|
|Reopened|When you want to re-<br>evaluate a closed<br>MalOp.|When the system<br>detects new<br>activity related to<br>a MalOp that<br>was closed.|
|Under<br>investigation|When you want to specify<br>that the Malop is<br>currently under<br>investigation.|When a MalOp<br>with a<br>**Pending/New**<br>status is<br>escalated by the<br>user.|
|On hold|The MalOp has not been<br>resolved, but<br>investigation is not<br>currently active.|N/A|
|Closed|The MalOp review is<br>complete and it is closed<br>out. This can be because<br>the MalOp was deemed<br>as benign and marked as<br>Exclude or because<br>remediating action was<br>taken for a malicious<br>MalOp and it is no longer<br>considered an open<br>threat.|N/A|



[See Remediate MalOps (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)

[remediate-malops&language=en_US#remediate-malops) for](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)


information on setting the investigation status during the

remediation process.

## Investigation status without the non-Data

## Platform architecture


The following table describes the different MalOp statuses in

environments without the Data Platform architecture and how they


are set.


|Investigation<br>status|Description|
|---|---|
|Unread|Recently discovered MalOps that have not<br>yet been viewed. Cybereason automatically<br>assigns new MalOps the Unread status.<br>When you or another analyst views the<br>MalOp the status automatically moves to<br>Under Investigation.|
|To review|MalOps that you have read and specifcally<br>marked for review.|
|Not relevant|MalOps that are not relevant to your<br>organization. Marking MalOps as Not<br>relevant prevents identical MalOps from<br>appearing in the Cybereason interface.<br>Additionally, if the root cause of the MalOp is<br>a fle hash, IP address, or domain,<br>Cybereason adds the root cause to the<br>allowlist.<br>This action is the same as using the Malop is<br>benign - Exclude option in the**Malops**<br>**management** screen.|
|Remediated|MalOps that you or another analyst<br>remediated. After applying a remediation<br>solution, you must manually mark the item as<br>Remediated so the platform will continue<br>monitoring similar occurrences of the threat<br>and alert you if it reappears.<br>The Cybereason platform moves MalOps<br>marked as Not relevant to the Archived<br>section on the Malop inbox screen.|



[See Remediate MalOps (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)


[remediate-malops&language=en_US#remediate-malops) for](https://nest.cybereason.com/s/knowledge-base?article=24-1-remediate-malops&language=en_US#remediate-malops)

information on setting the investigation status during the


remediation process.


For Endpoint Protection MalOps, you can use the **Mark as**


**resolved** button to indicate a MalOp has been manually resolved.

## View the MalOp state


When you set the MalOp's investigation status, the platform also


automatically updates the MalOp's state to show where along the

path to resolution a MalOp is at the moment.


The MalOp state differs from the investigation status as it reflects


the progress toward resolution instead of the MalOp's position in

the investigation and triage process.


The MalOp states are updated accordingly depending on the

investigation statuses and activities of items associated with the


MalOp:








|Investigation<br>status|MalOp state|
|---|---|
|New|When the investigation status is**New**, the<br>MalOp state my be one of the following:<br>Active (in most cases)<br>Inactive - if the root cause process for<br>an Endpoint Protection MalOp is<br>suspended)<br>Resolved - if the root cause process for<br>an Endpoint Protection MalOp is<br>prevented)|
|Under<br>Investigation|When the investigation status is**Under**<br>**Investigation**, the MalOp state may be one<br>of the following:<br>Active (in most cases)<br>Inactive - if you use**Prevent fle**<br>**execution** response option|
|Reopened|When the investigation status is**Reopened**,<br>the MalOp state may be one of the<br>following:<br>Active (in most cases)<br>Inactive - if the root cause process for<br>an Endpoint Protection MalOp is<br>suspended<br>Resolved - if the root cause process for<br>an Endpoint Protection MalOp is<br>prevented|
|Closed|When the investigation status is**Closed**, the<br>MalOp state may be one of the following:<br>Resolved (in most cases)<br>Excluded - if you use the**Exclude**<br>option for a MalOp|
|On Hold|Active|


## Set the MalOp priority

You can add one of the following tags to MalOps to help prioritize


the response process:


**High**


**Medium**

**Low**


The priority feature can help security analysts determine which

MalOps are more urgent and which require further investigation.


For example, you might assign a **High** priority to a MalOp that

indicates a Remote Access Trojan (RAT) on a domain controller.


Likewise, you might assign a **Low** priority to a known adware

application on a lab or research and development (R&D) machine.


The priority feature is also helpful to organizations that do not have

an external ticketing or case management system and that also


rely entirely on the **Malops management** screen to manage
MalOp workflows.


You set a MalOp's priority from the **Priority** column on the **Malops**


**management** screen. If the column is not visible, click the

columns icon on the upper right of the MalOps list and check the


box next to **Priority** . The priority column has a drop-down menu

for each MalOp, from which you can select a priority to assign to


that MalOp.


You can filter MalOps by priority. To do this, select the priority in


the **Filters** options.

## Mark a MalOp status


For AI Hunting MalOps you can use the **Mark as** option in the


**Malop details** screen or the **Mark as resolved** button in the

**Malops management** screen to quickly exclude a MalOp or to


better organize MalOps.


**Mark as** options in the **Malop details** screen for AI Hunting


MalOps include the following:


|Malop<br>status|Description|
|---|---|
|**Unread**|Recently discovered MalOps that have not yet<br>been viewed. Cybereason automatically<br>assigns new MalOps the Unread status. When<br>you or another analyst views the MalOp the<br>status automatically moves to**Under**<br>**Investigation**.|
|**To review**|MalOps that you have read and specifcally<br>marked for review.|
|**Not**<br>**relevant**|MalOps that are not relevant to your<br>organization. Marking MalOps as**Not relevant**<br>prevents identical MalOps from appearing in<br>the Cybereason interface.<br>Additionally, if the root cause of the MalOp is a<br>fle hash, IP address, or domain, Cybereason<br>adds the root cause to the allowlist.<br>This action is the same as using the**Malop is**<br>**benign - Exclude** option in the**Malops**<br>**management** screen.|
|**Remediated**|MalOps that you or another analyst<br>remediated. After applying a remediation<br>solution, you must manually mark the item as<br>Remediated so the platform will continue<br>monitoring similar occurrences of the threat<br>and alert you if it reappears.<br>Cybereason moves MalOps marked as Not<br>relevant to the**Archived** section on the**Malop**<br>**inbox** screen.|



For Endpoint Protection MalOps, you can use the **Mark as**

**resolved** button in the **Malops management** screen to indicate


that a MalOp has been manually resolved.


In addition, if your Cybereason environment uses the Data


Platform infrastructure, above the MalOps list, click **Set status to**

and select the status.


## Escalate a MalOp

To quickly note that a MalOp requires addressing, click the

**Escalate** button in the MalOp's **Escalation** column. If the column


is not visible, click the columns icon on the upper right of the

MalOps list and check the box next to **Escalation** . To remove a


MalOp from esclation, click the **x** next to the MalOp's **Escalated**

label in the Escalation column.


You can quickly view escalated MalOps using the **Escalated**

**Malops only** checkbox on the upper right of the MalOps list (for


environments not using the new Data Platform infrastructure) or by

selecting **Escalated** in the **Investigation status** section in the


filters on the left side of the screen (for environments using the

new Data Platform infrastructure).


Escalating a MalOp only adds an internal label to the MalOp
which enables you to later filter by escalated MalOps. If you


escalate the MalOp, it does not affect email notificatons for

MalOps.

## Add MalOp labels


You can assign one or more labels to each MalOp so that you can

organize any MalOps that your Cybereason platform detects.


Note


Local analysts cannot use the MalOp label function.


For example, use MalOp labels to track:


|Categorization|Examples|
|---|---|
|Attack Types|RAT, Keyloger, Ransomware, Adware|


|Categorization|Examples|
|---|---|
|Attack Campaigns|5/17 Spear Phishing Campaign, 2/17<br>DDoS|
|VIP Users|CFO, Domain Admin, DB Admin|
|Threat Actors|Fuzzy Panda, APT26, Sandworm,<br>Shady Rat|
|IT Policy Violations|Games, P2P, Unapproved Browser|
|Responsible<br>Analyst|Analyst_A, Analyst_B|


**To create labels, follow these steps:**


1. Above the MalOps list on the left, click **Labels** .

2. In the **Manage labels** dialog box, start typing the name of


your new label in the search field. The **Add new label** button

appears.


3. Click **Add new label**, and click **Save** .


**To delete labels, follow these steps:**


1. Above the MalOps list on the left, click **Labels** .

2. Search for existing labels.


3. Click the 'x' on the label, and then click **Save** .


**To apply or remove labels, follow these steps:**


1. In the list, select the MalOp or MalOps that you want.

2. Above the MalOps list on the left, click **Labels** .


3. From the **Manage labels** dialog box, do one of the following:


To apply an existing label, select the label.


To remove the label, click the 'x'.

4. Click **Save** .


Note


When you click the 'x' on a label when one or more MalOps


are selected, the Cybereason platform removes the label from

the selected MalOps but does not delete the label. To delete a


label, click the 'x' on the label when no MalOps are selected.


You can filter MalOps by label. To do this, select the label that you


want in the **Filters** options.

## Resolve a MalOp


For all MalOps you can manually resolve any MalOp in the main


Malops management screen.



