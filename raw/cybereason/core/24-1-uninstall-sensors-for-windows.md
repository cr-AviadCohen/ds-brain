**To uninstall an online sensor from the Sensors screen, follow**


**these steps:**


1. In the **System > Sensors** screen, select the online sensors to


uninstall.

2. Above the sensors list, click **Actions** and select **Uninstall** :


3. In the **Uninstall** dialog box, click **Yes, uninstall** .


The Cybereason platform then runs the command on the machine


to uninstall the sensor.


After the sensor uninstalls, in the **Sensors** screen, the uninstalled


sensor displays grayed out (like an offline sensor), and the **Last**

**update status** column displays **Uninstall initiated** .

## Uninstall sensors from multiple machines
## (appropriate for mass deployments)


To uninstall sensors from multiple machines, run the following

command:


**On Windows versions earlier than Windows 11 24H2:**


```
 wmic process call create "cmd.exe /c for

 /r \"%programdata%\Package Cache\\" %a

 in (cybereasonsensor.exe) do if exist %a

 %a /uninstall /quiet /norestart

 AP_UNINSTALL_CODE=\"<password>\""

```

**On Windows versions Windows 11 24H2 and later:**


Note


On Windows 11 24H2 and later, Microsoft has discontinued


support for WMIC commands, so you must use PowerShell to

uninstall the sensor.

```
 Get-ChildItem -Path

 "$env:ProgramData\Package Cache" 
 Recurse -Filter "cybereasonsensor.exe" |

 ForEach-Object {& $_.FullName /uninstall

 /quiet /norestart AP_UNINSTALL_CODE="

 <password>"}

```

Note


If this command is executed without administrator privileges,


the machine's end user will be required to answer "Do you

want to allow this app to make changes to your device?.


If an uninstall password is required, replace <password> with the

password. To obtain this password, contact Technical Support.


Place the password between escaped quotes as shown above. If

no uninstall password is required, do not use the


AP_UNINSTALL_CODE="<password>" flag.

## Uninstall sensors from individual


Use one of the following options:


1. Use the Add/Remove Programs option in the operating


system to remove the Cybereason sensor program.


2. Run this command as an administrator:


```
   <file name> /uninstall /quiet

   /norestart -l <log file>

   AP_UNINSTALL_CODE="<password>"

```

In this example:


**<file name>** is the name of the installer file used to install

the sensor. Verify that it is the same version as the sensor


you are uninstalling.

**/uninstall** is the command to uninstall the sensor


**/quiet** is the command to not show any prompts

**/norestart** is the command to not restart the machine in


situations where a restart is normally required.
**-l** is the command to create a log file


**<password>** is the uninstall password if required. To

obtain this password, contact Technical Support. Place


the password between quotes as shown above. If no

uninstall password is required, do not use the


AP_UNINSTALL_CODE="<password>" flag.

For the MSI uninstall command for sensor versions older than


18.0, see the specific version's documentation.


Cybereason recommends that you check the uninstallation


logs to verify a machine restart is not required, as there are

cases where a manual restart of the machine is required.


Note


When uninstalling a sensor, the Windows Restart Manager


reports errors during the uninstallation. You can safely ignore

these errors.

## Uninstall using an passkey file


You can uninstall multiple sensors using an passkey file. You can
generate this file from the **Actions** menu in the **Sensors** screen.


You copy the file to endpoint machines can run the file on
endpoints and it is capable of uninstalling both online and offline


sensors without requiring the uninstall password.


Note


This feature is available for early access in version 23.2.4 and

later and is generally available in version 23.2.148 and later. In


[versions earlier than 23.2.148, open a Technical Support](https://nest.cybereason.com/s/support)

[(/s/support) case to enable this feature.](https://nest.cybereason.com/s/support)


**To uninstall a sensor with a passkey file, follow these steps:**



