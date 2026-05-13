## Monitor sensor actions in the Sensor Actions screen

From the **Sensor Actions** screen, you can view all essential


actions performed on the sensor, and information about each

action.


The following information is available about each action:








|Column name|Description|
|---|---|
|Action Status|The status of the action:<br>Unknown, Completed, Failed.|
|Action Type|The type of sensor action that<br>was performed: Upgrade,<br>Installation, Uninstall.|
|Machine Name|The name of the machine on<br>which the sensor was<br>installed, upgraded or<br>uninstalled.|
|Error|The error that was retrieved<br>during sensor installation or<br>upgrade.|
|Error Message|The error message, which<br>describes the cause of the<br>installation or upgrade failure.<br>There may be more than one<br>failure. See the 'Errors'<br>section below for a list of error<br>messages.|
|Internal IP Address|The internal IP address of the<br>machine.|


|Column name|Description|
|---|---|
|Initiated At|The time and date on which<br>the action was initiated.|
|Version at start|The installed sensor version<br>prior to the sensor action.|
|Version at end|The installed sensor version<br>following the sensor action.|


On this screen, you can:


Add or remove columns. Column sort is not yet available.


Search for sensor actions by machine name or internal IP

address.


Filter the results according to the **Action Type**, **Action Status**,

and **Error** .


Important


If an installation or upgrade is successful, the status is


reflected in the **Sensor Actions** screen. When an uninstall
action is successful, the success status is not reflected in the


screen, as the sensor was already removed and no longer

communicating with the server. The Sensor Actions screen still


displays an error when an uninstall fails.

## View installation or upgrade Errors in the

## Sensor Actions screen


In case of installation or upgrade failure, the Sensor Actions


screen displays errors from different sources:


**From the sensor:** These errors represent failures during


installation.

**From the Detection server:** These errors represent failures


from the validations performed before a package is sent to the

sensors.


The table below lists the available errors:


Note


The error messages displayed in the Sensor Actions screen

are more elaborate than the messages described below. For


example, for **Failure reason unknown**, the following error

message is displayed: **Failure reason unknown: Failed to**


**verify uninstall code or file. Uninstall is denied.**


|Error|Error<br>Code|Error<br>Messa|ge|
|---|---|---|---|
|FAILURE_REASON_UNKNOWN|0|Failure<br>reason<br>unknow|n|
|FAILED_TO_VERIFY_CERTIFICATE|1|Failed t<br>verify<br>bundle<br>certifc|o<br>'s<br>ation.|
|NEWER_INSTALLED|2|Downg<br>is not<br>suppor<br>installa<br>version<br>x.x.x.x<br>installe<br>version<br>Y.Y.Y.Y.|rade<br>ted,<br>tion<br> is<br>and<br>d<br> is|
|OS_NOT_SUPPORTED|3|OS not<br>suppor|ted|
|ARCH_MISMATCH|4|One of<br>followin<br>A 32-bi<br>installa<br>cannot<br>installe<br>a 64-bi<br>Windo<br>machin<br>A 64-bi<br>installa<br>cannot<br>installe<br>a 32-bi<br>Windo<br>machin|the<br>g:<br>t<br>tion<br> be<br>d on<br>t<br>ws<br>e.<br>t<br>tion<br> be<br>d on<br>t<br>ws<br>e.|
|ALREADY_UPDATED|5|Alread<br>update|y<br>d|
|MISSING_PACKAGE_FROM_FILE_SYSTEM|6|Missing<br>packag<br>from fl<br>system|e<br>e|
|||||


|Error|Error<br>Code|Error<br>Messa|ge|
|---|---|---|---|
|MSI_FILE_CORRUPTED|7|MSI fle<br>corrupt|ed|
|TIMEOUT|8|Timeou|t|
|FAILED_TO_SHUT_DOWN_SELF_PROTECT|9|Failed t<br>shut do<br>self pro|o<br>wn<br>tect|
|SERVICE_PACK_IS_INSUFFICIENT|10|Insuffc<br>service<br>pack -<br>require<br>{n}, fou<br>{n-?}.|ient<br><br>d<br>nd:|
|BUILD_NUMBER_IS_INSUFFICIENT|11|Insuffc<br>build<br>numbe<br>require<br>{n}, fou<br>{n-?}.|ient<br>r -<br>d<br>nd:|
|DENY_REPAIR|15|This<br>installa<br>does n<br>suppor<br>Repair<br>action.|tion<br>ot<br>t the|
|SAME_VERSION_INSTALLED|16|Cannot<br>install t<br>same<br>version<br>new bu|he<br> of a<br>ild.|
|PACKAGE_FAILED|18|Packag<br>failed.|e|
|BUNDLE_FAILED_TO_EXECUTE|19|Bundle<br>failed t<br>execut|o<br>e|
|BUNDLE_FAILED_TO_APPLY|20|Bundle<br>failed t<br>apply|o|
|UNINSTALL_IS_DENIED|21|Uninsta<br>denied|ll is|
|||||


|Error|Error<br>Code|Error<br>Message|
|---|---|---|
|BAD_UNINSTALL_PASSWORD|22|Failed to<br>verify<br>uninstall<br>password.|
|BAD_OSV_FILE|23|Failed to<br>verify OSV<br>fle.|





