[behavior-when-exceeding-5-ram) for details.](https://nest.cybereason.com/s/knowledge-base?article=24-1-sensor-error-handling&language=en_US#sensor-behavior-when-exceeding-5-ram)


On Windows endpoints, If DPI collection is enabled, an additional

30 MB RAM will be consumed/partially consumed.

## CPU usage


Cybereason sensors generally consume less than 5% of CPU on

average on an idle machine.


CPU usage is managed less strictly than RAM. For example,

sensors do not enforce CPU usage limits.


Under normal circumstances, sensors should consume CPU

resources as follows:


When the machine is idle, the sensor uses between 0% and

1.3% of CPU resources.


When the machine is in use, the sensor uses an average of

3% or less of CPU resources.


The sensor temporarily consumes more than 5% of CPU after
the first deployment, and when restarted. In these cases, CPU


consumption typically returns to normal after about 3 minutes.

For an average endpoint user machine, a quick scan should


use a single CPU core for a maximum of 5-10 minutes.


Note


For Linux and Mac users: If you use the top command to

monitor processes, CPU usage for the sensor's minionhost


process is displayed as a total percentage across all cores,

and so it can appear to be higher than 5% on a multi-core


machine. For example, on a machine with 4 cores, 4% CPU

consumption would indicate 1% CPU usage on each core.


Each sensor consumes an average of 1.2 - 2.4 Kbps. Using the

higher estimate of 2.4 Kbps, this results in ~10 MB network usage


per 10 hr. work day per endpoint.


The following table shows projected network usage for different


network sizes, using the calculation:


Total network usage in Mbps = [2400 bps x (number of


endpoints)] / 220








|Number of<br>endpoints|Total network usage in Mbps<br>(megabits per second)|
|---|---|
|100|0.23 Mbps|


|Number of<br>endpoints|Total network usage in Mbps<br>(megabits per second)|
|---|---|
|1000|2.29 Mbps|
|10K|23 Mbps|
|50K|114 Mbps|
|100K|229 Mbps|


Note


The more active a machine is, the higher the network usage.

## Sensors and disk resources


Sensors use a maximum of ~150 MB on the disk.


This includes:


Sensor software: ~50 MB

Data storage space: ~100 MB (see below)


Sensors store data to disk when the sensor becomes

disconnected from or cannot transmit data to the Detection server.


The sensor can store up to 100,000 items on the disk. The

estimated space used to store this data is ~100 MB.


Cybereason uses a FIFO (first in, first out) storage model.
Historical data is cleared when 100 MB is filled up, leaving the


most recent data on the endpoint.

## Sensors with Endpoint Protection

## features enabled


This section includes estimates for sensor resource usage with


Endpoint Protection/NGAV features enabled.


The figures below represent usage estimates for all NGAV features


enabled. The **Anti-Malware > Signatures mode** feature accounts

for most of the additional resource usage. Other NGAV features


(Anti-Ransomware, PowerShell protection, Artificial Intelligence,

Application Control) account for a very minor part of resource


usage.


Note


Sensors using **Anti-Malware > Signatures mode** download


1.5 MB of Signature database updates per day.


Note


The figures below are estimates. Actual usage may vary

between environments.

## CPU usage estimates



|Scenario|CPU|
|---|---|
|Running in the background with no<br>malware found.|< %5 average|
|Upon fle disinfection.|%10 for a short spike<br>(depends on disinfection<br>scenario)|
|Under general stress (machine<br>under stress but not from<br>malware/disinfection scenarios).|%10 average|
|Under NGAV stress: disinfecting<br>thousands of malware<br>simultaneously.|~50% for disinfection<br>duration. Disinfection<br>duration is < 0.1 sec.<br>per fle.|
|During full scan|Up to 1 CPU core, i.e up<br>to 25% on a machine<br>with a 4 core processor.|

## RAM usage estimates

|Windows|Linux|macOS|
|---|---|---|
|600 MB|600 MB|900 MB|



Notes:





Memory usage can be elevated in certain scenarios, such as


during a full scan, on a busy machine that is performing file

operations, or during signature database updates.


Cybereason does not take up the RAM listed above

permanently, it uses only as much as needed.


## Network usage estimates






|Scenario|Network usage|
|---|---|
|Not during update (i.e.<br>most of the time).|< 2.4 Kbps (kilobits per second)|
|Initial installation: frst<br>update.|Downloads ~300 MB at maximum<br>speed (similar to a regular fle<br>download, no throttling)1.|
|AV - subsequent<br>updates (default query<br>frequency: every 15<br>min.)|Query without update takes 1-20<br>KB per hour, Query with DB update<br>(approx. 3-5 times per day)<br>downloads 0 - 2 MB.|



1When a sensor that has been offline for two weeks or more


comes back online, the sensor may download a ~300 MB

signatures package that contains an update, similar to a newly


installed sensor.

## Sensors and disk resources estimates


Sensors use a maximum of 2 GB on the disk. This includes:


Sensor software: ~100 MB

Data storage space: 150 MB (see below)


Signatures DB: ~1.2 GB


Sensors store data to disk when the sensor becomes


disconnected from or cannot transmit data to the Detection server.

The maximum amount of space the sensor uses to store data on


disk is approximately 150 MB.


Cybereason uses a FIFO (first in, first out) storage model.


Historical data is cleared when 150 MB is filled up, leaving the

most recent data on the endpoint.

## Analysis speed


Anti-Malware performs analysis of files on access and before they

can be executed, to detect and prevent malware. Anti-Malware


analyzes file for malware in less than 100 milliseconds.


[See Add sensor processes to third-party tool allowlists (all OSs)](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)


[(/s/knowledge-base?article=24-1-pre-installation-requirements-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)

[and-instructions&language=en_US#add-sensor-processes-to-](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)


[third-party-tool-allowlists-all-oss) for a list of sensor processes.](https://nest.cybereason.com/s/knowledge-base?article=24-1-pre-installation-requirements-and-instructions&language=en_US#add-sensor-processes-to-third-party-tool-allowlists-all-oss)


Note



