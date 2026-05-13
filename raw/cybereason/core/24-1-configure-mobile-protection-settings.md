5. When available, in the **Auto response** column, for specific


threat alerts, select the possible response action ( **Block**


device traffic or **Secure*** device traffic through a secure

channel):






|Action|Included Alerts|
|---|---|
|**Block**|Supported threat alerts include:<br>Phishing<br>Data Leaks<br>Malware Network Traffc<br>Cryptojacking<br>Spam<br>Download from a Third-Party App Store<br>Malware<br>Risky iOS Profle|
|**Secure**|Supported threat alerts include:<br>Risky Hotspots<br>Man-in-the-Middle attacks (including all<br>subtypes of threat alerts)|



6. Above the threat list, click **Save** to update all changes.


[For details on each threat, see Cybereason Mobile Threat Alerts](https://nest.cybereason.com/s/knowledge-base?article=24-1-cybereason-mobile-threat-alerts&language=en_US#cybereason-mobile-threat-alerts)


[(/s/knowledge-base?article=24-1-cybereason-mobile-threat-](https://nest.cybereason.com/s/knowledge-base?article=24-1-cybereason-mobile-threat-alerts&language=en_US#cybereason-mobile-threat-alerts)

[alerts&language=en_US#cybereason-mobile-threat-alerts).](https://nest.cybereason.com/s/knowledge-base?article=24-1-cybereason-mobile-threat-alerts&language=en_US#cybereason-mobile-threat-alerts)

## Add UEM tags to alert your UEM/MDM


You can add specific tags for each threat to enable your
UEM/MDM platform to perform specific response actions when


Cybereason Mobile detects the threat on a device.


The use of tags is supported on these MDM platforms:


Workspace ONE

Microsoft Endpoint Manager (formerly Intune)


IBM MaaS360

MobileIron Core


Note


Certain UEM/MDM platforms have additional response actions


that are specific to the UEM/MDM platform and are performed

by the UEM/MDM platform. These response actions are


performed based on the UEM tags you add.


These response actions performed by the UEM/MDM platform


are different from the automatic response actions performed

by Cybereason Mobile.


**To add UEM tags, follow these steps:**


1. As part of the process to integrate your UEM/MDM platform


with Cybereason Mobile, ensure that you configure conditional

access for your UEM/MDM platform.


For details on how to set up conditional access, see:

[Configure Conditional Access for Endpoint Manager](https://nest.cybereason.com/s/article/2946481#toc-step-7-configure-conditional-access-for-endpoint-manager)


[(/s/article/2946481#toc-step-7-configure-conditional-](https://nest.cybereason.com/s/article/2946481#toc-step-7-configure-conditional-access-for-endpoint-manager)

[access-for-endpoint-manager)](https://nest.cybereason.com/s/article/2946481#toc-step-7-configure-conditional-access-for-endpoint-manager)


[Configure Conditional Access for Workspace ONE](https://nest.cybereason.com/s/article/2946543#toc-step-7-configure-conditional-access-for-workspace-one)
[(/s/article/2946543#toc-step-7-configure-conditional-](https://nest.cybereason.com/s/article/2946543#toc-step-7-configure-conditional-access-for-workspace-one)


[access-for-workspace-one)](https://nest.cybereason.com/s/article/2946543#toc-step-7-configure-conditional-access-for-workspace-one)

[Add a compliance rule and apply the rule to custom](https://nest.cybereason.com/s/article/2948082#toc-step-11-add-a-compliance-rule-and-apply-the-rule-to-custom-attribute-and-groups)


[attributes and groups (/s/article/2948082#toc-step-11-](https://nest.cybereason.com/s/article/2948082#toc-step-11-add-a-compliance-rule-and-apply-the-rule-to-custom-attribute-and-groups)

[add-a-compliance-rule-and-apply-the-rule-to-custom-](https://nest.cybereason.com/s/article/2948082#toc-step-11-add-a-compliance-rule-and-apply-the-rule-to-custom-attribute-and-groups)


[attribute-and-groups) (for IBM MaaS360)](https://nest.cybereason.com/s/article/2948082#toc-step-11-add-a-compliance-rule-and-apply-the-rule-to-custom-attribute-and-groups)

[Create a compliance policy and apply it to a label](https://nest.cybereason.com/s/article/2947998#toc-step-10-create-a-compliance-policy-and-assign-it-to-a-label)


[(/s/article/2947998#toc-step-10-create-a-compliance-](https://nest.cybereason.com/s/article/2947998#toc-step-10-create-a-compliance-policy-and-assign-it-to-a-label)

[policy-and-assign-it-to-a-label) (for MobileIron Core)](https://nest.cybereason.com/s/article/2947998#toc-step-10-create-a-compliance-policy-and-assign-it-to-a-label)


2. In the **Security Policy > Mobile security policy** screen, next

to the threat, click the **+** button to open the edit field to add a


tag.


3. Enter the tag from your UEM/MDM platform to use. These tags


are created by your UEM/MDM platform administrators.


As you type, the **Mobile security policy** screen displays

available tags that match your current entry.


4. Click **Save** to update all changes.

## Add trusted root certificates


To help the detection of mobile threats, Cybereason Mobile


cryptographically analyzes various SSL certificates and their
issuers to verify the certificate using known global root certificate


authorities. If your mobile infrastructure utilizes other internal
certificates or certificate authorities, Cybereason Mobile may


generate unnecessary security alerts for these certificates.


You should upload your trusted root certificates in your Mobile


security profile to prevent these events.


**To add a trusted root certificate, follow these steps:**


1. In the Cybereason platform, navigate to the **Security Profile >**


**Mobile security policy** screen.


2. In the **Mobile security policy** screen, open the **Trusted root**

**certificates** tab.


3. In the main part of the **Trusted Root Certificate** tab, drag the

certificate to the edit area or click the edit area to browse to


the certificate file.


4. Click **Save** to update all changes.

## Update your Service Control settings


Service Controls in Cybereason Mobile enable you to control more


advanced settings for your devices, such as profile PIN locks,

routing options, and data routing options, data privacy mode, and


advanced APN preferences.


Your Cybereason Mobile team will help you set these options in


your Cybereason Mobile instance but you should be aware of the

options you have.


You can set the following options:


|Pin locked<br>Profiles<br>(iOS<br>devices<br>only)|This option enables you to prevent users from<br>removing the Cybereason Mobile sensor<br>(Wandera app) from a device. When enabled,<br>this requires the device user to enter a PIN<br>number to remove the app and its associated<br>profile from their device.<br>These PIN codes are dynamically generated by<br>Cybereason Mobile and are unique to the<br>device.<br>Due to change by Apple for app permissions,<br>this option is available in a different manner for<br>different iOS versions:<br>If you have devices running iOS versions<br>earlier than iOS 13, you can use this option<br>on all devices.<br>If you have devices running iOS versions 13<br>and later, the device must be a supervised<br>device. If your devices with iOS 13 and later<br>are not supervised devices, talk to your<br>Apple representative to learn how to make<br>these devices into supervised devices.|
|---|---|
|Privacy<br>mode|End-user privacy is a growing concern for<br>organizations, especially as regional regulations<br>take hold to protect individuals and their digital<br>lives.<br>By default, Cybereason Mobile displays the real<br>user information, including web browsing and<br>app activity in reports. This setting enables you<br>to anonymize user information and activity in<br>reports where this information is normally<br>included.|
|Search<br>Engines|You can also enable the use of SafeSearch for<br>all devices that use the Proxy level of protection.<br>If you enable Google SafeSearch, all proxy-<br>enabled devices will have Google search results<br>fltered.|







