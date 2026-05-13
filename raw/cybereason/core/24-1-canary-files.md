## How does Cybereason monitor canary

Cybereason maintains a persistence file and log file to keep track


of canary objects on your system. The persistent file (a .bin file)

tracks the canary objects currently deployed. Cybereason writes


the persistence file before any other file system operation so if
issues arise, the sensor can reference the persistence file to


delete orphaned canary objects left on the file system.


The log file (ProgramData\crs1\crs_log.txt) contains specific


entries documenting any operation on the canary files (e.g.,

creation, deletion, re-use) and helps with debugging and


identifying computer configurations and scenarios deployed on

the customer side.

## Canary object deployment


Canary objects are installed in root folder locations (e.g., C:\, D:\,

etc.) and the main (C:\Users) directory for the machine, as well as


in locations specific to any user who is logged in at the time of

deployment/redeployment.


On each machine, canary objects collectively occupy an average

of 4 MB of disk space per root directory, plus about another 8 MB


per logged-in user. If a drive does not have enough available

space, the Cybereason platform does not deploy the objects and


issues a log message stating there is not enough available space

to deploy canary objects on this drive. The Cybereason platform


continues the deployment process on other drives.


Users must be physically logged in to a machine at the time of


deployment or redeployment for canary objects to be deployed

into the user folder. Canary objects are not deployed to user


folders for users who are not logged in at the time of deployment

or redeployment.


The following table describes where Cybereason places canary
folders. Each canary folder contains 9 canary files.


Note


If your organization uses a third-party cloud backup tool, it is

expected that canary objects will be copied to the cloud


backup as well.


Canary objects are not deployed:


on external hard drives (e.g. USB devices)

on network drives


In addition, canary objects are not deployed in the user folder

( **Documents** folder or **Desktop** folder) in the following situations:


If a user is connected to any virtual or physical machine via

Remote Desktop at the time of deployment.


If a user is logged in to a machine with a Roaming Profile at

the time of deployment.


Note that in any of these cases, the system in general is protected

by the objects in the root drives and in the main Users directory


(C:\Users).


Canary objects are redeployed on a periodic basis (see Canary


object redeployment). If the user is logged in at the time of

redeployment, canary objects are deployed to the user folder.


You can customize canary object locations. See Customize


canary object names and locations.


## Canary object redeployment

The Cybereason platform periodically redeploys canary objects to


ensure the folders and files on your system are as effective as

possible.


The Cybereason platform attempts to redeploy canary objects:


When the Anti-Ransomware service starts (for example, after


the machine restarts)

Five minutes after the Anti-Ransomware service starts


Every 24 hours
If a user deletes a canary file


If an agent other than Cybereason changes canary files


The redeployment process is optimized to reuse as many canary


files currently deployed on the file system as possible. Because of

this, some canary object names will not change upon


redeployment.

## Canary object naming conventions


The Cybereason canary object naming convention prevents an


attacker from easily identifying a computer protected with the

Cybereason solution. The following sections describe the


Cybereason canary object naming conventions and specify how
you can customize the names for easier identification within your


organization:


|Naming<br>convention|Details|
|---|---|
|Canary<br>folder<br>names|Canary folder names are derived from a base<br>name, which is generated based on the<br>machine name. The Cybereason platform<br>generates the canary folder name by<br>prepending a letter to this base name. The<br>Cybereason platform determines the specifc<br>leading letter by scanning the fle system and<br>assigning a letter that ensures the folders<br>appear frst and last in an ascending or<br>descending alphabetical sort of the fle system.<br>This action ensures that any ransomware fnds<br>the canary objects frst.<br>The naming convention allows for easy<br>identifcation of canary folders on a computer,<br>while ensuring that different machines have<br>different canary folder names.<br>Example canary folder names:<br>AEzaS36GsA<br>XEzaS36GsA<br>The following image is an example of canary<br>folders at the root level (C:\).|


|Naming<br>convention|Details|
|---|---|
|Canary fle<br>names|Most canary fle names consist of common<br>English words separated by random delimiters.<br>For others, the flename is a string of between<br>3-6 random characters (numbers, letters) and<br>delimiters.<br>Canary fles can have the following 10 fle<br>types:<br>Plain text fle (.txt)<br>Microsoft Excel 97-2004 Workbook File<br>(.xls)<br>Rich text document (.rtf)<br>Microsoft Word 97-2004 document (.doc)<br>SQL fle (.sql)<br>Microsoft Excel Workbook (.xlsx)<br>Microsoft database fle (.mdb)<br>Privacy enhanced mail fle (.pem)<br>Microsoft Word document (.docx)<br>JPEG (.jpg)<br>Example canary fle names:<br>boxer_kilowatt_drapery_vitality.txt<br>pL1ytzl8Cqw.sql<br>The following image is an example of canary<br>fles deployed at the user level (within the<br>aca4zfbr canary folder).|



If users see canary folders and files, the objects can appear
alarming to users who do not understand why the files are there.


You can help users understand by sharing with them the naming
conventions and locations in which the users will find canary files.


For more information, see Help users identify canary objects.


## Customize canary object names and

To help users identify canary objects, you can append strings to


canary folder and file names. These strings can help users more

readily recognize canary objects and clear up any confusion


about their appearance. Appending strings can also make it
easier for you to identify and exclude these files from scanning by


third party security products that might find such files irregular.


You can also specify where to place canary folders on endpoints,


and determine if canary folders and files are visible or hidden from

users in each location.


Important


For full protection, Cybereason recommends not to hide


canary folders and files.


[For details on how to set behaviors for canary files, see Set canary](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-canary-file-based-anti-ransomware-modes&language=en_US#set-canary-file-preferences)


[file preferences (/s/knowledge-base?article=24-1-set-the-canary-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-canary-file-based-anti-ransomware-modes&language=en_US#set-canary-file-preferences)
[file-based-anti-ransomware-modes&language=en_US#set-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-canary-file-based-anti-ransomware-modes&language=en_US#set-canary-file-preferences)


[canary-file-preferences).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-canary-file-based-anti-ransomware-modes&language=en_US#set-canary-file-preferences)


[Open a Technical Support (/s/support) case for assistance with](https://nest.cybereason.com/s/support)


customization settings.


The Cybereason platform performs canary object cleanup to


avoid leaving unused canary objects on disk.


A canary object cleanup procedure occurs when the Anti

Ransomware service stops. The service stops when you:


Disable the Anti-Ransomware solution


Shut down the machine

Stop the service via the local services


Uninstall the sensor


Canary files are stored in canary folders. The files and folders are


collectively called canary objects).


If users see canary objects, the objects can appear alarming to


users who do not understand why the canary files are there. You

can help users understand by sharing with them the naming


conventions and locations in which the users will find canary files.


In most cases, canary objects are hidden from the user. Please


note that they will be visible if a user's machine is configured to
show hidden files. To view any hidden canary objects, make sure


you:



