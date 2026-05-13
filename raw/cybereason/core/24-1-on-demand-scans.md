2. During and after the scan, the Cybereason system tray


(CrAmTray.exe) displays one of the following statuses:












|Status|Description|
|---|---|
|Starting a path<br>scan|Signatures AV receives the path<br>scanning command and initiates the<br>scan.|
|Scan done|The scan is complete.|
|Busy|The system is already scanning a<br>custom path. This status is displayed<br>when the user initiates a scan while the<br>system is busy initiating another full or<br>system scan from the UI tray. This status<br>is not displayed when a scan is initiated<br>from the command line.|
|Scan aborted|The scan is aborted when a**Scan stop**<br>command is returned from the command<br>line or UI system tray during a path<br>scan.|
|Error in path<br>scan|Indicates an error in reading the status of<br>the path scan in the UI. This may also<br>indicate a Signatures AV error.|
|Cannot open<br>path - check<br>permissions|This error is displayed when the user<br>initiates a scan on a folder that is not<br>accessible or does not exist. The user is<br>recommended to check the folder<br>permissions.|



Example of the Cannot open path - check permissions error in


the system tray:

## On demand scan from the system tray


You can perform a quick scan or full scan of machines from the


system tray.


**To perform a scan from the system tray, follow these steps:**


1. Right-click the Cybereason icon on the system tray.

2. Select **Quick Scan** or **Full Scan** .


For more details on the notifications seen when you run a scan


[from the system tray, see System tray icon - Signatures scan](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-signatures-scan-actions-and-details)

[actions and details (/s/knowledge-base?article=24-1-endpoint-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-signatures-scan-actions-and-details)


[machine-notifications-and-desktop-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-signatures-scan-actions-and-details)

[settings&language=en_US#system-tray-icon-signatures-scan-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-signatures-scan-actions-and-details)


[actions-and-details).](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-signatures-scan-actions-and-details)

## Command Line (CLI) scan on the


This feature is available on supported Windows operating


systems.


You can can initiate the following Anti-Malware scans from the


command line (CLI), on the endpoint itself:


Full scan


Quick scan

Scan of a specific path


A scan initiated from the command line is the same as a

scheduled scan or a scan initiated from the UI; for example,


exclusions are not scanned.


**To run a scan from the command line, follow these steps:**


1. Open the command prompt.

2. Navigate to the following path:


**C:\Program Files\Cybereason ActiveProbe**

3. Enter CrScanTool.exe followed by the command for the action


you want to take:

|Command|Description|
|---|---|
|update|Updates the signature database|
|scan full|Initiates a full system scan|
|scan quick|Initiates a quick system scan|
|scan stop|Stops an ongoing scan|
|scan path <path>|Scans the specifed path|



**Examples**


The following command initiates a full scan:

```
 C:\Program Files\Cybereason ActiveProbe>

 CrScanTool.exe scan full

```

The following command scans a specific path:

```
 C:\Program Files\Cybereason ActiveProbe>

 CrScanTool.exe scan path

 C:\Users\john.doe\Documents\

## On demand scan from the Sensors

## screen

```

This feature is available for all supported operating systems.


You can select specific sensors in the **Sensors** screen and


perform full or quick on demand scans. Local drives are scanned,

not network drives.


You can view the last time a scan was completed in the **Last**

**quick scan** and **Last full scan** columns of the Sensors screen.


**To perform an on demand scan, follow these steps:**


1. From the **System > Sensors** screen, select the sensors on


which to run the scan.

2. From the Actions menu, select **Start system scan** .


3. Select the type of scan you want to perform: Full / Quick.


You can select **Stop system scan** to stop a scan in progress.


Note


A full scan may cause higher CPU usage than usual.

## - Known Limitations on-demand scans


The following are known limitations for the various types of scans:






|Scan<br>type|Limitations|
|---|---|
|Right-<br>click<br>scans|Only one scan at a time can be performed,<br>other AV commands that are received are<br>rejected. Commands cannot be queued.<br>To scan a specifc path, the path can contain a<br>maximum of 1,040 characters.<br>Universal Naming Convention (UNC) path is<br>only supported if the path is mapped as a<br>drive and is visible to the LocalSystem user.|


|Scan<br>type|Limitations|
|---|---|
|CLI<br>scans|Currently there is no indication that a scan is in<br>progress. The only indication is that the<br>command has been successfully sent.<br>Only one scan at a time can be performed,<br>other AV commands that are received are<br>rejected. Commands cannot be queued.<br>To scan a specifc path, the path can contain a<br>maximum of 1,040 characters.<br>Universal Naming Convention (UNC) path is<br>only supported if the path is mapped as a<br>drive and is visible to the LocalSystem user.|







