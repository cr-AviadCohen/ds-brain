# UEBA - AD Examples.xlsx

## HBOS Example
| Unnamed: 0 | Unnamed: 1 | Unnamed: 2 | Unnamed: 3 | Unnamed: 4 | Unnamed: 5 | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Unnamed: 9 | Unnamed: 10 | Unnamed: 11 | HBOS | Unnamed: 13 | Unnamed: 14 | Unnamed: 15 | Unnamed: 16 | Unnamed: 17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| User ID | Timestamp | Day | Week | Data1 | Data2 | Data3 | ... | DataN | Dataset | NaN | NaN | Item | Probablity | Probability Score | Anomaly Score | NaN | Histogram-Based Anomaly Score |
| 1 | NaN | 1 | 1 | A | NaN | NaN | NaN | NaN | train | NaN | NaN | A | 0.4 | 1 | 0 | NaN | NaN |
| 1 | NaN | 2 | 1 | A | NaN | NaN | NaN | NaN | train | NaN | NaN | B | 0.3 | 0.75 | 0.124939 | NaN | NaN |
| 1 | NaN | 3 | 1 | A | NaN | NaN | NaN | NaN | train | NaN | NaN | C | 0.2 | 0.5 | 0.30103 | NaN | NaN |
| 1 | NaN | 4 | 1 | A | NaN | NaN | NaN | NaN | train | NaN | NaN | D | 0.1 | 0.25 | 0.60206 | NaN | NaN |
| 1 | NaN | 5 | 1 | B | NaN | NaN | NaN | NaN | train | NaN | NaN | NaN | NaN | 0.001 | NaN | NaN | NaN |
| 1 | NaN | 6 | 1 | B | NaN | NaN | NaN | NaN | train | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 7 | 1 | B | NaN | NaN | NaN | NaN | train | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 8 | 1 | C | NaN | NaN | NaN | NaN | train | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 9 | 1 | C | NaN | NaN | NaN | NaN | train | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 10 | 1 | D | NaN | NaN | NaN | NaN | train | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 8 | 2 | A | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 9 | 2 | A | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 10 | 2 | A | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 11 | 2 | B | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 12 | 2 | B | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 13 | 2 | D | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| 1 | NaN | 14 | 2 | E | NaN | NaN | NaN | NaN | test | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | Number of different IPs connected in time range | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | NaN | Day 1 | Day2 | Day3 | ... | ... | ... | Day7 | Avg | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 00:00-04:00: | 4 | 2 | NaN | ... | ... | ... | 2 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 04:00-08:00: | 8 | 7 | NaN | ... | ... | ... | 7 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 08:00-12:00: | 0 | 0 | NaN | ... | ... | ... | 0 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 12:00-16:00: | 0 | 0 | NaN | ... | ... | ... | 0 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 16:00-20:00: | 8 | 7 | NaN | ... | ... | ... | 7 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |
| NaN | NaN | 20:00-24:00: | 16 | 20 | NaN | ... | ... | ... | 20 | NaN | NaN | NaN | NaN | NaN | NaN | NaN | NaN |

## Sheet1
| about | 1-item list, with the following structure. notice that each key is a different item in a list, some of them might be None (i.e. no key-value) | [{'labels': [{'key': 'Category', 'value': 'Logon'},    {'key': 'Channel', 'value': 'Security'},    {'key': 'Opcode', 'value': 'Info'},    {'key': 'ImpersonationLevel', 'value': 'Impersonation'},    {'key': 'RestrictedAdminMode', 'value': '-'}]}] |
| --- | --- | --- |
| extensions.auth.mechanism | I saw | ['MECHANISM\_UNSPECIFIED', 'NETWORK', 'SERVICE'] |
| extensions.auth.details | PROBABLY directly correlates (i.e. ordinal encoder) to extensions.auth.mechanism | [NaN, '3', '5'] |
| intermediary | All are the same, from what I saw | [{'application': 'im\_msvistalog', 'ip': [{}]}]\t |
| meta.event\_hash | NaN | NaN |
| meta.event\_type | relevant, superset of meta.product.event\_type (e.g. USER\_LOGOUT is 4634; GENERIC\_EVENT is 4776, 4769, 5136....) | array(['GENERIC\_EVENT', 'USER\_LOGIN', 'USER\_LOGOUT',  'USER\_RESOURCE\_ACCESS', 'GROUP\_UNCATEGORIZED',  'REGISTRY\_UNCATEGORIZED', 'FILE\_OPEN'], dtype=object) |
| meta.product.deployment\_id | NaN | NaN |
| meta.product.event\_type | relevant, subset of meta.event\_type | array(['4769', '4776', '4624', '4768', '4634', '4672', '4662', '4648',  '4627', '5136', '4770', '4799', '4663', '4933', '4932', '4670',  '4771', '4674'], dtype=object) |
| meta.product.log\_id | NaN | NaN |
| meta.product.name | NaN | NaN |
| meta.product.product\_category | NaN | NaN |
| meta.timestamp.event | NaN | NaN |
| meta.vendor.name | NaN | NaN |
| principal.application | doesn't look informative | array(['BIZP2018$', nan, 'Kerberos', 'NTLM', |
| principal.ip | 1 item list of ip address and port | [{'address': '172.19.30.155', 'port': 62067}] |
| principal.primary\_ip | the ip address | 172.19.30.155 |
| principal.process.pid | not sure what is it, but looks like relevant to entity | NaN |
| principal.resource.labels | All are the same, from what I saw | [None] |
| principal.user.attribute.roles | All are the same, from what I saw | [{}] |
| principal.hostname | look like small variance but not unique variable, however not sure it'll be an important one, needs further empirical results | NaN |
| principal.user.display\_name | non informative for model itself, may be used to complete missing data (user.id if it's omitted for some reason) | NaN |
| principal.user.logon.linked\_id | seems as non informative UNLESS DOMAIN experty would explain otherwise | NaN |
| principal.user.windows\_sid | I don't understand it, but it looks like a great feature: nunique      38, count      4844 | array([nan, 'S-1-0-0', 'S-1-5-21-644443905-3601805816-3363717870-500',  'S-1-5-21-9122744-565515841-12547700-145755',  'S-1-5-21-9122744-565515841-12547700-140888', |
| principal.administrative\_domain | same here | array([nan, 'TEIJIN-FRONTIER', 'JUROKU', 'JRCTOKKI', 'HEC',  'NT AUTHORITY', 'KFAD'] |
| principal.user.id | ENTITY KEY IDENTIFIER | NaN |
| principal.process.access\_mask | I don't understand it, but it looks like an optional feature: nunique      7, count      236 | array([nan, '0x0', '0x100', '0x8', '0x2', '0x20', '0x10', '16777216'], |
| principal.process.command\_line | same here | array([nan, 'C:\\Windows\\System32\\lsass.exe',  'C:\\Windows\\System32\\svchost.exe',  'C:\\Windows\\System32\\services.exe',  'C:\\Program Files\\Cybereason ActiveProbe\\minionhost.exe'], |
| principal.process.file.path | redundant to principal.process.command\_line | NaN |
| result.action\_details | non informative; correlates with result.actions | AUDIT\_SUCCESS 9995 AUDIT\_FAILURE 5 |
| result.actions | non informative; correlates with result.action\_details | [ALLOW] 9995 [BLOCK] 5 |
| result.description | non infromative | ['0x0 - No error', nan,  '0x18 - Pre-authentication information was invalid'] |
| result.detection\_fields | might be used, needs parsing << e.g. xdm[col].explode().dropna().apply(pd.Series).pivot(columns="key").droplevel(0, axis=1) | [None,  None,  None,  {'key': 'TicketEncryptionType', 'value': '0x12'},  {'key': 'TicketOptions', 'value': '0x40810000'},  None] |
| result.rule.id | doesn't look informative | [nan, '-', '%%7688\r\n\t\t\t\t', '%%4435\r\n\t\t\t\t',  '%%5649\r\n\t\t\t\t', '%%7685\r\n\t\t\t\t', '%%4484\r\n\t\t\t\t'] |
| target.administrative\_domain | doesn't look informative | ['HEC.LOCAL', nan, 'HEC', 'KB-BS', 'KB-BS.LOCAL', 'TEIJIN-FRONTIER',  'TEIJIN-FRONTIER.COM', 'FREIA.JUROKU.CO.JP', 'JUROKU', 'JRCTOKKI',  'JRCTOKKI.CO.JP', 'DIRECTRI', 'DIRECTRI.LOCAL', 'NT AUTHORITY',  'kb-bs.local', 'Builtin', 'TAIYO', 'TAIYOINK.COM',  'jrctokki.co.jp', 'juroku', 'KFAD', 'KFAD.KYOEIFOOD.CO.JP',  'hec.local', 'freia.juroku.co.jp'] |
| target.application | same as corresponding principal field | array(['BIZP2018$', nan, 'Kerberos', 'NTLM', |
| target.group.group\_display\_name | same as corresponding principal field | NaN |
| target.group.ip | non infromative | NaN |
| target.group.windows\_sid | I think that target.user.windows\_sid will be more informative | NaN |
| target.process.command\_line | not informative to user as entity, might be slightly informative otherwise: nunique     64 count      350 | ['BIZP2018$', nan, 'krbtgt', 'HECDC6$', 'HEG-N24-0200$',  'KUMI0007$', 'DCS-2SCM-004$', 'HECDC5$', 'ROOT-6$', 'ROOT-3$', |
| target.resource.attribute.labels | needs  parsing, doesn't look very informative | NaN |
| target.resource.name | doesn't look informative | array(['BIZP2018$@HEC.LOCAL', '0144326', '0141560', ..., 'AVD-386$', |
| target.user.attribute.labels | needs  parsing, doesn't look very informative | NaN |
| target.user.attribute.permissions | needs parsing, derived features seems highly correlated | e.g. xdm[col].apply(lambda x: x[0].get("name")).str.get\_dummies(sep="\r\n\t\t\t").corr() |
| target.user.display\_name | NaN | NaN |
| target.user.group\_identifiers | NaN | NaN |
| target.user.id | NaN | NaN |
| target.user.logon.guid | NaN | NaN |
| target.user.user\_account\_domain | NaN | NaN |
| target.hostname | NaN | NaN |
| target.process.file.path | NaN | NaN |
| target.user.logon.authentication\_package | NaN | NaN |
| target.user.logon.elevated\_token | NaN | NaN |
| target.user.logon.impersonation\_level | NaN | NaN |
| target.user.logon.linked\_id | NaN | NaN |
| target.user.logon.process\_name | NaN | NaN |
| target.user.logon.type | extensions.auth.details | NaN |
| target.user.logon.virtual\_account | NaN | NaN |
| target.user.windows\_sid | NaN | NaN |
| target.resource.product\_object\_id | NaN | NaN |
| target.file.path | NaN | NaN |
| target.resource.sub\_type | NaN | NaN |
| target.group.product\_object\_id | NaN | NaN |
| target.registry.key | NaN | NaN |
| target.file.name | NaN | NaN |
| vendor.Keywords | NaN | NaN |
| vendor.ServiceName | NaN | NaN |
| vendor.Status | NaN | NaN |
| vendor.Task | NaN | NaN |
| vendor.source\_type | NaN | NaN |
| vendor.AccessList | NaN | NaN |
| vendor.AccessMask | NaN | NaN |
| vendor.AdditionalInfo | NaN | NaN |
| vendor.OperationType | NaN | NaN |
| vendor.Properties | NaN | NaN |

## Ofer - Event Rate
|  | Rand() | Fixed\_Rand() | Event Trigger | Unnamed: 4 | ID\_between\_events | Unnamed: 6 | Unnamed: 7 | Unnamed: 8 | Param | Value | Unnamed: 11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0.397510 | 0.421711 | 0 | 0.000000e+00 | 1 | 0.000000 | 0.000000 | NaN | Rate | 0.10 | NaN |
| 2 | 0.464363 | 0.926939 | 0 | 0.000000e+00 | 2 | 0.000000 | 0.000000 | NaN | Alph: Weight of current event | 0.20 | NaN |
| 3 | 0.125036 | 0.787164 | 0 | 0.000000e+00 | 3 | 0.000000 | 0.000000 | NaN | Beta: Decay | 0.05 | NaN |
| 4 | 0.591267 | 0.002012 | 1 | 2.000000e-01 | 1 | 0.200000 | 0.010000 | NaN | NaN | NaN |  |
| 5 | 0.206142 | 0.615788 | 0 | 1.600000e-01 | 2 | 0.200000 | 0.019500 | NaN | 0.099 | NaN | NaN |
| 6 | 0.854886 | 0.269126 | 0 | 1.280000e-01 | 3 | 0.200000 | 0.028525 | NaN | NaN | NaN | NaN |
| 7 | 0.340316 | 0.997671 | 0 | 1.024000e-01 | 4 | 0.200000 | 0.037099 | NaN | NaN | NaN | NaN |
| 8 | 0.264250 | 0.086879 | 1 | 2.819200e-01 | 1 | 0.281920 | 0.049340 | NaN | NaN | NaN | NaN |
| 9 | 0.781699 | 0.598618 | 0 | 2.255360e-01 | 2 | 0.281920 | 0.060969 | NaN | NaN | NaN | NaN |
| 10 | 0.018549 | 0.654719 | 0 | 1.804288e-01 | 3 | 0.281920 | 0.072016 | NaN | NaN | NaN | NaN |
| 11 | 0.955734 | 0.757913 | 0 | 1.443430e-01 | 4 | 0.281920 | 0.082512 | NaN | NaN | NaN | NaN |
| 12 | 0.133719 | 0.262097 | 0 | 1.154744e-01 | 5 | 0.281920 | 0.092482 | NaN | NaN | NaN | NaN |
| 13 | 0.351222 | 0.564040 | 0 | 9.237955e-02 | 6 | 0.281920 | 0.101954 | NaN | NaN | NaN | NaN |
| 14 | 0.475593 | 0.920518 | 0 | 7.390364e-02 | 7 | 0.281920 | 0.110952 | NaN | NaN | NaN | NaN |
| 15 | 0.132945 | 0.196036 | 0 | 5.912291e-02 | 8 | 0.281920 | 0.119501 | NaN | NaN | NaN | NaN |
| 16 | 0.104794 | 0.459035 | 0 | 4.729833e-02 | 9 | 0.281920 | 0.127622 | NaN | NaN | NaN | NaN |
| 17 | 0.262365 | 0.694804 | 0 | 3.783866e-02 | 10 | 0.281920 | 0.135336 | NaN | NaN | NaN | NaN |
| 18 | 0.079313 | 0.603356 | 0 | 3.027093e-02 | 11 | 0.281920 | 0.142666 | NaN | NaN | NaN | NaN |
| 19 | 0.571903 | 0.888170 | 0 | 2.421674e-02 | 12 | 0.281920 | 0.149628 | NaN | NaN | NaN | NaN |
| 20 | 0.534905 | 0.335782 | 0 | 1.937339e-02 | 13 | 0.281920 | 0.156243 | NaN | NaN | NaN | NaN |
| 21 | 0.935736 | 0.092709 | 1 | 2.154987e-01 | 1 | 0.215499 | 0.159206 | NaN | NaN | NaN | NaN |
| 22 | 0.452464 | 0.456544 | 0 | 1.723990e-01 | 2 | 0.215499 | 0.162020 | NaN | NaN | NaN | NaN |
| 23 | 0.468576 | 0.377443 | 0 | 1.379192e-01 | 3 | 0.215499 | 0.164694 | NaN | NaN | NaN | NaN |
| 24 | 0.960017 | 0.136085 | 0 | 1.103353e-01 | 4 | 0.215499 | 0.167235 | NaN | NaN | NaN | NaN |
| 25 | 0.193426 | 0.037807 | 1 | 2.882683e-01 | 1 | 0.288268 | 0.173286 | NaN | NaN | NaN | NaN |
| 26 | 0.942551 | 0.902529 | 0 | 2.306146e-01 | 2 | 0.288268 | 0.179035 | NaN | NaN | NaN | NaN |
| 27 | 0.307888 | 0.696870 | 0 | 1.844917e-01 | 3 | 0.288268 | 0.184497 | NaN | NaN | NaN | NaN |
| 28 | 0.736424 | 0.879659 | 0 | 1.475934e-01 | 4 | 0.288268 | 0.189686 | NaN | NaN | NaN | NaN |
| 29 | 0.582269 | 0.344509 | 0 | 1.180747e-01 | 5 | 0.288268 | 0.194615 | NaN | NaN | NaN | NaN |
| 30 | 0.560519 | 0.749434 | 0 | 9.445975e-02 | 6 | 0.288268 | 0.199297 | NaN | NaN | NaN | NaN |
| 31 | 0.405880 | 0.129306 | 0 | 7.556780e-02 | 7 | 0.288268 | 0.203746 | NaN | NaN | NaN | NaN |
| 32 | 0.330690 | 0.321391 | 0 | 6.045424e-02 | 8 | 0.288268 | 0.207972 | NaN | NaN | NaN | NaN |
| 33 | 0.002795 | 0.833431 | 0 | 4.836339e-02 | 9 | 0.288268 | 0.211987 | NaN | NaN | NaN | NaN |
| 34 | 0.567542 | 0.351677 | 0 | 3.869071e-02 | 10 | 0.288268 | 0.215801 | NaN | NaN | NaN | NaN |
| 35 | 0.635557 | 0.454245 | 0 | 3.095257e-02 | 11 | 0.288268 | 0.219424 | NaN | NaN | NaN | NaN |
| 36 | 0.143632 | 0.360140 | 0 | 2.476206e-02 | 12 | 0.288268 | 0.222866 | NaN | NaN | NaN | NaN |
| 37 | 0.553437 | 0.970040 | 0 | 1.980964e-02 | 13 | 0.288268 | 0.226137 | NaN | NaN | NaN | NaN |
| 38 | 0.731054 | 0.278677 | 0 | 1.584772e-02 | 14 | 0.288268 | 0.229243 | NaN | NaN | NaN | NaN |
| 39 | 0.697665 | 0.229108 | 0 | 1.267817e-02 | 15 | 0.288268 | 0.232194 | NaN | NaN | NaN | NaN |
| 40 | 0.563800 | 0.352239 | 0 | 1.014254e-02 | 16 | 0.288268 | 0.234998 | NaN | NaN | NaN | NaN |
| 41 | 0.004462 | 0.534619 | 0 | 8.114031e-03 | 17 | 0.288268 | 0.237662 | NaN | NaN | NaN | NaN |
| 42 | 0.783879 | 0.470672 | 0 | 6.491224e-03 | 18 | 0.288268 | 0.240192 | NaN | NaN | NaN | NaN |
| 43 | 0.630636 | 0.231750 | 0 | 5.192980e-03 | 19 | 0.288268 | 0.242596 | NaN | NaN | NaN | NaN |
| 44 | 0.411756 | 0.090472 | 1 | 2.041544e-01 | 1 | 0.204154 | 0.240674 | NaN | NaN | NaN | NaN |
| 45 | 0.727212 | 0.782826 | 0 | 1.633235e-01 | 2 | 0.204154 | 0.238848 | NaN | NaN | NaN | NaN |
| 46 | 0.289238 | 0.806972 | 0 | 1.306588e-01 | 3 | 0.204154 | 0.237113 | NaN | NaN | NaN | NaN |
| 47 | 0.993206 | 0.051290 | 1 | 3.045270e-01 | 1 | 0.304527 | 0.240484 | NaN | NaN | NaN | NaN |
| 48 | 0.058489 | 0.046213 | 1 | 4.436216e-01 | 1 | 0.443622 | 0.250641 | NaN | NaN | NaN | NaN |
| 49 | 0.221631 | 0.932068 | 0 | 3.548973e-01 | 2 | 0.443622 | 0.260290 | NaN | NaN | NaN | NaN |
| 50 | 0.939621 | 0.989522 | 0 | 2.839178e-01 | 3 | 0.443622 | 0.269456 | NaN | NaN | NaN | NaN |
| 51 | 0.298723 | 0.955946 | 0 | 2.271343e-01 | 4 | 0.443622 | 0.278165 | NaN | NaN | NaN | NaN |
| 52 | 0.279663 | 0.840573 | 0 | 1.817074e-01 | 5 | 0.443622 | 0.286437 | NaN | NaN | NaN | NaN |
| 53 | 0.608687 | 0.966168 | 0 | 1.453659e-01 | 6 | 0.443622 | 0.294297 | NaN | NaN | NaN | NaN |
| 54 | 0.298956 | 0.653406 | 0 | 1.162928e-01 | 7 | 0.443622 | 0.301763 | NaN | NaN | NaN | NaN |
| 55 | 0.831894 | 0.589426 | 0 | 9.303420e-02 | 8 | 0.443622 | 0.308856 | NaN | NaN | NaN | NaN |
| 56 | 0.341922 | 0.809836 | 0 | 7.442736e-02 | 9 | 0.443622 | 0.315594 | NaN | NaN | NaN | NaN |
| 57 | 0.584179 | 0.689242 | 0 | 5.954189e-02 | 10 | 0.443622 | 0.321995 | NaN | NaN | NaN | NaN |
| 58 | 0.135199 | 0.656004 | 0 | 4.763351e-02 | 11 | 0.443622 | 0.328077 | NaN | NaN | NaN | NaN |
| 59 | 0.936771 | 0.751514 | 0 | 3.810681e-02 | 12 | 0.443622 | 0.333854 | NaN | NaN | NaN | NaN |
| 60 | 0.908339 | 0.961086 | 0 | 3.048545e-02 | 13 | 0.443622 | 0.339342 | NaN | NaN | NaN | NaN |
| 61 | 0.366552 | 0.679480 | 0 | 2.438836e-02 | 14 | 0.443622 | 0.344556 | NaN | NaN | NaN | NaN |
| 62 | 0.784413 | 0.567769 | 0 | 1.951069e-02 | 15 | 0.443622 | 0.349510 | NaN | NaN | NaN | NaN |
| 63 | 0.228988 | 0.503858 | 0 | 1.560855e-02 | 16 | 0.443622 | 0.354215 | NaN | NaN | NaN | NaN |
| 64 | 0.097129 | 0.575894 | 0 | 1.248684e-02 | 17 | 0.443622 | 0.358686 | NaN | NaN | NaN | NaN |
| 65 | 0.113725 | 0.294440 | 0 | 9.989471e-03 | 18 | 0.443622 | 0.362932 | NaN | NaN | NaN | NaN |
| 66 | 0.437609 | 0.490138 | 0 | 7.991577e-03 | 19 | 0.443622 | 0.366967 | NaN | NaN | NaN | NaN |
| 67 | 0.955804 | 0.108546 | 0 | 6.393262e-03 | 20 | 0.443622 | 0.370800 | NaN | NaN | NaN | NaN |
| 68 | 0.431096 | 0.213059 | 0 | 5.114609e-03 | 21 | 0.443622 | 0.374441 | NaN | NaN | NaN | NaN |
| 69 | 0.132576 | 0.161752 | 0 | 4.091687e-03 | 22 | 0.443622 | 0.377900 | NaN | NaN | NaN | NaN |
| 70 | 0.848047 | 0.459909 | 0 | 3.273350e-03 | 23 | 0.443622 | 0.381186 | NaN | NaN | NaN | NaN |
| 71 | 0.904248 | 0.854934 | 0 | 2.618680e-03 | 24 | 0.443622 | 0.384308 | NaN | NaN | NaN | NaN |
| 72 | 0.474835 | 0.885827 | 0 | 2.094944e-03 | 25 | 0.443622 | 0.387273 | NaN | NaN | NaN | NaN |
| 73 | 0.959596 | 0.652564 | 0 | 1.675955e-03 | 26 | 0.443622 | 0.390091 | NaN | NaN | NaN | NaN |
| 74 | 0.719421 | 0.864397 | 0 | 1.340764e-03 | 27 | 0.443622 | 0.392767 | NaN | NaN | NaN | NaN |
| 75 | 0.840664 | 0.659268 | 0 | 1.072611e-03 | 28 | 0.443622 | 0.395310 | NaN | NaN | NaN | NaN |
| 76 | 0.672537 | 0.744668 | 0 | 8.580890e-04 | 29 | 0.443622 | 0.397726 | NaN | NaN | NaN | NaN |
| 77 | 0.052376 | 0.679797 | 0 | 6.864712e-04 | 30 | 0.443622 | 0.400020 | NaN | NaN | NaN | NaN |
| 78 | 0.954266 | 0.488037 | 0 | 5.491770e-04 | 31 | 0.443622 | 0.402200 | NaN | NaN | NaN | NaN |
| 79 | 0.454237 | 0.432009 | 0 | 4.393416e-04 | 32 | 0.443622 | 0.404271 | NaN | NaN | NaN | NaN |
| 80 | 0.271320 | 0.683621 | 0 | 3.514733e-04 | 33 | 0.443622 | 0.406239 | NaN | NaN | NaN | NaN |
| 81 | 0.398960 | 0.789268 | 0 | 2.811786e-04 | 34 | 0.443622 | 0.408108 | NaN | NaN | NaN | NaN |
| 82 | 0.017137 | 0.038582 | 1 | 2.002249e-01 | 1 | 0.200225 | 0.397714 | NaN | NaN | NaN | NaN |
| 83 | 0.172558 | 0.599363 | 0 | 1.601800e-01 | 2 | 0.200225 | 0.387840 | NaN | NaN | NaN | NaN |
| 84 | 0.243319 | 0.906365 | 0 | 1.281440e-01 | 3 | 0.200225 | 0.378459 | NaN | NaN | NaN | NaN |
| 85 | 0.825735 | 0.918949 | 0 | 1.025152e-01 | 4 | 0.200225 | 0.369547 | NaN | NaN | NaN | NaN |
| 86 | 0.898559 | 0.259883 | 0 | 8.201214e-02 | 5 | 0.200225 | 0.361081 | NaN | NaN | NaN | NaN |
| 87 | 0.019065 | 0.838372 | 0 | 6.560971e-02 | 6 | 0.200225 | 0.353038 | NaN | NaN | NaN | NaN |
| 88 | 0.804345 | 0.637583 | 0 | 5.248777e-02 | 7 | 0.200225 | 0.345398 | NaN | NaN | NaN | NaN |
| 89 | 0.164411 | 0.390114 | 0 | 4.199021e-02 | 8 | 0.200225 | 0.338139 | NaN | NaN | NaN | NaN |
| 90 | 0.553426 | 0.028240 | 1 | 2.335922e-01 | 1 | 0.233592 | 0.332912 | NaN | NaN | NaN | NaN |
| 91 | 0.890198 | 0.039035 | 1 | 3.868737e-01 | 1 | 0.386874 | 0.335610 | NaN | NaN | NaN | NaN |
| 92 | 0.467743 | 0.845884 | 0 | 3.094990e-01 | 2 | 0.386874 | 0.338173 | NaN | NaN | NaN | NaN |
| 93 | 0.724777 | 0.663856 | 0 | 2.475992e-01 | 3 | 0.386874 | 0.340608 | NaN | NaN | NaN | NaN |
| 94 | 0.231493 | 0.150617 | 0 | 1.980794e-01 | 4 | 0.386874 | 0.342921 | NaN | NaN | NaN | NaN |
| 95 | 0.244361 | 0.742246 | 0 | 1.584635e-01 | 5 | 0.386874 | 0.345119 | NaN | NaN | NaN | NaN |
| 96 | 0.569154 | 0.056416 | 1 | 3.267708e-01 | 1 | 0.326771 | 0.344201 | NaN | NaN | NaN | NaN |
| 97 | 0.712298 | 0.147418 | 0 | 2.614166e-01 | 2 | 0.326771 | 0.343330 | NaN | NaN | NaN | NaN |
| 98 | 0.817776 | 0.935558 | 0 | 2.091333e-01 | 3 | 0.326771 | 0.342502 | NaN | NaN | NaN | NaN |
| 99 | 0.215301 | 0.818986 | 0 | 1.673066e-01 | 4 | 0.326771 | 0.341715 | NaN | NaN | NaN | NaN |
| 100 | 0.851189 | 0.074497 | 1 | 3.338453e-01 | 1 | 0.333845 | 0.341322 | NaN | NaN | NaN | NaN |
| 101 | 0.328263 | 0.867034 | 0 | 2.670763e-01 | 2 | 0.333845 | 0.340948 | NaN | NaN | NaN | NaN |
| 102 | 0.157145 | 0.991427 | 0 | 2.136610e-01 | 3 | 0.333845 | 0.340593 | NaN | NaN | NaN | NaN |
| 103 | 0.589254 | 0.954017 | 0 | 1.709288e-01 | 4 | 0.333845 | 0.340256 | NaN | NaN | NaN | NaN |
| 104 | 0.006615 | 0.716007 | 0 | 1.367430e-01 | 5 | 0.333845 | 0.339935 | NaN | NaN | NaN | NaN |
| 105 | 0.295059 | 0.137421 | 0 | 1.093944e-01 | 6 | 0.333845 | 0.339631 | NaN | NaN | NaN | NaN |
| 106 | 0.350076 | 0.121615 | 0 | 8.751555e-02 | 7 | 0.333845 | 0.339341 | NaN | NaN | NaN | NaN |
| 107 | 0.918243 | 0.576444 | 0 | 7.001244e-02 | 8 | 0.333845 | 0.339066 | NaN | NaN | NaN | NaN |
| 108 | 0.044455 | 0.445924 | 0 | 5.600995e-02 | 9 | 0.333845 | 0.338805 | NaN | NaN | NaN | NaN |
| 109 | 0.460291 | 0.452825 | 0 | 4.480796e-02 | 10 | 0.333845 | 0.338557 | NaN | NaN | NaN | NaN |
| 110 | 0.175477 | 0.632683 | 0 | 3.584637e-02 | 11 | 0.333845 | 0.338322 | NaN | NaN | NaN | NaN |
| 111 | 0.281142 | 0.239864 | 0 | 2.867709e-02 | 12 | 0.333845 | 0.338098 | NaN | NaN | NaN | NaN |
| 112 | 0.965499 | 0.163322 | 0 | 2.294168e-02 | 13 | 0.333845 | 0.337885 | NaN | NaN | NaN | NaN |
| 113 | 0.950857 | 0.700458 | 0 | 1.835334e-02 | 14 | 0.333845 | 0.337683 | NaN | NaN | NaN | NaN |
| 114 | 0.121687 | 0.848917 | 0 | 1.468267e-02 | 15 | 0.333845 | 0.337491 | NaN | NaN | NaN | NaN |
| 115 | 0.849644 | 0.096418 | 1 | 2.117461e-01 | 1 | 0.211746 | 0.331204 | NaN | NaN | NaN | NaN |
| 116 | 0.511998 | 0.239313 | 0 | 1.693969e-01 | 2 | 0.211746 | 0.325231 | NaN | NaN | NaN | NaN |
| 117 | 0.071690 | 0.454436 | 0 | 1.355175e-01 | 3 | 0.211746 | 0.319557 | NaN | NaN | NaN | NaN |
| 118 | 0.988221 | 0.135569 | 0 | 1.084140e-01 | 4 | 0.211746 | 0.314166 | NaN | NaN | NaN | NaN |
| 119 | 0.468034 | 0.031919 | 1 | 2.867312e-01 | 1 | 0.286731 | 0.312795 | NaN | NaN | NaN | NaN |
| 120 | 0.690951 | 0.313813 | 0 | 2.293850e-01 | 2 | 0.286731 | 0.311492 | NaN | NaN | NaN | NaN |
| 121 | 0.773802 | 0.546769 | 0 | 1.835080e-01 | 3 | 0.286731 | 0.310254 | NaN | NaN | NaN | NaN |
| 122 | 0.658500 | 0.273113 | 0 | 1.468064e-01 | 4 | 0.286731 | 0.309077 | NaN | NaN | NaN | NaN |
| 123 | 0.913658 | 0.233319 | 0 | 1.174451e-01 | 5 | 0.286731 | 0.307960 | NaN | NaN | NaN | NaN |
| 124 | 0.361135 | 0.287690 | 0 | 9.395609e-02 | 6 | 0.286731 | 0.306899 | NaN | NaN | NaN | NaN |
| 125 | 0.052375 | 0.331692 | 0 | 7.516487e-02 | 7 | 0.286731 | 0.305890 | NaN | NaN | NaN | NaN |
| 126 | 0.437763 | 0.596105 | 0 | 6.013189e-02 | 8 | 0.286731 | 0.304932 | NaN | NaN | NaN | NaN |
| 127 | 0.369244 | 0.445144 | 0 | 4.810552e-02 | 9 | 0.286731 | 0.304022 | NaN | NaN | NaN | NaN |
| 128 | 0.421177 | 0.408763 | 0 | 3.848441e-02 | 10 | 0.286731 | 0.303158 | NaN | NaN | NaN | NaN |
| 129 | 0.078017 | 0.060616 | 1 | 2.307875e-01 | 1 | 0.230788 | 0.299539 | NaN | NaN | NaN | NaN |
| 130 | 0.300548 | 0.912801 | 0 | 1.846300e-01 | 2 | 0.230788 | 0.296102 | NaN | NaN | NaN | NaN |
| 131 | 0.908762 | 0.938118 | 0 | 1.477040e-01 | 3 | 0.230788 | 0.292836 | NaN | NaN | NaN | NaN |
| 132 | 0.039222 | 0.343285 | 0 | 1.181632e-01 | 4 | 0.230788 | 0.289734 | NaN | NaN | NaN | NaN |
| 133 | 0.212963 | 0.567176 | 0 | 9.453057e-02 | 5 | 0.230788 | 0.286786 | NaN | NaN | NaN | NaN |
| 134 | 0.498593 | 0.855462 | 0 | 7.562446e-02 | 6 | 0.230788 | 0.283986 | NaN | NaN | NaN | NaN |
| 135 | 0.475215 | 0.261052 | 0 | 6.049957e-02 | 7 | 0.230788 | 0.281326 | NaN | NaN | NaN | NaN |
| 136 | 0.924370 | 0.648949 | 0 | 4.839965e-02 | 8 | 0.230788 | 0.278799 | NaN | NaN | NaN | NaN |
| 137 | 0.318859 | 0.025361 | 1 | 2.387197e-01 | 1 | 0.238720 | 0.276795 | NaN | NaN | NaN | NaN |
| 138 | 0.242667 | 0.976321 | 0 | 1.909758e-01 | 2 | 0.238720 | 0.274892 | NaN | NaN | NaN | NaN |
| 139 | 0.911820 | 0.176179 | 0 | 1.527806e-01 | 3 | 0.238720 | 0.273083 | NaN | NaN | NaN | NaN |
| 140 | 0.855842 | 0.121142 | 0 | 1.222245e-01 | 4 | 0.238720 | 0.271365 | NaN | NaN | NaN | NaN |
| 141 | 0.923911 | 0.888408 | 0 | 9.777960e-02 | 5 | 0.238720 | 0.269733 | NaN | NaN | NaN | NaN |
| 142 | 0.590829 | 0.600468 | 0 | 7.822368e-02 | 6 | 0.238720 | 0.268182 | NaN | NaN | NaN | NaN |
| 143 | 0.097259 | 0.788452 | 0 | 6.257894e-02 | 7 | 0.238720 | 0.266709 | NaN | NaN | NaN | NaN |
| 144 | 0.557923 | 0.071048 | 1 | 2.500632e-01 | 1 | 0.250063 | 0.265877 | NaN | NaN | NaN | NaN |
| 145 | 0.884558 | 0.242153 | 0 | 2.000505e-01 | 2 | 0.250063 | 0.265086 | NaN | NaN | NaN | NaN |
| 146 | 0.250769 | 0.174459 | 0 | 1.600404e-01 | 3 | 0.250063 | 0.264335 | NaN | NaN | NaN | NaN |
| 147 | 0.131193 | 0.770950 | 0 | 1.280323e-01 | 4 | 0.250063 | 0.263621 | NaN | NaN | NaN | NaN |
| 148 | 0.537044 | 0.712420 | 0 | 1.024259e-01 | 5 | 0.250063 | 0.262943 | NaN | NaN | NaN | NaN |
| 149 | 0.150472 | 0.713712 | 0 | 8.194069e-02 | 6 | 0.250063 | 0.262299 | NaN | NaN | NaN | NaN |
| 150 | 0.735361 | 0.608229 | 0 | 6.555256e-02 | 7 | 0.250063 | 0.261687 | NaN | NaN | NaN | NaN |
| 151 | 0.817999 | 0.761361 | 0 | 5.244204e-02 | 8 | 0.250063 | 0.261106 | NaN | NaN | NaN | NaN |
| 152 | 0.681944 | 0.483186 | 0 | 4.195364e-02 | 9 | 0.250063 | 0.260554 | NaN | NaN | NaN | NaN |
| 153 | 0.121555 | 0.764895 | 0 | 3.356291e-02 | 10 | 0.250063 | 0.260030 | NaN | NaN | NaN | NaN |
| 154 | 0.198237 | 0.897952 | 0 | 2.685033e-02 | 11 | 0.250063 | 0.259531 | NaN | NaN | NaN | NaN |
| 155 | 0.404696 | 0.458637 | 0 | 2.148026e-02 | 12 | 0.250063 | 0.259058 | NaN | NaN | NaN | NaN |
| 156 | 0.268650 | 0.308791 | 0 | 1.718421e-02 | 13 | 0.250063 | 0.258608 | NaN | NaN | NaN | NaN |
| 157 | 0.871746 | 0.669437 | 0 | 1.374737e-02 | 14 | 0.250063 | 0.258181 | NaN | NaN | NaN | NaN |
| 158 | 0.320134 | 0.138747 | 0 | 1.099789e-02 | 15 | 0.250063 | 0.257775 | NaN | NaN | NaN | NaN |
| 159 | 0.643276 | 0.684242 | 0 | 8.798315e-03 | 16 | 0.250063 | 0.257389 | NaN | NaN | NaN | NaN |
| 160 | 0.509119 | 0.526032 | 0 | 7.038652e-03 | 17 | 0.250063 | 0.257023 | NaN | NaN | NaN | NaN |
| 161 | 0.206833 | 0.724134 | 0 | 5.630922e-03 | 18 | 0.250063 | 0.256675 | NaN | NaN | NaN | NaN |
| 162 | 0.816981 | 0.888706 | 0 | 4.504737e-03 | 19 | 0.250063 | 0.256344 | NaN | NaN | NaN | NaN |
| 163 | 0.768166 | 0.689043 | 0 | 3.603790e-03 | 20 | 0.250063 | 0.256030 | NaN | NaN | NaN | NaN |
| 164 | 0.935669 | 0.429337 | 0 | 2.883032e-03 | 21 | 0.250063 | 0.255732 | NaN | NaN | NaN | NaN |
| 165 | 0.122101 | 0.276188 | 0 | 2.306426e-03 | 22 | 0.250063 | 0.255449 | NaN | NaN | NaN | NaN |
| 166 | 0.497110 | 0.729467 | 0 | 1.845140e-03 | 23 | 0.250063 | 0.255179 | NaN | NaN | NaN | NaN |
| 167 | 0.906324 | 0.284725 | 0 | 1.476112e-03 | 24 | 0.250063 | 0.254924 | NaN | NaN | NaN | NaN |
| 168 | 0.722934 | 0.175855 | 0 | 1.180890e-03 | 25 | 0.250063 | 0.254680 | NaN | NaN | NaN | NaN |
| 169 | 0.730508 | 0.962539 | 0 | 9.447119e-04 | 26 | 0.250063 | 0.254450 | NaN | NaN | NaN | NaN |
| 170 | 0.307693 | 0.783639 | 0 | 7.557695e-04 | 27 | 0.250063 | 0.254230 | NaN | NaN | NaN | NaN |
| 171 | 0.770433 | 0.957714 | 0 | 6.046156e-04 | 28 | 0.250063 | 0.254022 | NaN | NaN | NaN | NaN |
| 172 | 0.514852 | 0.091361 | 1 | 2.004837e-01 | 1 | 0.200484 | 0.251345 | NaN | NaN | NaN | NaN |
| 173 | 0.143258 | 0.151709 | 0 | 1.603870e-01 | 2 | 0.200484 | 0.248802 | NaN | NaN | NaN | NaN |
| 174 | 0.479442 | 0.895637 | 0 | 1.283096e-01 | 3 | 0.200484 | 0.246386 | NaN | NaN | NaN | NaN |
| 175 | 0.224983 | 0.983968 | 0 | 1.026477e-01 | 4 | 0.200484 | 0.244091 | NaN | NaN | NaN | NaN |
| 176 | 0.446317 | 0.255937 | 0 | 8.211812e-02 | 5 | 0.200484 | 0.241911 | NaN | NaN | NaN | NaN |
| 177 | 0.101968 | 0.954615 | 0 | 6.569450e-02 | 6 | 0.200484 | 0.239839 | NaN | NaN | NaN | NaN |
| 178 | 0.703812 | 0.160045 | 0 | 5.255560e-02 | 7 | 0.200484 | 0.237871 | NaN | NaN | NaN | NaN |
| 179 | 0.460467 | 0.704552 | 0 | 4.204448e-02 | 8 | 0.200484 | 0.236002 | NaN | NaN | NaN | NaN |
| 180 | 0.827409 | 0.616505 | 0 | 3.363558e-02 | 9 | 0.200484 | 0.234226 | NaN | NaN | NaN | NaN |
| 181 | 0.385309 | 0.328096 | 0 | 2.690847e-02 | 10 | 0.200484 | 0.232539 | NaN | NaN | NaN | NaN |
| 182 | 0.258376 | 0.490405 | 0 | 2.152677e-02 | 11 | 0.200484 | 0.230936 | NaN | NaN | NaN | NaN |
| 183 | 0.062729 | 0.544816 | 0 | 1.722142e-02 | 12 | 0.200484 | 0.229414 | NaN | NaN | NaN | NaN |
| 184 | 0.392696 | 0.772752 | 0 | 1.377713e-02 | 13 | 0.200484 | 0.227967 | NaN | NaN | NaN | NaN |
| 185 | 0.142846 | 0.733317 | 0 | 1.102171e-02 | 14 | 0.200484 | 0.226593 | NaN | NaN | NaN | NaN |
| 186 | 0.133757 | 0.961388 | 0 | 8.817366e-03 | 15 | 0.200484 | 0.225287 | NaN | NaN | NaN | NaN |
| 187 | 0.222488 | 0.064054 | 1 | 2.070539e-01 | 1 | 0.207054 | 0.224376 | NaN | NaN | NaN | NaN |
| 188 | 0.108934 | 0.013598 | 1 | 3.656431e-01 | 1 | 0.365643 | 0.231439 | NaN | NaN | NaN | NaN |
| 189 | 0.344958 | 0.530978 | 0 | 2.925145e-01 | 2 | 0.365643 | 0.238149 | NaN | NaN | NaN | NaN |
| 190 | 0.509435 | 0.728544 | 0 | 2.340116e-01 | 3 | 0.365643 | 0.244524 | NaN | NaN | NaN | NaN |
| 191 | 0.694309 | 0.307904 | 0 | 1.872093e-01 | 4 | 0.365643 | 0.250580 | NaN | NaN | NaN | NaN |
| 192 | 0.281539 | 0.143329 | 0 | 1.497674e-01 | 5 | 0.365643 | 0.256333 | NaN | NaN | NaN | NaN |
| 193 | 0.480094 | 0.796220 | 0 | 1.198139e-01 | 6 | 0.365643 | 0.261799 | NaN | NaN | NaN | NaN |
| 194 | 0.375939 | 0.432443 | 0 | 9.585115e-02 | 7 | 0.365643 | 0.266991 | NaN | NaN | NaN | NaN |
| 195 | 0.884825 | 0.002327 | 1 | 2.766809e-01 | 1 | 0.276681 | 0.267475 | NaN | NaN | NaN | NaN |
| 196 | 0.103555 | 0.129626 | 0 | 2.213447e-01 | 2 | 0.276681 | 0.267936 | NaN | NaN | NaN | NaN |
| 197 | 0.479254 | 0.518335 | 0 | 1.770758e-01 | 3 | 0.276681 | 0.268373 | NaN | NaN | NaN | NaN |
| 198 | 0.707397 | 0.127723 | 0 | 1.416606e-01 | 4 | 0.276681 | 0.268788 | NaN | NaN | NaN | NaN |
| 199 | 0.626757 | 0.675876 | 0 | 1.133285e-01 | 5 | 0.276681 | 0.269183 | NaN | NaN | NaN | NaN |
| 200 | 0.850376 | 0.630185 | 0 | 9.066280e-02 | 6 | 0.276681 | 0.269558 | NaN | NaN | NaN | NaN |
| 201 | 0.602457 | 0.213894 | 0 | 7.253024e-02 | 7 | 0.276681 | 0.269914 | NaN | NaN | NaN | NaN |
| 202 | 0.351087 | 0.942674 | 0 | 5.802419e-02 | 8 | 0.276681 | 0.270252 | NaN | NaN | NaN | NaN |
| 203 | 0.778285 | 0.626044 | 0 | 4.641936e-02 | 9 | 0.276681 | 0.270574 | NaN | NaN | NaN | NaN |
| 204 | 0.639344 | 0.010238 | 1 | 2.371355e-01 | 1 | 0.237135 | 0.268902 | NaN | NaN | NaN | NaN |
| 205 | 0.683119 | 0.826595 | 0 | 1.897084e-01 | 2 | 0.237135 | 0.267314 | NaN | NaN | NaN | NaN |
| 206 | 0.719604 | 0.871224 | 0 | 1.517667e-01 | 3 | 0.237135 | 0.265805 | NaN | NaN | NaN | NaN |
| 207 | 0.776582 | 0.755864 | 0 | 1.214134e-01 | 4 | 0.237135 | 0.264371 | NaN | NaN | NaN | NaN |
| 208 | 0.045360 | 0.550250 | 0 | 9.713069e-02 | 5 | 0.237135 | 0.263009 | NaN | NaN | NaN | NaN |
| 209 | 0.693612 | 0.413145 | 0 | 7.770456e-02 | 6 | 0.237135 | 0.261716 | NaN | NaN | NaN | NaN |
| 210 | 0.446429 | 0.326765 | 0 | 6.216364e-02 | 7 | 0.237135 | 0.260487 | NaN | NaN | NaN | NaN |
| 211 | 0.669843 | 0.698488 | 0 | 4.973092e-02 | 8 | 0.237135 | 0.259319 | NaN | NaN | NaN | NaN |
| 212 | 0.892031 | 0.161187 | 0 | 3.978473e-02 | 9 | 0.237135 | 0.258210 | NaN | NaN | NaN | NaN |
| 213 | 0.068929 | 0.521686 | 0 | 3.182779e-02 | 10 | 0.237135 | 0.257156 | NaN | NaN | NaN | NaN |
| 214 | 0.397145 | 0.346017 | 0 | 2.546223e-02 | 11 | 0.237135 | 0.256155 | NaN | NaN | NaN | NaN |
| 215 | 0.953887 | 0.320388 | 0 | 2.036978e-02 | 12 | 0.237135 | 0.255204 | NaN | NaN | NaN | NaN |
| 216 | 0.222381 | 0.074187 | 1 | 2.162958e-01 | 1 | 0.216296 | 0.253259 | NaN | NaN | NaN | NaN |
| 217 | 0.605266 | 0.357780 | 0 | 1.730367e-01 | 2 | 0.216296 | 0.251411 | NaN | NaN | NaN | NaN |
| 218 | 0.816249 | 0.621209 | 0 | 1.384293e-01 | 3 | 0.216296 | 0.249655 | NaN | NaN | NaN | NaN |
| 219 | 0.747406 | 0.647847 | 0 | 1.107435e-01 | 4 | 0.216296 | 0.247987 | NaN | NaN | NaN | NaN |
| 220 | 0.794030 | 0.652129 | 0 | 8.859477e-02 | 5 | 0.216296 | 0.246402 | NaN | NaN | NaN | NaN |
| 221 | 0.036442 | 0.802676 | 0 | 7.087582e-02 | 6 | 0.216296 | 0.244897 | NaN | NaN | NaN | NaN |
| 222 | 0.933420 | 0.860088 | 0 | 5.670065e-02 | 7 | 0.216296 | 0.243467 | NaN | NaN | NaN | NaN |
| 223 | 0.454232 | 0.496835 | 0 | 4.536052e-02 | 8 | 0.216296 | 0.242108 | NaN | NaN | NaN | NaN |
| 224 | 0.440771 | 0.682505 | 0 | 3.628842e-02 | 9 | 0.216296 | 0.240818 | NaN | NaN | NaN | NaN |
| 225 | 0.583487 | 0.099551 | 1 | 2.290307e-01 | 1 | 0.229031 | 0.240228 | NaN | NaN | NaN | NaN |
| 226 | 0.053352 | 0.325862 | 0 | 1.832246e-01 | 2 | 0.229031 | 0.239669 | NaN | NaN | NaN | NaN |
| 227 | 0.081452 | 0.602910 | 0 | 1.465797e-01 | 3 | 0.229031 | 0.239137 | NaN | NaN | NaN | NaN |
| 228 | 0.295829 | 0.254159 | 0 | 1.172637e-01 | 4 | 0.229031 | 0.238631 | NaN | NaN | NaN | NaN |
| 229 | 0.871350 | 0.555682 | 0 | 9.381099e-02 | 5 | 0.229031 | 0.238151 | NaN | NaN | NaN | NaN |
| 230 | 0.009641 | 0.792937 | 0 | 7.504879e-02 | 6 | 0.229031 | 0.237695 | NaN | NaN | NaN | NaN |
| 231 | 0.808994 | 0.845664 | 0 | 6.003903e-02 | 7 | 0.229031 | 0.237262 | NaN | NaN | NaN | NaN |
| 232 | 0.181634 | 0.594883 | 0 | 4.803123e-02 | 8 | 0.229031 | 0.236851 | NaN | NaN | NaN | NaN |
| 233 | 0.611549 | 0.921928 | 0 | 3.842498e-02 | 9 | 0.229031 | 0.236460 | NaN | NaN | NaN | NaN |
| 234 | 0.875978 | 0.569359 | 0 | 3.073998e-02 | 10 | 0.229031 | 0.236088 | NaN | NaN | NaN | NaN |
| 235 | 0.239312 | 0.241331 | 0 | 2.459199e-02 | 11 | 0.229031 | 0.235735 | NaN | NaN | NaN | NaN |
| 236 | 0.436767 | 0.052517 | 1 | 2.196736e-01 | 1 | 0.219674 | 0.234932 | NaN | NaN | NaN | NaN |
| 237 | 0.360744 | 0.205681 | 0 | 1.757389e-01 | 2 | 0.219674 | 0.234169 | NaN | NaN | NaN | NaN |
| 238 | 0.996786 | 0.683154 | 0 | 1.405911e-01 | 3 | 0.219674 | 0.233444 | NaN | NaN | NaN | NaN |
| 239 | 0.995020 | 0.737512 | 0 | 1.124729e-01 | 4 | 0.219674 | 0.232756 | NaN | NaN | NaN | NaN |
| 240 | 0.072823 | 0.739106 | 0 | 8.997830e-02 | 5 | 0.219674 | 0.232102 | NaN | NaN | NaN | NaN |
| 241 | 0.482576 | 0.549372 | 0 | 7.198264e-02 | 6 | 0.219674 | 0.231480 | NaN | NaN | NaN | NaN |
| 242 | 0.724681 | 0.807317 | 0 | 5.758611e-02 | 7 | 0.219674 | 0.230890 | NaN | NaN | NaN | NaN |
| 243 | 0.977891 | 0.485604 | 0 | 4.606889e-02 | 8 | 0.219674 | 0.230329 | NaN | NaN | NaN | NaN |
| 244 | 0.432222 | 0.225856 | 0 | 3.685511e-02 | 9 | 0.219674 | 0.229796 | NaN | NaN | NaN | NaN |
| 245 | 0.163757 | 0.463896 | 0 | 2.948409e-02 | 10 | 0.219674 | 0.229290 | NaN | NaN | NaN | NaN |
| 246 | 0.733544 | 0.006963 | 1 | 2.235873e-01 | 1 | 0.223587 | 0.229005 | NaN | NaN | NaN | NaN |
| 247 | 0.654348 | 0.189332 | 0 | 1.788698e-01 | 2 | 0.223587 | 0.228734 | NaN | NaN | NaN | NaN |
| 248 | 0.452608 | 0.076013 | 1 | 3.430959e-01 | 1 | 0.343096 | 0.234452 | NaN | NaN | NaN | NaN |
| 249 | 0.965270 | 0.144744 | 0 | 2.744767e-01 | 2 | 0.343096 | 0.239884 | NaN | NaN | NaN | NaN |
| 250 | 0.413719 | 0.932211 | 0 | 2.195813e-01 | 3 | 0.343096 | 0.245045 | NaN | NaN | NaN | NaN |
| 251 | 0.190592 | 0.331915 | 0 | 1.756651e-01 | 4 | 0.343096 | 0.249948 | NaN | NaN | NaN | NaN |
| 252 | 0.234261 | 0.933478 | 0 | 1.405321e-01 | 5 | 0.343096 | 0.254605 | NaN | NaN | NaN | NaN |
| 253 | 0.925687 | 0.818404 | 0 | 1.124256e-01 | 6 | 0.343096 | 0.259030 | NaN | NaN | NaN | NaN |
| 254 | 0.649775 | 0.651662 | 0 | 8.994052e-02 | 7 | 0.343096 | 0.263233 | NaN | NaN | NaN | NaN |
| 255 | 0.124791 | 0.569743 | 0 | 7.195242e-02 | 8 | 0.343096 | 0.267226 | NaN | NaN | NaN | NaN |
| 256 | 0.854053 | 0.346876 | 0 | 5.756193e-02 | 9 | 0.343096 | 0.271020 | NaN | NaN | NaN | NaN |
| 257 | 0.675985 | 0.067528 | 1 | 2.460495e-01 | 1 | 0.246050 | 0.269771 | NaN | NaN | NaN | NaN |
| 258 | 0.231474 | 0.923846 | 0 | 1.968396e-01 | 2 | 0.246050 | 0.268585 | NaN | NaN | NaN | NaN |
| 259 | 0.534235 | 0.347021 | 0 | 1.574717e-01 | 3 | 0.246050 | 0.267458 | NaN | NaN | NaN | NaN |
| 260 | 0.272759 | 0.501952 | 0 | 1.259774e-01 | 4 | 0.246050 | 0.266388 | NaN | NaN | NaN | NaN |
| 261 | 0.373861 | 0.865627 | 0 | 1.007819e-01 | 5 | 0.246050 | 0.265371 | NaN | NaN | NaN | NaN |
| 262 | 0.255030 | 0.337848 | 0 | 8.062552e-02 | 6 | 0.246050 | 0.264405 | NaN | NaN | NaN | NaN |
| 263 | 0.332137 | 0.833732 | 0 | 6.450041e-02 | 7 | 0.246050 | 0.263487 | NaN | NaN | NaN | NaN |
| 264 | 0.742145 | 0.559607 | 0 | 5.160033e-02 | 8 | 0.246050 | 0.262615 | NaN | NaN | NaN | NaN |
| 265 | 0.520460 | 0.615502 | 0 | 4.128026e-02 | 9 | 0.246050 | 0.261787 | NaN | NaN | NaN | NaN |
| 266 | 0.134444 | 0.419312 | 0 | 3.302421e-02 | 10 | 0.246050 | 0.261000 | NaN | NaN | NaN | NaN |
| 267 | 0.411752 | 0.618317 | 0 | 2.641937e-02 | 11 | 0.246050 | 0.260252 | NaN | NaN | NaN | NaN |
| 268 | 0.334039 | 0.352513 | 0 | 2.113550e-02 | 12 | 0.246050 | 0.259542 | NaN | NaN | NaN | NaN |
| 269 | 0.883535 | 0.830361 | 0 | 1.690840e-02 | 13 | 0.246050 | 0.258868 | NaN | NaN | NaN | NaN |
| 270 | 0.261643 | 0.494343 | 0 | 1.352672e-02 | 14 | 0.246050 | 0.258227 | NaN | NaN | NaN | NaN |
| 271 | 0.844776 | 0.196874 | 0 | 1.082137e-02 | 15 | 0.246050 | 0.257618 | NaN | NaN | NaN | NaN |
| 272 | 0.085694 | 0.780202 | 0 | 8.657099e-03 | 16 | 0.246050 | 0.257039 | NaN | NaN | NaN | NaN |
| 273 | 0.818457 | 0.222540 | 0 | 6.925679e-03 | 17 | 0.246050 | 0.256490 | NaN | NaN | NaN | NaN |
| 274 | 0.929331 | 0.831356 | 0 | 5.540543e-03 | 18 | 0.246050 | 0.255968 | NaN | NaN | NaN | NaN |
| 275 | 0.236437 | 0.192244 | 0 | 4.432435e-03 | 19 | 0.246050 | 0.255472 | NaN | NaN | NaN | NaN |
| 276 | 0.784047 | 0.360651 | 0 | 3.545948e-03 | 20 | 0.246050 | 0.255001 | NaN | NaN | NaN | NaN |
| 277 | 0.252111 | 0.871996 | 0 | 2.836758e-03 | 21 | 0.246050 | 0.254553 | NaN | NaN | NaN | NaN |
| 278 | 0.861947 | 0.339719 | 0 | 2.269407e-03 | 22 | 0.246050 | 0.254128 | NaN | NaN | NaN | NaN |
| 279 | 0.641522 | 0.409218 | 0 | 1.815525e-03 | 23 | 0.246050 | 0.253724 | NaN | NaN | NaN | NaN |
| 280 | 0.596052 | 0.045827 | 1 | 2.014524e-01 | 1 | 0.201452 | 0.251111 | NaN | NaN | NaN | NaN |
| 281 | 0.474618 | 0.835167 | 0 | 1.611619e-01 | 2 | 0.201452 | 0.248628 | NaN | NaN | NaN | NaN |
| 282 | 0.587757 | 0.894047 | 0 | 1.289295e-01 | 3 | 0.201452 | 0.246269 | NaN | NaN | NaN | NaN |
| 283 | 0.153526 | 0.286200 | 0 | 1.031436e-01 | 4 | 0.201452 | 0.244028 | NaN | NaN | NaN | NaN |
| 284 | 0.593113 | 0.589298 | 0 | 8.251491e-02 | 5 | 0.201452 | 0.241899 | NaN | NaN | NaN | NaN |
| 285 | 0.669938 | 0.024589 | 1 | 2.660119e-01 | 1 | 0.266012 | 0.243105 | NaN | NaN | NaN | NaN |
| 286 | 0.929126 | 0.174342 | 0 | 2.128095e-01 | 2 | 0.266012 | 0.244250 | NaN | NaN | NaN | NaN |
| 287 | 0.393405 | 0.039006 | 1 | 3.702476e-01 | 1 | 0.370248 | 0.250550 | NaN | NaN | NaN | NaN |
| 288 | 0.714662 | 0.465953 | 0 | 2.961981e-01 | 2 | 0.370248 | 0.256535 | NaN | NaN | NaN | NaN |
| 289 | 0.808793 | 0.440560 | 0 | 2.369585e-01 | 3 | 0.370248 | 0.262221 | NaN | NaN | NaN | NaN |
| 290 | 0.088141 | 0.764661 | 0 | 1.895668e-01 | 4 | 0.370248 | 0.267622 | NaN | NaN | NaN | NaN |
| 291 | 0.644908 | 0.809098 | 0 | 1.516534e-01 | 5 | 0.370248 | 0.272753 | NaN | NaN | NaN | NaN |
| 292 | 0.869305 | 0.587014 | 0 | 1.213227e-01 | 6 | 0.370248 | 0.277628 | NaN | NaN | NaN | NaN |
| 293 | 0.125999 | 0.868445 | 0 | 9.705820e-02 | 7 | 0.370248 | 0.282259 | NaN | NaN | NaN | NaN |
| 294 | 0.161253 | 0.136824 | 0 | 7.764656e-02 | 8 | 0.370248 | 0.286658 | NaN | NaN | NaN | NaN |
| 295 | 0.310229 | 0.426368 | 0 | 6.211725e-02 | 9 | 0.370248 | 0.290838 | NaN | NaN | NaN | NaN |
| 296 | 0.681482 | 0.827952 | 0 | 4.969380e-02 | 10 | 0.370248 | 0.294808 | NaN | NaN | NaN | NaN |
| 297 | 0.909147 | 0.968622 | 0 | 3.975504e-02 | 11 | 0.370248 | 0.298580 | NaN | NaN | NaN | NaN |
| 298 | 0.429273 | 0.060686 | 1 | 2.318040e-01 | 1 | 0.231804 | 0.295242 | NaN | NaN | NaN | NaN |
| 299 | 0.692721 | 0.975741 | 0 | 1.854432e-01 | 2 | 0.231804 | 0.292070 | NaN | NaN | NaN | NaN |
| 300 | 0.857433 | 0.692586 | 0 | 1.483546e-01 | 3 | 0.231804 | 0.289056 | NaN | NaN | NaN | NaN |
| 301 | 0.736750 | 0.280852 | 0 | 1.186837e-01 | 4 | 0.231804 | 0.286194 | NaN | NaN | NaN | NaN |
| 302 | 0.438023 | 0.928803 | 0 | 9.494693e-02 | 5 | 0.231804 | 0.283474 | NaN | NaN | NaN | NaN |
| 303 | 0.852666 | 0.217159 | 0 | 7.595754e-02 | 6 | 0.231804 | 0.280891 | NaN | NaN | NaN | NaN |
| 304 | 0.266321 | 0.273545 | 0 | 6.076604e-02 | 7 | 0.231804 | 0.278436 | NaN | NaN | NaN | NaN |
| 305 | 0.621304 | 0.040798 | 1 | 2.486128e-01 | 1 | 0.248613 | 0.276945 | NaN | NaN | NaN | NaN |
| 306 | 0.710103 | 0.460849 | 0 | 1.988903e-01 | 2 | 0.248613 | 0.275529 | NaN | NaN | NaN | NaN |
| 307 | 0.427635 | 0.050162 | 1 | 3.591122e-01 | 1 | 0.359112 | 0.279708 | NaN | NaN | NaN | NaN |
| 308 | 0.610708 | 0.037440 | 1 | 4.872898e-01 | 1 | 0.487290 | 0.290087 | NaN | NaN | NaN | NaN |
| 309 | 0.736394 | 0.863648 | 0 | 3.898318e-01 | 2 | 0.487290 | 0.299947 | NaN | NaN | NaN | NaN |
| 310 | 0.909736 | 0.261946 | 0 | 3.118655e-01 | 3 | 0.487290 | 0.309314 | NaN | NaN | NaN | NaN |
| 311 | 0.860669 | 0.637095 | 0 | 2.494924e-01 | 4 | 0.487290 | 0.318213 | NaN | NaN | NaN | NaN |
| 312 | 0.995092 | 0.862528 | 0 | 1.995939e-01 | 5 | 0.487290 | 0.326667 | NaN | NaN | NaN | NaN |
| 313 | 0.536823 | 0.288299 | 0 | 1.596751e-01 | 6 | 0.487290 | 0.334698 | NaN | NaN | NaN | NaN |
| 314 | 0.420288 | 0.749080 | 0 | 1.277401e-01 | 7 | 0.487290 | 0.342328 | NaN | NaN | NaN | NaN |
| 315 | 0.437597 | 0.503091 | 0 | 1.021921e-01 | 8 | 0.487290 | 0.349576 | NaN | NaN | NaN | NaN |
| 316 | 0.792115 | 0.187273 | 0 | 8.175366e-02 | 9 | 0.487290 | 0.356461 | NaN | NaN | NaN | NaN |
| 317 | 0.116884 | 0.895250 | 0 | 6.540293e-02 | 10 | 0.487290 | 0.363003 | NaN | NaN | NaN | NaN |
| 318 | 0.588047 | 0.031100 | 1 | 2.523223e-01 | 1 | 0.252322 | 0.357469 | NaN | NaN | NaN | NaN |
| 319 | 0.898990 | 0.916335 | 0 | 2.018579e-01 | 2 | 0.252322 | 0.352211 | NaN | NaN | NaN | NaN |
| 320 | 0.953045 | 0.090168 | 1 | 3.614863e-01 | 1 | 0.361486 | 0.352675 | NaN | NaN | NaN | NaN |
| 321 | 0.594291 | 0.212360 | 0 | 2.891890e-01 | 2 | 0.361486 | 0.353116 | NaN | NaN | NaN | NaN |
| 322 | 0.336030 | 0.430311 | 0 | 2.313512e-01 | 3 | 0.361486 | 0.353534 | NaN | NaN | NaN | NaN |
| 323 | 0.162816 | 0.118693 | 0 | 1.850810e-01 | 4 | 0.361486 | 0.353932 | NaN | NaN | NaN | NaN |
| 324 | 0.312506 | 0.614313 | 0 | 1.480648e-01 | 5 | 0.361486 | 0.354310 | NaN | NaN | NaN | NaN |
| 325 | 0.155910 | 0.904823 | 0 | 1.184518e-01 | 6 | 0.361486 | 0.354668 | NaN | NaN | NaN | NaN |
| 326 | 0.458013 | 0.467467 | 0 | 9.476146e-02 | 7 | 0.361486 | 0.355009 | NaN | NaN | NaN | NaN |
| 327 | 0.870582 | 0.524672 | 0 | 7.580917e-02 | 8 | 0.361486 | 0.355333 | NaN | NaN | NaN | NaN |
| 328 | 0.496986 | 0.674676 | 0 | 6.064734e-02 | 9 | 0.361486 | 0.355641 | NaN | NaN | NaN | NaN |
| 329 | 0.156292 | 0.809226 | 0 | 4.851787e-02 | 10 | 0.361486 | 0.355933 | NaN | NaN | NaN | NaN |
| 330 | 0.665719 | 0.297018 | 0 | 3.881430e-02 | 11 | 0.361486 | 0.356211 | NaN | NaN | NaN | NaN |
| 331 | 0.052774 | 0.835751 | 0 | 3.105144e-02 | 12 | 0.361486 | 0.356475 | NaN | NaN | NaN | NaN |
| 332 | 0.762457 | 0.441615 | 0 | 2.484115e-02 | 13 | 0.361486 | 0.356725 | NaN | NaN | NaN | NaN |
| 333 | 0.321188 | 0.216235 | 0 | 1.987292e-02 | 14 | 0.361486 | 0.356963 | NaN | NaN | NaN | NaN |
| 334 | 0.380977 | 0.775740 | 0 | 1.589834e-02 | 15 | 0.361486 | 0.357189 | NaN | NaN | NaN | NaN |
| 335 | 0.198663 | 0.127493 | 0 | 1.271867e-02 | 16 | 0.361486 | 0.357404 | NaN | NaN | NaN | NaN |
| 336 | 0.458537 | 0.181172 | 0 | 1.017493e-02 | 17 | 0.361486 | 0.357608 | NaN | NaN | NaN | NaN |
| 337 | 0.675564 | 0.432491 | 0 | 8.139948e-03 | 18 | 0.361486 | 0.357802 | NaN | NaN | NaN | NaN |
| 338 | 0.339938 | 0.575422 | 0 | 6.511958e-03 | 19 | 0.361486 | 0.357986 | NaN | NaN | NaN | NaN |
| 339 | 0.411040 | 0.358441 | 0 | 5.209567e-03 | 20 | 0.361486 | 0.358161 | NaN | NaN | NaN | NaN |
| 340 | 0.844927 | 0.150792 | 0 | 4.167653e-03 | 21 | 0.361486 | 0.358328 | NaN | NaN | NaN | NaN |
| 341 | 0.289296 | 0.059452 | 1 | 2.033341e-01 | 1 | 0.203334 | 0.350578 | NaN | NaN | NaN | NaN |
| 342 | 0.307813 | 0.009088 | 1 | 3.626673e-01 | 1 | 0.362667 | 0.351182 | NaN | NaN | NaN | NaN |
| 343 | 0.128226 | 0.422655 | 0 | 2.901338e-01 | 2 | 0.362667 | 0.351757 | NaN | NaN | NaN | NaN |
| 344 | 0.670438 | 0.298544 | 0 | 2.321071e-01 | 3 | 0.362667 | 0.352302 | NaN | NaN | NaN | NaN |
| 345 | 0.313598 | 0.615466 | 0 | 1.856857e-01 | 4 | 0.362667 | 0.352820 | NaN | NaN | NaN | NaN |
| 346 | 0.590334 | 0.530236 | 0 | 1.485485e-01 | 5 | 0.362667 | 0.353313 | NaN | NaN | NaN | NaN |
| 347 | 0.103673 | 0.821848 | 0 | 1.188388e-01 | 6 | 0.362667 | 0.353781 | NaN | NaN | NaN | NaN |
| 348 | 0.265728 | 0.194599 | 0 | 9.507106e-02 | 7 | 0.362667 | 0.354225 | NaN | NaN | NaN | NaN |
| 349 | 0.067361 | 0.097036 | 1 | 2.760568e-01 | 1 | 0.276057 | 0.350316 | NaN | NaN | NaN | NaN |
| 350 | 0.572069 | 0.185903 | 0 | 2.208455e-01 | 2 | 0.276057 | 0.346603 | NaN | NaN | NaN | NaN |
| 351 | 0.947779 | 0.268434 | 0 | 1.766764e-01 | 3 | 0.276057 | 0.343076 | NaN | NaN | NaN | NaN |
| 352 | 0.897954 | 0.835600 | 0 | 1.413411e-01 | 4 | 0.276057 | 0.339725 | NaN | NaN | NaN | NaN |
| 353 | 0.124981 | 0.826225 | 0 | 1.130729e-01 | 5 | 0.276057 | 0.336542 | NaN | NaN | NaN | NaN |
| 354 | 0.211912 | 0.656883 | 0 | 9.045831e-02 | 6 | 0.276057 | 0.333518 | NaN | NaN | NaN | NaN |
| 355 | 0.556990 | 0.047393 | 1 | 2.723666e-01 | 1 | 0.272367 | 0.330460 | NaN | NaN | NaN | NaN |
| 356 | 0.788862 | 0.705763 | 0 | 2.178933e-01 | 2 | 0.272367 | 0.327555 | NaN | NaN | NaN | NaN |
| 357 | 0.455871 | 0.463404 | 0 | 1.743147e-01 | 3 | 0.272367 | 0.324796 | NaN | NaN | NaN | NaN |
| 358 | 0.282535 | 0.902211 | 0 | 1.394517e-01 | 4 | 0.272367 | 0.322174 | NaN | NaN | NaN | NaN |
| 359 | 0.182087 | 0.762719 | 0 | 1.115614e-01 | 5 | 0.272367 | 0.319684 | NaN | NaN | NaN | NaN |
| 360 | 0.507395 | 0.752931 | 0 | 8.924910e-02 | 6 | 0.272367 | 0.317318 | NaN | NaN | NaN | NaN |
| 361 | 0.670746 | 0.377978 | 0 | 7.139928e-02 | 7 | 0.272367 | 0.315071 | NaN | NaN | NaN | NaN |
| 362 | 0.153260 | 0.840084 | 0 | 5.711943e-02 | 8 | 0.272367 | 0.312935 | NaN | NaN | NaN | NaN |
| 363 | 0.720486 | 0.173320 | 0 | 4.569554e-02 | 9 | 0.272367 | 0.310907 | NaN | NaN | NaN | NaN |
| 364 | 0.413742 | 0.743478 | 0 | 3.655643e-02 | 10 | 0.272367 | 0.308980 | NaN | NaN | NaN | NaN |
| 365 | 0.340893 | 0.664488 | 0 | 2.924515e-02 | 11 | 0.272367 | 0.307149 | NaN | NaN | NaN | NaN |
| 366 | 0.084767 | 0.943658 | 0 | 2.339612e-02 | 12 | 0.272367 | 0.305410 | NaN | NaN | NaN | NaN |
| 367 | 0.056714 | 0.183580 | 0 | 1.871689e-02 | 13 | 0.272367 | 0.303758 | NaN | NaN | NaN | NaN |
| 368 | 0.453795 | 0.796885 | 0 | 1.497351e-02 | 14 | 0.272367 | 0.302188 | NaN | NaN | NaN | NaN |
| 369 | 0.174029 | 0.967444 | 0 | 1.197881e-02 | 15 | 0.272367 | 0.300697 | NaN | NaN | NaN | NaN |
| 370 | 0.329255 | 0.107714 | 0 | 9.583049e-03 | 16 | 0.272367 | 0.299281 | NaN | NaN | NaN | NaN |
| 371 | 0.920679 | 0.695401 | 0 | 7.666440e-03 | 17 | 0.272367 | 0.297935 | NaN | NaN | NaN | NaN |
| 372 | 0.881328 | 0.768954 | 0 | 6.133152e-03 | 18 | 0.272367 | 0.296657 | NaN | NaN | NaN | NaN |
| 373 | 0.553980 | 0.935475 | 0 | 4.906521e-03 | 19 | 0.272367 | 0.295442 | NaN | NaN | NaN | NaN |
| 374 | 0.811100 | 0.650972 | 0 | 3.925217e-03 | 20 | 0.272367 | 0.294288 | NaN | NaN | NaN | NaN |
| 375 | 0.785124 | 0.951396 | 0 | 3.140174e-03 | 21 | 0.272367 | 0.293192 | NaN | NaN | NaN | NaN |
| 376 | 0.419765 | 0.552055 | 0 | 2.512139e-03 | 22 | 0.272367 | 0.292151 | NaN | NaN | NaN | NaN |
| 377 | 0.581295 | 0.563866 | 0 | 2.009711e-03 | 23 | 0.272367 | 0.291162 | NaN | NaN | NaN | NaN |
| 378 | 0.800770 | 0.858852 | 0 | 1.607769e-03 | 24 | 0.272367 | 0.290222 | NaN | NaN | NaN | NaN |
| 379 | 0.781675 | 0.203009 | 0 | 1.286215e-03 | 25 | 0.272367 | 0.289329 | NaN | NaN | NaN | NaN |
| 380 | 0.966219 | 0.291455 | 0 | 1.028972e-03 | 26 | 0.272367 | 0.288481 | NaN | NaN | NaN | NaN |
| 381 | 0.288045 | 0.904266 | 0 | 8.231777e-04 | 27 | 0.272367 | 0.287675 | NaN | NaN | NaN | NaN |
| 382 | 0.788684 | 0.042816 | 1 | 2.006585e-01 | 1 | 0.200659 | 0.283325 | NaN | NaN | NaN | NaN |
| 383 | 0.479141 | 0.022672 | 1 | 3.605268e-01 | 1 | 0.360527 | 0.287185 | NaN | NaN | NaN | NaN |
| 384 | 0.187578 | 0.978700 | 0 | 2.884215e-01 | 2 | 0.360527 | 0.290852 | NaN | NaN | NaN | NaN |
| 385 | 0.142431 | 0.621333 | 0 | 2.307372e-01 | 3 | 0.360527 | 0.294336 | NaN | NaN | NaN | NaN |
| 386 | 0.715916 | 0.694907 | 0 | 1.845897e-01 | 4 | 0.360527 | 0.297645 | NaN | NaN | NaN | NaN |
| 387 | 0.638217 | 0.345731 | 0 | 1.476718e-01 | 5 | 0.360527 | 0.300789 | NaN | NaN | NaN | NaN |
| 388 | 0.261718 | 0.876193 | 0 | 1.181374e-01 | 6 | 0.360527 | 0.303776 | NaN | NaN | NaN | NaN |
| 389 | 0.307485 | 0.658320 | 0 | 9.450995e-02 | 7 | 0.360527 | 0.306614 | NaN | NaN | NaN | NaN |
| 390 | 0.825069 | 0.949929 | 0 | 7.560796e-02 | 8 | 0.360527 | 0.309309 | NaN | NaN | NaN | NaN |
| 391 | 0.733542 | 0.375722 | 0 | 6.048637e-02 | 9 | 0.360527 | 0.311870 | NaN | NaN | NaN | NaN |
| 392 | 0.576481 | 0.751486 | 0 | 4.838909e-02 | 10 | 0.360527 | 0.314303 | NaN | NaN | NaN | NaN |
| 393 | 0.372978 | 0.837055 | 0 | 3.871127e-02 | 11 | 0.360527 | 0.316614 | NaN | NaN | NaN | NaN |
| 394 | 0.657356 | 0.232748 | 0 | 3.096902e-02 | 12 | 0.360527 | 0.318810 | NaN | NaN | NaN | NaN |
| 395 | 0.117013 | 0.815657 | 0 | 2.477522e-02 | 13 | 0.360527 | 0.320896 | NaN | NaN | NaN | NaN |
| 396 | 0.414917 | 0.955527 | 0 | 1.982017e-02 | 14 | 0.360527 | 0.322877 | NaN | NaN | NaN | NaN |
| 397 | 0.440847 | 0.562530 | 0 | 1.585614e-02 | 15 | 0.360527 | 0.324760 | NaN | NaN | NaN | NaN |
| 398 | 0.140870 | 0.664459 | 0 | 1.268491e-02 | 16 | 0.360527 | 0.326548 | NaN | NaN | NaN | NaN |
| 399 | 0.185565 | 0.498366 | 0 | 1.014793e-02 | 17 | 0.360527 | 0.328247 | NaN | NaN | NaN | NaN |
| 400 | 0.527301 | 0.965969 | 0 | 8.118343e-03 | 18 | 0.360527 | 0.329861 | NaN | NaN | NaN | NaN |
| 401 | 0.511783 | 0.928257 | 0 | 6.494674e-03 | 19 | 0.360527 | 0.331394 | NaN | NaN | NaN | NaN |
| 402 | 0.290206 | 0.528730 | 0 | 5.195739e-03 | 20 | 0.360527 | 0.332851 | NaN | NaN | NaN | NaN |
| 403 | 0.812115 | 0.380515 | 0 | 4.156591e-03 | 21 | 0.360527 | 0.334235 | NaN | NaN | NaN | NaN |
| 404 | 0.018822 | 0.134832 | 0 | 3.325273e-03 | 22 | 0.360527 | 0.335549 | NaN | NaN | NaN | NaN |
| 405 | 0.094287 | 0.425800 | 0 | 2.660218e-03 | 23 | 0.360527 | 0.336798 | NaN | NaN | NaN | NaN |
| 406 | 0.769054 | 0.858412 | 0 | 2.128175e-03 | 24 | 0.360527 | 0.337985 | NaN | NaN | NaN | NaN |
| 407 | 0.600106 | 0.037789 | 1 | 2.017025e-01 | 1 | 0.201703 | 0.331171 | NaN | NaN | NaN | NaN |
| 408 | 0.166350 | 0.029225 | 1 | 3.613620e-01 | 1 | 0.361362 | 0.332680 | NaN | NaN | NaN | NaN |
| 409 | 0.837359 | 0.150352 | 0 | 2.890896e-01 | 2 | 0.361362 | 0.334114 | NaN | NaN | NaN | NaN |
| 410 | 0.455080 | 0.992532 | 0 | 2.312717e-01 | 3 | 0.361362 | 0.335477 | NaN | NaN | NaN | NaN |
| 411 | 0.230141 | 0.252809 | 0 | 1.850174e-01 | 4 | 0.361362 | 0.336771 | NaN | NaN | NaN | NaN |
| 412 | 0.618552 | 0.934484 | 0 | 1.480139e-01 | 5 | 0.361362 | 0.338000 | NaN | NaN | NaN | NaN |
| 413 | 0.774144 | 0.863968 | 0 | 1.184111e-01 | 6 | 0.361362 | 0.339168 | NaN | NaN | NaN | NaN |
| 414 | 0.190358 | 0.775104 | 0 | 9.472889e-02 | 7 | 0.361362 | 0.340278 | NaN | NaN | NaN | NaN |
| 415 | 0.281402 | 0.022739 | 1 | 2.757831e-01 | 1 | 0.275783 | 0.337053 | NaN | NaN | NaN | NaN |
| 416 | 0.930676 | 0.801022 | 0 | 2.206265e-01 | 2 | 0.275783 | 0.333990 | NaN | NaN | NaN | NaN |
| 417 | 0.456224 | 0.529028 | 0 | 1.765012e-01 | 3 | 0.275783 | 0.331080 | NaN | NaN | NaN | NaN |
| 418 | 0.100785 | 0.919699 | 0 | 1.412010e-01 | 4 | 0.275783 | 0.328315 | NaN | NaN | NaN | NaN |
| 419 | 0.431108 | 0.330102 | 0 | 1.129608e-01 | 5 | 0.275783 | 0.325688 | NaN | NaN | NaN | NaN |
| 420 | 0.538645 | 0.159326 | 0 | 9.036861e-02 | 6 | 0.275783 | 0.323193 | NaN | NaN | NaN | NaN |
| 421 | 0.856877 | 0.956735 | 0 | 7.229489e-02 | 7 | 0.275783 | 0.320822 | NaN | NaN | NaN | NaN |
| 422 | 0.224402 | 0.947527 | 0 | 5.783591e-02 | 8 | 0.275783 | 0.318570 | NaN | NaN | NaN | NaN |
| 423 | 0.861970 | 0.318200 | 0 | 4.626873e-02 | 9 | 0.275783 | 0.316431 | NaN | NaN | NaN | NaN |
| 424 | 0.086682 | 0.301953 | 0 | 3.701498e-02 | 10 | 0.275783 | 0.314399 | NaN | NaN | NaN | NaN |
| 425 | 0.426516 | 0.028933 | 1 | 2.296120e-01 | 1 | 0.229612 | 0.310159 | NaN | NaN | NaN | NaN |
| 426 | 0.701208 | 0.021814 | 1 | 3.836896e-01 | 1 | 0.383690 | 0.313836 | NaN | NaN | NaN | NaN |
| 427 | 0.040668 | 0.091623 | 1 | 5.069517e-01 | 1 | 0.506952 | 0.323492 | NaN | NaN | NaN | NaN |
| 428 | 0.488498 | 0.337064 | 0 | 4.055613e-01 | 2 | 0.506952 | 0.332665 | NaN | NaN | NaN | NaN |
| 429 | 0.094661 | 0.546257 | 0 | 3.244491e-01 | 3 | 0.506952 | 0.341379 | NaN | NaN | NaN | NaN |
| 430 | 0.445992 | 0.947545 | 0 | 2.595593e-01 | 4 | 0.506952 | 0.349658 | NaN | NaN | NaN | NaN |
| 431 | 0.769579 | 0.222703 | 0 | 2.076474e-01 | 5 | 0.506952 | 0.357522 | NaN | NaN | NaN | NaN |
| 432 | 0.224150 | 0.554924 | 0 | 1.661179e-01 | 6 | 0.506952 | 0.364994 | NaN | NaN | NaN | NaN |
| 433 | 0.330142 | 0.131592 | 0 | 1.328943e-01 | 7 | 0.506952 | 0.372092 | NaN | NaN | NaN | NaN |
| 434 | 0.050937 | 0.583190 | 0 | 1.063155e-01 | 8 | 0.506952 | 0.378835 | NaN | NaN | NaN | NaN |
| 435 | 0.559523 | 0.186327 | 0 | 8.505238e-02 | 9 | 0.506952 | 0.385241 | NaN | NaN | NaN | NaN |
| 436 | 0.152987 | 0.916963 | 0 | 6.804190e-02 | 10 | 0.506952 | 0.391326 | NaN | NaN | NaN | NaN |
| 437 | 0.594923 | 0.775059 | 0 | 5.443352e-02 | 11 | 0.506952 | 0.397107 | NaN | NaN | NaN | NaN |
| 438 | 0.646170 | 0.919812 | 0 | 4.354682e-02 | 12 | 0.506952 | 0.402600 | NaN | NaN | NaN | NaN |
| 439 | 0.923053 | 0.368438 | 0 | 3.483745e-02 | 13 | 0.506952 | 0.407817 | NaN | NaN | NaN | NaN |
| 440 | 0.557699 | 0.376423 | 0 | 2.786996e-02 | 14 | 0.506952 | 0.412774 | NaN | NaN | NaN | NaN |
| 441 | 0.656764 | 0.545223 | 0 | 2.229597e-02 | 15 | 0.506952 | 0.417483 | NaN | NaN | NaN | NaN |
| 442 | 0.584121 | 0.122996 | 0 | 1.783678e-02 | 16 | 0.506952 | 0.421956 | NaN | NaN | NaN | NaN |
| 443 | 0.145799 | 0.997589 | 0 | 1.426942e-02 | 17 | 0.506952 | 0.426206 | NaN | NaN | NaN | NaN |
| 444 | 0.225267 | 0.170268 | 0 | 1.141554e-02 | 18 | 0.506952 | 0.430243 | NaN | NaN | NaN | NaN |
| 445 | 0.262099 | 0.710918 | 0 | 9.132429e-03 | 19 | 0.506952 | 0.434079 | NaN | NaN | NaN | NaN |
| 446 | 0.107536 | 0.904332 | 0 | 7.305944e-03 | 20 | 0.506952 | 0.437722 | NaN | NaN | NaN | NaN |
| 447 | 0.457668 | 0.334316 | 0 | 5.844755e-03 | 21 | 0.506952 | 0.441184 | NaN | NaN | NaN | NaN |
| 448 | 0.117708 | 0.183945 | 0 | 4.675804e-03 | 22 | 0.506952 | 0.444472 | NaN | NaN | NaN | NaN |
| 449 | 0.612899 | 0.019110 | 1 | 2.037406e-01 | 1 | 0.203741 | 0.432436 | NaN | NaN | NaN | NaN |
| 450 | 0.611129 | 0.691720 | 0 | 1.629925e-01 | 2 | 0.203741 | 0.421001 | NaN | NaN | NaN | NaN |
| 451 | 0.296169 | 0.719675 | 0 | 1.303940e-01 | 3 | 0.203741 | 0.410138 | NaN | NaN | NaN | NaN |
| 452 | 0.588823 | 0.983757 | 0 | 1.043152e-01 | 4 | 0.203741 | 0.399818 | NaN | NaN | NaN | NaN |
| 453 | 0.939885 | 0.156385 | 0 | 8.345217e-02 | 5 | 0.203741 | 0.390014 | NaN | NaN | NaN | NaN |
| 454 | 0.713366 | 0.201554 | 0 | 6.676173e-02 | 6 | 0.203741 | 0.380700 | NaN | NaN | NaN | NaN |
| 455 | 0.530936 | 0.632135 | 0 | 5.340939e-02 | 7 | 0.203741 | 0.371852 | NaN | NaN | NaN | NaN |
| 456 | 0.162731 | 0.136016 | 0 | 4.272751e-02 | 8 | 0.203741 | 0.363447 | NaN | NaN | NaN | NaN |
| 457 | 0.219396 | 0.485183 | 0 | 3.418201e-02 | 9 | 0.203741 | 0.355462 | NaN | NaN | NaN | NaN |
| 458 | 0.117515 | 0.180880 | 0 | 2.734561e-02 | 10 | 0.203741 | 0.347876 | NaN | NaN | NaN | NaN |
| 459 | 0.101490 | 0.731146 | 0 | 2.187648e-02 | 11 | 0.203741 | 0.340669 | NaN | NaN | NaN | NaN |
| 460 | 0.605770 | 0.987821 | 0 | 1.750119e-02 | 12 | 0.203741 | 0.333822 | NaN | NaN | NaN | NaN |
| 461 | 0.742275 | 0.990585 | 0 | 1.400095e-02 | 13 | 0.203741 | 0.327318 | NaN | NaN | NaN | NaN |
| 462 | 0.160068 | 0.283920 | 0 | 1.120076e-02 | 14 | 0.203741 | 0.321139 | NaN | NaN | NaN | NaN |
| 463 | 0.509555 | 0.976015 | 0 | 8.960608e-03 | 15 | 0.203741 | 0.315269 | NaN | NaN | NaN | NaN |
| 464 | 0.395452 | 0.171192 | 0 | 7.168487e-03 | 16 | 0.203741 | 0.309693 | NaN | NaN | NaN | NaN |
| 465 | 0.810602 | 0.999459 | 0 | 5.734789e-03 | 17 | 0.203741 | 0.304395 | NaN | NaN | NaN | NaN |
| 466 | 0.019842 | 0.274881 | 0 | 4.587831e-03 | 18 | 0.203741 | 0.299363 | NaN | NaN | NaN | NaN |
| 467 | 0.002760 | 0.300360 | 0 | 3.670265e-03 | 19 | 0.203741 | 0.294582 | NaN | NaN | NaN | NaN |
| 468 | 0.718452 | 0.710492 | 0 | 2.936212e-03 | 20 | 0.203741 | 0.290040 | NaN | NaN | NaN | NaN |
| 469 | 0.311661 | 0.640974 | 0 | 2.348970e-03 | 21 | 0.203741 | 0.285725 | NaN | NaN | NaN | NaN |
| 470 | 0.792491 | 0.007763 | 1 | 2.018792e-01 | 1 | 0.201879 | 0.281532 | NaN | NaN | NaN | NaN |
| 471 | 0.088298 | 0.995248 | 0 | 1.615033e-01 | 2 | 0.201879 | 0.277550 | NaN | NaN | NaN | NaN |
| 472 | 0.814184 | 0.762453 | 0 | 1.292027e-01 | 3 | 0.201879 | 0.273766 | NaN | NaN | NaN | NaN |
| 473 | 0.298467 | 0.206013 | 0 | 1.033621e-01 | 4 | 0.201879 | 0.270172 | NaN | NaN | NaN | NaN |
| 474 | 0.022874 | 0.923931 | 0 | 8.268971e-02 | 5 | 0.201879 | 0.266757 | NaN | NaN | NaN | NaN |
| 475 | 0.223141 | 0.908215 | 0 | 6.615177e-02 | 6 | 0.201879 | 0.263513 | NaN | NaN | NaN | NaN |
| 476 | 0.821362 | 0.698805 | 0 | 5.292141e-02 | 7 | 0.201879 | 0.260432 | NaN | NaN | NaN | NaN |
| 477 | 0.992275 | 0.532679 | 0 | 4.233713e-02 | 8 | 0.201879 | 0.257504 | NaN | NaN | NaN | NaN |
| 478 | 0.831648 | 0.129468 | 0 | 3.386971e-02 | 9 | 0.201879 | 0.254723 | NaN | NaN | NaN | NaN |
| 479 | 0.141638 | 0.800736 | 0 | 2.709576e-02 | 10 | 0.201879 | 0.252081 | NaN | NaN | NaN | NaN |
| 480 | 0.281969 | 0.453401 | 0 | 2.167661e-02 | 11 | 0.201879 | 0.249570 | NaN | NaN | NaN | NaN |
| 481 | 0.814895 | 0.296123 | 0 | 1.734129e-02 | 12 | 0.201879 | 0.247186 | NaN | NaN | NaN | NaN |
| 482 | 0.472690 | 0.466924 | 0 | 1.387303e-02 | 13 | 0.201879 | 0.244921 | NaN | NaN | NaN | NaN |
| 483 | 0.301872 | 0.723306 | 0 | 1.109843e-02 | 14 | 0.201879 | 0.242768 | NaN | NaN | NaN | NaN |
| 484 | 0.110427 | 0.798926 | 0 | 8.878740e-03 | 15 | 0.201879 | 0.240724 | NaN | NaN | NaN | NaN |
| 485 | 0.157263 | 0.613113 | 0 | 7.102992e-03 | 16 | 0.201879 | 0.238782 | NaN | NaN | NaN | NaN |
| 486 | 0.014344 | 0.379797 | 0 | 5.682394e-03 | 17 | 0.201879 | 0.236937 | NaN | NaN | NaN | NaN |
| 487 | 0.358874 | 0.065144 | 1 | 2.045459e-01 | 1 | 0.204546 | 0.235317 | NaN | NaN | NaN | NaN |
| 488 | 0.145296 | 0.492658 | 0 | 1.636367e-01 | 2 | 0.204546 | 0.233779 | NaN | NaN | NaN | NaN |
| 489 | 0.595604 | 0.685251 | 0 | 1.309094e-01 | 3 | 0.204546 | 0.232317 | NaN | NaN | NaN | NaN |
| 490 | 0.850231 | 0.783187 | 0 | 1.047275e-01 | 4 | 0.204546 | 0.230928 | NaN | NaN | NaN | NaN |
| 491 | 0.405814 | 0.014633 | 1 | 2.837820e-01 | 1 | 0.283782 | 0.233571 | NaN | NaN | NaN | NaN |
| 492 | 0.366667 | 0.036432 | 1 | 4.270256e-01 | 1 | 0.427026 | 0.243244 | NaN | NaN | NaN | NaN |
| 493 | 0.177654 | 0.299485 | 0 | 3.416205e-01 | 2 | 0.427026 | 0.252433 | NaN | NaN | NaN | NaN |
| 494 | 0.914276 | 0.600292 | 0 | 2.732964e-01 | 3 | 0.427026 | 0.261163 | NaN | NaN | NaN | NaN |
| 495 | 0.963552 | 0.526960 | 0 | 2.186371e-01 | 4 | 0.427026 | 0.269456 | NaN | NaN | NaN | NaN |
| 496 | 0.484472 | 0.132878 | 0 | 1.749097e-01 | 5 | 0.427026 | 0.277334 | NaN | NaN | NaN | NaN |
| 497 | 0.218786 | 0.880509 | 0 | 1.399278e-01 | 6 | 0.427026 | 0.284819 | NaN | NaN | NaN | NaN |
| 498 | 0.799822 | 0.102009 | 0 | 1.119422e-01 | 7 | 0.427026 | 0.291929 | NaN | NaN | NaN | NaN |
| 499 | 0.344431 | 0.537034 | 0 | 8.955376e-02 | 8 | 0.427026 | 0.298684 | NaN | NaN | NaN | NaN |
| 500 | 0.881279 | 0.788150 | 0 | 7.164301e-02 | 9 | 0.427026 | 0.305101 | NaN | NaN | NaN | NaN |
| 501 | 0.771531 | 0.446895 | 0 | 5.731441e-02 | 10 | 0.427026 | 0.311197 | NaN | NaN | NaN | NaN |
| 502 | 0.464118 | 0.695649 | 0 | 4.585153e-02 | 11 | 0.427026 | 0.316989 | NaN | NaN | NaN | NaN |
| 503 | 0.067953 | 0.078587 | 1 | 2.366812e-01 | 1 | 0.236681 | 0.312973 | NaN | NaN | NaN | NaN |
| 504 | 0.827674 | 0.410782 | 0 | 1.893450e-01 | 2 | 0.236681 | 0.309159 | NaN | NaN | NaN | NaN |
| 505 | 0.561848 | 0.261282 | 0 | 1.514760e-01 | 3 | 0.236681 | 0.305535 | NaN | NaN | NaN | NaN |
| 506 | 0.837204 | 0.348843 | 0 | 1.211808e-01 | 4 | 0.236681 | 0.302092 | NaN | NaN | NaN | NaN |
| 507 | 0.463987 | 0.174490 | 0 | 9.694463e-02 | 5 | 0.236681 | 0.298822 | NaN | NaN | NaN | NaN |
| 508 | 0.479179 | 0.186985 | 0 | 7.755570e-02 | 6 | 0.236681 | 0.295715 | NaN | NaN | NaN | NaN |
| 509 | 0.721658 | 0.184640 | 0 | 6.204456e-02 | 7 | 0.236681 | 0.292763 | NaN | NaN | NaN | NaN |
| 510 | 0.448122 | 0.405984 | 0 | 4.963565e-02 | 8 | 0.236681 | 0.289959 | NaN | NaN | NaN | NaN |
| 511 | 0.463433 | 0.848648 | 0 | 3.970852e-02 | 9 | 0.236681 | 0.287295 | NaN | NaN | NaN | NaN |
| 512 | 0.410725 | 0.474603 | 0 | 3.176682e-02 | 10 | 0.236681 | 0.284764 | NaN | NaN | NaN | NaN |
| 513 | 0.089504 | 0.745647 | 0 | 2.541345e-02 | 11 | 0.236681 | 0.282360 | NaN | NaN | NaN | NaN |
| 514 | 0.131596 | 0.157107 | 0 | 2.033076e-02 | 12 | 0.236681 | 0.280076 | NaN | NaN | NaN | NaN |
| 515 | 0.846728 | 0.376457 | 0 | 1.626461e-02 | 13 | 0.236681 | 0.277906 | NaN | NaN | NaN | NaN |
| 516 | 0.348005 | 0.951101 | 0 | 1.301169e-02 | 14 | 0.236681 | 0.275845 | NaN | NaN | NaN | NaN |
| 517 | 0.199868 | 0.718411 | 0 | 1.040935e-02 | 15 | 0.236681 | 0.273887 | NaN | NaN | NaN | NaN |
| 518 | 0.984777 | 0.152886 | 0 | 8.327480e-03 | 16 | 0.236681 | 0.272027 | NaN | NaN | NaN | NaN |
| 519 | 0.897401 | 0.938637 | 0 | 6.661984e-03 | 17 | 0.236681 | 0.270259 | NaN | NaN | NaN | NaN |
| 520 | 0.314607 | 0.775383 | 0 | 5.329587e-03 | 18 | 0.236681 | 0.268580 | NaN | NaN | NaN | NaN |
| 521 | 0.336525 | 0.565255 | 0 | 4.263670e-03 | 19 | 0.236681 | 0.266986 | NaN | NaN | NaN | NaN |
| 522 | 0.006322 | 0.924471 | 0 | 3.410936e-03 | 20 | 0.236681 | 0.265470 | NaN | NaN | NaN | NaN |
| 523 | 0.490839 | 0.172384 | 0 | 2.728749e-03 | 21 | 0.236681 | 0.264031 | NaN | NaN | NaN | NaN |
| 524 | 0.629655 | 0.078910 | 1 | 2.021830e-01 | 1 | 0.202183 | 0.260938 | NaN | NaN | NaN | NaN |
| 525 | 0.186479 | 0.446023 | 0 | 1.617464e-01 | 2 | 0.202183 | 0.258001 | NaN | NaN | NaN | NaN |
| 526 | 0.269044 | 0.463173 | 0 | 1.293971e-01 | 3 | 0.202183 | 0.255210 | NaN | NaN | NaN | NaN |
| 527 | 0.137706 | 0.724095 | 0 | 1.035177e-01 | 4 | 0.202183 | 0.252558 | NaN | NaN | NaN | NaN |
| 528 | 0.062756 | 0.688484 | 0 | 8.281416e-02 | 5 | 0.202183 | 0.250040 | NaN | NaN | NaN | NaN |
| 529 | 0.698389 | 0.621321 | 0 | 6.625133e-02 | 6 | 0.202183 | 0.247647 | NaN | NaN | NaN | NaN |
| 530 | 0.052545 | 0.542553 | 0 | 5.300106e-02 | 7 | 0.202183 | 0.245374 | NaN | NaN | NaN | NaN |
| 531 | 0.396967 | 0.799579 | 0 | 4.240085e-02 | 8 | 0.202183 | 0.243214 | NaN | NaN | NaN | NaN |
| 532 | 0.981350 | 0.101233 | 0 | 3.392068e-02 | 9 | 0.202183 | 0.241163 | NaN | NaN | NaN | NaN |
| 533 | 0.723018 | 0.984341 | 0 | 2.713654e-02 | 10 | 0.202183 | 0.239214 | NaN | NaN | NaN | NaN |
| 534 | 0.093711 | 0.724246 | 0 | 2.170923e-02 | 11 | 0.202183 | 0.237362 | NaN | NaN | NaN | NaN |
| 535 | 0.375222 | 0.880450 | 0 | 1.736739e-02 | 12 | 0.202183 | 0.235603 | NaN | NaN | NaN | NaN |
| 536 | 0.510168 | 0.381760 | 0 | 1.389391e-02 | 13 | 0.202183 | 0.233932 | NaN | NaN | NaN | NaN |
| 537 | 0.893155 | 0.144402 | 0 | 1.111513e-02 | 14 | 0.202183 | 0.232345 | NaN | NaN | NaN | NaN |
| 538 | 0.000621 | 0.678912 | 0 | 8.892102e-03 | 15 | 0.202183 | 0.230837 | NaN | NaN | NaN | NaN |
| 539 | 0.737061 | 0.229567 | 0 | 7.113682e-03 | 16 | 0.202183 | 0.229404 | NaN | NaN | NaN | NaN |
| 540 | 0.563282 | 0.832066 | 0 | 5.690945e-03 | 17 | 0.202183 | 0.228043 | NaN | NaN | NaN | NaN |
| 541 | 0.986548 | 0.955055 | 0 | 4.552756e-03 | 18 | 0.202183 | 0.226750 | NaN | NaN | NaN | NaN |
| 542 | 0.919386 | 0.274957 | 0 | 3.642205e-03 | 19 | 0.202183 | 0.225522 | NaN | NaN | NaN | NaN |
| 543 | 0.765410 | 0.543683 | 0 | 2.913764e-03 | 20 | 0.202183 | 0.224355 | NaN | NaN | NaN | NaN |
| 544 | 0.106340 | 0.996771 | 0 | 2.331011e-03 | 21 | 0.202183 | 0.223246 | NaN | NaN | NaN | NaN |
| 545 | 0.707809 | 0.630584 | 0 | 1.864809e-03 | 22 | 0.202183 | 0.222193 | NaN | NaN | NaN | NaN |
| 546 | 0.743618 | 0.740264 | 0 | 1.491847e-03 | 23 | 0.202183 | 0.221192 | NaN | NaN | NaN | NaN |
| 547 | 0.531350 | 0.128104 | 0 | 1.193478e-03 | 24 | 0.202183 | 0.220242 | NaN | NaN | NaN | NaN |
| 548 | 0.159864 | 0.809346 | 0 | 9.547822e-04 | 25 | 0.202183 | 0.219339 | NaN | NaN | NaN | NaN |
| 549 | 0.423863 | 0.626959 | 0 | 7.638258e-04 | 26 | 0.202183 | 0.218481 | NaN | NaN | NaN | NaN |
| 550 | 0.512674 | 0.085893 | 1 | 2.006111e-01 | 1 | 0.200611 | 0.217588 | NaN | NaN | NaN | NaN |
| 551 | 0.159641 | 0.265985 | 0 | 1.604888e-01 | 2 | 0.200611 | 0.216739 | NaN | NaN | NaN | NaN |
| 552 | 0.864089 | 0.459447 | 0 | 1.283911e-01 | 3 | 0.200611 | 0.215932 | NaN | NaN | NaN | NaN |
| 553 | 0.892384 | 0.276769 | 0 | 1.027129e-01 | 4 | 0.200611 | 0.215166 | NaN | NaN | NaN | NaN |
| 554 | 0.157529 | 0.895814 | 0 | 8.217029e-02 | 5 | 0.200611 | 0.214439 | NaN | NaN | NaN | NaN |
| 555 | 0.509204 | 0.034009 | 1 | 2.657362e-01 | 1 | 0.265736 | 0.217003 | NaN | NaN | NaN | NaN |
| 556 | 0.391621 | 0.867128 | 0 | 2.125890e-01 | 2 | 0.265736 | 0.219440 | NaN | NaN | NaN | NaN |
| 557 | 0.433845 | 0.762400 | 0 | 1.700712e-01 | 3 | 0.265736 | 0.221755 | NaN | NaN | NaN | NaN |
| 558 | 0.422055 | 0.532981 | 0 | 1.360570e-01 | 4 | 0.265736 | 0.223954 | NaN | NaN | NaN | NaN |
| 559 | 0.327051 | 0.676541 | 0 | 1.088456e-01 | 5 | 0.265736 | 0.226043 | NaN | NaN | NaN | NaN |
| 560 | 0.616270 | 0.486628 | 0 | 8.707645e-02 | 6 | 0.265736 | 0.228028 | NaN | NaN | NaN | NaN |
| 561 | 0.315118 | 0.387694 | 0 | 6.966116e-02 | 7 | 0.265736 | 0.229913 | NaN | NaN | NaN | NaN |
| 562 | 0.612702 | 0.789611 | 0 | 5.572893e-02 | 8 | 0.265736 | 0.231704 | NaN | NaN | NaN | NaN |
| 563 | 0.079685 | 0.791949 | 0 | 4.458314e-02 | 9 | 0.265736 | 0.233406 | NaN | NaN | NaN | NaN |
| 564 | 0.224743 | 0.530571 | 0 | 3.566651e-02 | 10 | 0.265736 | 0.235022 | NaN | NaN | NaN | NaN |
| 565 | 0.336259 | 0.265538 | 0 | 2.853321e-02 | 11 | 0.265736 | 0.236558 | NaN | NaN | NaN | NaN |
| 566 | 0.811004 | 0.018324 | 1 | 2.228266e-01 | 1 | 0.222827 | 0.235872 | NaN | NaN | NaN | NaN |
| 567 | 0.217727 | 0.007622 | 1 | 3.782613e-01 | 1 | 0.378261 | 0.242991 | NaN | NaN | NaN | NaN |
| 568 | 0.392427 | 0.604856 | 0 | 3.026090e-01 | 2 | 0.378261 | 0.249755 | NaN | NaN | NaN | NaN |
| 569 | 0.741953 | 0.477348 | 0 | 2.420872e-01 | 3 | 0.378261 | 0.256180 | NaN | NaN | NaN | NaN |
| 570 | 0.321032 | 0.820837 | 0 | 1.936698e-01 | 4 | 0.378261 | 0.262284 | NaN | NaN | NaN | NaN |
| 571 | 0.587556 | 0.524363 | 0 | 1.549358e-01 | 5 | 0.378261 | 0.268083 | NaN | NaN | NaN | NaN |
| 572 | 0.235345 | 0.175153 | 0 | 1.239486e-01 | 6 | 0.378261 | 0.273592 | NaN | NaN | NaN | NaN |
| 573 | 0.615258 | 0.480082 | 0 | 9.915892e-02 | 7 | 0.378261 | 0.278825 | NaN | NaN | NaN | NaN |
| 574 | 0.417880 | 0.442174 | 0 | 7.932713e-02 | 8 | 0.378261 | 0.283797 | NaN | NaN | NaN | NaN |
| 575 | 0.067986 | 0.896117 | 0 | 6.346171e-02 | 9 | 0.378261 | 0.288520 | NaN | NaN | NaN | NaN |
| 576 | 0.997412 | 0.247856 | 0 | 5.076937e-02 | 10 | 0.378261 | 0.293007 | NaN | NaN | NaN | NaN |
| 577 | 0.853632 | 0.037448 | 1 | 2.406155e-01 | 1 | 0.240615 | 0.290388 | NaN | NaN | NaN | NaN |
| 578 | 0.913430 | 0.120939 | 0 | 1.924924e-01 | 2 | 0.240615 | 0.287899 | NaN | NaN | NaN | NaN |
| 579 | 0.280531 | 0.677658 | 0 | 1.539939e-01 | 3 | 0.240615 | 0.285535 | NaN | NaN | NaN | NaN |
| 580 | 0.335451 | 0.141506 | 0 | 1.231951e-01 | 4 | 0.240615 | 0.283289 | NaN | NaN | NaN | NaN |
| 581 | 0.675904 | 0.234164 | 0 | 9.855611e-02 | 5 | 0.240615 | 0.281155 | NaN | NaN | NaN | NaN |
| 582 | 0.662120 | 0.779937 | 0 | 7.884488e-02 | 6 | 0.240615 | 0.279128 | NaN | NaN | NaN | NaN |
| 583 | 0.398543 | 0.120681 | 0 | 6.307591e-02 | 7 | 0.240615 | 0.277203 | NaN | NaN | NaN | NaN |
| 584 | 0.123999 | 0.249085 | 0 | 5.046073e-02 | 8 | 0.240615 | 0.275373 | NaN | NaN | NaN | NaN |
| 585 | 0.363696 | 0.195616 | 0 | 4.036858e-02 | 9 | 0.240615 | 0.273635 | NaN | NaN | NaN | NaN |
| 586 | 0.892118 | 0.606499 | 0 | 3.229486e-02 | 10 | 0.240615 | 0.271984 | NaN | NaN | NaN | NaN |
| 587 | 0.663552 | 0.927838 | 0 | 2.583589e-02 | 11 | 0.240615 | 0.270416 | NaN | NaN | NaN | NaN |
| 588 | 0.917746 | 0.247292 | 0 | 2.066871e-02 | 12 | 0.240615 | 0.268926 | NaN | NaN | NaN | NaN |
| 589 | 0.601957 | 0.979993 | 0 | 1.653497e-02 | 13 | 0.240615 | 0.267510 | NaN | NaN | NaN | NaN |
| 590 | 0.166256 | 0.268143 | 0 | 1.322798e-02 | 14 | 0.240615 | 0.266166 | NaN | NaN | NaN | NaN |
| 591 | 0.206341 | 0.184645 | 0 | 1.058238e-02 | 15 | 0.240615 | 0.264888 | NaN | NaN | NaN | NaN |
| 592 | 0.581530 | 0.295777 | 0 | 8.465905e-03 | 16 | 0.240615 | 0.263675 | NaN | NaN | NaN | NaN |
| 593 | 0.350646 | 0.735929 | 0 | 6.772724e-03 | 17 | 0.240615 | 0.262522 | NaN | NaN | NaN | NaN |
| 594 | 0.852265 | 0.736757 | 0 | 5.418179e-03 | 18 | 0.240615 | 0.261426 | NaN | NaN | NaN | NaN |
| 595 | 0.165869 | 0.980735 | 0 | 4.334543e-03 | 19 | 0.240615 | 0.260386 | NaN | NaN | NaN | NaN |
| 596 | 0.626120 | 0.387514 | 0 | 3.467635e-03 | 20 | 0.240615 | 0.259397 | NaN | NaN | NaN | NaN |
| 597 | 0.653233 | 0.625957 | 0 | 2.774108e-03 | 21 | 0.240615 | 0.258458 | NaN | NaN | NaN | NaN |
| 598 | 0.213308 | 0.953250 | 0 | 2.219286e-03 | 22 | 0.240615 | 0.257566 | NaN | NaN | NaN | NaN |
| 599 | 0.900827 | 0.904846 | 0 | 1.775429e-03 | 23 | 0.240615 | 0.256718 | NaN | NaN | NaN | NaN |
| 600 | 0.472610 | 0.160876 | 0 | 1.420343e-03 | 24 | 0.240615 | 0.255913 | NaN | NaN | NaN | NaN |
| 601 | 0.167568 | 0.204486 | 0 | 1.136275e-03 | 25 | 0.240615 | 0.255148 | NaN | NaN | NaN | NaN |
| 602 | 0.617504 | 0.854693 | 0 | 9.090196e-04 | 26 | 0.240615 | 0.254422 | NaN | NaN | NaN | NaN |
| 603 | 0.296709 | 0.551977 | 0 | 7.272157e-04 | 27 | 0.240615 | 0.253731 | NaN | NaN | NaN | NaN |
| 604 | 0.209032 | 0.164671 | 0 | 5.817726e-04 | 28 | 0.240615 | 0.253076 | NaN | NaN | NaN | NaN |
| 605 | 0.490809 | 0.908823 | 0 | 4.654181e-04 | 29 | 0.240615 | 0.252453 | NaN | NaN | NaN | NaN |
| 606 | 0.909062 | 0.607226 | 0 | 3.723344e-04 | 30 | 0.240615 | 0.251861 | NaN | NaN | NaN | NaN |
| 607 | 0.785457 | 0.416533 | 0 | 2.978676e-04 | 31 | 0.240615 | 0.251299 | NaN | NaN | NaN | NaN |
| 608 | 0.399906 | 0.779271 | 0 | 2.382940e-04 | 32 | 0.240615 | 0.250764 | NaN | NaN | NaN | NaN |
| 609 | 0.542480 | 0.072654 | 1 | 2.001906e-01 | 1 | 0.200191 | 0.248236 | NaN | NaN | NaN | NaN |
| 610 | 0.683867 | 0.240572 | 0 | 1.601525e-01 | 2 | 0.200191 | 0.245833 | NaN | NaN | NaN | NaN |
| 611 | 0.715310 | 0.061871 | 1 | 3.281220e-01 | 1 | 0.328122 | 0.249948 | NaN | NaN | NaN | NaN |
| 612 | 0.162737 | 0.740176 | 0 | 2.624976e-01 | 2 | 0.328122 | 0.253857 | NaN | NaN | NaN | NaN |
| 613 | 0.368345 | 0.403696 | 0 | 2.099981e-01 | 3 | 0.328122 | 0.257570 | NaN | NaN | NaN | NaN |
| 614 | 0.068781 | 0.263782 | 0 | 1.679985e-01 | 4 | 0.328122 | 0.261097 | NaN | NaN | NaN | NaN |
| 615 | 0.135205 | 0.254505 | 0 | 1.343988e-01 | 5 | 0.328122 | 0.264449 | NaN | NaN | NaN | NaN |
| 616 | 0.035055 | 0.484733 | 0 | 1.075190e-01 | 6 | 0.328122 | 0.267632 | NaN | NaN | NaN | NaN |
| 617 | 0.732707 | 0.180654 | 0 | 8.601522e-02 | 7 | 0.328122 | 0.270657 | NaN | NaN | NaN | NaN |
| 618 | 0.616645 | 0.256855 | 0 | 6.881217e-02 | 8 | 0.328122 | 0.273530 | NaN | NaN | NaN | NaN |
| 619 | 0.891104 | 0.830340 | 0 | 5.504974e-02 | 9 | 0.328122 | 0.276260 | NaN | NaN | NaN | NaN |
| 620 | 0.121397 | 0.348417 | 0 | 4.403979e-02 | 10 | 0.328122 | 0.278853 | NaN | NaN | NaN | NaN |
| 621 | 0.777823 | 0.519388 | 0 | 3.523183e-02 | 11 | 0.328122 | 0.281316 | NaN | NaN | NaN | NaN |
| 622 | 0.097868 | 0.879194 | 0 | 2.818547e-02 | 12 | 0.328122 | 0.283657 | NaN | NaN | NaN | NaN |
| 623 | 0.170869 | 0.420644 | 0 | 2.254837e-02 | 13 | 0.328122 | 0.285880 | NaN | NaN | NaN | NaN |
| 624 | 0.631732 | 0.973971 | 0 | 1.803870e-02 | 14 | 0.328122 | 0.287992 | NaN | NaN | NaN | NaN |
| 625 | 0.846551 | 0.934129 | 0 | 1.443096e-02 | 15 | 0.328122 | 0.289998 | NaN | NaN | NaN | NaN |
| 626 | 0.294743 | 0.213389 | 0 | 1.154477e-02 | 16 | 0.328122 | 0.291905 | NaN | NaN | NaN | NaN |
| 627 | 0.279831 | 0.807082 | 0 | 9.235813e-03 | 17 | 0.328122 | 0.293715 | NaN | NaN | NaN | NaN |
| 628 | 0.201108 | 0.164899 | 0 | 7.388651e-03 | 18 | 0.328122 | 0.295436 | NaN | NaN | NaN | NaN |
| 629 | 0.287963 | 0.076854 | 1 | 2.059109e-01 | 1 | 0.205911 | 0.290960 | NaN | NaN | NaN | NaN |
| 630 | 0.386023 | 0.871587 | 0 | 1.647287e-01 | 2 | 0.205911 | 0.286707 | NaN | NaN | NaN | NaN |
| 631 | 0.480937 | 0.597984 | 0 | 1.317830e-01 | 3 | 0.205911 | 0.282667 | NaN | NaN | NaN | NaN |
| 632 | 0.314903 | 0.814194 | 0 | 1.054264e-01 | 4 | 0.205911 | 0.278830 | NaN | NaN | NaN | NaN |
| 633 | 0.695528 | 0.976364 | 0 | 8.434111e-02 | 5 | 0.205911 | 0.275184 | NaN | NaN | NaN | NaN |
| 634 | 0.147021 | 0.831782 | 0 | 6.747289e-02 | 6 | 0.205911 | 0.271720 | NaN | NaN | NaN | NaN |
| 635 | 0.191369 | 0.122099 | 0 | 5.397831e-02 | 7 | 0.205911 | 0.268429 | NaN | NaN | NaN | NaN |
| 636 | 0.754880 | 0.469846 | 0 | 4.318265e-02 | 8 | 0.205911 | 0.265304 | NaN | NaN | NaN | NaN |
| 637 | 0.563621 | 0.318362 | 0 | 3.454612e-02 | 9 | 0.205911 | 0.262334 | NaN | NaN | NaN | NaN |
| 638 | 0.984417 | 0.542618 | 0 | 2.763690e-02 | 10 | 0.205911 | 0.259513 | NaN | NaN | NaN | NaN |
| 639 | 0.691816 | 0.921490 | 0 | 2.210952e-02 | 11 | 0.205911 | 0.256833 | NaN | NaN | NaN | NaN |
| 640 | 0.228287 | 0.560613 | 0 | 1.768761e-02 | 12 | 0.205911 | 0.254287 | NaN | NaN | NaN | NaN |
| 641 | 0.790486 | 0.308810 | 0 | 1.415009e-02 | 13 | 0.205911 | 0.251868 | NaN | NaN | NaN | NaN |
| 642 | 0.775179 | 0.437858 | 0 | 1.132007e-02 | 14 | 0.205911 | 0.249570 | NaN | NaN | NaN | NaN |
| 643 | 0.775043 | 0.991757 | 0 | 9.056058e-03 | 15 | 0.205911 | 0.247387 | NaN | NaN | NaN | NaN |
| 644 | 0.245601 | 0.298683 | 0 | 7.244846e-03 | 16 | 0.205911 | 0.245313 | NaN | NaN | NaN | NaN |
| 645 | 0.804425 | 0.445033 | 0 | 5.795877e-03 | 17 | 0.205911 | 0.243343 | NaN | NaN | NaN | NaN |
| 646 | 0.585416 | 0.635442 | 0 | 4.636702e-03 | 18 | 0.205911 | 0.241471 | NaN | NaN | NaN | NaN |
| 647 | 0.437189 | 0.965692 | 0 | 3.709361e-03 | 19 | 0.205911 | 0.239693 | NaN | NaN | NaN | NaN |
| 648 | 0.872069 | 0.800259 | 0 | 2.967489e-03 | 20 | 0.205911 | 0.238004 | NaN | NaN | NaN | NaN |
| 649 | 0.344843 | 0.082566 | 1 | 2.023740e-01 | 1 | 0.202374 | 0.236223 | NaN | NaN | NaN | NaN |
| 650 | 0.607709 | 0.261116 | 0 | 1.618992e-01 | 2 | 0.202374 | 0.234530 | NaN | NaN | NaN | NaN |
| 651 | 0.798229 | 0.765532 | 0 | 1.295194e-01 | 3 | 0.202374 | 0.232923 | NaN | NaN | NaN | NaN |
| 652 | 0.194003 | 0.020806 | 1 | 3.036155e-01 | 1 | 0.303615 | 0.236457 | NaN | NaN | NaN | NaN |
| 653 | 0.090950 | 0.030425 | 1 | 4.428924e-01 | 1 | 0.442892 | 0.246779 | NaN | NaN | NaN | NaN |
| 654 | 0.074391 | 0.532882 | 0 | 3.543139e-01 | 2 | 0.442892 | 0.256585 | NaN | NaN | NaN | NaN |
| 655 | 0.927285 | 0.859331 | 0 | 2.834511e-01 | 3 | 0.442892 | 0.265900 | NaN | NaN | NaN | NaN |
| 656 | 0.212892 | 0.688547 | 0 | 2.267609e-01 | 4 | 0.442892 | 0.274750 | NaN | NaN | NaN | NaN |
| 657 | 0.398261 | 0.533476 | 0 | 1.814087e-01 | 5 | 0.442892 | 0.283157 | NaN | NaN | NaN | NaN |
| 658 | 0.479445 | 0.470084 | 0 | 1.451270e-01 | 6 | 0.442892 | 0.291144 | NaN | NaN | NaN | NaN |
| 659 | 0.143990 | 0.148601 | 0 | 1.161016e-01 | 7 | 0.442892 | 0.298731 | NaN | NaN | NaN | NaN |
| 660 | 0.408680 | 0.538037 | 0 | 9.288127e-02 | 8 | 0.442892 | 0.305939 | NaN | NaN | NaN | NaN |
| 661 | 0.376705 | 0.907811 | 0 | 7.430501e-02 | 9 | 0.442892 | 0.312787 | NaN | NaN | NaN | NaN |
| 662 | 0.173142 | 0.849698 | 0 | 5.944401e-02 | 10 | 0.442892 | 0.319292 | NaN | NaN | NaN | NaN |
| 663 | 0.668847 | 0.687179 | 0 | 4.755521e-02 | 11 | 0.442892 | 0.325472 | NaN | NaN | NaN | NaN |
| 664 | 0.398154 | 0.794978 | 0 | 3.804417e-02 | 12 | 0.442892 | 0.331343 | NaN | NaN | NaN | NaN |
| 665 | 0.424017 | 0.783497 | 0 | 3.043533e-02 | 13 | 0.442892 | 0.336921 | NaN | NaN | NaN | NaN |
| 666 | 0.281237 | 0.822480 | 0 | 2.434827e-02 | 14 | 0.442892 | 0.342219 | NaN | NaN | NaN | NaN |
| 667 | 0.203566 | 0.885427 | 0 | 1.947861e-02 | 15 | 0.442892 | 0.347253 | NaN | NaN | NaN | NaN |
| 668 | 0.955183 | 0.044176 | 1 | 2.155829e-01 | 1 | 0.215583 | 0.340669 | NaN | NaN | NaN | NaN |
| 669 | 0.114213 | 0.378805 | 0 | 1.724663e-01 | 2 | 0.215583 | 0.334415 | NaN | NaN | NaN | NaN |
| 670 | 0.944462 | 0.422865 | 0 | 1.379730e-01 | 3 | 0.215583 | 0.328473 | NaN | NaN | NaN | NaN |
| 671 | 0.136579 | 0.589182 | 0 | 1.103784e-01 | 4 | 0.215583 | 0.322829 | NaN | NaN | NaN | NaN |
| 672 | 0.156651 | 0.324394 | 0 | 8.830275e-02 | 5 | 0.215583 | 0.317467 | NaN | NaN | NaN | NaN |
| 673 | 0.033363 | 0.480999 | 0 | 7.064220e-02 | 6 | 0.215583 | 0.312372 | NaN | NaN | NaN | NaN |
| 674 | 0.074294 | 0.059091 | 1 | 2.565138e-01 | 1 | 0.256514 | 0.309579 | NaN | NaN | NaN | NaN |
| 675 | 0.589476 | 0.439501 | 0 | 2.052110e-01 | 2 | 0.256514 | 0.306926 | NaN | NaN | NaN | NaN |
| 676 | 0.571210 | 0.537061 | 0 | 1.641688e-01 | 3 | 0.256514 | 0.304406 | NaN | NaN | NaN | NaN |
| 677 | 0.753467 | 0.840994 | 0 | 1.313350e-01 | 4 | 0.256514 | 0.302011 | NaN | NaN | NaN | NaN |
| 678 | 0.177379 | 0.953779 | 0 | 1.050680e-01 | 5 | 0.256514 | 0.299736 | NaN | NaN | NaN | NaN |
| 679 | 0.446846 | 0.217089 | 0 | 8.405443e-02 | 6 | 0.256514 | 0.297575 | NaN | NaN | NaN | NaN |
| 680 | 0.217582 | 0.030188 | 1 | 2.672435e-01 | 1 | 0.267244 | 0.296058 | NaN | NaN | NaN | NaN |
| 681 | 0.640152 | 0.502649 | 0 | 2.137948e-01 | 2 | 0.267244 | 0.294618 | NaN | NaN | NaN | NaN |
| 682 | 0.313712 | 0.420268 | 0 | 1.710359e-01 | 3 | 0.267244 | 0.293249 | NaN | NaN | NaN | NaN |
| 683 | 0.845014 | 0.454395 | 0 | 1.368287e-01 | 4 | 0.267244 | 0.291949 | NaN | NaN | NaN | NaN |
| 684 | 0.484941 | 0.524524 | 0 | 1.094630e-01 | 5 | 0.267244 | 0.290713 | NaN | NaN | NaN | NaN |
| 685 | 0.601042 | 0.182235 | 0 | 8.757036e-02 | 6 | 0.267244 | 0.289540 | NaN | NaN | NaN | NaN |
| 686 | 0.922613 | 0.806267 | 0 | 7.005629e-02 | 7 | 0.267244 | 0.288425 | NaN | NaN | NaN | NaN |
| 687 | 0.334422 | 0.458720 | 0 | 5.604503e-02 | 8 | 0.267244 | 0.287366 | NaN | NaN | NaN | NaN |
| 688 | 0.329970 | 0.385871 | 0 | 4.483603e-02 | 9 | 0.267244 | 0.286360 | NaN | NaN | NaN | NaN |
| 689 | 0.199004 | 0.189529 | 0 | 3.586882e-02 | 10 | 0.267244 | 0.285404 | NaN | NaN | NaN | NaN |
| 690 | 0.075731 | 0.913944 | 0 | 2.869506e-02 | 11 | 0.267244 | 0.284496 | NaN | NaN | NaN | NaN |
| 691 | 0.075933 | 0.031282 | 1 | 2.229560e-01 | 1 | 0.222956 | 0.281419 | NaN | NaN | NaN | NaN |
| 692 | 0.843544 | 0.615678 | 0 | 1.783648e-01 | 2 | 0.222956 | 0.278496 | NaN | NaN | NaN | NaN |
| 693 | 0.778147 | 0.539271 | 0 | 1.426919e-01 | 3 | 0.222956 | 0.275719 | NaN | NaN | NaN | NaN |
| 694 | 0.697761 | 0.714345 | 0 | 1.141535e-01 | 4 | 0.222956 | 0.273081 | NaN | NaN | NaN | NaN |
| 695 | 0.983048 | 0.590026 | 0 | 9.132280e-02 | 5 | 0.222956 | 0.270575 | NaN | NaN | NaN | NaN |
| 696 | 0.714505 | 0.831415 | 0 | 7.305824e-02 | 6 | 0.222956 | 0.268194 | NaN | NaN | NaN | NaN |
| 697 | 0.380309 | 0.840161 | 0 | 5.844659e-02 | 7 | 0.222956 | 0.265932 | NaN | NaN | NaN | NaN |
| 698 | 0.433240 | 0.214094 | 0 | 4.675727e-02 | 8 | 0.222956 | 0.263783 | NaN | NaN | NaN | NaN |
| 699 | 0.680086 | 0.108080 | 0 | 3.740582e-02 | 9 | 0.222956 | 0.261742 | NaN | NaN | NaN | NaN |
| 700 | 0.208873 | 0.938913 | 0 | 2.992465e-02 | 10 | 0.222956 | 0.259802 | NaN | NaN | NaN | NaN |
| 701 | 0.265896 | 0.268316 | 0 | 2.393972e-02 | 11 | 0.222956 | 0.257960 | NaN | NaN | NaN | NaN |
| 702 | 0.131757 | 0.403598 | 0 | 1.915178e-02 | 12 | 0.222956 | 0.256210 | NaN | NaN | NaN | NaN |
| 703 | 0.510598 | 0.265105 | 0 | 1.532142e-02 | 13 | 0.222956 | 0.254547 | NaN | NaN | NaN | NaN |
| 704 | 0.029859 | 0.160764 | 0 | 1.225714e-02 | 14 | 0.222956 | 0.252968 | NaN | NaN | NaN | NaN |
| 705 | 0.795341 | 0.433077 | 0 | 9.805711e-03 | 15 | 0.222956 | 0.251467 | NaN | NaN | NaN | NaN |
| 706 | 0.374072 | 0.318522 | 0 | 7.844568e-03 | 16 | 0.222956 | 0.250041 | NaN | NaN | NaN | NaN |
| 707 | 0.600809 | 0.475378 | 0 | 6.275655e-03 | 17 | 0.222956 | 0.248687 | NaN | NaN | NaN | NaN |
| 708 | 0.827402 | 0.578026 | 0 | 5.020524e-03 | 18 | 0.222956 | 0.247401 | NaN | NaN | NaN | NaN |
| 709 | 0.276073 | 0.225281 | 0 | 4.016419e-03 | 19 | 0.222956 | 0.246178 | NaN | NaN | NaN | NaN |
| 710 | 0.068134 | 0.380106 | 0 | 3.213135e-03 | 20 | 0.222956 | 0.245017 | NaN | NaN | NaN | NaN |
| 711 | 0.159634 | 0.004324 | 1 | 2.025705e-01 | 1 | 0.202571 | 0.242895 | NaN | NaN | NaN | NaN |
| 712 | 0.185497 | 0.366926 | 0 | 1.620564e-01 | 2 | 0.202571 | 0.240879 | NaN | NaN | NaN | NaN |
| 713 | 0.134752 | 0.801604 | 0 | 1.296451e-01 | 3 | 0.202571 | 0.238963 | NaN | NaN | NaN | NaN |
| 714 | 0.906617 | 0.344900 | 0 | 1.037161e-01 | 4 | 0.202571 | 0.237144 | NaN | NaN | NaN | NaN |
| 715 | 0.779833 | 0.214289 | 0 | 8.297288e-02 | 5 | 0.202571 | 0.235415 | NaN | NaN | NaN | NaN |
| 716 | 0.631419 | 0.467877 | 0 | 6.637830e-02 | 6 | 0.202571 | 0.233773 | NaN | NaN | NaN | NaN |
| 717 | 0.435692 | 0.703279 | 0 | 5.310264e-02 | 7 | 0.202571 | 0.232213 | NaN | NaN | NaN | NaN |
| 718 | 0.396618 | 0.390822 | 0 | 4.248211e-02 | 8 | 0.202571 | 0.230731 | NaN | NaN | NaN | NaN |
| 719 | 0.494112 | 0.090704 | 1 | 2.339857e-01 | 1 | 0.233986 | 0.230893 | NaN | NaN | NaN | NaN |
| 720 | 0.583012 | 0.511060 | 0 | 1.871886e-01 | 2 | 0.233986 | 0.231048 | NaN | NaN | NaN | NaN |
| 721 | 0.333750 | 0.733510 | 0 | 1.497508e-01 | 3 | 0.233986 | 0.231195 | NaN | NaN | NaN | NaN |
| 722 | 0.247277 | 0.093955 | 1 | 3.198007e-01 | 1 | 0.319801 | 0.235625 | NaN | NaN | NaN | NaN |
| 723 | 0.735494 | 0.591409 | 0 | 2.558405e-01 | 2 | 0.319801 | 0.239834 | NaN | NaN | NaN | NaN |
| 724 | 0.178517 | 0.440999 | 0 | 2.046724e-01 | 3 | 0.319801 | 0.243832 | NaN | NaN | NaN | NaN |
| 725 | 0.523605 | 0.625081 | 0 | 1.637379e-01 | 4 | 0.319801 | 0.247631 | NaN | NaN | NaN | NaN |
| 726 | 0.132584 | 0.309295 | 0 | 1.309904e-01 | 5 | 0.319801 | 0.251239 | NaN | NaN | NaN | NaN |
| 727 | 0.153045 | 0.034727 | 1 | 3.047923e-01 | 1 | 0.304792 | 0.253917 | NaN | NaN | NaN | NaN |
| 728 | 0.618025 | 0.431940 | 0 | 2.438338e-01 | 2 | 0.304792 | 0.256461 | NaN | NaN | NaN | NaN |
| 729 | 0.127226 | 0.718179 | 0 | 1.950671e-01 | 3 | 0.304792 | 0.258877 | NaN | NaN | NaN | NaN |
| 730 | 0.234307 | 0.258712 | 0 | 1.560536e-01 | 4 | 0.304792 | 0.261173 | NaN | NaN | NaN | NaN |
| 731 | 0.442035 | 0.696013 | 0 | 1.248429e-01 | 5 | 0.304792 | 0.263354 | NaN | NaN | NaN | NaN |
| 732 | 0.986404 | 0.366537 | 0 | 9.987434e-02 | 6 | 0.304792 | 0.265426 | NaN | NaN | NaN | NaN |
| 733 | 0.747468 | 0.838162 | 0 | 7.989947e-02 | 7 | 0.304792 | 0.267394 | NaN | NaN | NaN | NaN |
| 734 | 0.513911 | 0.450659 | 0 | 6.391957e-02 | 8 | 0.304792 | 0.269264 | NaN | NaN | NaN | NaN |
| 735 | 0.961889 | 0.017720 | 1 | 2.511357e-01 | 1 | 0.251136 | 0.268358 | NaN | NaN | NaN | NaN |
| 736 | 0.524671 | 0.362237 | 0 | 2.009085e-01 | 2 | 0.251136 | 0.267497 | NaN | NaN | NaN | NaN |
| 737 | 0.608115 | 0.313954 | 0 | 1.607268e-01 | 3 | 0.251136 | 0.266678 | NaN | NaN | NaN | NaN |
| 738 | 0.362566 | 0.408708 | 0 | 1.285815e-01 | 4 | 0.251136 | 0.265901 | NaN | NaN | NaN | NaN |
| 739 | 0.935774 | 0.354661 | 0 | 1.028652e-01 | 5 | 0.251136 | 0.265163 | NaN | NaN | NaN | NaN |
| 740 | 0.970073 | 0.572954 | 0 | 8.229213e-02 | 6 | 0.251136 | 0.264462 | NaN | NaN | NaN | NaN |
| 741 | 0.799320 | 0.610020 | 0 | 6.583371e-02 | 7 | 0.251136 | 0.263795 | NaN | NaN | NaN | NaN |
| 742 | 0.134755 | 0.569792 | 0 | 5.266697e-02 | 8 | 0.251136 | 0.263162 | NaN | NaN | NaN | NaN |
| 743 | 0.452438 | 0.973969 | 0 | 4.213357e-02 | 9 | 0.251136 | 0.262561 | NaN | NaN | NaN | NaN |
| 744 | 0.894707 | 0.767993 | 0 | 3.370686e-02 | 10 | 0.251136 | 0.261990 | NaN | NaN | NaN | NaN |
| 745 | 0.652274 | 0.358323 | 0 | 2.696549e-02 | 11 | 0.251136 | 0.261447 | NaN | NaN | NaN | NaN |
| 746 | 0.083703 | 0.128061 | 0 | 2.157239e-02 | 12 | 0.251136 | 0.260932 | NaN | NaN | NaN | NaN |
| 747 | 0.323920 | 0.108367 | 0 | 1.725791e-02 | 13 | 0.251136 | 0.260442 | NaN | NaN | NaN | NaN |
| 748 | 0.938359 | 0.995887 | 0 | 1.380633e-02 | 14 | 0.251136 | 0.259976 | NaN | NaN | NaN | NaN |
| 749 | 0.178078 | 0.671387 | 0 | 1.104506e-02 | 15 | 0.251136 | 0.259534 | NaN | NaN | NaN | NaN |
| 750 | 0.385792 | 0.046538 | 1 | 2.088361e-01 | 1 | 0.208836 | 0.256999 | NaN | NaN | NaN | NaN |
| 751 | 0.092006 | 0.221727 | 0 | 1.670688e-01 | 2 | 0.208836 | 0.254591 | NaN | NaN | NaN | NaN |
| 752 | 0.453274 | 0.977710 | 0 | 1.336551e-01 | 3 | 0.208836 | 0.252304 | NaN | NaN | NaN | NaN |
| 753 | 0.323157 | 0.493593 | 0 | 1.069241e-01 | 4 | 0.208836 | 0.250130 | NaN | NaN | NaN | NaN |
| 754 | 0.266325 | 0.936331 | 0 | 8.553925e-02 | 5 | 0.208836 | 0.248065 | NaN | NaN | NaN | NaN |
| 755 | 0.121819 | 0.287476 | 0 | 6.843140e-02 | 6 | 0.208836 | 0.246104 | NaN | NaN | NaN | NaN |
| 756 | 0.356916 | 0.742571 | 0 | 5.474512e-02 | 7 | 0.208836 | 0.244241 | NaN | NaN | NaN | NaN |
| 757 | 0.517215 | 0.405027 | 0 | 4.379609e-02 | 8 | 0.208836 | 0.242470 | NaN | NaN | NaN | NaN |
| 758 | 0.720437 | 0.011916 | 1 | 2.350369e-01 | 1 | 0.235037 | 0.242099 | NaN | NaN | NaN | NaN |
| 759 | 0.772684 | 0.803264 | 0 | 1.880295e-01 | 2 | 0.235037 | 0.241746 | NaN | NaN | NaN | NaN |
| 760 | 0.923343 | 0.417461 | 0 | 1.504236e-01 | 3 | 0.235037 | 0.241410 | NaN | NaN | NaN | NaN |
| 761 | 0.619573 | 0.730711 | 0 | 1.203389e-01 | 4 | 0.235037 | 0.241091 | NaN | NaN | NaN | NaN |
| 762 | 0.960662 | 0.871053 | 0 | 9.627110e-02 | 5 | 0.235037 | 0.240789 | NaN | NaN | NaN | NaN |
| 763 | 0.094416 | 0.469429 | 0 | 7.701688e-02 | 6 | 0.235037 | 0.240501 | NaN | NaN | NaN | NaN |
| 764 | 0.834634 | 0.014231 | 1 | 2.616135e-01 | 1 | 0.261614 | 0.241557 | NaN | NaN | NaN | NaN |
| 765 | 0.905912 | 0.027747 | 1 | 4.092908e-01 | 1 | 0.409291 | 0.249943 | NaN | NaN | NaN | NaN |
| 766 | 0.516592 | 0.419211 | 0 | 3.274326e-01 | 2 | 0.409291 | 0.257911 | NaN | NaN | NaN | NaN |
| 767 | 0.361447 | 0.944117 | 0 | 2.619461e-01 | 3 | 0.409291 | 0.265480 | NaN | NaN | NaN | NaN |
| 768 | 0.060876 | 0.518424 | 0 | 2.095569e-01 | 4 | 0.409291 | 0.272670 | NaN | NaN | NaN | NaN |
| 769 | 0.179792 | 0.023888 | 1 | 3.676455e-01 | 1 | 0.367646 | 0.277419 | NaN | NaN | NaN | NaN |
| 770 | 0.862276 | 0.860860 | 0 | 2.941164e-01 | 2 | 0.367646 | 0.281930 | NaN | NaN | NaN | NaN |
| 771 | 0.027700 | 0.854543 | 0 | 2.352931e-01 | 3 | 0.367646 | 0.286216 | NaN | NaN | NaN | NaN |
| 772 | 0.040554 | 0.577860 | 0 | 1.882345e-01 | 4 | 0.367646 | 0.290288 | NaN | NaN | NaN | NaN |
| 773 | 0.441953 | 0.863295 | 0 | 1.505876e-01 | 5 | 0.367646 | 0.294156 | NaN | NaN | NaN | NaN |
| 774 | 0.553443 | 0.313857 | 0 | 1.204701e-01 | 6 | 0.367646 | 0.297830 | NaN | NaN | NaN | NaN |
| 775 | 0.361892 | 0.291704 | 0 | 9.637607e-02 | 7 | 0.367646 | 0.301321 | NaN | NaN | NaN | NaN |
| 776 | 0.192734 | 0.613242 | 0 | 7.710085e-02 | 8 | 0.367646 | 0.304637 | NaN | NaN | NaN | NaN |
| 777 | 0.805310 | 0.078680 | 1 | 2.616807e-01 | 1 | 0.261681 | 0.302489 | NaN | NaN | NaN | NaN |
| 778 | 0.119328 | 0.268104 | 0 | 2.093445e-01 | 2 | 0.261681 | 0.300449 | NaN | NaN | NaN | NaN |
| 779 | 0.105936 | 0.344988 | 0 | 1.674756e-01 | 3 | 0.261681 | 0.298510 | NaN | NaN | NaN | NaN |
| 780 | 0.008278 | 0.228770 | 0 | 1.339805e-01 | 4 | 0.261681 | 0.296669 | NaN | NaN | NaN | NaN |
| 781 | 0.504659 | 0.053796 | 1 | 3.071844e-01 | 1 | 0.307184 | 0.297195 | NaN | NaN | NaN | NaN |
| 782 | 0.372835 | 0.806021 | 0 | 2.457475e-01 | 2 | 0.307184 | 0.297694 | NaN | NaN | NaN | NaN |
| 783 | 0.988397 | 0.843444 | 0 | 1.965980e-01 | 3 | 0.307184 | 0.298169 | NaN | NaN | NaN | NaN |
| 784 | 0.839361 | 0.387623 | 0 | 1.572784e-01 | 4 | 0.307184 | 0.298619 | NaN | NaN | NaN | NaN |
| 785 | 0.917517 | 0.866191 | 0 | 1.258227e-01 | 5 | 0.307184 | 0.299048 | NaN | NaN | NaN | NaN |
| 786 | 0.377948 | 0.229873 | 0 | 1.006582e-01 | 6 | 0.307184 | 0.299455 | NaN | NaN | NaN | NaN |
| 787 | 0.820438 | 0.362100 | 0 | 8.052655e-02 | 7 | 0.307184 | 0.299841 | NaN | NaN | NaN | NaN |
| 788 | 0.034934 | 0.935341 | 0 | 6.442124e-02 | 8 | 0.307184 | 0.300208 | NaN | NaN | NaN | NaN |
| 789 | 0.486131 | 0.307378 | 0 | 5.153699e-02 | 9 | 0.307184 | 0.300557 | NaN | NaN | NaN | NaN |
| 790 | 0.044768 | 0.499782 | 0 | 4.122959e-02 | 10 | 0.307184 | 0.300888 | NaN | NaN | NaN | NaN |
| 791 | 0.203467 | 0.724557 | 0 | 3.298367e-02 | 11 | 0.307184 | 0.301203 | NaN | NaN | NaN | NaN |
| 792 | 0.254280 | 0.703586 | 0 | 2.638694e-02 | 12 | 0.307184 | 0.301502 | NaN | NaN | NaN | NaN |
| 793 | 0.310587 | 0.566043 | 0 | 2.110955e-02 | 13 | 0.307184 | 0.301786 | NaN | NaN | NaN | NaN |
| 794 | 0.210233 | 0.676320 | 0 | 1.688764e-02 | 14 | 0.307184 | 0.302056 | NaN | NaN | NaN | NaN |
| 795 | 0.585692 | 0.687196 | 0 | 1.351011e-02 | 15 | 0.307184 | 0.302313 | NaN | NaN | NaN | NaN |
| 796 | 0.631710 | 0.607360 | 0 | 1.080809e-02 | 16 | 0.307184 | 0.302556 | NaN | NaN | NaN | NaN |
| 797 | 0.969088 | 0.529651 | 0 | 8.646472e-03 | 17 | 0.307184 | 0.302788 | NaN | NaN | NaN | NaN |
| 798 | 0.106532 | 0.382830 | 0 | 6.917178e-03 | 18 | 0.307184 | 0.303008 | NaN | NaN | NaN | NaN |
| 799 | 0.519066 | 0.225681 | 0 | 5.533742e-03 | 19 | 0.307184 | 0.303216 | NaN | NaN | NaN | NaN |
| 800 | 0.962428 | 0.860752 | 0 | 4.426994e-03 | 20 | 0.307184 | 0.303415 | NaN | NaN | NaN | NaN |
| 801 | 0.813834 | 0.910773 | 0 | 3.541595e-03 | 21 | 0.307184 | 0.303603 | NaN | NaN | NaN | NaN |
| 802 | 0.319410 | 0.155202 | 0 | 2.833276e-03 | 22 | 0.307184 | 0.303782 | NaN | NaN | NaN | NaN |
| 803 | 0.488585 | 0.861042 | 0 | 2.266621e-03 | 23 | 0.307184 | 0.303952 | NaN | NaN | NaN | NaN |
| 804 | 0.232998 | 0.679368 | 0 | 1.813297e-03 | 24 | 0.307184 | 0.304114 | NaN | NaN | NaN | NaN |
| 805 | 0.589583 | 0.436692 | 0 | 1.450637e-03 | 25 | 0.307184 | 0.304268 | NaN | NaN | NaN | NaN |
| 806 | 0.695023 | 0.430579 | 0 | 1.160510e-03 | 26 | 0.307184 | 0.304413 | NaN | NaN | NaN | NaN |
| 807 | 0.612698 | 0.760479 | 0 | 9.284079e-04 | 27 | 0.307184 | 0.304552 | NaN | NaN | NaN | NaN |
| 808 | 0.629359 | 0.612091 | 0 | 7.427263e-04 | 28 | 0.307184 | 0.304684 | NaN | NaN | NaN | NaN |
| 809 | 0.726855 | 0.154321 | 0 | 5.941811e-04 | 29 | 0.307184 | 0.304809 | NaN | NaN | NaN | NaN |
| 810 | 0.166681 | 0.841543 | 0 | 4.753448e-04 | 30 | 0.307184 | 0.304927 | NaN | NaN | NaN | NaN |
| 811 | 0.846542 | 0.927131 | 0 | 3.802759e-04 | 31 | 0.307184 | 0.305040 | NaN | NaN | NaN | NaN |
| 812 | 0.621170 | 0.950411 | 0 | 3.042207e-04 | 32 | 0.307184 | 0.305147 | NaN | NaN | NaN | NaN |
| 813 | 0.072871 | 0.497192 | 0 | 2.433766e-04 | 33 | 0.307184 | 0.305249 | NaN | NaN | NaN | NaN |
| 814 | 0.141764 | 0.428597 | 0 | 1.947012e-04 | 34 | 0.307184 | 0.305346 | NaN | NaN | NaN | NaN |
| 815 | 0.059038 | 0.653383 | 0 | 1.557610e-04 | 35 | 0.307184 | 0.305438 | NaN | NaN | NaN | NaN |
| 816 | 0.843359 | 0.500534 | 0 | 1.246088e-04 | 36 | 0.307184 | 0.305525 | NaN | NaN | NaN | NaN |
| 817 | 0.140699 | 0.137251 | 0 | 9.968704e-05 | 37 | 0.307184 | 0.305608 | NaN | NaN | NaN | NaN |
| 818 | 0.914303 | 0.361312 | 0 | 7.974963e-05 | 38 | 0.307184 | 0.305687 | NaN | NaN | NaN | NaN |
| 819 | 0.500335 | 0.553932 | 0 | 6.379971e-05 | 39 | 0.307184 | 0.305762 | NaN | NaN | NaN | NaN |
| 820 | 0.274028 | 0.371610 | 0 | 5.103976e-05 | 40 | 0.307184 | 0.305833 | NaN | NaN | NaN | NaN |
| 821 | 0.180718 | 0.801421 | 0 | 4.083181e-05 | 41 | 0.307184 | 0.305901 | NaN | NaN | NaN | NaN |
| 822 | 0.550160 | 0.767274 | 0 | 3.266545e-05 | 42 | 0.307184 | 0.305965 | NaN | NaN | NaN | NaN |
| 823 | 0.727876 | 0.917628 | 0 | 2.613236e-05 | 43 | 0.307184 | 0.306026 | NaN | NaN | NaN | NaN |
| 824 | 0.642484 | 0.332848 | 0 | 2.090589e-05 | 44 | 0.307184 | 0.306084 | NaN | NaN | NaN | NaN |
| 825 | 0.508384 | 0.171375 | 0 | 1.672471e-05 | 45 | 0.307184 | 0.306139 | NaN | NaN | NaN | NaN |
| 826 | 0.829412 | 0.308049 | 0 | 1.337977e-05 | 46 | 0.307184 | 0.306191 | NaN | NaN | NaN | NaN |
| 827 | 0.017364 | 0.821259 | 0 | 1.070381e-05 | 47 | 0.307184 | 0.306241 | NaN | NaN | NaN | NaN |
| 828 | 0.091948 | 0.722949 | 0 | 8.563051e-06 | 48 | 0.307184 | 0.306288 | NaN | NaN | NaN | NaN |
| 829 | 0.558430 | 0.704674 | 0 | 6.850441e-06 | 49 | 0.307184 | 0.306333 | NaN | NaN | NaN | NaN |
| 830 | 0.124536 | 0.212617 | 0 | 5.480353e-06 | 50 | 0.307184 | 0.306375 | NaN | NaN | NaN | NaN |
| 831 | 0.649163 | 0.433752 | 0 | 4.384282e-06 | 51 | 0.307184 | 0.306416 | NaN | NaN | NaN | NaN |
| 832 | 0.868574 | 0.857193 | 0 | 3.507426e-06 | 52 | 0.307184 | 0.306454 | NaN | NaN | NaN | NaN |
| 833 | 0.078006 | 0.716428 | 0 | 2.805941e-06 | 53 | 0.307184 | 0.306491 | NaN | NaN | NaN | NaN |
| 834 | 0.543140 | 0.581317 | 0 | 2.244753e-06 | 54 | 0.307184 | 0.306525 | NaN | NaN | NaN | NaN |
| 835 | 0.231167 | 0.205921 | 0 | 1.795802e-06 | 55 | 0.307184 | 0.306558 | NaN | NaN | NaN | NaN |
| 836 | 0.211761 | 0.370694 | 0 | 1.436642e-06 | 56 | 0.307184 | 0.306590 | NaN | NaN | NaN | NaN |
| 837 | 0.719881 | 0.342835 | 0 | 1.149313e-06 | 57 | 0.307184 | 0.306619 | NaN | NaN | NaN | NaN |
| 838 | 0.270463 | 0.907093 | 0 | 9.194507e-07 | 58 | 0.307184 | 0.306648 | NaN | NaN | NaN | NaN |
| 839 | 0.395947 | 0.188683 | 0 | 7.355605e-07 | 59 | 0.307184 | 0.306674 | NaN | NaN | NaN | NaN |
| 840 | 0.680252 | 0.960747 | 0 | 5.884484e-07 | 60 | 0.307184 | 0.306700 | NaN | NaN | NaN | NaN |
| 841 | 0.051756 | 0.071449 | 1 | 2.000005e-01 | 1 | 0.200000 | 0.301365 | NaN | NaN | NaN | NaN |
| 842 | 0.809545 | 0.925902 | 0 | 1.600004e-01 | 2 | 0.200000 | 0.296297 | NaN | NaN | NaN | NaN |
| 843 | 0.792968 | 0.551810 | 0 | 1.280003e-01 | 3 | 0.200000 | 0.291482 | NaN | NaN | NaN | NaN |
| 844 | 0.864394 | 0.546839 | 0 | 1.024002e-01 | 4 | 0.200000 | 0.286908 | NaN | NaN | NaN | NaN |
| 845 | 0.658821 | 0.367745 | 0 | 8.192019e-02 | 5 | 0.200000 | 0.282563 | NaN | NaN | NaN | NaN |
| 846 | 0.735923 | 0.104414 | 0 | 6.553615e-02 | 6 | 0.200000 | 0.278434 | NaN | NaN | NaN | NaN |
| 847 | 0.285965 | 0.485613 | 0 | 5.242892e-02 | 7 | 0.200000 | 0.274513 | NaN | NaN | NaN | NaN |
| 848 | 0.806963 | 0.953836 | 0 | 4.194314e-02 | 8 | 0.200000 | 0.270787 | NaN | NaN | NaN | NaN |
| 849 | 0.584098 | 0.553535 | 0 | 3.355451e-02 | 9 | 0.200000 | 0.267248 | NaN | NaN | NaN | NaN |
| 850 | 0.658892 | 0.300669 | 0 | 2.684361e-02 | 10 | 0.200000 | 0.263885 | NaN | NaN | NaN | NaN |
| 851 | 0.661019 | 0.059575 | 1 | 2.214749e-01 | 1 | 0.221475 | 0.261765 | NaN | NaN | NaN | NaN |
| 852 | 0.483299 | 0.842002 | 0 | 1.771799e-01 | 2 | 0.221475 | 0.259750 | NaN | NaN | NaN | NaN |
| 853 | 0.824751 | 0.500003 | 0 | 1.417439e-01 | 3 | 0.221475 | 0.257837 | NaN | NaN | NaN | NaN |
| 854 | 0.312837 | 0.392182 | 0 | 1.133951e-01 | 4 | 0.221475 | 0.256019 | NaN | NaN | NaN | NaN |
| 855 | 0.952691 | 0.284771 | 0 | 9.071611e-02 | 5 | 0.221475 | 0.254291 | NaN | NaN | NaN | NaN |
| 856 | 0.376060 | 0.756935 | 0 | 7.257289e-02 | 6 | 0.221475 | 0.252651 | NaN | NaN | NaN | NaN |
| 857 | 0.982402 | 0.886612 | 0 | 5.805831e-02 | 7 | 0.221475 | 0.251092 | NaN | NaN | NaN | NaN |
| 858 | 0.089810 | 0.955966 | 0 | 4.644665e-02 | 8 | 0.221475 | 0.249611 | NaN | NaN | NaN | NaN |
| 859 | 0.703535 | 0.581054 | 0 | 3.715732e-02 | 9 | 0.221475 | 0.248204 | NaN | NaN | NaN | NaN |
| 860 | 0.520716 | 0.853155 | 0 | 2.972586e-02 | 10 | 0.221475 | 0.246868 | NaN | NaN | NaN | NaN |
| 861 | 0.451642 | 0.746868 | 0 | 2.378068e-02 | 11 | 0.221475 | 0.245598 | NaN | NaN | NaN | NaN |
| 862 | 0.868489 | 0.406291 | 0 | 1.902455e-02 | 12 | 0.221475 | 0.244392 | NaN | NaN | NaN | NaN |
| 863 | 0.086597 | 0.085293 | 1 | 2.152196e-01 | 1 | 0.215220 | 0.242933 | NaN | NaN | NaN | NaN |
| 864 | 0.394994 | 0.056992 | 1 | 3.721757e-01 | 1 | 0.372176 | 0.249395 | NaN | NaN | NaN | NaN |
| 865 | 0.723317 | 0.772883 | 0 | 2.977406e-01 | 2 | 0.372176 | 0.255534 | NaN | NaN | NaN | NaN |
| 866 | 0.694860 | 0.348498 | 0 | 2.381925e-01 | 3 | 0.372176 | 0.261366 | NaN | NaN | NaN | NaN |
| 867 | 0.840993 | 0.753602 | 0 | 1.905540e-01 | 4 | 0.372176 | 0.266907 | NaN | NaN | NaN | NaN |
| 868 | 0.678786 | 0.177619 | 0 | 1.524432e-01 | 5 | 0.372176 | 0.272170 | NaN | NaN | NaN | NaN |
| 869 | 0.477772 | 0.382925 | 0 | 1.219545e-01 | 6 | 0.372176 | 0.277171 | NaN | NaN | NaN | NaN |
| 870 | 0.726371 | 0.290992 | 0 | 9.756363e-02 | 7 | 0.372176 | 0.281921 | NaN | NaN | NaN | NaN |
| 871 | 0.397438 | 0.008303 | 1 | 2.780509e-01 | 1 | 0.278051 | 0.281727 | NaN | NaN | NaN | NaN |
| 872 | 0.220612 | 0.749435 | 0 | 2.224407e-01 | 2 | 0.278051 | 0.281544 | NaN | NaN | NaN | NaN |
| 873 | 0.148155 | 0.869616 | 0 | 1.779526e-01 | 3 | 0.278051 | 0.281369 | NaN | NaN | NaN | NaN |
| 874 | 0.864050 | 0.272570 | 0 | 1.423621e-01 | 4 | 0.278051 | 0.281203 | NaN | NaN | NaN | NaN |
| 875 | 0.403585 | 0.759487 | 0 | 1.138897e-01 | 5 | 0.278051 | 0.281045 | NaN | NaN | NaN | NaN |
| 876 | 0.512551 | 0.194710 | 0 | 9.111172e-02 | 6 | 0.278051 | 0.280896 | NaN | NaN | NaN | NaN |
| 877 | 0.544982 | 0.041152 | 1 | 2.728894e-01 | 1 | 0.272889 | 0.280495 | NaN | NaN | NaN | NaN |
| 878 | 0.665992 | 0.408538 | 0 | 2.183115e-01 | 2 | 0.272889 | 0.280115 | NaN | NaN | NaN | NaN |
| 879 | 0.098314 | 0.991407 | 0 | 1.746492e-01 | 3 | 0.272889 | 0.279754 | NaN | NaN | NaN | NaN |
| 880 | 0.597616 | 0.232307 | 0 | 1.397194e-01 | 4 | 0.272889 | 0.279411 | NaN | NaN | NaN | NaN |
| 881 | 0.950576 | 0.643917 | 0 | 1.117755e-01 | 5 | 0.272889 | 0.279085 | NaN | NaN | NaN | NaN |
| 882 | 0.460817 | 0.836602 | 0 | 8.942039e-02 | 6 | 0.272889 | 0.278775 | NaN | NaN | NaN | NaN |
| 883 | 0.629593 | 0.745497 | 0 | 7.153631e-02 | 7 | 0.272889 | 0.278480 | NaN | NaN | NaN | NaN |
| 884 | 0.611877 | 0.326448 | 0 | 5.722905e-02 | 8 | 0.272889 | 0.278201 | NaN | NaN | NaN | NaN |
| 885 | 0.815607 | 0.512065 | 0 | 4.578324e-02 | 9 | 0.272889 | 0.277935 | NaN | NaN | NaN | NaN |
| 886 | 0.061174 | 0.052305 | 1 | 2.366266e-01 | 1 | 0.236627 | 0.275870 | NaN | NaN | NaN | NaN |
| 887 | 0.462311 | 0.254710 | 0 | 1.893013e-01 | 2 | 0.236627 | 0.273908 | NaN | NaN | NaN | NaN |
| 888 | 0.098204 | 0.368914 | 0 | 1.514410e-01 | 3 | 0.236627 | 0.272044 | NaN | NaN | NaN | NaN |
| 889 | 0.819848 | 0.828152 | 0 | 1.211528e-01 | 4 | 0.236627 | 0.270273 | NaN | NaN | NaN | NaN |
| 890 | 0.115017 | 0.163833 | 0 | 9.692225e-02 | 5 | 0.236627 | 0.268591 | NaN | NaN | NaN | NaN |
| 891 | 0.480484 | 0.187923 | 0 | 7.753780e-02 | 6 | 0.236627 | 0.266992 | NaN | NaN | NaN | NaN |
| 892 | 0.819321 | 0.718746 | 0 | 6.203024e-02 | 7 | 0.236627 | 0.265474 | NaN | NaN | NaN | NaN |
| 893 | 0.595391 | 0.098584 | 1 | 2.496242e-01 | 1 | 0.249624 | 0.264682 | NaN | NaN | NaN | NaN |
| 894 | 0.926367 | 0.167294 | 0 | 1.996994e-01 | 2 | 0.249624 | 0.263929 | NaN | NaN | NaN | NaN |
| 895 | 0.252488 | 0.448552 | 0 | 1.597595e-01 | 3 | 0.249624 | 0.263213 | NaN | NaN | NaN | NaN |
| 896 | 0.044928 | 0.185394 | 0 | 1.278076e-01 | 4 | 0.249624 | 0.262534 | NaN | NaN | NaN | NaN |
| 897 | 0.852969 | 0.448675 | 0 | 1.022461e-01 | 5 | 0.249624 | 0.261888 | NaN | NaN | NaN | NaN |
| 898 | 0.527445 | 0.946105 | 0 | 8.179686e-02 | 6 | 0.249624 | 0.261275 | NaN | NaN | NaN | NaN |
| 899 | 0.198490 | 0.738078 | 0 | 6.543748e-02 | 7 | 0.249624 | 0.260693 | NaN | NaN | NaN | NaN |
| 900 | 0.190983 | 0.534468 | 0 | 5.234999e-02 | 8 | 0.249624 | 0.260139 | NaN | NaN | NaN | NaN |
| 901 | 0.000634 | 0.624283 | 0 | 4.187999e-02 | 9 | 0.249624 | 0.259614 | NaN | NaN | NaN | NaN |
| 902 | 0.890511 | 0.331932 | 0 | 3.350399e-02 | 10 | 0.249624 | 0.259114 | NaN | NaN | NaN | NaN |
| 903 | 0.076001 | 0.143090 | 0 | 2.680319e-02 | 11 | 0.249624 | 0.258640 | NaN | NaN | NaN | NaN |
| 904 | 0.248792 | 0.619619 | 0 | 2.144255e-02 | 12 | 0.249624 | 0.258189 | NaN | NaN | NaN | NaN |
| 905 | 0.598933 | 0.650514 | 0 | 1.715404e-02 | 13 | 0.249624 | 0.257761 | NaN | NaN | NaN | NaN |
| 906 | 0.430435 | 0.229646 | 0 | 1.372324e-02 | 14 | 0.249624 | 0.257354 | NaN | NaN | NaN | NaN |
| 907 | 0.282472 | 0.333489 | 0 | 1.097859e-02 | 15 | 0.249624 | 0.256967 | NaN | NaN | NaN | NaN |
| 908 | 0.657370 | 0.299775 | 0 | 8.782870e-03 | 16 | 0.249624 | 0.256600 | NaN | NaN | NaN | NaN |
| 909 | 0.157889 | 0.442675 | 0 | 7.026296e-03 | 17 | 0.249624 | 0.256251 | NaN | NaN | NaN | NaN |
| 910 | 0.367993 | 0.505063 | 0 | 5.621037e-03 | 18 | 0.249624 | 0.255920 | NaN | NaN | NaN | NaN |
| 911 | 0.963144 | 0.569904 | 0 | 4.496830e-03 | 19 | 0.249624 | 0.255605 | NaN | NaN | NaN | NaN |
| 912 | 0.144639 | 0.887839 | 0 | 3.597464e-03 | 20 | 0.249624 | 0.255306 | NaN | NaN | NaN | NaN |
| 913 | 0.848411 | 0.790665 | 0 | 2.877971e-03 | 21 | 0.249624 | 0.255022 | NaN | NaN | NaN | NaN |
| 914 | 0.099041 | 0.061758 | 1 | 2.023024e-01 | 1 | 0.202302 | 0.252386 | NaN | NaN | NaN | NaN |
| 915 | 0.807825 | 0.609944 | 0 | 1.618419e-01 | 2 | 0.202302 | 0.249882 | NaN | NaN | NaN | NaN |
| 916 | 0.591300 | 0.995160 | 0 | 1.294735e-01 | 3 | 0.202302 | 0.247503 | NaN | NaN | NaN | NaN |
| 917 | 0.674461 | 0.045189 | 1 | 3.035788e-01 | 1 | 0.303579 | 0.250307 | NaN | NaN | NaN | NaN |
| 918 | 0.446201 | 0.292054 | 0 | 2.428631e-01 | 2 | 0.303579 | 0.252970 | NaN | NaN | NaN | NaN |
| 919 | 0.722075 | 0.775763 | 0 | 1.942904e-01 | 3 | 0.303579 | 0.255501 | NaN | NaN | NaN | NaN |
| 920 | 0.155837 | 0.285457 | 0 | 1.554324e-01 | 4 | 0.303579 | 0.257905 | NaN | NaN | NaN | NaN |
| 921 | 0.532141 | 0.522674 | 0 | 1.243459e-01 | 5 | 0.303579 | 0.260188 | NaN | NaN | NaN | NaN |
| 922 | 0.557359 | 0.877304 | 0 | 9.947671e-02 | 6 | 0.303579 | 0.262358 | NaN | NaN | NaN | NaN |
| 923 | 0.266234 | 0.899530 | 0 | 7.958137e-02 | 7 | 0.303579 | 0.264419 | NaN | NaN | NaN | NaN |
| 924 | 0.739885 | 0.832578 | 0 | 6.366509e-02 | 8 | 0.303579 | 0.266377 | NaN | NaN | NaN | NaN |
| 925 | 0.368004 | 0.115504 | 0 | 5.093207e-02 | 9 | 0.303579 | 0.268237 | NaN | NaN | NaN | NaN |
| 926 | 0.259240 | 0.733894 | 0 | 4.074566e-02 | 10 | 0.303579 | 0.270004 | NaN | NaN | NaN | NaN |
| 927 | 0.870037 | 0.598727 | 0 | 3.259653e-02 | 11 | 0.303579 | 0.271683 | NaN | NaN | NaN | NaN |
| 928 | 0.370309 | 0.488367 | 0 | 2.607722e-02 | 12 | 0.303579 | 0.273278 | NaN | NaN | NaN | NaN |
| 929 | 0.341303 | 0.845131 | 0 | 2.086178e-02 | 13 | 0.303579 | 0.274793 | NaN | NaN | NaN | NaN |
| 930 | 0.874510 | 0.753911 | 0 | 1.668942e-02 | 14 | 0.303579 | 0.276232 | NaN | NaN | NaN | NaN |
| 931 | 0.351036 | 0.349827 | 0 | 1.335154e-02 | 15 | 0.303579 | 0.277599 | NaN | NaN | NaN | NaN |
| 932 | 0.227616 | 0.910083 | 0 | 1.068123e-02 | 16 | 0.303579 | 0.278898 | NaN | NaN | NaN | NaN |
| 933 | 0.493488 | 0.127884 | 0 | 8.544984e-03 | 17 | 0.303579 | 0.280132 | NaN | NaN | NaN | NaN |
| 934 | 0.867309 | 0.873229 | 0 | 6.835987e-03 | 18 | 0.303579 | 0.281305 | NaN | NaN | NaN | NaN |
| 935 | 0.191815 | 0.126725 | 0 | 5.468790e-03 | 19 | 0.303579 | 0.282418 | NaN | NaN | NaN | NaN |
| 936 | 0.859937 | 0.671237 | 0 | 4.375032e-03 | 20 | 0.303579 | 0.283476 | NaN | NaN | NaN | NaN |
| 937 | 0.933160 | 0.336758 | 0 | 3.500025e-03 | 21 | 0.303579 | 0.284482 | NaN | NaN | NaN | NaN |
| 938 | 0.194804 | 0.914798 | 0 | 2.800020e-03 | 22 | 0.303579 | 0.285436 | NaN | NaN | NaN | NaN |
| 939 | 0.363990 | 0.949417 | 0 | 2.240016e-03 | 23 | 0.303579 | 0.286343 | NaN | NaN | NaN | NaN |
| 940 | 0.587591 | 0.185363 | 0 | 1.792013e-03 | 24 | 0.303579 | 0.287205 | NaN | NaN | NaN | NaN |
| 941 | 0.955836 | 0.837177 | 0 | 1.433610e-03 | 25 | 0.303579 | 0.288024 | NaN | NaN | NaN | NaN |
| 942 | 0.911298 | 0.601206 | 0 | 1.146888e-03 | 26 | 0.303579 | 0.288802 | NaN | NaN | NaN | NaN |
| 943 | 0.226254 | 0.548777 | 0 | 9.175107e-04 | 27 | 0.303579 | 0.289541 | NaN | NaN | NaN | NaN |
| 944 | 0.225364 | 0.009160 | 1 | 2.007340e-01 | 1 | 0.200734 | 0.285100 | NaN | NaN | NaN | NaN |
| 945 | 0.835241 | 0.050737 | 1 | 3.605872e-01 | 1 | 0.360587 | 0.288875 | NaN | NaN | NaN | NaN |
| 946 | 0.396641 | 0.108125 | 0 | 2.884698e-01 | 2 | 0.360587 | 0.292460 | NaN | NaN | NaN | NaN |
| 947 | 0.169220 | 0.494856 | 0 | 2.307758e-01 | 3 | 0.360587 | 0.295867 | NaN | NaN | NaN | NaN |
| 948 | 0.027902 | 0.459607 | 0 | 1.846206e-01 | 4 | 0.360587 | 0.299103 | NaN | NaN | NaN | NaN |
| 949 | 0.246483 | 0.258129 | 0 | 1.476965e-01 | 5 | 0.360587 | 0.302177 | NaN | NaN | NaN | NaN |
| 950 | 0.562113 | 0.539051 | 0 | 1.181572e-01 | 6 | 0.360587 | 0.305097 | NaN | NaN | NaN | NaN |
| 951 | 0.231583 | 0.559012 | 0 | 9.452577e-02 | 7 | 0.360587 | 0.307872 | NaN | NaN | NaN | NaN |
| 952 | 0.198235 | 0.379070 | 0 | 7.562062e-02 | 8 | 0.360587 | 0.310508 | NaN | NaN | NaN | NaN |
| 953 | 0.411360 | 0.790930 | 0 | 6.049649e-02 | 9 | 0.360587 | 0.313012 | NaN | NaN | NaN | NaN |
| 954 | 0.524658 | 0.741770 | 0 | 4.839720e-02 | 10 | 0.360587 | 0.315390 | NaN | NaN | NaN | NaN |
| 955 | 0.870125 | 0.784268 | 0 | 3.871776e-02 | 11 | 0.360587 | 0.317650 | NaN | NaN | NaN | NaN |
| 956 | 0.390234 | 0.313073 | 0 | 3.097421e-02 | 12 | 0.360587 | 0.319797 | NaN | NaN | NaN | NaN |
| 957 | 0.092163 | 0.981683 | 0 | 2.477936e-02 | 13 | 0.360587 | 0.321837 | NaN | NaN | NaN | NaN |
| 958 | 0.534284 | 0.958283 | 0 | 1.982349e-02 | 14 | 0.360587 | 0.323774 | NaN | NaN | NaN | NaN |
| 959 | 0.430348 | 0.723629 | 0 | 1.585879e-02 | 15 | 0.360587 | 0.325615 | NaN | NaN | NaN | NaN |
| 960 | 0.382900 | 0.327333 | 0 | 1.268703e-02 | 16 | 0.360587 | 0.327363 | NaN | NaN | NaN | NaN |
| 961 | 0.502741 | 0.742657 | 0 | 1.014963e-02 | 17 | 0.360587 | 0.329025 | NaN | NaN | NaN | NaN |
| 962 | 0.389661 | 0.902456 | 0 | 8.119702e-03 | 18 | 0.360587 | 0.330603 | NaN | NaN | NaN | NaN |
| 963 | 0.635027 | 0.572727 | 0 | 6.495762e-03 | 19 | 0.360587 | 0.332102 | NaN | NaN | NaN | NaN |
| 964 | 0.507683 | 0.183803 | 0 | 5.196609e-03 | 20 | 0.360587 | 0.333526 | NaN | NaN | NaN | NaN |
| 965 | 0.054200 | 0.925898 | 0 | 4.157287e-03 | 21 | 0.360587 | 0.334879 | NaN | NaN | NaN | NaN |
| 966 | 0.183357 | 0.993465 | 0 | 3.325830e-03 | 22 | 0.360587 | 0.336165 | NaN | NaN | NaN | NaN |
| 967 | 0.584727 | 0.470978 | 0 | 2.660664e-03 | 23 | 0.360587 | 0.337386 | NaN | NaN | NaN | NaN |
| 968 | 0.469614 | 0.619920 | 0 | 2.128531e-03 | 24 | 0.360587 | 0.338546 | NaN | NaN | NaN | NaN |
| 969 | 0.607535 | 0.680682 | 0 | 1.702825e-03 | 25 | 0.360587 | 0.339648 | NaN | NaN | NaN | NaN |
| 970 | 0.980882 | 0.638110 | 0 | 1.362260e-03 | 26 | 0.360587 | 0.340695 | NaN | NaN | NaN | NaN |
| 971 | 0.347348 | 0.074564 | 1 | 2.010898e-01 | 1 | 0.201090 | 0.333715 | NaN | NaN | NaN | NaN |
| 972 | 0.918845 | 0.030857 | 1 | 3.608718e-01 | 1 | 0.360872 | 0.335072 | NaN | NaN | NaN | NaN |
| 973 | 0.566568 | 0.869165 | 0 | 2.886975e-01 | 2 | 0.360872 | 0.336362 | NaN | NaN | NaN | NaN |
| 974 | 0.956637 | 0.651410 | 0 | 2.309580e-01 | 3 | 0.360872 | 0.337588 | NaN | NaN | NaN | NaN |
| 975 | 0.203008 | 0.614893 | 0 | 1.847664e-01 | 4 | 0.360872 | 0.338752 | NaN | NaN | NaN | NaN |
| 976 | 0.501266 | 0.941565 | 0 | 1.478131e-01 | 5 | 0.360872 | 0.339858 | NaN | NaN | NaN | NaN |
| 977 | 0.712008 | 0.227064 | 0 | 1.182505e-01 | 6 | 0.360872 | 0.340909 | NaN | NaN | NaN | NaN |
| 978 | 0.585071 | 0.132383 | 0 | 9.460039e-02 | 7 | 0.360872 | 0.341907 | NaN | NaN | NaN | NaN |
| 979 | 0.006086 | 0.047778 | 1 | 2.756803e-01 | 1 | 0.275680 | 0.338596 | NaN | NaN | NaN | NaN |
| 980 | 0.145191 | 0.273492 | 0 | 2.205442e-01 | 2 | 0.275680 | 0.335450 | NaN | NaN | NaN | NaN |
| 981 | 0.151029 | 0.363357 | 0 | 1.764354e-01 | 3 | 0.275680 | 0.332461 | NaN | NaN | NaN | NaN |
| 982 | 0.716779 | 0.370737 | 0 | 1.411483e-01 | 4 | 0.275680 | 0.329622 | NaN | NaN | NaN | NaN |
| 983 | 0.928012 | 0.571461 | 0 | 1.129187e-01 | 5 | 0.275680 | 0.326925 | NaN | NaN | NaN | NaN |
| 984 | 0.025666 | 0.560317 | 0 | 9.033492e-02 | 6 | 0.275680 | 0.324363 | NaN | NaN | NaN | NaN |
| 985 | 0.136687 | 0.881531 | 0 | 7.226794e-02 | 7 | 0.275680 | 0.321929 | NaN | NaN | NaN | NaN |
| 986 | 0.756983 | 0.650221 | 0 | 5.781435e-02 | 8 | 0.275680 | 0.319616 | NaN | NaN | NaN | NaN |
| 987 | 0.052382 | 0.745683 | 0 | 4.625148e-02 | 9 | 0.275680 | 0.317420 | NaN | NaN | NaN | NaN |
| 988 | 0.988777 | 0.947691 | 0 | 3.700119e-02 | 10 | 0.275680 | 0.315333 | NaN | NaN | NaN | NaN |
| 989 | 0.797602 | 0.874589 | 0 | 2.960095e-02 | 11 | 0.275680 | 0.313350 | NaN | NaN | NaN | NaN |
| 990 | 0.707786 | 0.135681 | 0 | 2.368076e-02 | 12 | 0.275680 | 0.311467 | NaN | NaN | NaN | NaN |
| 991 | 0.908250 | 0.679349 | 0 | 1.894461e-02 | 13 | 0.275680 | 0.309677 | NaN | NaN | NaN | NaN |
| 992 | 0.215424 | 0.023890 | 1 | 2.151557e-01 | 1 | 0.215156 | 0.304951 | NaN | NaN | NaN | NaN |
| 993 | 0.010731 | 0.797032 | 0 | 1.721245e-01 | 2 | 0.215156 | 0.300461 | NaN | NaN | NaN | NaN |
| 994 | 0.535763 | 0.383400 | 0 | 1.376996e-01 | 3 | 0.215156 | 0.296196 | NaN | NaN | NaN | NaN |
| 995 | 0.047954 | 0.270970 | 0 | 1.101597e-01 | 4 | 0.215156 | 0.292144 | NaN | NaN | NaN | NaN |
| 996 | 0.557299 | 0.271441 | 0 | 8.812777e-02 | 5 | 0.215156 | 0.288295 | NaN | NaN | NaN | NaN |
| 997 | 0.748670 | 0.249231 | 0 | 7.050221e-02 | 6 | 0.215156 | 0.284638 | NaN | NaN | NaN | NaN |
| 998 | 0.182926 | 0.398085 | 0 | 5.640177e-02 | 7 | 0.215156 | 0.281164 | NaN | NaN | NaN | NaN |
| 999 | 0.202578 | 0.283877 | 0 | 4.512142e-02 | 8 | 0.215156 | 0.277863 | NaN | NaN | NaN | NaN |
| 1000 | 0.287448 | 0.204221 | 0 | 3.609713e-02 | 9 | 0.215156 | 0.274728 | NaN | NaN | NaN | NaN |

## Ofer - Var Value
| Time: | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Var1 | 28.0 | 100.0 | 28.0 | 37.0 | 85 | 42.000000 | 95.000000 | 23.000000 | 85.000000 | 69.000000 | 78.000000 | 79.000000 | 30.000000 | 92.000000 | 12.0 | 35.000000 | 48.000000 | 84.000000 | 32.000000 | 77.000000 | 62.000000 |
| NaN | NaN | NaN | NaN | NaN | Rate: | 8.888889 | 10.750000 | 8.611111 | 10.194444 | 11.083333 | 10.888889 | 11.916667 | 10.111111 | 12.027778 | 10.0 | 9.055556 | 8.222222 | 8.361111 | 8.416667 | 8.000000 | 9.388889 |
| NaN | NaN | NaN | NaN | NaN | X: | 16.266667 | 25.566667 | 13.400000 | 23.566667 | 22.500000 | 23.466667 | 24.833333 | 16.133333 | 26.700000 | 13.6 | 15.533333 | 16.266667 | 21.233333 | 14.366667 | 19.866667 | 19.533333 |
