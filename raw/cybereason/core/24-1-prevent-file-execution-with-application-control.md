Application Control is not supported on endpoints with


Cluster Shared Volume (CSV).


The Cybereason platform adds every hash marked for


prevention to the blocklist.

The Cybereason platform generates an Endpoint Protection


MalOp of type **App Control** when the hash is prevented in the

future.


Important


Be careful not to mark critical applications such as cmd.exe,


explorer.exe, and PowerShell for prevention. If you do choose

to prevent critical applications, note that legitimate processes


may be prevented as well.


[You enable Application Control through Sensor Policies](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


[(/s/knowledge-base?article=24-1-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)

[policies&language=en_US#sensor-policies) or by using](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


installation parameters.


Note


Installation parameter settings override policy settings for that

sensor.


**Enable in a sensor policy (recommended):**


In a sensor policy, in the **App Control** screen, enable Application


Control.


**Enable in installation parameters:**


When you install a sensor, you can enable or disable Application

Control with the **AP_APP_CTRL** command line parameter as


follows:


|AP_APP_CTRL value|Description|
|---|---|
|1|Enable Application Control|
|2|Disable Application Control. (Default)|

## Mark files for prevention

Analysts can mark executables or modules for prevention using

one or more of the following methods:






|Location|How to prevent|
|---|---|
|**Malops**<br>**management**<br>screen|1. On the left of the**Malops management**<br>screen, above the MalOp results, click<br>**Respond**.<br>2. Select 'Malop is malicious - Remediate'.<br>3. Select 'Prevent execution' and click<br>**Respond**.|
|**Malop details**<br>screen|1. In the top right of the**Malop details**<br>screen, click**Respond**.<br>2. Select the**Prevention** checkbox and<br>click**Apply**.|
|**Investigation**<br>screen|1. In the**Element details** screen, click<br>**Prevention**.<br>2. Click**Prevent**.|
|**Reputations**<br>screen|1. In the**Security > Profle >**<br>**Reputations** screen, click**Add item** or<br>**Upload CSV**.<br>2. Add the new reputation item (fle hash,<br>domain name, or IP address).<br>3. If you are adding a fle hash value,<br>ensure you select the**Detect and**<br>**Prevent** option or ensure that the CSV<br>fle has the value set accordingly for<br>prevention in the appropriate column.|



To stop prevention later, use the **Investigation** screen to locate

the item you prevented. From the item's Element Details pane,


click the **Prevention** button and select **Stop preventing** .



