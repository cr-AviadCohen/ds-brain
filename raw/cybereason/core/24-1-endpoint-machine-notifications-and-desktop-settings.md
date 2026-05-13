The end user machine displays a popup notification when


malware is detected. Notifications also appear in the Windows

Action Center.


Note


The color of the Cybereason icon has been changed to white.


In previous versions, the icon is blue.


If a scan is run on your machine, you will see one of these


statuses:












|Status|Description|
|---|---|
|Starting a path<br>scan|Signatures AV receives the path scanning<br>command and initiates the scan.|
|Scan done|The scan is complete.|
|Busy|The system is already scanning a custom<br>path. This status is displayed when the user<br>initiates a scan while the system is busy<br>initiating another full or system scan from the<br>UI tray. This status is not displayed when a<br>scan is initiated from the command line.|
|Scan aborted|The scan is aborted when a**Scan stop**<br>command is returned from the command<br>line or UI system tray during a path scan.|
|Error in path<br>scan|Indicates an error in reading the status of<br>the path scan in the UI. This may also<br>indicate a Signatures AV error.|
|Cannot open<br>path - check<br>permissions|This error is displayed when the user<br>initiates a scan on a folder that is not<br>accessible or does not exist. The user is<br>recommended to check the folder<br>permissions.|



Depending on whether something is detected on the machine,

you may see one of the following statuses:


|Status|Meaning|
|---|---|
|A malicious fle was<br>quarantined from<br>this path|An analyst selected the**Quarantine**<br>**fle** remediation action for this endpoint<br>machine, and a fle under the specifed<br>path was quarantined.|
|A malicious process<br>was terminated|An analyst selected the**Kill active**<br>**processes** remediation action for this<br>endpoint machine (the machine on<br>which the notifcation is triggered).|
|A malicious registry<br>key was deleted|An analyst selected the**Remove a**<br>**registry entry** remediation action for<br>this endpoint machine (the machine on<br>which the notifcation is triggered).|
|A quarantined fle<br>was restored under<br>this path|An analyst selected the**Unquarantine**<br>**fle** remediation action for this endpoint<br>machine, and a fle was restored under<br>the specifed path.|
|API invocation|Exploit protection detected an attempt<br>to breach the API invocation mitigation.|
|Binary loading|Exploit protection detected an attempt<br>to breach the binary loading mitigation.|
|Can't update now.<br>Please try again<br>later.|User clicked to update, but Anti-<br>Malware > Signatures update failed.|
|Child process<br>creation|Exploit protection detected an attempt<br>to breach the child process creation<br>mitigation.|
|Cybereason<br>protection is being<br>installed|A frst update of the Anti-Malware ><br>Signatures database is in progress.|
|Detection only|Anti-Malware > Signatures is set to<br>Detect mode.|
|Download and<br>execute|The Cybereason platform detected an<br>attempt to execute a downloaded<br>payload.|
|Dynamic code<br>generation|Exploit protection detected an attempt<br>to breach the dynamic code<br>generation mitigation.|
|Exploit attempt<br>detected|Exploit protection detected an exploit<br>attempt.|


|Status|Meaning|
|---|---|
|Exploit attempt<br>prevented|Exploit protection detected and<br>prevented an exploit attempt.|
|Export address|Exploit protection detected an attempt<br>to breach the export address fltering<br>mitigation.|
|Heap spray|Exploit protection detected an attempt<br>to breach the heap spray mitigation.|
|Import address|Exploit protection detected an attempt<br>to breach the import address fltering<br>mitigation.|
|Malicious download|The Cybereason platform detected an<br>attempt to launch malicious<br>'Downloads' commands.|
|Malicious fle was<br>detected|Anti-Malware detected a malicious fle.|
|Malware was<br>quarantined|Anti-Malware quarantined a malicious<br>fle.|
|Malicious payload<br>detected|The Cybereason platform detected<br>and blocked a malicious payload.|
|Malicious<br>PowerShell<br>command was<br>blocked|The Cybereason platform detected<br>and blocked a malicious PowerShell<br>command.|
|Malware was<br>blocked|Anti-Malware blocked a malicious fle.|
|Malware was<br>detected and<br>disinfected|Anti-Malware detected and disinfected<br>a malicious fle.|
|Malware was<br>detected|Anti-Malware detected a malicious fle.|
|.NET Malicious<br>foating module|The Cybereason platform detected a<br>malicious foating module.|
|PowerShell attack<br>was blocked|The Cybereason platform detected<br>and blocked a PowerShell attack.|
|PowerShell attack<br>was detected|The Cybereason platform detected a<br>PowerShell attack.|


|Status|Meaning|
|---|---|
|Ransomware was<br>detected|The Cybereason platform detected a<br>malicious process that indicates a<br>ransomware attack.|
|Simulate execution|Exploit protection detected an attempt<br>to breach the simulate execution<br>mitigation.|
|Stack integrity|Exploit protection detected an attempt<br>to breach the stack integrity mitigation.|
|System call|Exploit protection detected an attempt<br>to breach the system call mitigation.|
|System is currently<br>performing an<br>update|Anti-Malware > Signatures is currently<br>downloading an update.|
|Update is on the<br>way|User clicked to update. Anti-Malware ><br>Signatures update is now in progress.|
|USB device was<br>blocked|The Cybereason platform blocked a<br>removable storage device on the<br>endpoint machine (the**Endpoint**<br>**controls > Device control** option is<br>enabled on the policy assigned to this<br>endpoint machine).|
|Your machine is no<br>longer isolated.|An analyst selected the**Stop isolating**<br>remediation action for this endpoint<br>machine.|
|Your machine was<br>isolated for security<br>purposes. Contact<br>your IT team.|An analyst selected the Isolate<br>machine remediation action for this<br>endpoint machine (the machine on<br>which the notifcation is triggered).|
|Your PC is protected|Anti-Malware > Signatures is enabled<br>and is set to Disinfect mode.|



On the machine, the machine user can optionally perform a


manual Anti-Malware signature database update in the System

tray icon by clicking **Update** . This is not usually necessary, as by


default, signatures are updated every 15 minutes.


## - System tray icon Signatures scan

## actions and details

The machine user can right-click the Cybereason icon to perform


updates or Anti-Malware Signatures scans, or to view the Anti
Malware Signatures status and installation details. For more


[information on types of Signatures scans, see How does](https://nest.cybereason.com/s/knowledge-base?article=24-1-signature-based-analysis&language=en_US#how-does-signature-based-analysis-work)

[signature-based analysis work? (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-signature-based-analysis&language=en_US#how-does-signature-based-analysis-work)


[signature-based-analysis&language=en_US#how-does-signature-](https://nest.cybereason.com/s/knowledge-base?article=24-1-signature-based-analysis&language=en_US#how-does-signature-based-analysis-work)

[based-analysis-work).](https://nest.cybereason.com/s/knowledge-base?article=24-1-signature-based-analysis&language=en_US#how-does-signature-based-analysis-work)


When a machine user right-clicks the Cybereason icon, the


following options are visible:



|Option|Description|
|---|---|
|Update|Instructs the Cybereason platform to immediately<br>trigger an update of the Anti-Malware signature<br>database.|
|Quick<br>scan|Runs a quick scan. For more information on types of<br>scans, see Confgure scan properties<br>(/s/knowledge-base?article=24-1-set-the-anti-<br>malware-modes&language=en_US#confgure-scan-<br>properties).|
|Full<br>scan|Runs a full scan. For more information on types of<br>scans, see Confgure scan properties<br>(/s/knowledge-base?article=24-1-set-the-anti-<br>malware-modes&language=en_US#confgure-scan-<br>properties).|
|Stop<br>scan|Stops a scan that is currently running. This action is<br>only visible when a scan is in progress.|


Note





If a user attempts to click **Quick scan** or **Full scan** while a
scan is running, one of the following notifications appears in


the system tray: "The Cybereason platform is running a quick

scan" or "The Cybereason platform is running a full scan".


Details related to the Anti-Malware Signatures mode feature are


visible below the actions. Details include:









|Field|Description|
|---|---|
|Connection<br>Status|The connection status of the sensor with the<br>Cybereason server (from version 23.1.152<br>and higher).|
|Status|The**Anti-Malware > Signatures** mode status.<br>For example, this indicates whether the<br>feature is being installed or whether a scan is<br>running.|
|Last update|The time of the last Anti-Malware signature<br>database update.|
|Last full scan|The time of the last full scan.|
|Last quick<br>scan|The time of the last quick scan.|
|Signature DB<br>version|The version of the Signatures database.|
|Version|The Cybereason sensor version (from version<br>23.1.152 and higher).|

## Configure end user desktop settings

You can configure end user UI settings to show/hide the system
tray icon and notifications on end user machines.


Administrators can configure the following settings when creating

or editing policies:


Show/hide the system tray icon.
Show or hide notifications of activity for different NGAV


features.


This enables SOC teams to notify end users when remediation


actions are performed on their machine.


To help deliver notifications, the Cybereason sensors use the


system tray icon. Before you can deliver specific notifications, you

must enable the system tray icon:


1. In your sensor policy, navigate to the **Endpoint UI Settings**


screen.


2. In the **Endpoint UI Settings** screen, find the **System tray**


**icon** section and set the toggle to **Show** .



