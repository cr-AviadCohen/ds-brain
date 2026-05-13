## Manually quarantine from the Malop details screen

To quarantine a file from the **Malop details** screen:

1. Click **Respond** from a specific MalOp's **Malops details**


screen, and select **Quarantine** .


2. In the **Respond** window, select the **Quarantine** check box for

the file(s) you want to quarantine.


3. Click **Apply response**

## Manually quarantine from the Malops


To quarantine a file from the **Malops management** screen:


1. Select the check box next to the MalOp or MalOps whose


associated file or files you want to quarantine.

2. Click **Respond** .


3. Select **Malop is malicious - Remediate** .

4. In the **Respond** window, select the **Quarantine** check box for


the file(s) you want to quarantine.


5. Click **Apply response**


## Quarantined file locations

When you quarantine a file, the Cybereason platform places the


file in the following folder location:


**Windows** : C:\ProgramData\apv2\Quarantine


**Mac** : /usr/local/cybereason/Quarantine

**Linux** : /opt/cybereason/sensor/Quarantine


You cannot change this default location.


The Cybereason platform deletes quarantined files after 30 days.


The cleanup is scheduled to run daily (every 24 hours) and on

sensor startup.

## Search for quarantined files


You can use the **Quarantine File** Element in the **Investigation**
screen to search for currently quarantined files. If you identify a file


that you want to unquarantine, click the Element from the results

grid to display the **Element details** pane. From there, you can


download the file or access the MalOp associated with the file.


Beginning in version 23.2.148 and later, you can also view all
quarantined files in the **Quarantine files** screen.


Note


This screen is disabled by default. Contact your Customer


Success Manager to request access to this screen.


This screen displays the full list of the files, along with the details


about these quarantined files. Select different columns to show a
variety of information about quarantined files.


From this screen, you can search for a specific quarantined files


by **Original file name**, **Original file path**, **Original File SHA-**
**1/MD5** file hash value, or **Machine name** .


Likewise, you can filter the list of quarantined files to view files


associated with a MalOp, files from online machines, and files that

are from machines of different operating system types.


## Download a quarantined file

You can download a quarantined file without first removing the file

from quarantine.


Note


The machine must be online and connected to your


Cybereason environment to download the quarantined file.


To download a currently quarantined file, search for the


quarantined file, open the **Element details** pane, and select
**Download file** .


During this action, the quarantined file remains encrypted in the
quarantined folder and no changes are made to the file itself.


## Remove a file from quarantine

You can unquarantine a file that was quarantined within the last 30


days. When you unquarantine a file, the Cybereason platform
places the file back in its location at the time of quarantine. If the


original folder does not exist, the Cybereason platform moves up
the folder hierarchy until it find an existing folder.


You unquarantine a file when responding to MalOps from the

**Malop details** or **Malops management** screen.


You also have the option to add the file to the allowlist. This
ensures that the unquarantined file will not trigger a MalOp in the


future.

## Unquarantine from the MalOp details

## screen


**To unquarantine a file from the Malop details screen, follow**


**these steps:**

1. In a specific MalOps **Malop Details** screen, click **Respond**


and select **Unquarantine** .


2. In the **Respond** window, select the **Unquarantine** check box


for the file(s) you want to remove from quarantine.
3. (Optional) To add the unquarantined file to the allowlist, select


the **Unquarantine the file and add it to the allowlist.**

checkbox.


4. Click **Apply response**

## Unquarantine from the Malops


**To unquarantine a file from the Malops management screen,**


**follow these steps:**


1. Select the check box next to the MalOp or MalOps whose


associated file or files you want to remove from quarantine.

2. Click **Respond** .


3. Select **Malop is malicious - Remediate** .

4. In the **Respond** window, select the **Unquarantine** check box


for the file(s) you want to remove from quarantine.
5. (Optional) To add the unquarantined file to the allowlist, select


the **Unquarantine the file and add it to the allowlist.**

checkbox.


6. Click **Apply response** .

## Unquarantine a file from the Quarantine

## Files screen


Note


This screen is disabled by default. Contact your Customer

Success Manager to request access to this screen.


In versions 23.2.148 and later, you can unquarantine files from the
**Quarantined Files** screen. You can select one or more files to


unquarantine, which enables you to more efficiently address these



