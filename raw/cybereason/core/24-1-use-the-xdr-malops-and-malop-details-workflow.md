What data sources are reporting the events?


What are the attack vectors?

What are the affected assets and how many assets are


targeted?

When did the activity happen?


Understand why this MalOp was triggered


What is the reasoning behind the MalOp steps?


What is the correlation between steps?

What are the details from the vendor platform/product?


Analyze what is happening to determine if this is legitimately

malicious


What does threat intel say about the IOA/IOCs from this

Malop?


What are the actions taken for indicators in the MalOp?

How frequent is this indicator in your environment?


What does the security community say about these

indicators?


Resolve the incident (if needed)

## Evaluate scope and severity


After the MalOp is generated, you should first understand the


scope and severity of the MalOp to help you make an initial

determination of the seriousness of the events in the MalOp.


You should consider the following items.

## What threats were detected?


In the **Overview** tab of the XDR MalOp details, look at the steps


contained in the MalOp.


You should understand what malicious activities are represented


by these steps. Since the step names are different MITRE ATT&CK

tactics, techniques, and sub-techniques, you can quickly identify


the steps and attack techniques that are occurring and which

activities concern you the most.


You can view high-level details of the step in the **Overview** tab.


If you want to see additional details about an individual step, click


the step to display the step details card:


You should view and understand the details contained in each

step to best understand what happened to cause the MalOp.


In addition, you should view the sequence of steps. Evaluate

whether these steps are in a logical sequence, likely representing


an escalating attack, or a collection of activities on single assets.

## What data sources are reporting the


Depending on the MalOp, the activities may be occurring in many


different parts of your organization or you network.


In the **Summary** pane of the XDR MalOp details, you can quickly


see the data sources associated with the steps and events in the

MalOp.


Identifying the different integrations that report the events will give

you a good indication of the nature of the attack. For example, if a


MalOp reports events from Fortinet Fortigate or your Palo Alto

NGFW, you can determine the attack affects your network.


Likewise, if the MalOp contains events from Azure or Okta, there

are users are user accounts that are affected.


## What are the attack vectors?

In addition to understanding the individual steps in the MalOp and


the activities represented in each of these steps, you gain a basic

view how the steps/events occurred.


In the **Overview** tab, in each step, you can view the primary target

for each step. This could be a user account, an email address, an


IP address, and so forth.


Evaluating these vectors will better help you gain an overall


understanding and sense of the MalOp and threat it represents.

## What are the affected assets and how

## many assets are targeted?


In any attack, you want to determine the breadth of the attack as


well as the seriousness of the attack, based on what assets are

targeted.


In the **Summary** tab of the MalOp details overview, you can view

the **Scope** of the MalOp.


You should determine if this MalOp represents a large or small

number of assets, or whether the assets targeted are high value


assets.


## When did the activity happen?

For this MalOp, it is also important to understand when the MalOp


activity occurred.


In the **Summary** tab for the overview details, you can see the


basic time information for the MalOp:


In addition, you can see this information for each step in the step


details card:

## Understand why this MalOp was


To help you fully understand the MalOp, you should understand


the reasons behind the MalOp creation.


Use these steps to better analyze the reasons behind the MalOp


generation.

## What is the reasoning behind the MalOp


For each MalOp, the step displays the name based on the MITRE


ATT&CK tactic, technique, or sub-technique for the activity

represented by the events in a given step. This helps you identify t


first glance what activity the events in each step represent. This

name and basic description should make it clear why a step is


part of the MalOp.


Once you get the basic idea why a step was created (whether it


was base on a single suspicious event or multiple suspicious

events), look at the details for each step, including the step


overview details and included suspicious events to see the

reasons behind why the step was created.


For example, see if there are multiple similar types of activities

(such as a denial of access to a network, failed logins, and so


forth), or similar machines, users, or other assets.

## What is the correlation between steps?


In addition to analyzing the reasons a given step was added in the


MalOp, you should also understand the connection between the

steps.


While the steps in the MalOp **Overview** tab are ordered based on

time, the activities were detected/reported, there could be a


connection between steps. For example, if you see a step related

to a suspicious login, and then see another step for misuse of


credentials, you can see the pattern of activity and understand

why the steps are included in the same MalOp.


In addition, in the **Overview** tab, you can also view a list of top


correlation points between the steps:


Use those points to understand how the parts of the MalOp and


attack sequence are connected.

## What are the details from the vendor


In the end, because the events in the MalOp are combined


together from your various connected integrations, you should
also view the vendor or product-specific information for each step


and for each event inside the steps.


Cybereason XDR parses the logs from your various connected


integrations and is able to use the data for further enrichment and

analysis. However, the MalOp details also contain a section for the


vendor specific fields, so you can analyze further based on the

original reported data.


Inside a given step or suspicious event, you can navigate to the
**Additional Details** section to see the vendor or product specific


information for a step or event.

## Analyze what is happening to determine

## if this is legitimately malicious


Once you understand the scope and severity of the MalOp and


the events contained in the MalOp, and also understand why this

MalOp was created, you should analyze all the indicators


associated with the MalOp to determined whether the activity

represented by this MalOp is genuinely malicious or a false


positive for your organization.


## What does threat intel say about the

## IOA/IOCs from this Malop?

For each MalOp, you are also able to view related indicators that


are not specific assets (such as machines or user identities) for

the steps and events in the MalOp.


In the **Detected elements** tab of the MalOp, you can see a

collection of all the related indicators for the events associated


with this MalOp. This can be attachment files, connections,

messages, and so forth.


You should view the details about these indicators and


understand if these values are expected. Compare the details
about related indicators, such as the file hash value or IP address,


against known threat intel sources and assess whether the

indicators are legitimately malicious for you or not.

## What are the actions taken for indicators

## in the MalOp?


For each of the indicators, there may have been actions taken on

that indicator. For example, for a connection, the connection may


have been allowed or blocked. Likewise, for a user account, the

account may have been suspended or blocked.


The action could have been manually performed by someone in


your organization or automatically as part of the configuration or

policy on the integrated platform.


Look at this action and understand why these actions were taken,

and whether this was expected and necessary for your


organization.


## How frequent is this indicator in your

For each indicator, you also want to analyze how often an indicator


occurs in the activity associated with a MalOp. If a specific

message attachment is reported in the **Detected elements** tab


frequently, this may be an indicator of a phishing attack.


Likewise, if you see an indicator in the **Detected elements** tab,


see if this is a common item in your organization. If you see a file in
the list of elements, this may be a legitimate file for your


organization, such as proxy configuration script for machine

connection. If you see the same IP address often, this could be


because it is an internal IP address for company resources.


Items that do not appear often or are not expected to be listed in


the related indicators would cause concern and would help you

determine that the activity in this MalOp is likely malicious.

## about these indicators?


Lastly, you should perform your own independent research for the

related indicators found in this MalOp. Through various security


blogs and searches, you may see that the community at large

considers n item to be genuinely malicious or not malicious.

## Resolve the incident (if needed)


After you determine that a MalOp is indeed malicious or a false

positive, you should take steps to resolve the MalOp.


If the MalOp is legitimately malicious, in the **Response** tab of the

MalOp details, you can see the recommended response actions:


You can perform some of these actions in your integrated


platforms. Other actions can be performed directly from

Cybereason XDR.


If a MalOp is a false positive, you can update your third-party


integration platforms to ensure these items are allowed. For

example, in your integrated platforms, you may need to add an IP


address, file hash, or connection to an allowlist. Likewise you can

update security policies in these platforms to not detect or report


the activity related to this MalOp.





