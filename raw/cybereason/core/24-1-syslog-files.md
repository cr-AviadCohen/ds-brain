|Log|Log file name|Triggering<br>event|Location|
|---|---|---|---|
|Malop<br>syslog|syslog.log|When a Malop<br>is generated or<br>updated|Detection<br>servers|


|Log|Log file name|Triggering<br>event|Location|
|---|---|---|---|
|Malware<br>syslog|syslog.log|When a<br>malware alert is<br>generated or<br>updated<br>Note<br>Since<br>Malware<br>alerts also<br>cause the<br>creation of<br>a Endpoint<br>Protection<br>MalOp, you<br>will fnd<br>them both<br>in this same<br>syslog.log<br>fle as AI<br>Hunting<br>MalOps.|WebApp<br>server|
|User<br>Audit<br>syslog|userAuditSyslog.log|When a<br>Cybereason<br>user performs<br>an action|WebApp<br>server|



[See Syslog Messages (/s/knowledge-base?article=24-1-syslog-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages&language=en_US#syslog-messages)

[messages&language=en_US#syslog-messages) for details on the](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages&language=en_US#syslog-messages)


syslog messages in the logs you download.

## Retrieve syslog files


Users with the System Admin role can download the MalOp and


User Audit syslog files.

## MalOp syslog


To download the MalOp syslog, navigate to the **System >**


**Overview** screen and click **Fetch logs** .


When you click this option, the platform downloads all logs for the


selected Detection Server server. The MalOp syslog (syslog.log) is

included among them. You can select which server to display



