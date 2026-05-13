|Area|Details|
|---|---|
|Malop<br>comments|Using double quotes in a MalOp comment is<br>not supported.|


|Area|Details|
|---|---|
|Remediation<br>actions|It is not always possible to quarantine fles<br>on network drives, in cases where the<br>machine's user lacks permissions to<br>perform operations on the network drive.<br>In the**Malop details** screen, if the MalOp<br>has hundreds of processes, if you click<br>**Investigate** to investigate all the<br>processes at once, the Investigation<br>screen may take a long time to load. In<br>this case, we recommend investigating<br>individual processes from the<br>Investigation screen.<br>When printing a MalOp report, the date<br>format for localized reports is partly<br>displayed in English.<br>Preventing fles from executing using the<br>Application Control feature is not<br>considered a remediation option and thus<br>cannot be sent to offine sensors.<br>However, the action will appear in the<br>**Response history** if it was performed in<br>conjunction with a remediation action.<br>Machine isolation requires the Windows<br>Base Filtering Engine (BFE) service to be<br>running. This service is normally running.<br>If the BFE service is not running for any<br>reason, restart the BFE service and<br>reattempt to isolate the machine.<br>In environments that use the Dynamic<br>Host Confguration Protocol (DHCP)<br>protocol to allocate IP addresses<br>dynamically, the Cybereason platform<br>machine isolation exclusions rules may<br>not function properly since these rules are<br>based on IP addresses. In addition, in<br>some cases, dynamic IP addresses may<br>result in server connectivity problems due<br>to networking issues. If this occurs, you<br>should work with your IT teams to resolve<br>server connectivity issues.<br>Isolating machines is not supported for<br>endpoint machines running on SLES and<br>CentOS 6 operating systems.<br>For sensors running on macOS Big Sur<br>machines, when you add a fle to the<br>blocklist, quarantine the fle, and then<br>click the**Respond** button for the related<br>MalOp in the Malops management|


|Area|Details|
|---|---|
||screen, the**Quarantine fle** action is still<br>available even though the fle has already<br>been quarantined.<br>If you install a sensor on a machine<br>running macOS Big Sur, isolate the<br>machine running the sensor, and then<br>remove the sensor, the machine remains<br>isolated.|
|Remediation<br>of offine<br>sensors|Actions sent to offine sensors are listed<br>as**Pending** in the**Response history** UI<br>view. If the Detection server is restarted<br>before the action is completed, the action<br>will have a**Failed** status.<br>When performing actions on offine<br>sensors Cybereason will record all actions<br>even if another action of the same type is<br>pending. When updating the response<br>history, Cybereason will update only the<br>latest entry; all others will remain in the<br>**Pending** state.<br>For remediation actions sent to offine<br>sensors, the action may take up to<br>approximately 10 minutes to execute after<br>the sensor comes online.|







