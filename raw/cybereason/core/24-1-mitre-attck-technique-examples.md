**Process** Element -> filter for Parent from removable device is _True_


**Query 2:**


**Process** Element -> filter for Parent running from removable


device is _True_

## Execution: Command line interface


**Goal:** Find instances of a process running a command.


**Explanatory statement:** I want to find examples of <<a

command>> running in my environment.


Construct the following query:


**Process** Element -> filter for Command line contains ______


You can add any command used in the command line as the text

in this query.

## Persistence: Create Account


**Goal:** Find when a user creates a persistence mechanism through

account creation.


**Explanatory statement:** I want to find instances of account

creation that enable an attacker to maintain persistence on a


machine.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for Creation of a localgroup user


account is _True_


**Query 2:**


**Process** Element -> filter for Creation of a Localgroup remote user

account is _True_


**Query 3:**


**Process** Element -> filter for Creation of localgroup remote admin


account is _True_

## Defense Evasion: Masquerading


**Goal:** Find application masquerading as something else.


**Explanatory statement:** I want to find examples of a process
masquerading as a different type of application or file.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for Masquerading as a movie evidence

is _True_


**Query 2:**


**Process** Element -> filter for Masquerading as a Windows


accessibility feature evidence is _True_


**Query 3:**


**Process** Element -> filter for Malicious use of an OS process is


_True_

## Credential Access: Credential Dumping


**Goal:** Find when an attacker performs credential dumping.


**Explanatory statement:** I want to find examples of a process


performing a credential dump from different locations on a

machine.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for Registry credentials dump is _True_


**Query 2:**


**Process** Element -> filter for Credential theft tool execution is _True_


**Query 3:**


**Process** Element -> filter for Mimikatz execution was detected is

_True_


**Goal:** Find when an attacker is performing reconnaissance on a


machine through trying to learn more about accounts on the

machine.


**Explanatory statement:** I want to find examples of processes

performing account discovery.


Construct this query:


**Process** Element -> filter for Account discovery is _True_

## Lateral Movement: Remote Desktop


**Goal:** Find use of the Remote Desktop Protocol to move through

the network.


**Explanatory statement:** I want to find examples of when the

Remote Desktop protocol was used in my environment.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for Remote Desktop Protocol enabled is

_True_


**Query 2:**


**Process** Element -> filter for Remote Desktop Protocol has been


started is _True_

## Collection: Data from Local System


**Goal:** Find attackers collecting information from the local file

system.


**Explanatory statement:** I want to find examples of commands
used for collection of information from the local file system.


Construct this query:


**Process** Element -> filter for Command line is _fsutil_


Note there are other commands used for collecting information
from the file system. This is an example of a common one, but you


can substitute other commands in this query as needed.

## Exfiltration: Exfiltration over Command

## and Control Channel


**Goal:** Find data being sent over a command and control

connection.


**Explanatory statement:** I want to find examples of data theft

through command and control through instances of a large


amount of data being transmitted to questionable addresses.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for High data transmitted is _True_


**Query 2:**


**Process** Element -> filter for High Data Volume Transmitted to


Malicious Address is _True_


**Query 3:**


**Process** Element -> filter for Has suspicious external connection


is _True_

## Command and Control: Remote File Copy


**Goal:** Find a process using command and control to copy files

from my environment.


**Explanatory statement:** I want to find instances of specific

processes initiating connections that usually enable copying of


files elsewhere.


Construct one of the following queries:


**Query 1:**


**Process** Element -> filter for rundll32.exe OS abuse is _True_


**Query 2:**


**Process** Element -> filter for FTP communication is _True_


**Query 3:**


**Process** Element -> filter for Ftp.exe is descendant of suspicious

process is _True_


**Query 4:**


**Process** Element -> filter for High Data Volume Transmitted to

Malicious Address is _True_





