# Project MCP.docx

🏁 Main

**Project
Model Context Protocol (MCP)**

#

# General

* **Description:**
  + Development of MCP Server for Cybereason.
  + The MCP Server should contain the routing logic and various tools implementations.
    Each tool is responsible for a single API call.

![](data:image/png;base64...)

* **Owner:**
* Shachar Wirzeberger
* Ohav Peri
* **Code:**
  + <https://github.com/cybereason-labs/data-science/tree/mcp-dev-client> (not relevant – Shachar Wirzeberger DELETE)
  + <https://github.com/cybereason-labs/data-science/tree/mcp-dev> (Streamlit)
  + <https://github.com/cybereason-labs/data-science/tree/mcp-dev-shachar> (Current MCP)
* **Jira:**
  + [ENG-2049: MCP Server for Cybereason | Innovation POC](https://cybereason.atlassian.net/browse/ENG-2049?atlOrigin=eyJpIjoiOGFhYzRlMjAwMzYwNDY2YTkzNTJmMjkwYWNiM2YxNmIiLCJwIjoiaiJ9)
  + [ENG-2457: Q3 - POC on Core - implement MCP Client](https://cybereason.atlassian.net/browse/ENG-2457?atlOrigin=eyJpIjoiMWUwNTI5NTljYTUzNDhjYWEyN2QzZTAxN2UwOWYwZWIiLCJwIjoiaiJ9)
* **Presentations:**
  + [Presentation](https://docs.google.com/presentation/d/1ROvGtg0t9UVCsxe4mYU31mpcTWzI1EM5HuJ95Ly44wY/edit?slide=id.g366939f9e2b_0_58#slide=id.g366939f9e2b_0_58)
  + [Innovation Workshop](https://docs.google.com/presentation/d/1ADNjd5tQxw1zfxikvQuiJrjX8qumVfRsclY8yEAFHq4/edit?slide=id.g34da0722ad5_0_8#slide=id.g34da0722ad5_0_8)
* [Architecture](https://app.diagrams.net/?state=%7B%22ids%22:%5B%221bjn2jUMrJ07Ojhd7kkZASpek9A_8-lEf%22%5D,%22action%22:%22open%22,%22userId%22:%22114475530764424765290%22,%22resourceKeys%22:%7B%7D%7D)
* [MCP Server APIs](https://docs.google.com/spreadsheets/d/1Pc3hnyBuxM1Tb0FgSgtSJE7mygCAVnhgfqLvEc2VS2k/edit?gid=0#gid=0)
* [Phoneix Feature Parity List](https://docs.google.com/spreadsheets/d/1Z9PeodPmXdVr9-OW1lggJS-Sc-PoyaB49TicqHhkRv0/edit?gid=80802813#gid=80802813)
* [Cybereason API Guide](https://nest.cybereason.com/s/article/cybereason-api-guide)
* [#Slack Channel](https://cybereason.enterprise.slack.com/archives/C08V0L8GJEL)
* **More Info:**
  + <https://modelcontextprotocol.io/introduction>
  + [AutoMCP](https://github.com/brizzai/auto-mcp)
  + [Build and Deploy a Remote MCP Server to Google Cloud Run in Under 10 Minutes](https://cloud.google.com/blog/topics/developers-practitioners/build-and-deploy-a-remote-mcp-server-to-google-cloud-run-in-under-10-minutes)

# Issues

* Part of the APIs return too many tokens (e.g., 81K tokens), then we easily each the 450K tokens per minute limit of Azure OpenAI GPT4o
  + API wasn’t meant to be utilized by LLMs, so it returns tons of data.
* Can we get direct connection to the database rather than API?
* How can we know that an API really did the required action (e.g., process kill) – can we verify the machine?

# Tasks

* Search for the source code of Cybereason API – it will help us know how to use them better.
* Presentation in Innovation Workshop
* **MCP Server:**
  + Implement the MCP Server so that it can be consumed in the standard way using MCP clients (Claude Desktop, Cursor, etc.)
  + Support NPX
    - ask Or Golov& Shani Kahlon for publishing approval
  + Implement ALL APIs
  + Authentication? OAuth?
  + Optimization?
  + Should we build the MCP Server with more nodes?
    For example, divide the APIs to categories, than when input arrives, select the right category.
* **Demo:**
  + Create a video demo for MCP from Claude on interesting case. 1-2 minutes video. (for Or GolovIsrael Barak)- <https://drive.google.com/drive/u/0/folders/1cqYV93TDk30P8AZJvFZceTxsxre7NcGu>
* **MCP Client:**
  + Make the MCP client support connecting multiple MCP servers, one of them is cybereason.
  + Make the MCP client connect the host via an address, like http://<host>:<port>
* **General:**
  + Add to the project support for Docker
  + Software engineer the code:
    - Clean, neat code.
    - Divide code into classes: agent, tools (inherent Tool abstract class), etc.
    - Use LangChain & Langraph
  + Update Phoenix API with Shachar Wirzeberger comments about specific APIs that may be change to make it easy for customers to use (from MCP perspective)
* **Learn:**
  + MCP resources, prompts, sampling
* **Future:**
  + Create infrastructure for user feedback.
    Streamlit easily supports user feedback widget => can be saved into a database.
    This should allow us to collect user’s queries and answers, detect problems, and improve our MCP.

# Questions

## MCP-implementation questions

* Do we need to implement our MCP server as production-grade?
  + Or Golov NO
* How do our clients consume our MCP?
  + From internal AI chatchot? Claude?
  + Our MCP server should supply something to the customer AI so the customer knows how to communicate with the MCP (JSON?). As we saw on Cursor Ohav Peri

Example of configuring MCP servers on Cursor:
![](data:image/png;base64...)

* What is the role of the “*MCP Client”* Or Golov is talking about?
  In general, an MCP client is on the client’s side, and it gets configuration to connect different MCP servers.
  To be the Host for the different customers?
* Ohav Peri ChatGPT about MCP Client:<https://chatgpt.com/share/68580d93-756c-800b-a585-df3410b8b80c>

## MCP-technical/conceptual questions

* Ohav PeriShachar Wirzeberger
  Figure out where does the routing take place? At *Client’s AI* side, or *MCP Server* side?
  In the current POC, all routing logic resides on the server side on which an agent hosts a set of tools, each mapped to its own API, and dynamically selects the appropriate API to call for every request.
* Does Client’s AI knows only the description of different MCP’s and chooses one? Or it is aware of the tools also behind the MCP, and chooses the specific tool?

#

# MCP Project Summary

#### **1. First Implementation – “dump client”, “smart mcp server”:**

In the version demonstrated so far, we implemented a “smart agent” running on our server and a “dumb client” that simply sends user messages.

This approach is suitable when we want to embed a chat directly into our product — where the user interacts with the product and asks the chat questions.

In this implementation:

* I created tools tailored to our needs.
* It may result in more accurate API generation and selection, but this is not guaranteed and still needs validation.
* All costs of API calls are incurred by Cybereason.

#### **2. Second Implementation – “smart client”, “dumb mcp server”:**

This version is based on the generic implementation provided at [modelcontextprotocol.io](https://modelcontextprotocol.io/quickstart/server).

Here:

* The client is “smart” and is powered by the client’s own LLM.
* The client connects to our MCP server, which only hosts mcp.tools — no agent.
* The external LLM retrieves available tools from our server and decides whether to use a tool, and which one.

In this setup:

* We only need to provide a generic MCP server that clients can call.
* The cost of LLM queries and API usage is on the client side, not Cybereason.

🤝 Meetings

**Meetings**

# 2025.07.01 – Or Golov

* Demo:
  + Demonstrate MCP Client CLI
  + Demonstrate MCP in Claude Desktop
  + Publish MCP as NPX
* Talk about the difference between MCP Server and Agent (chat that run on our UI)
* How are customers going to consume MCP?
* API Implementation:
  + Prioritize APIs as part of them are not working.
  + Who is responsible for the APIs and can direct us (Chen Aviani)?
  + Does all APIs are relevant? We saw that we work on old server that have APIs that doesn’t exist in new server and on new server there is apis that don't exist on our.
    - Ensure the NEST API documentation is up to date so all UI-supported actions can be reliably performed via the API. We must verify that every API action is accurately replicable through the UI, and that we can make sure it did what it was intended to, otherwise we can’t ensure implementation quality. Currently, some actions can't be simulated via the API, even with the documentation, and it's unclear who to contact for clarification, despite consulting Eli and Chen (for example, remediation [APIs](https://nest.cybereason.com/maniyuaru/api-documentation/all-versions/remediate-items-0)). This gap hinders proper MCP implementation and validation.

Or recommendations:

* Map all APIs and meet with Eli’s Team (with Or)
* [Phoenix API](https://docs.google.com/spreadsheets/d/1Z9PeodPmXdVr9-OW1lggJS-Sc-PoyaB49TicqHhkRv0/edit?usp=drivesdk)

# [Title]

…

✅ Tasks

**Tasks**

* Task 1
* Task 2

❓ MCP - QA

1. where in the code mcp\_client it get the mcp.tool from the server?

**Answer:**

**Looking at the `mcp\_client.py` code, the client gets the MCP tools from the server in the `process\_query` method. Here's the specific section:**

**Read file: mcp\_client.py**

**The MCP client gets the tools from the server in \*\*two key places\*\*:**

**## 1. \*\*During Connection\*\* (lines 107-148 in `connect\_to\_server` method):**

**```python**

**async def connect\_to\_server(self, server\_script\_path: str):**

**# ... connection setup ...**

**# List available tools**

**if self.session is None:**

**raise RuntimeError("Failed to initialize session")**

**response = await self.session.list\_tools()**

**tools = response.tools**

**tool\_names = [tool.name for tool in tools]**

**logger.info(f"Connected to server with {len(tools)} tools: {tool\_names}")**

**```**

**## 2. \*\*For Each Query\*\* (lines 165-180 in `process\_query` method):**

**```python**

**# Fetch available tools**

**response = await self.session.list\_tools()**

**available\_tools: List[ChatCompletionToolParam] = []**

**for tool in response.tools:**

**# Ensure description is not None**

**description = tool.description or f"Tool: {tool.name}"**

**tool\_param: ChatCompletionToolParam = {**

**"type": "function",**

**"function": {**

**"name": tool.name,**

**"description": description,**

**"parameters": tool.inputSchema or {}**

**}**

**}**

**available\_tools.append(tool\_param)**

**```**

**## How it works:**

**1. \*\*`self.session.list\_tools()`\*\* - This is the MCP protocol call that asks the server "what tools do you have?"**

**2. \*\*The server responds\*\* with a list of tools, each containing:**

**- `tool.name` - The function name (e.g., "get\_file\_reputation")**

**- `tool.description` - Description of what the tool does**

**- `tool.inputSchema` - JSON schema defining the parameters**

**3. \*\*The client converts\*\* these MCP tools into OpenAI's tool format so that Azure OpenAI can understand and choose which tools to call**

**4. \*\*When OpenAI decides\*\* to call a tool, the client uses `await self.session.call\_tool(tool\_name, tool\_args)` to actually execute it on the server**

**The key MCP protocol methods used are:**

**- `session.list\_tools()` - Get available tools from server**

**- `session.call\_tool(name, args)` - Execute a specific tool on the server**

**This happens fresh for every query to ensure the client always has the most up-to-date list of available tools from the server.**

1. if i have multipile mcp server, how the client know which one to call?

**Answer:**

**Great question! The current MCP client implementation only connects to \*\*one server at a time\*\*. Let me show you how it works and then explain how you could handle multiple servers.**

**## Current Single Server Implementation**

**Looking at the current code:**

**Read file: mcp\_client.py**

**The current implementation has:**

**- \*\*One session\*\*: `self.session`**

**- \*\*One connection\*\*: connects to a single server script**

**- \*\*All tools come from that one server\*\***

**## How to Handle Multiple MCP Servers**

**There are several approaches to handle multiple servers:**

**### \*\*Approach 1: Tool Name Prefixing (Recommended)\*\***

**Each server could prefix its tools with a unique identifier:**

**```python**

**# Server 1 (Cybereason): cybereason\_get\_file\_reputation, cybereason\_list\_users**

**# Server 2 (GitHub): github\_create\_issue, github\_list\_repos**

**# Server 3 (Database): db\_query\_users, db\_insert\_record**

**```**

**### \*\*Approach 2: Multiple Sessions with Tool Routing\*\***

**Here's how you could modify the client to handle multiple servers:**

**```python**

**class MultiServerMCPClient:**

**def \_\_init\_\_(self):**

**self.servers = {} # server\_name -> session**

**self.tool\_to\_server = {} # tool\_name -> server\_name**

**async def connect\_to\_servers(self, server\_configs):**

**"""**

**server\_configs = {**

**"cybereason": "mcp\_server.py",**

**"github": "github\_server.py",**

**"database": "db\_server.py"**

**}**

**"""**

**for server\_name, script\_path in server\_configs.items():**

**session = await self.\_connect\_single\_server(script\_path)**

**self.servers[server\_name] = session**

**# Map tools to servers**

**response = await session.list\_tools()**

**for tool in response.tools:**

**self.tool\_to\_server[tool.name] = server\_name**

**async def process\_query(self, query: str):**

**# Collect all tools from all servers**

**all\_tools = []**

**for server\_name, session in self.servers.items():**

**response = await session.list\_tools()**

**for tool in response.tools:**

**# Add server context to tool description**

**description = f"[{server\_name}] {tool.description}"**

**all\_tools.append({**

**"type": "function",**

**"function": {**

**"name": tool.name,**

**"description": description,**

**"parameters": tool.inputSchema or {}**

**}**

**})**

**# Let OpenAI choose tools from all servers**

**response = openai.chat.completions.create(**

**model="gpt-4",**

**messages=messages,**

**tools=all\_tools**

**)**

**# Execute tools on the correct server**

**for tool\_call in response.choices[0].message.tool\_calls:**

**tool\_name = tool\_call.function.name**

**server\_name = self.tool\_to\_server[tool\_name]**

**session = self.servers[server\_name]**

**# Execute on the correct server**

**result = await session.call\_tool(tool\_name, tool\_args)**

**```**

**### \*\*Approach 3: Smart Server Selection\*\***

**The client could analyze the query and automatically choose the right server:**

**```python**

**def determine\_server(self, query: str) -> str:**

**query\_lower = query.lower()**

**if any(word in query\_lower for word in ['malop', 'cybereason', 'reputation', 'sensor']):**

**return "cybereason"**

**elif any(word in query\_lower for word in ['github', 'repo', 'issue', 'pull request']):**

**return "github"**

**elif any(word in query\_lower for word in ['database', 'sql', 'query', 'table']):**

**return "database"**

**else:**

**return "default" # or ask user to clarify**

**```**

**## Current Limitation**

**Right now, your client connects to \*\*only one server\*\* at startup:**

**```bash**

**python mcp\_client.py mcp\_server.py # Only connects to this one server**

**```**

**All tools come from that single server, so there's no ambiguity about which server to call - there's only one!**

**## Recommendation**

**For your current Cybereason setup, you probably want to keep it simple with one server. But if you plan to add more servers later, I'd recommend:**

**1. \*\*Tool prefixing\*\* - Each server prefixes its tools (e.g., `cybereason\_`, `github\_`, `db\_`)**

**2. \*\*Server context in descriptions\*\* - Tool descriptions mention which system they interact with**

**3. \*\*Let OpenAI decide\*\* - The AI model is smart enough to choose the right tools based on context**

**Would you like me to show you how to implement multi-server support, or are you planning to stick with the single Cybereason server for now?**

1. so if i only have the mcp\_server i will need to pay for it?

**Answer:**

**\*\*No, if you only have the MCP server, you don't need to pay for anything!\*\***

**Let me clarify the confusion:**

**## What Each Component Does**

**### \*\*MCP Server\*\* (`mcp\_server.py`) - \*\*FREE\*\***

**- Runs locally on your machine**

**- Connects to Cybereason APIs**

**- Provides tools via MCP protocol**

**- \*\*Cost: $0\*\* (just uses your computer's resources)**

**### \*\*MCP Client\*\* (`mcp\_client.py`) - \*\*COSTS MONEY\*\***

**- Uses Azure OpenAI API to understand natural language**

**- Decides which tools to call**

**- Formats responses nicely**

**- \*\*Cost: Azure OpenAI API charges\*\***

**## Your Options**

**### \*\*Option 1: MCP Server Only\*\* - \*\*FREE\*\***

**You can use the MCP server directly without the AI client:**

**```python**

**# Direct tool calls - no AI needed**

**import tools**

**# Authenticate**

**tools.authenticate()**

**# Call tools directly**

**users = tools.list\_users()**

**reputation = tools.get\_file\_reputation("d41d8cd98f00b204e9800998ecf8427e")**

**malops = tools.query\_malops(start\_time, end\_time)**

**```**

**\*\*Pros\*\*: Free, fast, direct API access**

**\*\*Cons\*\*: No natural language, you need to know exact function names and parameters**

**### \*\*Option 2: MCP Server + Client\*\* - \*\*COSTS MONEY\*\***

**Your current setup with natural language:**

**```bash**

**Query: "get reputation for file hash abc123"**

**# AI decides to call get\_file\_reputation("abc123")**

**```**

**\*\*Pros\*\*: Natural language interface, AI decides which tools to use**

**\*\*Cons\*\*: Costs money for Azure OpenAI API calls**

**### \*\*Option 3: Other MCP Clients\*\* - \*\*VARIES\*\***

**You could use different MCP clients:**

**- \*\*Claude Desktop\*\*: Uses Anthropic's API (costs money)**

**- \*\*Local LLM client\*\*: Uses local models like Ollama (free but needs good hardware)**

**- \*\*Custom simple client\*\*: Basic tool selection without AI (free)**

**## The Key Point**

**\*\*The MCP server itself is completely free\*\* - it just runs on your computer and talks to Cybereason.**

**\*\*You only pay when you add AI\*\* to understand natural language and automatically choose tools.**

**## Simple Free Alternative**

**If you want to avoid costs, you could create a simple menu-driven client:**

**```python**

**# Simple free client**

**print("Available tools:")**

**print("1. List users")**

**print("2. Get file reputation")**

**print("3. Query malops")**

**choice = input("Select tool: ")**

**if choice == "1":**

**result = tools.list\_users()**

**elif choice == "2":**

**hash\_val = input("Enter file hash: ")**

**result = tools.get\_file\_reputation(hash\_val)**

**# etc...**

**```**

**\*\*So to answer your question directly: The MCP server alone costs nothing. You only pay when you add AI capabilities for natural language processing.\*\***

1. How to make llm choose the right server automatically?

**Answer:**

**Great question! Currently, your MCP client is designed to connect to \*\*only one server at a time\*\*. Let me explain the current limitation and then show you how to modify it to support multiple servers with LLM-based server selection.**

**## Current Architecture (Single Server)**

**Looking at your current `mcp\_client.py`:**

**Read file: mcp\_client.py**

**Currently, you have:**

**- \*\*One session\*\*: `self.session`**

**- \*\*One connection\*\*: connects to a single server script path**

**- \*\*All tools from that one server\*\* are presented to the LLM**

**## Solution: Multi-Server MCP Client with LLM-Based Server Selection**

**Here's how to modify your client to support multiple MCP servers with intelligent server selection:**

**Now let me add the multi-server connection and selection methods:**

**Now let me update the `process\_query` method to work with multiple servers:**

**Now I need to update the tool execution part to use the correct server:**

**Now let me update the main function and add a new method to set up multiple servers:**

**Let me also add a command to list servers in the chat loop:**

**Now let me create an example of how to use this multi-server setup:**

**Let me also create a simple example of another MCP server to demonstrate the multi-server concept:**

**Now let me update the multi-server example to include the file server:**

**Finally, let me create a README explaining how the multi-server system works:**

**## Summary**

**I've successfully modified your MCP client to support \*\*multiple servers with LLM-based server selection\*\*! Here's what I implemented:**

**### 🔧 \*\*Key Changes Made\*\***

**1. \*\*Multi-Server Architecture\*\*:**

**- Modified `MCPClient` class to manage multiple server connections**

**- Added server configuration with descriptions and capabilities**

**- Each server maintains its own session and tools**

**2. \*\*LLM-Based Server Selection\*\*:**

**- `select\_best\_servers\_for\_query()` uses GPT-4 to analyze queries**

**- Compares user queries against server descriptions and capabilities**

**- Automatically selects the most appropriate server(s)**

**3. \*\*Intelligent Tool Routing\*\*:**

**- Tools are mapped to their originating servers**

**- Execution happens on the correct server automatically**

**- Supports queries that need multiple servers**

**### 📁 \*\*Files Created\*\***

**- \*\*`multi\_server\_example.py`\*\* - Complete example showing multi-server setup**

**- \*\*`simple\_file\_server.py`\*\* - Example file management MCP server**

**- \*\*`README\_multi\_server.md`\*\* - Comprehensive documentation**

**### 🚀 \*\*How to Use\*\***

**\*\*Multi-Server Mode:\*\***

**```bash**

**python multi\_server\_example.py**

**```**

**\*\*Single Server Mode (still works):\*\***

**```bash**

**python mcp\_client.py mcp\_server.py**

**```**

**### 🧠 \*\*LLM Server Selection Examples\*\***

**| Your Query | Selected Server | Why |**

**|------------|----------------|-----|**

**| "Check malware reputation for google.com" | `cybereason` | Security/malware keywords |**

**| "List files in current directory" | `file\_manager` | File/directory operations |**

**| "Show threat data and list .py files" | \*\*Both servers\*\* | Multi-capability query |**

**### ✨ \*\*Key Benefits\*\***

**1. \*\*Automatic\*\*: No manual server selection needed**

**2. \*\*Intelligent\*\*: LLM understands which server to use**

**3. \*\*Scalable\*\*: Easy to add new specialized servers**

**4. \*\*Backward Compatible\*\*: Existing single-server code still works**

**5. \*\*Flexible\*\*: Single queries can use multiple servers**

**### 🎯 \*\*Next Steps\*\***

**1. \*\*Test the multi-server setup\*\*:**

**```bash**

**python multi\_server\_example.py**

**```**

**2. \*\*Try these example queries\*\*:**

**- "Check reputation for google.com" → Uses Cybereason**

**- "List files in current directory" → Uses File Manager**

**- "Show me users and current files" → Uses both servers**

**3. \*\*Create your own specialized servers\*\* using the pattern in `simple\_file\_server.py`**

**The LLM now acts as an intelligent router, automatically selecting the right server(s) for each query based on their descriptions and capabilities!**

1. which parametrs FastMCP get and what they do?

**Answer:**

**Below is a concise “field guide” to the FastMCP constructor.
 Every keyword is optional; if you omit it FastMCP falls back to a sensible default.**

| **Group** | **Parameter** | **What it controls** |
| --- | --- | --- |
| **Identity / metadata** | **name** | **Human-friendly server name shown to clients (default “FastMCP”) (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
|  | **version** | **Arbitrary version string (e.g. "2.3.1"); forwarded in discovery payloads so clients can pin or compare versions (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
|  | **instructions** | **High-level natural-language instructions that describe how LLMs should use the server and its tools (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **Security / auth** | **auth** | **An OAuthProvider (or subclass). If omitted, FastMCP falls back to the bearer-token provider that reads FASTMCP\_BEARER\_TOKEN from the environment (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **HTTP behaviour** | **middleware** | **A list of Starlette/FastAPI middleware instances injected into the auto-generated ASGI app (e.g. CORS, rate-limit, Sentry, etc.) (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **Lifecycle** | **lifespan** | **Async context-manager factory called once on startup / shutdown – perfect for DB connections, warm-up tasks, etc. When omitted FastMCP supplies a no-op lifespan (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **Serialization & caching** | **tool\_serializer** | **Callable that converts non-JSON-serialisable return values (e.g. Pandas DF → CSV) into strings before they are sent to the client (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
|  | **cache\_expiration\_seconds** | **TTL for FastMCP’s built-in TimedCache (used by Resources & Tools with cache=True). 0 disables caching (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
|  | **mask\_error\_details** | **When True tool/resource exceptions are stripped to a generic message before reaching the client – useful for production security (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **Duplicate-handling policy** | **on\_duplicate\_tools on\_duplicate\_resources on\_duplicate\_prompts** | **Strategy when you register two objects with the same name: "warn" (default), "error", "replace", or "ignore" (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**,** [**gofastmcp.com**](https://gofastmcp.com/servers/tools?utm_source=chatgpt.com)**)** |
| **URI formatting** | **resource\_prefix\_format** | **How FastMCP prefixes templated resources – "path" (modern default) or legacy "protocol" (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**,** [**gofastmcp.com**](https://gofastmcp.com/servers/composition?utm_source=chatgpt.com)**)** |
| **Selective exposure** | **include\_tags, exclude\_tags** | **Sets of OpenAPI tags; only tools/resources whose tags match include (and not in exclude) are exposed. Handy for multitenant or staged roll-outs (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **Composition** | **tools** | **List of Tool objects or plain callables. They are auto-wrapped and registered at construction time (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
|  | **dependencies** | **Extra Python-module names that FastMCP should watch for hot-reload (or bundle when using the CLI build command) (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |
| **Deprecated (2.8+)** | **log\_level, debug, host, port, sse\_path, message\_path, streamable\_http\_path, json\_response, stateless\_http** | **Legacy per-server runtime flags. Keep them at None; today you supply these values when you call mcp.run() instead (**[**github.com**](https://github.com/jlowin/fastmcp/raw/main/src/fastmcp/server/server.py)**)** |

### **Typical minimal usage**

**from fastmcp import FastMCP**

**mcp = FastMCP(**

**name="Cybereason Demo",**

**instructions="Provide Cybereason security APIs to the LLM.",**

**on\_duplicate\_tools="error", # fail fast during start-up**

**resource\_prefix\_format="path",**

**)**

### **Why you might reach for the advanced knobs**

* **tool\_serializer – return a Matplotlib figure or a bytes object exactly once without re-implementing every tool.**
* **lifespan – open a PostgreSQL pool, push Prometheus gauges, or seed a cache.**
* **include\_tags / exclude\_tags – publish a “beta” set of tools to early-access users while hiding them from everyone else.**
* **mask\_error\_details – avoid leaking stack traces that contain internal hostnames or secrets.**

**Those are all the knobs FastMCP currently exposes—everything else (TLS, transports, workers) is configured later when you call run() (or via global fastmcp.settings).**

5. Different between the two implementations?

**Answer:**

### **Short answer**

**Running the FastMCP server itself is free-–it’s just Python code.
 What can cost money are the things the server (or client) does on each request:**

| **Potential cost** | **When it applies** | **Who pays** |
| --- | --- | --- |
| **LLM tokens (Azure OpenAI, OpenAI API, Anthropic, etc.)** | **Whenever an LLM is asked to *understand free-text and choose a tool* or *stream a response*** | **Whoever owns the API key used by the FastMCP *router* (your company if the router runs on your server; the customer if the router runs in their client)** |
| **Cybereason API quotas / licence** | **The underlying Cybereason SaaS may meter certain endpoints; check your contract** | **Usually your company (the tenant that owns the Cybereason environment)** |
| **Infrastructure (VM/container, bandwidth)** | **CPU/GPU time to host the FastMCP server, plus egress traffic** | **The party that hosts the server (typically you)** |

### **Two common deployment patterns and who bears the cost**

| **Pattern** | **Where does the LLM reasoning happen?** | **LLM cost borne by…** | **Network cost** |
| --- | --- | --- | --- |
| **“Smart server / thin client” (the POC you asked about earlier)Client sends *plain English* → server’s MCP agent chooses a tool, hits Cybereason** | **Inside the server process (your Azure OpenAI key)** | **You – every chat turn with the server burns tokens** | **One round-trip (client → server, server → Cybereason, back)** |
| **“Smart client / lean server” (FastMCP quick-start) Client has its own agent; it calls /list\_tools, picks the right tool, then hits the tool endpoint with structured JSON** | **In the client’s environment (their own key)** | **Your customer** | **Two round-trips but the server does no LLM work** |

**If you only need machine-to-machine calls (e.g., your UI already knows which Cybereason endpoint to hit), you can bypass the LLM layer entirely. In that case the MCP server is little more than a typed reverse proxy, so the per-call cost is essentially zero beyond ordinary hosting and Cybereason licensing.**

### **How to keep costs predictable**

1. **Token ceilings – Azure OpenAI lets you set usage caps per resource or per key; point the MCP router at a key with a daily limit.**
2. **Rate-limit middleware – Add Starlette middleware to throttle requests per IP or per user.**
3. **Force structured mode – Expose only the /call\_tool path to production clients and require them to specify tool\_name + args explicitly; reserve the natural-language router for internal use.**
4. **Cache read-heavy endpoints – FastMCP’s built-in TimedCache (set cache=True on a tool or adjust cache\_expiration\_seconds) can cut token *and* API usage for idempotent calls.**
5. **Monitor & alert – Stream request/response sizes and token counts to Prometheus or another APM so you notice runaway costs early.**

### **TL;DR**

* **FastMCP code is free; costs arise only from the services it *calls*.**
* **If the LLM router runs on your server, every natural-language query that flows through it will bill your Azure/OpenAI account.**
* **Move the router to the client side (or require direct tool calls) if you want end-users to bear token costs instead.**

6. What mcp.tool() can get as parameters?

**Answer:**

**Let me search for information about the FastMCP `@mcp.tool()` decorator and its parameters.**

**Search files...**

**Ran tool**

**Based on the documentation I found, here are the parameters that the `@mcp.tool()` decorator can accept:**

**## \*\*@mcp.tool() Decorator Parameters\*\***

**The `@mcp.tool()` decorator in FastMCP accepts the following optional parameters:**

**### \*\*Basic Parameters\*\***

**- \*\*`name`\*\* (`str | None`): Sets the explicit tool name exposed via MCP. If not provided, uses the function name.**

**- \*\*`description`\*\* (`str | None`): Provides the description exposed via MCP. If set, the function's docstring is ignored for this purpose.**

**### \*\*Organization & Metadata\*\***

**- \*\*`tags`\*\* (`set[str] | None`): A set of strings to categorize the tool. Clients might use tags to filter or group available tools.**

**### \*\*Control Parameters\*\***

**- \*\*`enabled`\*\* (`bool`, default: `True`): A boolean to enable or disable the tool. Disabled tools won't appear in tool lists.**

**- \*\*`exclude\_args`\*\* (`list[str] | None`): A list of argument names to exclude from the tool schema shown to the LLM. Only arguments with default values can be excluded.**

**### \*\*Annotations\*\***

**- \*\*`annotations`\*\* (`ToolAnnotations | dict | None`): An optional object or dictionary to add additional metadata about the tool.**

**#### \*\*ToolAnnotations Attributes:\*\***

**- \*\*`title`\*\* (`str | None`): A human-readable title for the tool**

**- \*\*`readOnlyHint`\*\* (`bool | None`): If true, the tool does not modify its environment**

**- \*\*`destructiveHint`\*\* (`bool | None`): If true, the tool may perform destructive updates to its environment**

**- \*\*`idempotentHint`\*\* (`bool | None`): If true, calling the tool repeatedly with the same arguments will have no additional effect**

**- \*\*`openWorldHint`\*\* (`bool | None`): If true, this tool may interact with an "open world" of external entities**

**## \*\*Examples\*\***

**### \*\*Basic Usage\*\***

**```python**

**@mcp.tool()**

**def add(a: int, b: int) -> int:**

**"""Adds two numbers together."""**

**return a + b**

**```**

**### \*\*With Custom Parameters\*\***

**```python**

**@mcp.tool(**

**name="find\_products", # Custom tool name**

**description="Search the product catalog with optional category filtering.",**

**tags={"catalog", "search"}, # Tags for organization**

**enabled=True, # Tool is enabled**

**exclude\_args=["api\_key"], # Hide api\_key from LLM**

**annotations={**

**"title": "Product Search",**

**"readOnlyHint": True,**

**"openWorldHint": False**

**}**

**)**

**def search\_products\_implementation(query: str, category: str | None = None, api\_key: str = "default") -> list[dict]:**

**"""Internal function description."""**

**# Implementation...**

**return [{"id": 1, "name": "Product"}]**

**```**

**### \*\*Disabling Tools\*\***

**```python**

**@mcp.tool(enabled=False)**

**def maintenance\_tool():**

**"""This tool is currently under maintenance."""**

**return "This tool is disabled."**

**```**

**### \*\*Excluding Arguments\*\***

**```python**

**@mcp.tool(exclude\_args=["user\_id"])**

**def get\_user\_details(query: str, user\_id: str = None) -> str:**

**"""Get user details. user\_id will be injected by server, not provided by LLM."""**

**# Implementation...**

**return f"Details for user {user\_id}: {query}"**

**```**

**## \*\*Important Notes\*\***

**1. \*\*Functions with `\*args` or `\*\*kwargs` are NOT supported\*\* as tools because FastMCP needs to generate a complete parameter schema.**

**2. \*\*All parameters are optional\*\* - if not provided, FastMCP will use sensible defaults (function name, docstring, etc.).**

**3. \*\*Type annotations are essential\*\* for proper tool functionality as they inform the LLM about expected data types and enable validation.**

**4. \*\*The decorator returns a Tool object\*\*, not the original function, so the decorated function is no longer directly callable from Python code.**

**This gives you fine-grained control over how your tools appear and behave in the MCP ecosystem!**
