```
 CEF:1|Cybereason|Cybereason||Malop|Malop

 Created|10|

 cs1Label=malopId cs1=

 <xx.xxxxxxxxxxxxxxxxxxx>

 cs2Label=malopDetectionType

 cs2=MalopProcess

 cs3Label=malopActivityType

 cs3=LATERAL_MOVEMENT

 cs4Label=malopSuspect cs4=mimikatz.exe

 cs5Label=malopKeySuspicion

 cs5=Credential Theft Malop

 cs6Label=linkToMalop

 cs6=localhost:8080/#/malop/<xx.xxxxxxxxx

 xxxxxxxxxx>

 cn1Label=affectedMachinesCount cn1=1

 cn2Label=affectedUsers

 cn2=1 cn3Label=isSigned cn3=0

 start=Dec 19 2017, 15:58:14 IST

 rt=Dec 19 2017, 15:58:14 IST

 requestContext=mimikatz.exe

 reason=blacklist

## MalOp machine details updated

```

The following example show a syslog message for updating a


MalOp with machine details.

```
 CEF:1|Cybereason|Cybereason||Malop|Malop

 Machine Information|10|

 cs1Label=malopId cs1=

 <xx.xxxxxxxxxxxxxxxxxxx>

 cs2Label=affectedMachine cs2=<xxxxx>

 cn1Label=affectedMachinesCount

 cn1=1 cs3Label=parentProcess cs3=1724

 cs4Label=childrenProcess cs4=[]

 cs5Label=OSVersion cs5=Windows_10 c

 n2Label=isOnline cn2=1

 cn3Label=isOriginalMachine cn3=1

 rt=Dec 19 2017, 15:58:14 IST

 suser=ieuser dvc=<xx.x.x.xx>

```

## User Action syslog messages

This section contains various examples taken from the User Action


syslog.


The following example show a syslog message for a user login.

```
 May 16 03:10:41 admin-host

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 General/Login|0|cs1Label=username

 cs1=/admin@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 16 2023, 03:10:41

 UTC cs2Label=loginMethod cs2=CERTIFICATE

 cs3Label=userRole

 cs3=executive/user_admin/sys_admin/analy

 zer/analyst_l3/api cs4Label=machineName

 cs4=adminhost cs5Label=machineIP

 cs5=12.34.56.78

## Add a comment to a MalOp

```

The following example show a syslog message for when a


comment was added to a MalOp.

```
 May 18 05:40:21 admin-host

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 Malop

 Investigation/MalopComment|0|cs1Label=us

 ername cs1=/admin@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 18 2023, 05:40:19

 UTC cs2Label=malopId

 cs2=AAAA07yggO88yCJQ

 cs3Label=linkToMalop

 cs3=https://myserver.cybereason.net:443/

 #/malop/AAAA07yggO88yCJQ

 (https://myserver.cybereason.net:443/#/m

 alop/AAAA07yggO88yCJQ)

```

## Change a MalOp's status

The following example show a syslog message for when an


analyst changed the status of a MalOp.

```
 May 25 13:09:26 ses-445

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 Malop

 Investigation/ChangeMalopState|0|cs1Labe

 l=username cs1=/admin@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 25 2023, 13:09:24

 UTC cs2Label=malopID

 cs2=AAAA0xaUuGXeyJVF

 cs3Label=linkToMalop

 cs3=https://myserver.cybereason.net:443/

 #/malop/AAAA0xaUuGXeyJVF

 (https://myserver.cybereason.net:443/#/m

 alop/AAAA0xaUuGXeyJVF) cs4Label=oldState

 cs4=ToReview cs5Label=newState

 cs5=ToReview

## Malop remediation

```

The following example show a syslog message for a remediation


action on a MalOp.


```
 May 23 09:47:51 admin-hot

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 Malop

 Investigation/RemediationDetails|0|cs1La

 bel=username cs1=/analystl3@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 23 2023, 09:47:51

 UTC cs2Label=malopID cs2=NOMALOP

 cs3Label=linkToMalop

 cs3=ERROR_GETTING_MALOLP_EXTERNAL_LINK

 cs4Label=remediationType

 cs4=UNISOLATE_MACHINE

 cs5Label=affectedMachineName

 cs5=842037066.1198775089551518743

 cs6Label=affectedElement cs6=

 deviceCustomDate2Label=actionOccurranceT

 ime deviceCustomDate2=May 23 2023,

 09:47:51 UTC

## Machine isolation

```

The following example show a syslog message for a machine


isolation action on a MalOp.

```
 May 23 09:47:50 admin-host

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 Malop

 Investigation/MachineIsolation|0|cs1Labe

 l=username cs1=/analystl3@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 23 2023, 09:47:50

 UTC cs2Label=malopId cs2=

 cs3Label=linkToMalop cs3=

 cn2Label=affectedMachineCount cn2=1

## Run investigation query

```

The following example show a syslog message for a user running

an investigation query.


```
 May 16 03:27:34 admin-host

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 Investigation/Query|0|cs1Label=username

 cs1=/admin@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 16 2023, 03:27:34

 UTC cs2Label=QueryDetails cs2=Module >

 Process cs3Label=QueryParameters

 cs3=Module: elementDisplayName Equals

 FWPolicyIOMgr.DLL {FLOATING},

 desktopthemes.dll {FLOATING}, isFloating

 true > Process: creationTime Between

 1684103281000, 1684189681000

## Remote Shell utility use

```

The following example show a syslog message for a user


connecting to a machine with the Remote Shell utility.

```
 May 25 11:38:15 admin-host

 auditSyslogLogger

 CEF:0|Cybereason|Cybereason||UserAction|

 Remote Shell/Connect|0|cs1Label=username

 cs1=/analystl3@myserver.com

 cn1Label=actionSuccess cn1=1

 deviceCustomDate1Label=userActionTime

 deviceCustomDate1=May 25 2023, 11:38:15

 UTC cs2Label=remote_shell_mode

 cs2=NON_RESTRICTED act=connect

 dvchost=ad src=12.34.56.78

## Behavioral whitelisting

```

The following example show a syslog message for a previewing


the effect of a behavioral whitelisting rule on existing MalOps.



