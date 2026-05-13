## Step 1: Create the query


For this tutorial, you create a query to find instances of the


BITSAdmin LOLBin technique. Once you have the query, you can

then add more columns to return related information about


instances of the BITAdmin utility.


**To build the query, follow these steps:**


1. In your Cybereason platform, navigate to the **Investigation**


screen.


2. In the **Investigation** screen, add a **Process** Element.
3. Below the Process Element, in the **Search for filters** filed,


enter **Process name** and select it from the dropdown list.

4. Select **contains** .


5. Enter _bitsadmin.exe_ for the value for the Process name filter.

6. Next to the **bitsadmin.exe** value, enter **Command line** and


select it from the dropdown list.

7. Select **contains** .


8. Enter _add file_ **OR** _transfer_ **OR** _download_ for the values.


Your query should look like this:

## Add additional columns


For the results, given what we know about the use of the


BITSAdmin utility by attackers, there are potentially a few

worthwhile items to investigate:


Child processes launched by BITSAdmin

Files opened by the BITSAdmin utility


Connections made by the utility

Machines on which the utility was run (as there are also


instances where the utility is used legitimately)


Given these criteria, there are numerous different columns to add


as part of the query results.


**To add relevant columns, follow these steps:**


1. Below the query builder, above the results area, click **Edit**


**columns** .


2. In the **Edit columns** dialog box, in the upper-right hand

corner, in the **Search all columns** field, enter **Children** . The


Cybereason platform displays a list of related Features.

3. From the list of columns, select **Children** .


This adds the **Children** column to the list of results. This


column is only visible when you run the query.

4. Repeat steps 2 and 3 to add additional columns:






|Column|Purpose|
|---|---|
|Owner machine|The machine on which the instance of<br>the BITSAdmin utility was found.|
|Connections|A list of connections made by instances<br>of the BITSAdmin utility.|
|Opened fles|A list of fles opened by the BITSAdmin<br>utility.|
|Has external<br>connection<br>Has internal<br>connection<br>Has outgoing<br>connection|Indicates whether the instance of the<br>BITS Admin utility has opened internal,<br>external, or outgoing connections.|



There are numerous additional columns (Features) available to


use with this query. However, the columns we have added can
sufficiently provide some initial data for our query example.


5. Run the query.



