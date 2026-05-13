|Command|Description|Example|
|---|---|---|
|Get-Help|Displays information about<br>PowerShell commands and<br>concepts.|Get-Help|


## Data extraction commands

The following commands enable you to retrieve data on the


selected machine:






















|Command|Description|Example|
|---|---|---|
|Get-ChildItem|Retrieves a list of fles or MAC<br>timestamps from one or more<br>directories. This command can also<br>identify MAC timestamps. Specify<br>the directories with the_path_<br>parameter.|Get-ChildIte<br>C:\Windows|
|Get-ComputerInfo|Retrieves system and operating<br>system properties.|Get-Compu|
|Get-Content|Lists the contents of a fle. List the<br>fle with the_path_ parameter.|Get-Conten<br>C:\Windows|
|Get-History|Retrieves a list of commands<br>entered in this session.|Get-History|
|Get-HotFix|Lists the hotfxes applied on the<br>selected machine.|Get-HotFix|
|Get-Item|Retrieves a list of items from the<br>specifed directory. Add a directory<br>with the_path_ parameter.|Get-Item C|
|Get-ItemProperty|Gets the property of a selected<br>item. This is often used to retrieve<br>the property values of registry<br>entries.|Get-ItemPro|
|Get-<br>ItemPropertyValue|Gets a value for one or more<br>properties of an item.|Get-ItemPro<br>'HKLM:\SO<br>NT\Current|
|Get-<br>NetTCPConnection|Retrieves the current TCP<br>connections. Use this command to<br>view the TCP connection properties<br>like local and remote IP addresses,<br>local or remote ports, and the<br>connection state.|Get-NetTCP|


|Command|Description|Example|
|---|---|---|
|Get-PnpDevice|Retrieves a list of storage devices<br>connected to the endpoint<br>machine, including the device<br>details and connection status. The<br>Get-PnpDevice command is<br>commonly used when adding<br>Device control exclusions<br>(/s/knowledge-base?article=24-1-<br>set-the-device-control-access-<br>modes&language=en_US#manage-<br>individual-devices).<br>Note<br>To enable the Get-PnpDevice<br>command, contact Technical<br>Support.|Get-PnpDe<br>Format-Tab<br>Property In|
|Get-PSDrive|Gets the list of drives in the current<br>session.|Get-PSDriv|
|Get-Service|Lists the services currently running<br>on the machine.|Get-Service<br>eq 'Stoppe|
|Get-TimeZone|Gets the current time zone or a list<br>of available timezones.|Get-TimeZo|
|Get-WinEvent|Lists the events from event logs and<br>event tracing fles.|Get-WinEve|
|Write-Host|Enables you to write messages to<br>the console. This can be used to<br>run a command or script<br>interactively.|Write-Host|
|Process and export commands<br>The following commands enable you to process and export data<br>on the selected machine:|Process and export commands<br>The following commands enable you to process and export data<br>on the selected machine:|Process and export commands<br>The following commands enable you to process and export data<br>on the selected machine:|


|Command|Description|Example|
|---|---|---|
|ConvertFrom-<br>Csv|Converts<br>data from<br>another<br>format to a<br>CSV fle<br>format.|Get-Content<br>C:\Users\user\Documents\Book1.csv<br>| ConvertFrom-Csv|
|ConvertTo-<br>Html|Converts<br>the output<br>to HTML<br>output. You<br>can also<br>use the<br>command<br>to defne<br>HEAD,<br>TITLE, and<br>BODY<br>attributes.|Get-Content<br>C:\Users\user\Documents\Book1.csv<br>| ConvertTo-Html|
|ForEach-<br>Object|Adds a**For**<br>loop to<br>PowerShell<br>commands.|Get-Service | ForEach-Object<br>{$_.Status, $_.DisplayName}|
|Format-table|Displays the<br>output in a<br>table.|Get-Service | Format-Table -Property<br>Name,DependentServices|
|Get-Date|Displays the<br>current date<br>and time.<br>You can<br>also use<br>this<br>command<br>to add or<br>subtract<br>days when<br>fltering the<br>output.|Get-Date -Format d|
|Select-Object|Selects<br>specifc<br>properties<br>from a<br>command.|Get-Service | Select-Object -<br>Property Name|


|Command|Description|Example|
|---|---|---|
|Select-String|Select a<br>specifc<br>string from<br>the output.|Get-ChildItem<br>c:\windows\system32\*.txt -Recurse |<br>Select-String -Pattern 'Microsoft'|
|Sort-Object|Sorts the<br>properties<br>in<br>ascending<br>or<br>descending<br>order.|Get-History | Sort-Object -<br>Descending|
|Where-<br>Object|Filters the<br>output for<br>specifc<br>properties.|Get-Service | Where-Object<br>{$_.Status -eq 'Stopped'}|


## Remediation commands

The following commands enable you to perform remediation on

the selected machine:








|Command|Description|Example|Col4|
|---|---|---|---|
|Disable-LocalUser|Disables local<br>user accounts.<br>When this<br>account is<br>disabled, this<br>prevents the<br>user from<br>logging on.|Disable-LocalUser -Name<br>'username'||


|Command|Description|Example|Col4|
|---|---|---|---|
|Remove-Item|Deletes one or<br>more items. It<br>is possible to<br>use this<br>command to<br>delete many<br>different types<br>of items,<br>including fles,<br>folders,<br>registry<br>keys,variables,<br>aliases, and<br>functions.|Remove-Item C:\Test\*.*||
|Remove-<br>ItemProperty|Deletes a<br>property and<br>its value from<br>an item. You<br>can use this to<br>delete registry<br>values and the<br>data these<br>registry entries<br>store.|Remove-ItemProperty -Path<br>'HKLM:\SOFTWARE\Microsoft\te<br>-Name 'test1'||
|Remove-Job|Removes<br>PowerShell<br>background<br>jobs.|Remove-Job -Name .batch -For||
|Remove-LocalUser|Deletes local<br>user accounts.|Remove-LocalUser -Name<br>'AdminContoso02'||
|Remove-<br>LocalGroupMember|Removes a<br>user or users<br>from a local<br>group.|Remove-LocalGroupMember -<br>Group 'Administrators' -Membe<br>'Admin02'||
|||||


|Command|Description|Example|Col4|
|---|---|---|---|
|Stop-Process|Stops one or<br>more running<br>processes.<br>You can<br>specify a<br>process by<br>process name<br>or process ID<br>(PID), or pass<br>a process<br>object to this<br>command.|Stop-Process -Name 'notepad'||
|Unregister-<br>ScheduledTask|Unregisters a<br>scheduled<br>task from the<br>Windows<br>Scheduler<br>service on a<br>local<br>computer.|Unregister-ScheduledTask -<br>TaskName 'HardwareInventory'||
|Output processing parameters<br>The following parameters are supported to enable you to better<br>use your commands:<br>**Parameter**<br>**Description**<br>**Example**<br>ErrorAction<br>Specifes a<br>custom error<br>action for a<br>command. The<br>most common<br>option is to<br>SilentlyContinue<br>or a value of**0**.<br>Stop-Process -Name<br>invalidprocess -ErrorAction<br>SilentlyContinue<br>FilterHashtable<br>Filters the event<br>logs.<br>Get-WinEvent -FilterHashtable<br>@{logname='application'}|Output processing parameters<br>The following parameters are supported to enable you to better<br>use your commands:<br>**Parameter**<br>**Description**<br>**Example**<br>ErrorAction<br>Specifes a<br>custom error<br>action for a<br>command. The<br>most common<br>option is to<br>SilentlyContinue<br>or a value of**0**.<br>Stop-Process -Name<br>invalidprocess -ErrorAction<br>SilentlyContinue<br>FilterHashtable<br>Filters the event<br>logs.<br>Get-WinEvent -FilterHashtable<br>@{logname='application'}|Output processing parameters<br>The following parameters are supported to enable you to better<br>use your commands:<br>**Parameter**<br>**Description**<br>**Example**<br>ErrorAction<br>Specifes a<br>custom error<br>action for a<br>command. The<br>most common<br>option is to<br>SilentlyContinue<br>or a value of**0**.<br>Stop-Process -Name<br>invalidprocess -ErrorAction<br>SilentlyContinue<br>FilterHashtable<br>Filters the event<br>logs.<br>Get-WinEvent -FilterHashtable<br>@{logname='application'}||


|Parameter|Description|
|---|---|
|ErrorAction|Specifes a<br>custom error<br>action for a<br>command. The<br>most common<br>option is to<br>SilentlyContinue<br>or a value of**0**.|
|FilterHashtable|Filters the event<br>logs.|


|Parameter|Description|Example|
|---|---|---|
|Force|Forces the<br>command to<br>bypass the fle<br>attribute<br>settings for<br>hidden and<br>system.|Remove-Job -Name .batch -Force|
|Include|Includes a<br>specifc set of<br>fles in the<br>command.|Get-ChildItem -Path<br>$env:SystemRootSystem32 -<br>Include_e_|
|Path|Defnes the<br>directory to use<br>in the<br>command.|Remove-ItemProperty -Path<br>'HKLM:\SOFTWARE\Microsoft\test'<br>-Name 'test1'|
|Recurse|Performs an<br>action<br>recursively.|Get-ChildItem<br>c:\windows\system32\*.txt -<br>Recurse | Select-String -Pattern<br>'Microsoft'|


## Supported aliases

The following aliases are supported:














|Alias|Description|Function|Example|
|---|---|---|---|
|cd|Changes the<br>location on which<br>to run subsequent<br>commands.|Set-<br>Location||
|ps|Gets the details<br>for a process.|Get-<br>Process||
|help|Displays the Help<br>about supported<br>commands.|Get-Help||
|dir|Retrieves a list of<br>children for a<br>specifed item.|Get-<br>ChildItem||


|Alias|Description|Function|Example|
|---|---|---|---|
|sl|Sets a specifc<br>location for<br>running<br>commands.|Set-<br>Location||
|Chdir|Sets a specifc<br>location for<br>running<br>commands.|Set-<br>Location||
|%|Performs an<br>operation against<br>each item in the<br>collection.|ForEach-<br>Object|Get-Service | %<br>{$_.Status,<br>$_.DisplayName}|
|?|Selects objects<br>from a collection<br>based on<br>property values.|Where-<br>Object|Get-Service | ?<br>{$_.Status -eq<br>'Stopped'}|









