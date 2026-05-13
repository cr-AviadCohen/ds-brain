|State in<br>Cybereason<br>UI|State in Installer<br>File|Description|
|---|---|---|
|Enabled|ACTIVE_NORMAL|The sensor actively<br>collects data and<br>transmits it to the server.|
|Suspended|ACTIVE_DELAYED|The sensor has shut<br>down automatically and<br>has stopped collecting<br>data for a period of time.|
|Disabled|INACTIVE|The sensor's data<br>collection has been<br>disabled.|


|State in<br>Cybereason<br>UI|State in Installer<br>File|Description|
|---|---|---|
|Service error|N/A|The sensor is connected<br>to the Cybereason<br>servers, however, due to<br>an error, collection<br>capabilities are affected.<br>To identify sensors that<br>are experiencing a<br>service error:<br>1. In the**System >**<br>**Sensors** screen,<br>click**Columns** and<br>add the**Service**<br>**status** column and<br>the**Sensor status**<br>column.<br>2. In the search box,<br>search for sensors<br>with a**Sensor**<br>**status** of**Online**<br>and a**Service**<br>**Status** of**Down**.<br>The sensors that are<br>visible in the search<br>results are experiencing<br>a service error. The<br>number of sensors in the<br>search results should<br>match the number of<br>sensors displayed next<br>to**Service error** in the<br>**System > Overview**<br>screen.<br>Sensors with a**Service**<br>**status** of**Up** are not<br>experiencing a service<br>error.<br>To resolve this error,<br>restart the sensor or<br>contact Technical<br>Support.|


If the collection module on the sensor experiences problems, the


sensor collection state changes to **Suspended**

(ACTIVE_DELAYED) for an hour during which collection is


stopped. The sensor maintains its connection to the server and

receives actions from the server during this time. After this hour,


the sensor returns to **Enabled** (ACTIVE_NORMAL) state.


When a sensor changes to the **Suspended** state, Endpoint


Protection/NGAV features (like Anti-Ransomware and Anti
Malware) continue to function, but you cannot change sensor


settings, and the sensor does not send data from these features to

the server.

## Sensor performance issues (Windows


If multiple sensor shutdowns occur 10 times within 24 hours, the

sensor enters **Sensor safe mode** for 30 min. During this time, the


sensor's MinionHost process stops running.


During Sensor safe mode:


For versions prior to 18.0:


The sensor does not maintain its connection to the server. The


sensor appears **Offline** in the **Sensors** screen and you

cannot interaction with the sensor during this time.


For versions 18.0+:


The sensor remains connected to the server and can receive


and perform a limited number of actions (fetch logs and

upgrade). In the **Sensors** screen, the collection state is


**Suspended** (ACTIVE_DELAYED), meaning that collection is

stopped.


During Sensor safe mode, Endpoint Protection/NGAV features

(such as Anti-Ransomware and Anti-Malware) continue to function,


but you cannot change feature settings, and the sensor does not

send data from these features to the server.


After 30 minutes in safe mode, the sensor attempts to return to its

normal functionality.

## Sensor behavior when exceeding 5%

## RAM


On Windows machines that exceed minimum resource

requirements, when a sensor exceeds 5% average RAM usage


over a period of 30 seconds, or experiences a spike of over 15%

RAM, the sensor behavior depends on factors such as how


recently it previously crashed or stopped collection. In some

cases, the sensor suspends or disables collection, and in others


the sensor enters Sensor safe mode.



