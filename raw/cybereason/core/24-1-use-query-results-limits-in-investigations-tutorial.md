6. Below the **Search for filters** field, click **Edit columns** .


7. In the **Edit columns** dialog box, in the upper right corner, in

the **Search all columns** field, enter **Has opened socket** .


8. Select the **Has opened socket** option.

9. Follow the previous two steps to add additional columns for:


**Has Malicious Connection**

**Rare remote address evidence**


**High Data Transmitted**

**Many internal connections**


You can use numerous other columns (Features) as desired.


10. Click **Get results** .


The Cybereason platform runs the query. Depending on how

many sensors you have in your environment, this query may take


some time to return results.

## Add query results


After you run the query, you receive a large number of results,


more than you can probably analyze. To help with this, you can

add query limits:


1. Above the results list, click **Limit results** . The **Limit results**


dialog box opens.


2. In the **Limit results** dialog box, adjust the results limit slider to


**10k** . This ensures that the Cybereason platform only returns

10,000 total results (although there may be more).


3. Below the slider, select **Sample results** . This option enables


the Cybereason platform to sample groups of very similar


results up to 1% of the total number of results instead of


returning all similar results. This frees up the platform to return


more unique results.

4. Below the **Sample results** option, add a time limit of **90**


seconds. This ensures that the results only include data from

sensors that returned information within a 90 second period.


Setting a timeout period ensures that you do not overload your

server for such a broad query.


5. Click **Apply** . The Cybereason platform returns the results


based on the new criteria.


As you adjust the criteria, you should see a difference in the

number of results.

## Limit results by time


In addition to filtering result totals, you can also limit (or filter)

results by time.


**To limit results by time, follow these steps:**


1. Above the results grid, to the right of the query builder, locate


the **Timeline** section.

2. In the **Timeline** section, select **Existed** .


3. Next to the **Existed** option, select **Last week** . This revised the


results instantly for results that existed in the past week. If you


run the query on a regular basis, this option enables you to

view only the most up-to-date results instead of reviewing


results you previously analyzed.


4. Use these time-based filters to help you narrow and analyze


only the most meaningful results.



