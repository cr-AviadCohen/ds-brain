|Device<br>type|Device<br>type<br>name|Example|Description|Supported<br>OS/version|Suppo<br>modes|Col7|
|---|---|---|---|---|---|---|
|USB<br>storage<br>devices|**USB**<br>**storage**<br>**device**|A USB<br>fash<br>drive|USB<br>storage<br>devices<br>identifed as<br>a USB mass<br>storage<br>device.|Windows<br>Linux<br>macOS|**Fu**<br>**Ac**<br>**Re**<br>**on**<br>(Av<br>on<br>Wi<br>an<br>on<br>**Blo**||
|MTP<br>devices|**MTP**<br>**device**|A<br>Samsung<br>or<br>Android<br>phone|Mobile<br>(Android<br>and iOS)<br>media<br>devices that<br>are<br>connected<br>to the<br>endpoint via<br>a USB<br>connection.|Windows<br>Linux|**Fu**<br>**ac**<br>**Blo**||
|USB<br>devices|**All**|A USB<br>keyboard|Other USB<br>devices,<br>such as a<br>USB<br>keyboard,<br>mouse, etc.<br>and to grant<br>or deny<br>access to<br>these<br>devices.|Windows<br>macOS<br>does not<br>support<br>blocking<br>such<br>devices<br>(e.g.<br>using<br>the<br>Manage<br>Devices<br>feature).<br>Linux|**Fu**<br>**Ac**<br>**Re**<br>**on**<br>**Blo**<br>se<br>ind<br>de<br>in<br>**Ma**<br>**de**<br>are||
|View Device control events and monitor<br>USB usage<br>Note|View Device control events and monitor<br>USB usage<br>Note|View Device control events and monitor<br>USB usage<br>Note|View Device control events and monitor<br>USB usage<br>Note|View Device control events and monitor<br>USB usage<br>Note|View Device control events and monitor<br>USB usage<br>Note||


This feature is available by default for Windows machines only


if you enabled Device Control in a sensor policy.


In the **Device control** screen, you can view Device control events


and easily monitor the usage of USB devices across your

environment. This can help you:


Ensure that defined policies are working effectively to reduce

data leak risks and USB drive-by malware.


Gain insight on events and improve your organization's

security posture.


For example, in your sensor policy, you instruct the Cybereason


platform to block USB devices. Then, as users insert USB devices

into endpoint machines that use that sensor policy, the


Cybereason platform blocks these USB device and reports these

events on the **Device control** screen. You can check the **Device**


**Control** screen regularly to ensure that the policy is enforced on

the relevant endpoint machines.


Click **Export** to export the list of device control events to a CSV
file.


Note


The data in the Device Control screen is retained for 30 days.


The screen includes reporting of **Block** and **Read only** events

only.

## View the Device control status in the

## Sensors screen


You can view the Device control status for single endpoints or for

groups of endpoints in the **System > Sensors** screen. To display


the Device control status, select **Columns** to the right of the

sensors table, and select the **Device control** column.


The **Device control** column is visible in the list of sensors:


View the Device control status:






|Status|Description|
|---|---|
|**Enabled**|Device control is enabled. The**Device control**<br>toggle in the**System > Policies management >**<br>**Endpoint Controls** screen is turned on with any<br>mode selected.|
|**Disabled**|The**Device control** toggle in the**System >**<br>**Policies management > Endpoint controls**<br>screen is turned off.|
|**Advanced**|Device control is enabled and exclusions are<br>defned, according to the following confguration:<br>The**Device control** toggle in the**System >**<br>**Policies management > Endpoint controls**<br>screen is turned on.<br>Exclusions have been added under the<br>**Device control exclusions** section.|



The information in the **Device control** column is also used as

metadata if you export the table to a CSV file.

## Related resources


[Security value of Device control (/s/article/2762629)](https://nest.cybereason.com/s/article/2762629)

[Device control FAQ (/s/article/2542330)](https://nest.cybereason.com/s/article/2542330)



