|Element UI Name|Description|
|---|---|
|Automatic Execution|An operation that is run automatically.|
|Connection|A connection operation between<br>machines, processes, and so forth.|
|DNS query resolved<br>Domain to Domain|A DNS query from one domain to<br>another that was resolved.|


|Element UI Name|Description|
|---|---|
|DNS query resolved<br>Domain to IP|A DNS query from a Domain to an IP<br>address that was resolved.|
|DNS query resolved<br>IP to Domain|A DNS query from an IP to a Domain<br>that was resolved.|
|DNS query<br>unresolved from<br>Domain|A DNS query from a domain that is<br>still not resolved.|
|DNS query<br>unresolved from IP|A DNS query from an IP address that<br>is still not resolved.|
|Domain Name|The name of a domain.|
|Driver|A driver for a machine, process, and<br>so forth.|
|File|A fle involved in an operation.|
|File Event|Operation performed by a process on<br>a fle.|
|Function Details|The information about a function<br>running|
|Hosts File|The fle on an operating system that<br>maps host names to IP addresses.|
|Image fle|The fle from the disk that executes<br>the process.|
|IP Address|The IP address of an operation.|
|IP Range Scan|An operation that scans the IP<br>addresses in a range.|
|Listening connection|The connection on the machine that<br>listens for incoming connection<br>requests.|
|Local network|A LAN for a specifc area.|
|Logon session|A computing session beginning with<br>successful logon and ending with a<br>user log off operation.|
|Machine|The machine involved in an operation.|


|Element UI Name|Description|
|---|---|
|Malop Logon session|The specifc computing session when<br>the user was logged on in which a<br>MalOp was created.|
|Malop Process|The specifc process involved in a<br>MalOp.|
|Module|The module involved in an operation.|
|Mount point|A directory on which an accessible<br>fle system is mounted.|
|Network Interface|The interface between two items in a<br>computer network.|
|Network Machine|A machine running on a network<br>involved in an operation.|
|Process|The process involved in an operation.|
|Proxy|The proxy used for a connection.|
|QuarantineFile|The fle involved in a quarantine<br>operation.|
|Registry Entry|An item in the computer's registry.|
|Registry Event|An event performed on a specifc<br>registry entry.|
|Remote Session|A computing session where a user<br>accesses a machine running in a<br>remote place.|
|Scheduled task|A task scheduled to run at a certain<br>time by the operating system's task<br>scheduler.|
|Scheduled task<br>action|The action that runs when a task runs<br>from the task scheduler.|
|Service|A service involved in an operation.|
|User|The user involved in an operation.|
|Wmi Persistent<br>Object|An object created when working with<br>the WMI capability of the Windows<br>operating system.|


Each Element type has descriptive Features. Features are


characteristics of a Element. These characteristics include

properties of the Element, such as the name of the Element, or


behaviors of the Element. Some Features enable you visibility into

what an Element is doing.


[For a full list of Features per Element, see the Query Elements and](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

[Features (/s/knowledge-base?article=query-api-token-query-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[elements-and-features-version-232148-and-later) in the](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

Cybereason API documentation.


For example, the Cybereason platform uses Features for

processes (the **Process** Element) such as these:


The name of the process -> **Process name** feature

The ID number of the thread the process uses -> **Thread ID**


feature

Process opens a connection to a known malicious IP address


-> **Connecting to a Known Malicious Address** feature

Process opens a module in a temporary folder -> **Module in**


**temporary folder** feature

Command line the process uses to run -> **Command line**


feature


You can use evidence and suspicions created through


Cybereason detection rules as Features. If a Feature is a evidence

or suspicion Feature, it displays an icon:


Evidence uses an eye icon ( ).


Suspicion uses the Suspicion icon ( ).


Features that are not evidence or suspicions use a filter icon (


).



