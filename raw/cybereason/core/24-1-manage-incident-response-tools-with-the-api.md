Request an Express IR environment (partners only)

Enable the DFIR module


Environment prerequisities

Prepare your Linux machines


Deploy Cybereason sensors

Enable IR tools in a sensor policy


Assign the Responder L2 role

Log in using the UI with the L2 Responder user


Log in using the API with the L2 Responder user

Log in the first time as the L2 responder user


Log in after the first time as the L2 responder user

Upload and deploy IR tools


Monitor IR tool deployment on endpoints

Run an IR tool


Monitor IR tool execution on endpoints

Upload IR tool results


Retrieve the results from the GCP bucket

Remove IR tools

## Request an Express IR environment


As a Cybereason partner, to use the IR tool management features,

you must request a special Express IR environment created for IR


[engagements. To request an Express IR environment, see How to](https://nest.cybereason.com/s/article/how-request-cybereason-express-ir-new-provisioning-management)

[Request a Cybereason Express IR Environment (/s/article/how-](https://nest.cybereason.com/s/article/how-request-cybereason-express-ir-new-provisioning-management)


[request-cybereason-express-ir-new-provisioning-management).](https://nest.cybereason.com/s/article/how-request-cybereason-express-ir-new-provisioning-management)


When your environment is ready, you receive an email with details


on how to access the environment. You can then deploy

Cybereason sensors to assist with the IR effort.


The IR tools environment contains the following:


|Feature|Details|
|---|---|
|Users|The environment contains two default users:<br>The default admin user<br>(**admin@cybereason.com**<br>**(mailto:admin@cybereason.com)**) with<br>the default password. This user has the<br>**Super user** role with the permissions of<br>all other roles.<br>The user you list when creating the<br>environment. This user has the following<br>roles:<br>User admin<br>L3 analyst<br>System admin<br>Policy admin<br>Responder L2<br>Executive<br>The API user (**api@cybereason.com**<br>**(mailto:api@cybereason.com)**) with the<br>default password. This user has the**API**<br>**user** role.|
|LiveFile<br>Search|Live File Search is enabled for the admin and<br>special user requested when creating the<br>environment.|
|Remote Shell|Unrestricted Remote Shell mode is enabled.|
|Endpoint<br>controls|The Endpoint controls section for sensor<br>policies is enabled.|
|MalOp<br>Grouping|MalOp grouping of similar MalOps is<br>enabled.|
|Two-factor<br>authentication<br>(2FA)|2FA is globally enabled for the environment<br>(as seen in the**Security Policy** screen).|
|IR tools<br>management|All IR tools deployment and management<br>capabilities are enabled.|
|DGA<br>detection|Domain classifcation evaluation is enabled.<br>This feature assists with detection of DGA<br>activity.|


## Enable the DFIR module

If you do not use an Express IR environment as a Cybereason IR


partner, you can purchase and enable the DFIR package in your

environment.


Note


To enable the DFIR package, you must upgrade your


environment to a higher Cybereason version from its current

version.


[Open a Technical Support (/s/support) to upgrade your](https://nest.cybereason.com/s/support)

environment and add the DFIR package to your environment. As


part of the DFIR package enablement, incident response tool

management features are also enabled for your environment.

## Environment prerequisities


In your environment in which you use IR tool deployment, you

must have the following prerequisites:


Endpoint machines must have the **GeoTrust RSA CA 2018**
**Intermediate CA** and **DigiCert Global Root CA** certificates in


the machine's operating system certificate store.
If your network uses mechanism such as certificate pinning,


SSL inspection, or other mechanisms that use TLS

termination, you must ensure that TLS termination is canceled


for any traffic from the endpoint machine to the Cybereason

platform.

## Prepare your Linux machines


If you use the Incident Response tool management features on

Linux machines, ensure you have the required packages installed


[on your machine. For details on these packages, see Install](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)

[required packages (Linux) (/s/knowledge-base?article=24-1-pre-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)


[installation-requirements-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)

[instructions&language=en_US#install-required-packages-linux).](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)


To ensure that the IR tool deployment functions smoothly, you

must install Cybereason sensors on all machines that are involved


an IR process.


[For details on sensor deployment, see Deploy Sensors](https://nest.cybereason.com/s/knowledge-base?article=24-1-deploy-sensors&language=en_US#deploy-sensors)


[(/s/knowledge-base?article=24-1-deploy-](https://nest.cybereason.com/s/knowledge-base?article=24-1-deploy-sensors&language=en_US#deploy-sensors)

[sensors&language=en_US#deploy-sensors).](https://nest.cybereason.com/s/knowledge-base?article=24-1-deploy-sensors&language=en_US#deploy-sensors)


Note


When allowing the sensor to communicate with the


Cybereason Detection and Registration servers within your

organization's network, you must also allow the sensor to


communicate with the Cybereason CMS service. For more

information on allowing sensor communication, see the


[Configure your firewall and network to allow sensor](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#configure-your-firewall-and-network-to-allow-sensor-communication-all-oss)

[communication (all OSs) (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#configure-your-firewall-and-network-to-allow-sensor-communication-all-oss)


[pre-installation-requirements-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#configure-your-firewall-and-network-to-allow-sensor-communication-all-oss)
[instructions&language=en_US#configure-your-firewall-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#configure-your-firewall-and-network-to-allow-sensor-communication-all-oss)


[network-to-allow-sensor-communication-all-oss).](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#configure-your-firewall-and-network-to-allow-sensor-communication-all-oss)

## Enable IR tools in a sensor policy


In a designated sensor policy, in the **Response settings** section


of the sensor policy, enable the **Manage Incident Response**

**Tools** option.


After you enable this option, ensure that you assign the specific

policy to the sensors you want to include in the IR engagement.

## Assign the Responder L2 role


IR tool management tasks are available for users with the

Responder L2 role. This role enforces two-factor (TFA) for each


user with the Responder role or requires you to enable SSO for a

user.


User admins assign the **Responder L2** role to Cybereason users

from the **Users** screen.


Note


Users with the Responder L2 role cannot be assigned the


**Sensor Admin L1**, **Local Analyst L1**, **Local Analyst L2**, or

**Local Responder** roles.

## Log in using the UI with the L2 Responder

## user


After a user admin assigns the L2 Responder role to your user,
you log in to the platform using the standard login flow.


After you enter your username and password:

On the first login, the platform displays a 16 character key.


Enter this key into your TOTP authentication program or app,

which will generate a one-time code that the user should


enter.

On subsequent logins, enter the one-time code from your


authentication program or app.


## Log in using the API with the L2

The login steps for the API differ depending on whether this is the


first time you log in or subsequent times.

## Log in the first time as the L2 responder

## user


[1. Log out with the API (/s/knowledge-base?article=log-in-with-](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api&version=#log-out-from-your-machine)


[the-api&version=#log-out-from-your-machine) of the](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api&version=#log-out-from-your-machine)

Cybereason platform or remove the JSESSION ID cookie from


your REST API client.

2. Log in using the API with the new L2 Responder user. For


[details on how to log in with the API, see Log in with the API](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api)

[(/s/knowledge-base?article=log-in-with-the-api).](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api)


3. In the response for the login request, locate the **sid-number**


section:

```
   <div class="sid-number">

   <span>XZYH</span>

   <span style="width: 10px;">

   </span>

   <span>Z6UI</span>

   <span style="width: 10px;">

   </span>

   <span>HG3V</span>

   <span style="width: 10px;">

   </span>

   <span>X6M6</span>

   </div>

```

4. From the **sid-number** section, combine the key parts between


each **span** tag.


In the example above, the full key would be

**XZYHZ6UIHG3VX6M6** .


This key is the key you use in your authentication utility or app

for the email address associated with the Responder L2 user.


5. In the authentication utility or app of your choice, set up two


factor authentication for the email for the Responder L2 user,


using the key you built from the previous login request.


Cybereason supports Two-Factor Authentication (TFA) for user


accounts using Time-based One Time Password (TOTP)

applications. Cybereason TFA supports TOTP applications


that support RFC 4226.


6. Login with two-factor authentication. For details on how to log


[in with two-factor authentication with the API, see Log in with](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api-with-tfa)

[the API with TFA (/s/knowledge-base?article=log-in-with-the-](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api-with-tfa)


[api-with-tfa).](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api-with-tfa)


The Cybereason platform returns a JSESSION ID that you can


reference in subsequent requests.


After you perform these steps you can perform any other IR tasks


using the Cybereason platform.

## Log in after the first time as the L2


1. Log in using the API with the L2 Responder user. For details


[on how to log in with the API, see Log in with the API](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api)

[(/s/knowledge-base?article=log-in-with-the-api).](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api)


2. Login with two-factor authentication. For details on how to log


[in with two-factor authentication with the API, see Log in with](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api-with-tfa)


[the API with TFA (/s/knowledge-base?article=log-in-with-the-](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api-with-tfa)

[api-with-tfa).](https://nest.cybereason.com/s/knowledge-base?article=log-in-with-the-api-with-tfa)


The Cybereason platform returns a JSESSION ID that you can

reference in subsequent requests.


After you perform these steps you can perform any other IR tasks

using the Cybereason platform.

## Upload and deploy IR tools


To enable you to run an IR tool on any machine with a Cybereason

sensor, you must upload the tool package to the Cybereason


platform. As part of the upload process, the Cybereason platform

deploys the package to the machine.


**To upload and deploy an IR tool, follow these steps:**

1. Ensure that the package file for the IR tool is present on the


machine from which you will run the API request to upload the
IR tool, and that the tool package file is smaller than 100 MB.


2. In your REST API client or script, create the request to upload


and deploy the execution. Ensure that you give the tool


package deployment a unique name.


For details on the API endpoint to upload and deploy an IR


[tool, see the Upload and Deploy a Tool Package](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-upload-and-deploy-a-tool-package)

[(/s/knowledge-base?article=incident-response-api-token-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-upload-and-deploy-a-tool-package)


[upload-and-deploy-a-tool-package) topic in the API](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-upload-and-deploy-a-tool-package)

documentation.


Note


If you have an existing tool package already deployed to


the Cybereason platform, you can upgrade the existing

package using this same process. When upgrading the


existing tool, change the name of the file but make sure
that the Operating System filter remains the same.


Cybereason does not support the upgrade of a tool with a
different Operating System filter.


3. Run the request or script using your REST API client or


automation framework.

## Monitor IR tool deployment on endpoints


You can use the Cybereason API to monitor the deployment

process and ensure the tool package deploys correctly. For


details on the API endpoint to monitor deployment, see the

[Monitor Incident Response Tool Deployment on Endpoints](https://nest.cybereason.com/s/knowledge-base?article=all-versions/monitor-incident-response-tool-deployment-endpoints)


[(/s/knowledge-base?article=all-versions/monitor-incident-](https://nest.cybereason.com/s/knowledge-base?article=all-versions/monitor-incident-response-tool-deployment-endpoints)

[response-tool-deployment-endpoints) topic in the API](https://nest.cybereason.com/s/knowledge-base?article=all-versions/monitor-incident-response-tool-deployment-endpoints)


documentation.

## Run an IR tool


Once the tool is successfully uploaded to the Cybereason


platform and deployed to the appropriate machines, you can run

the tool on selected machines.


**To run an IR tool on a machine, follow these steps:**


1. In your REST API client or script, create the request to run the


IR tool. For details on using the API endpoint to run the IRtool,

[see the Run an Incident Response Tool (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-run-an-incident-response-tool)


[article=incident-response-api-token-run-an-incident-response-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-run-an-incident-response-tool)

[tool) topic in the API documentation.](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-run-an-incident-response-tool)


In your API request body, ensure that you run the tool on a
specific sensor or a filtered group of sensors, but not both.


Specifying a specific sensor and a filtered group of sensors

will cause the request to fail.


If you use Sensor tampering protection in your environment,

ensure for each IR tool that you specify a directory for the


results files. By default, if you do not specify a results file

location, the tool results are saved to the sensor folder, which


is protected against any write operations. As a result, leaving

the output directory option blank will cause any tool execution


to fail.

2. Run the request or script using your REST API client or


automation framework.


The response for the request to run an IR tool contains a batch


number which indicates the successful initiation of the IR tool

action on selected endpoints. In order to monitor the execution


[status of the tool on endpoints, see the Monitor Incident Response](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-incident-response-tool-execution)


[Tool Execution (/s/knowledge-base?article=incident-response-api-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-incident-response-tool-execution)


[token-monitor-incident-response-tool-execution) reference topic in](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-incident-response-tool-execution)

the API documentation.

## Monitor IR tool execution on endpoints


You can use the Cybereason API to monitor the execution of the

tool and ensure the tool package runs correctly. Monitoring the


incident response tool execution is supported only for endpoints

on which the Cybereason sensor is installed. For details, see the


[Monitor Incident Response Tool Execution (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-incident-response-tool-execution)

[article=incident-response-api-token-monitor-incident-response-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-incident-response-tool-execution)


[tool-execution) reference topic in the API documentation.](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-monitor-incident-response-tool-execution)


You can also verify the status of the IR tool execution in the **Action**


**log** in the **Sensors** screen.

## Upload IR tool results


Once a tool successfully runs on an endpoint, you can upload the


results to a predefined Google Cloud Platform (GCP) bucket.


**To load the results to the GCP bucket, follow these steps:**


1. In your REST API client or script, create the request to load


the results. For details on the API endpoint to load the results,


[see the Load Results for an Incident Response Tool Execution](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-load-results-for-an-incident-response-tool-execution)

[(/s/knowledge-base?article=incident-response-api-token-load-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-load-results-for-an-incident-response-tool-execution)


[results-for-an-incident-response-tool-execution) reference](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-load-results-for-an-incident-response-tool-execution)

topic in the API documentation.


2. Run the request or script using your REST API client or


automation framework.


The maximum allowed size for the results file is 1.2 GB.

## Retrieve the results from the GCP


When the IR tool runs, the tool sends the results of the tool


execution to the directory that you specified in the tool execution

API request or to the default directory that the program uses.


After you uploaded results to GCP bucket from relevant endpoints

[by running the Load Results for an Incident Response Tool](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-load-results-for-an-incident-response-tool-execution)


[Execution (/s/knowledge-base?article=incident-response-api-](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-load-results-for-an-incident-response-tool-execution)

[token-load-results-for-an-incident-response-tool-execution) API,](https://nest.cybereason.com/s/knowledge-base?article=incident-response-api-token-load-results-for-an-incident-response-tool-execution)


you can now retrieve you results from the GCP bucket.


By default, the Cybereason platform searches for results files with


a **.zip** extension to send to the bucket. If you need to use other file

[extensions for results sets, open a Technical Support (/s/support)](https://nest.cybereason.com/s/support)


case and note the file extensions you need for your results files.



