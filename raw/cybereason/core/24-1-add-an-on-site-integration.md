|Prerequisite|Details|
|---|---|
|VM<br>operating<br>system|The VM on which you run the on-site collector agent<br>must run one of the supported Linux operating<br>systems, which include Debian, Ubuntu, RHEL, and<br>SUSE.|


|System<br>requirements|Your VM must meet these minimum system<br>requirements:<br>1 GB RAM for each collected data type. For<br>example, if you want to collect EDR, DNS, and<br>DHCP data, you would need 3 GB RAM.<br>2 CPUs. If you expect your connected integratio<br>to send more than 10,000 events per second, yo<br>may need between 4 and 6 CPUs.<br>100 MB free disk space|Col3|
|---|---|---|
|Docker|A virtual machine (VM) running Linux with Docker an<br>Docker compose (version 3.9 or higher) installed. Fo<br>details on how to install Docker, see Install the Dock<br>Engine on CentOS<br>(https://docs.docker.com/engine/install/centos/#insta<br>docker-engine) (for CentOS machines) or Install the<br>Docker Engine on Ubuntu<br>(https://docs.docker.com/engine/install/ubuntu/#insta<br>docker-engine).<br>To check that Docker is installed, you can use the<br>**docker -v** command.||
|Allow communication for the following addresses, ports, and<br>protocols to enable communication with your Chronicle<br>instance:<br>**Connection**<br>**Protocol**<br>**Destination**<br>**Port**<br>TCP<br>_malachiteingestion-_<br>_pa.googleapis.com_<br>_(https://malachiteingestion-_<br>_pa.googleapis.com)_<br>443<br>TCP<br>_europe-west2-malachiteingestion-_<br>_pa.googleapis.com (https://europe-_<br>_west2-malachiteingestion-_<br>_pa.googleapis.com)_<br>443<br>TCP<br>_asia-southeast1-malachiteingestion-_<br>_pa.googleapis.com (https://asia-_<br>_southeast1-malachiteingestion-_<br>_pa.googleapis.com)_<br>443|Allow communication for the following addresses, ports, and<br>protocols to enable communication with your Chronicle<br>instance:<br>**Connection**<br>**Protocol**<br>**Destination**<br>**Port**<br>TCP<br>_malachiteingestion-_<br>_pa.googleapis.com_<br>_(https://malachiteingestion-_<br>_pa.googleapis.com)_<br>443<br>TCP<br>_europe-west2-malachiteingestion-_<br>_pa.googleapis.com (https://europe-_<br>_west2-malachiteingestion-_<br>_pa.googleapis.com)_<br>443<br>TCP<br>_asia-southeast1-malachiteingestion-_<br>_pa.googleapis.com (https://asia-_<br>_southeast1-malachiteingestion-_<br>_pa.googleapis.com)_<br>443||


|Connection<br>Protocol|Destination|Port|
|---|---|---|
|TCP|_malachiteingestion-_<br>_pa.googleapis.com_<br>_(https://malachiteingestion-_<br>_pa.googleapis.com)_|443|
|TCP|_europe-west2-malachiteingestion-_<br>_pa.googleapis.com (https://europe-_<br>_west2-malachiteingestion-_<br>_pa.googleapis.com)_|443|
|TCP|_asia-southeast1-malachiteingestion-_<br>_pa.googleapis.com (https://asia-_<br>_southeast1-malachiteingestion-_<br>_pa.googleapis.com)_|443|


|Connection<br>Protocol|Destination|Port|
|---|---|---|
|TCP|_australia-southeast1-_<br>_malachiteingestion-_<br>_pa.googleapis.com (https://australia-_<br>_southeast1-malachiteingestion-_<br>_pa.googleapis.com)_|443|
|TCP|_accounts.google.com_<br>_(https://accounts.google.com)_|443|
|TCP|_gcr.io (https://gcr.io)_|443|
|TCP|_oauth2.googleapis.com_<br>_(https://oauth2.googleapis.com)_|443|
|TCP|_storage.googleapis.com_<br>_(https://storage.googleapis.com)_|443|
|TCP|_cybereasonartifactory.jfrog.io_<br>_(https://cybereasonartifactory.jfrog.io)_|443|


3. Select the relevant addresses for your region and add a

firewall rule exception for this address to enable


communication with your Cybereason platform:










|Region|Address|Countries<br>Included|
|---|---|---|
|US East|connect-us-e1-<br>1.cybereason.net/onPrem/*|United<br>States<br>Canada|
|EU West|connect-eu-w1-<br>1.cybereason.net/onPrem/*<br>connect-eu-w3-<br>1.cybereason.net/onPrem/*|Belgium<br>France<br>Germany<br>Italy<br>Netherlands<br>Switzerland<br>United<br>Kingdom|
|APAC<br>Northeast|connect-as-ne1-<br>1.cybereason.net/onPrem/*|Japan<br>South<br>Korea|


|Region|Address|Countries<br>Included|
|---|---|---|
|APAC<br>Southeast|connect-as-se1-<br>1.cybereason.net/onPrem/*|Australia<br>Indonesia<br>Singapore|



4. Enable log forwarding in your external platforms. For details


on the required configuration for each integration, find your

[integration on the Cybereason Integrations (/s/integrations)](https://nest.cybereason.com/s/integrations)


page. In the page for your specific integration, select the
**Configure** tab to view the configuration details for each


integration.


When you set up log forwarding, you will select an **IP**


**address**, **Port**, and **Protocol** to use for the log forwarding.
Then later, when you configure the access details in the


**Cybereason Connect** screen for the integration and the on
site collector, you will specify the same port and protocol. The


collector agent then listens on that port and protocol for logs

forwarded from your integrated platforms.


For each data source (integration) from which you forward

logs to the collector agent, you must specify a **unique** port for


each data source. For example, if you forward logs from Palo

Alto Firewall and Microsoft Exchange, you must use one


unique port for the Palo Alto logs and another unique port for

the Microsoft Exchange logs. Having a unique port enables


Cybereason XDR to use the correct parser for the data being

ingested.


Note


When you configure the port to use to forward logs to the


on-site collector, ensure that the address and port are
available to communicate based on your firewall settings


to ensure that the on-site collector is able to retrieve logs.


5. In the **Cybereason Connect** screen, select the relevant


integration.

6. In the **Access Details** section for the integration, in the **Name**


field, give the integration instance a name.

7. In the **On-Site Collector** details section, select an existing


collector or create a new one.


8. Click **Generate Collector** (if you are creating a new site) or


**Need to download collector again** (if you select a previously

created site).


The **deployment.zip** file downloads to your machine.


9. In the **Cybereason Connect** screen, click **Get Credentials** .


A new browser tab opens with the credentials in JSON syntax:


```
   {

   "jwt":"<JWT token>",

   "artifactoryPassword":"<password>"

   }

```

The Cybereason platform generates both of these values. You
should not modify either of these credentials as modification


of the credentials will cause the collector agent to not

communicate with your Cybereason platform.


These credentials are valid for 24 hours after generation. If

you do not install the collector on your VM within 24 hours, you


will need to generate the credentials again.
10. Copy the value of the **jwt** key and save it to a file with a **.txt**


suffix.

11. Note the password in a secure location as you will need it later


in the process.

12. Enter the relevant **Port** and **Protocol** on which the on-site


collector will listen on the VM machine.

13. Click **Connect** in the **Access Details** pane to finalize the


configuration.


If you navigate to the **My Integrations** pane, you will see the


integration added but it will report that Cybereason XDR has

never received data.


14. Move the **.txt** file with the value of the **jwt** key and the

**deployment.zip** file to the VM machine you prepared for the


on-site collector agent.
15. Unpack the **deployment.zip** file on the VM machine.


Note


If you use minikube to expand the deployment.zip file,


make sure you mount both the deployment.zip file and the
.txt file with the JWT key value.


16. In the unpacked **deployment.zip** file, run the deployment


script with this command:

```
   sh deployment.sh

   (https://deployment.sh) <path to the

   .txt file> '<password from generated

   credentials>'

```

In the command above, make sure you update the path to the


real path with your file and the password you noted earlier.


Depending on what version of Docker compose you are


using, you may need to modify the **docker-compose**

command. For example, if you are using Compose version 2,


you modify the **docker-compose** to **docker compose**

(without the hyphen). For up-to-date details on these


[commands, see Overview of docker compose CLI](https://docs.docker.com/compose/reference/)

[(https://docs.docker.com/compose/reference/) in the Docker](https://docs.docker.com/compose/reference/)


documentation.


Note


Ensure that the machine on which you run this file has

[network access to the Cybereason XDR on-site collector](https://cybereasonartifactory.jfrog.io/)


[artifactory (https://cybereasonartifactory.jfrog.io) required](https://cybereasonartifactory.jfrog.io/)

as part of the container installation.


After you run the script to start the on-site collector agent, the

following message should display in the command window and


the logs of the Docker container on the VM machine running the

agent:

```
 Starting to listen for <protocol> syslog

 on <address>:<port>.

```

The actual protocol, address, and port in your logs may differ
depending on the configuration you performed in the other


platform.


When your Chronicle instance and your Cybereason platform


receive the logs successfully, you find the following log entries in

the Docker container logs on the VM machine running the on-site


collector agent:

```
 Accepting new syslog TCP connection.

 Batch (<number_of_logs>, <integration>)

 successfully uploaded.

```

You can also check the logs of the Docker container for your on

site collector with the **docker ps** command. The output for this

command displays a list of Docker containers that are running on


the virtual machine. Then, you run the **docker logs -f <container**

**ID>** command to view the log itself, where you will see the same


lines as above.


The first time you start the on-site collector agent, it may take a


few minutes for the logs to arrive in your Chronicle instance and

your Cybereason platform so you may need to wait approximately


ten minutes to begin to see the data in your Cybereason


environment.


If there are issues where the on-site collector stops for any reason,


the on-site collector agent will perform an automatic restart of the
collector agent. You will also see a notification of this restart.


[If you have issues with the collector agent, see Troubleshooting](https://nest.cybereason.com/s/article/4782516)

[Problems with the XDR On-Site Collector Agent](https://nest.cybereason.com/s/article/4782516)


[(/s/article/4782516).](https://nest.cybereason.com/s/article/4782516)


Watch this video on deployment of the on-site collector agent for


Cybereason XDR:


Watch this video on how to verify the prerequisites and successful


deployment of the on-site collector agent for Cybereason XDR, as

well as some troubleshooting suggestions:



