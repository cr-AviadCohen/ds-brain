## Live File Search

You can search up to 5000 machines in a single file search


operation.
YAR files for a YARA rule file search must be 5 MB or smaller.


The Cybereason platform limits the number of results to a total
of 2500 results, and 20 per sensor. These results are the first


results found during the search, regardless of date. The

Cybereason platform also saves results for 20 days after the


initial search.

The Cybereason platform saves the environment's 50 most


recent searches. After reaching 50 searches, you cannot run

new searches unless previous searches are completed and


are removed. To view more details on the run searches, see

the system log.


The Cybereason platform does not search password
protected files.


When viewing the file search results, if the number of results

exceeds the available space in the browser display, you


cannot scroll to see additional results.

Searching for files with YARA rules is not supported for


machines running supported versions of Linux.
When searching for a file on a Linux machine, symbolic link


files are not followed.

## Browse files


You can only browse the file system for machines that are


currently online.

When you click **Browse Files** in the File Search screen, the UI


shows up to 1000 files and folders per directory. Upon

request, Technical Support can modify this limit.


When you enter a path for a file in the search filters, the

maximum length is 500 characters.


By default, when you browse through files from the Element
Details screen, you can view up to 1000 files. Open a


[Technical Support (/s/support) case to increase this limit.](https://nest.cybereason.com/s/support)
The maximum number of files you can view with the **Browse**


**files** button is 20,000.

## IR tool and forensic data ingestion task


To support incident response tool deployment, an endpoint


needs to have the GeoTrust RSA CA 2018 Intermediate CA

and DigiCert Global Root CA certificates in the operating


system certificate store.
If your network uses mechanisms such as certificate pinning,


SSL inspection, or other mechanisms that use TLS

termination, you must ensure that TLS termination is canceled


for any traffic from the endpoint machine to the Cybereason

platform.



