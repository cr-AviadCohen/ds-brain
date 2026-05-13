|Tag name|Description|Data<br>type|Value options|
|---|---|---|---|
|Critical<br>Asset|Specifes whether<br>or not this asset is<br>critical to your<br>organization|Boolean|TRUE, FALSE|
|Department|Department the<br>asset belongs to|String|Free text: 100<br>characters max<br>ASCII<br>characters only|


|Tag name|Description|Data<br>type|Value options|
|---|---|---|---|
|Location|Location of the<br>asset|String|Free text:100<br>characters max<br>ASCII<br>characters only|
|Device<br>Type|Type of asset|String|Free text:100<br>characters max<br>ASCII<br>characters only|
|Custom<br>Tags|Single feld for<br>custom tag<br>information|String|Free text: 100<br>characters<br>max, ASCII<br>characters only|


Important









To prevent unintended tagging, you cannot add tags to


sensors that have the same machine name or FQDN value as

another sensor in your environment.

## Add tags


There are two ways to add sensor tags:

Update the CSV template file


[Create sensor tags (/s/knowledge-base?article=sensor-api-](https://nest.cybereason.com/s/knowledge-base?article=sensor-api-token-create-sensor-tags)

[token-create-sensor-tags) for individual sensors using the API](https://nest.cybereason.com/s/knowledge-base?article=sensor-api-token-create-sensor-tags)


**To add tags using a CSV file**


1. In the **System > Sensors** screen, click the **Actions** button.


Note


It does not matter what, if any, machines are selected


before clicking the **Actions** button.


2. Select **Import sensor tags CSV** .


3. In the pop-up, click **Download an example file** to download

the **sensor_tags_example** CSV file.


4. In the downloaded CSV file, update the file with the fields


noted in the following table.










|Field<br>header|Description|Value options|
|---|---|---|
|entity<br>type|Type of entity to set tags<br>for.|MACHINE|
|entity id|Unique ID of the entity.<br>This value is case<br>sensitive and must match<br>the machine name<br>exactly as it appears in<br>the**Sensors** screen.|Example:<br>CEO_Laptop|
|tag<br>name|One of the fve tag names<br>defned by Cybereason|Critical asset,<br>Department,<br>Location, Device<br>type, Custom Tags|
|tag<br>value|Custom value for the<br>specifed 'tag name' feld|Example value for<br>tag name<br>'Department':<br>Finance|
|action|States whether to add or<br>remove the specifed tag<br>for the entity|SET<br>REMOVE|



5. After you update the tag details in the CSV file, drag and drop

a CSV file or click **Browse to upload** and select the CSV file


6. Click **Import** to upload the file.


7. After the file successfully uploads, click **Import** to apply the


file to your sensors.

## Sensor tag CSV file requirements


The CSV file containing the sensor tag details **must** meet the


following requirements:

It must be a CSV in comma-separated file format (not tab


delimited or otherwise formatted).

The first row (or first five comma-separated values) must


match the values in the **Field** header column.

The file size must be below 300 MB.


There is no limit on the number of sensor tags that can be
included in the CSV file.


The characters in the file must be in UTF-8 or a UTF-8

interpretable character set.


The # character is not supported in machine names.


Note


The sensor tagging CSV upload supports character sets that

can be interpreted using UTF-8 without BOM. This includes


UTF-8 without BOM itself, as well as ASCII characters, which

is effectively a subset of UTF-8.


The following image is an example CSV file an administrator might

upload to apply sensor tags.

## Verify upload


To verify that the Cybereason platform is processing your upload:


1. In the **Sensors** screen, view the **Actions log** to verify your file


was successfully uploaded.


Important


A successful upload does not necessarily mean there are


no errors in a row in the CSV file. See the Troubleshoot the

CSV upload section for more information.


2. Click **Download summary file** to view the sensor tag upload

summary CSV file to verify that each row is free of errors. In


addition to the fields in the uploaded CSV file, the summary
file contains the following columns:












|Field<br>header|Description|Value options|
|---|---|---|
|Prior tag<br>values|Previous value of the tag<br>for this entity, if any.|Valid value tags|
|Results|Indicates whether or not<br>the action succeeded.|Success, Failure|
|Errors|Description of why the<br>action failed.|Various error<br>descriptions|



The following image is an example of a summary file that

contains errors (indicated by the 'failure' value in the 'Results'


column).


3. If your file contains errors, make corrections in your CSV file


and re-upload it.


To download machine information, including the values for the


tags:


1. From the UI **System > Sensors** screen select the sensors you


want information for.

2. Click the **Actions** button.


3. Select **Export to CSV** .

## Troubleshoot the CSV upload


Cybereason verifies the sensor tags CSV file in two phases:


1. On upload

2. On import


Your file could fail to upload if:


It is not in CSV format


The file too large (>300 MB)

The number of columns is incorrect


Your file could upload successfully, but not import if:


The time between successful upload and when you click the
**Import** button exceeds five minutes.


Important


A successful upload does not necessarily mean there are not


errors on the row level. View the sensor tagging summary CSV
file to verify that each row is free of errors. If your file contains


errors, make corrections in your CSV file and reupload it.

## Use tags to filter sensors


Sensor tags allow administrators to easily filter, manage, and


query sensors.


**To filter sensors by tag:**


From the **System > Sensors** screen, use the filter field to specify

the tag name, operator, and value. For example, you could search


for 'Department contains QA':

## Maintain tags


It is important to keep sensor tags up-to-date so system


administrators have accurate information about every machine on

your network.


Whenever any of the following events occurs, update and reload
your sensor tags file:


You add one or more machines to your network.

You retire one or more machines from your network.


The status of any machine on your network changes, with

regards to the tagged attributes:


Critical Asset

Department


Location

Device Type


Custom



