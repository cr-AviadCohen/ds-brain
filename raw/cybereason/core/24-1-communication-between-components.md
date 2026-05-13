## Sensors to Detection servers

Sensors communicate with their Detection server through port 443


via proprietary bi-directional RPC protocol over a persistent TCP

connection. The Detection servers can throttle the amount of data


sensors send to avoid overload. Throttled data is resent again. In

addition, the sensors send only the changes in the data, in chunks


at various times. If sensors require an update, the Detection server

issues the update (which it pulled from the Update server) to the


sensor through a Remote Procedure Call. The Detection server is

also tasked with stopping or starting sensor data collection.


Note


In the Cybereason platform, Detection servers do not


communicate directly with each other.


The sensors and Detection server communicate through different


methods depending on whether or not your configuration includes

a Registration server, as illustrated in the following table:






|Registration<br>server|Communication method|
|---|---|
|Yes|Sensor contacts the Registration server,<br>which assigns the sensor to a Detection<br>server.|
|No|Sensor communicates directly with the<br>Detection server that was provided as part<br>of the installation package.|


## Update server to other servers

All Cybereason customers share the Global Update server. This


server also hosts any updates for the Cybereason platform. To

avoid unwanted system changes, updates are not automatically


deployed to Cybereason servers and sensors. Instead, the

Detection servers, Registration server, and WebApp server can


pull updates from the Global Update server when necessary.

## Detection servers to Global and Private

## Threat Intel servers


For the Cybereason platform to leverage threat intelligence

services, the Detection servers need to send sensor information to


the Private Threat Intel server. The Detection servers send IP,

hash, and domain information to the Private Threat Intel server,


which checks the data against the organization's personal

blocklist and allowlist.


If the Private Threat Intel server does not respond with a definitive
classification for the data from the Detection server, it checks the


data against the external Global Threat Intel server, which hosts



