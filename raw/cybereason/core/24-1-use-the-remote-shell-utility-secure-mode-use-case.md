To do this, you use the Remote Shell utility.


In the **Investigation** screen, click **Remote Shell** . You are then

prompted to select your machine:


The Remote Utility screen opens directly in the Cybereason

platform window.


At first, the command line window is empty, without a cursor. This

is because your Cybereason server is establishing the connection


between itself and the machine and the connection:


Once the status at the top of the window changes to Online, the


cursor appears and the command line is ready to use.


Because you remember that the process in question created a


number of registry entries, you run the command to list the registry

entries from the key the process used:

```
 Get-Item -Path

 Registry::HKEY_CURRENT_USER\SOFTWARE\Mic

 rosoft\Windows\CurrentVersion\Run

```

The command returns the list of registry entries created. You read


the list of commands and find the ones the process created.


Then, you run a command to delete the necessary entries:

```
 Remove-ItemProperty -Path

 "HKLM:\Software\SmpApplication" -Name

 "SmpProperty"

```

You also do the same for the scheduled tasks the process


created.


You then go to the folder containing the malicious file that runs the


process is located. Using the Windows API you quarantine the file
and explore other files in the same directory. Since you find a


number of them worth further investigation, you compress the files
into zip file.


After you finish, you return to the Remote Shell window and click

**End Session** to close the connection.


Back in the Cybereason UI, you use the File Search window to


locate and download the files.


Your Cybereason WebApp server saves a record of all commands


used and responses to the server logs. Users with the **System**

**Admin** role can retrieve these logs after a session is complete.


Sensor logs note any connections to the machine from the Remote
Shell utility and system changes such as file modification, etc.).
