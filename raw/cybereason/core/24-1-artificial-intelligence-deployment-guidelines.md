with high and medium confidence levels, but does not prevent


detected malware from executing.


During this phase, review the Endpoint Protection MalOps in the


**Malops management** screen, and mark to exclude any false

positives.


Continue to Phase 2 when the following conditions are met:


The feature is deployed for 7 days.


A majority of endpoints have the feature enabled for at least 2

days.


You have analyzed all Endpoint Protection MalOps.

You have marked to exclude all false positives.


There are no new false positives in the last 24 hours.

## Phase 2: Steady state


Set the Artificial Intelligence modes as follows:


**Detect mode:** Moderate

**Prevent mode:** Moderate


In this phase, Cybereason prevents the execution of unknown
malware detected with high and medium level of confidence. If


you are satisfied with the system behavior, you can remain on

these settings.

## Phase 3 (Optional): Aggressive detection


You may want to take a more aggressive strategy for detecting
malware. If so, set the Artificial Intelligence modes as follows:


**Detect mode:** Aggressive

**Prevent mode:** Moderate


In this state, Artificial Intelligence prevents the execution of
unknown malware that with high or medium levels of confidence,


and detects (but does not prevent) unknown malware that was
detected with low confidence. Users will likely experience a higher


number of Endpoint Protection MalOps.

## Expand your deployment


After you reach a Steady state (Phase 2), you can expand your


deployment of Artificial Intelligence to additional endpoints in your

organization.


Expand your deployment in one of two ways:


|Deployment|Description|
|---|---|
|Expand<br>deployment in<br>steady state|In cases where the expanded deployment<br>is expected to have the same type of<br>machines and user profles, Cybereason<br>recommends keeping the steady state<br>settings, expand the deployment to new<br>machines, and analyze new fndings.|
|Expand<br>deployment<br>while disabling<br>prevention|If the expanded deployment includes a<br>new network or a network with very<br>different characteristics of machines and/or<br>users, Cybereason recommends that you<br>restart the deployment from the initial<br>phase (Phase 1) and continue as<br>described in this guide.|





