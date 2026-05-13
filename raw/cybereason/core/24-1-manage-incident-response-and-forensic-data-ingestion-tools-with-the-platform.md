The **IR Tools** screen supports the deployment and running of


tools on up to 5,000 endpoint machines. If you need to deploy

and run the tools on more than 5,000 machines, you should


use the API to perform these operations.


The use of IR and Forensic data ingestion tools is supported on


Windows and Linux machines.


The forensic data ingestion tool package provided with your DFIR


purchase includes the Velociraptor agent, an open-source

forensic investigation tool, which regularly undergoes Cybereason


performance and security testing. Any issues with the Velociraptor

agent are the responsibility of and will be resolved by Rapid7 and


the Velociraptor team.

In this topic:


Request an Express IR environment (partners only)

Enable the DFIR module


Environment prerequisities

Prepare your Linux machines


Deploy Cybereason sensors

Enable IR tools in a sensor policy


Assign the Responder L2 role

Add a tool package


Deploy a tool package

Run a tool package


Upload results to a GCP bucket

Delete a tool package


View results from a tool package execution

Investigate a machine

## Request an Express IR environment


As a Cybereason partner, to use the IR tool management features,

you must request a special Express IR environment created for IR


[engagements. To request an Express IR environment, see How to](https://nest.cybereason.com/resource-documents/how-request-cybereason-express-ir-new-provisioning-management)

[Request a Cybereason Express IR Environment (/resource-](https://nest.cybereason.com/resource-documents/how-request-cybereason-express-ir-new-provisioning-management)


[documents/how-request-cybereason-express-ir-new-provisioning-](https://nest.cybereason.com/resource-documents/how-request-cybereason-express-ir-new-provisioning-management)

[management).](https://nest.cybereason.com/resource-documents/how-request-cybereason-express-ir-new-provisioning-management)


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

## Add a tool package


To run an IR tool on any machine with a Cybereason sensor, you

must add the tool package to the Cybereason platform. You


specify the name and default configuration for the package when

it is deployed to machines later.


**To add a tool package, follow these steps:**

1. Ensure that the package file for the IR tool is present on the


machine from which you access the **IR Tools** screen.


Note


The tool package file must be smaller than 100 MB to


upload.


2. In your Cybereason platform, navigate to the **IR Tools** screen.


3. In the **IR Tools** screen, click **Add Tool** .


4. In the **Add Tool** pane, give the tool package a unique name


and optional description.


Note


You must provide a unique name for each tool, even if it is

a different version of the same tool program.


5. In the **Package file** edit field, click **Choose file** and select the


tool package.


6. In the **Tool run commands** section, optionally add details on

the run configuration for this package:


The **Program** name used to run the package


If you are running your own tool packages, you do not


need to add a value in this field. You should use this field

when you are using another program to run your


package.


Note


If you want to run script files as your tool package,
Cybereason recommends that you use this field to


specify the specific application or program that


should run the script. Adding the program name


ensures that the Cybereason platform loads the

correct script interpreter instead of a default system


shell.


**Command line arguments** to use when the tool runs


Note


If the commands you want to use contain a backslash


character in the command, ensure you add an

escape character around the string with the quotes.


For example, if you have this command **-tsource C -**

**target EvidenceOfExecution -tdest**


**C:CybereasonForensicsKape**, you need to add an

escape character with the backslash string, so the


string will now be the **C:\CybereasonForensics\Kape**

string. You can also use the forward slash without the


escape character, such as

**C:/CybereasonForensics/Kape** .


**Location for the results file** to which to write the
collected data after the tool finishes running.


If you leave this field empty, the sensor writes the output

for the tool execution to the default sensor directory on the


endpoint. For example, on Windows machines, the sensor

adds the results in the


**C:/ProgramData/apv2/IRToolsOutput/IRTOOLS.**

**<packageName>/** folder.


The values you enter in this section are used as the default
run configuration for tool execution. You can use other


commands in a specific execution later as needed. If you do

not provide command line arguments or a result directory later


when running the tool, the default you enter here is used.


Note


If you have an existing tool package already deployed to

the Cybereason platform, you can upgrade the existing


package using this same process. When upgrading the

existing tool, change the package.


7. Click **Add** .


The tool package is added in the list of available tool packages.


It may take a short period of time to see the tool package display


in the list of deployed packages, depending on your internet

connection on the machine from which you are adding this


package file.


You will see additional tools in the list of available tools that you


did not deploy yourself. These are the out-of-the-box forensic data

ingestion tools included with your DFIR package:

## Deploy a tool package


After you upload the tool package to your Cybereason platform,


you can deploy the package as needed on an ongoing basis. This

enables you to save the package on your Cybereason platform as


needed but deploy to different sets of machines as the needed

arises.


You should use this option when you select the **Static** deployment

type when you add a package. **To deploy a tool package, follow**


**these steps:**


1. In the **IR Tools** screen, click **Deploy Tool** .


2. In the **Deploy Tool** pane, select the tool to deploy.

3. In the **Deployment Type** section, select the maner in which to


deploy the tool:






|Deployment<br>type|Description|
|---|---|
|Dynamic|Deploy tools**automatically** on a rolling,<br>ongoing basis as other machines become<br>available (e.g. online). If you select this<br>option, each time a sensor that matches<br>the selected operating system comes<br>online, the Cybereason platform deploys<br>the package fle to the new sensor.<br>If you want to deploy the tool to all<br>machines of a specifc type, such as all<br>Windows machines, you use this option.|


|Deployment<br>type|Description|
|---|---|
|Static|Deploy tools**manually a single time** to a<br>specifc set of machines.<br>If you want to deploy the tool a specifcally<br>target set of machines one time, use this<br>option.<br>If you select this option, you can deploy<br>up to 50 machines in a single deployment.|



If you use Sensor tampering protection in your environment,


ensure for each IR tool that you specify a directory for the
results files. By default, if you do not specify a results file


location, the tool results are saved to the sensor folder, which

is protected against any write operations. As a result, leaving


the output directory option blank will cause any tool execution

to fail.


For forensics data ingestion tools, the results file is saved to
the **C:ProgramDatacrdfir** folder.


4. If you select the **Dynamic** deployment type, in the **Machines**

**to deploy on** field, select the type of operating system to


which to deploy the tool:


In addition, in the **OS Versions** field, select the operating


system versions to which to deploy the tool:


For example, if you select **Windows** for the **Machines to**


**deploy on** option, in the **OS Versions** option, you can select

**Windows 7**, **Windows 8.1**, and so forth.


Note


If you select this option for the tool package, you will not


be able to modify the type later to the **Static** option. For

example, if you use this option to deploy a tool to all your


Windows 10 machines, but later you want to deploy a tool

to an additional number of machines that are not Windows


10 machines, you can add the tool again with a **different**

**package name** and select the **Static** deployment type.


5. If you select **Static** for the deployment type, in the **Machines**


**to deploy on** section, select the filter by which to set the

machine list:



|Filter|Details|
|---|---|
|OS|Select the type of operating system to which<br>to deploy the tool.<br>After you select the operating system type, if<br>needed in the**OS Versions** feld, select the<br>relevant versions for the operating system<br>type.|
|Machine<br>name|Select the machine name string to which to<br>deploy the tool.<br>You select an operator (**Is Not**, **Is**, **Not**<br>**Contains** or**Contains**) and the string that is<br>in the machine name.|
|CSV|Add a CSV fle with specifc machine names<br>to which to deploy the tool.<br>In your CSV fle, in each line, add the sensor<br>ID in the Cybereason platform uses for the<br>sensor. You can retrieve a list of sensor IDs<br>for all your sensors in the**System > Sensors**<br>screen.<br>Click**Choose File** and navigate to the fle.|


6. Click **Deploy** .


Note





You can deploy a tool to a maximum of 1000 machines in a

single deployment operation.


For each deployment type, before you click **Deploy**, you can also

view the list of machines to which the tool will deploy when you


finalize the deployment configuration. This list displays in the

**System > Sensors** screen.


The deployment grid in the **Tools** tab adds the deployment type

for the tool, and updates the deployment status and details as the


deployment progresses:


If you would like to view the deployment status of various


machines for each tool, select the **Deployed Machines** tab:


You select the tool name and the Cybereason platform updates


the list of target machines for the deployment, including the

deployment status, sensor status, and deployment details.

## Run a tool package


Once the tool is successfully deployed to the appropriate

machines, you can run the tool on selected machines.


You can use the default configuration included with the tool

package when you uploaded the tool or specify a unique run


configuration for each tool package execution.


**To run a tool package, follow these steps:**


1. In the **IR Tools** screen, in the **Deployed Machines** tab, click


**New Run** .


2. In the **New Run** pane, in the **Select Tool** field, select the tool


to run.


3. Below the **Select Tool** field, update the tool run configuration


as needed.


When you select the tool, you see the tool, you see the default


configuration when you uploaded and deployed the tool. You

can edit these values as needed.


4. In the **Select machines** field, select the machines on which to


run the tool:


5. Click **Run** .


The Cybereason platform sends the command to the tool package


on the machine and the tool runs. You can verify the status of the

tool execution in the package grid in the **Tools** tab:

## Upload results to a GCP bucket


After you finish the execution of a tool and collect the results, you

are able to upload the results to your own dedicated GCP bucket.


**To upload results to a GCP bucket, follow these steps:**


1. In the **IR Tools** screen, open the **Deployed Machines** tab.


2. In the **Deployed Machines** tab, click the **Upload Results to**


**GCP** button.


3. In the **Upload Results to GCP** pane, in the **Selected tool** edit


box, select the tool from which you want to upload results.


4. In the **Select machines** edit field, select the machines from


which to retrieve results to upload:


5. In the **Path with files to upload** edit field, enter the path to

the results file (if needed):


6. Click **Upload Files** .


The Cybereason platform uploads the files to your GCP bucket for


you to retrieve later.


If you want to see the details of your GCP bucket, in the **Account**


**Details** section at the top of the **Upload Results to GCP** pane,

expand the section to view the address for the bucket and the


service account key.

## Delete a tool package


After you have completed the work with your IR tool, you can


remove these tools from endpoint machines.


**To remove a tool package, follow these steps:**


1. In the **IR Tools** tab, in the tool deployment grid, in the row with


your tool name, click the three dots to display more options:


2. In the menu options, select **Delete Tool** .


When you delete the tool package, the Cybereason platform


deletes the tool from the saved tools on the platform and removes

the package from endpoint machines.

## View results from a tool package


When the incident response tool or forensic data ingestion tool

runs, the tool sends the results of the tool execution to the


directory that you specified in the tool execution configuration

when you started the tool execution.


After the tool execution is complete, you can view the tool results
file on each machine.


**To view results, follow these steps:**


1. In the **IR Tools** screen, select the **Deployed Machines** tab.


2. In the **Deployed Machines** tab, in the tool selector list, select


the name of your tool package.


The machine list updates depending on the tool name.

3. In the machine list, in the row for the machine, click the three


dots to display the menu options:


4. Select **View Results Files** .


The Cybereason platform opens a new browser tab to the
directory where the results files were saved. You can view and


extract the result files from there as needed.



