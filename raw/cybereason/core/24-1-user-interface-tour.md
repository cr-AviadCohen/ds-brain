## UI Tour Video


Watch this video for an overview of the Cybereason UI.


Before you log in, Cybereason Customer Success gives you a


URL for the Cybereason UI, a username, and a password.


To log in to Cybereason, navigate to the URL for the Cybereason


UI, and then enter the username and password in the login

screen.


Enter the username and password provided to you by Customer

Success to login to the Cybereason UI.


The Cybereason UI opens, showing the EPP Overview dashboard.

## EPP Overview Dashboard


When you log in to the Cybereason platform, the **EPP Overview**


**Dashboard** screen opens. This screen provides a high-level

overview of the recent threats that the Cybereason platform has


detected.


At the top of the Dashboard, you can view a high-level summary


of all detected activity in the selected time frame, including:






|Summary item|Description|
|---|---|
|Total detections|The total number of suspicions created in<br>the selected time period.|
|Total MalOps|The total number of MalOps created in the<br>selected time period independently of the<br>current state or status of the MalOp.|
|Prevented<br>MalOps|The total number of MalOps prevented for<br>the selected time period.|
|Active MalOps|The total number of open or active MalOps<br>for the selected time period. This count<br>does not include**Resolved** or**Excluded**<br>MalOps.|
|Escalated<br>MalOps|The total number of MalOps escalated for<br>the selected time period.|
|Mean Time to<br>Repair or<br>Resolution<br>(MTTR)|The average time to resolve a MalOp in the<br>selected time period. This is the average of<br>**Closed** and**Creation Time** for all MalOps<br>closed in the selected time period (usually<br>measured in days).|
|Affected users|The number of users with at least one<br>MalOp (not including**Resolved** or<br>**Excluded** MalOps).|


|Summary item|Description|
|---|---|
|Affected hosts|The cumulative number of hosts associated<br>with MalOps over the selected time period<br>(not including**Resolved** or**Excluded**<br>MalOps).<br>This number does not correspond with the<br>number of sensors installed, but instead<br>shows a total number of hosts that have<br>been involved in MalOps.|


In addition to the summary, you can view a number of different


graphs in the dashboard, including:






|Graph|Details|
|---|---|
|Active<br>MalOps by<br>status|The total number of MalOps for each<br>investigation status. This help you understand if<br>MalOps have been analyzed or triaged in a<br>timely manner by your team.|
|Active<br>MalOps by<br>severity|The total number of MalOps grouped by the<br>calculated severity of the MalOp. This graph<br>helps you analyze the severity and urgency of<br>all detected malicious activity in your<br>environment.|
|MalOp<br>resolution<br>tracking|The trend of all MalOps triggered over time, as<br>well as MalOps closed in the selected time<br>frame. This graph helps you ensure that<br>MalOps are being analyzed and triaged in an<br>appropriate manner by your team.|
|MalOps by<br>Mitre Tactic|The number of times a MITRE attack is<br>associated with a MalOp or the detections that<br>led to a MalOp.|
|MalOps by<br>detection<br>engine|All MalOps sorted by the different detection<br>engines used by the Cybereason platform.|
|Top IOCs|The top 5 IOCs that were root causes of<br>MalOps. These IOCs can be:<br>File names/hashes<br>IP addresses<br>Domain names<br>Processes|


|Graph|Details|
|---|---|
|Machines<br>by status|The total number of machines grouped by<br>status, including:<br>Infected and online<br>Infected but offine<br>Clean but online<br>Clean but offine|



Click on any section of a graph to navigate to the relevant screen


to learn more. For example, if you click on a section in one of the

**Active MalOps** graphs, you will open the Malops management


screen filtered accordingly. You can also click on MalOps by

MITRE tactic graph to navigate to the most critical MalOps for your


organization. For example, click on the Tactic **Impact** and see the

corresponding MalOps.


If you click on a section in the **Top IOCs** graph, you open the

**Investigation** screen to learn more.


As needed, you can filter the various graphs and charts by time or

by detection engine:


If your environment uses sensor grouping, you can also filter by

sensor groups.


You can also export your current view to a PDF document if you


need to share the dashboard with others. In the upper right corner
of the screen, click **Export** to save the current view to a PDF file:

## Discovery Board (deprecated)


Note


The Discovery Board is deprecated and is now replaced by

the EPP Overview dashboard. The Discovery Board will


continue to be available for existing customers until the end-of
life (EOL) period, but Cybereason recommends that you


transition to the EPP Overview dashboard instead. New

customers will not have access to the Discovery dashboard.


The Discovery board provides a high-level overview of the recent

threats that Cybereason has detected.


From the **Discovery board**, you can view Malops by:


Activity


Type

Time


Status


In the upper area of the screen, Malops are represented by


colored circles.


The Malops are grouped according to their place in the attack


lifecycle.

Larger circles indicate a larger number of affected machines.


Circles with a lighter color indicate more recent activity.


To further investigate a specific Malop, click a Malop on this


screen.


The bottom area of the screen includes a summary of malware


[alerts. For more details, see Manage Malware Alerts](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-malware-alerts&language=en_US#manage-malware-alerts)

[(/s/knowledge-base?article=24-1-manage-malware-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-malware-alerts&language=en_US#manage-malware-alerts)


[alerts&language=en_US#manage-malware-alerts).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-malware-alerts&language=en_US#manage-malware-alerts)


Note


The **Malops management** screen replaces the **Malop inbox**

and **Malware alerts** screens from previous Cybereason


versions. The **Malop inbox** and **Malware alerts** screens will

remain in the UI temporarily to allow current customers to


make the transition.


The **Malops management** screen provides a unified view of all


MalOps in your environment, including MalOps that the

Cybereason platform's automatic hunting engine generates as


well as MalOps that the Cybereason NGAV service generates.


From the **Malops management** screen, you can:


[View Malops (/s/knowledge-base?article=24-1-view-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops&language=en_US#view-malops)


[malops&language=en_US#view-malops) (if you do not have](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops&language=en_US#view-malops)

[the new Data Platform) or View MalOps with the Data Platform](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)


[Architecture (/s/knowledge-base?article=24-1-view-malops-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)

[with-the-data-platform-architecture&language=en_US#view-](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)


[malops-with-the-data-platform-architecture) (if you have the](https://nest.cybereason.com/s/knowledge-base?article=24-1-view-malops-with-the-data-platform-architecture&language=en_US#view-malops-with-the-data-platform-architecture)

new Data Platform)


Access the **Malop Details** screen for each MalOp

[Understand Threat Activity (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-threat-activity&language=en_US#understand-threat-activity)


[understand-threat-activity&language=en_US#understand-](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-threat-activity&language=en_US#understand-threat-activity)

[threat-activity)](https://nest.cybereason.com/s/knowledge-base?article=24-1-understand-threat-activity&language=en_US#understand-threat-activity)


Note


For existing Cybereason environments, the **Malop inbox**


screen is now deprecated. You can still use the **Malop inbox**

to interact with Malops, but we recommend that you transition


to use of the **Malops management** screen instead.


The **Malop inbox** displays the malicious operations that the


Cybereason platform detects in your organization.


From the **Malop inbox**, you can:


Group and filter MalOps to gain an understanding of your

system status


Add, remove, and create priority and custom MalOp labels

Sort the list by Type, Root causes, Affected machines,


Detected activity, Labels, creation date, time of last activity,

and Status


Assign or archive one or more MalOps

Drill down into the details of a MalOp


[For more details on analyzing Malops, see Analyze MalOps and](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)

[Determine Threat Level (/s/knowledge-base?article=24-1-analyze-](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)


[malops-and-determine-threat-level&language=en_US#analyze-](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)

[malops-and-determine-threat-level).](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-malops-and-determine-threat-level&language=en_US#analyze-malops-and-determine-threat-level)


Note


The **Malops management** screen replaces the **Malware**


**alerts** screen. You can still use the **Malware alerts** screen to

interact with malware, but we recommend that you transition to


the new view.


Analysts can monitor and manage malware alerts that are


generated by your Endpoint Prevention and NGAV settings in the

**Malware alerts** screen.


In this screen you can:


View malware alerts that need your attention

Investigate malware in more detail


View alerts that have been address (according to your sensor

policy settings)


[For more details, see Manage Malware Alerts (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-malware-alerts&language=en_US#manage-malware-alerts)

[base?article=24-1-manage-malware-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-malware-alerts&language=en_US#manage-malware-alerts)


[alerts&language=en_US#manage-malware-alerts) and How to](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-malware-alerts&language=en_US#manage-malware-alerts)

[Manage and Respond to NGAV Detections on the MalOps](https://nest.cybereason.com/s/article/6684681)


[Management Screen (/s/article/6684681).](https://nest.cybereason.com/s/article/6684681)

## Malop Details


When you drill down into a specific MalOp, you'll see the **Malops**


**details** screen, which displays a graphical and textual view of the

MalOp you selected.


Depending on the MalOp, the **Malop details** screen contains the


following tabs:


Overview: Provides the high-level details of the MalOp,


including a description and a visual diagram.

Processes: Provides an in-depth look at the malicious


processes associated with the Malop.

Files: Appears for Endpoint Protection MalOps. Lists


information about files that are associated with the detected

malware.


Machines: Provides information about the machine on which


the MalOp was discovered.

Users: Provides information about users associated with the


MalOp.

Communications: Provides information about any incoming


and outgoing communications that are associated with the

malicious behavior.


[For more details, see Examine MalOp Details (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-examine-malop-details&language=en_US#examine-malop-details)

[article=24-1-examine-malop-details&language=en_US#examine-](https://nest.cybereason.com/s/knowledge-base?article=24-1-examine-malop-details&language=en_US#examine-malop-details)


[malop-details).](https://nest.cybereason.com/s/knowledge-base?article=24-1-examine-malop-details&language=en_US#examine-malop-details)


The **Investigation** screen enables you to query endpoint sensor,


CWP sensor, and XDR log source data. Use this screen to

investigate Malops and malware, and to conduct hunts for


malicious behavior.


In the **Investigation** screen, you can:


Construct a query

Inspect results in a grid view or timeline view


Dive into specific Elements in the **Element Details** screen


You can start an investigation directly from the **Investigation**


screen, from the MalOp detail screen's **Process** tab, or from the

**Malware alerts** screen.


[For more details on investigation, see Perform a Hunt or](https://nest.cybereason.com/s/knowledge-base?article=24-1-perform-a-hunt-or-investigation&language=en_US#perform-a-hunt-or-investigation)

[Investigation (/s/knowledge-base?article=24-1-perform-a-hunt-or-](https://nest.cybereason.com/s/knowledge-base?article=24-1-perform-a-hunt-or-investigation&language=en_US#perform-a-hunt-or-investigation)


[investigation&language=en_US#perform-a-hunt-or-investigation).](https://nest.cybereason.com/s/knowledge-base?article=24-1-perform-a-hunt-or-investigation&language=en_US#perform-a-hunt-or-investigation)


[For details on Elements and their Features, see Query Elements](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[and Features (/s/knowledge-base?article=query-api-token-query-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

[elements-and-features-version-232148-and-later).](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


## Element Details

The **Element Details** screen provides more information on


suspicions you reveal when investigating.


On the **Investigation screen**, click an Element from the


results of your investigation to reveal the **Element Details**

screen.


Click the Expand button to open the details summary in a new

window.


Click any Element in the tree to view more details about that
specific Element.


Use the **Element Details** screen to view:


Affected machines, users, connections, and session

A timeline


Properties

Suspicions and evidence associated with the Element


Reputation status of the Element (allowlist or blocklist)

Malops associated with the Element


Note


Some details apply only to certain Element types, such as


processes.

## Security Profile


The **Security profile** screen allows you to manage security profile


settings for your organization.


From the **Security profile** screen you can:


[Search reputation sources (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-reputations&language=en_US#search-reputation-information)

[manage-reputations&language=en_US#search-reputation-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-reputations&language=en_US#search-reputation-information)


[information)](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-reputations&language=en_US#search-reputation-information)

[Upload or download custom reputation lists (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-reputations&language=en_US#manage-reputations)


[base?article=24-1-manage-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-reputations&language=en_US#manage-reputations)

[reputations&language=en_US#manage-reputations)](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-reputations&language=en_US#manage-reputations)


[Create behavioral allowlisting rules (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-behavioral-allowlisting-rules&language=en_US#manage-behavioral-allowlisting-rules)

[article=24-1-manage-behavioral-allowlisting-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-behavioral-allowlisting-rules&language=en_US#manage-behavioral-allowlisting-rules)


[rules&language=en_US#manage-behavioral-allowlisting-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-behavioral-allowlisting-rules&language=en_US#manage-behavioral-allowlisting-rules)

[rules)](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-behavioral-allowlisting-rules&language=en_US#manage-behavioral-allowlisting-rules)


[Create custom detection rules (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-custom-detection-rules&language=en_US#custom-detection-rules)

[article=24-1-custom-detection-](https://nest.cybereason.com/s/knowledge-base?article=24-1-custom-detection-rules&language=en_US#custom-detection-rules)


[rules&language=en_US#custom-detection-rules)](https://nest.cybereason.com/s/knowledge-base?article=24-1-custom-detection-rules&language=en_US#custom-detection-rules)

[Manage machine isolation (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-isolate-machines&language=en_US#isolate-machines)


[isolate-machines&language=en_US#isolate-machines)](https://nest.cybereason.com/s/knowledge-base?article=24-1-isolate-machines&language=en_US#isolate-machines)


The tabs in the **System** screen allow you to view and manage


your organization's sensors and servers, including the ability to

create and manage sensor policies and groups.


The **System** screen has the following tabs:


**Dashboard**  - View a summary of your sensors, including

sensor statuses, versions, OS types, and activity trends.


**Overview**  - View general information about a server,

download sensors installers, and fetch logs.


**Sensors**  - Monitor and manage your sensors. For more

[information, see Monitor and Manage Sensors (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-monitor-and-manage-sensors&language=en_US#monitor-and-manage-sensors)


[base?article=24-1-monitor-and-manage-](https://nest.cybereason.com/s/knowledge-base?article=24-1-monitor-and-manage-sensors&language=en_US#monitor-and-manage-sensors)


[sensors&language=en_US#monitor-and-manage-sensors).](https://nest.cybereason.com/s/knowledge-base?article=24-1-monitor-and-manage-sensors&language=en_US#monitor-and-manage-sensors)


**Policy management**  - Create and edit sensor policies. For

[more information, see Sensor Policies (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


[article=24-1-sensor-policies&language=en_US#sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)

[policies).](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-policies&language=en_US#sensor-policies)


**Detection servers**   - Monitor and manage your Detection

[servers. For more information, see Monitor Servers](https://nest.cybereason.com/s/knowledge-base?article=24-1-monitor-servers&language=en_US#monitor-servers)


[(/s/knowledge-base?article=24-1-monitor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-monitor-servers&language=en_US#monitor-servers)

[servers&language=en_US#monitor-servers).](https://nest.cybereason.com/s/knowledge-base?article=24-1-monitor-servers&language=en_US#monitor-servers)


**Sensor groups**  - Add sensor groups to enable users with the
Sensor L1 admin role to manage specific groups of sensors.


[For more information, see Manage Sensor Groups](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)

[(/s/knowledge-base?article=24-1-manage-sensor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)


[groups&language=en_US#manage-sensor-groups).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-sensor-groups&language=en_US#manage-sensor-groups)


The **Users** screen lists the user accounts for the Cybereason


platform.


From the **Users** screen you can:


Create new users


Manage existing users

Set and edit security roles


Note


Individual users can manage their password and email


settings. You must be a user admin to create and manage

other user accounts.


Users can see a subset of all user accounts by filtering users by

role, or by searching by user or role name.


[For more details on user management tasks, see Manage Users](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-users&language=en_US#manage-users)


[(/s/knowledge-base?article=24-1-manage-](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-users&language=en_US#manage-users)

[users&language=en_US#manage-users).](https://nest.cybereason.com/s/knowledge-base?article=24-1-manage-users&language=en_US#manage-users)


Use the **Settings** screen to configure Cybereason platform

settings.


From the **Settings** screen you can:

[Define an SMTP server (/s/knowledge-base?article=24-1-set-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-notification-preferences&language=en_US#define-an-smtp-server)


[notification-preferences&language=en_US#define-an-smtp-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-notification-preferences&language=en_US#define-an-smtp-server)

[server)](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-notification-preferences&language=en_US#define-an-smtp-server)


[Configure notification settings (/s/knowledge-base?article=24-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-notification-preferences&language=en_US#set-notification-preferences)
[1-set-notification-preferences&language=en_US#set-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-notification-preferences&language=en_US#set-notification-preferences)


[notification-preferences)](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-notification-preferences&language=en_US#set-notification-preferences)

[Enable or disable two-factor authentication (/s/knowledge-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-up-two-factor-authentication&language=en_US#set-up-two-factor-authentication)


[base?article=24-1-set-up-two-factor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-up-two-factor-authentication&language=en_US#set-up-two-factor-authentication)

[authentication&language=en_US#set-up-two-factor-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-up-two-factor-authentication&language=en_US#set-up-two-factor-authentication)


[authentication)](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-up-two-factor-authentication&language=en_US#set-up-two-factor-authentication)

[Set password policies (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-define-a-password-policy&language=en_US#define-a-password-policy)


[define-a-password-policy&language=en_US#define-a-](https://nest.cybereason.com/s/knowledge-base?article=24-1-define-a-password-policy&language=en_US#define-a-password-policy)

[password-policy)](https://nest.cybereason.com/s/knowledge-base?article=24-1-define-a-password-policy&language=en_US#define-a-password-policy)

## Cybereason Connect


If you use Cybereason XDR, the **Cybereason Connect** screen

enables to add integrations and manage connection details for


these integrations.


[For details, see Use Cybereason Connect (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-cybereason-connect&language=en_US#use-cybereason-connect)


[article=24-1-use-cybereason-connect&language=en_US#use-](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-cybereason-connect&language=en_US#use-cybereason-connect)

[cybereason-connect).](https://nest.cybereason.com/s/knowledge-base?article=24-1-use-cybereason-connect&language=en_US#use-cybereason-connect)



