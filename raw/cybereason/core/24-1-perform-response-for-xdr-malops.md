**Workspace** integrations: Phishing techniques


**Identity** integrations: Brute force attacks, misuse of valid

accounts, and the use of Multi-Factor Authentication Request


Generation

**Network** integrations: Phishing, Drive-by compromise, and


exploits of public-facing applications.


In this topic:


Before you begin

Enable response actions per integration


Add the relevant integration permissions

View recommended response actions


Perform response actions

Perform response actions for network platforms


View the status of response actions

Known limitations - XDR response actions


Related resources


Use XDR response actions


Integration configuration


Before you begin using response actions for XDR MalOps, you


should understand the following items:


Compile your list of existing platforms that integrate with


Cybereason XDR and that are supported for response actions

Decide for which integrations you want to enable response


actions through Cybereason XDR.

Decide which response actions you want to enable. To see the


full list of actions supported for an integration, see the

**Supported Actions** tab in the relevant integrations tab.


In addition, if you would like Cybereason to generate a test MalOp

in your Cybereason environment to test the response actions, you


should provide the following information to your Customer

Success Manager or Technical Account Manager:


Your Cybereason user name

Your Cybereason account name


The domain name for your Cybereason environment


After you share this information with Cybereason Technical


Support, the test MalOp will be generated in your Cybereason

environment within three business days.

## Enable response actions per integration


For each integration on which you want to perform response

actions in the external platform directly from Cybereason XDR, you


need to enable the response actions in the integration
configuration in the **Cybereason Connect** screen.


Note


If you have previously configured an integration, you will need


to enable each of the actions in the integration configuration. If
you are setting up an integration for the first time, the actions


are already selected by default.


**To enable response actions, follow these steps:**


1. In the **Cybereason Connect** screen, add an integration or

select the integration to display the integration configuration in


the **Access Details** pane.

2. In the **Access Details** pane, in the **Connected response**


**actions** area, click the down arrow to display available

response actions:


3. Select one or more of the actions to enable the action.


Note


For those integrations that share the same source data (such


as Okta Audit and Okta Context, or Azure AD Audit, Azure AD

Context, and Azure AD Sign-Ins), when you set up response


actions for one of the integrations, the response actions apply

to all of the related integrations.

## Add the relevant integration permissions


For each integration for which you want to perform response

actions, you need to grant permissions for Cybereason XDR to


perform actions in your external platform. These permissions differ

for each integration.


To view the details on the configuration required for each


integration, see the relevant tab in the individual integration page

[in the Cybereason Integrations (/s/integrations) documentation.](https://nest.cybereason.com/s/integrations)

## View recommended response actions


When Cybereason XDR creates an XDR MalOp, part of the MalOp

generation process involves the creation of the recommendation


response for suspicious events that were not remediated or

mitigated by your integrated platforms and therefore are still active


threats/events. These recommendations are included in the

overview details for the MalOp.


**To view recommended response actions, follow these steps:**


1. In the **XDR Malops** screen, open an XDR MalOp.


2. In the XDR MalOp details, at the left side of the **Overview** tab,


next to the **Summary** tab, click **Response** :


3. Expand each recommendation to see the details.


The recommendation includes the following details:


**Action name:** The recommended action, such as **Delete**

**file** or **Reset password** .


**Element:** The icon of the Element on which the action

should be executed (e.g. User, Machine, File, Process,


Message)

**Indicators:** A list of required properties you need to


perform the response action, such as Message ID or

email address.


The available recommendations and indicators differ depending


on the items associated with the XDR MalOp:


Note


In the recommendation details, the each recommended

response action is for a single integration source. In some


cases, such as when the recommendation is to block a

specific URL or IP address, you may need to perform this


action in multiple different platforms.












|Action|Target<br>Item(s)|Action<br>description|Required<br>indicators<br>for action|
|---|---|---|---|
|Add hash to<br>blocklist|Attachment<br>(for email<br>message)|Add the fle<br>hash value for<br>a message<br>attachment to<br>the blocklist to<br>avoid future<br>execution of<br>the fle.|Attachments<br>for an email<br>message|


|Action|Target<br>Item(s)|Action<br>description|Required<br>indicators<br>for action|
|---|---|---|---|
|Block<br>authentication<br>from IP|Connection|Block any<br>authentication<br>attempts from<br>a specifc IP<br>address.|Source IP<br>address to<br>block|
|Block email<br>sender|Message|Add the email<br>sender<br>address to the<br>blocklist to<br>prevent future<br>malicious<br>emails from<br>this address.|Message<br>sender email<br>address|
|Block traffc<br>to IP|Connection|Block all traffc<br>to a specifc<br>address.|IP address<br>for the<br>performer of<br>the activity|
|Block traffc<br>to URL|Connection|Block all traffc<br>to a specifc<br>URL.|URL for the<br>performer of<br>the activity|
|Close active<br>sessions|User|Close active<br>sessions for<br>the specifed<br>user.|Source user<br>name or<br>target user<br>name|
|Delete all<br>emails from<br>sender|Message|Delete all email<br>messages<br>from the<br>specifc<br>sender.|Sender<br>email<br>address|
|Delete email<br>by message<br>ID|Message|Delete all<br>instances of a<br>phishing email<br>with the same<br>message ID.|Message ID<br>and email<br>address|
|Reset user<br>password|User|Reset the<br>password for<br>the specifed<br>user.|Source user<br>name or<br>target user<br>name|


|Action|Target<br>Item(s)|Action<br>description|Required<br>indicators<br>for action|
|---|---|---|---|
|Suspend user<br>account|User|Suspend a<br>user's account<br>to prevent<br>them from<br>performing<br>different<br>actions inside<br>the network.|Source user<br>name or<br>target user<br>name|



In the list of XDR MalOps in the main **XDR MalOps** screen, you


can also see the recommended response actions in the

**Recommended response** column:


Click on the action name to display the details.

## Perform response actions


For some integrations, you can perform response actions directly


from Cybereason XDR instead of needing to go into your other

platform to take action.


If you are able to perform a remediation action, the **Response** tab

displays a checkbox next to the action name:


**To perform response actions, follow these steps:**


1. In the **Response** tab of an XDR MalOp, select the action to


perform or the indicator on which to perform the action.


If you select the action, all indicators (targets) for that action


are automatically selected.


2. Click **Commit** .


After you click **Commit**, Cybereason XDR sends the command to


perform the action.


If the action succeeds, you can view a message with details on


when an which user performed the action:


If the action fails, you can view an error message about the failure:

## Perform response actions for network


Note


To perform response actions for network platforms, you must


have the Threat Intel and Reputation microservice enabled in

your environment. For details on how to enable this contact


your Customer Success Manager.


For network-based integrations included with the Cybereason


XDR **Network** module, you can perform actions to respond to
network-based attacks, such as blocking network traffic to an IP


address


However, unlike Workspace or Identity-based integrations, you


work both in the XDR MalOp details screen and the **Reputations**

screen.


**To perform response actions for network integrations, follow**

**these steps:**


1. In the **Response** tab of an XDR MalOp, select the action to


perform or the indicator on which to perform the action.


If you select the action, all indicators (targets) for that action


are automatically selected.


2. Click **Commit** .


After you click **Commit**, Cybereason XDR sends the


command to perform the action.


If the action succeeds, you can view a message with details


on when and which user performed the action:


If the action fails, you can view an error message about the


failure:


For this action, the Cybereason platform adds the IP address

to the platform blocklist, with an XDR action of **Prevent** :


The Cybereason platform does not detect access to or prevent

the IP addresses. However, the IP addresses added to the list are


retrieved by your firewall. You can then decide whether to add the
IP address to the firewall blocklist or detection list.


If you want Cybereason XDR to later not include the IP address in
the list retrieved by your firewall, in the **Reputations** screen, select


the IP address, and in the **XDR Action**, select **None** or delete the

IP address.


## View the status of response actions

As you analyze and perform response actions, you have the ability


to view the action status to understand if an action is successful or

not.


In the MalOp list in the **XDR MalOps**, in the **Response status**

column, you can view the status for all response actions:

## Known limitations - XDR response


In the **Response** tab in the XDR MalOp details, the


**Recommended response** field displays the number of

unique actions to take, not the total number of actions/targets


on which you need to take actions. For example, the

**Recommended response** may say **7 actions**, which means


there are seven unique actions to take, but for each of these

actions you may need to perform the response on multiple


targets/indicators.

For those integrations that share the same source data (such


as Okta Audit and Okta Context, or Azure AD Audit, Azure AD

Context, and Azure AD Sign-Ins), when you set up response


actions for one of the integrations, the response actions apply

to all of the related integrations.


When you enable response actions for Azure AD Audit, the

same actions are automatically enabled for the Azure AD


Context and Azure AD Sign-Ins integrations.

When you enable response actions for Okta Audit, the same


actions are automatically enabled for the Okta Context

integration.

## Related resources

## Use XDR response actions


[View the Global Response History (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-the-global-response-history&language=en_US#view-the-global-response-history)

[article=24-1-view-the-global-response-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-the-global-response-history&language=en_US#view-the-global-response-history)


[history&language=en_US#view-the-global-response-history)](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-the-global-response-history&language=en_US#view-the-global-response-history)

## Integration configuration


**Azure AD**


[Configure your Azure AD Platform to Retrieve Activity Logs](https://nest.cybereason.com/s/knowledge-base?article=configureAzure)

[and Enable Remediation Actions (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=configureAzure)


[article=configureAzure)](https://nest.cybereason.com/s/knowledge-base?article=configureAzure)



