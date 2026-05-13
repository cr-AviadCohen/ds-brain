## Step 1: Define rule properties

1. On the left side of the **Create custom detection rule** screen,


fill out the **Configure rule type** section.


The following table describes the rule creation fields.






|Field|Description|
|---|---|
|Rule name|A unique name for this rule.|
|Detection<br>type|Detection types represent categories of<br>methods Cybereason uses to detect<br>malicious behavior. Cybereason<br>recommends choosing the Custom rule<br>option when creating a rule to differentiate<br>MalOps triggered by your rule.<br>If you want MalOps triggered by your rule<br>to be classifed and presented according<br>to another detection type, select that type<br>here.<br>**Valid options**:<br>Known malware<br>Malicious process<br>PUP<br>Command and Control<br>Reconnaissance<br>Extension manipulation<br>Process injection<br>Persistence<br>Elevated access<br>Phishing<br>Data transmission volume<br>Credential theft<br>Lateral movement<br>Ransomware<br>Blocklist<br>Custom rule (recommended)<br>Compromised user|


|Field|Description|
|---|---|
|Description|A description for this rule.<br>Note<br>The Save button will not activate if this<br>feld contains blank lines.|
|Detected<br>activity|The type of activity this rule is detecting.<br>Select the value that most closely<br>describes the activity your rule is detecting.<br>**Valid options**:<br>Infection<br>Privilege escalation<br>Scanning<br>Lateral movement<br>C&C<br>Data theft<br>Stolen credentials|
|Root cause<br>element|The underlying reason why the activity this<br>rule is detecting is considered malicious.<br>**Valid options**:<br>Self (Default) - The activity itself is<br>malicious<br>Image fle - The activity's image fle is<br>malicious<br>Parent process - The activity's parent<br>process is malicious|


## Step 2: Select a starting Element

On the **Build a rule canvas**, select a **Logon session** or **Process**


Element.


The **Process** Element instructs the Cybereason platform to


trigger a MalOp based on a process that the platform

encounters.


The **Logon session** option instructs the Cybereason platform
to trigger a MalOp on a session instead of on a specific


process. You may want to start with the **Logon session**

Element if you want to be alerted when a certain user


performs an action.


## Step 3: Add Elements and Features

Add Elements to your rule by clicking the plus sign (+) on the right


of an Element.


Note


Some Elements can only be connected to specific Elements.


Add filters by hovering over an Element to reveal the **Add filter**


button. Use the filters field to specify Features, operators, and

values that you want to use for your rule. For details on the


Features available for each type of Element you can use to build a

[rule, see Supported Features for Custom Detection Rules](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-for-custom-detection-rules&language=en_US#supported-features-for-custom-detection-rules)


[(/s/knowledge-base?article=24-1-supported-features-for-custom-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-for-custom-detection-rules&language=en_US#supported-features-for-custom-detection-rules)

[detection-rules&language=en_US#supported-features-for-custom-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-for-custom-detection-rules&language=en_US#supported-features-for-custom-detection-rules)


[detection-rules). For details on how to build the parts of the rule,](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-for-custom-detection-rules&language=en_US#supported-features-for-custom-detection-rules)

[see Build a Query (/s/knowledge-base?article=24-1-build-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#build-a-query)


[query&language=en_US#build-a-query) for more information on](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#build-a-query)
using filters.


Remove an Element from the rule by hovering over the Element

and clicking the red 'X' to the left of the Element name.


Important


Removing an Element removes all child Elements connected


to it.


Toggle between full screen view and minimized screen view by


clicking the arrow on the top right of the screen.

## Step 4: Select a grouping feature


If needed, select a grouping feature. By default, MalOps that are


triggered by custom rules are grouped according to rule. This

means that the Cybereason platform groups multiple instances of


a certain rule-defined behavior into one MalOp. The **Grouping**

**features** section of the **Create custom detection rule** screen


provides alternative grouping options. You can group multiple
instances of a defined behavior into separate MalOps according


to the following features:


Process name


Parent process name


Owner machine

User name


SHA1 hash

Product name


For example, if a single rule detects five instances of the same

behavior and **Process name** is selected as the grouping feature,


the Cybereason platform triggers a MalOp for each unique

process name.


Note


If you select more than one grouping feature, the Cybereason


platform groups together only items that match ALL the

selected features.

## Step 5: Set the automatic remediation
## action (optional)


You can specify how the Cybereason platform responds to

MalOps generated by your custom detection rule logic. Setting


automatic remediation options increases your security posture by

automatically and immediately containing threats and preventing


them from spreading across your network. This feature reduces

the time that security analysts need to manage these incidents.


To add an auto-remediation action to a custom detection rule,

select a response option from the **Set remediation action** section.


Automatic remediation options include:


**Kill process** : When the Cybereason platform detects the
behavior specified in the rule, it will kill the associated


process.
**Quarantine file** : When the Cybereason platform detects the


behavior specified in the rule, it will quarantine the associated
file.


**Isolate machine** : When the Cybereason platform detects the
behavior specified in the rule, it will isolate the affected


machines.


Note


Automatic remediation options occur on all machines

associated with the respective custom rule.


## Save, enable, or disable a rule

After building a rule, click **Save Rule** from the **Create custom**


**detection rule** screen.


Important


Custom detection rules are automatically enabled when you

click **Save rule** .


Once the rule has been saved, it is visible and can be modified
from the table on the **Security Profile > Custom detection rules**


screen.


To disable the rule, slide the **Status** slider to **Off** on the **Custom**


**detection rules** screen. To hide disabled rules, select the **Hide**

**disabled** check box.


Note


Rules are not retroactive.

## Edit or delete a rule


To edit an existing rule, select the rule on the **Custom detection**

**rules** screen and click **Edit Rule** .


To delete an existing custom detection rule, click the three vertical

dots to the right of the rule on the **Custom detection rules**


screen, and then click **Delete** .


Deleting a rule does not remove it from the system. Instead, the


rule is deactivated and moved to the **Deleted** tab on the **Custom**

**detection rules** screen. MalOps triggered by deleted rules remain


unchanged.


Important


You cannot restore deleted rules.

## View modification log


To view changes that were made to a specific rule, click the rule


on the **Custom detection rules** screen to preview the rule, and
then click **Open modification log** .



