Server configuration data, such as IP address, DNS, and


proxy settings, allowing for a full restore of the servers should

the need arise.


Detection data which is stored in the CMC Engine.

Cybereason provides mechanisms for restoring this data only,


if a full restore is not necessary.

## Detection server backup


Cybereason automatically backs up each Detection server by:


Taking daily snapshots of the Detection server. Snapshots

include detection data in the In-Memory Graph database.


Storing recordings of raw data sent from sensors to the

Detection server. These recordings are stored in buffers on


the sensor and are used to supplement the daily snapshot in

the event of a restore.


Backing up server configuration files and database.


See retention times for each of the previous processes in the


tables of the Cybereason backup archives section.

## Detection server recovery


The following cases outline recovery steps for the most common


scenarios:


**Case 1:** If the server fails unexpectedly and can be recovered,


Cybereason Technical Support restarts the server. The server
continues to function using the current configuration files and


database:


1. Loading the latest snapshot to restore data up to the point


when the snapshot was taken.

2. Loading the recordings from the snapshot creation time


onwards. This restores data to the most current state.


The following image illustrates this process:


Note


The file size for the snapshot and recordings depends on the


environment and on the amount of data received from sensors.


The recovery time depends on the data size and can take several


hours.


**Case 2:** If the server fails unexpectedly and it cannot be


recovered, Cybereason Technical Support reinstalls the server.

After the reinstallation:


1. Technical Support restores detection data from the latest


snapshot.


2. Technical Support loads recordings from the snapshot


creation time onwards. This restores data to the most current


state.

3. Technical support restores server configuration files and the


database from the latest backup.


Recovery time for each phase varies, as listed in the following


table:

|Component|Retention time|
|---|---|
|Server re-<br>installation|30 min.|
|Loading data|Depends on the data size; can take<br>several hours.|
|Database restore|30 min.|


## BYOK Bring Your Own Key


Cybereason supports BYOK (Bring Your on Key) encryption for


the GCP bucket containing your Backup recordings. Customers

who wish to encrypt their recording backups using BYOK must


[use Fortanix (https://www.fortanix.com/solutions/use-case/bring-](https://www.fortanix.com/solutions/use-case/bring-your-own-key-hold-your-own-key)

[your-own-key-hold-your-own-key) (a third-party vendor) to set this](https://www.fortanix.com/solutions/use-case/bring-your-own-key-hold-your-own-key)


up. Please contact your Cybereason Account Manager who can

connect you with Fortanix for your BYOK setup.

## Additional server backup


Cybereason automatically backs up server configuration files and

the database for the following servers:


WebApp server

Private Threat Intel server


Registration server

## Additional server recovery


The following cases outline recovery steps for the most common


scenarios:


**Case 1:** If the server fails unexpectedly and it can be recovered,


Cybereason Technical Support restarts the server and it continues
to function using the current configuration files and database.


**Case 2:** If the server fails unexpectedly and it cannot be


recovered, Cybereason Technical Support reinstalls the server.

After the server reinstallation, Cybereason Technical Support


restores server configuration files and database from the latest

backup.

## Cybereason backup archives


Cybereason Technical Support automatically backs up your data
daily and generates a *.tgz file, named as follows:

```
 <Server Name>_<Date>.tgz

```

The backup archive contains server configuration files and
detection data files, as described in the following tables:

## Server configuration data files (all












|Backup file|Data<br>description|Estimated<br>file size|Retention<br>time|
|---|---|---|---|
|managment_facter.json|Main<br>confguration<br>fles for each<br>server. The<br>fles exist on<br>each<br>Cybereason<br>server and<br>contain all the<br>server<br>settings (for<br>example,<br>Hostname, IP<br>address,<br>DNS, etc.).|Averages<br>~10<br>kilobytes|Indefnitely|


|Backup file|Data<br>description|Estimated<br>file size|Retention<br>time|
|---|---|---|---|
|puppet.conf|Confguration<br>fle containing<br>the current<br>version<br>information<br>and<br>connection<br>information to<br>the<br>Cybereason<br>Update<br>server.|Averages<br>~5<br>kilobytes|Indefnitely|
|Regions_confg|Confguration<br>related to the<br>Registration<br>server. The<br>fle contains<br>logical<br>distribution of<br>sensors<br>between<br>Detections<br>servers.|Averages<br>~20<br>kilobytes|Indefnitely|
|MongoDB dump|Application<br>database for<br>various<br>confgurations<br>and statuses<br>(for example,<br>reputation<br>lists, System<br>user<br>information,<br>etc.).|Averages<br>~ 15 MB*|Indefnitely|


## Detection data (Detection server only)








|Backup<br>file|Data<br>description|Estimated<br>file size|Retention time|
|---|---|---|---|
|Snapshot|Daily<br>backup of<br>the data in<br>the Memory<br>Graph<br>Database.<br>This fle<br>contains all<br>detection<br>information<br>up until<br>snapshot<br>creation.|Averages<br>~36 GB*|1 week|


|Backup<br>file|Data<br>description|Estimated<br>file size|Retention time|
|---|---|---|---|
|Recordings|Raw user<br>data<br>received<br>from<br>sensors<br>assigned to<br>the server.<br>Recordings<br>are<br>generated<br>constantly<br>and used to<br>supplement<br>the<br>Snapshot<br>during a<br>system<br>restore.|Averages<br>~12.5 GB*|30 days<br>**Note:** For Historical<br>Data Lake<br>customers, the<br>Cybereason<br>platform retains<br>recordings<br>according to the<br>retention period<br>confgured for the<br>Historical Data<br>Lake instance. For<br>example, if the<br>Historical Data<br>Lake instance is<br>confgured to 60<br>days, the<br>Cybereason<br>platform retains the<br>recordings for 60<br>days.<br>For Incident<br>Response<br>customers, the<br>retention period is<br>90 days.<br>If you would like to<br>extend the retention<br>period, you can<br>purchase a backup<br>data extension<br>package. For more<br>information, see<br>Backup Data<br>Extension<br>Packages<br>(/s/article/6596571).|



The backup file size depends on the environment and the amount


of data received from sensors.


## Backup intervals and archives storage

Cybereason provides AWS S3 as a backup storage. The following


table describes backup intervals, as well as how many backup

archives are retained at any one time. _N_ represents the current


backup.













|Server|Recommended<br>backup interval|Recommended<br>number of backup<br>archives|
|---|---|---|
|Detection<br>server|Daily|_N_ + 2 daily snapshots|
|WebApp<br>server|Weekly|_N_ + 2 daily backups of<br>server confguration<br>fles only|
|Private Threat<br>Intel server|Weekly|_N_ + 2 daily backups of<br>server confguration<br>fles only|
|Registration<br>server|Weekly|_N_ + 2 daily backups of<br>server confguration<br>fles only|

## Backup script



Cybereason Technical Support executes the backup script via a


cronjob on the target server. This enables control over the backup

execution.


During the script execution, the script verifies the server type and

creates the archive package based on the backup manifest for


the specific server type.


Once the backup package is created, it is transferred to the


customer's S3 dedicated bucket.


There is full separation in S3 between customers. Backups per


customer are saved in a dedicated library.


In addition, as a handshake mechanism, recovery verifies that the


destination server has the same organization name as the S3

bucket library. If the organization names are different, the recovery


script fails.

## Backup package


The backup package is named using the following naming


convention:



