# OWLINET

Source: `OWLINET.drawio` (drawio)

## Page: Page-1

- Knowledge Base
- 1. INGESTION LAYER
- API Gateway
- Auth Check
- Redis Cache
- MCP Scraper
- Action: Attach TenantID
- Enforce Rate Limits
- Zero-Cost Dedupe:
- Returns cached JSON if
- URL hash exists
- Sanitization Stack:
- Puppeteer + Readability.js
- Output: Clean Markdown
- Drop Request &
- Return cached result
- 2. TRIAGE LAYER
- Redis Queue
- Small AI Model
- Actionable?
- Model: Llama-3.2-3B / Phi-4 / Gemma-3
- Run on: CPU or Cheap GPU
- Task: Filter Noise
- NOISE: Marketing, Patch Notes
- SIGNAL: IOCs, TTPs, Analysis
- Archive & Drop
- 3. THE FORGE
- Redis Queue
- 🦉 OWLINT Engine
- Vector DB
- Golden YARA Set
- Syntax Rules
- Orchestrator: LangGraph
- Observability: LangFuse
- Validation: Pydantic
- POC (ORCH): GPT-5.1-mini / Claude 3.5 API
- PROD: Fine-Tuned Llama-3-70B
- or Mistral Codestral 22B
- (Secure / Self-Hosted)
- 4. SELF-HEALING QA
- Syntax OK?
- FP Check?
- Clean Index
- Enrichment
- 5. DELIVERY & ALERTING
- Postgres DB
- XDR / MalOp API
- 📦 FINAL OUTPUT
- 1. Valid YARA Rule (.yar)
- 2. Enriched JSON Report
- 3. MalOp Context Update
- Data Partitioned
- by TenantID
- Active Enrichment:
- Match IOCs in Report
- to Open MalOps
- New
- Cached
- Noise
- Yes
- RAG: Inject Style
- Error: Retry Loop
- Pass
- Pass
- FP Risk: Harden

---

To regenerate visual: install drawio-desktop and run
`drawio -x -f svg "OWLINET.drawio"` then embed `![[OWLINET.drawio.svg]]`.
