**To perform a basic file search, follow these steps:**


1. In your Cybereason platform, navigate to the **Live File Search**


screen.


2. In the **File Search** screen, select the **Standard search** tab.

3. In the **Standard search** screen, in the **File properties**


section, in the **Name** field, enter the file name

_ransom_encrypt.exe_ .


4. Click **Search** .


By default, the search will run for 10 minutes. If you want in later


searches, you can extend the timeout period.


This search runs on up to 5000 sensors connected to your


Cybereason environment.


The Cybereason platform saves the search so you can run it again


in the future. You can also remove the search if you want to, or if

you reach the maximum number of saved searches.

## Search a specific machine or folder


Searching for only a file name could take a long time or lead to

confusing results (especially if, for example, you use a wildcard to


search for files of a specific type). To help you target the file
search, you can search specific folders or machines.


For this tutorial, imagine you learned from threat intelligence that

this ransomware is an attachment that users download. Therefore,


you modify the existing search for _ransom_encrypt.exe*_ to search
the **Downloads** folder. If you know more about the file, such as the


machines it targeted, or the time when it entered one machine in

your organization, you can also search by **Machines** and **Time** .


**To perform a more specific search, follow these steps:**


1. In the **Live File Search** screen, select the **Standard search**


tab.

2. In the **Standard search** tab, in the **File properties** section, in


the **Name** field, enter _ransom_encrypt.exe_ .
3. Next to the **File name** field, find the **Folders** field. This is the


place you enter the specific folders that you want to search.
4. In the **Folders** field, enter **%userprofile%/Downloads** .


5. Click **Search** .


By default, the search will run for 10 minutes. If you want in later


searches, you can extend the timeout period.


This search runs on up to 5000 sensors connected to your


Cybereason environment.

## Analyze the results


When the search completes, the Cybereason platform displays


the results in a grid at the bottom of the **File Search** screen.



