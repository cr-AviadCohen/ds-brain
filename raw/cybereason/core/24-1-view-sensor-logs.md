Here is an example of accessing the Anti-Malware (signatures


feature) log:


1. On the machine, in the `C:\ProgramData\apv2\Logs` folder,


find the **AmSvc.log** log file, alongside the other sensor log
files:


1. Open the file. Here is how it appears, displaying notifications


of first time update and malware detection:

## Find log files on sensor machines


If a sensor is not connected and you need to troubleshoot an


issue on the sensor, you can access sensor logs directly on the

machine. The tables below show the location and name of log


files.


**Machines with Windows 7 and higher or Windows Server 2008**


**and higher:**
















|Log type|Log name|Log location|Col4|
|---|---|---|---|
|Sensor logs|Several log fles. Main log fle<br>is:<br>CybereasonActiveProbe.log|C:\ProgramData\apv||
|Sensor<br>communication<br>logs|CybereasonActiveConsole.log|C:\ProgramData\apv||
|Anti-Malware<br>signatures log|AmSvc.log|C:\ProgramData\apv||
|Anti-<br>Ransomware<br>log|CybereasonCrs.log|C:\ProgramData\crs1||


|Log type|Log name|Log location|
|---|---|---|
|Execution<br>Prevention<br>service log|CRExecPrev.log|C:\ProgramData\crb1|
|Application<br>Control log|AcScanner.log|C:\ProgramData\crb1|
|Anti-Malware<br>(artifcial<br>intelligence)<br>log|NGAV.log|C:\ProgramData\crb1|




|Operating system|Sensor log location|
|---|---|
|Mac|/usr/local/cybereason/Logs|
|Linux|/opt/cybereason/sensor/Logs/|





