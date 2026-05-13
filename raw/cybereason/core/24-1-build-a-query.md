1. Build a query: Select Elements, such as **Process** or **User** to


add to your query.

2. Filter bar: Add Features, operators, and values to apply to the


selected Element. You can also click the **Filters** button to view

a list of Features to filter by.


3. Timeline and Suspicions filters: Filter query results by the time

the result was created or existed, or by a specific suspicion.


4. Get results: Run or re-run your query.

5. Action bar: Limit the number of results shown with the **Limit**


**results** button, export the results with the **Export CSV** button,

or customize which columns are displayed in the results with


the **Edit columns** button.

6. Query results: View the results of your query. Click an item to


view the **Element details** pane for the element.

7. Pagination: Specify how many results appear on one page


(100, 500, 1000, 2000, or 4000), and navigate between

pages.


Each query statement uses one or more phrases that narrow

down the query results. Each phrase contains an Element (such


as 'Process' or 'File'), one or more Feature for the Element (such

as 'Process name'), and values for each Feature (such as the


name of the process you are filtering by).


Elements, which appear as green circles in the **Build a query**


section of the **Investigation** screen, are the main building blocks

of queries. For each Element you add to your query chain, you


can use the filters box below the Element to specify Features of
the Element by which to filter.


Features are the characteristics or behaviors of the Elements,


such as 'Process name'. For each Feature you add to the filter,

you can specify one or more values (such as the process's name


you want to filter by).


You can also add an individual Feature to the filter statement


multiple times. For example, you can add **Command line**

**contains 'abc'** and **Command line does not contain 'xyz'** to the


same filter statement to return items whose command line

contains the string 'abc' but not the string 'xyz'.


You can add multiple filters (Feature/operator/value statements) to

an Element. These statements are connected by an implicit 'AND'


logical operator. Alternatively, you can separate the statements by

an 'OR' logical operator by hovering over the space between the


statements and clicking the 'OR' button that appears. Statements

separated by 'AND' logic return only items that satisfy both


statements. Statements separated by 'OR' logic return results that

satisfy at least one of the statements.

## Build an investigation query


1. In the **Investigation** screen, from the top part of the screen,


select an Element.


2. Select additional Elements from the **Build a query** section to


create a query path. The path shows the logic of your search.


The query builder displays your choices under the **Search for**
**filters** bar. By default, there is a logical AND between


Elements.


3. Select an Element in your query path to filter by a property


(Feature) of that Element. The screenshot in step 2 has the

**Logon session** Element selected.


4. In the **Search for filters** box, start typing to find a Feature, or


click the **Filters** button to view the list of available Features.


5. Add operators and values to the filters box. See the Apply


search options for Features section below.


**Tip** : Use tab-completion for faster query building.
6. Add other Elements and filters as needed.


In the following screenshot we added the **Product type is**
**Microsoft Office** filter to the **Process** Element, and the


**Product type is Shell** filter to the **Children** Element. The


query will return shell processes that are children of Microsoft


Office processes.


[For more query examples, see Query Use-Case Examples](https://nest.cybereason.com/s/knowledge-base?article=24-1-query-use-case-examples&language=en_US#query-use-case-examples)


[(/s/knowledge-base?article=24-1-query-use-case-](https://nest.cybereason.com/s/knowledge-base?article=24-1-query-use-case-examples&language=en_US#query-use-case-examples)

[examples&language=en_US#query-use-case-examples).](https://nest.cybereason.com/s/knowledge-base?article=24-1-query-use-case-examples&language=en_US#query-use-case-examples)


7. Select a timeframe within which to search. Options include the


last hour, 6 hours, 12 hours, or 24 hours, the last 3 or 7 days,


or all data. Default value is 24 hours.


8. Click **Get Results** . Alternately, press CTRL+Enter (Windows)


or Command+Enter (Mac).


The Cybereason platform returns a list of all items that fit the


query. Columns in the results grid display various properties of


each Element. The indicates the number of suspicions


associated with this Element. The indicates the number


of Malops associated with this Element.


[For details on sorting and filter the results, see Analyze Query](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-query-results&language=en_US#analyze-query-results)


[Results (/s/knowledge-base?article=24-1-analyze-query-](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-query-results&language=en_US#analyze-query-results)

[results&language=en_US#analyze-query-results).](https://nest.cybereason.com/s/knowledge-base?article=24-1-analyze-query-results&language=en_US#analyze-query-results)


Note


When you click **Get Results**, ensure that you select the


Element for which you want to view results. The platform

displays the results by Element type. The results always


show the type of the last (right-most) Element in the query

chain unless a different Element is selected. If you have


multiple items in the query chain and you select an earlier

item, the results represent the earlier Element, not the full


chain.

## Apply search options for Features


When you add multiple Features to an Element, add search


operators. The available operators differ depending on the data
type of Feature, as specified in the following tables. For details on


[the data type for each Feature, see the see the Query Elements](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

[and Features (/s/knowledge-base?article=query-api-token-query-](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)


[elements-and-features-version-232148-and-later) topic in the](https://nest.cybereason.com/s/knowledge-base?article=query-api-token-query-elements-and-features-version-232148-and-later)

Cybereason API documentation.

## String and enum data type operators






|Operator|Description|
|---|---|
|is|Returns items that are an exact match to the<br>search string or the selected enum value.|
|is not|Returns items that are not an exact match to the<br>search string or the selected enum value.|
|contains|Returns items in which the search string or<br>selected enum value appears, even as only part<br>of the complete string.|
|doesn't<br>contain|Returns items that do not contain the search<br>string or selected enum value.|
|matches<br>word|Returns items in which the entire word appears<br>as its own string. The Cybereason platform will<br>not return results for items in which the word<br>appears as part of a larger string. For example,<br>entering "matches word: svchost" returns<br>"svchost.exe" values. However, searching for<br>"matches word: svc" does not return<br>"svchost.exe" nor any other result that contains<br>"svc" within a longer word.<br>For customers with the older platform<br>architecture, use**is**.|


|Operator|Description|
|---|---|
|doesn't<br>match<br>word|Returns items that do not contain the search<br>string. For customers with the older platform<br>architecture, use**is not**.|
|starts with|Returns items that start with the selected value.<br>Note<br>This operator is supported for use only when<br>building behavioral allowlisting rules for<br>command line Features.|
|ends with|Returns items that end with the selected value.<br>Note<br>This operator is supported for use only when<br>building behavioral allowlisting rules for<br>command line Features.|


## Numeric data type operators














|Operator|Description|
|---|---|
|equals|Returns items that are an exact match to the<br>numeric value in the query.|
|doesn't<br>equal|Returns items that are not an exact match to the<br>numeric value in the query.|
|less than|Returns items that are less than the numeric<br>value in the query.|
|greater<br>than|Returns items that are greater than the numeric<br>value in the query.|
|between|Returns items that are between two values,<br>including the two values.|



