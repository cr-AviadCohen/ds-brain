## Create an upgrade request

To request an upgrade, contact your Cybereason representative

(CSM, TAM, SE) who will be able to log the upgrade request on


[your behalf, if you do not have one open a Technical Support](https://nest.cybereason.com/s/support)

[(/s/support) case. You must submit your request 7 days prior to](https://nest.cybereason.com/s/support)


the desired upgrade time, however no later than the close of

business on every Monday. Requests that are submitted after the


close of business on Monday will be processed the following

Monday.


In the upgrade request, you can select the upgrade start time.


Upgrades will be performed during the following maintenance


windows:


Sunday - Thursday 07:00-18:00 Israel Standard Time (IST)


(GMT+2).

Sunday - Thursday 09:00-18:00 Japan Standard Time (JST)


(GMT+9) (limited - requires approval from the NOC team)

For environments with up to 5 Detection servers, 12:00 PM IST


is the latest hour* Cybereason can start the upgrade.

For environments with more than 5 Detection servers, 08:00


AM IST is the latest hour* Cybereason can start the upgrade.

Special cases must be approved by the NOC team.


In addition, you can ask to change the default configuration for
selected features. The configuration changes will occur during the


upgrade process.


Technical Operations processes requests based on the number of


incoming requests and in-progress upgrades, and limits the

number of upgrades performed each day. In the event there is a


delay to your scheduled upgrade, Technical Operations will notify

you as soon as possible.


During the upgrade process, Technical Operations first deploys

the upgraded version of Cybereason in a new ("green")


environment. After the upgraded environment is ready, Technical

Operations migrates the data from the old ("blue") environment to


the new environment. Upgrade rollback is possible during this

time, and the Cybereason UI in the old environment remains


available with only a temporary suspension of visibility into new

activity. The upgrade mainly affects the availability of new data


and does not affect system availability.


An estimated downtime period of six to eight hours is expected


during maintenance. Under certain circumstances, the downtime

period may be more than eight hours. If an extension is required,


Cybereason Technical Operations will notify you by email.


During the upgrade process, you will receive one or more of the


following maintenance notifications:


Important


If you are not sure you are set up to receive upgrade
notifications, please reach out to Technical Support.






|Maintenance<br>Notification|Description|
|---|---|
|Planned<br>Upgrade (Blue<br>Green)|A notifcation is sent with the planned<br>maintenance timeline (start time).|
|Upgrade<br>Complete|A notifcation is sent when the upgrade<br>successfully completes. At this time, the<br>environment is up and running, post-<br>production tests have demonstrated<br>success, and the environment is ready for<br>use.|
|Maintenance<br>Cancelled|A notifcation is sent if the maintenance was<br>cancelled due to a rollback.|
|Maintenance<br>Extension|A notifcation is sent if additional time is<br>required to start or perform the upgrade.<br>An extension enables the relevant technical<br>teams to fx any technical issues that were<br>encountered, instead of rolling back.|



Depending on the technical issues that were encountered during

upgrade, a rollback can be performed within 2-4 hours (before


sensor connectivity) or 4-6 hours (following sensor connectivity).


Following upgrade, the old environment will remain active for 7


days for rollback purpose, but generally rollbacks are not

performed. Cybereason will only implement a rollback if it deems it


necessary and will contact you accordingly.


Service Pack updates can also involve downtime, depending on


the Service Pack content. The expected downtime for a full

environment upgrade (without sensors) is similar to a major


version upgrade.


## Upgrade Steps

Important


The upgrade process is performed by Cybereason Technical

Operations. You are not required to perform these steps. The


information in this section is included in order to provide a

better understanding of the process.


Sensor upgrades are not required for server upgrades. In

addition, no IP or DNS changes are required.
















|Step|Estimated<br>duration|Downtime<br>implications|Impact of<br>the stage on<br>your<br>environment|Custo<br>appro<br>Stage|Col6|
|---|---|---|---|---|---|
|1. Stop sensor<br>collection<br>from the<br>Detection<br>servers|5 min.|Sensors are<br>not<br>connected to<br>the servers<br>during the<br>upgrade. No<br>data is lost<br>while sensors<br>are<br>disconnected<br>from the<br>servers.<br>Sensors store<br>the collected<br>data locally<br>until the new<br>environment<br>is available.|Low|No||
|1. Create a<br>build of the<br>new version<br>environment,<br>including<br>WebApp<br>server,<br>Detection<br>servers, and<br>Registration<br>server|1 hr.|None. This is<br>done as part<br>of the<br>upgrade<br>process.|Low|No||


|Step|Estimated<br>duration|Downtime<br>implications|Impact of<br>the stage on<br>your<br>environment|Custo<br>appro<br>Stage|Col6|
|---|---|---|---|---|---|
|1. Backup old<br>environment|1-2 hrs.|UI in the old<br>environment<br>is still<br>available but<br>sensors do<br>not send new<br>data.<br>Investigation<br>queries<br>return results<br>based on<br>existing data.|Low|No||
|1. Copy<br>backup fles<br>and data to<br>the new<br>servers|1-2 hrs.|UI in the old<br>environment<br>is still<br>available but<br>sensors do<br>not send new<br>data.<br>Investigation<br>queries<br>return results<br>based on<br>existing data.|Low|No||
|1. Load data<br>on the new<br>server|1-2 hrs.|UI in the old<br>environment<br>is still<br>available but<br>sensors do<br>not send new<br>data.<br>Investigation<br>queries<br>return results<br>based on<br>existing data.|Low|No||
|||||||


|Step|Estimated<br>duration|Downtime<br>implications|Impact of<br>the stage on<br>your<br>environment|Custo<br>appro<br>Stage|Col6|
|---|---|---|---|---|---|
|1. Confgure<br>the new<br>environment<br>(WebApp<br>server,<br>Detection<br>servers,<br>Registration<br>server)|15 min.|UI in the old<br>environment<br>is still<br>available but<br>sensors do<br>not send new<br>data.<br>Investigation<br>queries<br>return results<br>based on<br>existing data.|Low|No||
|1. Sanity<br>checks<br>(compare<br>the old<br>environment<br>to the new<br>environment)|30 min.|UI in the old<br>environment<br>is still<br>available but<br>sensors do<br>not send new<br>data.<br>Investigation<br>queries<br>return results<br>based on<br>existing data.|Low|No||
|1. Change the<br>default<br>feature<br>confguration<br>according to<br>customer<br>request|1 hr.|UI in the old<br>environment<br>is still<br>available but<br>sensors do<br>not send new<br>data.|Low|No||
|||||||


|Step|Estimated<br>duration|Downtime<br>implications|Impact of<br>the stage on<br>your<br>environment|Custo<br>appro<br>Stage|
|---|---|---|---|---|
|1. DNS<br>confguration<br>and IP<br>association|15 min.|Route DNS<br>server names<br>& IP<br>addresses to<br>the new<br>environment.<br>The old<br>environment<br>is not<br>accessible at<br>this point, but<br>servers are<br>online for fast<br>rollback if<br>required.|High|Yes|
|1. Enable<br>sensor<br>connectivity<br>to Detection<br>servers|5 min.|Sensors start<br>to send all<br>saved data<br>from the last<br>6-8 hours<br>(which during<br>that time they<br>were<br>disconnected<br>from the<br>servers).|Medium|Yes|
