|Component|System Area|
|---|---|
|Pingdom|User experience|
|Zabbix|System monitoring|
|ELK (elastic search)|Logs monitoring|
|Zabbix|Application-level monitoring|
|Grafana|Visual graphs and trends|


**Zabbix server**


The Zabbix server is located on the Cybereason AWS private
monitoring VPC. The Zabbix server runs a set of predefined


actions to notify the teams responsible for each issue. The Zabbix

server can run various corrective actions to solve issues


automatically.


**Zabbix agents**


Zabbix agents are installed as part of the general Cybereason

image. Agents run with the relevant monitoring template. Once a


policy threshold is exceeded, a message is sent to the central

server that represents the problem graphically on the service map


and on the central console. Zabbix agents can run various

corrective actions to solve issues automatically.


The solution monitors the following types of data for Cybereason

services infrastructure:


Application availability

Performance


Faults


The monitoring solution enables infrastructure management from


the bottom up, throughout all levels of the computing environment

of the service, including:


Network management

Operation system management


Database management

Application management


At each level, Zabbix enables system administrators to:


View the real-time status of the service


Analyze the root-cause of each issue
Access tools to fix issues



