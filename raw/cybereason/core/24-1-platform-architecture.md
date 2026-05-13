To learn about how the different pieces of the Cybereason

[platform communicate, see Communication Between Components](https://nest.cybereason.com/s/knowledge-base?article=24-1-communication-between-components&language=en_US#communication-between-components)


[(/s/knowledge-base?article=24-1-communication-between-](https://nest.cybereason.com/s/knowledge-base?article=24-1-communication-between-components&language=en_US#communication-between-components)

[components&language=en_US#communication-between-](https://nest.cybereason.com/s/knowledge-base?article=24-1-communication-between-components&language=en_US#communication-between-components)


[components).](https://nest.cybereason.com/s/knowledge-base?article=24-1-communication-between-components&language=en_US#communication-between-components)

## Components in your network


To help the Cybereason platform effectively detect, prevent, and


respond to malicious activity in your network, you use the following

components in your network:






|Component|Description|
|---|---|
|Endpoint<br>machine<br>sensors|You install the endpoint sensor on machines in<br>your organization. Sensors collect data about<br>the events and operations that occur on each<br>endpoint throughout your organization.<br>Sensors send the collected data to Detection<br>servers for analysis. For details, see Sensor<br>Architecture (/s/knowledge-base?article=24-1-<br>sensor-architecture&language=en_US#sensor-<br>architecture).|
|Analyst<br>users|Analyst users, on endpoint machines, log in to<br>the Cybereason console to analyze detected<br>behavior and respond accordingly.|


## Components in your dedicated

## Cybereason environment

To help organize and analyze the collected data from endpoint


sensors, as well as report this data in the Cybereason console, the

Cybereason platform uses a number of components that are


deployed in the cloud in your dedicated Cybereason instance.


|Component|Description|
|---|---|
|Registration<br>server|The Registration server enables you to<br>perform load management for Detection<br>servers by automatically assigning sensors to<br>specifc Detection servers. Upon installation,<br>the Registration server maps sensors to<br>Detection servers using a capacity-aware<br>round-robin allocation method or the<br>application of assignment rules you specify for<br>sensors. When a sensor is assigned to a<br>Detection server, the sensor maintains the<br>connection with the Detection server and<br>sends the sensor's endpoint data to that<br>Detection server<br>Note<br>A Registration server is installed for all<br>customer deployments. However, for trials,<br>it is possible to deploy the Cybereason<br>platform without a Registration server.<br>For more information about the Registration<br>server, see Registration server FAQ<br>(/s/article/2121985).|


|Component|Description|
|---|---|
|Detection<br>servers|Detection servers perform data collection,<br>recording, and data analysis of the data<br>received from the sensors. Detection servers<br>use the built-in CMC Engine to collect, record,<br>and analyze data from the sensors. The CMC<br>Engine communicates with the Global and<br>Private Threat Intel servers to determine the<br>classifcation for all analyzed activity.<br>In addition to the CMC Engine, each Detection<br>server hosts a 1 TB partition containing the<br>following:<br>Backup snapshots of the CMC Engine for<br>recovery purposes<br>Raw recordings of the actual data from the<br>sensors<br>Detection servers facilitate sensor<br>management actions, such as starting or<br>stopping data collection and updating<br>software<br>Work with Technical Support to deploy<br>Detection and Registration servers. The<br>Cybereason Technical Services team<br>provisions Detection servers for cloud<br>deployments, and assists with on-premises<br>deployments.|
|NGAV Local<br>update<br>server|If you use NGAV and have a large number of<br>endpoints, you can install one or more NGAV<br>Local Update servers in your network. This<br>server delivers Anti-Malware signature<br>updates to your organization's endpoints more<br>quickly, since it resides on the internal network.<br>This capability can be especially signifcant<br>during the frst-time enabling of the**Anti-**<br>**Malware > Signatures** mode on sensors,<br>during which the full signature database is<br>deployed to each endpoint. Using the NGAV<br>Local update server can help to avoid<br>potential traffc issues on the external network.<br>You can install more than one NGAV Local<br>update server if necessary.<br>For more information about confguring the<br>NGAV Local update server, see NGAV Local<br>Update Server (/s/knowledge-base?article=24-<br>1-ngav-local-update-<br>server&language=en_US#ngav-local-update-<br>server).|


|Component|Description|
|---|---|
|WebApp<br>server|The WebApp server contains a wide variety of<br>data, including:<br>The Cybereason UI<br>A database with encrypted user data and<br>MalOp information<br>The Private Threat Intel server<br>A web service layer<br>When you interact with the UI, the WebApp<br>server queries the Detection servers for the<br>necessary information. In this way, the<br>WebApp server operates as a single<br>management point for Cybereason<br>components in your organization.|
|Private<br>Threat Intel<br>server|The Private Threat Intel server is specifc to<br>your environment. The server hosts your<br>organization's custom reputation information<br>(allowlists and blocklists) and compares those<br>settings with data it receives from the<br>Detection servers.<br>The Private Threat Intel server is also the<br>platform's link to outside intelligence sources.<br>If the Private Threat Intel server does not make<br>a defnitive judgment on data received from<br>the Detection servers, it queries the Global<br>Threat Intel server, which contains globally-<br>recognized information on malware. Results<br>received from the Global Threat Intel server<br>are recorded in the Private Threat Intel server<br>for 24 hours, eliminating the need to<br>repeatedly query remote sources about the<br>same information in a short period of time.<br>24 hours after an entity was checked,<br>Cybereason rechecks the IP, hash, or domain<br>against the threat intelligence resources to<br>verify the classifcation is current.|


|Component|Description|
|---|---|
|Environment<br>microservers|For each environment, microservices perform<br>MalOp decision-making, behavioral<br>allowlisting, asset tagging, and sensor<br>management. This enables a more distributed<br>component layout and improves scalability<br>making future versions of the Cybereason<br>platform more effcient and reliable for<br>upgrades.<br>Cybrereason Technical Support and Technical<br>Services install and manage microservices for<br>Cloud customers.|



The following video describes the Cybereason Detection and

Registration servers:





The following video describes the Threat Intel servers:


## Components shared by all environments

In addition, the Cybereason platform uses components based on


services shared by all customers. Each unique Cybereason

environment has a segmented section for their data with these


services so there is not shared data between environments.






|Component|Description|
|---|---|
|Global<br>update<br>server|The Global Update server is shared among all<br>customers and contains server and sensor<br>update packages, new versions of the<br>Cybereason platform, and security patches.<br>So as not to interrupt your current working<br>environment, your Detection, Registration, and<br>WebApp servers retrieve the necessary data<br>and software updates from the Update server<br>when you choose to apply the updates.|


|Component|Description|
|---|---|
|Data<br>Platform<br>services|For Cybereason environments that employ the<br>new Data Platform works with the Data<br>Platform infrastructure which enables more<br>streamlined handling and storage of data.<br>For a more specifc look at the Data Platform's<br>services, see the architecture articles in the<br>Data Platform Documentation<br>(https://nest.cybereason.com/data-platform-<br>documentation).|
|NGAV Global<br>update<br>server|The NGAV Global update server is a<br>Cybereason server in the cloud that delivers<br>frequent signature updates to the**Anti-**<br>**Malware > Signatures** services on each<br>endpoint.<br>To allow communication with this server, see<br>Enable communication with the Cybereason<br>Global Update servers (all OSs)<br>(/s/knowledge-base?article=24-1-pre-<br>installation-requirements-and-<br>instructions&language=en_US#enable-<br>communication-with-the-cybereason-global-<br>update-servers-all-oss).|
|Detection<br>rule services|The Detection rule service, managed by the<br>Security Research team, enables the addition<br>of detection logic for the Cybereason<br>platform's Detect server and Cross Machine<br>Correlation engine on an ongoing basis. Using<br>this service, the Security Research team adds<br>detections that do not require the upgrade of<br>the platform's sensors or servers.|


|Component|Description|
|---|---|
|Global Threat<br>Intel server|The Cybereason platform uses a shared<br>Global Threat Intel server to compare data in<br>your in-memory graph to globally recognized<br>threat sources to determine the reputation of a<br>given fle, IP address, or domain. The Global<br>Threat Intel server is updated daily, ensuring<br>your data is checked against the most recent<br>threat information in the cybersecurity<br>industry.<br>The Global Threat Intel server uses artifcial<br>intelligence algorithms running on live global<br>intel data to determine if objects are malicious<br>or benign and categorize them accordingly.<br>Information gained from the Global Threat<br>Intel server is fed to your Private Threat Intel<br>server, which communicates the fndings to<br>your Detection servers.<br>24 hours after an entity was checked, the<br>Cybereason platform rechecks the IP, hash, or<br>domain against the threat intelligence<br>resources to verify the classifcation is current.|
|Endpoint<br>Management<br>channel|The Endpoint Management Channel is used to<br>deliver security content at the sensor level.<br>Examples of content sent to the server via the<br>Endpoint Management Channel include:<br>Detection logic<br>New detection/prevention capabilities<br>Software updates<br>The Cybereason platform uses this Channel,<br>for example, for DFIR tool deployment and<br>sensor upgrades.|





