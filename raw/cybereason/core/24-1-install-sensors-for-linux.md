|Installation option|Details|
|---|---|
|Install Full Stack and Replace<br>3rd Party Antivirus|You can use the Cybereason<br>sensor as a full endpoint<br>protection tool that replaces<br>your existing antivirus tool.<br>Used in this way, Cybereason<br>provides a full stack of<br>endpoint protection and EDR<br>functionality.<br>With this type of installation,<br>you must remove the third-<br>party antivirus from the<br>machine.|


|Installation option|Details|
|---|---|
|Install Alongside 3rd Party<br>Antivirus|If you do not wish to replace<br>your existing antivirus tool,<br>you can install the<br>Cybereason sensor alongside<br>it on your endpoints. Used in<br>this way, Cybereason<br>complements your existing<br>tool with additional endpoint<br>protection and EDR features.<br>With this type of installation,<br>you can enable all<br>Cybereason features, except<br>for the Anti-Malware ><br>Signatures mode feature,<br>which must remain disabled.|


Note





You do not need to perform the deployment steps described

in this section after you upgrade a sensor to a new


Cybereason version. These steps are only required during

initial sensor installation.


[For a list of Linux sensor processes, see Linux sensor processes](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-architecture&language=en_US#linux-sensor-processes)

[(/s/knowledge-base?article=24-1-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-architecture&language=en_US#linux-sensor-processes)


[architecture&language=en_US#linux-sensor-processes).](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-architecture&language=en_US#linux-sensor-processes)


In this topic:


Create and configure sensor policies and groups

Create and configure sensor security policies


Create and configure sensor groups

Install required packages


Set up a proxy on Linux machines

Deploy sensors for Linux


Verify the sensor for Linux is running

Users and sensors for Linux


Stop sensors for Linux

Uninstall Linux sensors from the Sensors screen


Uninstall sensors from individual Linux machines

Known limitations - sensors for Linux


Related resources


## Create and configure sensor policies and

## Create and configure sensor security

Cybereason recommends configuring sensor policy settings


before installing sensors. Configure these settings from the

**System > Policy management** [screen. See Sensor Policies](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


[(/s/knowledge-base?article=24-1-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)

[policies&language=en_US#sensor-policies) for guidance.](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


When working with a Linux sensor that is assigned a policy where

**Anti-Malware > Signatures mode** is enabled, scheduled and on


demand scans run automatically according to policy settings. No
specific deployment steps are required.


Important


To avoid accidental scans of Linux sensors, Cybereason


recommends that you do not assign Linux sensors the same

policy as Windows or Mac sensors. When sensors from


multiple operating systems are assigned the same policy,

enabling the AV Signatures mode feature automatically


enables Linux AV and triggers AV operations on each of the

supported operating systems.


To improve performance of Anti-Malware on access file scans on

Linux machines, network drives and mount points are excluded.


Once you install sensors, the sensors receive the settings in your

assigned policies.

## Create and configure sensor groups


If you choose to use sensor groups, you can create sensor groups

before installation and assign sensors automatically upon


installation in one of the following ways:

Download the group-specific installation package. The group

specific installation packages assign the sensor to a specific

sensor group when installed.


Add logic to the group to automatically assign certain sensors
[to a specific group on installation. See Create group](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)


[assignment logic (/s/knowledge-base?article=24-1-manage-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)

[sensor-groups&language=en_US#create-group-assignment-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)


[logic) for instructions on creating assignment logic.](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#create-group-assignment-logic)


Note


Sensors installed with a group-specific installation package

will ignore sensor grouping logic.


## Install required packages

Note


The Cybereason Linux sensor packages are not supported for

Linux 32-bit operating systems.


Before you install the Cybereason Linux sensor package on Linux

operating systems, verify that the following languages and


packages are installed on the endpoint.


For more details on how to find and install missing packages and


[a script to check that all dependencies are installed, see How to](https://nest.cybereason.com/s/article/8289406)

[Check and Install Missing Packages for Linux Sensor Installations](https://nest.cybereason.com/s/article/8289406)


[(/s/article/8289406).](https://nest.cybereason.com/s/article/8289406)












|Language/Package/Utility|Notes|
|---|---|
|Python 2.6+ or Python 3.x|The Cybereason platform<br>supports all Python 3<br>versions, up to the latest<br>Python version.|
|iptables|Required for machine<br>isolation to work.|
|libcurl.so.4||
|libnsl.so.1|If you experience installation<br>issues on RHEL or CentOS<br>8.3 or 8.4, see Sensor Fails to<br>Start on RHEL 8 Distributions<br>(/s/article/2943473).librt.so.1|
|librt.so.1||
|libpthread.so.0||
|libm.so.6||
|libgcc_s.so.1||
|libc.so.6||
|ld-linux-x86-64.so.2||
|libdl.so.2||
|libpopt.so.0||
|libelf.so.1||


|Language/Package/Utility|Notes|
|---|---|
|libattr.so.1||
|libz.so.1||
|libudev.so.1|This library is part of the<br>**systemd** package supported<br>on CentOS 7 and later|
|libcap.so.2|Enables retreiving and setting<br>Linux capabilities|
|librpm.so (https://librpm.so)|Allows RPM metadata<br>enrichment for the supported<br>operating system. Applicable<br>for RPM-based Linux<br>distributions.|
|librpmio.so<br>(https://librpmio.so)|Allows RPM metadata<br>enrichment for the supported<br>operating system. Applicable<br>for RPM-based Linux<br>distributions.|
|gdb|Required for Debian only -<br>Allows maximum debugging<br>capabilities. Recommended<br>for all Linux operating<br>systems.<br>**WARNING:** The Cybereason<br>sensor can function without<br>the**gdb** package but will<br>have reduced debugging<br>capabilities. We recommend<br>installing the**gdb** package to<br>enable these capabilities.|
|policycoreutils-devel|Required (CentOS/RHEL 7.6-<br>7.9, Ubuntu 20.04/22.04)) to<br>use the eBPF framework. See<br>the table below for steps to<br>perform for the eBPF<br>framework.|


## Set up a proxy on Linux machines

Sensors on Linux machines detect if there is a proxy defined on


the machine. If the sensor detects a proxy, the sensor connects to

the Registration/Detection servers via the proxy.


If you need to set up a proxy for a Linux machine, ensure you


create this before the sensor installation. For information on how to

[set up the proxy, see Add a proxy connection on Linux machines](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-proxy-connection-details&language=en_US#add-a-proxy-connection-on-linux-machines-using-automatic-detection)


[using automatic detection (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-proxy-connection-details&language=en_US#add-a-proxy-connection-on-linux-machines-using-automatic-detection)
[configure-proxy-connection-details&language=en_US#add-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-proxy-connection-details&language=en_US#add-a-proxy-connection-on-linux-machines-using-automatic-detection)


[proxy-connection-on-linux-machines-using-automatic-detection).](https://nest.cybereason.com/s/knowledge-base?article=24-1-configure-proxy-connection-details&language=en_US#add-a-proxy-connection-on-linux-machines-using-automatic-detection)


Note


Proxy creation is not done as part of the command line

installation for the sensor installation.


1. In the **System > Overview** screen, download the Linux

installer file:


a. Select **Download Cybereason Installers** . The installation


options pane appears.


b. Select a sensor group. The group-specific installation

packages assign the sensor to a specific sensor group


when installed.

c. Select the appropriate Linux package.


Note


Sensor admin L1 users can download a group-specific


installation package for groups specified in their user

settings from the **System > Sensors** screen.


2. Run the following command to install the Cybereason sensor:


**On CentOS/RHEL/Oracle Linux/Amazon Linux:**

```
   sudo rpm -ivh <RPM file>

```

**On Ubuntu/Debian:**

```
   sudo dpkg -i <deb file>

```

Note


All Linux operating systems require Python 2.6+ or Python

3.0+ to be installed. For a full list of Linux installation


[requirements, see Install required packages (Linux)](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)


[(/s/knowledge-base?article=24-1-pre-installation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)


[requirements-and-instructions&language=en_US#install-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)

[required-packages-linux).](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#install-required-packages-linux)


On the machine, the sensor installs to the

**/opt/cybereason/sensor** folder.


Important


The sensor only works from the above directory. Changing the


directory causes the sensor to stop functioning.

## Verify the sensor for Linux is running


Run the following command:


**On CentOS 7/RHEL 7/Oracle Linux 7, 8, 9/Ubuntu 16 LTS or**

**later:**

```
 systemctl status cybereason-sensor

```

**On CentOS 6/RHEL 6/Oracle Linux 6/Amazon Linux/Ubuntu 14**

**LTS:**

```
 initctl status cybereason-sensor

## Users and sensors for Linux

```

The sensor runs as a new user (cybereason) and group

(cybereason), which is automatically created by the sensor


installer. The 'cybereason' user enables the sensor to run with the

minimum required privileges, instead of running as the root user.


Some privileges are necessary for the sensor to perform functions,
such as collecting data from privileged locations of the file system.


To allow this, the sensor process starts as the root user in order to

acquire root capabilities, but then switches to the 'cybereason'


user while retaining a minimal subgroup of these capabilities. The

process itself can access privileged locations, but the


'cybereason' user cannot.


The 'cybereason' user is created without a home directory and


without shell access to prevent login and remote command

execution. This user is not part of the sudoers list and has no


special privileges.


Using the 'cybereason' user is preferable and is sufficient for all


functional requirements. If for some reason you require the sensor

to run as the root user instead, contact Technical Support to make


this change, as it requires a change in the package configuration.

## Stop sensors for Linux


On the machine, run the following command:


**On CentOS 7/RHEL 7/Oracle Linux 7, 8, 9/Ubuntu 16 LTS or**


**later:**

```
 sudo systemctl stop cybereason-sensor

```

**On CentOS 6/RHEL 6/Oracle Linux 6/Amazon Linux/Ubuntu 14**


**LTS:**

```
 sudo initctl stop cybereason-sensor

## Uninstall Linux sensors from the Sensors

## screen

```

You can uninstall sensors from the **Sensors** screen.


**To uninstall a sensor from the Sensors screen, follow these**

**steps:**


1. In the **System > Sensors** screen, select the sensors to


uninstall.


2. Above the sensors list, click **Actions** and select **Uninstall** :


3. In the **Uninstall** dialog box, click **Yes, uninstall** .


The Cybereason platform then runs the command on the machine


to uninstall the sensor.


After the sensor uninstalls, in the **Sensors** screen, the uninstalled


sensor displays grayed out (like an offline sensor), and the **Last**

**update status** column displays **Uninstall initiated** .

## Uninstall sensors from individual Linux


To uninstall sensors on Linux endpoints, run the following

command:


**On CentOS/RHEL/Oracle Linux/Amazon Linux:**

```
 sudo rpm -e cybereason-sensor

```

**On Ubuntu:**

```
 sudo dpkg -r cybereason-sensor

```

Note


If you have trouble uninstalling, check that the relevant files

[and processes listed in the Add sensor processes to third-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)


[party tool allowlists (all OSs) (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)

[pre-installation-requirements-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)


[instructions&language=en_US#add-sensor-processes-to-third-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)

[party-tool-allowlists-all-oss) tables are not being blocked by](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)


any third-party antivirus tools.

## - Known limitations sensors for Linux


The following are known limitations for Linux installation tasks.


Presently, you cannot run the sensor in a environment using

Python 3.12.


The Linux sensor does not create a core dump if gcore is not

installed on the machine.


Cybereason does not support the use of command line

installation parameters when installing Linux sensors.



