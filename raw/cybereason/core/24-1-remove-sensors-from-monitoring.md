**Archived:** The sensor has been stale for an extended period


of time and is now archived.

**Decommissioned:** The sensor has been archived for an


extended period of time and is no longer connected to the

Cybereason platform in any way. As part of being


decommissioned, the Cybereason platform tries to uninstall or

remove the sensor on the endpoint machine for Windows


machines or removes the sensors from the platform (for Mac

and Linux sensors)


**Deleted:** The sensor has permanently been removed from the

Cybereason platform.


If an archived sensor reconnects, the sensor state automatically

reverts to **Online** . If a decommissioned sensor reconnects to the


platform, you can restore the sensor.

## Why are these states important?


It is important for analysts to understand which machines are


actively collecting data and have been offline for long periods of

time. If a sensor has disconnected for a long time, the Cybereason


platform may not have all relevant data as part of the investigation

of a MalOp. Being able to quickly identify such sensors can help


you determine which machines are no longer relevant, or if you

need to investigate the machine before continuing the attack


investigation.


As an administrator, it is important to identity sensors that have


been disconnected for periods, so that you can attempt to bring

them online, or alternatively, archive or decommission them so that


the Cybereason platform does not list the sensor with the active
sensors. Archiving or decommissioning sensors clarifies the actual


set of active sensors, helping you focus their attention on active

sensors only.

## Archive or unarchive a sensor


Sensors can be archived automatically or manually.


Auto-archive of sensors occurs after the sensor has been stale for


a set period of time. Automatic unarchiving of sensors occurs if an

archived sensor comes online and reconnects to the Cybereason


platform.


You may decide to manually archive sensors if, for example, you


are aware that a machine is out of use or you want to remove the

sensor even earlier from the list of active sensors. You can archive


offline or stale sensors, but not online sensors. Likewise, you can

manually unarchive a sensor.


Note


Archiving does not uninstall the sensor. You must still go to the


machine and follow the standard uninstall process to fully

uninstall the sensor, or decommission the sensor to trigger the


uninstall flow (on Windows machines only).


**To manually archive a sensor, follow these steps:**


1. In the **System > Sensors** screen, from the sensor list, select


the sensors you want to archive.


2. Above the sensors list, click **Actions** and select **Archive**


**sensors** .


3. In the dialog box, add a reason for archiving (optional) and


click **Yes, archive** .


The Cybereason platform moves the selected sensors to the

**Archive** list.


**To manually unarchive a sensor, follow these steps:**


1. In the **System > Sensors** screen, in the **Archive** screen,


select the sensors you want to unarchive.

2. Above the sensor list, click **Actions** and select **Unarchive**


**sensors** .

3. In the dialog box, add a reason for unarchiving (optional) and


click **Yes, unarchive** .


Note


Once a sensor has been manually unarchived, it will not be

auto-archived again. The only way to archive it again is to


manually archive it.

## Manage settings for stale, archived, and


You can set when sensors become automatically stale, archived,


decommissioned or deleted sensors in the **Settings > Stale &**

**archived sensors** screen.


In this screen, you enable automatic archive, decommission, or
deletion of sensors, and configure the timing of the automatic


transition for when sensors are set as stale, archived,

decommissioned, or deleted. You can also set email notifications


for stale and archived sensors.


**To configure the timing of automatic transitions, follow these**


**steps:**


1. In the **Settings > Stale and archived sensors** screen, in the


**Timing** section, as needed, set the toggles for **Enable auto-**

**archive**, **Enable auto-decommission**, or **Enable auto-delete**


to **On** .


2. Still in the **Timing** section, in the **Mark sensors** edit field,


enter the number of days after which the Cybereason platform

sets the sensors as stale, archives the sensors,


decommissions the sensors, or deletes the sensors.


For example, if you set:


Mark sensors as stale after 30 days

Archive stale sensors after 60 days


Then, after 30 days of being offline, a sensor is set to stale.

After 60 days of being stale, a sensor is archived (meaning


after 90 days (30 + 60) of being offline).
3. In the **Email Notifications** section, set the **Enable**


**notifications** toggle to **On** for each type of operation about
which you want to receive notifications.


If you enable notifications, users with the System Admin role
will receive email notifications about stale or archived sensors.


Note


Email notifications related to stale/archived sensors are


managed separately from other email notification
preferences. If **Enable email notifications** is set to **On**,


appropriate users will receive the email even if the **Enable**
**notification** checkbox is not selected for their user in the


**Users** screen.


From this email, system and sensor administrators can click a


link to configure stale and archived sensor settings or click a

link to see an updated list of stale and archived sensors.


Note


Administrators can receive a daily email notification including


an archived sensors report. This report is sent even thwne

there are no stale or archived sensors on endpoints to which


the relevant policy is applied. In this case, the email states that

0 sensors are archived.


Note


[This feature is not enabled by default. Open a Technical](https://nest.cybereason.com/s/support)


[Support (/s/support) case to enable this feature in your](https://nest.cybereason.com/s/support)

environment.


If you have a sensor that you no longer need to monitor or


manage, but you cannot reach the machine to uninstall the sensor,

you can decommission the sensor.


**To decommission a sensor, follow these steps:**


1. In the **System > Sensors** screen, select the sensors you want


to decommission.

2. Above the sensor list, click **Actions** and select


**Decommission** . The Decommission Sensors dialog box is

displayed.


3. Select **Decommission** .


Once the sensor is decommissioned, it is no longer visible in the


sensor list. In addition, the Cybereason platform tries daily

(between 12 am and 5 am UTC) to uninstall the sensor from


Windows machines if the endpoint machine is online and

connected to the Cybereason platform. For sensors on Mac and


Linux machines, the platform removes the sensor from the

platform.


Once the Cybereason platform successfully uninstalled or

removed the sensors, the sensor is deleted from the platform and


cannot be restored in any way. If you want to restore this sensor

later, you must reinstall the sensor and restore the sensor from the


**Decommissioned sensors** list.


Because these sensors are removed from active communication


with the Cybereason platform you may see the status of **None** for

the **Last update status** column or **Uninstalled** when the sensor is


successfully uninstalled.


**To restore a sensor that was decommissioned, follow these**


**steps:**


1. In the **System > Sensors** screen, select the


**Decommissioned sensors** link on the right hand side of the

screen.


2. In the **Decommissioned sensors** screen, select the sensors


you want to restore.

3. Click **Actions** and select **Restore Sensors** .

## Identify stale and archived sensors


You can quickly identify the sensor connection state by its icon in

the **System > Sensors** screen:






|Sensor Status|Icon|Description|
|---|---|---|
|Online||The sensor is connected to the<br>Detection server.|
|Offine||The sensor is not connected to the<br>Detection server.|
|Stale||The sensor has been<br>disconnected from the Detection<br>server for an extended period of<br>time.|
|Archived||The sensor is disconnected from<br>the Detection server and has been<br>archived.|
|Decommissioned||The sensor has been<br>decommissioned, removed from<br>any connection with the<br>Cybereason platform or<br>uninstalled, and scheduled for<br>deletion.|


## View and manage stale, archived, and

The Cybereason platform displays stale sensors in the main list of


active sensors. The Cybereason platform displays archived

sensors in a separate screen, although they are still counted in the


**Assigned sensors** column for sensor policies.


To view stale sensors, in the **Quick filters** area of the **System >**


**Sensors** screen, select **Stale** . Stale sensors are displayed in the

results list:


To view archived sensors, click **Archive** in the top right of the


**System > Sensors** screen. The Cybereason platform displays a

list of archived sensors:


To view decommissioned sensors, click **Decommissioned**

**sensors** in the top right side of the **System > Sensors** screen.


The Cybereason platform displays the list of decommissioned

sensors scheduled for uninstall/removal and deletion. Because


these sensors are removed from active communication with the

Cybereason platform you may see the status of **None** for the **Last**


**update status** column or **Uninstall initiated** when the sensor is

successfully uninstalled.


Verify on the machine to confirm that the uninstallation has

completed.


For an archived sensor, you can perform a limited set of actions

from the **Actions** menu:


Investigate sensors
Export the archived sensors list to a CSV file


Unarchive or restore sensors

Decommission sensors
