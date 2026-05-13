address, a process, a module, or a domain. In contrast,


behavioral allowlisting rules prevent MalOps that would have been

created based on **behaviors** . A behavior is any suspicious activity


on your system that could be part of a MalOp. You can define a
behavioral allowlisting rule to ensure a specific subset of


behaviors does not trigger a MalOp.


Before the platform generates a MalOp for a specific instance of


suspicious behavior, the Cybereason platform checks if this

behavior matches any currently enabled behavioral allowlisting


rule. If so, the platform does not generate a MalOp.

## Create a behavioral allowlisting rule


To create a new rule, click **Create new rule** from the **Behavioral**


**allowlisting** screen. The **Create new rule** screen appears:

## 1. Give the name a rule and specify the

## root cause


First, give your rule a name and description, and select a root

cause:


**Rule Name:** The name displayed in the list of rules in the

**Enabled**, **Disabled**, or **Archived** tab.


**Description:** The text displayed in the **Suspect Information**
field in the **Element Details** screen for Elements associated


with this rule.

**Root Cause Type:** The underlying reason why the behavior


you want to allow would be considered malicious. Cybereason

uses these same root causes to identify and categorize


MalOps throughout the UI.


When you select a root cause, the **Define rule properties** area


displays.


## 2. Define the rule properties

1. Under **Define rule properties**, click **Select an element** .


2. Select an Element from the drop-down list. You can select a


Process, IP address, or Domain Name Element, depending on


the Root Cause Type you select.
3. Click the filter icon to add one or more filters to specify


features of the Element you want to allow. For example, you

could add **Process name is AeXNSAgent.exe** .


In versions 23.2.87 and earlier, the following characters are

not supported during the creation of a behavioral allowlisting


rule:


"


&

[


]

{


}

,


Beginning in versions 23.2.12X and later, you can use these

characters when creating the rule.


For more information on Elements and filters available, see

[Build a Query (/s/knowledge-base?article=24-1-build-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#build-a-query)


[query&language=en_US#build-a-query).](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#build-a-query)

4. To add another Element to the expression, click the plus sign


icon and then **Add element** .

5. Click outside the filter box to activate the **Add** button, and


click **Add** to add the expression to the rule.

6. To add another expression to the rule, select another Element


and repeat this procedure. You can delete any expression by

clicking the trash can icon to the right.


As you build the rule, you can use the **AND** operator between

parts of the rule. This ensures that the MalOp is excluded only if all


of the conditions in the rule are met.


## Preview and save the Rule

1. Click **Preview the impact this rule would have had on**


**existing Malops** to see the existing MalOps in your system

that the rule would have prevented the Cybereason platform


from creating.

2. Click **Save** to save and enable the behavioral allowlisting rule.


When you add a behavioral allowlisting rule, by default the

Cybereason platform enables the rule and the rule takes effect


immediately. However, the rule does not apply to previous

MalOps.


The Cybereason platform keeps a history of all MalOps prevented

by the rule, from the time it was created or enabled. If you re

enable a rule, the platform resumes creating history entries for that

rule.


For a detailed look at how to create several different behavioral

[allowlisting rules, see Add a Behavioral Allowlisting Rule - Tutorial](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-behavioral-allowlisting-rule-tutorial&language=en_US#add-a-behavioral-allowlisting-rule-tutorial)


[(/s/knowledge-base?article=24-1-add-a-behavioral-allowlisting-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-behavioral-allowlisting-rule-tutorial&language=en_US#add-a-behavioral-allowlisting-rule-tutorial)

[rule-tutorial&language=en_US#add-a-behavioral-allowlisting-rule-](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-behavioral-allowlisting-rule-tutorial&language=en_US#add-a-behavioral-allowlisting-rule-tutorial)


[tutorial).](https://nest.cybereason.com/s/knowledge-base?article=24-1-add-a-behavioral-allowlisting-rule-tutorial&language=en_US#add-a-behavioral-allowlisting-rule-tutorial)

## Edit the rule after initial creation


If you want to edit the rule after you create it, click the three dots to


the right of the rule name and select **Edit** . Update the fields

accordingly and save the changes.


Edits take effect immediately, but are not retroactive. The list of

allowlisted events associated with a rule includes all MalOps


triggered by any iteration of the rule.


Note


If the rule you are editing contains illegal characters, no data
appears under the **Define rule properties** when editing the


rule.


In some cases, you may want to use an existing rule as the basis


of a new rule. In this case, you can duplicate existing rules.


**To duplicate a rule, follow these steps:**


1. In the **Behavioral allowlisting** screen, click the three dots to


the right of the rule creation date-time, and select **Duplicate** .


2. The **Create new rule** pane appears populated with


information from the duplicated rule, along with "Copy" added


to the rule name.

3. Make any desired changes, and click **Save** .


## Disable, archive, or re-enable a rule

To disable, archive, or re-enable a rule:


1. In the **Behavioral allowlisting** screen, click the three dots to


the right of the rule creation date-time.


2. Select **Enable**, **Disable**, or **Archive** to change the status of


the rule.


When you disable or archive a rule, the platform does not

retroactively generate MalOps for the behavior that the rule


specifies.

## View behavioral allowlisting rules


You can view behavioral allowlisting rules in multiple places in the


Cybereason platform:


|Location|Details|
|---|---|
|From the<br>Security<br>Profle<br>page|The Behavioral allowlisting screen provides<br>three tabbed lists -**Enabled**, **Disabled**, and<br>**Archived** - that display all the rules you have<br>defned. Click a tab to see the rules in that<br>status category. Click the appropriate tab to see<br>the rules in that status category.<br>Click the rule to view more details or edit the<br>rule. For example:<br>Click the**Allowlisted events** button to view a<br>list of events that did not trigger a MalOp due to<br>this behavioral allowlisting rule. This list includes<br>all Malops triggered by any iteration of the rule,<br>but does not include events prior to the creation<br>of the rule because behavioral allowlisting rules<br>are not retroactive.|


|Location|Details|
|---|---|
|In the<br>Element<br>Details<br>screen|You can view and investigate evidence and<br>suspicions related to behaviors that are allowed<br>from the**Investigation** screen's**Element**<br>**Details** pane.<br>Under the**Allowlisted** section, Cybereason<br>shows you the allowlisting rules that prevented<br>the evidence and/or suspicions from becoming<br>a MalOp. Information includes:<br>Rule name<br>Rule description<br>Rule ID<br>Rule criteria|

## - Known limitations Behavioral

The following are known limitations for the Cybereason behavioral


allowlisting feature.


When editing an existing rule, it is not possible to change the


rules expresssions with the logic for the exclusion. If you need

to update the rule expression logic, delete the rule and create


a new rule.

When editing an existing rule, you cannot modify the **Rule**


**name** .

In the **Behavioral allowlisting** screen, the **Request to**


**preview** option does not return a list of MalOps that would be

generated for rules that are based on IP/Domain arguments


for IP/Domain decision features.

When creating a behavioral allowlisting rule, if you click to


preview the impact the rule would have on existing MalOps,

then click **Go to Malop** on a resulting MalOp, this navigates


away from the rule, and the rule is not saved. Instead, to view

the resulting MalOp, right-click and open the resulting MalOp


in a new tab.

Behavioral allowlisting rules support the use of Japanese


characters. However, you cannot use apostrophes when

creating a behavioral allowlisting rule.



