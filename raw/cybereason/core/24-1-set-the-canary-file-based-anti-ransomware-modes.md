|Mode|Description|Recommendation|
|---|---|---|
|Disabled<br>(default)|Anti-Ransomware is<br>disabled. Disabling Anti-<br>Ransomware cleans up<br>existing canary fles from<br>endpoints.|Not recommended.<br>Can be used in cases<br>where ransomware<br>detection is not<br>required, or if it is<br>necessary to remove<br>canary fles.|
|Detect|Anti-Ransomware is<br>enabled in detect-only<br>mode. When<br>ransomware is detected,<br>a MalOp is generated,<br>but no further action is<br>taken.|Not recommended.<br>Use for testing<br>purposes only.|
|Suspend|Anti-Ransomware is<br>enabled in detect and<br>suspend mode. When<br>ransomware is detected,<br>a MalOp is generated,<br>and a specifc thread of<br>the process is<br>suspended. This thread<br>is permanently<br>suspended and cannot<br>run or perform actions,<br>while the rest of the<br>process can keep<br>running.|Not recommended.<br>Use for testing<br>purposes only.|


|Mode|Description|Recommendation|
|---|---|---|
|Prevent|Anti-Ransomware is<br>enabled in detect,<br>suspend, and prevent<br>mode. When<br>ransomware is detected,<br>a MalOp is generated,<br>the process is<br>suspended, and the<br>same process is<br>prevented from<br>executing on the same<br>endpoint machine.<br>Note<br>Cybereason<br>recommends that you<br>enable Application<br>Control when using<br>this mode. If<br>Application Control is<br>disabled, the<br>Cybereason platform<br>does not prevent the<br>process from<br>executing in the<br>future on the same<br>endpoint machine.|Recommended.|

## Set canary file preferences

To help detect ransomware, the Anti-Ransomware feature uses


canary files. Canary files are designed in a way that encourages
malware to attack these files first, which alerts the Cybereason


platform to the presence of ransomware.


**To configure canary file preferences, follow these steps:**


1. In your sensor policy, navigate to the **Anti-Ransomware**

screen, locate the **Canary files** section, and then select the


folders where you want to place canary files from the following

options:


**Root drives**

**Users folder**


**Desktop**

**Users documents**


Important


To fully benefit from the ransomware feature, Cybereason

recommends to select relevant folder locations and not to


leave all folder checkboxes cleared. If you do not select
any folders, the canary files functionality is considered


disabled.


2. For each file location, select the visibility of the canary files:


**Visible:**

**Hidden**


**System hidden**


Important


For full protection, select the **Visible** option for all selected

folders.


3. Below the canary file location options, locate the Suffix


section.


4. For the **Folder suffix** and **File suffix** options, add your

custom file suffix. Your custom suffix must use only letters and


numbers.

## Configure behavioral Anti-Ransomware

## detection options


You can also instruct the Cybereason platform to detect


ransomware based on the following behaviors:


The ransomware deletes shadow copies on the machine as


part of its pattern.

The ransomware edits the Master Boot Record (MBR) on


Windows machines.


**To enable behavioral Anti-Ransomware features, follow these**


**steps:**

1. In the **Anti-Ransomware** screen, below the **Canary files**


section, locate the **Shadow copy** option and set the toggle to

**On** .


This option enables the Cybereason platform to find

ransomware that deletes shadow copies on the machine as


part of its pattern.
2. Below the **Shadow copy** section, find the **MBR** section and


set the toggle to **On** .
This option enables you to find ransomware that edits the


Master Boot Record (MBR) on Windows machines.

## individual sensors


You can configure Anti-Ransomware for individual sensors in the


**Sensors** screen.



