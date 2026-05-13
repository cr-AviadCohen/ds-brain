|Device<br>type|Supervision available|
|---|---|
|iOS|For iOS devices, you can have**supervised** or<br>**unsupervised** devices.<br>You make an iOS device a supervised device<br>through the Apple Device Enrollment Program<br>(DEP).|


|Device<br>type|Supervision available|
|---|---|
|Android|Android have both partially managed and fully<br>managed devices through Android Enterprise.<br>For fully managed devices, you can have:<br>Company-owned devices<br>Employee owned devices<br>For partially managed devices, you add a**Work**<br>**Profle** to user devices. You can use the Work<br>Profle for:<br>Company-owned devices<br>Employee owned devices|


Before you select your deployment mode, you need to evaluate

the devices in your organization and assess what types of devices


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
|Cloud Proxy|The proxy protection mode provides a secure<br>proxy for your mobile devices to access the<br>network. Mobile Threat Defense routes device<br>traffc through the proxy to provide protection<br>against network-based attacks.|
|Secure<br>Access<br>Layer (SAL)<br>- Secure<br>DNS|This protection mode extends the proxy<br>protection and provides additional benefts:<br>The ability to create a secure network<br>when needed, such as when a type of<br>network-based threat is detected<br>Detection of threats to the device based<br>on certain activities|
|Next-Gen<br>VPN|This mode provides a VPN with a data<br>encryption protocol for applications without<br>user interactions.|



For details on the device support and service support for each of


[these modes, see Traffic Vectoring Options](https://docs.jamf.com/jamf-security/radar/documentation/Traffic_Vectoring_Options.html)

[(https://docs.jamf.com/jamf-](https://docs.jamf.com/jamf-security/radar/documentation/Traffic_Vectoring_Options.html)


[security/radar/documentation/Traffic_Vectoring_Options.html) in](https://docs.jamf.com/jamf-security/radar/documentation/Traffic_Vectoring_Options.html)

the Jamf Security documentation.


[Please see our Legal Disclaimer (/s/article/legal-disclaimer-third-](https://nest.cybereason.com/s/article/legal-disclaimer-third-party-web-sites)

[party-web-sites) on links to third party web sites.](https://nest.cybereason.com/s/article/legal-disclaimer-third-party-web-sites)



