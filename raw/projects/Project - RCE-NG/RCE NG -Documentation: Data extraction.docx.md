# RCE NG -Documentation: Data extraction.docx

Rce ng -Documentation:

Data extraction:

You need to obtain permissions for the following Vault:

vault-prod-asia-northeast1

vault-prod-asia-southeast1

vault-prod-europe-west1

Vault-prod-europe-west3 -- **(europe-west6 is also here)**

vault-prod-me-central2

MT - vault-prod-us-east1

Example of the permissions path in Vault for the DB: **suites/siem-alerts-suite/stacks/us-e1-1-stack/db-credentials**

Go to PGAdmin and connect to the server of the relevant DB for example: sa\_suite\_us\_e1\_1\_stack .

The query we used:

select

s.customer\_id,

a.detection\_time,

event

from sa.alert as a join sa.suspicious\_event as s on (a.id=s.alert\_id)

where detection\_time BETWEEN '2025-04-28 00:00:00' AND '2025-04-28 23:59:59'

AND event->>'tactic' IS NOT NULL



After running the model, we reached the following conclusions and Questions:

* There is a lack of information to determine whether the correlation is TP/FP.
* Do we need additional details about the event, such as information on the process or file?.
* It’s time to start discussing the next stage of filtering ([FILTERS](https://cybereason.enterprise.slack.com/files/U05PZF9PWLU/F08776ZL4QH/filters) ) according to integration categories ([Integrations Categories](https://cybereason.enterprise.slack.com/files/U05PZF9PWLU/F086DUHQULF/integrations_categories_))

The following query retrieves the data post RCE correlation:

The BQ project is:dc-us-e1-1-stack-prod-e3

SELECT

customer\_id,

alert\_name,

triggering\_rule,

data\_source,

FORMAT\_TIMESTAMP('%Y-%m-%d %H:%M:%S', TIMESTAMP\_SECONDS(CAST(CAST(JSON\_VALUE(event, "$.creationTime") AS INT64) / 1000 AS INT64))) AS CreationTime,

JSON\_VALUE(event, "$.eventId") AS event\_id,

JSON\_VALUE(event, "$.alertGuid") AS alert\_guid,

tactic,

techniques,

sub\_techniques,

-- IP Addresses

JSON\_EXTRACT(event, "$.sourceIpAddress.address") AS source\_ip,

JSON\_EXTRACT(event, "$.connection.localAddress.address") AS local\_ip,

JSON\_EXTRACT(event, "$.connection.remoteAddress.address") AS remote\_ip,

-- ADSIDs

JSON\_EXTRACT(event, "$.sourceMachine.adSid") AS source\_ad\_sid,

JSON\_EXTRACT(event, "$.connection.ownerMachine.adSid") AS owner\_ad\_sid,

JSON\_EXTRACT(event, "$.connection.remoteMachine.adSid") AS remote\_ad\_sid,

-- Computer Names

JSON\_EXTRACT(event, "$.sourceMachine.computerName") AS source\_computer\_name,

JSON\_EXTRACT(event, "$.connection.ownerMachine.computerName") AS owner\_computer\_name,

JSON\_EXTRACT(event, "$.connection.remoteMachine.computerName") AS remote\_computer\_name,

-- URL Domain Name

JSON\_EXTRACT(event, "$.connection.urlDomain.name") AS url\_domain\_name,

-- Emails (Aggregates all available email addresses)

JSON\_EXTRACT(event, "$.sourceUser.emailAddresses.email") AS source\_user\_email\_address,

JSON\_EXTRACT(event, "$.targetGroup.emailAddresses.address") AS target\_group\_email\_address,

JSON\_EXTRACT(event, "$.targetUser.emailAddresses.email") AS target\_user\_email\_address,

JSON\_EXTRACT(event, "$.message.receipientAddresses.email") AS recipient\_email\_address,

JSON\_EXTRACT(event, "$.message.senderAddress.email") AS sender\_email\_address,

-- User SIDs

JSON\_EXTRACT(event, "$.sourceUser.sid") AS source\_user\_sid,

JSON\_EXTRACT(event, "$.targetUser.sid") AS target\_user\_sid,

-- User Names

JSON\_EXTRACT(event, "$.sourceUser.username") AS source\_username,

JSON\_EXTRACT(event, "$.targetUser.username") AS target\_username,

-- URLs (Aggregates all available URLs)

JSON\_EXTRACT(event, "$.connection.urlDomain.url") AS url,

JSON\_EXTRACT(event, "$.message.link.url") AS link\_url

FROM `dc-us-e1-1-stack-prod-e3.dc\_rce\_dataset.correlation\_output`

WHERE

TIMESTAMP\_SECONDS(CAST(CAST(JSON\_VALUE(event, "$.creationTime") AS INT64) / 1000 AS INT64)) BETWEEN TIMESTAMP("2024-11-18 00:00:00") AND TIMESTAMP("2024-11-19 23:59:59")

and date BETWEEN "2024-10-18" and "2024-11-19"

AND tactic IS NOT NULL;



To identify all related events for each triaged Malop

The BQ project is: global-soc-project

WITH RankedData AS (

SELECTJSON\_EXTRACT\_SCALAR(data, '$.CustomerName') AS CustomerName,

REGEXP\_EXTRACT(JSON\_EXTRACT\_SCALAR(data, '$.CustomerURL'), r'//(.+?)\.cybereason\.net') AS customer\_id,

JSON\_VALUE(data, "$.malopId") as MalopId,

JSON\_VALUE(data, "$.malopName") as MalopName,

JSON\_VALUE(data, "$.severity") as Severity,

JSON\_EXTRACT\_SCALAR(data, '$.Classification') AS Classification,

JSON\_EXTRACT(data, "$.suspiciousEvents") as suspicious\_Events,

DATE(TIMESTAMP\_SECONDS(CAST(CAST(JSON\_VALUE(data, "$.creationTime") AS INT64) / 1000 AS INT64))) AS CreationTime,

DATE(TIMESTAMP\_SECONDS(CAST(CAST(JSON\_VALUE(data, "$.lastUpdateTime") AS INT64) / 1000 AS INT64))) AS LastUpdateTime,

ROW\_NUMBER() OVER (PARTITION BY JSON\_VALUE(data, "$.malopId") ORDER BY CAST(JSON\_VALUE(data, "$.lastUpdateTime") AS INT64) DESC) AS rn

FROM `global-soc-14311f.xdr\_malop\_amer.rce\_triage\_result`

WHERE JSON\_EXTRACT\_SCALAR(data, '$.Classification') IS NOT NULL

)SELECT CustomerName, customer\_id, MalopId, MalopName, Severity, Classification, CreationTime,suspicious\_Events

FROM RankedData

WHERE CreationTime between "2024-12-03" and "2024-12-04"



Observe Query

 make\_col principal\_ip\_address: string(xdm.principal.ip[0].address)

make\_col principal\_user\_name: string(xdm.principal.user.display\_name)

make\_col principal\_computer\_id: string(xdm.principal.asset.id)

make\_col principal\_computer\_name: string(xdm.principal.asset.hostname)

make\_col principal\_user\_email: string(xdm.principal.user.email\_addresses)

make\_col principal\_user\_id: string(xdm.principal.user.id)

make\_col target\_ip\_address: string(xdm.target.ip[0].address)

make\_col target\_user\_name: string(xdm.target.user.display\_name)

make\_col target\_computer\_id: string(xdm.target.asset.id)

make\_col target\_computer\_name: string(xdm.target.asset.hostname)

make\_col target\_user\_email: string(xdm.target.user.email\_addresses)

make\_col target\_user\_id: string(xdm.target.user.id)

make\_col product\_category: string(xdm.meta.product.product\_category)

make\_col customer\_id: customerIdentifier

drop\_col customerIdentifier

drop\_col product

drop\_col product\_event\_type

drop\_col principal\_id

drop\_col principal\_ip

drop\_col target\_id

drop\_col target\_ip

drop\_col action

drop\_col log\_hash

drop\_col data

drop\_col xdm

//drop\_col event\_type

//drop\_col EXTRA

//drop\_col timestamp

filter customer\_id = "ccbji1"

filter not is\_null(product\_category)

make\_col not\_null\_count:

if(is\_null(principal\_ip\_address), 0, 1) +

if(is\_null(principal\_user\_name), 0, 1) +

if(is\_null(principal\_computer\_id), 0, 1) +

if(is\_null(principal\_computer\_name), 0, 1) +

if(is\_null(principal\_user\_email), 0, 1) +

if(is\_null(principal\_user\_id), 0, 1) +

if(is\_null(target\_ip\_address), 0, 1) +

if(is\_null(target\_user\_name), 0, 1) +

if(is\_null(target\_computer\_id), 0, 1) +

if(is\_null(target\_computer\_name), 0, 1) +

if(is\_null(target\_user\_email), 0, 1) +

if(is\_null(target\_user\_id), 0, 1)

filter not\_null\_count > 1

timechart 1h,

count: count(1),

group\_by(

customer\_id, product\_category,

principal\_ip\_address, principal\_user\_name, principal\_computer\_id,

principal\_computer\_name, principal\_user\_email, principal\_user\_id,

target\_ip\_address, target\_user\_name, target\_computer\_id,

target\_computer\_name, target\_user\_email, target\_user\_id

)


