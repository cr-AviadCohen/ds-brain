The Remote Utility screen opens directly in the Cybereason


platform screen.


At first, the command line window is empty, without a cursor. This


is because your Cybereason server is establishing the connection

between itself and the machine and the connection:


Once the status at the top of the window changes to Online, the

cursor appears and the command line is ready to use.


To download the script, you run the following command:

```
 Invoke-WebRequest -Uri $url -OutFile

 $output" (For example : Invoke
 WebRequest -Uri

 "https://www.robvanderwoude.com/files/me

 mory_ps.txt

 (https://www.robvanderwoude.com/files/me

 mory_ps.txt)" -OutFile "script.ps1

```

In addition, you run the following command to enable script


execution (a PowerShell requirement):

```
 Set-ExecutionPolicy -ExecutionPolicy

 Unrestricted

```

Then, you run the downloaded script using regular PowerShell


execution. The script runs and the results return automatically.



