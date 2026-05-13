## Collected System-Level data

Cybereason sensors collect the following system-level data:


Note


OS support varies for different system-level data collections


are supported. For details on the supported operating systems

[for each collection, see Endpoint machine data collection](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-data-collection-features)


[features (/s/knowledge-base?article=24-1-supported-features-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-data-collection-features)

[by-operating-system&language=en_US#endpoint-machine-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-data-collection-features)


[data-collection-features).](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-data-collection-features)








|Data Type|Description|Information Collected|
|---|---|---|
|Connections|Any connection<br>opened on a<br>machine.|Connection properties,<br>including address/port,<br>direction, connection<br>origin, and connection<br>state<br>Data transmitted, both<br>received bytes and<br>transmitted bytes<br>Creation time, end<br>time, and the frst time<br>the connection was<br>seen by Cybereason<br>Remote port or server<br>address and port used<br>by the connection<br>Transport protocol<br>Machines and<br>processes involved in<br>the connection<br>DNS query and<br>domains in the<br>connection<br>Proxies utilized by the<br>connection|


|Data Type|Description|Information Collected|
|---|---|---|
|DNS query<br>(all types)|Requests to a<br>particular site or<br>address to get<br>the domain<br>name.|Resolved Domain-to-<br>Domain<br>Resolved Domain-to-IP<br>Resolved IP-to-Domain<br>Unresolved to Domain<br>Unresolved to IP<br>DNS queries can also be<br>called**Domain request**<br>**and response**. Collected<br>information includes:<br>Source and target<br>domains<br>The resolving server for<br>the DNS request and<br>resolution status<br>Record type for the<br>DNS request<br>TTL range for the DNS<br>query resolution<br>Error codes sent for<br>unresolved DNS<br>queries|
|Drivers|All drivers<br>currently<br>installed on the<br>machine.|Driver properties,<br>including name, path,<br>hash value, version,<br>and size<br>Creation time<br>File associated with the<br>driver<br>Machine name on<br>which the driver is<br>found<br>Services associated<br>with the driver|


|Data Type|Description|Information Collected|
|---|---|---|
|Files|Details about<br>the fle, its<br>properties,<br>internal details,<br>and behavior.|Properties, including<br>name, path, size, fle<br>type, fle version,<br>extension types<br>Description information<br>from fle metadata,<br>including description,<br>product name and title<br>for the program that<br>created the fle,<br>product type and<br>version, company<br>name, internal fle<br>name, legal copyright,<br>legal trademarks,<br>private build markers,<br>special build markers,<br>and comments added<br>to the fle<br>Hash values (MD5,<br>SHA-1, and SHA-256<br>values)<br>Signatures (both MD5<br>and SHA1) and signer<br>details<br>Creation and end times<br>of the fle and the last<br>time the fle was<br>modifed<br>Download details,<br>including the email<br>address of the person<br>sending the fle, email<br>message ID, email<br>subject of the email<br>containing the fle, or<br>the URL from which the<br>fle was downloaded<br>Machine name on<br>which the fle is found<br>Original fle name and<br>fle version if a fle is<br>quarantined<br>Scan information and<br>remediation status<br>Security user ID for the<br>user opening the fle|


|Data Type|Description|Information Collected|
|---|---|---|
|File events|CREATE,<br>RENAME, and<br>DELETE<br>operations on<br>fles.|Event type<br>The frst time<br>Cybereason collected<br>the fle event<br>The fle on which the<br>fle event is performed<br>The machine on which<br>the fle event occurs<br>The process that<br>performed the fle<br>event<br>The user currently<br>logged into the<br>machine on which the<br>fle event occurs|
|Hosts fle|Details<br>translating IP<br>addresses or<br>domain names<br>into other names<br>on a specifc<br>machine.|The number of entries<br>in the fle<br>The machine name on<br>which the hosts fle is<br>found<br>DNS entries in the<br>hosts fle|
|IP Address|IP addresses for<br>connections.|The numerical address<br>Physical location<br>information, including<br>city, country name and<br>code, region, and<br>latitude/longitude<br>The IP version<br>The name of the<br>machine to which the<br>IP address belongs<br>Related DHCP and<br>network interfaces|
|IP Range<br>Scans|IP addresses<br>retrieved from<br>scan process.|The range of IP<br>addresses<br>The creation time of the<br>scan<br>The process<br>performing the scan|


|Data Type|Description|Information Collected|
|---|---|---|
|Listening<br>Connection|Any listening<br>connection<br>opened on a<br>machine.|Local address and port<br>used by the connection<br>Transport protocol the<br>connection uses<br>Address type the<br>connection uses<br>End time for the<br>connection<br>Machine name on<br>which the listening<br>connection is found<br>Owner process for the<br>listening connection|
|Local<br>Network|Information on<br>the local<br>network|Address details,<br>including the gateway<br>IP, gateway MAC<br>address and MAC<br>address format<br>DHCP and DNS server<br>addresses<br>Machine name on<br>which the local network<br>is found<br>Default search domain<br>for the network<br>Wif SSID<br>IP ranges on the local<br>network|


|Data Type|Description|Information Collected|
|---|---|---|
|Logon<br>Sessions|Details for logon<br>sessions.|Session IP<br>Session UID<br>Source IP<br>Windows logon details<br>for the session<br>Logon application and<br>type used to log on to<br>the session<br>Creation and end time<br>and the last time the<br>logon session was<br>seen by Cybereason<br>Machines involved in<br>the logon session<br>Remote machine or<br>remote network<br>machine names<br>involved in the session<br>Client logon sessions<br>associated with this<br>logon session<br>Processes opened in<br>the logon session<br>User who opened the<br>logon session|


|Data Type|Description|Information Collected|
|---|---|---|
|Machine|Machine details|Machine properties,<br>including name and<br>FQDN, model, machine<br>type, operating system<br>type, platform, and<br>organization<br>Last time the machine<br>was seen by<br>Cybereason and last<br>connection time<br>Performance statistics,<br>including CPU count,<br>total and free disk<br>space, and free<br>memory<br>First active user on the<br>machine<br>Hash value of the<br>Master Boot Record<br>Processes running on<br>the machine<br>Users logged into the<br>machine<br>Services running on<br>the machine<br>Removable devices<br>and mount points<br>connected to the<br>machine<br>Device model and<br>serial number (on<br>macOS machines in<br>versions 23.1.44 and<br>later)|


|Data Type|Description|Information Collected|
|---|---|---|
|Modules|All modules<br>running on the<br>machine.|Module properties<br>including module<br>name, size, hash value,<br>and address<br>Allocated protection for<br>the module<br>Header allocated size<br>Header protection<br>End time for the<br>module<br>File associated with the<br>module<br>Machine on which the<br>module is found<br>Modules found in the<br>operating system<br>standard load<br>database<br>Registry keys<br>associated with the<br>module<br>Address to which the<br>module was loaded|
|Mount<br>Points|Associated<br>mount points.|Mount point properties,<br>including drive/volume<br>name, device name,<br>and mount point type<br>Source of the mount<br>point<br>Creation time and end<br>time for the mount<br>point<br>Machine on which the<br>mount point is found<br>User and user<br>credentials used to<br>create the mount point<br>The fles associated<br>with the mount point|


|Data Type|Description|Information Collected|
|---|---|---|
|Network<br>Interface|Information on<br>the network<br>interface.|Interface ID<br>Address details<br>including gateway IP<br>and internal IP<br>MAC address format<br>Related server<br>information for the<br>interface's DHCP and<br>NDS servers<br>IP addresses<br>associated with the<br>network interface<br>End time of the<br>interface<br>Transaction statistics<br>for the interface<br>Network interface fags<br>Machine name on<br>which the interface is<br>found<br>Proxies used by the<br>interface<br>Local networks using<br>the interface|
|Network<br>Machine|Information on<br>the network<br>machine.|Host name<br>Domain FQDN|


|Data Type|Description|Information Collected|
|---|---|---|
|Processes|Short-lived and<br>long-lived<br>process<br>information. On<br>Linux machines,<br>these processes<br>may display as<br>aggregated<br>processes.|Process properties,<br>including ID, fle hash,<br>state, functions, path,<br>integrity, CPU/memory<br>usage, RWX sections,<br>and hidden process<br>status<br>Process hierarchy<br>Creation and end time,<br>and the frst and last<br>time seen by<br>Cybereason<br>User and machine<br>information about the<br>process<br>Connections (with IP<br>address/domain name)<br>that the process<br>opens, connection<br>source, data<br>transmitted by the<br>process, and<br>download information<br>Files opened by the<br>process and fle events<br>performed on these<br>fles<br>Process command line<br>Modules associated<br>and loaded by the<br>process<br>Process injection<br>details, including<br>Thread IDs and count,<br>and injected processes<br>or threads and the<br>injection method<br>Details on the process<br>image fle, including<br>hash value, extension,<br>path, and signature<br>WMI details, including<br>the source of the WMI<br>activity, cause, queries<br>used, and WMI<br>persistent objects<br>created<br>Windows opened by<br>the process|


|Data Type|Description|Information Collected|
|---|---|---|
|||Details on what the<br>process has<br>downloaded<br>Changes in the input or<br>output used by the<br>process (in versions<br>23.2.8X and later)|
|Proxy|All proxies<br>confgured on<br>the machine.|IP address for the<br>proxy<br>URL for the proxy PAC<br>fle<br>Port the proxy uses<br>Host name<br>Discovery type used<br>for the proxy|
|Quarantine<br>File|The version of a<br>fle after it has<br>been<br>quarantined by<br>the Cybereason<br>platform.|MD5 and SHA1 hash<br>values for the fle<br>Original fle name<br>Creation time of the<br>quarantined fle (not<br>the original fle)|
|Registry<br>Entry|Specifc registry<br>keys associated<br>with autoruns.|Registry key for this<br>entry<br>Value of the registry<br>entry<br>End time of the entry<br>Machine name on<br>which this entry is<br>found|
|Registry<br>Events|Specifed<br>registry keys<br>that you select.|Registry key<br>associated with this<br>registry event<br>Path to the registry key<br>Data and data type in<br>the registry key<br>Process and machine<br>for the registry key<br>associated with the<br>registry events|


|Data Type|Description|Information Collected|
|---|---|---|
|Remote<br>Logon<br>Sessions|Information on<br>remote logon<br>sessions.|Authentication protocol<br>used for the remote<br>session<br>Client machine, client<br>machine user, and<br>client remote session<br>Server machine and<br>logon session<br>First time the remote<br>session was detected<br>by Cybereason<br>Resource type for the<br>remote session<br>User that started the<br>remote session<br>Processes opened<br>during the remote<br>session|
|Remote<br>Procedure<br>Calls|Information<br>about select<br>Remote<br>Procedure Call<br>(RPC)<br>operations<br>associated with<br>the machine (in<br>the MS-RPC<br>Element.|Authentication level<br>used by the RPC<br>operation<br>Authentication service<br>used by the RPC<br>operation<br>Target port and target<br>IP address for the RPC<br>operation<br>Source for the RPC<br>operation<br>Impersonation level for<br>the RPC operation<br>UUID and unique<br>operation number<br>generated by the<br>machine for the RPC<br>operation<br>Protocol used by the<br>RPC operation<br>Process that created<br>the RPC operation<br>Machine on which the<br>RPC operation ran|


|Data Type|Description|Information Collected|
|---|---|---|
|Scheduled<br>Task|Information on<br>scheduled<br>tasks.|User who created the<br>scheduled task and<br>the last user to update<br>the task<br>Scheduled task state<br>Task status<br>Last time the task was<br>run<br>Machine name on<br>which the scheduled<br>task is found|
|Scheduled<br>Task Actions|Information on<br>scheduled task<br>actions.|Action arguments<br>Path to the scheduled<br>task for the action<br>File associated with the<br>scheduled task action|
|Service|All services<br>currently<br>running on a<br>machine.|Service properties<br>including service state<br>and sub-state, service<br>type, and service<br>characteristics<br>Login name used by<br>the service when it<br>runs<br>Binary fle associated<br>with the service<br>Command line used by<br>the program that runs<br>the service<br>Unit fle path for the fle<br>associated with the<br>service<br>System process status<br>for the process<br>associated with the<br>service<br>Process that created<br>the service<br>Machine on which the<br>service is running<br>Drivers associated with<br>the service<br>End time for the<br>service|


|Data Type|Description|Information Collected|
|---|---|---|
|Users|Information on<br>all users.|User properties,<br>including user name<br>and organization,<br>domain, and privilege<br>levels<br>Security identifer (SID)<br>Last login time<br>Number of days since<br>a password change<br>Machine names and<br>number of machines to<br>which this user is<br>logged into<br>Processes the user is<br>running<br>Number of<br>downloaded processes|
|WMI Activity|Information on<br>both local WMI<br>activity and<br>remote WMI<br>activity. While<br>this is<br>information is<br>collected<br>separately from<br>other Elements,<br>the WMI activity<br>is reported<br>under Process<br>activity details.|Operation that created<br>the WMI activity<br>Source of the WMI<br>activity<br>Creation time for the<br>WMI activity<br>WMI client information,<br>including the IP<br>address, machine<br>name, and process<br>creating the WMI<br>activity<br>Executed processes<br>and server processes<br>in the context of the<br>WMI activity<br>WMI persistent objects<br>created by the WMI<br>activity<br>WMI queries used in<br>the context of the WMI<br>activity|


|Data Type|Description|Information Collected|
|---|---|---|
|WMI<br>Persistent<br>Objects|Information on<br>WMI persistent<br>objects.|WMI client information,<br>including the IP<br>address, machine<br>name, and process<br>creating the WMI<br>activity<br>Persistent object<br>consumer details,<br>including the consumer<br>name, action, fle path,<br>and image fle<br>Process that created<br>the object<br>Filter details<br>Machine name on<br>which the WMI<br>Persistent object is<br>found|



The Cybereason platform collects data in all languages. The data


is displayed according to the endpoint sensor OS language.


Note


Sensors do not collect the file content, or network packet

[information. Analysts can Search for Files on Machines](https://nest.cybereason.com/s/knowledge-base?article=24-1-search-for-files-on-machines&language=en_US#search-for-files-on-machines)


[(/s/knowledge-base?article=24-1-search-for-files-on-](https://nest.cybereason.com/s/knowledge-base?article=24-1-search-for-files-on-machines&language=en_US#search-for-files-on-machines)
[machines&language=en_US#search-for-files-on-machines) to](https://nest.cybereason.com/s/knowledge-base?article=24-1-search-for-files-on-machines&language=en_US#search-for-files-on-machines)


gain further insight into potentially malicious files.

## Collected Active Directory data


Each sensor gathers the following Active Directory information for


the machine and its users every 30 minutes:


**User attributes** :


SID

Display name


User principal name

Department


Company

Email


sAMAccountName

Primary GroupId


Member Of (multiple values)

Organizational Units (multiple values)


Country


Title

Created Time


**Machine attributes** :


SID


Description

Organizational Units (multiple values)


DNS Host Name

Location


Office


YOU can use the **Investigation** screen to search for specific


Active Directory data. The following screen shot displays the **User**
Element's Active Directory filters.


Note


Not every Active Directory-related filter has the term 'Active


Directory' in the title.

## Enable or disable collections


You can enable or disable data collection processes at the sensor


level from the **System > Sensors** screen:


Note


To enable or disable data collection, you must ensure that the


sensor not assigned to a sensor group and does not have an

assigned sensor policy to enable/disable data collection on


that sensor.



