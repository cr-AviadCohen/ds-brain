The exported CSV file is exported in UFT-8 format. If your


environment is in Japanese, ensure you open the CSV file with
a BOM to ensure the data in the CSV file displays correctly.

## Sensor metadata columns


The sensors CSV file is organized as a table. Each row represents
an individual sensor and each column represents configuration


information about each sensor. The same metadata is also

displayed in the columns of **System > Sensors** screen.


The table below describes each metadata column.


Note


There are small differences between how data is displayed in

the UI and in the CSV (for example, CPU usage is displayed


as a percentage in the UI and as a decimal value in the CSV).
The example values in the table below reflect the CSV display.
















|Field|Description|Example valu|
|---|---|---|
|Sensor ID|Concatenation of the Detection<br>server ID and sensor PylumID|5b472a712d0e<br>PYLUMCLIENT<br>1988-35CF-01|
|PylumID|Sensor identifer|PYLUMCLIENT<br>1988-35CF-01|
|GUID|GUID of the sensor|761fdb262d7e|
|FQDN|Fully qualifed domain name of the<br>machine|cyber.cyber.lo|
|Machine<br>name|Name of the machine|cyber|
|Internal IP<br>address|IP address of the machine as it<br>appears to the internal network|123.45.67.89|
|External IP<br>address|External IP address of the machine<br>as it appears across the internet|123.45.67.89|
|Firewall<br>control|The Personal frewall control<br>(/s/knowledge-base?article=24-1-<br>personal-frewall-<br>control&language=en_US#personal-<br>frewall-control) modes|Advanced|


|Field|Description|Example valu|
|---|---|---|
|Site|Site name as defned in the<br>**Detection Servers** screen|Default|
|Site ID|The ID of the site the sensor is<br>assigned to, if you are using<br>Registration servers and have sites<br>set up.|0|
|Anti-<br>Ransomware<br>mode|The Anti-Ransomware mode|Disabled|
|App Control<br>mode|App Control mode|Not installed|
|Isolated|If the machine is isolated. Values are:<br>TRUE<br>FALSE|FALSE|
|Last seen|The last time the sensor connected to<br>the server before disconnecting.<br>This CSV feld corresponds to the<br>**Last seen** column in the<br>**Sensors** screen. However, the<br>**Last seen** column in the<br>**Sensors** screen is populated<br>only for sensors that are currently<br>**Offine**.<br>This CSV feld may differ from the<br>**Last pylumID message update**<br>**time** if the sensor is currently<br>online but was disconnected in<br>the past. This is because the<br>**Last seen** value is only updated<br>when a sensor disconnects.|16/12/2019 09|
|Last pylumID<br>message<br>update time|The last time the sensor<br>communicated with the server.|16/12/2019 09|
||||


|Field|Description|Example valu|
|---|---|---|
|Sensor status|Connection state for the sensor.<br>Values are:<br>**Online:** The sensor is connected<br>to the Detection server.<br>**Offine:** The sensor is not<br>connected to the Detection<br>server.<br>**Stale:** The sensor has been<br>disconnected from the Detection<br>server for an extended period of<br>time.<br>**Archived:** The sensor is<br>disconnected from the Detection<br>server and has been archived.|Online|
|Service status|Main Cybereason service activity.<br>Values are:<br>**Up:** The main service is running<br>on the endpoint.<br>**Down:** The main service is<br>inactive.<br>Note: Service status is always**Down**<br>when sensor status is**Offine**.|Up|
|Last status<br>action|The last manual action. Values are:<br>Archive<br>Unarchive|None|
|Archived or<br>unarchived<br>comment|The comment entered during the last<br>archive/unarchive action|Archiving sens|
|Sensor<br>archived by<br>user|The user who performed the last<br>archive/unarchive action|admin|
|Server name|The Detection server name|t1|
|Server ID|The Detection server ID|5b472a712d0e|
|Server IP|The Detection server IP|987.65.43.21|
|OS|The OS of the machine|Linux|
|OS version|The OS version of the machine|CentOS Linux|
||||


|Field|Description|Example valu|
|---|---|---|
|Data<br>collection|Collection state of the sensor. Values<br>are:<br>**Enabled:** The sensor actively<br>collects data and transmits it to<br>the server.<br>**Suspended:** The sensor has<br>shut down automatically and has<br>stopped collecting data for a<br>period of time.<br>**Disabled:** The sensor's data<br>collection has been disabled.<br>**Advanced:** Data collection is<br>enabled and an advanced<br>collection is enabled (e.g. DPI,<br>non-exe fle collection)|Enabled|
|Sensor<br>version|Version of the Cybereason sensor|23.2.23|
|Console<br>version|Version of the console used by your<br>Cybereason platform servers|18|
|First seen|The frst time the sensor went online|47:52.0|
|Uptime|Amount of time since the sensor has<br>been started/restarted|20d 16:15:28|
|CPU usage|The average CPU usage of the<br>sensor in the last minute. The number<br>displayed is the global CPU usage<br>on the machine across all cores.|0.008333194|
|Memory<br>usage|The memory usage in bytes|48537600|
|Outdated|Is the sensor version outdated?<br>Values are:<br>TRUE<br>FALSE|FALSE|
|Signatures<br>mode state|The**Anti-Malware > Signatures**<br>mode|Disabled|
|Signatures<br>mode origin|The source of the**Anti-Malware >**<br>**Signatures** mode|Set by Policy|
|Last<br>Signatures<br>update|The last time the**Anti-Malware >**<br>**Signatures** database was updated|16/12/2019 09|
||||


|Field|Description|Example valu|
|---|---|---|
|Signatures DB<br>Version|The version number of the**Anti-**<br>**Malware > Signatures** database|80094|
|PowerShell<br>mode|The Fileless protection mode|Disabled|
|Remote Shell<br>Status|The status of the Remote Shell<br>feature. Values are:<br>Disabled<br>Enabled|Disabled|
|Anti-Malware<br>mode|The Anti-Malware mode|Disabled|
|Anti-Malware<br>mode origin|The source of the Anti-Malware mode|Set by Policy|
|Last full scan|The last time a full scan was<br>performed on the machine. Values<br>are:<br>Date and time of the last full<br>scan.<br>**In progress** if a full scan is in<br>progress.<br>**Not performed** if a full scan was<br>not yet performed.|16/12/2019 09|
|Last quick<br>scan|The last time a quick scan was<br>performed on the machine. Values<br>are:<br>Date and time of the last quick<br>scan.<br>**In progress** if a quick scan is in<br>progress.<br>**Not performed** if a quick scan<br>was not yet performed.|16/12/2019 09|
|Organization|The organization name|Internal|
|Proxy address|The proxy address if there is a proxy|192.168.1.100|
|Last<br>prevention<br>error|The last prevention error|null|
|Last exit<br>reason|The last sensor failure status|Stop request r|
||||


|Field|Description|Example valu|
|---|---|---|
|Actions in<br>progress|Number of actions sent to sensor that<br>are in progress or pending|0|
|Pending<br>actions|A list of the pending actions|null|
|Last upgrade<br>result|The status of the last sensor<br>upgrade. Values are:<br>None<br>InProgress<br>Succeeded<br>AlreadyUpdated|AlreadyUpdate|
|Department|Department associated with the<br>sensor|IT|
|Device control|The Device control (/s/knowledge-<br>base?article=24-1-device-<br>control&language=en_US#device-<br>control) modes|Disabled|
|Location|A user-defned string representing<br>the geographic or organizational<br>location of the device the sensor is<br>installed on.|UK|
|Critical Asset|Notes whether or not the sensor is<br>considered a critical asset. Values<br>are:<br>**TRUE:** sensor is considered a<br>critical asset.<br>**FALSE:** sensor is not considered<br>a critical asset.|TRUE|
|Device Type|User-defned string representing the<br>type of device the sensor is installed<br>on.|Server|
|Exploit<br>protection<br>mode|The Exploit protection (/s/knowledge-<br>base?article=24-1-exploit-<br>protection&language=en_US#exploit-<br>protection) mode|Enabled|
|Custom tags|Tags associated with the sensor|demo-sensor|
|AI detect<br>mode|The**Anti-Malware > Artifcial**<br>**intelligence Detect** mode|Aggressive|
||||


|Field|Description|Example valu|
|---|---|---|
|AI detect<br>mode origin|The source of the**Anti-Malware >**<br>**Artifcial Intelligence Detect** mode|Set by Policy|
|AI prevent<br>mode|The**Anti-Malware > Artifcial**<br>**Intelligence Prevent** mode|Aggressive|
|AI prevent<br>mode origin|The source of the**Anti-Malware >**<br>**Artifcial Intelligence Prevent** mode|Set by Policy|
|Assigned<br>Policy|Name of the policy assigned to the<br>sensor. Value will be**Default** if<br>assigned to the Default policy, and<br>**Legacy** for sensors not upgraded to<br>19.1+|Default|
|Policy ID|Policy ID for the sensor's assigned<br>policy.|e8394fd922sd|
|Policy Last<br>Update|Values are:<br>Date and time of the last time a<br>user modifed the policy.<br>Empty if no policy is assigned to<br>the sensor.|16/12/2019 09|
|Compliance|Notes whether or not the sensor is<br>compliant with its assigned policy.<br>Values are:<br>TRUE - The sensor's security<br>settings match those of its<br>assigned policy (i.e. does not<br>contain additional overrides).<br>FALSE - The sensor's security<br>settings are different than those<br>specifed in its assigned policy<br>(for example, a sensor whose<br>Anti-Malware settings was<br>overridden using the**Sensors**<br>screen).|TRUE|
|Deleted by|The Cybereason user that removed<br>the sensor from the**Sensors** screen|user@myserve<br>(mailto:user%4|
|Deleted date|The date someone removed the<br>sensor from the**Sensors** screen.|16/12/2019 09|
|Document<br>protection<br>status|The status of the Document<br>protection mode||
||||


|Field|Description|Example valu|
|---|---|---|
|Document<br>protection<br>mode|The current mode set for Behavioral<br>Document protection|ENABLED|
|Organizational<br>Unit|The unit in the organization to which<br>machine on which the sensor is<br>installed belongs||
|Group name|The name of the group to which the<br>sensor belongs (if you enabled<br>sensor grouping in your environment)|Unassigned|
|Serial number|The serial number of the macOS<br>machine on which the sensor is<br>installed|C02FC160MD|
|Device model|The model of the device for the<br>macOS machine on which the sensor<br>is installed|MacBookPro1|
|Group<br>assignment|The method of assignment for the<br>sensor to the sensor group. Possible<br>values include:<br>Dynamic<br>Manual|Dynamic|
|BEP mode|The mode set for Behavioral<br>Execution Prevention. Possible<br>values include:<br>Disabled<br>Detect<br>Prevent|Disabled|
|VPP mode|The mode set for Variant Payload<br>Protection. Possible values include:<br>Disabled<br>Detect<br>Prevent|Disabled|
|Variant fle<br>prevention<br>mode|The mode set for Variant File<br>Protection. Possible values include:<br>Disabled<br>Detect<br>Prevent|Disabled|
|Unique<br>sensor key|In versions 23.2.148 and later, the<br>unique key generated for the sensor<br>to uninstall the sensor.||
||||



