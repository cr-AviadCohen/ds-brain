# FILTERS.docx

1. If product type =(Secure Web Gateway or IDS/IPS) AND the correlation includes the same tactic and all the events tagtype is EVIDENCE.([furukawa](https://docs.google.com/document/d/1W0S9nGgXbSuZ2BVQerzR9c2J5noU8soLLtKhO41nSHI/edit?tab=t.0))

MALOP WORTHY TODAY

| worthy criteria | conditions |  |
| --- | --- | --- |
| has-high-event | at least one event with [original\_threat\_score >= 90 & event.dataSourceCategory NOT IN ('IDS/IPS'; 'Secure web gateway') & SUSPICION] | active |
| has-MEDIUMish-event | at least one event with [original\_threat\_score (X >= 55) & event.dataSourceCategory NOT IN ('IDS/IPS'; 'Secure web gateway') & SUSPICION] & step\_category!='account-takeover' | active |
| ato-MEDIUMish-multi-alerts | at least one event with [original\_threat\_score (X >= 55) & step\_category='account-takeover' & SUSPICION] & unique\_suspicious\_names>1 | active |
| over-x-LOWish-events | at least (N >= 10) events with [original\_threat\_score (Y >= 20) & event.dataSourceCategory NOT IN ('IDS/IPS'; 'Secure web gateway')] & [step\_category!='account-takeover' & at least one SUSPICION] | active |
| over-x-events | at least (M >= 50) events with [event.dataSourceCategory NOT IN ('IDS/IPS'; 'Secure web gateway')] & at least one SUSPICION | active |
| multi-step-malop | step name>1 | active |
| network-multi-alerts | at least (N >= 50) events with [event.dataSourceCategory IN ('IDS/IPS'; 'Secure web gateway')] & [at least one SUSPICION & unique\_suspicious\_names > 1 | active |
| over-x-victims | at least one SUSPICION & (victims.ipAddress.address>=5 OR victims.emailAddress.email>=14 OR victims.user.username>=5 OR victims.machine.computerName>=5 | active |
| ato-suspect-performer | at least one suspect of step\_category='account-takeover' that have suspicious performer (no\_events\_for\_ip OR always\_fail | research |
| ato-important-user | at least one event of step\_category='account-takeover' that have victim.user important (in vip list) | research |
