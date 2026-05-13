You then see these detections as **Suspicious events** and **XDR**


**MalOps** . You can analyze these events and MalOps to see items

that require your attention.


In addition, the platform's detection and correlation engine,
identity management service, and threat classification service


enrich events with identity and additional security context data.

For example, when you view XDR data, you can view enrichment


information related to the user accounts and identities associated

with the MalOp. You can also see security enrichment with the


MITRE ATT&CK tactics, techniques, and sub-techniques for an

event, both for malicious and non-malicious activities. For details


[on the MITRE ATT&CK matrix, see MITRE ATT&CK Knowledge](https://attack.mitre.org/wiki/Main_Page)

[Base (https://attack.mitre.org/wiki/Main_Page).](https://attack.mitre.org/wiki/Main_Page)


The full integration process involves steps on the Cybereason

XDR side and the integrated platform side:






|Area|Description|
|---|---|
|Cybereason<br>XDR|You add and confgure Cybereason XDR<br>integrations in the**Cybereason Connect**<br>screen. If the integration sends log sources<br>through a cloud feed, you can confgure the<br>connection to the other platform directly in the<br>**Connect** screen. For integrations that do not<br>use a cloud feed, such as frewalls, you install<br>an on-site collector agent that collects the logs<br>and securely forwards these logs to<br>Cybereason XDR.<br>For details on how to use the Cybereason<br>Connect screen, see Use Cybereason Connect<br>(/s/knowledge-base?article=24-1-use-<br>cybereason-connect&language=en_US#use-<br>cybereason-connect). For details on how to<br>how to install an on-site collector, see Add an<br>On-Site Integration (/s/knowledge-base?<br>article=24-1-add-an-on-site-<br>integration&language=en_US#add-an-on-site-<br>integration).|
|Integrated<br>platform|You also enable log forwarding in each<br>integrated platform. The steps to enable this<br>log forwarding differ depending on the<br>integrated platform. For details on how to<br>confgure these exports, select your<br>integrations from the Cybereason Integrations<br>(/s/integrations) page and select the**Confgure**<br>tab from the integration documentation page.|


Once you add and configure the integration, the Cybereason


platform, through your Google Chronicle instance, retrieves the

log sources from other platforms.


For a full, up-to-date list of the available integrations and the
required information and configuration for each integration, see


the Cybereason Connect screen in your Cybereason environment

[or the Cybereason Integrations (/s/integrations) page.](https://nest.cybereason.com/s/integrations)



