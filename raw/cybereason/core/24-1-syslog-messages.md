|Message<br>part|Details|
|---|---|
|**Syslog**<br>**prefx**|The syslog prefx contains a timestamp, the IPv4<br>address or host name of the system that sends<br>the event, and the name of the component that<br>writes the message.<br>**Example:**<br>`<134>Sep 30 09:26:20 server-`<br>`detection01 syslogLogger`<br>`CEF:0|Cybereason|Cybereason||`<br>`Malop|Malop`<br>`Created|10|cs1Label=malopId`|


|Message<br>part|Details|
|---|---|
|**CEF**<br>**header**|The CEF header is a pipe delimited (|) set of<br>values identifying the following:<br>CEF version<br>Vendor<br>Product<br>Product version<br>Event class (/s/knowledge-base?article=24-<br>1-syslog-messages-events-and-<br>severity&language=en_US#event-classes)<br>Event name (/s/knowledge-base?article=24-<br>1-syslog-messages-events-and-<br>severity&language=en_US#event-names)<br>Severity (/s/knowledge-base?article=24-1-<br>syslog-messages-events-and-<br>severity&language=en_US#severity)<br>**Example:**<br>`CEF:0|Cybereason|Cybereason|2`<br>`3.2|Malop|Malop Created|10|`|
|**Extension**<br>**felds**|The Extension felds (/s/knowledge-base?<br>article=24-1-syslog-messages-extension-<br>felds&language=en_US#syslog-messages-<br>extension-felds) contain predefned and custom<br>felds, logged as key-value pairs.|



[For details on the events connected in the CEF header, see Syslog](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-events-and-severity&language=en_US#syslog-messages-events-and-severity)


[Messages - Events and Severity (/s/knowledge-base?article=24-1-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-events-and-severity&language=en_US#syslog-messages-events-and-severity)

[syslog-messages-events-and-severity&language=en_US#syslog-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-events-and-severity&language=en_US#syslog-messages-events-and-severity)


[messages-events-and-severity).](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-events-and-severity&language=en_US#syslog-messages-events-and-severity)


[For details on the syslog extension fields, see Syslog Messages -](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)


[Extension Fields (/s/knowledge-base?article=24-1-syslog-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)
[messages-extension-fields&language=en_US#syslog-messages-](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)


[extension-fields).](https://nest.cybereason.com/s/knowledge-base?article=24-1-syslog-messages-extension-fields&language=en_US#syslog-messages-extension-fields)



