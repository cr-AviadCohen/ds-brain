# MCP.pptx

<!-- Slide number: 1 -->
# MCP

Data Science Team
Slack channel: mcp

### Notes:

<!-- Slide number: 2 -->

![](GoogleShape328p57.jpg)
# What is MCP (Model Context Protocol)
MCP is an open, structured protocol, that standardizes how applications provide context to LLMs.Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals devices and accessories.
MCP provides a standardized way to connect AI models to different data sources / tools / services.
Protocol
Model
Context
https://modelcontextprotocol.io/

### Notes:
MCP is an open, structured protocol, that standardizes how applications provide context to LLMs.
Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various peripherals devices and accessories.
So, MCP provides a standardized way to connect AI models to different data sources, tools, and services.
Since there is a protocol, different models can use different contexts.

<!-- Slide number: 3 -->
# Why MCP
MCP help you build agents and complex workflows on top of LLMs.
MCP Server:Make an API accessible, in natural language, to humans and AI (agents)

![](GoogleShape342p58.jpg)

![HD wallpaper: problem, solution, decision, think, choose ...](GoogleShape341p58.jpg)

### Notes:
With MCP we can build complex agentic workflows on top of LLMs.
An MCP Server, make an API accessible, in natural language, to humans and AIs.

<!-- Slide number: 4 -->

![](GoogleShape347p59.jpg)

### Notes:
With MCP we can build complex agentic workflows on top of LLMs.
An MCP Server, make an API accessible, in natural language, to humans and AIs.

<!-- Slide number: 5 -->

![](GoogleShape352p60.jpg)

### Notes:

<!-- Slide number: 6 -->
# MCP Trend
MCP is a growing industry trend
Data providers (e.g., CRMs, security tools, analytics platforms) want to be “in the loop” during LLM decision-making.
ChatGPT/Gemini connectors:

![](GoogleShape360p61.jpg)

![](GoogleShape358p61.jpg)

### Notes:
So MCP is currently a growing industry trend we here from everywhere.
All the data providers want to be “in the loop” during agentic workflows decision-making.
Here you can see an example of ChatGPT and Gemini, using “connectors” to different data sources, that can be allowed easily using MCP protocol.

<!-- Slide number: 7 -->
# MCP Examples
Native support for MCP on Microsoft Windows
SQLite - Database interaction and business intelligence features
Google Drive - File access and search capabilities for Google Drive
GitHub - Repository management, file operations, and GitHub API integration
Slack
https://github.com/punkpeye/awesome-mcp-servers

### Notes:
Here you can see some example of MCPs.
Last week Microsoft announced that they will support MCP natively on Windows.It will allow user, for example, to instruct LLM to do operations on file system, configurations, etc.

<!-- Slide number: 8 -->
# Project Goal
Develop an MCP for Cybereason and make it accessible to clients AI.
Ex. Customer will have his AI and would like to perform actions over CR product

Building POC to demonstrate capabilities of MCP

Gain knowledge on designing CR’s MCP for production

The world is going to “connect AI with AI”

![3d White people with dart and target. Success in business. (Provided by Getty Images)](GoogleShape371p63.jpg)

### Notes:
So the goal of our project is to develop an MCP for Cybereason product, and make it accessible to client’s AI.
For example, the AI of a customer will have ability to perform actions over CR product.
We now build a POC to demonstrate the capabilities of our MCP and gaining knowledge on how to design MCP for production.
We now preparing Cybereason for the emerging paradigm of “AI-to-AI”, where autonomous agents collaborate across systems.

<!-- Slide number: 9 -->

![](GoogleShape379p64.jpg)
# Architecture
https://drive.google.com/drive/u/0/folders/1D2QGMcKcUFlXXKC3VsLUss1FiqFp8yNZ

### Notes:
When we are talking about MCP architecture, there are two sides, a client side and Cybereason side.
On the client side, the user ask its LLM/AI-agent for something. The AI has a connection to various MCPs from different vendors, one of them is Cybereason.The AI may decide that in order to answer the user’s query it should use the Cybereason MCP.
On Cybereason MCP side we have an MCP client and MCP server.
The MCP client which serves as a facade, and manages the connections with all the different clients.
The MCP server is implemented as simple agent with tools. It gets an input in natural language, and choose which tool to use in order to answer the question.
Each tool call an API on Cybereason platform.

Note that the Cybereason MCP just exposes the API functionality to interact with, in natural language.

<!-- Slide number: 10 -->
# Next Steps
Broaden the set of API we support in our MCP server (e.g., query)
Raise the MCP Server internally in Cybereason, for testing and feedback.
Develop our MCP client
Develop Cybereason AI agent

* * Feel free to contact us with more ideas

### Notes:
Regarding the next steps on our MCP project:
We will broaden the set of APIs we support on our MCP server.
We are willing to expose our MCP server to be accessible internally in Cybereason for testing, and user feedback.
Develop our own MCP client.
Develop an AI agent for Cybereason which will utilize the MCP server so solve complex tasks.

<!-- Slide number: 11 -->
# Live Demo

### Notes:
We will now move to a Live Demo presentation by Shachar.

<!-- Slide number: 12 -->
# Demo inputs
Call a simple api- list_saved_queries  use requests:
return all saved queries
give me all saved queries
Call more complex api which get parameters- create_user  use requests:
create user- avishahar@test.com, pas, analyst_l3- return bad password error
create user- avishahar@test.com, pasWord123#, analyst_admin- return bad role
create user- avishahar@test.com, pasWord123#, analyst_l3- success
Call api all users to see new user- list_users  use requests: return all users
Remove user- delete_user use requests: remove- avishahar@test.com
Call more complex api run_investigative_queries use requests- return all files, return files names include e and limit result to 3

### Notes:

<!-- Slide number: 13 -->

Q&A

### Notes:
