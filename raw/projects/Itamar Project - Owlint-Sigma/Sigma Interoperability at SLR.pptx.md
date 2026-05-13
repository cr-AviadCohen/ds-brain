# Sigma Interoperability at SLR.pptx

<!-- Slide number: 1 -->
# Sigma Interoperability
Itamar Hershko

### Notes:

<!-- Slide number: 2 -->
Tipper Pipeline
Motivation & Goals
Architecture
Use Cases
Sigma - Fusion - Splunk
Observability
Q&A

### Notes:
AI for EP Security
AIDRA as a Framework - #key idea, components, architecture, example (ps scripts as a poc, and noa for assembly)
Powershell scripts DEMO #(as poc)
LLM Assembly DEMO #(noa’s poc)
Next steps

<!-- Slide number: 3 -->
# Tipper Pipeline

![](GoogleShape632p57.jpg)

### Notes:
Santis slide

<!-- Slide number: 4 -->
# Motivation
Establish a common unified intermediate language for detection content
Convert Tipper signals and threat reports into validated Sigma rules and SIEM queries
Maximize research impact across platforms through seamless rule translation
Reduce manual triage, rule creation, and validation effort
Turn every report into expanded coverage at scale, automatically and reproducibly.

### Notes:
From Intel Pulse to Deployed Detection
Tipper already gives us early visibility into new threats, variants, and threat actors. The opportunity is to make that intelligence actionable, not let it stop at a notification.
Owlint Sigma closes that gap. It turns every meaningful intel signal into validated detection content, helping us move from “we know about it” to “we are protected against it.”
Amplifying the research team
Today, researchers spend valuable time reading reports, extracting detection logic, and manually writing rules. Owlint Sigma gives them an AI-assisted module that accelerates this workflow, drafts missing detections, validates them, and helps convert research into product-ready coverage faster.
Built to scale with the threat landscape
As intel feeds grow, every new report becomes another opportunity to strengthen coverage. Owlint Sigma is designed for production-volume intelligence, so our detection layer can continuously improve and stay ahead of attackers instead of catching up after the fact.

<!-- Slide number: 5 -->
# Goals
Enable flexible detection workflows
Report → Sigma → SIEM query,
SIEM query → Sigma
triggered by Tipper.
Improve rule quality
Multi-layer validation catches issues from syntax to end-to-end testing, keeping every detection accurate, consistent, and review-ready.
Expand detection coverage
Identify uncovered TTPs, variants, and attacker behaviors, then generate detection logic to close those gaps.

### Notes:
Expand detection coverage
We start by finding the gaps - TTPs, attacker variants, and behaviors no rule covers yet
Owlint reads threat intel and turns those gaps into actual detection logic
Every new report becomes more coverage, automatically
Improve rule quality
Every rule passes through multiple validation layers — syntax, semantics, formatting, and end-to-end testing
The system catches its own mistakes and corrects them before a rule reaches the analyst
What lands in front of the SOC is consistent, accurate, and review-ready
Enable flexible detection workflows
Threat report into Sigma into SIEM query — the standard direction
SIEM query back into Sigma — for migration, portability, or analysis
Both flows triggered automatically by Tipper, no manual handoff

Q: How does the validation work?
Four layers: syntax → semantic → output formatting → end-to-end QA
If any layer fails, the rule goes back to the LLM with the specific error
Up to 3 retry attempts; rules that still fail are skipped, not shipped broken
Q: Why Sigma as the intermediate language?
Vendor-neutral, active community, mature translator backends
Right level of abstraction — behavior, not just indicators
Write once, deploy to 8 SIEMs
Q: What if the LLM gets it wrong?
Validation layers reject bad output before it reaches anyone
Self-heal loop re-prompts with the specific error
Red Team agent reviews every rule for weaknesses
Failed rules are skipped with a documented reason, never shipped
Q: Is this just GPT writing rules?
GPT writes the first draft — the framework makes it shippable
4-layer validation, post-processors, structural checker, RAG dedup, Red Team review
12 closed correctness bugs and 7 architectural principles in the recent cluster
The engineering is around the LLM, not the LLM itself
Q: How accurate is it?
100% structural validity in the latest run
91% honest coverage of step-by-step detection logic across 5 scenarios
676 tests pinning specific behaviors, all passing
Operational FP rate is environment-specific — measured in the SOC, not at generation

<!-- Slide number: 6 -->
# Architecture

### Notes:

<!-- Slide number: 7 -->
# Architecture

![](GoogleShape661p61.jpg)

### Notes:
From Intel Pulse to Deployed Detection
Tipper already gives us early visibility into new threats, variants, and threat actors. The opportunity is to make that intelligence actionable, not let it stop at a notification.
Owlint Sigma closes that gap. It turns every meaningful intel signal into validated detection content, helping us move from “we know about it” to “we are protected against it.”
Amplifying the research team
Today, researchers spend valuable time reading reports, extracting detection logic, and manually writing rules. Owlint Sigma gives them an AI-assisted module that accelerates this workflow, drafts missing detections, validates them, and helps convert research into product-ready coverage faster.
Built to scale with the threat landscape
As intel feeds grow, every new report becomes another opportunity to strengthen coverage. Owlint Sigma is designed for production-volume intelligence, so our detection layer can continuously improve and stay ahead of attackers instead of catching up after the fact.

<!-- Slide number: 8 -->
# Architecture

![](GoogleShape668p62.jpg)

### Notes:
From Intel Pulse to Deployed Detection
Tipper already gives us early visibility into new threats, variants, and threat actors. The opportunity is to make that intelligence actionable, not let it stop at a notification.
Owlint Sigma closes that gap. It turns every meaningful intel signal into validated detection content, helping us move from “we know about it” to “we are protected against it.”
Amplifying the research team
Today, researchers spend valuable time reading reports, extracting detection logic, and manually writing rules. Owlint Sigma gives them an AI-assisted module that accelerates this workflow, drafts missing detections, validates them, and helps convert research into product-ready coverage faster.
Built to scale with the threat landscape
As intel feeds grow, every new report becomes another opportunity to strengthen coverage. Owlint Sigma is designed for production-volume intelligence, so our detection layer can continuously improve and stay ahead of attackers instead of catching up after the fact.

<!-- Slide number: 9 -->
# Use Cases

### Notes:

<!-- Slide number: 10 -->
# Use Cases
Track 1 - Threat Intel to Deployed Rules
Tipper collects threat intel and TTPs from a new APT report. Owlint turns them into validated detection rules across all 8 SIEMs before the SOC starts the next shift.
Track 2 - Sigma Rule Adoption
The community publishes high-quality Sigma rules. Owlint translates them into production-ready queries for your specific SIEM stack - no manual rewriting per platform

Track 3 - SIEM Migration
Migrating from one SIEM to another usually means rewriting hundreds of detections by hand. Owlint converts legacy queries into portable Sigma rules, then translates them into the target SIEM in hours.

### Notes:
From Intel Pulse to Deployed Detection
Tipper already gives us early visibility into new threats, variants, and threat actors. The opportunity is to make that intelligence actionable, not let it stop at a notification.
Owlint Sigma closes that gap. It turns every meaningful intel signal into validated detection content, helping us move from “we know about it” to “we are protected against it.”
Amplifying the research team
Today, researchers spend valuable time reading reports, extracting detection logic, and manually writing rules. Owlint Sigma gives them an AI-assisted module that accelerates this workflow, drafts missing detections, validates them, and helps convert research into product-ready coverage faster.
Built to scale with the threat landscape
As intel feeds grow, every new report becomes another opportunity to strengthen coverage. Owlint Sigma is designed for production-volume intelligence, so our detection layer can continuously improve and stay ahead of attackers instead of catching up after the fact.

<!-- Slide number: 11 -->
# Usage Examples

### Notes:

<!-- Slide number: 12 -->
# CLI Menu

![](GoogleShape694p66.jpg)

### Notes:

<!-- Slide number: 13 -->
# Rule Creation Loop

![](GoogleShape701p67.jpg)

### Notes:

<!-- Slide number: 14 -->
# RAG Collection & Storing

![](GoogleShape709p68.jpg)

### Notes:

<!-- Slide number: 15 -->
# Conversion Mechanism - Fusion

![](GoogleShape718p69.jpg)

### Notes:

<!-- Slide number: 16 -->
# Conversion Mechanism - Splunk

![](GoogleShape728p70.jpg)

### Notes:

<!-- Slide number: 17 -->
# Sigma Rule Example

![](GoogleShape738p71.jpg)
Detects POST requests to the SharePoint ToolPane.aspx endpoint with DisplayMode=Edit parameters - the entry point attackers use to inject malicious WebParts and achieve authenticated remote code execution.
Vendor-neutral source rule that Owlint translates into every SIEM's native query language.

### Notes:

<!-- Slide number: 18 -->
# Fusion Example

![](GoogleShape746p72.jpg)
The same detection logic, now expressed in Fusion's CEF-based DSL with preprocessor scoping - web-server device classes, vulnerability scanner allowlists, DMZ exclusions, and firewall-deny suppression - making the rule deployable across a multi-tenant SOC without alert flooding.

### Notes:

<!-- Slide number: 19 -->
# Splunk Example
The same Sigma logic translated into Splunk SPL, detecting suspicious POST requests to SharePoint ToolPane.aspx with DisplayMode=Edit parameters.
Index-scoped to IIS sourcetypes for performance, with private-IP exclusion to filter scanner noise - outputting key fields for quality triage.

![](GoogleShape754p73.jpg)

### Notes:

<!-- Slide number: 20 -->
Observability Examples

### Notes:

<!-- Slide number: 21 -->
# Langfuse – Forge example

![](GoogleShape767p75.jpg)

![](GoogleShape768p75.jpg)

### Notes:

<!-- Slide number: 22 -->
# Langfuse - RAG example

![](GoogleShape775p76.jpg)

### Notes:

<!-- Slide number: 23 -->
# Langfuse - Local RAG example

![](GoogleShape782p77.jpg)

![](GoogleShape783p77.jpg)

### Notes:

<!-- Slide number: 24 -->
# Langfuse – LLM Translator Example

![](GoogleShape790p78.jpg)

![](GoogleShape791p78.jpg)

### Notes:

<!-- Slide number: 25 -->
# Q & A

### Notes:

<!-- Slide number: 26 -->
# Thank you

### Notes:
