The following are known limitations for building queries.
If saved queries contain deprecated Features, those Features
will not be populated in the filter bar when you load the saved
query.
The description of your Investigation query (displayed under
the Element and Feature edit field) is partially untranslated for
platforms set to a language other than English.
When exporting information to CSV from the Investigation
screen, the CSV file contains the data as viewed from the
individual browser. This data may not be exactly the same as
the data saved in the server.
In the Investigation screen, columns related to capabilities
available on newer versions of the Cybereason sensor display
No Data for machines running older sensors.
In the Investigation screen, the end time is missing, if the end
time of a process was not collected.
URLs and domains that include non-ASCII characters (such
as Japanese) are displayed in punycode characters. To
obtain the actual domain/URL, you can use a punycode
converter.
The count filter does not validate that the user input value is a
number until after the query runs. After the query runs, NaN
(Not a Number) is displayed in the query statement.
In infrequent scenarios where the Detection server is sent a
high volume of data within a short time period (e.g. data on
autorun programs), some of the collected information will not
be saved and will not be visible in the Investigation >
Element details screen.
If you search for machine interactions with the Machine
Interaction element, when you search for machine names (for
example machine1), you may receive no results. This is due to
the fact that the displayed name for the Element in the
Investigation results is calculated after the Element is created
in the Cybereason CMC Engine. Therefore, the internal name
used by the CMC Engine (from the Element creation) is
different than the calculated name displayed in the results.
