|Role|Description|
|---|---|
|Analyst<br>(L1, L2,<br>and L3)|Assign this role to your security analysts who will<br>be responsible for investigation and<br>remediation. You can assign roles specifc to<br>analyst level:<br>L1 analysts can access security-related<br>data (MalOps and investigation) and can<br>perform limited operations on data.<br>L2 analysts can view automatically detected<br>information (evidence, suspicions, MalOps),<br>investigate MalOps, and build queries to<br>perform deep-dive investigations.<br>L3 analysts can view automatically detected<br>information (evidence, suspicions, MalOps),<br>investigate MalOps, and build queries to<br>perform deep-dive investigations into<br>operations that were not automatically<br>detected. In addition, L3 analysts can<br>perform remediation actions.|
|Analyst L1<br>Viewer|Assign this role to users to enable them to view<br>MalOp information, but not edit the MalOps<br>(such as changing the MalOp status, adding<br>MalOp comments, or adding MalOp labels).<br>Note<br>In environments without the new Data<br>Platform infrastructure, users with this role<br>do not have access to the Malop Inbox and<br>Malware Alerts screens.|


|Role|Description|
|---|---|
|Local<br>analyst (L1<br>and L2)|Assign this role to analysts who will be<br>responsible for managing incidents on sensors<br>in specifc sensor groups. Use the**Permissions**<br>section of the**Create User** screen, which<br>appears after selecting a Local analyst role, to<br>assign the user to one or more sensor groups.<br>Note<br>This role is available on Cloud deployments<br>only (not on On-Prem).<br>Note<br>This role is only available if you have<br>enabled sensor grouping in your<br>environment.<br>L1 local analysts can view MalOps and<br>investigate items that occur on sensors in<br>their assigned sensor groups.<br>L2 local analysts can also remediate these<br>MalOps.<br>All local analysts can view and search for<br>reputations from the**Security profle** ><br>**Reputation** screen.<br>You cannot have this role if you already have an<br>**Analyst L1/L2/L3** role or a**Responder L1/L2**<br>role assigned.<br>Note<br>This role is disabled by default. Open a<br>Technical Support (/s/support) case to make<br>this role available.|


|Role|Description|
|---|---|
|Local L1<br>Analyst<br>Viewer|Assign this role to users to enable them to view<br>MalOp information for their assigned groups,<br>but not edit the MalOps (such as changing the<br>MalOp status, adding MalOp comments, or<br>adding MalOp labels). Use the**Permissions**<br>section of the**Create User** screen, which<br>appears after selecting a Local analyst role, to<br>assign the user to one or more sensor groups.<br>Note<br>This role is available on Cloud deployments<br>only (not on On-Prem).<br>Note<br>This role is only available if you have<br>enabled sensor grouping in your<br>environment.<br>You cannot have this role if you already have the<br>**L1 Analyst Viewer** role assigned.<br>Note<br>In environments without the new Data<br>Platform infrastructure, users with this role<br>do not have access to the Malop Inbox and<br>Malware Alerts screens.|
|Responder<br>L1|Assign this role to users who will run interactive<br>commands directly on the machine with the<br>Remote Shell utility. You must enable two-factor<br>authentication (TFA) or SSO for users with the<br>Responder L1 role if you want them to use the<br>Remote Shell utility in Unrestricted mode.|
|Responder<br>L2|Assign this role to users who will manage<br>incident response management tasks, including<br>tool deployment and execution, and results<br>collection. You must enable two-factor<br>authentication (TFA) or SSO for users with the<br>Responder L2 role.|


|Role|Description|
|---|---|
|Local<br>Responder|Assign this role to users who will run interactive<br>commands directly on the machine with the<br>Remote Shell utility, in environments where<br>sensor grouping is enabled. You need to also<br>add the**Local Analyst** role for this user and<br>assign the sensor groups to access.<br>Note<br>This role is available on Cloud deployments<br>only (not on On-Prem).<br>Note<br>This role is only available if you have<br>enabled sensor grouping in your<br>environment.<br>You cannot have this role if you already have an<br>**Analyst L1/L2/L3** role or a**Responder L1/L2**<br>role assigned.<br>Note<br>This role is disabled by default. Open a<br>Technical Support (/s/support) case to make<br>this role available.|


|Role|Description|
|---|---|
|HDL<br>Analyst|HDL Analysts have access to the Historical Data<br>Lake user interface, and can run queries on<br>historical data. See Historical Data Lake<br>(/s/knowledge-base?article=24-1-historical-<br>data-lake&language=en_US#historical-data-<br>lake) for more information.<br>Note<br>This role is available on Cloud deployments<br>only (not on On-Prem).<br>Note<br>This role is disabled by default. Open a<br>Technical Support (/s/support) case to make<br>this role available.|
|System<br>admin|Assign this role to users who will be responsible<br>for the Cybereason platform system and sensor<br>settings.|
|System<br>viewer|Assign this role to users who should be able to<br>view the Cybereason platform system and<br>sensor settings. Users with this role cannot<br>change any settings.<br>Note<br>Users with the**System viewer** role have<br>read-only permissions for screens that the<br>System admin users have access to.|
|User admin|Assign this role to users who will be responsible<br>for creating and managing Cybereason users.|
|Executive|Assign this role to executive users who should<br>be able to view high-level MalOp and<br>investigation information.|
|Policy<br>admin|Assign this role to users who should be able to<br>upgrade sensors and create and assign sensor<br>security policies.|


|Role|Description|
|---|---|
|Sensor<br>admin L1|Assign this role to users who will be responsible<br>for managing certain groups of sensors. Use the<br>**Permissions** section of the**Create User**<br>screen, which appears after selecting the<br>Sensor admin L1 role, to assign the user to one<br>or more sensor groups.<br>Note<br>This role is only available if you have<br>enabled sensor grouping in your<br>environment.<br>You cannot have this role if you already have the<br>**Responder L2** role assigned.<br>Note<br>This role is disabled by default. Open a<br>Technical Support (/s/support) case to make<br>this role available.|
|Sensor<br>viewer|Assign this role to users who should have read<br>access to sensors in certain groups. Use the<br>**Permissions** section of the**Create User**<br>screen, which appears after selecting the<br>Sensor viewer role, to allow the user to read<br>information about sensors in those groups.<br>Note<br>This role is disabled by default. Open a<br>Technical Support (/s/support) case to<br>request this feature.<br>Note<br>If you grant a user the Sensor viewer role<br>along with a role that can access all groups,<br>the user will have read access to sensors in<br>all groups.|


In addition, the Cybereason platform has predefined roles that


represent common positions within an organization, such as SOC
lead. These predefined roles combine certain custom roles. You


can select only one predefined role for a user.



|Role|Description|
|---|---|
|SOC<br>lead|The SOC Lead predefned role combines the<br>permissions of a L3 Analyst and a User Admin,<br>enabling SOC Leads to have full visibility and<br>response abilities, along with the permissions<br>necessary to manage the user accounts for their<br>teams.|
|Super<br>user|The Super User predefned role gives full access to<br>perform the actions of all roles.<br>This role is used for SOC leads who also need system<br>management abilities, as well as for Cybereason's<br>own Incident Response and Customer Success<br>teams, so that they can provide the highest level of<br>support.|
|API<br>user|The API user role has permission to execute a subset<br>of API commands mainly for retrieving data as part of<br>SOC automations.<br>The API User role cannot run many API requests,<br>such performing response actions on a MalOp, due<br>to the permissions required for these API endpoints.<br>Therefore Cybereason recommends creating a<br>dedicated user for API purposes and assigning the<br>relevant roles. For additional details on API<br>permissions per API request, see the Permissions per<br>API request (/s/knowledge-base?article=required-<br>roles-per-endpoint) topic. You may also use the<br>Super user role for test or troubleshooting, as this role<br>has permission to send all API requests.<br>In addition, API user cannot log in to the Cybereason<br>platform UI, and therefore cannot change their<br>password.|


Note





If you select a predefined role for a user, the Cybereason


platform automatically selects the corresponding custom roles
for the pre-defined role. If you clear a selected custom role


after you select the pre-defined role, the Cybereason platform
clears the pre-defined role you previously selected.


## Permissions by role

The following tables detail the permissions assigned to each


Cybereason role.

## Administrator permissions


























|Permission|System<br>Admin|System<br>viewer|User<br>Admin|Policy<br>Admin|Sensor<br>Admin<br>L1|Se<br>vie|Col8|
|---|---|---|---|---|---|---|---|
|Add machine<br>isolation<br>exceptions|✓|||||||
|Add sensors<br>to groups|✓||||✓|||
|Add servers|✓|||||||
|Add user|||✓|||||
|Assign<br>policies|✓|||✓||||
|Change own<br>password|✓|✓|✓|✓|✓|✓||
|Confgure<br>email<br>notifcations<br>settings|✓|||||||
|Confgure<br>password<br>policy|✓|||||||
|Confgure<br>sensor tags|✓||||✓|||
|Confgure<br>SMTP server|✓|||||||
|Create sensor<br>groups|✓|||||||
|Create/edit<br>policies|✓|||✓||||


|Permission|System<br>Admin|System<br>viewer|User<br>Admin|Policy<br>Admin|Sensor<br>Admin<br>L1|Se<br>vie|Col8|
|---|---|---|---|---|---|---|---|
|Download<br>sensors<br>installation<br>package|✓||||✓|||
|Download<br>sensor logs|✓||||✓|||
|Download<br>user action<br>logs|||>✓|||||
|Enable TFA for<br>user|||✓|||||
|Enable TFA in<br>Settings|✓|||||||
|Export sensor<br>columns to<br>CSV|✓|✓|✓|✓|✓|✓||
|Manage<br>Security<br>profle settings|✓|||||||
|Manage<br>Sensor policy<br>settings|✓|||✓||||
|Manage<br>sensors<br>through the<br>**Sensors**<br>screen|✓|||✓|✓|||
|Manage sites|✓|||||||
|Modify user<br>roles|||✓|||||
|Monitor<br>Device Control<br>events|✓|✓|✓|✓|✓|✓||
|Perform<br>actions on<br>sensors|✓|||✓|✓|||
|||||||||


|Permission|System<br>Admin|System<br>viewer|User<br>Admin|Policy<br>Admin|Sensor<br>Admin<br>L1|Se<br>vie|Col8|
|---|---|---|---|---|---|---|---|
|Print report|||||✓|||
|Remove<br>sensors from<br>groups|✓||||✓|||
|Decommission<br>sensors|✓|||✓|✓|||
|Remove<br>servers|✓|||||||
|Remove user|||✓|||||
|Reset user<br>password|||✓|||||
|Search<br>reputations|||||✓|||
|Send<br>feedback|✓|✓|✓||✓|||
|Stale &<br>archived<br>sensor<br>settings|✓||||✓|||
|Subscribe to<br>email<br>notifcation|✓|✓|✓|✓|✓|✓||
|Unlock user|||✓|||||
|Upgrade<br>sensors|✓|||✓|✓|||
|View sensors|✓|✓||✓|✓|✓||
|View servers|✓|✓||||||
|Note|Note|Note|Note|Note|Note|Note||


For details on the permissions required to use API endpoints,


[see the Permissions per API request (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=required-roles-per-endpoint)

[article=required-roles-per-endpoint) topic.](https://nest.cybereason.com/s/knowledge-base?article=required-roles-per-endpoint)

## Analyst and Executive user permissions


















|Permission|L1|L2|L3|L1<br>Viewer|Local<br>L1|Local<br>L2|Loc<br>L3|Col9|
|---|---|---|---|---|---|---|---|---|
|Add comment|✓|✓|✓||✓|✓|✓||
|Behavioral<br>allowlisting|||✓||||✓||
|Add or remove items<br>from reputation lists|||✓||||||
|Change MalOp<br>status|✓|✓|✓||||✓||
|Change own<br>password|✓|✓|✓|✓|✓|✓|✓||
|Create custom<br>detection rules|||✓||||✓||
|Defne display<br>columns|✓|✓|✓|✓|✓|✓|✓||
|Download fle||✓|✓|||✓|✓||
|File search|||✓||||||
|Isolate machines|||✓|||✓|✓||
|Limit query results by<br>number|✓|✓|✓|✓|✓|✓|✓||
|Limit query results by<br>time|||✓||||✓||
|MalOp<br>response/remediation<br>actions|||✓|||✓|✓||
|Manage reputations|||✓||||||


|Permission|L1|L2|L3|L1<br>Viewer|Local<br>L1|Local<br>L2|Loc<br>L3|Col9|
|---|---|---|---|---|---|---|---|---|
|Manage Security<br>profle settings|||✓||||||
|Monitor Device<br>Control events|✓|✓|✓|✓|✓|✓|✓||
|Print report|✓|✓|✓|✓|✓|✓|✓||
|Run investigation<br>query|✓|✓|✓|✓|✓|✓|✓||
|Save display<br>columns|✓|✓|✓|✓|✓|✓|✓||
|Save queries|✓|✓|✓||||||
|Search reputations|✓|✓|✓||||||
|Send feedback|✓|✓|✓|✓|✓|✓|✓||
|Subscribe to email<br>notifcation|✓|✓|✓|✓|✓|✓|✓||
|Unsuspend process|||✓|||✓|||
|View and create<br>MalOp labels|✓|✓|✓||||||
|View Discovery<br>board|✓|✓|✓|✓|||✓||
|View MalOp details|✓|✓|✓|✓|✓|✓|✓||
|View Malops<br>management screen|✓|✓|✓|✓|✓|✓|✓||
|View Malop inbox|✓|✓|✓||||✓||
|View XDR screens|✓|✓|✓|✓|✓|✓|✓||
|Note|Note|Note|Note|Note|Note|Note|Note||


For details on the permissions required to use API endpoints,


[see the Permissions per API request (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=all-versions/required-roles-endpoint)

[article=all-versions/required-roles-endpoint) topic.](https://nest.cybereason.com/s/knowledge-base?article=all-versions/required-roles-endpoint)

## Responder permissions


Users who need to perform additional or in-depth response tasks

should be given the Responder L1, Responder L2, or Local


Responder roles:






|Role|Permission|
|---|---|
|**Responder**<br>**L1**|Use the Remote Shell utility<br>Use the**File Search** screen to search for<br>fles and download fles<br>Note<br>You cannot use the**Responder L1** role with<br>the**Local Analyst L1/L2** or**Local**<br>**Responder** roles.|
|**Responder**<br>**L2**|Use the Remote Shell utility<br>Use the**Live File Search** screen to search<br>for fles and download fles<br>Perform incident response management<br>tasks<br>View sensors in the**Sensors** screen<br>Enable Remote Shell for selected sensors<br>Note<br>You cannot use the**Responder L2** role with<br>the**Local Analyst L1/L2** or**Local**<br>**Responder** roles.|


|Role|Permission|
|---|---|
|**Local**<br>**Responder**|Use the Remote Shell utility<br>View and manage MalOps, including<br>viewing MalOp details, updating MalOp<br>status, and adding MalOp comments<br>Run investigation queries<br>Use the**Live File Search** screen to search<br>for fles and download fles<br>Note<br>Users with the Local Responder role must<br>also have the Local Analyst L1/L2 role<br>assigned to view and manage MalOps and<br>run investigation queries. In addition, you<br>cannot use the**Local Responder** role with<br>the**Responder L1/L2** or**Analyst L1/L2/L3**<br>roles.|





