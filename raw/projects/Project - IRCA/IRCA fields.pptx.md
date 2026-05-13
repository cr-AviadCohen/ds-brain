# IRCA fields.pptx

<!-- Slide number: 1 -->

![](GoogleShape254p34.jpg)
# IRCA
PROJECT

### Notes:

<!-- Slide number: 2 -->
# Malops data extract chart
Detection Malop
Malop
API- rest/detection/inbox
To extract Malops GUIDs and detection engine
Malop GUID AND
Malop GUID AND
detectionEngines is not EDR AND data.resultIdToElementDataMap.<guid>.simpleValues.etectionType.values is not RANSOMWARE
detectionEngines is EDR AND data.resultIdToElementDataMap.<guid>.simpleValues.etectionType.values is RANSOMWARE
API- rest/detection/details
To extract detection Malops details
API- rest/crimes/unified
To extract Malop details (including process GUID)
Process GUID

API- rest/visualsearch/query/simple
To extract process details
‹#›

### Notes:

<!-- Slide number: 3 -->
# API- rest/detection/inbox

Description:
Return a list of all MalOps of all types (Endpoint Protection MalOps and Server-side MalOps)

Fields:
malops.guid (could be more than one guid)
malops.detectionEngines (the engine that triggered the malop) (could be more then one values)

We should check if the detectionEngines value is EDR or anything else:
If the value is equal to EDR- this is a Malop case
If the value is equal to EDR and data.resultIdToElementDataMap.<guid>.simpleValues.etectionType.values is equal to RANSOMWARE- this is a Malop case
If the value is not equal to EDR and data.resultIdToElementDataMap.<guid>.simpleValues.etectionType.values is not equal to RANSOMWARE - this is a Detection Malop case
‹#›

### Notes:

<!-- Slide number: 4 -->
# API- rest/crimes/unified

Description:
Return a list of all MalOps currently active in your environment.

Fields:
data.resultIdToElementDataMap.<guid> (contain multiple data of specific guid- could be more then one guid)
data.resultIdToElementDataMap.<guid>.simpleValues.decisionFeature.values (contain the malop name as written in the backend- for example Process.credentialTheftMalop(Malop decision))
data.resultIdToElementDataMap.<guid>.simpleValues.creationTime.values (should be the time that the Malop was created)
data.resultIdToElementDataMap.<guid>.simpleValues.rootCauseElementHashes.values (the process sha-1 hash)
data.resultIdToElementDataMap.<guid>.elementValues.primaryRootCauseElements.elementValues.guid (the process guid)
data.resultIdToElementDataMap.<guid>.elementValues.primaryRootCauseElements.elementValues.name (the process name)
data.resultIdToElementDataMap.<guid>.elementValues.affectedUsers.elementValues.name (user name) (could be more than one user)
data.resultIdToElementDataMap.<guid>.elementValues.affectedMachines.elementValues.name (machine name) (could be more than one machine)
data.resultIdToElementDataMap.<guid>.elementValues.affectedMachines.elementValues.guid (machine guid) (could be more than one machine)
‹#›

### Notes:

<!-- Slide number: 5 -->
# API- rest/visualsearch/query/simple

Description:
Run investigative query to find the relevant data of the suspected process.
Fields:
data.resultIdToElementDataMap.<process guid that related to the Malop>
data.resultIdToElementDataMap.<process guid>.simpleValues.creationTime.values (process creation time)
data.resultIdToElementDataMap.<process guid>.simpleValues.commandLine.values (process commandline)
data.resultIdToElementDataMap.<process guid>.simpleValues.endTime.values (process end time)
data.resultIdToElementDataMap.<process guid>.simpleValues.elementDisplayName.values (process name)
data.resultIdToElementDataMap.<process guid>.elementValues.parentProcess.elementValues.name (parent process name)
data.resultIdToElementDataMap.<process guid>.elementValues.imageFile.elementValues.elementValues.elementValues.name (file SHA-1 hash value)
Query:
{"queryPath":[{"requestedType":"DetectionEvents","filters":[{"facetName":"detectionEngine","filterType":"Equals","values":["AntiVirus"]}],"isResult":True}],"totalResultLimit":"100","perGroupLimit":100,"perFeatureLimit":100,"templateContext":"SPECIFIC","queryTimeout":120000,"pagination":{"pageSize":1000,"skip":0},"customFields":["detectionEngine","decisionStatus","detectionValue","firstSeen","process","user","ownerMachine","endTime","elementDisplayName"]}
‹#›

### Notes:

<!-- Slide number: 6 -->
# API- rest/detection/details

Description:
Return details on a specific MalOp (Endpoint Protection MalOps only)
Fields:
detectionEngines (the engine that triggered the detection malop) (could be more than one)
detectionTypes (the activity that was detected)(in our example- "Variant Payload Protection Detected Malicious Payload")
detectionValues (the signature name) (could be more than one)
decisionStatuses (detected or prevented)
machines.guid (machine guid)
processes.lastDetectionDecisionStatus (DDS_UNKNOWN in out example - could be dds_prevent or dds_detect)
processes.elementDisplayName (the name of the process than triggered the detection malop)
processes.ownerMachine (the name of the machine)
processes.calculatedUser (the name of the user)
processes.commandLine (the process commandline)
processes.creationTime (process creation time)
processes.guid (process guid)
‹#›

### Notes:

<!-- Slide number: 7 -->
# API- rest/detection/details - continue

Fields:
files.lastDetectionDecisionStatus
files.ownerMachineName
files.sha1String (file hash)
files.correctedPath (file path)
files.elementDisplayName (file name)
files.guid (file guid)

If there is no ‘processes.’ or ‘files.’ look for those fields (collect them if they're not empty []):
displayName
filePaths
fileHash
machines.displayName
users.displayName
commandLines
‹#›

### Notes:

<!-- Slide number: 8 -->
# Critical Processes

| Bitsadmin.exe Certutil.exe Cmd.exe Cmstp.exe Control.exe Csc.exe Cscript.exe Esentutl.exe Forfiles.exe Installutil.exe Mavinject.exe | Msbuild.exe Mshta.exe Powershell.exe Reg.exe Regasm.exe Regsvcs.exe Rundll32.exe Sc.exe Schtasks.exe Wscript.exe |
| --- | --- |
‹#›

### Notes:

<!-- Slide number: 9 -->
# API- rest/visualsearch/query/simple (Critical Processes)

Description:
Run investigative query to find the relevant data of the critical processes (mentioned in the last slide).
Fields:
data.resultIdToElementDataMap.<process guid>.simpleValues.creationTime.values (process creation time)
data.resultIdToElementDataMap.<process guid>.simpleValues.commandLine.values (process commandline)
data.resultIdToElementDataMap.<process guid>.simpleValues.endTime.values (process end time)
data.resultIdToElementDataMap.<process guid>.simpleValues.elementDisplayName.values (process name)
data.resultIdToElementDataMap.<process guid>.elementValues.parentProcess.elementValues.name (parent process name)
data.resultIdToElementDataMap.<process guid>.elementValues.imageFile.elementValues.elementValues.elementValues.name (file SHA-1 hash value)
Query:
{"queryPath":[{"requestedType":"Process","filters":[{"facetName":"ownerMachine","filterType":"Equals","values":["chen_win11_vm"]},{"facetName":"elementDisplayName","filterType":"Equals","values":["Bitsadmin.exe","certutil.exe","cmd.exe","cmstp.exe","control.exe","csc.exe","cscript.exe","esentutil.exe","forfiles.exe","installutil.exe","mavinject.exe","msbuild.exe","mshta.exe","reg.exe","regsam.exe","regsvcs.exe","sc.exe","schtasks.exe","wscript.exe","powershell.exe","rundll32.exe"]},{"facetName":"creationTime","filterType":"Between","values":[1754554803750,1754814009491]}],"isResult":True}],"totalResultLimit":"100","perGroupLimit":100,"perFeatureLimit":100,"templateContext":"SPECIFIC","queryTimeout":120000,"pagination":{"pageSize":1000,"skip":0},"customFields":["elementDisplayName","commandLine","creationTime","productType","parentProcess","imageFile","imageFile.companyName","imageFile.productName","relatedToMalop","iconBase64","ransomwareAutoRemediationSuspended","executionPrevented","isWhiteListClassification","matchedWhiteListRuleIds","endTime"]}
‹#›

### Notes:

<!-- Slide number: 10 -->
Data Extraction Chart
MALOPS
CRITICAL PROCESSES
API- rest/detection/inbox
To extract Malops GUIDs and detection engine(all the malops in the env)
API-rest/visualsearch/query/simple
To extract critical processes for specific machine
Detection Malop
Malop
Malop GUID AND
Malop GUID AND
detectionEngines is EDR AND data.resultIdToElementDataMap.<guid>.simpleValues.etectionType.values is RANSOMWARE
detectionEngines is not EDR AND data.resultIdToElementDataMap.<guid>.simpleValues.etectionType.values is not RANSOMWARE
API- rest/detection/details
To extract detection Malops details
(for each detection event)
API- rest/crimes/unified
To extract Malop details (including process GUID)
(for ech edr malop)
Process GUID

API- rest/visualsearch/query/simple
To extract process details
(for each process in a specific malop)

### Notes:
