# Hunter ／ AI Assistant Integration.docx

10.3.26

Gienel’s action items:

* Hunter Uses 3 MCPs:

1. Findings (equivilant to MalOps) MCP
2. Raw Events
3. Findings Enrichment (“Threat Away”)

please share for each MCP:

* + MCP connection config file
  + system promt that is specific to the MCP (currently in Hunter there is one big promp for all tools).
* Prompt Library (examples of queries that Hunter supports).
* CSV file containing the collection of the actual user queries previously made for Hunter (currently has only through OpenWebUI / LiteLLM).
* Statistics:
  + amount of active users:
    - SLR team
    - MSS team
    - GTO team
  + Total amount of queries sent from all users.
  + Total amount of queries sent from each user - NOT AVAILABLE because there is no query id in the logs.
  + Total amount of LLM requests.
  + Total amount of llm requests that are being sent for each of the Prompt Library queries (as an assessment for average amount of requests per user query).

MCP Connection json example

MCP Connection

{

"mcpServers": {

"cybereason-api-tools": {

"command": "<YOUR\_PYTHON\_PATH>",

"args": ["-m", "mcp\_server.run\_mcp\_server"],

"cwd": "<PATH\_TO\_AI\_ASSISTANT\_REPO\_SRC\_DIR>",

"env": {

"CYBEREASON\_HOST": "<https://your-host.cybereason.net>",

"CYBEREASON\_USERNAME": "your-user",

"CYBEREASON\_PASSWORD": "your-pass"

}

}

}

}

12.3.26

* Check if we can expose the 3 Fusion MCPs. Currently they are all internal. Gienel will reach out to the cloud operations team to get an approval, if not we will have to wait for the full company's integration.
* Gienel will supply a list of all Hunter capabilities (separated by the MCP that is enabling the tools), by sharing all the available tools (both by the MCPs and by the OpenWebUI built in tools).

Once we have that list, we will start working on making sure we support everything under the Assistant.

* Enable saving LLM requests in a recurring way under LiteLLM.
* In the meantime, get the questions manually.
* Statistics:
  + Gienel is working on a notebook that will calculate all the requested statistics programmatically.
* Statistics:

SOC analysts: 3 active users (both GTO, MSS)

SLR : 5 active (some are AI systems, similarly to office 365).

Gienel will share the numbers once the notebook will be implemented.
