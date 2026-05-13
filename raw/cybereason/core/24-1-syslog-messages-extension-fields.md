## Fields by event

The following tables list the extension fields available for each


syslog event, organized by event class.

## MALOP extension fields


















|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
|Malop<br>Created,<br>MalOp<br>Updated|cs1Label|malopID||
||cs1|Unique identifer for t<br>MalOp||
||cn1Label|affectedMachineCou||
||cn1|Number of machines<br>affected by the MalO||
||deviceCustomDate1Label|malopCreationTime||
||deviceCustomDate1|Timestamp for when<br>the MalOp was creat||
||cs2Label|malopDetectionType||
||cs2|Description of what<br>triggered the MalOp||
||cn2Label|affectedUsers||
||cn2|Number of users<br>affected by the MalO||
||deviceCustomDate2Label|malopUpdateTime||
||deviceCustomDate2|Timestamp for when<br>the MalOp was<br>updated||
||cs3Label|malopActivityType||
||cs3|Type of activity the<br>MalOp is attempting<br>execute||
||deviceCustomDate3Label|suspectCreationTime||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||deviceCustomDate3|Timestamp for when<br>the root cause proce<br>was created||
||cs4Label|malopSuspect||
||cs4|The suspicious event<br>that triggered the<br>MalOp||
||cs5Label|malopKeySuspicion||
||cs5|The reason the event<br>was found to be<br>suspicious.||
||cs6Label|linkToMalop||
||cs6|Link to the MalOp in<br>Cybereason platform||
||cs7Label|socFederationID||
||cs7|Unique identifer for t<br>sensor group of the<br>sensor associated w<br>the Malop||
||deviceCustomDate3Label|suspectCreationTime||
||detectionRule|The decision Feature<br>that caused the<br>creation or update of<br>this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||requestContext|The context in which<br>this MalOp was creat<br>or updated.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||reason|The reason this MalO<br>was generated.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||suser|The name of the user<br>associated with the<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||rt|The time the MalOp<br>was generated in the<br>Cybereason platform<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||deviceDnsDomain|The DNS name for th<br>machine associated<br>with the MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||start|The time the MalOp<br>activity started.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||parentProcess|The parent process o<br>the root cause of the<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||childrenProcess|Any child processes<br>the root cause of the<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||OSVersion|The operating system<br>version operating on<br>the machine associa<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||isOnline|If the machine<br>associated with this<br>MalOp is currently<br>connected to the<br>Cybereason platform<br>the time of MalOp<br>generation.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||isOriginalMachine|If this is the frst time<br>this machine has bee<br>involved with a MalO<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||isSigned|If the fle associated<br>with this MalOp is<br>signed by a verifed<br>signature authority.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable this feld.||
||affectedMachines|A list of all machines<br>associated with the<br>malicious activity in t<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||affected_machine_ip_addresses|The IP addresses of<br>machines associated<br>with the malicious<br>activity in the MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||affected_machine_domain|The domain of the<br>machines associated<br>with the malicious<br>activity in the MalOp.||
||affected_machine_os_version|The operating system<br>version of the machin<br>associated with the<br>malicious activity in t<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||affected_user_name|The user name<br>associated with the<br>malicious activity in t<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||affected_user_domain|The domain for the u<br>associated with the<br>malicious activity in t<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||affected_user_privilege|The privilege level of<br>the user associated<br>with the malicious<br>activity in this MalOp<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||malicious_process_creation_time|The creation time for<br>the process associat<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||malicious_process_pid|The unique identifer<br>(Process ID) for the<br>process associated<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||malicious_process_name|The name of the<br>process associated<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||malicious_process_command_line|The command line ru<br>by the process<br>associated with this<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||process_fle_name|The fle name<br>associated with the r<br>cause of this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||process_fle_path|The path to the fle<br>associated with the r<br>cause of this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||process_fle_sha1|The SHA-1 fle hash<br>value for the fle<br>associated with the r<br>cause of this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||process_fle_md5|The MD5 fle hash<br>value for the fle<br>associated with the r<br>cause of this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||parent_process_creation_time|The creation time of t<br>parent process of the<br>process associated<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||parent_process_pid|The unique identifer<br>(Process ID) for the<br>parent process of the<br>process associated<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||parent_process_name|The name of the pare<br>process of the proce<br>associated with this<br>MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
||parent_process_command_line|The command line fo<br>the parent process o<br>the process associat<br>with this MalOp.<br>This feld is disabled<br>default. Open a<br>Technical Support<br>(/s/support) case to<br>enable the**Dedicate**<br>**Messages** that includ<br>this feld.||
|Malop<br>Machine<br>Information|cs1Label|malopID||
||cs1|Unique identifer for t<br>MalOp||
||cn1Label|affectedMachinesCo||
||cn1|Number of machines<br>affected by the MalO||
||cs2Label|affectedMachine||
||cs2|Name of the machine||
||cs3Label|socFederationID||
||cs3|Unique identifer for t<br>sensor group of the<br>sensor associated w<br>the MalOp||
||deviceCustomDate1Label|malopUpdateTime||
|||||


|Event<br>name(s)|Field key name|Value|Col4|
|---|---|---|---|
||deviceCustomDate1|Timestamp for when<br>the MalOp was<br>updated||
|Malop<br>Updated<br>Machine<br>Information|cs1Label|malopID||
||cs1|Unique identifer for t<br>Malop||
||cn1Label|affectedMachinesCo||
||cn1|Number of machines<br>affected by the MalO||
||cs2Label|affectedMachine||
||cs2|Name of the machine||
||deviceUpdatedDate1Label|machineUpdatedTim||
||deviceUpdatedDate1|Timestamp for when<br>the machine was<br>added to the Malop||
|MALWARE extension fields<br>**Event**<br>**name(s)**<br>**Field key name**<br>**Value**<br>Malware<br>Created,<br>Malware<br>Updated<br>eventId<br>Unique identifer of<br>this Malware alert<br>dvchost<br>Name of the device<br>on which the malware<br>was detected.<br>cs1Label<br>virusName|MALWARE extension fields<br>**Event**<br>**name(s)**<br>**Field key name**<br>**Value**<br>Malware<br>Created,<br>Malware<br>Updated<br>eventId<br>Unique identifer of<br>this Malware alert<br>dvchost<br>Name of the device<br>on which the malware<br>was detected.<br>cs1Label<br>virusName|MALWARE extension fields<br>**Event**<br>**name(s)**<br>**Field key name**<br>**Value**<br>Malware<br>Created,<br>Malware<br>Updated<br>eventId<br>Unique identifer of<br>this Malware alert<br>dvchost<br>Name of the device<br>on which the malware<br>was detected.<br>cs1Label<br>virusName||


|Event<br>name(s)|Field key name|Value|
|---|---|---|
|Malware<br>Created,<br>Malware<br>Updated|eventId|Unique identifer of<br>this Malware alert|
||dvchost|Name of the device<br>on which the malware<br>was detected.|
||cs1Label|virusName|


|Event<br>name(s)|Field key name|Value|
|---|---|---|
||cs1|If the alert is<br>known malware:<br>detection name<br>If the alert is<br>unknown<br>malware:<br>'AI.StaticAnalysis'<br>If the alert is<br>fleless: scenario<br>name (e.g.,<br>download &<br>execute,<br>malicious<br>command,<br>malicious<br>download)|
||cs2Label|context|
||cs2|Context of the<br>specifc alert:<br>If the alert is<br>known malware:<br>full fle path<br>If the alert is<br>unknown<br>malware: full fle<br>path<br>If the alert is<br>fleless and<br>scenario is<br>'download &<br>execute' or<br>'malicious<br>download': URL<br>of malicious<br>payload<br>If the alert is<br>fleless and<br>scenario is<br>''malicious<br>command':<br>pattern name|
||cs3Label|investigation|
||cs3|Link to investigation of<br>the alert.|


|Event<br>name(s)|Field key name|Value|
|---|---|---|
||deviceCustomDate1Label|malwareCreationTime|
||deviceCustomDate1|Timestamp of the<br>Malware alert|

## USERACTION extension fields

All USER_ACTION syslog messages contain the following fields:


**cs1Label:** username

**cs1:** Username for the user performing the action


**cn1Label:** actionSuccess

**cn1:** **0** if the action failed, **1** if the action succeeded


**deviceCustomDate1Label:** userActionTime

**deviceCustomDate1:** Time the action occurred


**cs6Label:** userclassification
**cs6:** String value from the User classification field in the **Users**


screen


In addition, each action group includes specific fields, as shown in


the following tables.
**CUSTOM RULES** action group extension fields




















|Event<br>name(s)|Field key<br>name|Value|
|---|---|---|
|RuleCreated|cs2Label|userRole|
||cs2|String with the set of roles<br>assigned for the user that<br>created the custom detection<br>rule|
||cs3Label|ruleName|
||cs3|Name of the custom detection<br>rule|
||cs4Label|active|
||cs4|Specifes whether the rule is<br>enabled (**true**) or disabled<br>(**false**)|
|RuleUpdated|cs2Label|userRole|


|Event<br>name(s)|Field key<br>name|Value|
|---|---|---|
||cs2|String with the set of roles<br>assigned for the user that<br>created the custom detection<br>rule|
||cs3Label|ruleName|
||cs3|The name of the custom<br>detection rule|
||cs4Label|feld|
||cs4|The feld in the rule that was<br>updated|
||cs5Label|old|
||cs5|The old value for the feld that<br>was updated|
||cs7Label|new|
||cs7|The new value for the feld that<br>was updated|


**DETECTION RULES** action group extension fields










|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
|DecisionFeatureCreated/DecisionFeatureUpdated,<br>SuspicionCreated/SuspicionUpdated|cs2Label|userRo|
||cs2|String<br>user th|
||cs3Label|decisio|
||cs3|Name<br>suspic|
||cs4Label|action|
||cs4|Details|


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
||c5Label|Server|
||c5|IP add|
|**GENERAL** action group extension felds<br>**Event name(s)**<br>**Field key**<br>**name**<br>**Value**<br>Login<br>cs2Label<br>loginMethod<br>cs2<br>The login<br>method for the<br>user<br>cs3Label<br>userRole<br>cs3<br>String with the<br>set of user<br>roles for this<br>user<br>cs4Label<br>machineName<br>cs4<br>Name for the<br>machine from<br>which the user<br>logged in<br>cs5Label<br>machineIP<br>cs5<br>IP address for<br>the machine<br>from which the<br>user logged in<br>Logout<br>cs2Label<br>userRole<br>cs2<br>String with the<br>set of user<br>roles for this<br>user<br>cs3Label<br>machineName|**GENERAL** action group extension felds<br>**Event name(s)**<br>**Field key**<br>**name**<br>**Value**<br>Login<br>cs2Label<br>loginMethod<br>cs2<br>The login<br>method for the<br>user<br>cs3Label<br>userRole<br>cs3<br>String with the<br>set of user<br>roles for this<br>user<br>cs4Label<br>machineName<br>cs4<br>Name for the<br>machine from<br>which the user<br>logged in<br>cs5Label<br>machineIP<br>cs5<br>IP address for<br>the machine<br>from which the<br>user logged in<br>Logout<br>cs2Label<br>userRole<br>cs2<br>String with the<br>set of user<br>roles for this<br>user<br>cs3Label<br>machineName|**GENERAL** action group extension felds<br>**Event name(s)**<br>**Field key**<br>**name**<br>**Value**<br>Login<br>cs2Label<br>loginMethod<br>cs2<br>The login<br>method for the<br>user<br>cs3Label<br>userRole<br>cs3<br>String with the<br>set of user<br>roles for this<br>user<br>cs4Label<br>machineName<br>cs4<br>Name for the<br>machine from<br>which the user<br>logged in<br>cs5Label<br>machineIP<br>cs5<br>IP address for<br>the machine<br>from which the<br>user logged in<br>Logout<br>cs2Label<br>userRole<br>cs2<br>String with the<br>set of user<br>roles for this<br>user<br>cs3Label<br>machineName|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
|Login|cs2Label|loginMethod|
||cs2|The login<br>method for the<br>user|
||cs3Label|userRole|
||cs3|String with the<br>set of user<br>roles for this<br>user|
||cs4Label|machineName|
||cs4|Name for the<br>machine from<br>which the user<br>logged in|
||cs5Label|machineIP|
||cs5|IP address for<br>the machine<br>from which the<br>user logged in|
|Logout|cs2Label|userRole|
||cs2|String with the<br>set of user<br>roles for this<br>user|
||cs3Label|machineName|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
||cs3|Name for the<br>machine from<br>which the user<br>logged in|
||cs4Label|machineIP|
||cs4|IP address for<br>the machine<br>from which the<br>user logged in|
|NotifcationSettingChange|cn2Label|newState|
||cn2|The new<br>notifcation<br>state (**1** if<br>notifcation<br>setting is<br>enabled,**0** if<br>disabled)|
||cn3Label|oldState|
||cn3|The old<br>notifcation<br>state (**1** if<br>notifcation<br>setting is<br>enabled,**0** if<br>disabled)|
|ChangePassword|No<br>additional<br>felds|N/A|
|ChangeConfgurationSettings|No<br>additional<br>felds|N/A|
|ChangeConfgurationDetails|cs2Label|propertyName|
||cs2|Name of the<br>property user<br>confgured|
||cn2Label|NewState|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
||cn2|The new<br>collection state<br>(**1** if collection<br>setting is<br>enabled,**0** if<br>disabled)|
||cn3Label|oldState|
||cn3|The old<br>collection state<br>(**1** if collection<br>setting was<br>enabled,**0** if<br>disabled)|
|CollectionConfgurationOverride|No<br>additional<br>felds|N/A|
|CollectionConfgurationOverrideDetails|cs2Label|propertyName|
||cs2|Name of the<br>property user<br>is overriding|
||cn2Label|state|
||cn2|New override<br>value (**1** if<br>enabled,**0** if<br>disabled)|
|CollectionConfgurationOverrideSensor|cs2Label|sensorId|
||cs2|Unique<br>identifcation<br>for the sensor<br>on which the<br>user<br>performed the<br>override|
|RegistryEventsInclusionAdd|cs2Label|key|
||cs2|The registry<br>key added in<br>the inclusion<br>list|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
||cn2Label|approved|
||cn2|Whether the<br>update was<br>verifed as<br>correctly<br>formatted|
||cn3Label|depth|
||cn3|Whether or not<br>to collect<br>specifc values<br>from all keys<br>and subkeys of<br>the specifed<br>registry key|
||cs3Label|values|
||cs3|The specifc<br>values to<br>collect from<br>this registry<br>key|
|RegistryEventsInclusionModify|cs2Label|key|
||cs2|The registry<br>key modifed|
||cn2Label|approved|
||cn2|Whether the<br>update was<br>verifed as<br>correctly<br>formatted|
||cn3Label|depth|
||cn3|Whether or not<br>to collect<br>specifc values<br>from all keys<br>and subkeys of<br>the specifed<br>registry key|
||cs3Label|values|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
||cs3|The specifc<br>values to<br>collect from<br>this registry<br>key|
||cs4Label|oldKey|
||cs4|The registry<br>key value used<br>in this inclusion|
||cn4Label|oldapproved|
||cn4|Whether the<br>update was<br>verifed as<br>correctly<br>formatted|
||cn5Label|olddepth|
||cn5|Whether or not<br>to collect<br>specifc values<br>from all keys<br>and subkeys of<br>the specifed<br>registry key|
||cs5Label|oldvalues|
||cs5|The previously<br>entered values<br>to collect from<br>this registry<br>key|
|RegistryEventsInclusionKeep|cs2Label|key|
||cs2|The value of<br>the registry|
||cn2Label|approved|
||cn2|Whether the<br>update was<br>verifed as<br>correctly<br>formatted|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
||cn3Label|depth|
||cn3|Whether or not<br>to collect<br>specifc values<br>from all keys<br>and subkeys of<br>the specifed<br>registry key|
||cs3Label|values|
||cs3|The specifc<br>values to<br>collect from<br>this registry<br>key|
|RegistryEventsInclusionDelete|cs2Label|key|
||cs2|The value of<br>the registry key<br>to delete|
||cn2Label|approved|
||cn2|Whether the<br>update was<br>verifed as<br>correctly<br>formatted|
||cn3Label|depth|
||cn3|Whether or not<br>to collect<br>specifc values<br>from all keys<br>and subkeys of<br>the specifed<br>registry key|
||cs3Label|values|
||cs3|The specifc<br>values to<br>collect from<br>this registry<br>key|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
|IRToolsDownloadResults|cs2Label|packageName|
||cs2|The unique<br>name for the IR<br>tool package|
||cs3Label|outputDirectory|
||cs3|The directory<br>to which to<br>write the<br>results for the<br>tool execution|
|IRToolsDownloadResultsSensor|cs2Label|sensorID|
||cs2|The sensor ID<br>for the sensor<br>from which to<br>download<br>results from a<br>IR tool<br>execution|
|IRToolsRunCommand|cs2Label|packageName|
||cs2|The unique<br>name for the IR<br>tool package|
||cs3Label|commandLine|
||cs3|The command<br>line to use to<br>run the tool|
||cs4Label|outputDirectory|
||cs4|The directory<br>to which to<br>write the<br>results for the<br>tool execution|
|IRToolsRunCommandSensor|cs2Label|sensorId|
||cs2|The sensor ID<br>for the sensor<br>on which to run<br>an IR tool|


**INVESTIGATION** action group extension fields




















|Event name(s)|Field key<br>name|Value|
|---|---|---|
|DeleteQuery,<br>saveQuery,<br>EditQuery|cs2Label|queryName|
||cs2|The name of the saved<br>query for the action|
||cs3Label|queryDescription|
||cs3|The description of the<br>saved query for the action|
|Query|cs2Label|QueryDetails|
||cs2|Details of the query run<br>by a user|
||cs3Label|QueryParameters|
||cs3|The parameters for the<br>query when it was run|
|FileSearchQuery|cs2Label|QueryDetails|
||cs2|Details of the fle search<br>query|
||cs3Label|AffectedHosts|
||cs3|The list of machines on<br>which the fle search<br>query was run|
|GetFile|fleName|File name|
||fleName|The name of the fle<br>downloaded|
|BrowseFolder|cs2Label|FolderName|
||cs2|The name of the folder<br>where the user performed<br>a fle browse|
||cs3Label|MachineName|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
||cs3|The machine on which the<br>user viewed the folder<br>directories|



**MALOP INVESTIGATION** action group extension fields














|Event name(s)|Field key name|Value|
|---|---|---|
|ChangeMalopState|cs2Label|malopID|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|oldState|
||cs4|Old state of|
||cs5Label|newState|
||cs5|New state of|
|Remediation|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|remediationT|


|Event name(s)|Field key name|Value|
|---|---|---|
||cs4|The type of<br>performed (<br>**UNSUSPEN**<br>**KILL_PREV**<br>**KILL_PROC**<br>**QUARANTI**<br>**UNQUARAN**<br>**DELETE_RE**<br>**ISOLATE_M**<br>**UNISOLATE**|
||cn2Label|affectedMac|
||cn2|Number of a<br>for this reme|
||cn3Label|affectedElem|
||cn3Label|Number of a<br>remediation|
|RemediationDetails|cs2Label|malopID|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|remediationT|
||cs4|The type of<br>performed (<br>**UNSUSPEN**<br>**KILL_PREV**<br>**KILL_PROC**<br>**QUARANTI**<br>**UNQUARAN**<br>**DELETE_RE**<br>**ISOLATE_M**<br>**UNISOLATE**|
||cs5Label|affectedMac|
||cs5|Name for the<br>this remedia|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cs6Label|affectedElem|
||cs6|Unique iden<br>item for this|
||deviceCustomDate2Label|actionOccur|
||deviceCustomDate2|Time when t<br>remediation<br>failed for this|
|MachineIsolation|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cn2Label|affectedMac|
||cn2|Number of a<br>for this mach<br>operation|
|MachineIsolationDetails|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|affectedMac|
||cs4|Name for the<br>the machine|
||cs5Label|affectedMac|
||cs5|IP address f<br>machine for<br>isolation ope|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cs6Label|affectedMac|
||cs6|ID of the Cy<br>the target m|
||deviceCustomDate2Label|actionOccur|
||deviceCustomDate2|Time when t<br>isolation act<br>failed) for th|
|AbortRemediation|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|remediationT|
||cs4|The type of<br>performed (<br>**UNSUSPEN**<br>**KILL_PREV**<br>**KILL_PROC**<br>**QUARANTI**<br>**UNQUARAN**<br>**DELETE_RE**<br>**ISOLATE_M**<br>**UNISOLATE**|
|MalopComment|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|Link to the M<br>Cybereason|
||cs3|Link to the M<br>Cybereason|
|ManualCustomReputations|cs2Label|malopGuid|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|actionType|
||cs4|Type of actio<br>item (**Add**, **C**|
||cn2Label|affectedIOC|
||cn2|Number of I|
|CustomReputationsDetails|cs2Label|actionType|
||cs2|Type of prev<br>occurred (**A**<br>**Remove**)|
||cs3Label|IOCValue|
||cs3|Value added|
||cs4Label|IOCType|
||cs4|Type of item<br>**Domain**, or|
||cs5Label|IOCReputat|
||cs5|Reputation a<br>(**Whitelist** o|
||cs6Label|oldIOCRepu|
||cs6|Previous val<br>(**Whitelist** o|
||cn2Label|IOCPreventi|
||cn2|Current prev<br>item (**1** if ena<br>disabled)|
||cn3Label|oldIOCPreve|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cn3|Previous pre<br>item (**1** if ena<br>disabled) if t<br>**Change**|
||deviceCustomDate2Label|actionOccur|
||deviceCustomDate2|Time when t<br>update occu|
|StopMachineIsolation|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cn2Label|affectedMac|
||cn2|Number of a<br>for this oper|
|StopMachineIsolationDetails|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|affectedMac|
||cs4|Name for the<br>this operatio|
||cs5Label|affectedMac|
||cs5|IP address f<br>machine for|
||cs6Label|pylumID|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cs6|ID of the Cy<br>the target m|
||deviceCustomDate2Label|actionOccur|
||deviceCustomDate2|Time when t<br>isolation act<br>failed) for th|
|DeleteMalopComment|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
|GenerateReport|cs2Label|exportType|
||cs2|MalopRepor|
|GetFile|cs2Label|malopId|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|actionType|
||cs4|Type of prev<br>occurred (**A**<br>**Remove**)|
||cn2Label|affectedFileC|
||cn2|Number of f|
|GetFileDetails|cs2Label|malopId|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|linkToMalop|
||cs3|Link to the M<br>Cybereason|
||cs4Label|actionType|
||cs4|Type of prev<br>occurred (**A**<br>**Remove**)|
||cs5Label|fleName|
||cs5|Name of the|
||cs6Label|fleHash|
||cs6|Hash of the|
||deviceCustomDate2Label|actionOccur|
||deviceCustomDate2|Time when t<br>or failed for|
|MalopInboxAccess|No additional felds|N/A|
|CreateMalopLabel|cs2|createdLabe|
||cs2|The label tex|
|AddMalopLabel|cs2Label|malopID|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|createdLabe|
||cs3|The label ad<br>MalOp|
|RemoveMalopLabel|cs2Label|malopID|
||||


|Event name(s)|Field key name|Value|
|---|---|---|
||cs2|Unique iden<br>Cybereason<br>the MalOp o<br>took an actio|
||cs3Label|createdLabe|
|**REMOTE SHELL** action group extension felds<br>**Event name(s)**<br>**Field**<br>**key**<br>**name**<br>**Value**<br>Connect/Disconnect<br>cs2Label<br>remote_shell_mode<br>cs2<br>The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED<br>User Input<br>cs2Label<br>input<br>cs2<br>String with the command a<br>user ran.<br>cs3Label<br>remote_shell_mode<br>cs3<br>The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED<br>act<br>user_input<br>dvchost<br>Machine name for the<br>target machine for the<br>Remote shell utility session<br>src<br>IP address for the target<br>machine|**REMOTE SHELL** action group extension felds<br>**Event name(s)**<br>**Field**<br>**key**<br>**name**<br>**Value**<br>Connect/Disconnect<br>cs2Label<br>remote_shell_mode<br>cs2<br>The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED<br>User Input<br>cs2Label<br>input<br>cs2<br>String with the command a<br>user ran.<br>cs3Label<br>remote_shell_mode<br>cs3<br>The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED<br>act<br>user_input<br>dvchost<br>Machine name for the<br>target machine for the<br>Remote shell utility session<br>src<br>IP address for the target<br>machine|**REMOTE SHELL** action group extension felds<br>**Event name(s)**<br>**Field**<br>**key**<br>**name**<br>**Value**<br>Connect/Disconnect<br>cs2Label<br>remote_shell_mode<br>cs2<br>The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED<br>User Input<br>cs2Label<br>input<br>cs2<br>String with the command a<br>user ran.<br>cs3Label<br>remote_shell_mode<br>cs3<br>The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED<br>act<br>user_input<br>dvchost<br>Machine name for the<br>target machine for the<br>Remote shell utility session<br>src<br>IP address for the target<br>machine|


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
|Connect/Disconnect|cs2Label|remote_shell_mode|
||cs2|The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED|
|User Input|cs2Label|input|
||cs2|String with the command a<br>user ran.|
||cs3Label|remote_shell_mode|
||cs3|The mode for the Remote<br>Shell utility. Possible values<br>include:<br>DISABLED<br>RESTRICTED<br>NONE_RESTRICTED|
||act|user_input|
||dvchost|Machine name for the<br>target machine for the<br>Remote shell utility session|
||src|IP address for the target<br>machine|


**SECURITY PROFILE** action group extension fields




































|Event(s)|Field|Value|
|---|---|---|
|PowerShellProtectionMode,<br>PowerShellDownloadAndExecuteMode,<br>PowerShellMaliciousDownloadsMode,<br>PowerShellScriptAnalysisMode,<br>DotNetFloatingModulesMode|cs2Label|oldMode|
||cs2|Setting for the<br>mode before<br>user made a<br>change|
||cs3Label|newMode|
||cs3|New mode<br>setting<br>specifed by<br>user|
|PowerShellProcessExclusions|cs2Label|ActionType|
||cs2|Type of action<br>user<br>performed<br>with regards<br>to process<br>exclusions|
||cs3Label|ProcessName|
||cs3|Name of the<br>process the<br>user excluded<br>from Fileless<br>protection|
|PowerShellScriptAnalysisExclusions|cs2Label|ActionType|
||cs2|Type of action<br>user<br>performed<br>with regards<br>to script<br>analysis<br>exclusions|
||cs3Label|FunctionName|


|Event(s)|Field|Value|
|---|---|---|
||cs3|Pattern the<br>user excluded<br>from Fileless<br>protection<br>script analysis|


**SENSOR MANAGEMENT** action group extension fields












|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
|ManualArchiveInvoked|cn2Label|totalSensorsArchived|
||cn2|The number of senso<br>archived|
||cs2Label|previousStates|
||cs2|The previous state fo<br>were archived|
|ManualUnarchiveInvoked|cn2Label|totalSensorsUnarchiv|
||cn2|The number of senso<br>unarchived|
|SensorArchived|cs2Label|previousState|
||cs2|The previous state fo<br>was archived|
||cs3Label|sensorId|
||cs3|Unique identifer the<br>platform used for the|
|SensorUnarchived|cs2Label|sensorId|
||cs2|Unique identifer the<br>platform used for the|
|SensorDeleted|cs2Label|sensorId|
||cs2|Unique identifer the<br>platform used for the|


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
|ManualDeleteInvoked|cn2Label|totalDeletedSensors|
||cn2|The total number of s<br>from the**Sensors** sc|
|SensorDecommissioned|cs2Label|sensorId|
||cs2|Unique identifer the<br>platform used for the|
|ManualDecommissionInvoked|cn2Label|totalDecommissione|
||cn2|The total number of s<br>decommissioned|
|ManualRevertDecommissionInvoked|cn2Label|totalRevertedDecom|
||cn2|The total number of s<br>removed from**Decom**<br>status|
|SensorRevertDecommission|cs2Label|sensorId|
||cs2|Unique identifer the<br>platform used for the|
|SettingsChanged|No felds|N/A|
|EntityTagsCsvUpload|cn2|rowCount|
||cn2|Number of rows in th<br>CSV fle that was upl|
|EntityTagsCsvSubmit|cn2|rowCount|
||cn2|Number of rows in th<br>CSV fle that was upl|
|EntityTagsApiCalled|cn2|rowCount|
||cn2|Number of rows in th<br>CSV fle that was upl|
|EntityTagsEvent|cs2Label|eventLine|
||cs2|The tag that was upd|
|ManualAntiMalwareModesInvoked|cn2Label|totalMachines|
||||


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
||cn2|Total number of sens<br>Anti-Malware mode w<br>updated|
||cs2Label|antiMalwareState|
||cs2|The Anti-Malware mo<br>manually by the user|
||cs3Label|signatureAntivirusSta|
||cs3|The Anti-Malware > S<br>that was set manuall|
||cs4Label|staticAnalysisDetect|
||cs4|The Anti-Malware > A<br>Intelligence**Detect** m<br>manually by the user|
||cs5Label|staticAnalysisPreven|
||cs5|The Anti-Malware > A<br>Intelligence**Prevent**<br>set manually by the u|
|SensorAntiMalwareModesPreview|cs2Label|previousAntiMalware|
||cs2|The previous Anti-Ma|
||cs3Label|previousSignatureAn|
||cs3|The previous setting<br>Malware > Signature|
||cs4Label|previousStaticAnalys|
||cs4|The previous setting<br>Malware > Artifcial I<br>mode|
||cs5Label|previousStaticAnalys|
||cs5|The previous setting<br>Malware > Artifcial I<br>**Prevent** mode|
||cs7Label|sensorId|
||||


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
||cs7|Unique identifer the<br>platform used for the|
|CreatePolicy|cs2Label|confguration|
||cs2|The policy confgura|
|UpdatePolicy|cs2Label|confguration|
||cs2|The policy confgura<br>updated|
|AssignPolicy|cs2Label|policyId|
||cs2|The unique identifer<br>was assigned to a se|
||cn2Label|keepManualOverride|
||cn2|Whether or not to ke<br>sensor settings (**1** to<br>overrides,**0** to overri|
||cn3Label|numberOfSensors|
||cn3|The number of senso<br>policy was assigned|
|DeletePolicy|cs2Label|policyId|
||cs2|The unique identifer<br>platform uses for the<br>deleted|
||cs3Label|assignToPolicyId|
||cs3|The policy to which t<br>that previously had t<br>deleted|
|CreateGroup|cs2Label|groupId|
||cs2|The unique identifer<br>platform uses for the|
||cs2Label|groupName|
||cs2|The name for the sen|
||||


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
|EditGroup|cs2Label|groupId|
||cs2|The unique identifer<br>platform uses for the|
||cs3Label|groupName|
||cs3|The name for the sen|
|EditGroupsPriority|cs2Label|groupId|
||cs2|The unique identifer<br>Cybereason platform<br>group|
||cs3Label|priority|
||cs3|The priority assigned|
|DeleteGroup|cs2Label|deletedGroupId|
||cs2|The unique identifer<br>platform uses for the<br>deleted|
||cs3Label|reassignedToGroupI|
||cs3|The unique identifer<br>platform uses for the<br>assign sensors that w<br>assigned to the dele|
|AddSensorsToGroup|cs2Label|groupId|
||cs2|Unique identifer the<br>platform uses for the|
||cs3Label|flter|
||cs3|The flter used for au<br>assignment of senso|
||cn2Label|totalSensorCount|
||cn2|Number of sensors a<br>group|
||cn3Label|failureSensorCount|
||||


|Event name(s)|Field<br>key<br>name|Value|
|---|---|---|
||cn3|Number of sensors t<br>added to the group|
|RemoveSensorsFromGroup|cs2Label|groupId|
||cs2|Unique identifer the<br>platform uses for the|
||cs3Label|flter|
||cs3|The flter used for au<br>assignment of senso|
||cn2Label|totalSensorCount|
||cn2|Number of sensors a<br>group|
||cn3Label|failureSensorCount|
||cn3|Number of sensors t<br>added to the group|
|**USER MANAGEMENT** action group extension felds<br>**Event name(s)**<br>**Field key**<br>**name**<br>**Value**<br>Add user, Edit<br>user, Delete user<br>cs2Label<br>userFields<br>cs2<br>List of key-value pairs for<br>information on:<br>username<br>role(s)<br>assigned group(s)<br>login method<br>two factor<br>authentication status<br>notifcation status|**USER MANAGEMENT** action group extension felds<br>**Event name(s)**<br>**Field key**<br>**name**<br>**Value**<br>Add user, Edit<br>user, Delete user<br>cs2Label<br>userFields<br>cs2<br>List of key-value pairs for<br>information on:<br>username<br>role(s)<br>assigned group(s)<br>login method<br>two factor<br>authentication status<br>notifcation status|**USER MANAGEMENT** action group extension felds<br>**Event name(s)**<br>**Field key**<br>**name**<br>**Value**<br>Add user, Edit<br>user, Delete user<br>cs2Label<br>userFields<br>cs2<br>List of key-value pairs for<br>information on:<br>username<br>role(s)<br>assigned group(s)<br>login method<br>two factor<br>authentication status<br>notifcation status|


|Event name(s)|Field key<br>name|Value|
|---|---|---|
|Add user, Edit<br>user, Delete user|cs2Label|userFields|
||cs2|List of key-value pairs for<br>information on:<br>username<br>role(s)<br>assigned group(s)<br>login method<br>two factor<br>authentication status<br>notifcation status|


**IR TOOLS** action group extension fields
























|Event name(s)|Field key<br>name|Value|
|---|---|---|
|DeliverPackage|cs2Label|packageName|
||cs2|The unique name of the<br>IR tool package that<br>was deployed|
||cs3Label|packageSize|
||cs3|The size of the package<br>deployed|
||cs4Label|sensorContentType|
||cs4|The version of the<br>package|
||cs5Label|owner|
||cs5|Owner of the tool<br>package|
|DeliverPackageDetails|cs2Label|packageName|
||cs2|The unique name of the<br>IR tools package to<br>deploy|
||cs3Label|supportedOS|
||cs3|The supported<br>operating systems<br>where the package was<br>deployed|
|DeletePackage|cs2Label|packageName|
||cs2|The unique name of the<br>IR tool package<br>removed from endpoint<br>machines|





