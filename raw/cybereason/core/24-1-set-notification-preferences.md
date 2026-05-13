1. In the **Settings** screen, Navigate to the **SMTP server** section.


2. In the **SMTP server** section, click **Default** .

3. Request the IP of the SMTP server from Cybereason Technical


Support.

4. In your organization's network settings, enable users to


receive emails from the SMTP server IP.


**To configure a custom SMTP server:**


1. In the **Settings** screen, navigate to the **SMTP server** section.

2. In the **SMTP** section, click **Custom** .


3. Configure settings as desired. Configuration options are


described in the following table.












|Field|Description|
|---|---|
|Host name|The IP address or host name of<br>the SMTP server.|
|Port|The port on which you are<br>communicating with the server.|
|Secure<br>communication<br>protocol|The secure protocol over which<br>the mail is sent.|
|Email|Email address to which to send a<br>test email notifcation.|
|Password|Cybereason password<br>associated with the email<br>address.|



4. Optionally, send a test email to the email you provide.


5. Click **Add server** to save your changes.

## Enable and configure global notifications


System administrators can enable and configure notification


settings from the **Settings** screen **Notification** section. These
notification settings apply to all users with notifications enabled.


Users with the Local analyst L1 or L2 role will only receive emails

about MalOps that involve sensors in the sensor groups the user


has access to.


Notifications are sent in the following scenarios:






|Scenario|Details|
|---|---|
|MalOp is created|Email notifcations are sent for any<br>new MalOp.<br>For example, if the AI Hunting Engine<br>created a new AI Hunting MalOp with<br>the**Active** state, an email notifcation<br>is sent to all relevant users. Likewise, if<br>the platform creates a Endpoint<br>Protection MalOp with the state of<br>**Resolved** since the malware<br>associated with the MalOp was<br>quarantined, an email notifcation is<br>sent to the relevant users.|


|Scenario|Details|
|---|---|
|MalOp is updated|Email notifcations are sent when a<br>new suspicion is added to an existing<br>MalOp, regardless of the existing<br>MalOp state or MalOp investigation<br>status.<br>For example, a suspicion was<br>detected by the Cybereason platform,<br>and was associated by the platform<br>with an existing AI Hunting MalOp in<br>the**Active** state. As a result, the**Last**<br>**update time** for the MalOp is<br>updated. A notifcation will be sent in<br>this scenario to all relevant users.<br>Likewise, if a malware fle was<br>quarantined on an endpoint machine,<br>the platform associated this malware<br>event in an existing Endpoint<br>Protection MalOp with the**Resolved**<br>state and**Closed** investigation status.<br>As a result, the**Last update time* for**<br>**the MalOp is updated, but the**<br>**MalOp remains in the Resolved**<br>state with the investigation status still<br>**Closed**. A notifcation will be sent in<br>this scenario to all relevant users.|
|MalOp is<br>updated/reevaluated|In versions 24.1.41 and later, for<br>Endpoint Protection MalOps,<br>notifcations are sent when a detected<br>event is the same event as an event<br>that was already associated with the<br>MalOp.<br>For example, a process was detected<br>and/or prevented by the Cybereason<br>platform and was reported as an<br>event in an Endpoint Protection<br>MalOp. When the same process is<br>again detected and/or prevented and<br>associated with the same MalOp, a<br>notifcation is sent to all relevant users.|



Notification options include:


|Notification<br>Setting|Description|
|---|---|
|Enable email<br>notifcations|When set to**On**, all users with notifcations<br>enabled will receive an email according to<br>the settings in this section.|
|MalOp Type|Choose which type of MalOp users should<br>receive notifcations for. Options are:<br>AI Hunting MalOps<br>Endpoint Protection MalOps|
|Frequency|Choose when email notifcations are sent.<br>Options are:<br>Immediate: An email is sent each time a<br>notifcation is triggered.<br>Daily: A summary email is sent at the end<br>of each day for the notifcations that<br>occurred since the last email was sent.<br>Weekly: A summary email is sent at the<br>end of each week for the notifcations that<br>occurred since the last email was sent.|
|Notify me<br>when|Choose what action triggers an email<br>notifcation. Options are:<br>MalOp is created: Send notifcation when<br>any MalOp is created<br>MalOp is created or updated: Send<br>notifcation when any MalOp is created,<br>or when an Active MalOp is updated. A<br>MalOp is considered updated when the<br>behavior that frst caused the MalOp<br>occurs again.|


## Enable notifications for individual users

User admins can enable notifications for individual users and
individual users can enable notifications for themselves.


**Enable individual notifications as a User administrator:**


1. In the **Users** screen,locate the user name, and click **Edit** .


2. In the user settings, select **Enable notifications** .

3. Click **Save** to update the user settings.


Note


Users with the Local analyst L1 or L2 role will only receive


emails about MalOps that involve sensors in the sensor

groups the user has access to.


**Enable notifications for your own user:**


1. In the upper right corner of the Cybereason platform (from any


screen), click your user name to display the user preferences

menu.


2. In the user preferences menu, select **Enable email**

**notifications** .

## ## Known limitations notifications


The following are known limitations for email notifications.


Email notifications cannot be sent when configured to send

over TLS or SSL.


Translations to languages other than English are not available
for email notifications.


If the LastPass Chrome extension is enabled, and an

administrator edits user details in the **Users** screen, LastPass


automatically fills in the password fields, and the administrator

is forced to change the user password. To resolve this


limitation, disable the LastPass Chrome extension for the

Cybereason platform.


If a sensor moves to a new Detection server as part of a

rebalancing operation in your environment, you may


sometimes get redundant notification emails about MalOps

related to that sensor.


In the MalOp email notification, a Connection to a malicious

domain MalOp contains a clickable link to the malicious


domain.

If your WebApp server is restarted, because the notification


history is maintained in the WebApp server database for up to
30 days, you may receive notifications for irrelevant MalOps


that were updated in the previous 30 days.





