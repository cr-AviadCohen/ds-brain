# Project Data Science Brain
Participants: Aviad Cohen, Guy Kassorla
Itamar Hershko came with the idea of a second brain for personal use.
Aviad and Guy took it further by creating a second brain for the Data Science team.

## meeting summary.

The meeting between Aviad and Guy focuses on the architectural design and implementation of a **"Data Science Brain," a centralized AI knowledge base for their team**, inspired by Andrej Karpathy's "Wiki LLM" concept.

Here is a highly detailed summary of the technical discussions, debates, and action items from the meeting:

**Current State of the "Data Science Brain"**
Aviad explains that he currently has a fully functioning version of the "Brain" running locally on his machine, powered by an instance of Claude. The system operates out of a single Git repository containing several key components:
*   **Raw Material & Wiki:** A directory storing vast amounts of unprocessed data, and a "Wiki" directory containing the processed output. The Wiki is formatted as Obsidian Markdown files, which use YAML frontmatter and double-bracket tags to create a web of interconnected nodes (e.g., linking a note about Inbar as a manager to a note about the Data Science team).
*   **System Instructions:** A `.cloud` folder and `cloud.md` file that serve as the schema and system instructions for the LLM. These define specific commands Claude can execute, such as `ingest`, `query`, and `lint`.
*   **The Ingestion Pipeline:** Currently, Aviad drops new data into an "Inbox" folder. Claude detects this, processes the data into the "Raw" folder, structures it, and pushes the connected notes into the "Wiki". Claude also runs periodic "linting" to find and fix contradictions or broken links within the knowledge graph.

**The Goal: Transitioning to a Global Team Brain**
The central problem is that this system is currently private. The goal is to transform it into a **global brain that serves the entire Data Science team** (Aviad, Guy, Itamar, and Inbar). By doing so, if a team member is working on a new project like "Martin News", their local instance of Claude can connect to the Brain and instantly access the full context of the company, previous discussions, and relevant personnel (like Jose) without needing manual prompting.

**Architectural Proposals and the "Inbox" Rule**
To make the brain global, the team discussed separating the architecture into a server-side processor and client-side access points:
*   **The Server VM:** They propose running a shared Ubuntu Virtual Machine hosting an instance of Claude. This server would run automated background triggers: it would pull from Git every few minutes, check the "Inbox" for new data, ingest it into the Wiki, and perform daily linting.
*   **Local Client Access (MCP & Obsidian):** Each team member would connect to the Brain locally using the Model Context Protocol (MCP) linked to their desktop Obsidian application, which in turn is connected to Git.
*   **The Collision Problem:** Aviad realized a major risk: if everyone's local Claude has full access to the Git repository via Obsidian, a user's local Claude might try to push processed data directly to the Wiki, bypassing the ingestion pipeline and causing sync conflicts.
*   **The Solution:** They agreed on a strict rule—**local instances of Claude are only allowed to read the Wiki for querying, and can only write to the "Inbox" folder**. The Server VM will be the sole entity responsible for taking data from the Inbox and officially merging it into the Wiki.

**The Branching Debate: Unified vs. Split Repository**
A significant portion of the meeting was spent debating how to structure the Git repository to protect the system files:
*   **Aviad’s Split Approach:** Aviad wanted the server to hold the full repository, but local users to clone a restricted branch that *only* contains the data folders (Inbox, Raw, Wiki). He wanted to completely hide the system files (like the `.cloud` code) from the local LLM to physically prevent it from accidentally modifying the architecture.
*   **Guy’s Unified Approach:** Guy argued that maintaining split branches that sync only specific folders is overly complex. She suggested using a single unified branch for everyone and simply hiding the system folders within Obsidian's UI, while strictly instructing Claude not to touch them.
*   **AI Arbitration:** During the meeting, Aviad actually asked Claude if Git natively supports auto-syncing folder subsets across branches. Claude confirmed it does not (without using manual scripts like `git subtree`), effectively proving Guy's point.
*   **Resolution:** Aviad conceded, and they agreed to use a **single unified branch**. To ensure safety, they will create a highly robust "Skill" (a custom system prompt) for the local Claude instances, explicitly defining its boundaries so it knows how to query data and push to the Inbox without corrupting system files.

**Next Steps and Team Dynamics**
Aviad noted he would feed the meeting transcript to Claude to automatically generate action items, and they plan to physically sit together in the office the next day to build the solution. However, this will have to wait until after Aviad finishes an upcoming presentation and meets with Inbar.

The meeting highlighted a highly collaborative dynamic, with Aviad explicitly thanking Guy for arguing with him, noting that constructive pushback is the best way to refine complex architectural designs.

Finally, before closing the call, Aviad mentioned a concerning update regarding the team they are collaborating with on the "Martin News" project: it appears that team works directly inside AWS workspaces and **does not even use Git for version control**, relying instead on downloading code as ZIP files.