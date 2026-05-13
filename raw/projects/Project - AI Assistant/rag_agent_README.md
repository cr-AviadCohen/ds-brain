# Cybereason Knowledge Base RAG Agent

RAG agent that answers questions about Cybereason products using the official Knowledge Base stored in Salesforce. Articles are synced into a Qdrant vector store, and a deterministic LangGraph pipeline handles retrieval and answer generation with exactly **1 LLM call** per query.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Architecture](#architecture)
4. [File Map](#file-map)
5. [Configuration](#configuration)
6. [Salesforce Sync](#salesforce-sync)
7. [Running the Agent](#running-the-agent)
8. [Evaluation](#evaluation)
9. [Testing the Upload Pipeline](#testing-the-upload-pipeline)
10. [How It Connects to the Orchestrator](#how-it-connects-to-the-orchestrator)
11. [Pipeline Step-by-Step](#pipeline-step-by-step)
12. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### 1. Qdrant (Docker)

The RAG agent requires a running Qdrant instance. Start it from the repo root:

```bash
docker-compose -f docker-build/docker-compose.yaml up -d qdrant
```

- REST API: `http://localhost:6333`
- Dashboard: `http://localhost:6333/dashboard`
- gRPC: `http://localhost:6334`

**If Qdrant is not running**, the agent will raise a `ConnectionError` at init time with a clear message. The orchestrator catches this and skips the RAG agent gracefully (all other agents continue working).

### 2. Environment Variables

Add the following to your `.env` file:

```bash
# ── Azure OpenAI (required for the LLM generation step) ──
AZURE_OPENAI_KEY=<your_key>
AZURE_OPENAI_ENDPOINT=<your_endpoint>
AZURE_OPENAI_API_VERSION=<api_version>

# ── Salesforce (required for syncing articles into Qdrant) ──
# Two auth flows are supported (set in rag_config_salesforce.yaml):
#   "client_credentials" (default) -- OAuth2 client credentials
#   "password"                     -- username/password with security token

# Required for both flows:
SALESFORCE_CONSUMER_KEY=<connected_app_consumer_key>
SALESFORCE_CONSUMER_SECRET=<connected_app_consumer_secret>

# Required only for password auth flow:
SALESFORCE_USERNAME=<integration_user_email>
SALESFORCE_PASSWORD=<password>
SALESFORCE_SECURITY_TOKEN=<security_token>
SALESFORCE_DOMAIN=login   # "login" for production, "test" for sandbox

# ── Qdrant (optional, only if auth is enabled) ──
QDRANT_API_KEY=<your_key>
```

**Embeddings are local** -- the `BAAI/bge-base-en-v1.5` model is downloaded from HuggingFace on first run (~440 MB). No API key is needed (but `HF_API_KEY` can help if you hit download rate limits).

### 3. Install Dependencies

```bash
uv sync
```

Key packages: `simple-salesforce`, `langchain-qdrant`, `langchain-huggingface`, `sentence-transformers`, `beautifulsoup4`.

---

## Quick Start

```bash
# 1. Start Qdrant
docker-compose -f docker-build/docker-compose.yaml up -d qdrant

# 2. Run the initial full sync (Salesforce -> Qdrant)
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_upload

# 3. Run the agent in CLI mode
uv run python -m agents.cybereason.agent_cr_rag_salesforce.agent_rag_salesforce
```

---

## Architecture

### Three-Stage Retrieval Pipeline

```
Query
  │
  ▼
Stage 1: Vector Search (Qdrant)
  Embed query with bge-base-en-v1.5 -> fetch top_k=20 candidates -> score_threshold=0.3
  │
  ▼
Stage 2: Cross-Encoder Reranking
  Rerank all 20 candidates with ms-marco-MiniLM-L-6-v2 -> keep top 20 (no truncation)
  │
  ▼
Stage 3: LLM Truncation
  Send top 5 reranked documents as context to the LLM
```

### Query Graph

```
                         ┌─── retrieve ────────┐
                         │  (3-stage pipeline)  │
   START ── classify_query ──┤                  ├── generate ── END
                         │                      │
                         └─── retrieve_by_id ──┘
                              (article lookup)
```

| Node | LLM Call | What It Does |
|------|----------|--------------|
| `classify_query` | No | Regex check: does the query contain an article number (e.g. `#000012345`)? |
| `retrieve` | No | 3-stage pipeline: vector search (20) -> rerank (20) -> truncate to 5 for LLM |
| `retrieve_by_id` | No | Fetch all chunks for a specific article number from Qdrant via `scroll_by_field` |
| `generate` | **Yes (1)** | System prompt + retrieved context + user question -> LLM answer with citations |

Routing: if the query references a specific article (`#000012345`), it goes to `retrieve_by_id`. Otherwise it goes to `retrieve` (semantic search).

### Ingestion Pipeline

```
Salesforce Knowledge API
        │
   rag_upload.py  (full or delta sync)
        │
   SOQL query ──▶ Clean HTML (BeautifulSoup) ──▶ Chunk (1000 chars / 200 overlap)
        │
   RAG.upload_documents() ──▶ Embed (bge-base-en-v1.5) ──▶ Upsert to Qdrant
        │
   Verify (cross-check SF article count vs Qdrant)
```

### Class Hierarchy

```
Agent (base)
  └── Agent_RAG (abstract: classify -> retrieve -> generate graph, default source formatting)
        └── Agent_RAG_Graph (concrete: Salesforce KB, overrides format_sources)

RAG (generic pipeline: VectorStore + reranker + 3-stage retrieve)
  └── used by Agent_RAG (via rag_instance)
  └── used by SalesforceKnowledgeUpload (via rag.upload_documents)

QdrantVectorStore (langchain-qdrant)
  └── Flat_Payload_Qdrant_Vector_Store (flat payload read/write for existing collection)
```

### Shared Utils

| Module | Role |
|--------|------|
| `utils/rag/rag.py` | `RAG` class, `Rag_Reranker`, `create_embeddings`, `create_text_splitter` |
| `utils/rag/rag_qdrant.py` | Low-level Qdrant helpers: `create_qdrant_client`, `init_qdrant_collection`, `delete_by_field`, `scroll_by_field` |
| `utils/rag/rag_eval.py` | `Rag_Evaluator`, `Eval_Report`, `build_collection_name` -- generic retrieval metrics (Hit@K, MRR, nDCG) |
| `utils/rag/rag_generate_test_set.py` | `generate_test_set()` -- LLM-powered QA pair generation with async parallelism, incremental save, and resume |
| `utils/agents/agent_rag.py` | Abstract `Agent_RAG` with LangGraph pipeline and default `format_sources` |

---

## File Map

```
agent_cr_rag_salesforce/
├── README.md                        # This file
├── rag_config_salesforce.yaml       # All RAG settings (vector store, SF, embedding, chunking, retrieval, reranker, LLM)
├── agent_rag_salesforce.py          # Agent_RAG_Graph class + create_rag_agent() factory
├── rag_upload.py                    # Ingestion pipeline: Salesforce -> Qdrant (full + delta sync)
│                                    #   also defines Flat_Payload_Qdrant_Vector_Store, Rag_Config_Salesforce
├── rag_generate_test_set.py         # Test set generation: fetch SF articles -> LLM QA pairs (--sample, --concurrency)
├── rag_eval_salesforce.py           # Retrieval evaluation: run_eval() with Flat_Payload_Qdrant_Vector_Store
├── rag_eval_test_set_salesforce.json # Golden test set: queries with expected url_name identifiers
├── eval_configs/                    # Experiment config YAMLs for A/B evaluation runs
├── eval_results/                    # Evaluation outputs (one subdir per config_name)
│   └── <config_name>/
│       ├── eval_report.json         # Full per-query results
│       ├── eval_stats.json          # Aggregate metrics
│       └── eval_results.csv         # Results in CSV format
├── _dev/
│   ├── tasks.md                     # Development task tracker
│   ├── test_upload.py               # Upload pipeline test harness (temp collection, 5 articles)
│   └── agent_rag_react/             # Legacy ReAct agent (retained for comparison)
│       ├── agent_rag_react.py       # ReAct agent (2-3 LLM calls/query)
│       ├── tools_rag.py             # SearchDocumentationTool, GetArticleByIdTool
│       └── test_tools_rag.py        # Tool-level tests
└── __init__.py
```

---

## Configuration

All RAG settings are in `rag_config_salesforce.yaml`:

### Vector Store

| Setting | Default | Description |
|---------|---------|-------------|
| `vector_store.url` | `http://localhost:6333` | Qdrant endpoint |
| `vector_store.collection_name` | `salesforce_knowledge` | Qdrant collection name |

### Salesforce

| Setting | Default | Description |
|---------|---------|-------------|
| `salesforce.object_name` | `Video__kav` | Salesforce Knowledge object (KnowledgeArticleVersion) |
| `salesforce.language` | `en_US` | Article language filter |
| `salesforce.auth_flow` | `client_credentials` | OAuth2 flow (`client_credentials` or `password`) |
| `salesforce.instance_url` | `https://cybereason.my.salesforce.com` | Salesforce instance URL |
| `salesforce.api_version` | `64.0` | Salesforce REST API version |
| `salesforce.sync_schedule` | `weekly` | Intended sync cadence |

### Embedding & Chunking

| Setting | Default | Description |
|---------|---------|-------------|
| `embedding.model_name` | `BAAI/bge-base-en-v1.5` | Local HuggingFace embedding model (768 dimensions) |
| `chunking.strategy` | `recursive` | Splitting method (`recursive`, `character`, `token`, `markdown`) |
| `chunking.chunk_size` | `1000` | Max characters per chunk |
| `chunking.chunk_overlap` | `200` | Overlap between consecutive chunks |

### Retrieval (Three-Stage Pipeline)

| Setting | Default | Description |
|---------|---------|-------------|
| `retrieval.top_k` | `20` | Stage 1: candidates to fetch from vector search |
| `retrieval.score_threshold` | `0.3` | Stage 1: minimum cosine similarity |
| `reranker.enabled` | `true` | Stage 2: enable cross-encoder reranking |
| `reranker.model_name` | `cross-encoder/ms-marco-MiniLM-L-6-v2` | Stage 2: reranker model |
| `reranker.top_k` | `20` | Stage 2: candidates to rerank (all retrieved) |
| `llm.top_k` | `5` | Stage 3: documents sent to the LLM after reranking |

---

## Salesforce Sync

### Full Sync

Fetches **all** published Knowledge articles, recreates the Qdrant collection from scratch, chunks, embeds via the `RAG` class, and upserts:

```bash
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_upload
```

### Delta Sync

Fetches only articles modified since the last sync. Updated articles are re-embedded; archived articles are deleted from Qdrant:

```bash
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_upload --delta
```

If no previous sync timestamp is found, delta sync falls back to a full sync automatically.

### Run Delta Sync Daily at 00:00 (cron)

Use the wrapper script:

```bash
/home/opc/code/AI-Assistant/scripts/run_sf_delta_sync.sh
```

Install a cron job:

```bash
crontab -e
```

Add this line:

```cron
0 0 * * * /home/opc/code/AI-Assistant/scripts/run_sf_delta_sync.sh
```

This runs every day at midnight (server local time) and writes logs to:
`/home/opc/code/AI-Assistant/logs/sf_delta_sync/`

### How It Works

1. **SOQL query** fetches articles from the `Video__kav` object (`PublishStatus = 'Online'`, `IsLatestVersion = true`, `Language = 'en_US'`).
2. **Deduplication** keeps only the latest `VersionNumber` per `UrlName`.
3. **HTML cleaning** strips tags (BeautifulSoup), normalizes unicode, collapses whitespace.
4. **Text assembly** combines title + classification metadata + summary + all body fields + links + keywords.
5. **Chunking** via `create_text_splitter` from `utils.rag.rag` (1000 chars, 200 overlap). Each chunk carries rich metadata (article_number, title, category, module, version, etc.).
6. **Upload** via `RAG.upload_documents()` -- converts chunks to LangChain `Document` objects, embeds with `BAAI/bge-base-en-v1.5`, and upserts through the `Flat_Payload_Qdrant_Vector_Store` (which stores metadata as flat payload fields).
7. **Verification** cross-checks Salesforce article count vs Qdrant distinct articles, logs mismatches.

### Sync Metadata

Tracked in `data/` at the repo root:
- `sf_sync_metadata.json` -- latest sync timestamp and stats.
- `sf_sync_history.jsonl` -- append-only log of all sync runs.

---

## Running the Agent

### Standalone CLI

```bash
uv run python -m agents.cybereason.agent_cr_rag_salesforce.agent_rag_salesforce
```

### Via the Orchestrator

The agent is registered in the orchestrator as `agent_cr_rag_salesforce`. Enable it in `orchestrator_config.yaml`:

```yaml
orchestrator:
  agents:
    cybereason:
      agent_cr_rag_salesforce:
        enabled: true
        model_id: "gpt-5.2"
        memory_last_x_message: 5
```

Then run the orchestrator normally:

```bash
uv run python -m orchestrator.orchestrator
```

### Example Queries

```
How do I configure sensor policies?
What are the system requirements for the Cybereason sensor?
Tell me about article #000012345
How does the isolation feature work?
What are the steps to investigate a MalOp?
```

---

## Evaluation

Evaluation is a two-step process: (1) generate a golden test set from Salesforce articles, then (2) run retrieval evaluation against the Qdrant vector store.

### Step 1: Generate a Test Set

The test set generator fetches articles from Salesforce, sends each one to an LLM to produce a question + ground-truth answer, and writes the result to JSON. Supports random sampling and parallel LLM calls.

```bash
# Generate from 1000 randomly sampled articles (recommended):
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_generate_test_set \
    --sample 1000 --concurrency 10

# Generate from the full corpus:
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_generate_test_set

# Custom output path:
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_generate_test_set \
    --sample 1000 --concurrency 10 --output my_test_set.json
```

| Flag | Default | Description |
|------|---------|-------------|
| `--sample N` | all articles | Randomly sample N articles from the full Salesforce corpus |
| `--concurrency N` | `10` | Max parallel LLM calls (`1` = sequential) |
| `--output PATH` | `rag_eval_test_set_salesforce.json` | Output JSON file path |
| `--model ID` | `gpt-5.2` | Azure OpenAI deployment ID |
| `--config PATH` | production config | Path to a RAG config YAML |

**Crash resilience:** Progress is saved incrementally to a `.progress.jsonl` sidecar file. If the process is interrupted, rerun the same command -- already-processed articles are skipped automatically. The progress file is cleaned up after the final JSON is written.

### Step 2: Run the Evaluation

Evaluates retrieval quality by querying Qdrant for each test case and measuring whether the expected article appears in the top K results.

```bash
# Default (production config + default test set):
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_eval_salesforce

# With a specific experiment config:
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_eval_salesforce \
    --config eval_configs/phase1_bge_small.yaml

# With a custom test set:
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_eval_salesforce \
    --test-set path/to/test_set.json
```

The eval uses `Flat_Payload_Qdrant_Vector_Store` with `content_payload_key="text"` to match the upload pipeline's flat payload layout. It retrieves all 20 candidates (vector search + reranking, no LLM truncation) so Hit@K metrics reflect full retrieval quality.

### Evaluation Pipeline

```
Test Set JSON
    │
    ▼
For each query:
    │
    Stage 1: Vector Search (top_k=20, threshold=0.3)
    Stage 2: Cross-Encoder Reranking (all 20 candidates)
    (no Stage 3 truncation -- eval sees all 20)
    │
    ▼
Compare retrieved url_names against expected url_names
    │
    ▼
Compute: Hit@K (K=1..20), MRR, nDCG, Context Precision, Context Recall
    │
    ▼
Save to eval_results/<config_name>/
    ├── eval_report.json    # Full per-query breakdown
    ├── eval_stats.json     # Aggregate metrics
    └── eval_results.csv    # Tabular results for spreadsheets
```

### Test Set Format

`rag_eval_test_set_salesforce.json` -- each entry has a query, expected articles (matched by `url_name`), and a ground-truth answer:

```json
[
  {
    "query": "What default port must be accepted when installing sensors on a Mac?",
    "expected_articles": [
      {
        "url_name": "24-1-install-sensors-for-mac",
        "title": "Install Sensors for Mac",
        "evidence": "you must accept the default port of 443"
      }
    ],
    "ground_truth_answer": "You must accept the default port of 443.",
    "query_id": "tc_0001"
  }
]
```

### Metrics

| Metric | Description |
|--------|-------------|
| **Hit@K** | Did the expected article appear in the top K results? (K=1..20) |
| **MRR** (Mean Reciprocal Rank) | Average of 1/rank for the first correct result |
| **nDCG** | Normalized Discounted Cumulative Gain (binary relevance) |
| **Context Precision** | Fraction of top-K results that are relevant |
| **Context Recall** | Fraction of expected articles found anywhere in results |

---

## Testing the Upload Pipeline

A standalone test harness validates `rag_upload.py` against a temporary Qdrant collection using a small sample of 5 articles:

```bash
uv run python -m agents.cybereason.agent_cr_rag_salesforce._dev.test_upload
```

### What It Does

| Step | Description |
|------|-------------|
| **Initialize** | Creates a `salesforce_knowledge_test` collection in Qdrant |
| **Full Sync** | Fetches 5 articles from Salesforce, chunks, embeds, upserts |
| **Collection Stats** | Verifies Qdrant collection is GREEN with expected point count |
| **Delta Sync** | Runs immediately after full sync -- expects 0 changed articles |
| **Retrieval Check** | Runs a test query to verify search returns results |
| **Cleanup** | Deletes the `salesforce_knowledge_test` collection |

The test exits with code 0 on success, 1 on failure. Safe to run at any time -- it never touches the production `salesforce_knowledge` collection.

---

## How It Connects to the Orchestrator

In `orchestrator.py`, the agent is created by `create_rag_agent()`:

```python
from agents.cybereason.agent_cr_rag_salesforce.agent_rag_salesforce import create_rag_agent

if config.is_agent_enabled("agent_cr_rag_salesforce"):
    try:
        agent_cr_rag = create_rag_agent(model_id=..., langfuse_enabled=False, memory_last_x_message=...)
        agents.append(agent_cr_rag)
    except ConnectionError:
        log.warning("RAG agent skipped — Qdrant is not reachable")
```

The `ConnectionError` guard means the orchestrator starts normally even if Docker/Qdrant is down -- the RAG agent is simply unavailable.

---

## Pipeline Step-by-Step

| # | Step | File | Details |
|---|------|------|---------|
| 1 | Collect data | `rag_upload.py` | SOQL via `simple-salesforce`, pagination, two auth flows |
| 2 | Clean & normalize | `rag_upload.py` | HTML stripping (BeautifulSoup), unicode normalization, whitespace collapse |
| 3 | Deduplicate | `rag_upload.py` | Keep only latest version per `UrlName` |
| 4 | Chunk | `rag_upload.py` | `RecursiveCharacterTextSplitter` (1000/200), rich per-chunk metadata |
| 5 | Upload | `rag_upload.py` | `RAG.upload_documents()` -> embed with `bge-base-en-v1.5` -> upsert via `Flat_Payload_Qdrant_Vector_Store` |
| 6 | Verify | `rag_upload.py` | Cross-check SF count vs Qdrant distinct articles |
| 7 | Classify query | `agent_rag_salesforce.py` | Regex: article number present? Route accordingly |
| 8 | Retrieve | `agent_rag_salesforce.py` / `utils/rag/rag.py` | `RAG.retrieve()`: vector search (20) -> rerank (20) -> truncate (5) |
| 9 | Generate | `utils/agents/agent_rag.py` | System prompt + context + question -> LLM answer |
| 10 | Format sources | `agent_rag_salesforce.py` | Salesforce-specific citations: article numbers, versions, dates |
| 11 | No-answer handling | `utils/agents/agent_rag.py` | `NO_RESULTS` context signal -> agent gives honest "I don't know" |
| 12 | Generate test set | `rag_generate_test_set.py` | Fetch SF articles -> LLM QA pairs (`--sample`, `--concurrency`, incremental `.jsonl` save) |
| 13 | Evaluate | `rag_eval_salesforce.py` | `Flat_Payload_Qdrant_Vector_Store` + `RAG.retrieve()` (20 candidates, no LLM truncation) -> Hit@K, MRR, nDCG |
| 14 | Delta refresh | `rag_upload.py` | `--delta` flag, archived article deletion, sync history log |

---

## Troubleshooting

### "ConnectionError: Cannot reach Qdrant"

Qdrant Docker container is not running. Start it:

```bash
docker-compose -f docker-build/docker-compose.yaml up -d qdrant
```

Verify it's healthy:

```bash
curl http://localhost:6333/healthz
```

If you don't need the RAG agent, set `enabled: false` in `orchestrator_config.yaml`.

### First run is very slow

The embedding model (`BAAI/bge-base-en-v1.5`, ~440 MB) and the reranker model (`cross-encoder/ms-marco-MiniLM-L-6-v2`, ~80 MB) are downloaded from HuggingFace on first use. Subsequent runs use the local cache.

### "No document found with article_number='...'"

The article may not have been synced yet. Run a full sync:

```bash
uv run python -m agents.cybereason.agent_cr_rag_salesforce.rag_upload
```

### Delta sync returns 0 articles

This is normal if nothing changed in Salesforce since the last sync. Check `data/sf_sync_metadata.json` for the last sync timestamp.

### Qdrant URL inside Docker vs local development

- **Local dev**: `http://localhost:6333` (default in `rag_config_salesforce.yaml`)
- **Inside Docker**: The `ai_assistant` container reaches Qdrant via `http://qdrant:6333` (Docker service name). You may need to override the URL via environment variable or config.

---

