# Ask Seinfeld presentation..pptx

<!-- Slide number: 1 -->

![](GoogleShape381p1.jpg)
# Ask Seinfeld
customer support bot
December 2024

### Notes:

<!-- Slide number: 2 -->
# Project Value
Efficiency and Cost Reduction
Streamlining support processes to reduce response times and operational costs.

Enhancing Support Quality
Delivering consistent, accurate, and high-quality assistance.

Empowering the Support Team
Simplifying workflows and freeing up valuable time to focus on more complex issues.

### Notes:
Let me walk you through the key values of this project.
First, Efficiency and Cost Reduction: Optimize support processes to reduce response times and operating costs by using history of previously solved issues.
Next, Enhancing Support Quality: This project is focused on delivering consistent, accurate, and high-quality assistance to ensure a better experience for both customers and team members.
Finally, Empowering the Support Team: By simplifying workflows, we free up valuable time for our support team to focus on more complex and impactful issues, helping them work smarter, not harder.

<!-- Slide number: 3 -->
# Challenges

Stay on context
⇒ Answering relevant queries only

Prioritizing answers
⇒ Time & Context (Jira, Salesforce)

Guarantee an answer on relevant topic
⇒ Even if the data does not exist in Jira or Salesforce

Keep the answers short and concise

### Notes:
One of the challenge was to create a solution that is not answering questions that are not related to the Cybereason.
Another challenges were to prioritize Jira and Salesforce tickets and answer queries that are not related to the Jira and Salesforce from the Nest documentation.
Also we wanted to answer on user’s query even if the data doesn’t exist in Jira or Salesforce so query can be answered from the nest documentation.
we wanted to keep the answers  short and concise

Let’s talk about the architecture and how we solved those challenges

<!-- Slide number: 4 -->
# Technical Architecture

![](GoogleShape401g31babde2973_0_25.jpg)

### Notes:
Regarding architecture:
we have 2 main parts (chat application which is front-end UI and conversation engine which is back-end).

Mongodb communicates with the front-end and save the user’s sessions.
Front-end send API requests to the python application which are stored on google clouds virtual machine.
Backend communicates with pgvector vectorstore to retrieve embeddings for the Jira, Salesforce and Nest documentation based on the user query.

After extraction it goes to the LLM to generate end response. User’s and bot conversations are stored in BigQuery as well as user’s feedbacks. Also we have CI/CD pipeline on Github Actions that builds docker image and push to artifactory.

<!-- Slide number: 5 -->
# Solution Design

![](GoogleShape407g31d1cdd3609_1_5.jpg)

### Notes:
Inside the application design looks like this:

So user send a query to the application. After that semantic router detects if the query is related to our known topics (Politics, coding, finance, etc). If it is related than we return to user predefined answers corresponding to that topic.
After that we check if the query related to Jira and Salesforce. If it is than we retrieve data from the database and answer users question.
If we don’t find relevant information in Jira/Salesforce data then we try to check if we have related documents in the Nest documentation.
If we have than we retrieve data from the database and answer to the query.
If not then we respond with predefined answer that we don’t have necessary information.

<!-- Slide number: 6 -->
# Solution - Response

![](GoogleShape413g31babde2973_0_6.jpg)
The user asks free text queries.

The bot generates a free text answer, based on the most relevant data from the DB.

The response includes links to the sources of relevant information.

### Notes:
The user can ask queries in free text on the on the front-end. Bot will generate a free text answer based on the embedded data in the database. At the end of outputs are links that are pointing where the information actually is.

<!-- Slide number: 7 -->
# Solution - Feedback

![](GoogleShape422g31d1cdd3609_1_11.jpg)

The UI allows customers to give feedback on different aspects of the response.

### Notes:
In the UI Users can leave feedback for us. Either they can press thumbs up or thumbs down buttons, either they can give free text feedback. So we can improve product in the future based on user’s feedback.  Currently it is manually

We can think about automation but it is costly and time consuming.

<!-- Slide number: 8 -->
# Demo
http://cybereasonai.eng.cybereason.net/
‹#›

### Notes:

<!-- Slide number: 9 -->
# Next Steps

Automate Jira / Salesforce tickets data and documentation data scraping process

Slack integration
Create Ask Seinfeld bot from slack

More guardrails
More cases (sport, medical, automotive etc) for the bot to declare are out of scope,
rather than announcing it doesn’t have the information.

Give access to customer support teams
Collect their feedback
Use the feedback to evaluate and improve the product capabilities

Add support for Japanese Language

Create a bot that acts like an agent
This bot acts as a data retrieval helper
We can create a bot that performs actions: open tickets, run searches, calculates analytics etc
‹#›

### Notes:

Automate the process:
Orchestrate Jira and salesforce scraping, regenerate vectorstore on new updates to jira, salesforce, documentation
More guardrails

<!-- Slide number: 10 -->
Thank you

### Notes:
