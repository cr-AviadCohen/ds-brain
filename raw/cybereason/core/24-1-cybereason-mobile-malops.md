## Next steps: Abnormal Process Activity

Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.

## Android Device possible tampering


The "Android device possible tampering" MalOp is triggered when

an attacker removes the manufacturer's device security limitations


on an Android device. This MalOp indicates that the device is fully

compromised and cannot be trusted.

## Next steps: Android Device possible


Turn on the device Airplane mode to isolate the device.

Uninstall the app and delete any leftover artifacts through the


device file manager.
Instruct the device to forget any suspicious or malicious Wifi


networks.


The "App tampering" MalOp is triggered when an attacker


removes an app's device security limitations. This MalOp indicates

that the app is fully compromised and cannot be trusted.

## Next steps: App tampering


Turn on the device Airplane mode to isolate the device.

Uninstall the app and delete any leftover artifacts through the


device file manager.

## Device configurations that may put

## corporate and personal data at risk


The "Device configurations that may put corporate and personal


data at risk" MalOp is triggered when Cybereason Mobile
discovers configurations on the device that cause the device to be


at risk for data theft.

## Next steps: Device configurations


Turn on the device Airplane mode to isolate the device.


Update the device configurations to match your organization's
preferred configuration settings.


The "Device is Jailbroken/rooted" MalOp is triggered when a user

or attacker gains root access to the device operating system.


On iOS, a user "jailbreaks" the device by using a series of kernel


patches to remove restrictions that the iOS, iPadOS, tvOS, or

watchOS operating systems have placed on the device. This in


turn gives the user root access to the mobile operating system

and the ability to install other software that is not available through


the App Store.


On Android, a user "roots" the device by giving root access to


various operating system subsystems. This action also gives the

user superuser permissions, similar to the process on a Linux


machine.

## Next steps: Device is jailbroken/rooted


Back up the contents of the device.


Reformat the device.

## Elevation of privileges on the device


The "Elevation of privileges on the device" MalOp is triggered


when an attacker or user uses techniques to gain a higher level of

privileges, such as the following techniques:


Entering the device with limited privileges and using a device

vulnerability to obtain higher privileges


Exploit attempts

## Next steps: Elevation of privileges on the


Back up the contents of the device.


Reformat the device.

## Malicious application


The "Malicious application" MalOp is triggered when Cybereason


Mobile detects a malicious app on one or more devices. The

following actions trigger this MalOp:


Threat intelligence sources classify an app as malicious or as

a malware variant.


The app modifies existing application libraries.

The app injects outside libraries into the device.


The app creates connections to malicious addresses.

## Next steps: Malicious application


Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.


## Malware that aggressively displays ads,

## negatively affecting user productivity

## and device performance

The "Malware that aggressively displays ads" MalOp is triggered


when Cybereason Mobile detects app activity with a large number

of ads. This affects the user's ability to use the device and in turn


affects the device performance.

## Next steps: Malware that aggressively


Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.

## Malware that attempts to obtain

## escalated system privileges


The "Malware that attempts to obtain escalated system privileges"

MalOp is triggered when Cybereason Mobile detects app activity


that is trying to change the app's privilege level.

## Next steps: Malware that attempts to

## obtain escalated system privileges


Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.

## Malware that blocks access to a device

## until a ransom is paid


The "Malware that blocks access to a device until a ransom is

paid" MalOp is triggered when Cybereason Mobile detects app


activity that is trying to lock and encrypt a device until the device

user pays a ransom to unlock the device. This is the equivalent of


ransomware for a mobile device.

## Next steps: Malware that blocks access

## to a device until a ransom is paid


Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.


## MITM attack

The "MITM attack" MalOp is triggered when an attacker uses the


Man in the Middle technique to secretly relay and potentially alter

communications between the device and another party.

## Next steps: MITM attack


Turn on the device Airplane mode to isolate the device.
Instruct the device to forget any suspicious or malicious Wifi


networks.

## MITM attack via ARP


The "MITM attack via ARP" MalOp is triggered when an attacker


uses an Address Resolution Protocol (ARP) spoofing attack and
the Man in the Middle technique to intercept network traffic.

## Next steps: MITM attack via ARP


Turn on the device Airplane mode to isolate the device.
Instruct the device to forget any suspicious or malicious Wifi


networks.

## MITM - Fake SSL Certificate


The "MITM - Fake SSL Certificate" MalOp is triggered when an


attacker uses the Man in the Middle technique to intercept
network traffic by removing the Secure Sockets Layer (SSL)


certificate from the device or communication. In this case, the

device sends unencrypted communications that seem to be


encrypted.

## Next steps: MITM - Fake SSL Certificate


Turn on the device Airplane mode to isolate the device.


Instruct the device to forget any suspicious or malicious Wifi

networks.

## MITM attack through SSL Strip


The "MITM attack through SSL Strip" MalOp is triggered when an

attacker uses the Man in the Middle technique to intercept


network traffic and then downgrades the communication protocol

from HTTPS to HTTP. This MalOp enables the attacker to


eavesdrop and manipulate the data that users send through the
network, hijack network traffic, steal credentials, or deliver


malware to a device.

## Next steps: MITM - SSL Strip


Turn on the device Airplane mode to isolate the device.


Instruct the device to forget any suspicious or malicious Wifi


networks.

## MITM via ICMP redirect


The "MITM via ICMP redirect" MalOp redirect is triggered when an


attacker uses an Internet Control Message Protocol (ICMP) attack
and the Man in the Middle technique to intercept network traffic.


This MalOp enables the attacker to eavesdrop and manipulate the
data that users send through the network, hijack network traffic,


steal credentials, or deliver malware to a device.

## Next steps: MITM via ICMP redirect


Turn on the device Airplane mode to isolate the device.


Instruct the device to forget any suspicious or malicious Wifi

networks.

## Persistent modification to device's file


The "Persistent modification to device's file system" MalOp is

triggered when a user or attacker adds a persistence mechanism


to a file on the device's file system.

## - Next steps Persistent modification to

## device's file system


Back up the contents of the device.


Reformat the device.


The "Rogue Access Point" MalOp is triggered when a device


connects to a malicious network. Most devices try to connect to
the Wifi access point that has the strongest signal. Attackers can


set up wireless access points and attempt to cause devices to join

their network. After the device joins the malicious network, the


attacker can manipulate the traffic from the devices.

## Next steps: Rogue Access Point


Turn on the device Airplane mode to isolate the device.


Instruct the device to forget any suspicious or malicious Wifi

networks.

## Sideloaded apps


The "Sideloaded apps" MalOp is triggered when an app is
installed on a device from a source that is not the device's official


App Store. This action usually happens when a user selects the

option on a device to install apps from unknown sources.


## Next steps: Sideloaded apps

Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.

## Site designed to deceive the end user into

## corporate information through a


The "Site designed to deceive the end user into submitting

sensitive personal or corporate information through a seemingly


trusted web form" MalOp is triggered when the device visits a site

that contains what appears to be a regular web form. However,


analysis of the network traffic shows that the web form sends

sensitive information to malicious sites.

## Next steps: Site designed to deceive the

## end user


Turn on the device Airplane mode to isolate the device.

## Suspicious iOS App


The "Suspicious iOS App" MalOp is triggered when Cybereason


Mobile detects abnormal behavior for an app on an iOS device.

## Next steps: Suspicious iOS App


Turn on the device Airplane mode to isolate the device.


Uninstall the app and delete any leftover artifacts through the
device file manager.

## System tampering


The "System tampering" MalOp is triggered when an attacker

removes the manufacturer's device security limitations on an


Android device. This MalOp indicates that the device is fully

compromised and cannot be trusted.

## Next steps: System tampering


Turn on the device Airplane mode to isolate the device.

Uninstall the app and delete any leftover artifacts through the


device file manager.
Instruct the device to forget any suspicious or malicious Wifi


networks.



