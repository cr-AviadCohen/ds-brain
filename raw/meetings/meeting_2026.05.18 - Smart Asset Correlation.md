Meeting Date: May 18, 2026
Project: Smart Asset Correlation
Participants:
- Xin Tang (Data Engineer/Architect, Phoenix XDR)
- Inbar Dekel (AI/Data Science Team Lead)
- Aviad Cohen (AI Architect)
- Guy Michaela Kassorla (Data Scientist)
- Adria (Product Manager, Phoenix XDR)

Here is a comprehensive and detailed summary of the "Smart Asset Correlation" meeting, structured to capture the technical, architectural, and strategic nuances discussed by the teams.

# Meeting Summary

## 1. Executive Summary
*   **Purpose:** The meeting was a deep dive and knowledge transfer session led by Xin Tang for the AI/Data Science team (Inbar, Aviad, and Guy). The focus was on the data modeling and architecture for "Smart Asset and Identity Correlation" within the new XDR platform (Phoenix).
*   **The Core Problem:** Customers use multiple security integrations (AWS, Azure, CrowdStrike, etc.) that report the same physical assets and users multiple times, requiring a system to merge and correlate them into single identities.
*   **Current Progress:** Xin’s team has completed "Phase 1", which successfully merges assets based on exact matching keys (e.g., matching device IDs from vendor APIs). 
*   **The Request for the AI Team:** The AI team is tasked with building a secondary, asynchronous machine learning/rules-based service (Phase 2/Mode 3) to infer complex behavioral relationships between assets based on raw event data (e.g., inferring a user "owns" a machine because they log into it frequently).
*   **Key Technical Constraint:** The AI correlation service will query a central ClickHouse database containing up to 15 petabytes of data. The team must utilize pre-filtering "rules" to reduce data loads and ensure they do not exhaust the database's computing resources.

## 2. Meeting Context
*   **What the meeting was about:** Defining how the XDR system models "assets" (machines, users) versus "instances" (vendor-specific logs of those assets), and detailing the AI team's role in correlating these entities using behavior-based logic.
*   **Main Participants:** 
    *   *Xin Tang:* The primary speaker, likely a lead data engineer or architect for the Phoenix XDR platform, explaining the data models and database schemas.
    *   *AI/Data Science Team:* Inbar Dekel (Team Lead), Aviad Cohen (AI Architect), and Guy Michaela Kassorla (Data Scientist).
*   **Background:** The company is building an XDR platform called Phoenix. To effectively execute automated threat responses (like isolating a machine or deleting an account), the system must have a perfectly merged view of all assets associated with a specific threat. 

## 3. Key Topics Discussed

**Topic 1: Asset Instances vs. Canonical Assets**
*   **What was discussed:** The fundamental data model for the XDR platform divides assets into two layers to handle data from multiple integrations.
*   **Details:** 
    *   **Instance Layer:** The raw record reported directly by a specific integration (e.g., an EC2 instance reported by AWS, or the same machine reported by a Cyber EDR tool). A single physical machine might have multiple instances.
    *   **Canonical Layer:** The unified, real-world physical machine or user. The system uses matching logic (like shared IPs or hostnames) to link multiple instances into one canonical asset. 

**Topic 2: Inventory Data vs. Discovered Data**
*   **What was discussed:** The two different ways the system ingests asset information.
*   **Details:** "Inventory" data comes directly from vendor APIs (e.g., asking AWS for a list of endpoints) and serves as the ultimate ground truth. "Discovered" data is parsed from raw behavioral events (logs) when no API endpoint is available. Discovered data will never overwrite Inventory data to preserve the ground truth.

**Topic 3: Architectural Flow and the AI Team's Role**
*   **What was discussed:** How the AI team's behavioral correlation service will integrate into the existing architecture.
*   **Details:** The AI team will build a scheduled, independent service that periodically queries the **ClickHouse database** (a column-based data warehouse storing all raw, parsed event data). The service will use behavioral rules and ML to find relationships, then write its findings (with a confidence score) to a separate **PostgreSQL database (TB)**, which handles relational transactions.

**Topic 4: Database Performance and Filtering Rules**
*   **What was discussed:** The critical need to avoid crashing the ClickHouse database.
*   **Details:** Because the XDR platform handles roughly 2,000 organizations and up to 15 petabytes of data, the AI team cannot run models against the raw dataset. They must define "rules" (domain-specific SQL queries) to pre-filter and shrink the data payload before applying any ML models. Xin noted there is currently only one ClickHouse node, making resource preservation vital.

## 4. Decisions and Agreements
*   **Development Language:** Aviad confirmed that since the AI service is asynchronous and primarily waits on database queries, the team can use Python rather than being forced to use a faster language like Rust.
*   **Environment Usage:** The AI team will use the 'Dev' environment to access raw ClickHouse events because it allows for faster iteration, though they can use 'Staging' for more stable portal functionality.
*   **Parallel Development:** The AI team is free to begin working on "Phase 2 / Mode 3" (Behavior Inferred relations) immediately in parallel with Xin's ongoing work on Phase 1. 

## 5. Action Items

| Action Item | Owner | Deadline | Context / Notes |
| :--- | :--- | :--- | :--- |
| **Create a dedicated Slack channel** | Aviad | Completed | Aviad opened the channel during the meeting to share links, repos, and Confluence docs. |
| **Share GitHub and Database access/links** | Xin Tang | Not specified | Xin needs to drop the links to the Phoenix repos, documentation, and ClickHouse DB into the new Slack channel. |
| **Define correlation filtering rules** | AI Team / Domain Experts | Not specified | The AI team needs to collaborate with domain experts (potentially "Hen's team" or "Fear/Three") to define the rules needed to filter data before applying ML. |
| **Set up a weekly sync meeting** | Adria (PM) / Inbar | Next week | Inbar will contact the product manager, Adria, to schedule a recurring alignment meeting. |

## 6. Open Questions / Unresolved Issues
*   **Who owns the correlation "rules"?** There is slight confusion over who will write the actual rules used to filter data. Xin suggested the AI team needs researchers to help write them, while the AI team noted that the necessary domain experts ("Hen's team") are currently at capacity.
*   **Schema/Data Validations:** Aviad noted that the data schemas presented by Xin lacked strict definitions for mandatory vs. optional fields, though Xin clarified that most fields are optional except for primary keys. 

## 7. Risks and Concerns
*   **Database Overload:** There is a severe risk of the AI service consuming too much memory/CPU from the single ClickHouse database node if queries are poorly optimized.
*   **Domain Knowledge Bottleneck:** The AI team lacks the cybersecurity domain knowledge required to know *what* behaviors indicate a valid relationship between a user and a machine. If they cannot secure time from the research team to build these heuristic rules, the project will stall.

## 8. Strategic Implications
*   **Crucial for Automated Response (MDR):** Proper asset correlation is not just a display feature; it is strategically critical for the product's response capabilities. If the system cannot accurately group all instances of a compromised user, automated actions (like isolating a machine or disabling an account) will fail or be incomplete. 
*   **False Negatives vs. False Positives:** In the context of asset merging, Xin indicated that over-merging (false positives in correlation) is preferable to missing an asset (false negatives) because it ensures malicious activity is fully contained, even if it occasionally scopes in extra assets. 
*   **Scaling Threat Detection:** By enriching detections with correlated assets, the XDR platform will allow analysts to query past events related to newly discovered hostnames or MAC addresses across *all* vendor integrations simultaneously. 

## 9. Important Quotes or Signals
*   *On the difference between instance and asset:* "Instance is what you see and asset is the true asset... the only one that you want that the instances are correlated to." *(Aviad Cohen)*.
*   *On architectural priorities:* "We mainly trust the information for what we can get from the Vendor... This is the final truth always a fan of truth ground truth from the vendor directly." *(Xin Tang)*.
*   *On system limitations and the need for rules:* "Because the click house may contain a tons of data and you must filter them out before you apply some machine learning models. So you cannot apply the machine learning models on the entire data." *(Aviad Cohen)*.
*   *On language choice:* "Most of the time you is waiting to waiting the response of a database. So it's not a very high transparent or very low latency required from your language... it's fine if you are more familiar with Python." *(Xin Tang)*.

## 10. Recommended Follow-Up
*   **Who should be contacted:** Inbar should immediately reach out to "Hen" or the relevant threat research leads to secure bandwidth for defining the behavioral filtering rules.
*   **What should be clarified:** The exact schema mapping between the ClickHouse database (where events live) and the PostgreSQL/TB database (where relationships will be stored) needs to be reviewed by Aviad once access is granted.
*   **What documents/plans should be created:** A preliminary queries/rules document outlining exactly what SQL logic will be used to extract subsets of data from ClickHouse. 
*   **What should happen before the next meeting:** The AI team must successfully authenticate into the 'Dev' ClickHouse environment and execute a successful test query to view the raw data schemas.