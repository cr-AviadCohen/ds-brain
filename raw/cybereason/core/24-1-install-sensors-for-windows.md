|Installation<br>option|Details|
|---|---|
|Install Full Stack<br>and Replace<br>3rd Party<br>Antivirus|You can use the Cybereason sensor as a<br>full endpoint protection tool that replaces<br>your existing antivirus tool. Used in this<br>way, Cybereason provides a full stack of<br>endpoint protection and EDR functionality.<br>With this type of installation, you must<br>remove the third-party antivirus from the<br>machine.|
|Install Alongside<br>3rd Party<br>Antivirus|If you do not wish to replace your existing<br>antivirus tool, you can install the<br>Cybereason sensor alongside it on your<br>endpoints. Used in this way, Cybereason<br>complements your existing tool with<br>additional endpoint protection and EDR<br>features.<br>With this type of installation, you can<br>enable all Cybereason features, except for<br>the Anti-Malware > Signatures mode<br>feature, which must remain disabled.|




Ongoing signature updates


Related resources

## Step 1: Create and configure sensor

## policies and groups


To ensure you are protecting your endpoint machines immediately


after sensor installation, you should create sensor security policies

and the necessary sensor groups before you install any sensors.

## Create and configure sensor security


Cybereason recommends configuring sensor policy settings
before installing sensors. Configure these settings from the


**System > Policy management** screen. For details on how to

[create a sensor policy, Sensor Policies (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


[article=24-1-sensor-policies&language=en_US#sensor-policies).](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


Depending on whether you are using an existing antivirus program


or replacing your existing antivirus program with your Cybereason

sensor, you set the **Anti-Malware > Signatures mode** differently:






|Keep existing<br>antivirus<br>program|In the Anti-Malware screen of your sensor<br>policy, do not enable the Signatures mode,<br>so as not to interfere with your third-party<br>antivirus.<br>For additional protection, you can set the<br>Anti-Malware feature to On and enable the<br>Artificial Intelligence and Behavioral<br>document protection features.|
|---|---|
|Replace<br>existing<br>antivirus|In the**Anti-Malware** screen, enable<br>**Signatures** mode. You can set the other Anti-<br>Malware settings as needed to suite your<br>needs.|



Once you install sensors, the sensors receive the settings in your

assigned policies.


Note


Some sensor security settings can also be configured using


sensor personalization or installation parameters, with the

assistance of Technical Support.


## Create and configure sensor groups

If you choose to use sensor groups, create sensor groups before


installation and assign sensors automatically upon installation with

logic to the group to automatically assign certain sensors to a


[specific group on installation. See Create group assignment logic](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)

[(/s/knowledge-base?article=24-1-manage-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)


[groups&language=en_US#create-group-assignment-logic) for](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)

details on how to create assignment logic..


If you are an MSSP, you can download a group-specific installation
package. The group-specific installation packages assign the


sensor to a specific sensor group after installation.


Note


Sensors installed with a group-specific installation package

ignore sensor grouping logic.

## Step 2: Download the sensor installation


Download the sensor installer file from the **System > Overview**

screen:


1. In the **Overview** screen, select **Download Cybereason**


**Installers** . The installation options pane appears.


2. If needed, select a sensor group. The group-specific

installation packages assign the sensor to a specific sensor


group when installed.

3. Select the appropriate Windows package.


a. Installer file with signatures included (32 bit and 64 bit)


(recommended) - Supported on Windows only


b. Installer file without signatures (32 bit and 64 bit)
If you choose the first option to use an installer file with


signatures included, you avoid sensors having to download
the signatures database (~300 MB) upon first time update,


conserving network resources. This option to include the

signatures also protects machines from malware as soon as


the sensor is installed, since the sensor does not have to wait

to download the signature database to the endpoint machine.


[Open a Technical Support (/s/support) case to enable this](https://nest.cybereason.com/s/support)

option.


If you are using the Cybereason sensor on a machine with

another antivirus program, you do not need to enable the


option to have an installer file with the signatures included.


Note


Sensor admin L1 users can download a group-specific


installation package for groups specified in their user

settings from the **System > Sensors** screen.


The installer files use the following naming pattern:

```
 ActiveProbe_22_1_7_0_<Org_Name>_<Server_

 URL>_443_ACTIVE_NORMAL.exe(Windows)/.pkg

 (Mac)/.rpm(Linux)

```

The file name contains all necessary information to configure the

Cybereason sensor:


Sensor version

Organization name


Cybereason Detection Server server IP/DNS address

Server port (default is 443)


Default collection state (ACTIVE_NORMAL is the default)


Sensors that run on Windows machines include EDR and NGAV


components. By default, NGAV features are disabled, no drivers

are installed on the kernel, and the sensor runs in user space only.


If you enable features that require drivers ( **Anti-Malware >**
**Signatures**, **Anti-Malware > Artificial Intelligence**, and


Application Control) drivers that support these features are

installed on the kernel automatically.

## Step 3: Uninstall existing antivirus if


If you are using the Cybereason sensor to replace an existing

antivirus program, the Cybereason platform's **Anti-Malware >**


**Signatures mode** cannot function properly alongside another

antivirus. Before enabling **Signatures mode**, uninstall any existing


antivirus tools on the endpoints and reboot the endpoint machine

to completely remove these tools from the endpoint machine's


memory.


Note


Cybereason works together with the Windows Security Center.

In some cases, Windows Defender is disabled automatically


when the **Anti-Malware > Signatures mode** is enabled. In

other cases, Windows Defender is not disabled automatically 

for example, on Windows Server 2016, Windows 7 (in some

cases), or if Windows Defender was enabled via Group Policy.


Also, components of Windows Defender such as antispyware

may remain enabled even if its antivirus component is


disabled.


Therefore, Cybereason highly recommends to disable


Windows Defender manually before enabling the **Signatures**

mode.


Other Endpoint Protection features can run alongside any

existing antivirus, including Windows Defender. Therefore, if


**Anti-Malware > Signatures mode** is disable, Windows

Defender is not disable automatically.

## Step 4: Install the sensor using the


You install the sensor for Windows across your organization by
running the installer file in the command line, using a software


distribution tool.


Note


For installation on single machines, you can open the installer
file on the endpoint and install the sensor using the installation


wizard. This may be useful for testing purposes, but is not

practical for large scale deployment.


Use the following syntax to install the sensor and specify sensor

settings using the Windows command line:

```
 <installer file name> /install /quiet

 /norestart -l <LogFilePath> /v

 "InstallFolder="C:\MyInstallDirectory""

 <installation parameter>=<installation

 parameter value>

```

Note


You must have administrative privileges to run the installation


command.


This command includes the following parameters:








|Command|Description|
|---|---|
|**<installer fle**<br>**name>**|The name of the installer fle used to<br>install the sensor.|
|**/install**|Installs the fle.|


|Command|Description|
|---|---|
|**/quiet**|Indicates to not show any prompts during<br>the installation process.|
|**/norestart**|Instructs the sensor to not restart while<br>the command is running.|
|**-l**|Creates a log fle.|
|**<LogFilePath>**|The path to the log fle.|
|**/v**<br>**"InstallFolder="**<br>**<different install**<br>**folder>""**|An optional command that installs the<br>sensor in a different folder than the<br>default folder.<br>Note<br>If the folder path includes spaces,<br>you must escape the spaces with<br>quotes to prevent the command from<br>failing. For example:**/v**<br>**"InstallFolder="C:Program" Files"**.|



For example, if you added all the parameters above, you would

have the following command:

```
 <installer file name> /install /quiet

 /norestart /v "InstallFolder="

 <installation folder>"" -l <log file

 path>

```

You can optionally set installation parameters to customize sensor

features. Installation parameters override sensor personalization


settings in a custom sensor package you receive from Technical

Support and settings adopted from the assigned security policy.


[See Supported sensor installation parameters (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

[base?article=24-1-sensor-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


[parameters&language=en_US#supported-sensor-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)

[parameters) for a list of installation parameters.](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-installation-parameters&language=en_US#supported-sensor-installation-parameters)


Important


When installing the sensor via SCCM, command line, or other


third-party deployment tools, and when using GPO, do not set

the **ALLUSERS=1** (per machine installation context), as this


can cause issues with sensor upgrades. This flag should


The Cybereason platform installs the sensor to the **C:Program**

**FilesCybereasonActiveProbe** and **C:Cybereason Execution**


**Prevention** folders.


Depending on whether you select the option to install the sensor


with the signatures database or not, the result is different:






|Signatures<br>database<br>included<br>(Windows<br>only)|When you run the installer file, the installer also<br>installs the signatures database file as well as<br>the sensor. You can optionally move the<br>signatures database zip file to a different<br>location (e.g to a shared network drive where it<br>is available for multiple machines). If you do<br>this, you must specify the full path to this file<br>using the AV_SIGNATURE_PATH installation<br>parameter. If this parameter is not specified, the<br>exe and signatures files must be located in the<br>same folder during installation.|
|---|---|
|No<br>signatures<br>database|If you select the installer fle without signatures,<br>after you enable**Anti-Malware > Signatures**<br>**mode**, the sensor automatically downloads the<br>signatures database (~300 MB) from the NGAV<br>Global or Local Update server. This download<br>happens within 15 minutes of installation and<br>can take several minutes to complete,<br>depending on network speed. While the frst<br>time update is in progress, Anti-Malware does<br>not protect the machine. After it completes, the<br>machine is protected, and if the end user<br>hovers over the Cybereason system tray icon,<br>the status**Your PC is protected** displays.|



After installation, a Cybereason icon appears on the end user's


system tray, and desktop notifications appear if malware is
[detected/prevented. See System tray icon and notifications](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-and-notifications)


[(/s/knowledge-base?article=24-1-endpoint-machine-notifications-](https://nest.cybereason.com/s/knowledge-base?article=24-1-endpoint-machine-notifications-and-desktop-settings&language=en_US#system-tray-icon-and-notifications)



