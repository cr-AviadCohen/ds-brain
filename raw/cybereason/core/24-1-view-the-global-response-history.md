|Column|Description|
|---|---|
|Action name|The name of the remediation action.|
|Response<br>integration|The platform that performed the remediation<br>actions.<br>If the action was performed on an endpoint<br>machine connected to your Cybereason<br>platform, the integration is**Cybereason EDR**.|
|Request<br>time|The time that the user performed the action in<br>the Cybereason platform.|
|Execution<br>time|The time the action was performed on the<br>target.<br>This time may be signifcantly later than the<br>**Request time** if the target was offine or<br>unreachable when the action was performed in<br>the Cybereason platform.|
|Status|The status of the action execution. If there was<br>an issue with performing the action, this<br>column displays details on the error. Hover<br>over the**Failed** value to learn more about the<br>error.|
|Indicator|The target Element for the action, such as<br>process name.|
|Target<br>identity|The target machine or user associated with the<br>action.|
|Related<br>Malop|The MalOp associated with this remediation<br>action. You can click on the MalOp ID to open<br>the Malop Details screen for that MalOp.|
|Committed<br>by|The Cybereason user that performed the<br>remediation action.|







