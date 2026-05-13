## First Execution of a downloaded process

**Goal:** Review the behavior of a downloaded process after it runs
for the first time. The results include information such as whether


the process has Suspicions, what the parent processes are, when

the processes were created, and so forth.


**Explanatory statement:** I want to investigate the behavior of a
process that was downloaded after that process runs for the first


time.


Construct this query:


**Process** Element -> filter for First Execution of Downloaded

Process is _True_

## DGA


**Goal:** Search for malicious characteristics of a process. The


results return information including the process tree, command
line arguments, and file path for each process.


**Explanatory statement:** I want to look at some malicious

characteristics of a process, such as the fact that it has


unresolved DNS queries or the image file is not verified.


Construct this query:


**Process** Element -> Has unresolved DNS queries is _True_ AND
Image file verified is _False_



