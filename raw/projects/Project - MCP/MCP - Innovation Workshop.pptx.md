# MCP - Innovation Workshop.pptx

<!-- Slide number: 1 -->
# MCP

Data Science Team
Slack channel: mcp

### Notes:
Hi everyone, happy and excited to be here with you.
Today i’ll present our MCP POC.

<!-- Slide number: 2 -->

![](GoogleShape328p57.jpg)
# MCP (Model Context Protocol)
MCP is an open protocol, that specifies how applications provide context to LLMs.
MCP provides a standardized way to connect AI models to different data sources / tools / services.
The world is going to “connect AI with AI” and MCP promotes it.
Protocol
https://modelcontextprotocol.io/
Model
Context

### Notes:
MCP is an open protocol, that specifies how applications provide context to LLMs.
MCP provides a standardized way to connect AI models to different data sources, tools, and services.
Since there is a protocol, different models can use different contexts.
The world is going to “connect AI with AI” and MCP promotes it.

<!-- Slide number: 3 -->
# Use Case
The world is going “connecting AI with AI”
In near future, every organization will have its own AI (local | cloud-based: openAI / Gemini)
We want our clients AI to work with our product, that is allows using MCP standard.

![](GoogleShape341p58.jpg)

### Notes:
So what is the use case we are talking about?
The world is going connecting AI with AI,So we understand, that in the near future, every company or organization will have its own AI, weather it is local or cloud-based, like OpenAI or Gemini.
We want to let our clients AI to communicate with our product – that is allowed using MCP standard protocol.

<!-- Slide number: 4 -->
# POC Goal
Develop an MCP for Cybereason and make it accessible to clients’ AI.
Ex. Customer will have his own AI and would like to perform actions over CR product
Prepare Cybereason for the emerging AI-to-AI paradigm.
Gain knowledge on designing the MCP for production.

![3d White people with dart and target. Success in business. (Provided by Getty Images)](GoogleShape346p59.jpg)

### Notes:
So the goal of our POC is to develop an MCP for Cybereason product, and make it accessible to client’s AI.
For example, the AI of a customer, will have ability to perform actions over CR product.
We now build a POC to demonstrate the capabilities of our MCP and gaining knowledge on how to design MCP for production.
We are now preparing Cybereason for the emerging paradigm of “AI-to-AI”, where autonomous agents collaborate across systems.

<!-- Slide number: 5 -->

![](GoogleShape354p60.jpg)
# Architecture Flow
https://drive.google.com/drive/u/0/folders/1D2QGMcKcUFlXXKC3VsLUss1FiqFp8yNZ

### Notes:
Here I’ll show you the architecture flow of MCP – it is not designed for scale yet.
When we are talking about MCP architecture flow, there are two sides, the client side and the Cybereason side.
On the client side, the user ask its AI LLM/Agent for something. The AI has a connection to various MCPs from different vendors, one of them is Cybereason.If the user asks about something related to Cybereason, the AI should decide to use Cybereason MCP to retrieve data, in order to answer the question.
On Cybereason MCP side we have an MCP client and MCP server.
The MCP Client serves as a facade, and manages the connections with all the different clients.
The MCP server is implemented as simple agent with tools. It gets an input in natural language, and choose which tool to use in order to answer the question. Each tool call an API on Cybereason platform.
In a nutshell, the MCP server exposes the API functionality to interact with, in natural language.
Until now we focused on implementing the MCP server, and we will work on the client after that.
We have implemented various APIs, I will show you on the next slide.
We feel very comfortable with what we did so far on the server, it is not finished yet, but in term of POC it seems good for use.

<!-- Slide number: 6 -->
# Supported APIs
Link to full API Sheet

![](GoogleShape362p61.jpg)

![](GoogleShape363p61.jpg)

### Notes:
Shachar has implemented various APIs from the product, for difference purposes, in different methods (GET/POST/..) and in different complexity levels.
The are simple APIs that doesn’t get any parameter, and there are more complex ones that get a lot of parameters.
Now you can see some statistics about the current status of implementation:
You can see the total number of APIs in NEST, and how many we have implemented so far in MCP.
At the right side you can see a histogram of different methods and complexity of APIs.

<!-- Slide number: 7 -->
# Next Steps
Decide Core / Phoenix / Both:
Broaden the set of API we support in our MCP server (e.g., query)
Raise the MCP Server internally in Cybereason, for testing and user feedback.
Develop our MCP client
Develop Cybereason AI agent

* * Feel free to contact us with more ideas

### Notes:
Regarding the next steps on our MCP project:
First, we need to decide with which version of the product we will integrate: core / phoenix or both.
We will broaden the set of APIs we support on our MCP server.
We are willing to expose our MCP server to be accessible internally in Cybereason for testing, and user feedback.
Develop the MCP client.
Develop an AI agent for Cybereason which will utilize the MCP server so solve complex tasks.

<!-- Slide number: 8 -->
# Live Demo

### Notes:
We will now move to a Live Demo presentation by Shachar.

<!-- Slide number: 9 -->
# Demo inputs
Call a simple api- list_saved_queries  use requests:
return all saved queries
Call more complex api which get parameters- create_user  use requests:
create user- avishahar@test.com, pas, analyst_l3- return bad password error
create user- avishahar@test.com, pasWord123#, analyst_l3- success
Call api all users to see new user- list_users  use requests: return all users
Remove user- delete_user use requests: remove- avishahar@test.com
Call more complex api run_investigative_queries use requests- return all machines, return machines names include e and limit result to 3

### Notes:

<!-- Slide number: 10 -->

Q&A

### Notes:
