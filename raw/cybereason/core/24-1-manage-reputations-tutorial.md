The blocklist is for detection purposes only. Blocklisting an


[item will not prevent that item from executing. See Prevent File](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)

[Execution with Application Control (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)


[article=24-1-prevent-file-execution-with-application-](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)
[control&language=en_US#prevent-file-execution-with-](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)


[application-control) for details on preventing execution.](https://nest.cybereason.com/s/knowledge-base?article=24-1-prevent-file-execution-with-application-control&language=en_US#prevent-file-execution-with-application-control)


To ensure your allowlist and blocklist work properly for your


organization, the reputations that you manually add have priority

over other Cybereason threat detection methods.


You can add custom reputations for the following items:

Files (if you add a file, the reputation you assign applies to all


files with the same hash)

IP addresses


Domain names (not including subdomains)

## Step 1: Find the key for the item


The Cybereason platform identifies an item on the allowlist or


blocklist by using a unique key for the item. The value of this key

depends on the type of item that you want to add to the allowlist or


blocklist. You can add values for IP address, domains, or file

hashes.


Depending on the item, you need to provide the following:

For a file, the unique key is either the MD5 or SHA-1 file hash


value. Note that if you want Application Control to
automatically block a file based on the file hash, you must use


a MD5 file hash value and have Application Control enabled in

your environment.


For an IP address, the unique key is the IP address itself.

For a domain name, the unique key is the domain name itself.


This example explains how to add an item using IP addresses. To
add a file or domain name to the allowlist or blocklist, follow the


same steps but update the key value accordingly.

## Step 2: Download the custom reputation


When you have the item key, follow these steps to download the


custom reputation list template:

1. Open the **Security profile > Reputation** screen.


2. In the **Upload custom reputation list section**, click


**Download template** .


The custom reputation list template CSV file downloads to your

machine.


## Step 3: Add reputations for items

Once you have downloaded the custom reputation list template


you are ready to add your items and details to the template file.


1. On your machine, open the


**custom_reputation_list_example.csv** file.

2. Delete the example data contained in rows 2 and 3 of the


template so that only the column headers are visible.
3. Populate the file with the following data:







|Column|Description|
|---|---|
|key|The IP address. You need to enter each IP<br>address to be added to the allowlist individually<br>in its own row. For this tutorial, we will use the<br>following example IP addresses:<br>48.124.150.242,<br>66.56.186.46,<br>160.205.31.15|
|reputation|Add**whitelist** to add the IP address to the<br>allowlist or**blacklist** to add the IP address to<br>the blocklist.|
|prevent<br>execution|false|
|comment|Leave blank|
|remove|false|


To add IP addresses to the allowlist, populate the file as follows:


To add IP address to the blocklist, populate the file as follows:

## Step 4: Upload the revised custom

## reputation list template


Once the file has been prepared, it can be uploaded on the

platform.



