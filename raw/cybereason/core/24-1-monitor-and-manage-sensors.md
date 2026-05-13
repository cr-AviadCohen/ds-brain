The **Sensors by OS Version** section lists the five OS versions


with the most sensors. Therefore, the total number of sensors

listed in the **Sensors by OS Version** section may not equal


the total number of sensors in the environment.

## View sensor coverage


The Asset Discovery (AD) scanner widget in the **System >**


**Dashboard** shows what percentage of domain assets are

protected by Cybereason sensors. The **Export CSV** option


produces a CSV file that lists unprotected endpoints that do not

have Cybereason sensors installed.


In the **System > Sensors** screen, the Cybereason platform

displays all your organization's sensors in a list, allowing you to


better manage large deployments.


**Legacy screen:**


**Versions 23.2.89 and later:**


Note


This new version of the **Sensors** screen is not generally


available. Contact your Customer Success Manager to gain

access to this version of the screen.


Use the common quick filters to quickly filter the list of sensors:


**Legacy screen (in the Quick filters area):**


**Versions 23.2.89 and later:**


If the common filters are not suitable, enter filter criteria in the
search box. As you type, matching filters are displayed, including


smart search capabilities. To learn more about how to use the

[smart search capabilities, see Apply search options for Features](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#apply-search-options-for-features)


[(/s/knowledge-base?article=24-1-build-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#apply-search-options-for-features)

[query&language=en_US#apply-search-options-for-features).](https://nest.cybereason.com/s/knowledge-base?article=24-1-build-a-query&language=en_US#apply-search-options-for-features)


**Legacy screen:**


**Versions 23.2.89 and later:**


If needed, you can select the Detection server or site from the


dropdown list in the top left corner. For deployments with over 10
Detection servers, you can search for a specific Detection server


by entering its name into the search box.


**Legacy screen:**


**Versions 23.2.89 and later:**


When you select a filter or a server name, the Cybereason


platform refreshes the sensor list to display the sensors that match
the selected filters. Offline sensors display as gray in the results


list.


To view different settings and details for any sensor in the list, click


**Columns** . The following columns are available:






|Column|Description|
|---|---|
|Actions|Number of actions sent to sensor that are in<br>progress or pending|
|AI Detect<br>mode|The current**Anti-Malware > Artifcial**<br>**Intelligence Detect** mode|
|AI Detect<br>mode origin|The source of the current**Anti-Malware >**<br>**Artifcial Intelligence Detect** mode|


|Column|Description|
|---|---|
|AI Prevent<br>mode|The current**Anti-Malware > Artifcial**<br>**Intelligence Prevent** mode|
|AI Prevent<br>mode origin|The source of the current**Anti-Malware >**<br>**Artifcial Intelligence Prevent** mode|
|Anti-Malware<br>mode|The current Anti-Malware mode|
|Anti-Malware<br>mode origin|The source of the current Anti-Malware<br>mode|
|Anti-<br>Ransomware<br>(ARW/PRP)<br>mode|The current Anti-Ransomware mode|
|App Control<br>mode|The current App Control mode|
|Assigned<br>policy|Name of the policy assigned to the sensor.<br>Value will be**Default** if assigned to the<br>Default policy and**Legacy** for sensors not<br>upgraded to 19.1+|
|Behavioral doc<br>mode|The current mode for theb Behavioral<br>Document Protection feature|
|Behavioral doc<br>sensitivity|The current sensitivity level of the Behavioral<br>Document Protection feature|
|BEP mode|The current mode for the Behavioral<br>Execution Prevention feature|
|CPU usage|The average CPU usage of the sensor in the<br>last minute. The number displayed is the<br>global CPU usage on the machine across all<br>cores.|
|Critical asset|Whether or not the sensor is considered a<br>critical asset. Values are:<br>**TRUE:** Th sensor is considered a critical<br>asset.<br>**FALSE:** The sensor is not considered a<br>critical asset.|
|Custom tags|Tags associated with the sensor|


|Column|Description|
|---|---|
|Data collection|Collection state of the sensor. Values are:<br>**Enabled:** The sensor collects data and<br>transmits it to the server.<br>**Suspended:** The sensor has shut down<br>automatically and has stopped<br>collecting data for a period of time.<br>**Disabled:** The sensor data collection<br>has been disabled.<br>**Advanced:** Data collection is enabled<br>and an advanced collection is enabled<br>(e.g. non-exe fle collection)|
|Department|Department associated with the sensor|
|Detection<br>server|The name of the Detection server the sensor<br>communicates with|
|Device control|The current Device Control mode set in the<br>Endpoint Controls section of the sensor<br>policy|
|Device model|The model of the device hosting the sensor|
|Device type|User-defned string representing the type of<br>device hosting the sensor|
|Exploit<br>protection<br>modes|The current Exploit Protection mode|
|External IP<br>address|External IP address of the machine as it<br>appears across the internet|
|Fileless<br>Protection<br>mode|The current Fileless Protection modle|
|Firewall control|The current Personal Firewall Control mode<br>set in the Endpoint Controls section of the<br>sensor policy|
|First seen|The frst time the sensor went online|
|FQDN|Fully qualifed domain name of the machine|


|Column|Description|
|---|---|
|Group<br>assignment|Indicates whether a specifc sensor was<br>added to a group by assignment logic<br>(**Dynamic**) or manually (**Manual**).<br>When a user removes a sensor from a<br>group, the sensor's Group Assignment value<br>will become**Dynamic** if it was previously<br>**Manual**.|
|Group name|Name of the group to which the sensor is<br>assigned|
|Installation key|The unique ID of the sensor that is<br>generated upon installation (available in<br>version 23.1.15x and later)|
|Internal IP<br>address|IP address of the machine as it appears to<br>the internal network|
|Isolated|Whether or not the machine is currently<br>isolated|
|Last exit<br>reason|The last sensor failure status|
|Last full scan|The last time a full scan was performed on<br>the machine. Values are:<br>Date and time of the last full scan.<br>**In progress** if a full scan is in progress.<br>**Not performed** if a full scan was not yet<br>performed.|
|Last<br>prevention<br>error|The last prevention error|
|Last quick<br>scan|Status of the last quick scan performed on<br>the machine. Values are:<br>Date and time of the last quick scan.<br>_In progress*_ if a quick scan is in<br>progress.<br>**Not performed** if a quick scan was not<br>yet performed.|
|Last seen|The last time the sensor connected to the<br>Cybereason platform before disconnecting.<br>This column is populated only for sensors<br>that are currently offine.|


|Column|Description|
|---|---|
|Last<br>signatures<br>update|The last time the**Anti-Malware >**<br>**Signatures** database was updated. If there<br>is a signatures mode error, the error is<br>displayed in this column. See Signatures<br>mode error messages (/s/article/2929629)<br>for more details.|
|Last update<br>status|The status of the last sensor upgrade. For a<br>list of possible values, see Monitor Upgrade<br>Process (/s/knowledge-base?article=24-1-<br>monitor-upgrade-<br>process&language=en_US#monitor-<br>upgrade-process)|
|Location|A user-defned string representing the<br>geographic or organizational location of the<br>device hosting the sensor|
|Memory usage|The memory usage in bytes|
|Organization|The organization name|
|Organizational<br>Unit (OU)|Organizational unit as defned in the Active<br>Directory for Windows machines|
|OS|OS of the machine hosting the sensor|
|OS version|OS version of the machine hosting the<br>sensor|
|Outdated|Whether or not the sensor version is<br>outdated. A sensor is considered outdated if<br>its version number is lower (older) than the<br>highest (newest) version available to<br>download from the**System** screen. Values<br>are:<br>TRUE<br>FALSE|
|Policy<br>compliance|Whether or not the sensor's settings comply<br>with the assigned policy. This value will be<br>FALSE if the sensor's security settings are<br>different than those specifed in its assigned<br>policy (for example, a sensor whose Anti-<br>Malware settings was overridden using an<br>action in the**Sensors** screen).|
|Policy ID|Policy ID for the sensor's assigned policy.|


|Column|Description|
|---|---|
|Policy Last<br>update|Timestamp of when a user last modifed the<br>policy|
|Proxy address|The proxy address if one is used|
|Remote Shell<br>mode|Whether or not the Remote Shell feature is<br>enabled|
|Sensor status|Connection state for the sensor. Values are:<br>**Online:** The sensor is connected to the<br>Detection server.<br>**Offine:** The sensor is not connected to<br>the Detection server.<br>**Stale:** The sensor has been<br>disconnected from the Detection server<br>for an extended period of time.<br>**Archived:** The sensor is disconnected<br>from the Detection server and has been<br>archived.|
|Sensor version|Version of the Cybereason sensor|
|Serial number|Serial number for the device hosting the<br>sensor|
|Service status|Main Cybereason service activity. Values<br>are:<br>**Up:** The main service is running on the<br>endpoint.<br>**Down:** The main service is inactive.<br>The Service status is always**Down** when<br>sensor status is**Offine**.|
|Signatures DB<br>version|Version of the signatures database in use|
|Signatures<br>mode current<br>state|The current**Anti-Malware > Signatures**<br>mode|
|Signatures<br>mode origin|The source of the current**Anti-Malware >**<br>**Signatures** mode|
|Site|Site name as defned in the**Detection**<br>**Servers** screen|
|Uptime|Amount of time since the sensor has been<br>started/restarted|


|Column|Description|
|---|---|
|Variant File<br>Prevention<br>mode|The current mode for the Variant File<br>Prevention feature|
|VPP mode|The current mode for the Variant Payload<br>Protection feature|


Note


Sensors may automatically change state as the result of a


system crash or some other unplanned event. If such an event

[happens, see Sensor Error Handling (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-error-handling&language=en_US#sensor-error-handling)


[article=24-1-sensor-error-handling&language=en_US#sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-error-handling&language=en_US#sensor-error-handling)

[error-handling) for more details.](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-error-handling&language=en_US#sensor-error-handling)

## Perform actions on sensors


You can update settings or perform actions for a single sensors or

batches of sensors from the **System > Sensors** screen. The


following actions are supported by the Cybereason platform:


Note


Any security setting changes made from the **System >**

**Sensors** screen take precedence over the settings in a


sensor's assigned policy.














|Action|Description|
|---|---|
|Upgrade<br>sensors|Upgrade the sensor(s) to the latest software<br>version.|
|Restart|Restart the sensor on the endpoint.|
|Fetch sensor<br>log|Download the sensor log fles. Note:<br>Fetching logs is supported for up to 10<br>sensors at a time.|
|Set policy|Assign a sensor security policy to the<br>selected sensors.|


|Action|Description|
|---|---|
|Set collection<br>modes|Set collection modes (/s/knowledge-base?<br>article=24-1-endpoint-data-<br>collection#enable-or-disable-collections) on<br>the endpoint.<br>This action is being deprecated and will<br>eventually no longer be available.|
|Set Remote<br>Shell mode|Set the mode of Remote Shell on the<br>endpoint. See Remote Shell (/s/knowledge-<br>base?article=24-1-respond-to-threats-on-a-<br>machine-with-remote-shell) for more details.|
|Set App Control<br>mode|Set the mode of Application Control on the<br>endpoint. If set here, this value takes<br>precedence over the App Control mode<br>setting in the sensor's associated sensor<br>policy.<br>Note<br>This action is being deprecated and will<br>eventually no longer be available.|
|Set Anti-<br>Ransomware<br>mode|Set the mode of Anti-Ransomware<br>(/s/knowledge-base?article=24-1-set-the-<br>canary-fle-based-anti-ransomware-<br>modes#set-the-canary-fle-based-anti-<br>ransomware-modes) on the endpoint. If set<br>here, this value takes precedence over the<br>Anti-Ransomware mode setting in the<br>sensor's associated sensor policy.<br>This action is being deprecated and will<br>eventually no longer be available.|
|Set PowerShell<br>mode|Set the mode of Fileless protection<br>(/s/knowledge-base?article=24-1-set-the-<br>fleless-protection-modes) on the endpoint.<br>If set here, this value takes precedence<br>over the PowerShell protection mode setting<br>in the sensor's associated sensor policy.<br>This action is being deprecated and will<br>eventually no longer be available.|


|Action|Description|
|---|---|
|Set Anti-<br>Malware mode|Set the mode of Anti-Malware<br>(/s/knowledge-base?article=24-1-set-the-<br>anti-malware-modes) on the endpoint. If set<br>here, this value takes precedence over the<br>Anti-Malware mode settings in the sensor's<br>associated sensor policy.<br>This action is being deprecated and will<br>eventually no longer be available.|
|Start system<br>scan|Start a full or quick Anti-malware ><br>Signatures scan on the endpoint. Local<br>drives are scanned, not network drives. You<br>can view the last time a scan was<br>completed in the 'Last quick scan' and 'Last<br>full scan' columns of this screen. Note that a<br>full scan may cause higher CPU usage than<br>usual.|
|Stop system<br>scan|Stop a scan that is in progress on the<br>endpoint.|
|Investigate|Investigate the machine in the Investigation<br>screen.|
|Export to CSV|Export the sensor confguration to a CSV<br>fle. This exports the confguration of all the<br>sensors in the results list using the current<br>flter (except for archived sensors). See<br>Export Sensor Metadata (/s/knowledge-<br>base?article=24-1-export-sensor-metadata)<br>for details on the contents of the CSV.|
|Import sensor<br>tags CSV|Import sensor tags from a CSV fle. See<br>Sensor Tagging (/s/knowledge-base?<br>article=24-1-sensor-tagging) for more<br>information.|
|Archive or<br>decommission<br>sensors|Archive or decommission (/s/knowledge-<br>base?article=24-1-remove-sensors-from-<br>monitoring) the sensors. The sensors are<br>moved to the Archived sensors screen and<br>do not appear in the active sensors list.|
|Add to group|Add selected sensors to a specifc sensor<br>group. Manual group assignment excludes<br>the sensor from sensor grouping logic, even<br>if the sensor's metadata changes.|


|Action|Description|
|---|---|
|Remove from<br>group|Remove the selected sensors from their<br>current group. Sensors will automatically be<br>assigned the 'Unassigned' group. Any<br>'Manual' 'Group Assignment' values will<br>change to 'Dynamic'.|
|Delete sensor|Disconnect the sensor from the<br>environment. Once the sensor is deleted<br>from a machine, it is no longer visible in the<br>UI. However, the sensor remains connected<br>to the Detection server and collects and<br>sends data for three days. See Uninstall<br>Sensors for Windows (/s/knowledge-base?<br>article=24-1-uninstall-sensors-for-windows)<br>for more information.|
|Create uninstall<br>fle|Create an uninstall fle for the selected<br>sensors. See Uninstall Sensors for Windows<br>(/s/knowledge-base?article=24-1-uninstall-<br>sensors-for-windows) for more information.|


Note





Some actions are supported for specific operating systems

[only. For details, see Supported Features by Operating System](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system)


[(/s/knowledge-base?article=24-1-supported-features-by-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system)

[operating-system).](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system)


**To perform actions on sensors, follow these steps:**


1. In the **Sensors** screen, select the sensors to update.


To select all sensors in the results list, click the checkbox at

the top of the list. This selects **all** the sensors in the results,


not only the first 500 that are displayed.

2. Above the sensor list, click **Actions** .


3. Select the action you want to perform from the dropdown list.


You can also use the API for sensor management actions. For

[details, see the Sensor Management API Reference](https://nest.cybereason.com/s/knowledge-base?article=sensor-api-token-manage-sensors)


[(/s/knowledge-base?article=sensor-api-token-manage-sensors).](https://nest.cybereason.com/s/knowledge-base?article=sensor-api-token-manage-sensors)

## Abort a sensor action


If you need to stop an action, in the upper right corner of the


**Sensors** screen, click the **Action log/In progress** dropdown,

click **Abort** . The Cybereason platform displays status **<number of**


**sensors> Aborted** is displayed when the abort succeeds.


If for some reason the request to abort a sensor action times out


(for example, due to a server connectivity issue) the Cybereason

platform displays the status '<number of sensors> Abort timeout'.


The default timeout period is one minute. To change this default,

contact Technical Support. Note that it may take up to one minute


after the timeout for the timeout status to be displayed.


## Queued actions for offline sensors

The Cybereason platform can queue many sensor management


and investigation actions for offline sensors. This enables

administrators and analysts to easily perform these actions without


being concerned with which sensors are currently online.


If the sensor on which the action is requested is not online, the


action enters pending status. By default, actions sent to offline

sensors are queued for 3 days. If, after 3 days, the sensor has not


come back online, the action is no longer queued and will not

execute if the sensor comes back online at a later time. Contact


Technical Support to increase this queue period.


The following actions are supported by the Cybereason platform


queued actions functionality:






|Action type|Items|
|---|---|
|**Sensor**<br>**management**|Update<br>Enable collection<br>Disable collection<br>Fetch sensor log<br>Install/Uninstall App Control<br>Set App Control mode<br>Set Anti-Ransomware mode<br>Set PowerShell mode<br>Set Anti-Malware mode|
|**Investigation**<br>**actions**|Isolate machines<br>Unisolate machines<br>Quarantine fles<br>Remove a registry entry<br>Kill and suspend processes<br>Unsuspend processes<br>Prevent fle execution with<br>Application Control|



Note that queuing is not necessary for these actions, which


happen immediately through the Cybereason platform server

infrastructure without having to communicate with the sensor:


Investigate

Export to CSV


Archive sensors

Unarchive sensors


[For more information, see Supported Capabilities for Offline](https://nest.cybereason.com/s/article/2444321)

[Sensors (/s/article/2444321).](https://nest.cybereason.com/s/article/2444321)


## Remove sensors from the Sensors

## screen

If you cannot reach the machine to uninstall the sensor directly,


you can use the **Sensors** screen to disconnect the sensor from

the environment.


**To disconnect a sensor from the environment follow these**

**steps** :


1. From the **System > Sensors** screen, select the sensor(s) you


want to remove.


Note


You can also delete sensors from the **Archived sensors**


screen.


2. Click **Actions > Delete Sensors** . The **Delete Sensors** dialog


box is displayed.


3. Select **Yes, delete** .


Once the sensor is removed, it is no longer visible in the **Sensors**


screen. However, the sensor remains connected to the Detection

server and collects and sends data for three days. Within 365


days, you can restore the sensor from the **Sensors > Deleted**

**sensors** screen.


**To restore a sensor that was removed, follow these steps** :


1. In the **Sensors** screen, click the **Deleted sensors** link on the


right-hand side of the screen.


2. In the **Deleted sensors** screen, select the sensor(s) you want


to revert.

3. Click **Actions > Revert Sensors** .


The selected sensor(s) are reverted and operational on the

machine from which they were removed.
