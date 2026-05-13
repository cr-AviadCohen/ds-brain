# Data Enrichment Process Documentation.docx

# **Data Enrichment Documentation**

## **Overview**

The goal of this process is to enhance XDR alerts by enriching them with additional context from related events of the same customer in Observe. This enrichment provides a more complete view of each alert, supports better analysis and decision-making, and helps fill in missing identity information.

## **Objectives**

* **Enrich Alert Data:** Augment alerts with relevant information from events to provide context and improve analysis.
* **Customer-Specific Processing:** Process and enrich data separately for each customer to maintain data integrity and relevance.
* **Performance Optimization:** Ensure the enrichment process is efficient and scalable.

## **Data Sources**

1. **Alerts Data (alerts\_df):** The XDR alerts, parsed according to CR schema, are ingested into the engine. We use the following query to extract the alerts from Siem Alerts suite (pgadmin).

You need to obtain permissions for the following Vault:

vault-prod-asia-northeast1

vault-prod-asia-southeast1

vault-prod-europe-west1

Vault-prod-europe-west3 -- **(europe-west6 is also here)**

vault-prod-me-central2

MT - vault-prod-us-east1

Example of the permissions path in Vault for the DB: **suites/siem-alerts-suite/stacks/us-e1-1-stack/db-credentials**

Go to PGAdmin and connect to the server of the relevant DB for example: sa\_suite\_us\_e1\_1\_stack .

SELECT

s.customer\_id,

a.detection\_time,

event->>'alertName' AS alert\_name,

event->>'tagType' AS tag\_type,

event->>'ruleName' AS triggering\_rule,

event->>'dataSource' AS data\_source,

event->>'eventId' AS event\_id,

event->>'alertGuid' AS alert\_guid,

event->>'dataSourceCategory' AS data\_source\_category,

tactic,

technique,

sub\_technique,

-- IP Addresses

event->'sourceIpAddress'->>'address' AS source\_ip,

event->'connection'->'remoteAddress'->>'address' AS remote\_ip,

-- ADSIDs

event->'sourceMachine'->>'adSid' AS source\_ad\_sid,

event->'connection'->'remoteMachine'->>'adSid' AS remote\_ad\_sid,

-- Computer Names

event->'sourceMachine'->>'computerName' AS source\_computer\_name,

event->'connection'->'remoteMachine'->>'computerName' AS remote\_computer\_name,

-- URL Domain Name

event->'connection'->'urlDomain'->>'name' AS url\_domain\_name,

-- Extracted Recipient Email (One row per email)

recipient.value->>'email' AS recipient\_email\_address,

-- Sender Email

event->'message'->'senderAddress'->>'email' AS sender\_email\_address,

-- User SIDs

event->'sourceUser'->>'sid' AS source\_user\_sid,

event->'targetUser'->>'sid' AS target\_user\_sid,

-- User Names

event->'sourceUser'->>'username' AS source\_username,

event->'targetUser'->>'username' AS target\_username,

-- URLs

event->'connection'->'urlDomain'->>'url' AS url,

FROM sa.alert AS a

JOIN sa.suspicious\_event AS s ON a.id = s.alert\_id

-- Fix: correct key is recipientAddresses

LEFT JOIN LATERAL jsonb\_array\_elements(event->'message'->'recipientAddresses') AS recipient(value) ON true

WHERE detection\_time BETWEEN '2025-02-25 00:00:00' AND '2025-02-25 23:59:59'

AND event->>'tactic' IS NOT NULL ;

 Make sure you are in the right region and adjust the time.

1. **Events Data (events\_df):** all the events from the relevant region (Observe Tanent). We collect the events while we use api requests. (The complete explanation can be found on page 6)

## **Preprocessing Steps**

1. **Load Data:**
   * Read the alerts data from a CSV file.
   * Fetch events data using the execute\_opal\_query function with specified parameters.
2. **Standardize Column Names:**
   * Rename columns to ensure consistency between datasets (e.g., renaming customerIdentifier to customer\_id).
3. **Add Index Column:**
   * Introduce an 'index' column to alerts\_df to uniquely identify each alert.
4. **Convert Timestamps:**
   * Convert 'detection\_time' in alerts\_df and 'timestamp' in events\_df to datetime objects for accurate time-based operations.
5. **Data Type Consistency:**
   * Convert all columns, except 'timestamp', to strings and handle missing values to ensure uniformity during processing.
6. **Identify Network-Related Data:**
   * Add an 'is\_network' column to both DataFrames to distinguish network-related records based on predefined product categories.

## **Enrichment Functions**

Three primary functions are used to enrich the alert data:

1. **enrich\_by\_ip(alert, filtered\_events):**
   * **Purpose:** Enhance an alert by finding the closest event that shares the same IP address. Depending on the match (principal or target IP), it fills corresponding fields in the alert.
   * **Process:**
     + Extract relevant IPs from the alert.
     + Calculate the time difference between the alert and each event.
     + Iterate over events sorted by time difference to fill missing fields in the alert based on IP matches.
2. **enrich\_by\_username(alert, events\_df):**
   * **Purpose:** Enrich an alert by finding the closest event with a matching username. Depending on the match (principal or target username), it fills corresponding fields in the alert.
   * **Process:**
     + Filter events that have an email, as enrichment requires this information.
     + Calculate the time difference between the alert and each event.
     + Iterate over events sorted by time difference to fill missing fields in the alert based on username matches.
3. **enrich\_by\_email(alert, events\_df):**
   * **Purpose:** Enhance an alert by finding the closest event with a matching email address. Depending on the match (principal or target email), it fills corresponding fields in the alert.
   * **Process:**
     + Filter events that have an IP or user information, as enrichment requires this data.
     + Calculate the time difference between the alert and each event.
     + Iterate over events sorted by time difference to fill missing fields in the alert based on email matches.

4. **enrich\_by\_userid(alert, events\_df)**

**Purpose:** Enhance an alert by locating the closest event with a matching user ID. Depending on whether the match is found in the principal or target user ID field, the function populates the relevant missing fields in the alert.

**Process:**

* Filter events to retain only those containing an email, as it's required for enrichment.
* Calculate the time difference between the alert and each event.
* Sort events by time difference and iterate through them to fill in missing alert fields based on user ID matches (either principal or target).

## **Workflow**

1. **Group Data by Customer:**
   * Both alerts\_df and events\_df are grouped by 'customer\_id' to ensure that enrichment is performed within the context of each customer.
2. **Enrichment Process:**
   * For each customer group:
     + Filter events where 'is\_network' is False.
     + Apply enrich\_by\_ip to alerts where 'is\_network' is True.
     + Apply enrich\_by\_username to alerts with non-null 'source\_username' or 'target\_username'.
     + Apply enrich\_by\_email to alerts with non-null 'sender\_email\_address' or 'recipient\_email\_address'.
3. **Save Enriched Data:**
   * Each enriched DataFrame is saved as a separate CSV file named enriched\_alerts\_customer\_{customer\_id}.csv in the 'enriched\_alerts' directory.

## **Performance Considerations**

* **Efficient Filtering:** By pre-filtering events based on the 'is\_network' flag, the enrichment functions process a reduced dataset, enhancing performance.
* **Time-Based Sorting:** Sorting events by the time difference relative to each alert ensures that the most relevant events are considered first during enrichment.
* **Customer-Specific Processing:** Handling data on a per-customer basis not only maintains data integrity but also allows for parallel processing opportunities, thereby improving scalability.

MAPPING SHEET-[IDM- mapping fields](https://docs.google.com/spreadsheets/d/1sdiXhiaqtC-lj4Q7INrCCUpf0PHZapxROMq4btPVcFM/edit?gid=0#gid=0)

# **API REQUEST- Executing OPAL Query and Fetching Paginated Results**

## **Overview**

This process involves executing an **OPAL query** via an API request and retrieving **paginated query results** into a **Pandas DataFrame**. The API supports **long polling** and **cursor-based pagination**, ensuring that large datasets can be fetched efficiently.

## **Process Flow**

1. **Get Access Key(POST /v1/logi)**

def get\_access\_key():

*"""*

*Sends a login request and retrieves the access key.*

*"""*

url = "https://131377279880.ap-1.observeinc.com/v1/login"

data = {

"user\_email": "your email",

"user\_password": "your password",

"tokenName": "your token"

}

headers = {"Content-Type": "application/json"}

try:

response = requests.post(url, json=data, headers=headers)

response.raise\_for\_status() # Raise an error for HTTP errors

return response.json().get("access\_key")

except requests.exceptions.RequestException as e:

print(f"Error fetching access key: {e}")

return None



1. **Execute OPAL Query (POST /v1/meta/export/query)**
   * Submits an OPAL query with required parameters.

{def execute\_opal\_query(api\_url, output\_stage, dataset\_inputs, pipeline, start\_time=None, interval=None, row\_count=None, paginate=True, accept\_format="text/csv"):

access\_key = get\_access\_key()

headers = {

"Authorization": f"Bearer 131377279880 {access\_key}",

"Accept": accept\_format,

"Content-Type": "application/json"

}

# Handle start\_time: Convert datetime to string if necessary

if start\_time is None:

start\_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ") # Default: current UTC time

elif isinstance(start\_time, datetime):

start\_time = start\_time.strftime("%Y-%m-%dT%H:%M:%SZ") # Convert datetime to ISO 8601

params = {

"startTime": start\_time,

"interval": interval,

"paginate": str(paginate).lower()

}

# Remove None values from params

params = {k: v for k, v in params.items() if v is not None}

# Construct the OPAL query payload

body = {

"query": {

"outputStage": output\_stage,

"stages": [

{

"input": dataset\_inputs, # Input datasets

"stageID": output\_stage, # Same as outputStage

"pipeline": pipeline # OPAL query pipeline

}

]

},

"rowCount": str(row\_count) # Ensure rowCount is a string

}

response = requests.post(api\_url, headers=headers, params=params, json=body)

if response.status\_code == 202:

cursor\_id = response.headers.get("X-Observe-Cursor-Id")

if cursor\_id:

print(f"Cursor ID retrieved: {cursor\_id}")

return fetch\_paginated\_results(cursor\_id, accept\_format, headers) # Fetch data

else:

print("No Cursor ID found in headers.")

return pd.DataFrame() # Return empty DataFrame

else:

print(f"Error: {response.status\_code}")

print(response.text)

return pd.DataFrame() # Return empty DataFrame on failure

"query": {

"outputStage": output\_stage,

"stages": [

{

"input": dataset\_inputs, # Input datasets

"stageID": output\_stage, # Same as outputStage

"pipeline": pipeline # OPAL query pipeline

}

]

},

"rowCount": str(row\_count) # Ensure rowCount is a string

}

# Define OPAL query pipeline

pipeline = r"""YOUR OPAL QUERY"""

dataset\_inputs = [

{"inputName": "main", "datasetId": "41137654"},

]



* + Enables **pagination** (paginate=True) and sets rowCount high to fetch large datasets.
  + Receives a 202 Accepted response while the query is processing.
  + Extracts the **cursor ID (X-Observe-Cursor-Id)** from response headers.

1. **Fetch Paginated Results (GET /v1/meta/export/query)**



def fetch\_paginated\_results(cursor\_id, accept\_format, headers):

*"""*

*Fetches all paginated results using the cursor ID and loads them into a Pandas DataFrame.*

*"""*

QUERY\_URL = api\_url\_page # Start with the base query URL

params = {"cursorId": cursor\_id, "numRows": 1000000000} # Adjust `numRows` as needed

df = pd.DataFrame()

while True:

response = requests.get(QUERY\_URL, headers=headers, params=params)

# Handle long polling (202 Accepted)

if response.status\_code == 202:

print("Query still in progress. Retrying in 5 seconds...")

time.sleep(5)

continue # Retry the request

elif response.status\_code != 200:

print(f"Error fetching paginated results: {response.status\_code}")

print(response.text)

break # Stop execution on error

# Process CSV or NDJSON response

if accept\_format == "text/csv":

data = pd.read\_csv(io.StringIO(response.text))

else:

data = pd.read\_json(io.StringIO(response.text), lines=True) # Handle NDJSON

df = pd.concat([df, data], ignore\_index=True)

# Extract pagination details

next\_page\_url = response.headers.get("X-Observe-Next-Page")

new\_cursor\_id = response.headers.get("X-Observe-Cursor-Id")

print(f"Loaded {len(data)} rows. Total rows so far: {len(df)}")

# Check if there is another page

if next\_page\_url:

QUERY\_URL = next\_page\_url # Update URL for the next request

elif new\_cursor\_id:

params["cursorId"] = new\_cursor\_id # Update cursor ID for the next request

else:

print("All pages loaded into DataFrame.")

break # Exit loop when no more pages

# Return the full DataFrame

return df



* + Uses the retrieved **cursor ID** to request query results.
  + Handles **long polling**:
    - If the query is still processing, the server returns 202 Accepted, and the request is retried after a short delay.
    - If the query is completed, results are returned with 200 OK.
  + Extracts **pagination headers**:
    - X-Observe-Next-Page: URL for fetching the next page.
    - X-Observe-Cursor-Id: Cursor ID for constructing the next request.
  + Continues fetching pages until **all data is retrieved**.

1. **Load Results into Pandas DataFrame**
   * Parses response data as **CSV** .
   * Appends each page's data to a **single DataFrame**.
   * Returns the full dataset for further processing.

## **Function Breakdown**

### **execute\_opal\_query()**

* Executes an OPAL query.
* Extracts cursorId from the API response.
* Calls fetch\_paginated\_results() to retrieve all pages.

### **fetch\_paginated\_results()**

* Uses cursorId to fetch query results.
* Handles pagination and long polling.
* Loads all retrieved data into a Pandas DataFrame.
* Returns the **final consolidated DataFrame**.

NOTES:

There is parser issue on fortigate- the user id is getting ip address-

{"intermediary":[{"asset":{"hardware":[{"key":"devid","value":"FGT60FTK22044917"}]},"hostname":"Valqua\_Rayong\_Fac"}],"meta":{"description":"Negotiate IPsec phase 2","event\_hash":["LTYxNDM2ODU4NTUxMTQ5ODM0NDA="],"event\_type":"GENERIC\_EVENT","product":{"event\_type":"event - vpn","log\_id":"0101037122","name":"Fortinet Fortigate","product\_category":"VPN"},"timestamp":{"event":1740517361189},"vendor":{"name":"Fortinet"}},"network":{"direction":"UNKNOWN"},"principal":{"ip":[{"address":"110.170.37.130","port":500}],"primary\_ip":"110.170.37.130","user":{"attribute":{"labels":[null]},"id":"110.170.37.130"}},"result":{"action\_details":"negotiate","actions":["ALLOW"],"severity\_details":"notice","summary":"negotiate IPsec phase 2"},"target":{"ip":[{"address":"61.90.172.210","port":500}],"primary\_ip":"61.90.172.210","user":{"id":"110.170.37.130"}},"vendor":{"advpnsc":"0","assignip":"N/A","cookies":"e5a148e8f85426fa/e3e8922c6058be1a","fctuid":"N/A","group":"N/A","outintf":"wan2","role":"responder","status":"success","useralt":"N/A","vd":"root","vpntunnel":"IPsec-Bangpoo","xauthgroup":"N/A","xauthuser":"N/A"}}


