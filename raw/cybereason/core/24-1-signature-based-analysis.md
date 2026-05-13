## Protection against known threats video

## How does signature-based analysis

Signature-based analysis utilizes file scans to find known malware.


By default, the Cybereason platform scans files that have

extension types that can be executed, loaded, or run, because


these files could contain malware or malicious content. For
example, scanned files include files that have **.exe**, **.dll**, and


**.docx** extensions.


Signature-based scans take place at the following times and


locations:


|Time of<br>scan|Description|How to<br>execute the<br>scan?|Location of<br>scanned<br>files|
|---|---|---|---|
|On access<br>fle scans|The Cybereason<br>platform scans<br>fles when the<br>end user<br>attempts to<br>access them.|Automatic|Local and<br>network<br>drives (note:<br>Linux<br>sensors do<br>not scan<br>network<br>drives)|
|Scheduled<br>scan|Administrators<br>can confgure<br>periodic full or<br>quick scheduled<br>scans at specifc<br>times.|Confgure<br>from the<br>Sensor<br>policy ><br>Anti-<br>Malware<br>screen.|Local drives|
|On<br>demand<br>scan|Administrators<br>can select<br>specifc sensors<br>and perform full<br>or quick on<br>demand scans.|Perform<br>from the<br>**System >**<br>**Sensors**<br>screen.|Local drives|



The Cybereason platform treats removable media such as USB


and external hard drives as local drives and includes these

removable media as part of scans. During scheduled scans, the


Cybereason platform scans any files inside the USB drive. During
an on-access scan, any file or directory that the user attempts to


open on the USB drive is scanned.


[For more details on scans, see Configure scan properties](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-anti-malware-modes&language=en_US#configure-scan-properties)


[(/s/knowledge-base?article=24-1-set-the-anti-malware-](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-anti-malware-modes&language=en_US#configure-scan-properties)
[modes&language=en_US#configure-scan-properties).](https://nest.cybereason.com/s/knowledge-base?article=24-1-set-the-anti-malware-modes&language=en_US#configure-scan-properties)


If you enable **Anti-Malware > Signatures mode**, sensors receive

signature database updates every 15 minutes from the NGAV


Global update server, ensuring that the database remains current

and helping the sensors detect and prevent known malware with


very high accuracy. The sensor downloads 1.5 MB of Signature

database updates per day.


Note


Signature-based analysis is supported on Windows, Mac, and


Linux endpoints. For details on supported platforms, see

[Endpoint machine prevention features (/s/knowledge-base?](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-prevention-features)


[article=24-1-supported-features-by-operating-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-prevention-features)

[system&language=en_US#endpoint-machine-prevention-](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-prevention-features)


[features).](https://nest.cybereason.com/s/knowledge-base?article=24-1-supported-features-by-operating-system&language=en_US#endpoint-machine-prevention-features)

## How does signature analysis determine if

## a file is malicious?


The Anti-Malware signatures analysis service scans files using


advanced detection logic. The service also inspects the file to
determine the file's reputation and to search for malicious content


embedded in the file, such as a module or script.


Depending on its findings, the Cybereason platform determines


other actions:






|Determination|Reputation|Anti-Malware Action|
|---|---|---|
|File is infected.|Allowlist|Ignore the fle and allow the<br>fle to be opened.|
|File is infected.|Neutral or<br>Blocklist|Prevent the fle from opening.<br>If Signatures mode is set to<br>**Disinfect**, disinfect the fle if<br>possible, and report the event<br>as an Endpoint Protection<br>MalOp in the**Malops**<br>**management** screen. If the<br>malware cannot be fully<br>cleaned from the fle, remove<br>the fle from the machine (do<br>not quarantine the fle). If<br>Signatures mode is set to<br>**Prevent**, prevent the fle from<br>executing but do not modify<br>or move the fle.|
|File is clean.|Neutral or<br>on allowlist|No action is taken and the fle<br>can be opened.|
|File is clean|Blocklist|Report the event as an<br>Endpoint Protection MalOp in<br>the**Malops management**<br>screen. Allow the fle to open.|



