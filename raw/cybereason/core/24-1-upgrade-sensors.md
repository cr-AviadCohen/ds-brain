Known issues and limitations - sensor upgrades


Related resources

## Prepare your machines for upgrade


Before you can perform the sensor upgrade, ensure your machine


meets the following requirements:






|Requirement|Details|
|---|---|
|Run a<br>supported<br>operating<br>system|Ensure the endpoint machine runs a<br>supported operating system. For the up-to-<br>date list of all supported operating systems,<br>see Supported OS Versions for the Sensor<br>(/s/knowledge-base?article=24-1-supported-<br>os-versions-for-the-<br>sensor&language=en_US#supported-os-<br>versions-for-the-sensor).|
|Meet<br>minimum<br>system<br>requirements|Check that the machine still meets the<br>minimum system requirements. For details,<br>see Understand the minimum system<br>requirements (all OSs) (/s/knowledge-base?<br>article=24-1-pre-installation-requirements-<br>and-<br>instructions&language=en_US#understand-<br>the-minimum-system-requirements-all-oss).|
|Check<br>required<br>certifcates|Ensure you have the correct certifcates still<br>installed on the machine. For details, see<br>Required Certifcates for Cybereason Sensor<br>Installation (/s/article/3140241).|
|Install<br>required<br>updates|On Windows machines, ensure that your<br>machine has the correct updates. For details,<br>see Install additional KBs (Windows)<br>(/s/knowledge-base?article=24-1-pre-<br>installation-requirements-and-<br>instructions&language=en_US#install-<br>additional-kbs-windows).|
|Download<br>required<br>version of the<br>sensor<br>package|Work with Technical Support and your<br>Customer Success team to ensure you have<br>the correct sensor package in your<br>Cybereason platform environment.|


## Perform an upgrade

You can upgrade sensors to the latest version using:


The **Sensors** screen


A software distribution tool


Note


When you upgrade from a version that is no longer supported

to a supported version, you must perform an uninstall of the


older version and a new install of the newer supported version,

instead of a normal upgrade.


Cybereason recommends that you upgrade sensors gradually, in

batches. This reduces server and network load, and allows you to


better control the process.


Sensor packages are automatically downloaded and can be used


to upgrade your sensor via an improved scaled process. The

sensor checks for a new package every 10 minutes and


downloads a new package if one is found.


When you upgrade a sensor, the sensor installs the pre

downloaded package for upgrade to the latest sensor version. For

[more information, see Scaled Sensor Upgrade Process - FAQ](https://nest.cybereason.com/s/article/5522576)


[(/s/article/5522576).](https://nest.cybereason.com/s/article/5522576)

## Upgrade through the Sensors screen


1. In the **System > Sensors** screen, search for the sensors you


want to upgrade using the filter box or the Quick filters. For

example, you could search for all sensors that are Outdated.


Tip


To help you label machines to upgrade, you could add a


custom sensor tag and then filter by the sensor tag. For

[details on how to use sensor tags, see Sensor Tagging](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-tagging&language=en_US#sensor-tagging)


[(/s/knowledge-base?article=24-1-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-tagging&language=en_US#sensor-tagging)

[tagging&language=en_US#sensor-tagging).](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-tagging&language=en_US#sensor-tagging)


2. In the sensor list, select the sensors to upgrade. To select all


sensors in the results list, click the checkbox at the top of the


list.

3. Above the sensor list, click **Actions > Upgrade sensors** .


When the platform upgrades sensors, the platform silently

upgrades the sensor in the background of the machine without the


need for the machine user to perform any tasks.

## Upgrade with a software distribution tool


You can also upgrade sensors through the command line using a


software distribution tool. Use the commands below to help you

create a script to perform an automated upgrade process.


To install sensors, use these commands:

**Windows machines**


<installer file name> /install /quiet /norestart -l <LogFilePath> /v

"InstallFolder="C:MyInstallDirectory"" <installation parameter>=


<installation parameter value>


Note


You must have administrative privileges to run the installation

command.


**MacOS machines**

```
 sudo installer -pkg /<path-to
 package>/<file name>.pkg -target /

```

**Linux machines**


**On CentOS/RHEL/Oracle Linux/Amazon Linux:**


```
 sudo rpm -Uvh <new RPM file>

```

**On Ubuntu:**

```
 sudo dpkg -i <new deb file>

## Upgrade sensors with a software

## distribution tool with Sensor Tampering

## Protection enabled

```

If you have enabled Sensor Tampering Protection and enabled the

**Extended Tampering Protection with passkey** option, when you


upgrade your sensors with a software distribution tool, you will
need the passkey file to perform the upgrade.


**To upgrade the sensors, follow these steps**


1. In the **Sensors** screen, select the sensors you need to


upgrade.

2. In the **Actions** menu above the sensors list, select **Download**


**passkey file** .
3. On the pop-up message, click **Yes, create the file** .


The file is downloaded to your machine. The file is a .p7b
PKCS certificate file that enables the sensor driver to identify


each sensor to be removed by its unique sensor key (ID). You
can save the file in any location you wish (on a local machine


or on a network drive), as long as you have the path to the file.

4. Run the upgrade command using this syntax:

```
   <installer file name> /install /quiet

   /norestart AP_UNINSTALL_OFFLINE_FILE=

   <path_to_passkey_file>

```

The variables in the command above include:


**<file name>** is the name of the installer file used to install

the sensor. Verify that it is the same version as the sensor


you are uninstalling.

**/install** is the command to install the sensor.


**/quiet** (optional) is the command to not show any

prompts.


**<path_to_passkey_file>** is the path to the passkey file.


[For details on the passkey file, see Uninstall using an passkey file](https://nest.cybereason.com/s/knowledge-base?article=24-1-uninstall-sensors-for-windows&language=en_US#uninstall-using-an-passkey-file)


[(/s/knowledge-base?article=24-1-uninstall-sensors-for-](https://nest.cybereason.com/s/knowledge-base?article=24-1-uninstall-sensors-for-windows&language=en_US#uninstall-using-an-passkey-file)
[windows&language=en_US#uninstall-using-an-passkey-file). For](https://nest.cybereason.com/s/knowledge-base?article=24-1-uninstall-sensors-for-windows&language=en_US#uninstall-using-an-passkey-file)


[details on Sensor Tampering Protection, see Use Sensor](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-sensor-tampering-protection&language=en_US#use-sensor-tampering-protection)


[Tampering Protection (/s/knowledge-base?article=24-1-use-](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-sensor-tampering-protection&language=en_US#use-sensor-tampering-protection)


[sensor-tampering-protection&language=en_US#use-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-sensor-tampering-protection&language=en_US#use-sensor-tampering-protection)

[tampering-protection).](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-sensor-tampering-protection&language=en_US#use-sensor-tampering-protection)

## View the upgrade status


After you start the upgrade process, you can view the status in the

**Action log** area at the top right of the screen. See the status of


each sensor in the **Last update status** column.


Note


In an environment that has a large number of sensors,

updating all the sensors may take several days.


During the upgrade, sensors move through these states:






|State|Description|
|---|---|
|Pending|The upgrade is in the queue.|
|In progress|The upgrade has been initiated and is<br>progressing normally.|
|Succeeded|The upgrade is complete.|
|Failed|The upgrade has failed.|
|Aborted|The upgrade was canceled.|
|Already up to<br>date|An upgrade was attempted but the sensor is<br>already on the latest version.|



If necessary, you can cancel sensor upgrades for upgrades that

are in progress.


1. In the **System > Sensors**, click the **In progress** dropdown list


at the top right corner of the screen.


2. Beside the **Upgrade sensor** action, click **Abort** . The


Cybereason platform cancels the upgrade operation for all the


sensors in that upgrade batch.


If you have enabled the Scaled sensor upgrade feature, sensors


automatically download sensor packages that can be used to

upgrade your sensor via an improved scaled process.


## Upgrade in environments with a

When you upgrade sensors in an environment with a Registration


server, the sensor-to-Detection server pairing is maintained as
long as your configuration has not changed. Configuration


changes that can affect Detection server assignment include

updates to the Manage sites screen, sensor assignment via CSV,


or Detection server removal.


After an update to server settings, it is possible to configure the


sensor to skip the Registration process again. If you enable this
configuration, the sensor connects directly to the saved Detection


Server. Contact Technical Support to personalize your sensors
with the appropriate configuration.


If you remove a Detection server, the sensors that were previously

assigned to that server contact the Registration server and the


Registration server reassigns the sensors among the remaining

Detection servers. You must delete the Detection server from the


**Detection servers** screen to ensure that the Registration server

does not reassign sensors to that Detection server.

## - Known issues and limitations sensor


This section includes known issues and limitations for sensor

upgrades. Consult with Technical Support for assistance with


these issues.






|Limitation|Details|
|---|---|
|Sensor<br>downgrade<br>and<br>upgrade|If you uninstalled the sensor and then installed<br>a lower sensor version (downgrade), it is not<br>possible to subsequently upgrade to the<br>original version (the uninstalled version) via the<br>UI.<br>For example:<br>1. Install 18.1.0.0.<br>2. Uninstall 18.1.0.0.<br>3. Install 17.5.0.0.<br>4. Attempt to upgrade to 18.1.0.0 via the UI.<br>The upgrade action does not complete<br>successfully.|


|Limitation|Details|
|---|---|
|Windows<br>Boot<br>Initialization<br>policy|After you upgrade your sensors, if you set the<br>Windows Boot Start Initialization Policy to**Good**<br>**only**, Cybereason may not recognize some<br>drivers that were loaded during machine startup<br>and returns an Unknown classifcation.<br>Cybereason recommends using the default<br>policy setting,**Good and unknown**.<br>For more information see, Sensor Upgrade -<br>Known Limitation and Cybereason<br>Recommendation (/s/article/2639629).|
|Scaled<br>sensor<br>upgrades|To use the scaled sensor upgrade process,<br>you must use one way SSL for sensor<br>communication. Two way SSL causes the<br>scaled sensor upgrade process to fail.<br>The scaled sensor upgrade process relies<br>on the CMS2probe infrastructure which is<br>preconfgured for environments built after<br>July 1st 2022.<br>The scaled sensor upgrade process relies<br>on the Endpoint Management Channel<br>infrastructure. The Endpoint Management<br>Channel infrastructure relies on a new set of<br>DNS connections, please ensure your<br>environment allows the connection of these<br>3 DNS addresses. For more information,<br>see Enable Communication with<br>Cybereason Servers (/s/knowledge-base?<br>article=24-1-enable-communication-with-<br>cybereason-<br>servers&language=en_US#enable-<br>communication-with-cybereason-servers).|







