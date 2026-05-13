At times, you may need to delete an integration from your
Cybereason XDR, such as when the connected platform is
generating too many false positive events or you are changing to
other products for your security needs.
In cases such as this, you should delete the integration from your
Cybereason XDR environment. If you simply stop the sending of
logs from the third-party integrated platform, Cybereason XDR will
continue to think there is an issue with log forwarding and report
this to you in various places throughout the XDR section of the
Cybereason platform. Therefore, full deletion will ensure there are
no errors for your team to continually address.
To delete an integration, follow these steps:
1. In the Cybereason platform, open the Cybereason Connect
screen and then view the My Integrations tab.
2. Select the integration you need to delete.
3. Click anywhere in the row to display the Access Details pane
for that integration.
4. In the Access Details pane for the integration, click Delete.
Note
For integrations that use the on-site collector, it will take a
few minute for the paused status to propagate to the on-
site collector agent. During this time, the on-site collector
agent will try to send logs to Cybereason XDR, so the data
from those logs will not be ingested into Cybereason XDR.
