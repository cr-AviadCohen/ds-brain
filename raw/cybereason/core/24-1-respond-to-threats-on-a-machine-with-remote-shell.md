## When should you use the Remote Shell?


The Remote Shell utility enables analysts to perform a set of live

actions on a machine with a Cybereason Sensor to assist in


response and remediation of malicious activity. This utility can also

be used for investigation on a single machine.


The utility aims to improve the work process around three main

security areas in the incident lifecycle:


**Triage:** When planning the response or remediation

necessary for a MalOp, sometimes details are missing around


the relevance of a MalOp or information about the Elements

included in the MalOp. This utility enables you to access


machines involved in the MalOp and collect those details.

**Remediation:** The utility provides analysts additional


response capabilities along with existing, out-of-the-box

remediation features. For example, with the Remote Shell


utility you can remove a service associated with malicious

activity from the registry and in the service database.


**Investigation:** While you are investigating malicious activity,


you may feel you need additional context around an incident.

Use this utility to discover and collect additional information on


a machine. In addition, you can collect information on a

machine that is not consumable as processes data in the


Cybereason platform, such as registry data for non-autorun

entries.


This feature is disabled by default. Contact Technical Support to
configure your server and Sensors to support this feature.

## Remote Shell utility requirements


To use the Remote Shell utility, you must meet the following

requirements:






|Requirement|Details|
|---|---|
|Operating<br>system|A sensor installed on a machine running<br>Windows 7 or higher or any supported<br>version of Linux.|
|Required<br>packages|If you use the Remote Shell on a Linux<br>machine, ensure that**/bin/bash** is installed on<br>the machines.|
|PowerShell<br>version|The Remote Shell utility supports different<br>PowerShell versions depending on the<br>Remote Shell mode you select.<br>If you use**Secure** mode, you must have<br>PowerShell version 5.1 or higher on the<br>machine where the sensor is installed.<br>For some Windows operating systems,<br>the default PowerShell version is earlier<br>than 5.1. If your default PowerShell<br>version is earlier than version 5.1,<br>perform a manual upgrade to PowerShell<br>5.1 or a later version.<br>If you use**Unrestricted** mode, you can<br>use PowerShell version 2 and later.|


|Requirement|Details|
|---|---|
|Cybereason<br>role|A user admin must assign you one of the<br>proper roles:<br>**Responder L1**<br>**Responder L2**<br>**Local Responder** and**Local Analyst**<br>roles (available in environments with<br>sensor grouping enabled).<br>If you remove the relevant Responder role for<br>a user, this update takes effect only after the<br>Remote Shell utility session ends.<br>Users with the**System Admin** role can view<br>the logs containing the PowerShell<br>commands and responses.|
|Sensor<br>Confguration|Update the sensor using these steps:<br>1. Contact Technical Support to set the<br>Remote Shell confguration on your<br>server and sensors and enable<br>**Unrestricted** mode if needed.<br>2. Set the**Set remote shell mode** option in<br>the**Assets > Endpoints** screen for each<br>machine on which you want to use the<br>Remote Shell utility.|
|Network<br>connection|Ensure that your network is not a public<br>network. Due to PowerShell limitations,<br>restricted Remote Shell does not work if your<br>network is set to a**Public** network.|


Note




If you perform any updates for a user, such as changing their


role or enabling Remote Shell for the server or for a sensor, the

user must refresh their browser window to see the Remote


Shell button and use the Remote Shell utility.


As the Remote Shell feature enables you to perform operations


directly on a machine in your environment and change information

on that machine, Cybereason has added certain safeguards to


ensure your machines, servers, and environment are kept safe

from inappropriate use of the utility.






|Safeguard|Description|
|---|---|
|Confguration|When preparing your sensors and server to<br>use the Remote Shell utility, confgure the<br>following items:<br>Technical Support must confgure your<br>sensors and server to use the Remote<br>Shell.<br>When working with Technical Support, if<br>there are machines with Cybereason<br>sensors on which you do not want the<br>Remote Shell to access, Technical<br>Support can exclude the sensor setting<br>change on these machines or you can<br>manually disable this option in the<br>**Assets > Endpoints** screen.<br>You must also confgure access to<br>each sensor from the**Assets >**<br>**Endpoints** screen.|
|User Access|Only the users with the**Responder L1**,<br>**Responder L2**, or**Local Responder/Local**<br>**Analyst** roles have access to the Remote<br>Shell utility.|
|Command<br>Usage|In**Restricted** mode, the number of<br>commands you can use is limited.|
|Machine<br>Access from<br>the Cybereason<br>UI|If you perform any browser action while in a<br>tab showing the Cybereason UI or have a<br>period of inactivity, the connection between<br>the Cybereason server and the machine is<br>immediately terminated.|


## Assign the Responder role

Before you begin, ensure that a user admin for your Cybereason


platform assigns one of the following roles:


**Responder L1**


**Responder L2**

**Local Responder** AND **Local Analyst** (available in


environments with sensor grouping enabled)


Note


You cannot assign both the **Local Responder** or **Local**

**Analyst** roles and **Responder L1/L2** role to one user.


Additionally, users with the **Local Responder** role must also

have the **Local Analyst** role assigned so they can access the


screens needed to start a Remote Shell session.


User admins must enable Two-factor authentication (TFA) for to


use the Remote Shell utility in **Unrestricted** mode.


Note


If your Cybereason user account is set to use SSO, the option

to enable two-factor authentication (TFA) is not available.

## Use the Remote Shell utility


You can access the Remote Shell utility from the **Malop Details** or

**Element Details** screens. The utility uses its own windows which


open a shell interface on the selected machine. This utility tries to

replicate the user experience of the PowerShell IDE that is


commonly used for incident response.


1. Ensure that the Remote Shell utility is enabled on your servers


and sensors. Contact Technical Support to set the Remote
Shell configuration for your server and make sure you enable


the Remote Shell on individual sensors in the **System >**

**Sensors** screen.


Note


If you want to use **Unrestricted** mode for Remote Shell,


you must first enable Remote Shell utility and then enable

Unrestricted mode separately. Open a support ticket with


Technical Support to enable the Remote Shell utility and

Unrestricted mode.


2. Log out and log in to the Cybereason platform using two

factor authentication.


3. If needed, isolate the machine for remediation. For details on


[isolation, see Isolate Machines (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-isolate-machines&language=en_US#isolate-machines)

[article=24-1-isolate-machines&language=en_US#isolate-](https://nest.cybereason.com/s/knowledge-base?article=24-1-isolate-machines&language=en_US#isolate-machines)


[machines).](https://nest.cybereason.com/s/knowledge-base?article=24-1-isolate-machines&language=en_US#isolate-machines)

4. In the **Malop Details** or **Investigation** screens, click **Remote**


**Shell** .


5. In the Remote Shell utility dialog box, in the dropdown list,


select the machine.


An individual machine with a sensor can have one Remote


Shell connection active at a time. However, as an analyst on

the Cybereason platform, you can open multiple Remote Shell


utility sessions for multiple machines.


Note


Offline machines are greyed out in the dialog.


6. At the bottom of the dialog, in the **Select the Remote Shell**


**mode** section, select the mode to use:


7. If you selected **Unrestricted** mode, enter your two-factor


authentication code.


Note


If your user administrator has enabled SSO for your user


account, you do not need to enter a two-factor
authentication code and the field to enter the two-factor


authentication mode does not display.


8. The Remote Shell command line utility opens:


Note


Depending on your available network bandwidth, the start


of the Remote Shell session on the machine may take a

few seconds. In environments with low bandwidth, this


session start may take more than 15 seconds.


By default, the command line begins at **C:** .


If there are errors, view the error message at the top of the

Remote Shell window for details.


9. Enter PowerShell commands as needed to perform


remediation and investigation.


When running the Remote Shell utility in Restricted mode, you

can run only selected commands. For details on the


[supported commands, see Supported Commands for Remote](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-commands-for-remote-shell&language=en_US#supported-commands-for-remote-shell)


[Shell (/s/knowledge-base?article=24-1-supported-commands-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-commands-for-remote-shell&language=en_US#supported-commands-for-remote-shell)


[for-remote-shell&language=en_US#supported-commands-for-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-commands-for-remote-shell&language=en_US#supported-commands-for-remote-shell)

[remote-shell).](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-commands-for-remote-shell&language=en_US#supported-commands-for-remote-shell)


When running the Remote Shell utility in unrestricted mode,

you can run any commands.


Your Cybereason WebApp server saves a record of all

commands used and responses to the server logs. Users with


the **System Admin** role can retrieve these logs after a session

is complete. Sensor logs note any connections to the machine


from the Remote Shell utility and system changes such as file
modification, etc.).


Note


The commands and logs of the commands are not


localized.


On some Linux operating systems, certain **CTRL +** operations


(such as **CTRL-C**, **CTRL-V** and so forth) are not supported for

use with the Remote Shell utility that runs in your browser.


Your server also adds the Remote Shell session to the syslog.
10. After you have finished, click **End Session** to disconnect from


the utility. The connection displays as offline and you can

navigate to other parts of the Cybereason UI as needed.


If you perform other common browser operations, such as

closing the browser tab or window, navigating to the previous


screen or a different URL, or navigating to another part of the

Cybereason UI, your Cybereason server prompts you if you


want to end the session.

11. If the machine or utility loses connection during the session,


click **Reconnect** to reestablish the connection. You must

manually initiate the reconnection as your Cybereason server


will not automatically try to reconnect.


If the session ends due to a network disconnection, it may


take up to 5 minutes to reestablish a new session with the
specific machine.


Note


If there is no activity on the Remote Shell utility for 5


minutes, your Cybereason server ends the Remote Shell

utility session.

## Remote Shell utility window


The Remote Shell utility window provides many options to assist


your remediation efforts. Use any of these options to help

investigate on a given machine:






|Area|Description|
|---|---|
|Status bar|Details on the session include the name of<br>the machine to which the utility connected<br>and the status of the connection and utility.<br>You can click the machine name in the<br>status bar to close or reopen a session.|
|Command line<br>interface|The area to enter commands to run on the<br>remote machine.<br>This window supports standard PowerShell<br>command line shell text entry. In addition,<br>the utility enables you to cut and paste<br>commands from other windows on your<br>machine.<br>As you type and receive responses, the<br>utility saves the history of the commands<br>used and the responses. If the connection<br>to the machine stops, the utility keeps the<br>history until you reconnect and close the<br>window.|


|Area|Description|
|---|---|
|Element details|The Remote Shell window displays a<br>number of details about the machine and<br>the sensor, including:<br>Machine properties<br>Data on what is happening on the<br>machine. This includes the number of<br>users, processes, services, drivers,<br>registry entries, and logon sessions<br>currently on the machine.<br>Device properties for the machine<br>Sensor property information<br>This data refects data collected by your<br>Detection Servers, not the Remote Shell<br>utility.|
|Session<br>management<br>toolbar|Enables you to manage the remote session.<br>If the connection or the utility disconnects,<br>click**Reconnect** to try to reestablish the<br>connection.<br>Click**End Session** to end the session, close<br>the utility, and end the connection to the<br>remote machine.|


## Remote Shell usage errors

Since the Remote Shell utility uses a remote connection from your

Cybereason server to a machine, you may encounter errors when


using this utility. The utility displays these errors in the header of

the utility window, but use the workarounds to help you continue


working with the utility.








|Error|Cause|Workaround|
|---|---|---|
|Connection to<br>remote machine<br>unexpectedly<br>terminated|The sensor is not<br>connected to the<br>network|Ensure that your<br>sensor is running<br>correctly and<br>connected to your<br>network.|
|Remote<br>PowerShell utility<br>unexpectedly<br>terminated|The Remote Shell<br>utility crashed or<br>exited|Click**Reconnect** to<br>reestablish the<br>connection or<br>restart your sensor.|


|Error|Cause|Workaround|
|---|---|---|
|Failed<br>connecting to<br>remote machine|The Remote Shell<br>utility did not start|Click**Reconnect**<br>again.|
|The probe on<br>the remote<br>machine cannot<br>support the<br>requested<br>operation or<br>initialize the<br>connection|There are multiple<br>causes:<br>Your sensor is<br>an older sensor<br>version that<br>does not<br>support the<br>Remote Shell<br>version<br>The Remote<br>Shell feature is<br>disabled in the<br>sensor<br>confguration|Do one of the<br>following<br>depending on the<br>issue:<br>Upgrade your<br>sensor to the<br>newest version<br>Contact<br>Technical<br>Support for<br>assistance in<br>sensor<br>confguration.|
|The Remote<br>machine is<br>unreachable|The Remote Shell<br>utility could not<br>connect to the<br>sensor machine|Verify that your<br>sensor is running<br>correctly and<br>connected to the<br>network.|
|Session already<br>open against<br>this endpoint|The sensor already<br>has an active<br>Remote Shell utility<br>session open for the<br>machine|Wait until the<br>previous session<br>fnishes and try<br>again.|
|Internal server<br>error|The server<br>encountered an<br>error opening up a<br>Remote Shell<br>session to the<br>machine|Click**Reconnect** to<br>reestablish the<br>session.|
|Remote Shell<br>utility screen<br>closed after 5<br>minute threshold<br>of inactivity|There was no<br>interaction between<br>your Cybereason<br>server and the<br>Remote Shell utility<br>for at least fve<br>minutes|Click**Reconnect** to<br>reestablish the<br>connection.|



