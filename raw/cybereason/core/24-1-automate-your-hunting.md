```
import requests

username = "<your user

name>"

password = "<password>"

server = "<server URL>"

port = "443"

data = {

"username":

username,

"password":

password

}

headers = {"Content-Type":

"application/json"}

base_url = "https://" +

server + ":" + port

login_url = base_url +

"/login.html"

session =

requests.session()

response =

session.post(login_url, data=data,

verify=True)

print response.status_code

print

session.cookies.items()

url =

"https://myenvironment.cybereason.net

/rest/visualsearch/query/simple

(https://myenvironment.cybereason.net

/rest/visualsearch/query/simple)"

query = '{"queryPath":

[{"requestedType":"Process","filters"

:

[{"facetName":"isDownloadedFromIntern

et","values":[true]},

{"facetName":"firstExecutionOfDownloa

dedProcessEvidence","values":

[true]}],"isResult":true}],"totalResu

```


