|Behavior|Indicators|
|---|---|
|Host<br>enumeration|Attackers can perform host enumeration with<br>many commands. These differ between each<br>operating system, but include:<br>**Windows:** _whoami //all_, _net user_,<br>_hostname_, _ipconfg_<br>**Mac and Linux:** _whoami_, _id_, _hostname_,<br>_ifconfg_<br>This is not an exhaustive list of all<br>commands, but these are commonly used.|
|Network<br>enumeration|Like host enumeration, network enumeration<br>uses some basic commands on each<br>operating system:<br>**Windows:** _net view_, _netstat_, _netuse_<br>**Mac and Linux:** _mount_, _netstat*_|
|Process<br>enumeration|Attackers also use commands for process<br>enumeration, which differ on each operating<br>system:<br>**Windows:** _net start_, _sc query_, _tasklist_,<br>_schtasks //query_, _at_<br>**Mac:** _launchctl list_, _ps -A_, _crontab -//_<br>**Linux:** _service -status-all_, _initctl list_, _ps -_<br>_A_, _crontab -//_|



From these indicators, we can now explain exactly for what we

want to search:


1. We want to find evidence of commands performing host


enumeration.


2. We want to find evidence of commands performing network


enumeration.


3. We want to find evidence of commands performing process


enumeration.


4. We want to find evidence of processes performing network


scanning.


5. We want to find evidence of user activity at irregular times of


the day.

## Step 3: Construct hunting queries


Use the statements above to construct queries.

1. **Statement 1:** We want to find evidence of commands


performing host enumeration.


Because of our indicators of host enumeration use


commands, we will use the **Command line** feature filter on the
**Process** Element. This filter enables you to specify text used


in the command line of a process and then search for this text.


Since the commands are different for Windows operating


systems and Mac/Linux operating systems, we will need to

run separate queries for the different operating systems. We


add the Machine Element first to ensure that the query only

returns results from a certain operating system.


You construct these queries:


**Machine** Element -> Filter for OS Type is _Windows_ THEN


**Processes** Element -> Filter for Command line contains

_whoami// all_ OR _netuser_ OR _hostname_ OR _ipconfig_


**Machine** Element -> Filter for OS Type is _Mac_ OR _Linux_ THEN


**Processes** Element -> Filter for Command line contains

_whoami_ OR _hostname_ OR _ifconfig_ OR _id_


2. **Statement 2:** We want to find evidence of commands


performing network enumeration.


Like for statement one, our indicators are the use of certain

commands. As a result, we will use the **Command line**


feature on the **Process** Element. We will again need to run

separate queries for the Windows operating systems and


Mac/Linux operating systems.


You construct these queries:


**Machine** Element -> Filter for OS Type is _Windows_ THEN


**Processes** Element -> Filter for Command line contains _net_


_view_ OR _netstat_ OR _netuse_


**Machine** Element -> Filter for OS Type is _Mac_ OR _Linux_


**Process** Element -> Filter for Command line contains _mount_


or _netstat_


3. **Statement 3:** We want to find evidence of commands


performing process enumeration.


Like the first two statements, we are using commands as the


indicator. We will use a similar query with the **Command line**
feature filter on the **Process** Element with separate queries for


Windows, Mac, and Linux.


You construct these queries:


**Machine** Element -> Filter for OS Type is _Windows_ THEN


**Processes** Element -> Filter for Command line contains _net_


_start_ OR _sc query_ OR _tasklist_ OR _schtasks //query_ OR _at_


**Machine** Element -> Filter for OS Type is _Mac_ THEN


**Processes** Element -> Filter for Command line contains


_launchctl list_ OR _ps -A_ OR _crontab -//_


**Machine** Element -> Filter for OS Type is _Linux_ THEN


**Processes** Element -> Filter for Command line contains


_service -status-all_ OR _initctl list_ OR _ps -A_ OR _crontab -//_


4. **Statement 4:** We want to find evidence of processes


performing network scanning.


In this case, we have a detection rule for network scanners

that will return any process thought to be performing activities


classified as network scanning or possibly associated with

network scanning.


You construct this query:


**Process** Element -> filter for Network Scanner is _True_


5. **Statement 5:** We want to find evidence of user activity at


irregular times of the day


For this, we must look at users to see activity on their


machines. On the **User** Element there is a filter for evidence

on **Irregular time of day activity** .


You construct this query:


**User** Element -> filter for Irregular time of day activity is _True_

## Step 4: Analyze your results


Now that you have the queries, you can run them. Analyze the


results that have been returned to see if any evidence of internal

reconnaissance is found.



