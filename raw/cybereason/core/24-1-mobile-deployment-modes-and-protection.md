|Device<br>type|Supervision available|
|---|---|
|iOS|For iOS devices, you can have**supervised** or<br>**unsupervised** devices.<br>You make an iOS device a supervised device<br>through the Apple Device Enrollment Program<br>(DEP).|


|Device<br>type|Supervision available|
|---|---|
|Android|Android have both partially managed and fully<br>managed devices through Android Enterprise.<br>For fully managed devices, you can have:<br>Company-owned devices<br>Employee owned devices<br>For partially managed devices, you add a**Work**<br>**Profle** to user devices. You can use the Work<br>Profle for:<br>Company-owned devices<br>Employee owned devices|


Before you select your deployment mode, you need to evaluate

the devices in your organization and asses what types of devices


you have and the required level of supervision you need.


For each device type and level of supervision, the effect on and


the needs of the device user vary:






|Device<br>type|Supervision|Device user involvement|
|---|---|---|
|iOS|Supervised|The device user manages the<br>settings and controls for the<br>device.<br>Through your UEM/MDM, you can<br>install applications and profles<br>without the need for the device<br>user to perform any actions.<br>There are a limited number of<br>permissions that require the<br>device user's approval.|
|iOS|Unsupervised|The device user is in full control of<br>the device. You can use these<br>devices with your UEM/MDM,<br>which will give you partial control<br>and visibility into the device.<br>However, all required apps,<br>profles, and permissions required<br>the full cooperating of the device<br>user to perform the necessary<br>actions.|


|Device<br>type|Supervision|Device user involvement|
|---|---|---|
|Android|Fully<br>managed|For**company-owned** devices, the<br>device is in the control of the<br>organization.<br>In general, these devices are<br>locked down and only used for<br>specifc actions. While the device<br>settings and controls are<br>managed by the device user, you<br>can install apps and profles<br>without the need for the device<br>user to take any action.<br>A limited number of permissions<br>will require device user interaction.<br>For**employee-owned** devices,<br>the device user is in full control of<br>the device. Use of these devices<br>requires manual steps by you and<br>the device user.|
|Android|Partially<br>managed|For both**company-owned** and<br>**employee-owned** devices, the<br>device uses the**Work Profle**.<br>For employee owned-devices, the<br>device user must install the Work<br>Profle with the apps and settings<br>required. For company owned<br>devices, the profle installation is<br>done automatically.<br>The mobile sensor is installed<br>inside the Work Profle.<br>Both types of devices enable the<br>device user to maintain control<br>over device settings.|


## What deployment modes are available?

Deployment modes include:


|Level|Details|
|---|---|
|Proxy|The proxy protection level provides a secure<br>proxy for your mobile devices to access the<br>network. Cybereason Mobile routes device traffc<br>through the proxy to provide protection against<br>network-based attacks.|
|Secure<br>Access<br>Layer<br>(SAL)|This protection level extends the proxy<br>protection and provides additional benefts:<br>The ability to create a secure network when<br>needed, such as a type of network-based<br>threat is detected<br>Detection of threats to the device based on<br>certain activities|



You perform the necessary setup and configuration for these

modes with your Customer Success team as part of your


onboarding process.

## What type of deployment mode should I


To help you select the deployment mode you need, consider your


device types, level of supervision, and the required deployment

mode.


The table below indicates what deployment mode is supported for

each type of device and supervision level:














|Device<br>type/supervision|Proxy mode<br>supported?|Secure Access<br>Layer mode<br>supported?|
|---|---|---|
|iOS supervised|Yes|Yes|
|iOS unsupervised|Yes|Yes|
|Android fully managed<br>employee owned<br>devices|Yes (with<br>Samsung Knox)|Yes|
|Android fully managed<br>company owned<br>devices|Yes (with<br>Samsung Knox)|Yes|


|Device<br>type/supervision|Proxy mode<br>supported?|Secure Access<br>Layer mode<br>supported?|
|---|---|---|
|Android partially<br>managed employee<br>owned devices|Yes (if sensor is<br>installed outside<br>of the Work<br>Profle)|Yes (only with<br>Work Profle)|
|Android partially<br>managed company<br>owned devices|Yes (if sensor is<br>installed outside<br>of the Work<br>Profle)|Yes (only with<br>Work Profle)|







