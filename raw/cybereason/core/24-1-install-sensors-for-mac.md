|Installation option|Details|
|---|---|
|Install Full Stack and Replace<br>3rd Party Antivirus|You can use the Cybereason<br>sensor as a full endpoint<br>protection tool that replaces<br>your existing antivirus tool.<br>Used in this way, Cybereason<br>provides a full stack of<br>endpoint protection and EDR<br>functionality.<br>With this type of installation,<br>you must remove the third-<br>party antivirus from the<br>machine.|


|Installation option|Details|
|---|---|
|Install Alongside 3rd Party<br>Antivirus|If you do not wish to replace<br>your existing antivirus tool,<br>you can install the<br>Cybereason sensor alongside<br>it on your endpoints. Used in<br>this way, Cybereason<br>complements your existing<br>tool with additional endpoint<br>protection and EDR features.<br>With this type of installation,<br>you can enable all<br>Cybereason features, except<br>for the Anti-Malware ><br>Signatures mode feature,<br>which must remain disabled.|



You can install the sensor on a single endpoint, or on multiple


endpoints using a software distribution tool.


Note


You do not need to perform the deployment steps described

in this section after you upgrade a sensor to a new


Cybereason version. These steps are only required during

initial sensor installation.


[For a list of Mac sensor processes, see Mac sensor processes](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-architecture&language=en_US#mac-sensor-processes)

[(/s/knowledge-base?article=24-1-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-architecture&language=en_US#mac-sensor-processes)


[architecture&language=en_US#mac-sensor-processes).](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-architecture&language=en_US#mac-sensor-processes)


In this topic:


Create and configure sensor policies and groups

Create and configure sensor security policies


Create and configure sensor groups

Deploy sensors for Mac


Enable Full Disk Access for macOS sensors

Additional installation steps for Mac AV


Verify the sensor for Mac is running

Upgrading to macOS Ventura and above


Disable/enable sensors for Mac

Uninstall macOS sensors from the Sensors screen


Uninstall sensors from individual macOS machines


Uninstallation script


Remove SSL Certificates (if needed)

Known limitations - Mac sensors


Related resources


## Create and configure sensor policies and

## Create and configure sensor security

Cybereason recommends configuring sensor policy settings


before installing sensors. Configure these settings from the

**System > Policy management** [screen. See Sensor Policies](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


[(/s/knowledge-base?article=24-1-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)

[policies&language=en_US#sensor-policies) for guidance.](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


Once you install sensors, the sensors receive the settings in your

assigned policies.

## Create and configure sensor groups


If you choose to use sensor groups you can create sensor groups

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


Perform the steps in this section for all Mac sensor installations. If

you intend to enable Mac AV now or in the future, you must


perform additional steps in the next section.


Note


If you are deploying sensors on macOS 12.3 (Monterey) and

the sensor version is lower than 22.1.124, you must ensure


that Python 2.7 is installed on the machine, as Python is no

longer provided with macOS beginning with macOS 12.3


(Monterey).


To install sensors on the Mac, you must accept the default port of


443.


During the installation, you may see a pop-up message asking for


further consent: "This package will run a program to determine if

the software can be installed". When you see this message, click


**Continue** .


**To install sensors on one or more endpoints using the**


**command line (recommended):**


1. In the **System > Overview** screen, download the .pkg


installer package:


a. Select **Download Cybereason Installers** . The installation


options pane appears.
b. Select a sensor group. The group-specific installation


packages assign the sensor to a specific sensor group

when installed.


c. Select the macOS package.


Note


Sensor admin L1 users can download a group-specific
installation package for groups specified in their user


settings from the **System > Sensors** screen.


2. Use a software distribution tool to install the .pkg installer


package on the endpoints.


Here is an example of an installation command:

```
 sudo installer -pkg /<path-to
 package>/<file name>.pkg -target /

```

For example, the file name can have the syntax

**ActiveProbe_21_2_100_0_example.cybereason.net_443_ACTI**


**VE_NORMAL.pkg** .


If you perform installation/upgrade using a software distribution


tool (e.g. Jamf Pro), it is possible to allow the software in advance
as part of the distribution flow via the TCC (Transparency,


Consent, and Control) profile. In addition, Cybereason

recommends adding permissions for full disk access to the TCC


profile.


In this scenario, the AV driver can be allowed without requiring


manual steps on the machine.


You may need to add the sensor driver to the allowlist using the


following Kernel/Team ID: GUNFMW623Y


**To install a sensor on a single endpoint using the installation**


**wizard:**


1. In the **System > Overview** screen, download the .pkg


installer package.


a. Select **Download Cybereason Installers** . The installation


options pane appears.
b. Select a sensor group. The group-specific installation


packages assign the sensor to a specific sensor group

when installed.


c. Select the appropriate Mac package.


Note


Sensor admin L1 users can download a group-specific
installation package for groups specified in their user


settings from the **System > Sensors** screen.


2. Open the .pkg installer package on the machine to start the


installation wizard.

3. Follow the wizard to complete installation.


Important


On the **Network Configuration** screen, select


**Registration service**, as shown in the following image.


On the machine, the sensor installs to the **/usr/local/cybereason**


folder

## Enable Full Disk Access for macOS

## sensors


This section includes additional steps required for installation and


operation of the sensor. These steps are required whether or not

you enable Mac AV or if you installed the sensor on a previous


macOS version, then upgraded the operating system.


You must also perform these steps after upgrading the


Cybereason sensor to this version.


Installation of the macOS sensor installs an AV driver, regardless


of if AV is enabled.


If you are deploying sensors via Jamf, you can perform the


[automated procedure in this article: macOS Deployment via Jamf](https://nest.cybereason.com/s/article/7745196)

[(/s/article/7745196) instead of the steps below.](https://nest.cybereason.com/s/article/7745196)


**After running the installer package, follow these steps to**


**enable full disk access for the Cybereason sensor application:**


1. Open **System Preferences** .


2. Click **Security and Privacy** .

3. Click the Lock icon to make changes.


4. In the **Privacy tab**, select **Full Disk Access** .

5. Open a new **Finder** window and press **command + shift + G**


to enter the sensor installation path.

6. Enter this path:


**/Library/PreferencePanes/ActiveProbe.prefPane/Contents/**

**MacOS** )


7. Drag all the contents of the MacOS folder, except **lib** files, to


the Full Disk Access list (see image below).


Important


In macOS versions Tahoe (26.1) and later, when you drag


and drop the contents of the macOS folder to the Full Disk

Access list, **you may not see it displayed in the Full**


**Disk Access list** and may think that your action has not

succeeded, but please be aware that your action has


succeeded and that it does exist there.


8. Ensure that all the four selected ActiveProbe items display


and are selected in the Full Disk Access list (see image

below).


9. Close the **System Preferences** window.


## Additional installation steps for Mac AV

Note


If you are using the Cybereason sensor to replace an existing

antivirus program, the Cybereason platform's **Anti-Malware >**


**Signatures mode** cannot function properly alongside another

antivirus. Before enabling **Signatures mode**, uninstall any


existing antivirus tools on the endpoints and reboot the

endpoint machine to completely remove these tools from the


endpoint machine's memory.


If you plan to enable Mac AV (Anti-Malware > Signatures mode)


now or in the future, perform the installation steps described under

Enable Full Disk Access for macOS sensors, and then perform the


steps in this section:


Note


The installation can take several minutes to complete. After

installation, it may take several minutes until the sensor


downloads the Signatures DB.


**To set up Anti-Malware (AV) for macOS machines, follow these**


**steps:**


1. Restart the machine.


2. Navigate to the **Anti-Malware** screen in your sensor policy.

3. In the **Anti-Malware** screen, enable Anti-Malware.


4. Set **Signatures mode** to **Disinfect** .


5. In the **System > Sensors** screen, verify the following statuses


for the sensor:


Sensor status: **Online**


Data collection: **Enabled**


Signatures mode: **Disinfect**


After you enable Anti-Malware and set the **Signatures mode**, the


sensor automatically downloads the signatures database (~300

MB) from the NGAV Global or Local Update server. This download


can take several minutes to complete, depending on network
speed. While first time update is in progress, Anti-Malware does


not protect the machine. After it completes, the machine is

protected.


The sensor automatically retrieves signature updates from the

Update server on a frequent basis. By default, signature updates


[occur every 15 minutes. For more information, see Ongoing](https://nest.cybereason.com/s/knowledge-base?article=24-1-install-sensors-for-windows&language=en_US#ongoing-signature-updates)

[signature updates (/s/knowledge-base?article=24-1-install-](https://nest.cybereason.com/s/knowledge-base?article=24-1-install-sensors-for-windows&language=en_US#ongoing-signature-updates)


[sensors-for-windows&language=en_US#ongoing-signature-](https://nest.cybereason.com/s/knowledge-base?article=24-1-install-sensors-for-windows&language=en_US#ongoing-signature-updates)

[updates).](https://nest.cybereason.com/s/knowledge-base?article=24-1-install-sensors-for-windows&language=en_US#ongoing-signature-updates)


Watch this video for a short demo of enabling Mac AV.

## Verify the sensor for Mac is running


To verify your sensor is running correctly, open a terminal with root


privileges and type the following command:

```
 ps -ax | 'CybereasonSensor$'

```

## Upgrading to macOS Ventura and above

If you are upgrading machines that have the sensor installed to


macOS Ventura or above, and you are not using an MDM to

[perform this upgrade, you must perform these Steps after](https://nest.cybereason.com/s/article/8455456)


[upgrade to Ventura or higher (/s/article/8455456).](https://nest.cybereason.com/s/article/8455456)

## Disable/enable sensors for Mac


On a machine, open a terminal with root privileges and enter the


following commands.


**To disable the sensor:**

```
 sudo launchctl unload -w

 "/Library/LaunchDaemons/com.cybereason.s

 ensor.plist

```

**To enable the sensor:**

```
 sudo launchctl load -w

 "/Library/LaunchDaemons/com.cybereason.s

 ensor.plist

## Uninstall macOS sensors from the

## Sensors screen

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

## Uninstall sensors from individual macOS


**To uninstall sensors on MacOS endpoints, follow these steps:**


1. On the machine, create an empty file named **cr_uninstall.sh** .

2. Copy the content of the script in the Uninstallation


script section and paste the content into the
**cr_uninstall.sh** file.


3. Save the file and remember the path to the file. Ensure the .sh

file is saved with LF line feed (or run dos2unix or similar tool


on it if not) to prevent a syntax error when running it on the

Mac machine.


4. Open a Terminal window, and run the following commands:

```
   chmod +x cr_uninstall.sh

```

```
sudo /bin/bash

/the_path_to/cr_uninstall.sh

```

Note


If you have trouble uninstalling, check that the relevant
[files and processes listed in the Add sensor processes to](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions)


[third-party tool allowlists (all OSs) (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions)

[article=24-1-pre-installation-requirements-and-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions)


[instructions) tables are not being blocked by any third-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions)

party antivirus tools.


Note


For sensors on endpoints running Big Sur and later, the


Cybereason platform does not install system extensions

as part of the sensor installation. When you uninstall the


sensor, you do not need to uninstall any additional

components or extensions.


## Uninstallation script

```
 #!/bin/bash

 if [[ $BASH != "/bin/bash" ]]; then

 echo "This script must be run as

 bash!"

 exit -1

 fi

 if [[ $EUID -ne 0 ]]; then

 echo "This script must be run as

 root!"

 exit -1

 fi

 function remove_daemon() {

 local daemon_label="$1"

 local

 daemon_plist_fpath="/Library/LaunchDaemo

 ns/""$2"

 if [ $(sudo launchctl list |

 grep -c "${daemon_label}") -gt 0 ]; then

 sudo launchctl unload -wF

 "${daemon_plist_fpath}"

 fi

 sudo launchctl remove

 "${daemon_label}" || true

 sudo rm -f

 "${daemon_plist_fpath}"

 return 0

 }

 function remove_driver() {

 local driver_bundle_id="$1"

 local driver_package_name="$2"

 osx_ver=$(sw_vers 
 productVersion | awk -F '.' '{print

 $1}')

 if [ ${osx_ver} -eq 10 ]; then

 # before macOS 11 Big Sur

 if [[ $(sudo kextstat -l -b

 "${driver_bundle_id}") ]]; then

 echo "- Removing BD

 driver"

 sudo kextunload -b

 "${driver_bundle_id}"

 fi

 fi

```

```
sudo rm -rf

"/Library/Extensions/${driver_package_na

me}"

return 0

}

# Sensor daemon

sensor_daemon_label="CybereasonSensor.ap

p"

sensor_plist_fname="com.cybereason.senso

r.plist"

# AV.sext daemon

av_sext_daemon_label="CybereasonAv.app"

av_sext_plist_fname="com.cybereason.av.s

ext.plist"

# AV.kext daemon

av_kext_daemon_label="CybereasonAvKext.a

pp"

av_kext_plist_fname="com.cybereason.av.k

ext.plist"

# BD driver

bd_driver_bundle_id="com.Bitdefender.iok

it.av"

bd_driver_package_name="IOKitBDAv.kext"

# Installed ActiveProbe version

ap_ver=$(defaults read

"/Library/PreferencePanes/ActiveProbe.pr

efPane/Contents/Info.plist" \

'CFBundleVersion' 2>&1 | egrep -v

'(defaults|CFBundleVersion)')

echo "Uninstalling ActiveProbe
"${ap_ver}" ..."

echo "- Removing ActiveProbe

daemons"

remove_daemon

"${sensor_daemon_label}"

"${sensor_plist_fname}"

remove_daemon

```

```
 "${av_sext_daemon_label}"

 "${av_sext_plist_fname}"

 remove_daemon

 "${av_kext_daemon_label}"

 "${av_kext_plist_fname}"

 # Removing BD driver

 remove_driver

 "${bd_driver_bundle_id}"

 "${bd_driver_package_name}"

 echo "- Removing ActiveProbe

 Preference Pane"

 sudo rm -rf

 "/Library/PreferencePanes/ActiveProbe.pr

 efPane"

 echo "- Cleanup logs, quarantine,

 packages and configuration"

 sudo rm -rf "/usr/local/cybereason"

 sudo

 /Applications/.DnsCollector.app/Contents

 /MacOS/DnsCollector -uninstall

 sudo rm -rf

 /Applications/.DnsCollector.app

 echo "Done."

## Remove SSL Certificates (if needed)

```

Cybereason certificates for Two-Way SSL communication are


imported to the System keychain. You can remove them using the

Keychain Access UI:


**To remove certificates using Keychain Access UI follow these**

**steps:**


Delete all items listed below by right-clicking the item and

selecting **Delete <item>** (Admin password will be requested):


Delete the private key (expand the > in the client certificate or

search for it in the 'Keys' list).


Delete the Client certificate.
Delete the CA certificate.


## - Known limitations Mac sensors

The following are known limitations for Mac sensors.



|Type|Details|
|---|---|
|Mac AV|Endpoint Protection<br>features including Anti-<br>Malware > Artifcial<br>Intelligence, Fileless<br>protection, and Anti-<br>Ransomware are not<br>supported.<br>Archive fle scanning (zip,<br>tar, rar, etc.) is not<br>supported.<br>There are no end user<br>alerts for<br>detected/prevented<br>malware (popup alerts on<br>the machine itself).<br>It is not possible to<br>enable Signatures mode<br>using an installation<br>parameter during sensor<br>installation.<br>Installation with the<br>signatures DB included is<br>not supported.<br>The installation can take<br>several minutes to<br>complete.<br>If your Mac system<br>settings prevent enabling<br>the Mac AV feature, the<br>**System > Sensors**<br>screen shows the<br>process as**Initializing**,<br>instead of issuing an<br>error. The**CrAv.log** fle<br>will show that there is an<br>issue loading the driver.|

## Related resources





[Mac sensor installation issues (/s/article/147)](https://nest.cybereason.com/s/article/147)


[MacOS deployment via JAMF MDM (/s/article/7745196)](https://nest.cybereason.com/s/article/7745196)

[Mac AV does not prevent malware after installation](https://nest.cybereason.com/s/article/1933808)


[(/s/article/1933808)](https://nest.cybereason.com/s/article/1933808)


[Uninstall Cybereason Sensors FAQ (/s/article/6139711)](https://nest.cybereason.com/s/article/6139711)


[Please see our Legal Disclaimer (/s/article/legal-disclaimer-third-](https://nest.cybereason.com/s/article/legal-disclaimer-third-party-web-sites)

[party-web-sites) on links to third party web sites.](https://nest.cybereason.com/s/article/legal-disclaimer-third-party-web-sites)



