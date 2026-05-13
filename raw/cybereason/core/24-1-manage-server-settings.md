Available settings differ for environments with and without a

Registration server.

## Detection server settings (with a
## Registration server)


















|Field|Description|
|---|---|
|Server<br>name|The name of the Detection server. Cybereason<br>recommends that you use a name that<br>describes the server in a way that will make it<br>easily discernible from other servers in the<br>organization.|
|WebApp<br>interface|The IP address or hostname of the Detection<br>server to which the WebApp server connects.|
|Port|The port through which the WebApp server<br>communicates with the Detection server.|
|Site|The site to which the Detection server is<br>assigned.|
|Sensor<br>interface|The IP address or hostname of the Detection<br>server to which the sensors connect.|
|Port|The port through which sensors communicate<br>with the Detection server.|
|Capacity<br>(Optional)|The maximum number of sensors to assign to<br>this Detection server.|
|Use proxy|If selected, sensors connect to this Detection<br>server via a proxy. You can set to:<br>Auto detect: Auto detect the proxy<br>PAC server: Use a PAC server and enter its<br>URL<br>Proxy List: Enter a Proxy list (enter a<br>hostname and port for each proxy)|


|Field|Description|
|---|---|
|Sensors|The number of sensors connected to the<br>Detection server.<br>This number refects the number of sensors<br>active in the past hour, not the number of<br>sensors active when you view this page. If you<br>want to see the real-time accurate count of<br>active sensors, you can view the active sensors<br>in the**Sensors** screen.|


## Detection server settings (with no
## Registration server)













|Field|Description|
|---|---|
|Server<br>name|The name of the Detection server. Cybereason<br>recommends that you use a name that<br>describes the server in a way that will make it<br>easily discernible from other servers in the<br>organization.|
|Hostname|The IP address or hostname of the Detection<br>server to which the sensors connect.|
|Port|The port through which sensors communicate<br>with the Detection server.|
|Capacity<br>(Optional)|The maximum number of sensors to assign to<br>this Detection server.|
|Sensors|The number of sensors connected to the<br>Detection server.|

## Add a new Detection server

As you monitor and manage your Detection servers, you want to


ensure that you have visibility into all Detection servers. Ensure

that you add all your Detection servers for your environment.


**To add a new Detection server to your environment:**


1. In the **System > Detection servers** screen, click **Add**


**detection server** .

2. Define the Detection server settings according to the fields in


the tables above.


|Field|Description|
|---|---|
|Registration<br>server status|The status of the Registration server: online<br>or offine|
|Host name|The IP address or host name of the<br>Registration server to which the WebApp<br>server connects.|
|Port|The port used by the WebApp server to<br>communicate with the registration server.|



