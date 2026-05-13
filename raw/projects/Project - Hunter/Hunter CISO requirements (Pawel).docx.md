# Hunter CISO requirements (Pawel).docx

* + - the data is not leaving through any other channels, so web search will be restricted.
    - security groups setup: for example: GTO analysts will be in the GTO analysts group, and will have access only to the data of the customers they are entitled to. (this wasnt a problem because they usually have access to all the customers, they didnt really have to limit that in the queries). The same goes for spiderlabs (they had slightly broader access).

The problem starts when you want to give access to other personnel. for example potentially customers that obviously should have access only to their own data. The requirement was that this should be enforced through the backend and not through the AI prompt because it’s easy to bypass.

* they were concerned by the prompt if it’s read only or also write access - for hunter it’s read only from the beggining
* what they have in hunter is good enough for internal usage. When we want to move it into a broader stage we’ll have to discuss it again.

Generally speaking:

AWS Bedrock - they are using it because they are “all in” AWS.

Bedrock is FedRAMP compliant (FedRAMP compliant (technically, "FedRAMP Authorized") means the cloud-based AI service has met the rigorous security standards required by the U.S. federal government to process, store, or transmit federal data.)

they were concerned about data privacy - dont want the customers data that is used by the LLM to be trained on or something like that.

They already have customer data under AWS, it’s an openSearch instance hosted there, so if something leakes, it would leake also from the hunter instance.

opensearch - all of the data from fusion starts in 2 opensearch clusters:

1. one for the raw data
2. second for the findings (security incidents)

MCP is lying on the same server, it’s a plug-in to that open web ui that is running the interface. They wrote that connector themselves. It's an open search connector that sends the query and gets the result back to hunter

GTO Analysts feedback.

AlertLogic is only maintaining one project and so they won't have to be a part of the AI in dev meetings. first tuesday of the month - my team, 2nd is Santi, 3rd is Gienel.
