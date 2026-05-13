|Parameter|Description|
|---|---|
|AP_CRS_SERVICE_MODE|Install Anti-Ransom<br>actions to take if ran<br>detected.|
|ANTI_MALWARE|Enable or disable A|
|AP_POWERSHELL_SERVICE_MODE|Enable or disable F|
|||


|Parameter|Description|
|---|---|
|AP_AV_MODE|Set the Anti-Malwar<br>mode.|
|AP_AV_PROXY_LIST|Defnes a proxy ser<br>communication betw<br>and the Anti-Malwa<br>database. Provide a<br>separated list of pro<br>following format:<br><server IP or DNS n<br>This parameter is sp<br>Malware Signatures<br>defne a proxy for c<br>between the sensor<br>and Registration se<br>AP_SIGNON_PROX<br>Note<br>If you are using th<br>Signatures mode,<br>want to add the<br>AP_AV_PROXY_L<br>ensure that the se<br>receive Signature<br>database update<br>connection.|
|||


|Parameter|Description|
|---|---|
|AP_AV_PROXY_TYPE|Defnes the commu<br>the proxy server us<br>communication betw<br>and the Anti-Malwa<br>database. Values c<br>PAC. HTTP is used<br>single proxy or list o<br>in the AP_AV_PROX<br>PAC is used when t<br>referenced in the A<br>parameter.<br>This parameter is sp<br>Malware Signatures<br>defne a proxy for c<br>between the sensor<br>and Registration se<br>AP_SIGNON_PROX<br>parameter.|
|AP_GROUP_ID|Parameter to prese<br>group ID|
|AP_ORGANIZATION|Unique organization<br>in the server installa<br>Your Cybereason C<br>representative can<br>this value. You can<br>in the installer pack<br>provided for your or|
|AP_PORT|Port used by the se<br>the Cybereason De<br>Your Cybereason C<br>representative can<br>this value. You can<br>in the installer pack<br>provided for your or<br>Note<br>Be sure to disable<br>of sensor traffc to|
|||


|Parameter|Description|
|---|---|
|AP_POLICIES_INITIAL_POLICY_ID|Assign the specifed<br>the sensor. If this pa<br>blank, the Default p|
|AP_POLICIES_KEEP_SENSOR_CONFIGURATION|Used mainly when<br>or later from a versi<br>When set to_1_, sens<br>individual security c<br>top of the policy de<br>AP_POLICIES_INIT<br>parameter. We reco<br>parameter to 0 for n<br>for upgrades.|
|AP_SA_DETECT_MODE|Sensitivity level for t<br>Detect mode.|
|AP_SA_PREVENT_MODE|Sensitivity level for t<br>Prevent mode.|
|AP_SERVER|URL or IP address o<br>Detection server. Yo<br>Customer Success<br>provide you with thi<br>also fnd this value<br>package name prov<br>organization.<br>Note<br>Be sure to disable<br>of sensor traffc to|
|||


|Parameter|Description|
|---|---|
|AP_SIGNON_SERVER|URL or IP address o<br>Registration server.<br>exclusive with AP_S|
|AP_SIGNON_PORT|Port used by the se<br>a Cybereason Regi<br>is mutually exclusiv<br>AP_SERVER/AP_PO|
|AP_DETECTION_PROXY_AS_SIGNON|Whether the sensor<br>proxy settings conf<br>Registration server.<br>When enabled (1),<br>the proxy defned in<br>AP_SIGNON_PROX<br>AP_SIGNON_PROX<br>communication betw<br>and the Detection s<br>settings defned in t<br>servers screen are<br>When disabled (0),<br>the proxy settings d<br>Detection servers s|
|AP_SIGNON_PROXY_LIST|For environments w<br>server. A comma-se<br>proxy servers in the<br><server IP or DNS n<br>AP_SIGNON_PROX<br>AP_PROXY_LIST ar<br>exclusive.<br>Ensure you either s<br>AP_DETECTION_PR<br>parameter to**1**, or d<br>the Detection serve<br>**servers** screen in th|
|||


|Parameter|Description|
|---|---|
|AP_SIGNON_PROXY_TYPE|For environments w<br>server. Values can b<br>HTTP is used when<br>proxy or list of spec<br>AP_SIGNON_PROX<br>PAC is used when t<br>referenced in the<br>AP_SIGNON_PROX<br>AP_SIGNON_PROX<br>AP_PROXY_TYPE a<br>exclusive.<br>Note<br>If you are using th<br>Signatures mode,<br>a value for the<br>AP_AV_PROXY_T<br>to enable the sen<br>Signatures mode<br>updates with a pr|
|AP_STATE|The sensor state at<br>sensor data collect<br>information.|
|AP_UNINSTALL_CODE|When uninstalling a<br>been protected with<br>password, use this<br>the uninstall passwo<br>password, contact|
|||


|Parameter|Description|
|---|---|
|AV_SIGNATURE_PATH|When installing sen<br>Malware signatures<br>included (Windows<br>optionally place the<br>database zip fle in<br>than the installation<br>shared network fold<br>you must use this p<br>provide the path to<br>fle. Enter the full pa<br>the fle name.<br>Note<br>The Signatures zi<br>**cumulative.zip**. F<br>AV_SIGNATURE_<br>the Signatures zip<br>not rename the fl|
|AP_PROXY_LIST|**This parameter is**<br>**legacy environmen**<br>**include a Registra**<br>**best practice, we r**<br>**the AP_SIGNON_P**<br>**parameter instead**<br>Comma-separated<br>servers or PAC fles<br>format:<br><server IP or DNS n<br>Port>,<server IP or<br>Port><br>It is not possible to<br>one PAC proxy.<br>This parameter may<br>proxy is not in use o<br>be auto-detected b|
|||


|Parameter|Description|
|---|---|
|AP_PROXY_TYPE|**This parameter is**<br>**legacy environmen**<br>**include a Registra**<br>**best practice, we r**<br>**the AP_SIGNON_P**<br>**parameter instead**<br>HTTP or PAC. HTTP<br>AP_PROXY_LIST pa<br>a single proxy or lis<br>proxies. PAC is use<br>AP_PROXY_LIST pa<br>references a PAC f<br>type in the following<br>For HTTP proxies:<br>AP_PROXY_LIST=<<br><Proxy_Port><br>AP_PROXY_TYPE=<br>For PAC fles:<br>AP_PROXY_LIST=<<br>AP_PROXY_TYPE=<br>Note<br>This parameter m<br>the proxy is not in<br>proxy can be auto<br>sensor. This param<br>omitted if the AP_<br>parameter is not p<br>command line.|
|Note<br>In most cases, it is not necessary to set the<br>AP_ORGANIZATION, AP_SERVER, AP_SIGNON_SERVER,<br>AP_PORT, AP_SIGNON_PORT and AP_STATE parameters, as<br>these parameters are usually preset by Technical Support<br>using sensor personalization. Modifying these parameters|Note<br>In most cases, it is not necessary to set the<br>AP_ORGANIZATION, AP_SERVER, AP_SIGNON_SERVER,<br>AP_PORT, AP_SIGNON_PORT and AP_STATE parameters, as<br>these parameters are usually preset by Technical Support<br>using sensor personalization. Modifying these parameters|



