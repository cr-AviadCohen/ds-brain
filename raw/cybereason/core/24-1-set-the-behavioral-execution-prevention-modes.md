|Mode|Description|When to use this<br>setting|
|---|---|---|
|Disabled|Do not use Behavioral<br>execution prevention<br>(default).<br>In this scenario, while<br>the Behavioral execution<br>prevention feature is set<br>to**Off** on the endpoint,<br>the Cybereason platform<br>applies the proprietary<br>detection rules in the<br>platform's Cross<br>Machine Correlation<br>(CMC) engine.|You want to collect<br>data on process<br>behavior, without<br>preventing the<br>processes.|


|Mode|Description|When to use this<br>setting|
|---|---|---|
|Detect|Detect anomalies in<br>process characteristics,<br>but take no further action<br>on the endpoint.|You want to detect<br>anomalies in<br>process<br>characteristics,<br>without preventing<br>the processes.<br>You want to be<br>aware of<br>suspicious<br>processes and<br>use that data for<br>investigation and<br>hunting.|
|Prevent|Prevent malicious<br>processes executing.|You want to identify<br>and block malicious<br>processes.|


## Set the Variant payload prevention mode

Variant payload prevention allows you to protect your organization


against powerful attack tools, by performing real-time analysis of

memory. You can use Variant payload prevention as a powerful


protection layer on top of Behavioral execution protection, or

independently, even when Behavioral execution protection is


disabled.


In your sensor policy, in the **Behavioral execution prevention**


screen, under the **Variant payload prevention** section, select one

of the following modes:


|Mode|Description|
|---|---|
|Disabled|Do not use Variant payload prevention (default).|
|Detect|Detect in-memory attacks, but take no further<br>action on the endpoint. With this mode, you can<br>use collected data about suspicious processes for<br>investigation and hunting.|
|Prevent|Prevent in-memory attacks.|



