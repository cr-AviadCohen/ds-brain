The following table describes the differences between the


automatic assignment groups and the manual assignment groups:
















|Group|Description|Sensor assignment|
|---|---|---|
|Automatic<br>Assignment<br>Groups|The Automatic<br>Assignment<br>Groups tab<br>contains groups<br>that use<br>assignment logic,<br>as specifed<br>when creating or<br>editing a group.|Sensors are assigned to<br>an Automatic Assignment<br>group when they satisfy a<br>group's assignment logic.|
|Manual<br>Assignment<br>Groups<br>k your Intern|The Manual<br>Assignment<br>Groups tab<br>contains groups<br>in which the<br>sensors are<br>manually<br>~~assigned to the~~<br>et connection and|Sensors must be manually<br>added to these groups.<br>Manually assigned<br>sensors are excluded from<br>group assignment logic.<br>For example, if you<br>manually assigned a<br>sensor to group A, and<br>the sensor's IP address<br>changes to an address<br>try again.|
||group.|specifed as criteria for<br>assignment to group B,<br>the sensor will remain in<br>group A.|



The tabs in the **Groups** screen lists their associated groups along


with the following properties:








|Column|Description|
|---|---|
|Priority|For Automatic Assignment Groups, the priority<br>represents the order in which a group's<br>assignment logic is compared to new sensors.<br>The platform frst looks at the assignment logic<br>in the group with priority 1. If the sensor does<br>not meet the grouping criteria, the platform<br>checks the group with priority '2', and then '3',<br>and so on.|
|Group<br>name|Name of the group|
|Description|Optional description of the group|


|Column|Description|
|---|---|
|No. Sensors|Number of sensors assigned to the group|
|Assignment<br>logic|For Automatic Assignment Groups, a brief<br>description of the assignment logic defned for<br>the group|
|Policy|Security policy applied to sensors in the group|
|Creation<br>time|Timestamp of when the group was created|
|Last edited<br>time|Timestamp of when the group was last edited|






|Property|Operators|
|---|---|
|Organizational unit (as defned in the Active<br>Directory for Windows machines)|contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern|
|Machine name|contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern|


|Chec|Property|Operators|Col4|
|---|---|---|---|
|Chec|Organization (as defned in the server<br>installation process.You can fnd this value in<br>the installer package name provided for your<br>organization.)|contains<br>is<br>doesn't<br>contain<br>is not|contains<br>is<br>doesn't<br>contain<br>is not|
|Chec|Internal IP address|contains<br>is<br>doesn't<br>contain<br>is not<br>is in range<br>is not in<br>range|contains<br>is<br>doesn't<br>contain<br>is not<br>is in range<br>is not in<br>range|
|Chec|External IP address<br>k your Internet connection and try again.|contains<br>is<br>doesn't<br>contain<br>is not<br>is in range<br>is not in|contains<br>is<br>doesn't<br>contain<br>is not<br>is in range<br>is not in|
|range<br>OS<br>contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern<br>FQDN<br>contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern<br>If you want to add multiple values for a part of an assignment rule,<br>ensure you select the**OR** operator between the multiple values:||range|range|
|range<br>OS<br>contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern<br>FQDN<br>contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern<br>If you want to add multiple values for a part of an assignment rule,<br>ensure you select the**OR** operator between the multiple values:|OS|contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern|contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern|
|range<br>OS<br>contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern<br>FQDN<br>contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern<br>If you want to add multiple values for a part of an assignment rule,<br>ensure you select the**OR** operator between the multiple values:|FQDN|contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern|contains<br>is<br>doesn't<br>contain<br>is not<br>matches<br>pattern|


|Role|Manage<br>groups|Add/remove<br>sensors|View sensors<br>in groups|
|---|---|---|---|
|System<br>admin|All groups|All groups|All groups|
|Sensor<br>admin L1|None|Groups specifed<br>in user settings|Groups<br>specifed in<br>user settings|
|Policy<br>admin|None|None|All groups|


**Analysts** :






























|Role|View<br>MalOps|Investigate<br>Elements|Reputations|Remediate<br>MalOps|
|---|---|---|---|---|
|Analyst<br>L1/L2/L3<br>k your Inte|All<br>MalOps<br>rnet conn|All<br>Elements<br>ection and tr|L1 and L2:<br>View and<br>search L3:<br>Manage<br>y again.|L3 only|
|Local<br>Analyst<br>L1/L2|MalOps<br>involving<br>sensors<br>in their<br>assigned<br>groups|Elements<br>occurring<br>on sensors<br>in their<br>assigned<br>groups|View and<br>search|L2 only, for<br>MalOps<br>involving<br>sensors in<br>their<br>assigned<br>groups|


## - Known limitations sensor grouping

You can add a maximum of 500 groups to your environment.
Email notifications regarding stale or archived sensors apply


to all sensors in the environment, regardless of the recipient's

sensor group permissions.


When a machine moves between groups, local analysts with

permissions for the source group continue to see updates for


the users associated with the machine.

Local analysts cannot apply labels to MalOps.

## Related resources


[Benefits of sensor grouping (/s/article/2667007)](https://nest.cybereason.com/s/article/2667007)

[Sensor Grouping FAQ (/s/article/3106891)](https://nest.cybereason.com/s/article/3106891)



