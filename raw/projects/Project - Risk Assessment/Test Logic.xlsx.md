# Test Logic.xlsx

## mapping cases
| Engine Rule Type | event type |
| --- | --- |
| Sigma | BepEvent |
| NaN | AntiStealerEvent |
| Yara | VspEvent |
| NaN | SecretScannerEvent |
| NaN | VppEvent |
| NaN | VfpEvent |
| Mlav | MlavEvent |
| Cloud Av | CloudAvEvent |
| Regular | PRPEventRansomware |
| NaN | PRPEventMBR |
| NaN | PRPEventShadows |
| NaN | PRPEventEncryption |
| NaN | PRPEventRestore |
| NaN | SelfProtectRegEvent |
| NaN | SelfProtectProcessEvent |
| NaN | SelfProtectServiceEvent |
| NaN | SelfProtectThreadEvent |
| NaN | SelfProtectFileEvent |
| NaN | AppControlUnsignedEvent |
| NaN | AppControlCategoryEvent |
| NaN | AppControlCompilerEvent |
| NaN | FilelessEvent |
| NaN | ShellcodeDetectionEvent |
| NaN | ProcessIntegrityEvent |
| NaN | ClassicInjectionEvent |

## Cloud Av
| Unnamed: 0 | score | is\_by\_hash | malware\_family\_name | edge | json example |
| --- | --- | --- | --- | --- | --- |
| CloudAvEvent | -1 | False | wiper | NaN | NaN |
| NaN | NaN | NaN | stealer | NaN | NaN |
| NaN | NaN | NaN | ransomware | NaN | NaN |
| NaN | NaN | NaN | unkown family | NaN | NaN |
| NaN | NaN | NaN | none | NaN | NaN |
| NaN | else | True | wiper | min: score=threshold | NaN |
| NaN | NaN | NaN | NaN | max:score=1 | NaN |
| NaN | NaN | NaN | stealer | min: score=threshold | NaN |
| NaN | NaN | NaN | NaN | max:score=1 | NaN |
| NaN | NaN | NaN | ransomware | min: score=threshold | NaN |
| NaN | NaN | NaN | NaN | max:score=1 | NaN |
| NaN | NaN | NaN | unkown family | min: score=threshold | NaN |
| NaN | NaN | NaN | NaN | max:score=1 | NaN |
| NaN | NaN | NaN | none | min: score=threshold | NaN |
| NaN | NaN | NaN | NaN | max:score=1 | NaN |
| NaN | NaN | False | wiper | min:similarity score=81 | NaN |
| NaN | NaN | NaN | NaN | max:similarity score=0 | NaN |
| NaN | NaN | NaN | stealer | min:similarity score=81 | NaN |
| NaN | NaN | NaN | NaN | max:similarity score=0 | NaN |
| NaN | NaN | NaN | ransomware | min:similarity score=81 | NaN |
| NaN | NaN | NaN | NaN | max:similarity score=0 | NaN |
| NaN | NaN | NaN | unkown family | min:similarity score=81 | NaN |
| NaN | NaN | NaN | NaN | max:similarity score=0 | NaN |
| NaN | NaN | NaN | none | min:similarity score=81 | NaN |
| NaN | NaN | NaN | NaN | max:similarity score=0 | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN |
| edge=true | NaN | NaN | NaN | NaN | NaN |
| min | score-threshold=0 | score=threshold | NaN | NaN | NaN |
| max | score-threshold=1-threshold | NaN | NaN | NaN | NaN |
| edge=false | NaN | NaN | NaN | NaN | NaN |
| max | similarity score (differnce)=0.0001 | NaN | NaN | NaN | NaN |
| min | similarity score =81 | NaN | NaN | NaN | NaN |

## Mlav
| Unnamed: 0 | is\_blocklisted | edge | json example from observe | score | same json diffrent parameters | score |
| --- | --- | --- | --- | --- | --- | --- |
| MlavEvent | True | max: mlav\_score=1 | {"detections":[{"indicator\_type":"File","is\_block\_listed":true,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.977876","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083344111,"trigger":"IdleScan","type":1,"uuid":"e99197bd-c410-48cd-8d09-438ab4a2dbf7"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"kernel32.dll"},{"module\_type":"ImportedModules","name":"user32.dll"},{"module\_type":"ImportedModules","name":"advapi32.dll"},{"module\_type":"ImportedModules","name":"oleaut32.dll"},{"module\_type":"ImportedModules","name":"kernel32.dll"},{"module\_type":"ImportedModules","name":"advapi32.dll"},{"module\_type":"ImportedModules","name":"kernel32.dll"},{"module\_type":"ImportedModules","name":"gdi32.dll"},{"module\_type":"ImportedModules","name":"user32.dll"},{"module\_type":"ImportedModules","name":"kernel32.dll"},{"module\_type":"ImportedModules","name":"oleaut32.dll"},{"module\_type":"ImportedModules","name":"shell32.dll"},{"module\_type":"ImportedModules","name":"wininet.dll"}],"file":{"entropy":"0.888063","is\_pe\_file":true,"name":"vipasana1.bin","path":"c:\\rw\\rwtools\\tools\\samples\\samples\_full\\vipasana1.bin","reputation":"Malicious","sha1":"3a0b855dd052b2cdc6453f6cbdb858c7b55762b0","sha256":"0442cfabb3212644c4b894a7e4a7e84c00fd23489cc4f96490f9988e6074b6ab","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.2 | {"detections":[{"indicator\_type":"File","is\_block\_listed":true,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.997217","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083414593,"trigger":"IdleScan","type":1,"uuid":"13c75ab3-3264-47f5-92f3-ae12acf829c4"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"KERNEL32.dll"},{"module\_type":"ImportedModules","name":"ADVAPI32.dll"},{"module\_type":"ImportedModules","name":"SHELL32.dll"},{"module\_type":"ImportedModules","name":"CRYPT32.dll"},{"module\_type":"ImportedModules","name":"IPHLPAPI.DLL"},{"module\_type":"ImportedModules","name":"WS2\_32.dll"}],"file":{"entropy":"0.789150","is\_pe\_file":true,"name":"lorenze.bin","path":"n","reputation":"Malicious","sha1":"a4b41efc63460f980130b67eb33c0bd061206744","sha256":"a0ccb9019b90716c8ee1bc0829e0e04cf7166be2f25987abbc8987e65cef2e6f","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.290019 |
| NaN | NaN | min: mlav\_score=threshold | {"detections":[{"indicator\_type":"File","is\_block\_listed":true,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.891817","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083332009,"trigger":"IdleScan","type":1,"uuid":"19b3b665-bac1-4d94-a8c6-d4427c62f9a8"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"user32.dll"},{"module\_type":"ImportedModules","name":"oleaut32.dll"},{"module\_type":"ImportedModules","name":"kernel32.dll"},{"module\_type":"ImportedModules","name":"MSVBVM60.DLL"}],"file":{"company\_name":"Damo Inc","entropy":"0.793293","internal\_name":"QuantumQuditSimulator","is\_pe\_file":true,"name":"mountlocker.bin","original\_name":"QuantumQuditSimulator.exe","path":"c:\\rw\\rwtools\\tools\\samples\\samples\_full\\mountlocker.bin","product\_name":"Quantum Qudit Simulator","product\_version":"1.0.0.42","reputation":"Malicious","sha1":"f9eb40f6d3d4c83852e3781886db762bef8564e0","sha256":"e7c277aae66085f1e0c4789fe51cac50e3ea86d79c8a242ffc066ed0b0548037","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.2 | {"detections":[{"indicator\_type":"File","is\_block\_listed":true,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.877217","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083414593,"trigger":"IdleScan","type":1,"uuid":"13c75ab3-3264-47f5-92f3-ae12acf829c4"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"KERNEL32.dll"},{"module\_type":"ImportedModules","name":"ADVAPI32.dll"},{"module\_type":"ImportedModules","name":"SHELL32.dll"},{"module\_type":"ImportedModules","name":"CRYPT32.dll"},{"module\_type":"ImportedModules","name":"IPHLPAPI.DLL"},{"module\_type":"ImportedModules","name":"WS2\_32.dll"}],"file":{"entropy":"0.789150","is\_pe\_file":true,"name":"lorenze.bin","path":"n","reputation":"Malicious","sha1":"a4b41efc63460f980130b67eb33c0bd061206744","sha256":"a0ccb9019b90716c8ee1bc0829e0e04cf7166be2f25987abbc8987e65cef2e6f","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.204579 |
| NaN | False | max: mlav\_score=1 | {"detections":[{"indicator\_type":"File","is\_block\_listed":false,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.999975","threshold":"0.986000"}],"metadata":{"action":2,"action\_details":"Block","description":"Malicious File Was Blocked","event\_type":"MlavEvent","timestamp":1741106044500,"trigger":"IdleScan","type":1,"uuid":"c268451d-24c8-4afa-9cf1-c63168847ca3"},"target":{"asset":{"agent\_version":"26.1.21.1","domain":"bb-winsrv2022","ip\_address":"172.46.20.75","mac\_address":"00:50:56:A2:01:08","name":"BB-WINSRV2022","os\_name":"WIN SERVER 2022","os\_type":"Windows","os\_version":"10.0.20348","sensor\_id":"3051758c-b8b4-4bb8-8d2d-4057d3fb411e","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"mscoree.dll"}],"file":{"entropy":"0.974314","is\_pe\_file":true,"name":"c9bb2a5da881b05074d7af899fb359ba899cf5503d696729d27a518b6914223d","path":"c:\\00\_malicious\_files\\dotnet\_dll\_moderate\\c9bb2a5da881b05074d7af899fb359ba899cf5503d696729d27a518b6914223d","sha1":"228609616ee1fe12d9ffeacdcd7a0cdcbecf854f","sha256":"c9bb2a5da881b05074d7af899fb359ba899cf5503d696729d27a518b6914223d","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: , Header Classification: MANAGED\_DLL, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.7 | {"detections":[{"indicator\_type":"File","is\_block\_listed":false,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.997217","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083414593,"trigger":"IdleScan","type":1,"uuid":"13c75ab3-3264-47f5-92f3-ae12acf829c4"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"KERNEL32.dll"},{"module\_type":"ImportedModules","name":"ADVAPI32.dll"},{"module\_type":"ImportedModules","name":"SHELL32.dll"},{"module\_type":"ImportedModules","name":"CRYPT32.dll"},{"module\_type":"ImportedModules","name":"IPHLPAPI.DLL"},{"module\_type":"ImportedModules","name":"WS2\_32.dll"}],"file":{"entropy":"0.789150","is\_pe\_file":true,"name":"lorenze.bin","path":"n","reputation":"Malicious","sha1":"a4b41efc63460f980130b67eb33c0bd061206744","sha256":"a0ccb9019b90716c8ee1bc0829e0e04cf7166be2f25987abbc8987e65cef2e6f","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.210019 |
| NaN | NaN | min: mlav\_score=threshold | {"detections":[{"indicator\_type":"File","is\_block\_listed":false,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.887217","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083414593,"trigger":"IdleScan","type":1,"uuid":"13c75ab3-3264-47f5-92f3-ae12acf829c4"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"KERNEL32.dll"},{"module\_type":"ImportedModules","name":"ADVAPI32.dll"},{"module\_type":"ImportedModules","name":"SHELL32.dll"},{"module\_type":"ImportedModules","name":"CRYPT32.dll"},{"module\_type":"ImportedModules","name":"IPHLPAPI.DLL"},{"module\_type":"ImportedModules","name":"WS2\_32.dll"}],"file":{"entropy":"0.789150","is\_pe\_file":true,"name":"lorenze.bin","path":"c:\\rwsamples\\autosamples\\lorenze.bin","reputation":"Malicious","sha1":"a4b41efc63460f980130b67eb33c0bd061206744","sha256":"a0ccb9019b90716c8ee1bc0829e0e04cf7166be2f25987abbc8987e65cef2e6f","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.2 | {"detections":[{"indicator\_type":"File","is\_block\_listed":false,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.877217","threshold":"0.870000"}],"metadata":{"action":0,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741083414593,"trigger":"IdleScan","type":1,"uuid":"13c75ab3-3264-47f5-92f3-ae12acf829c4"},"target":{"asset":{"agent\_version":"26.1.20.1","domain":"desktop-7gb1376","ip\_address":"10.0.2.15","mac\_address":"08:00:27:66:AC:46","name":"DESKTOP-7GB1376","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"c942576a-4039-429f-adcc-cd37bb9fc582","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"KERNEL32.dll"},{"module\_type":"ImportedModules","name":"ADVAPI32.dll"},{"module\_type":"ImportedModules","name":"SHELL32.dll"},{"module\_type":"ImportedModules","name":"CRYPT32.dll"},{"module\_type":"ImportedModules","name":"IPHLPAPI.DLL"},{"module\_type":"ImportedModules","name":"WS2\_32.dll"}],"file":{"entropy":"0.789150","is\_pe\_file":true,"name":"lorenze.bin","path":"n","reputation":"Malicious","sha1":"a4b41efc63460f980130b67eb33c0bd061206744","sha256":"a0ccb9019b90716c8ee1bc0829e0e04cf7166be2f25987abbc8987e65cef2e6f","signature\_info":{"is\_signature\_verified":false,"is\_signed":false,"is\_verif\_fail":true,"reason\_verify\_fail":"no\_signature"},"type":"Extension Classification: .bin, Header Classification: UNMANAGED\_EXE, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | 8.124579 |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| {"detections":[{"indicator\_type":"File","is\_block\_listed":true,"method":"ML","name":"MLAV detection","rule":{"version":"0.000000"},"score":"0.299208","threshold":"0.986000"}],"metadata":{"action":4,"action\_details":"Report","description":"Malicious File Was Reported","event\_type":"MlavEvent","timestamp":1741121701965,"trigger":"IdleScan","type":1,"uuid":"203dc635-87a5-440c-b8fe-a526dadd2c36"},"target":{"asset":{"agent\_version":"99.26.279.1","domain":"sensor001","ip\_address":"172.46.6.150","mac\_address":"00:50:56:A2:05:9D","name":"SENSOR001","os\_name":"WIN 10 22H2","os\_type":"Windows","os\_version":"10.0.19045","sensor\_id":"N/A","type":"HOST"},"process":{"external\_modules":[{"module\_type":"ImportedModules","name":"mscoree.dll"}],"file":{"company\_name":"Newtonsoft","creation\_time":1615742212438,"entropy":"0.741113","internal\_name":"Newtonsoft.Json.dll","is\_pe\_file":true,"modification\_time":1612869300000,"name":"Newtonsoft.Json.dll","original\_name":"Newtonsoft.Json.dll","path":"C:\\Program Files\\Git\\mingw64\\libexec\\git-core\\Newtonsoft.Json.dll","product\_name":"Json.NET","product\_version":"12.0.3+7c3d7f8da7e35dde8fa74188b0decff70f8f10e3","sha1":"1248142eb45eed3beb0d9a2d3b8bed5fe2569b10","sha256":"7f912b28a07c226e0be3acfb2f57f050538aba0100fa1f0bf2c39f1a1f1da814","signature\_info":{"is\_signature\_verified":true,"is\_signed":true,"is\_verif\_fail":false,"reason\_verify\_fail":"signed\_and\_verified","signer":"Json.NET (.NET Foundation)"},"size":700336,"type":"Extension Classification: .dll, Header Classification: MANAGED\_DLL, AI Classification [Details]: label: pebin, Score: 1, Is Text: false"}}}} | score =-2 | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| observe query: | make\_col event\_type:string(FIELDS.metadata.event\_type)\nfilter event\_type != "NetworkConnection: NoSubType"\nfilter event\_type = "MlavEvent"\nmake\_col score:string(FIELDS.detections[0].score)\nmake\_col threshold:string(FIELDS.detections[0].threshold)\nmake\_col is\_block\_listed:bool(FIELDS.detections[0].is\_block\_listed)\nfilter is\_block\_listed = false | NaN | NaN | NaN | NaN | NaN |

## Yara
| cases: | edge | 1 detection | more then 1 detection |
| --- | --- | --- | --- |
| VspEvent | min: score=trheshold | NaN | NaN |
| NaN | max: score=100 | NaN | NaN |
| SecretScannerEvent | min: score=trheshold | NaN | NaN |
| NaN | max: score=100 | NaN | NaN |
| VppEvent | min: score=trheshold | NaN | NaN |
| NaN | max: score=100 | NaN | NaN |
| VfpEvent | min: score=trheshold | NaN | NaN |
| NaN | max: score=100 | NaN | NaN |
| NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN |
| edge | NaN | NaN | NaN |
| max | detection.score=100 | NaN | NaN |
| min | detection.score=threshold | NaN | NaN |

## Sigma
| cases: | 1 detection |
| --- | --- |
| BepEvent | NaN |
| AntiStealerEvent | NaN |

## additions
| action | permission | asset | integrity |
| --- | --- | --- | --- |
| 0 | NaN | HOST | LOW |
| 1 | NaN | VIRTUAL\_MACHINE | MEDIUM |
| 2 | NaN | MOBILE | HIGH |
| 3 | NaN | IOT | PROTECTED |
| 4 | NaN | UNKNOWN | SYSTEM |
| 5 | NaN | NaN | UNKNOWN |
| 6 | NaN | NaN | UNTRUSTED |
| 7 | NaN | NaN | NaN |
