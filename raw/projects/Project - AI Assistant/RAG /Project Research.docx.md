# Project Research.docx

gpt deep research

# **Building a Salesforce Knowledge–Backed RAG System for Large-Scale “Nest” Documentation**

## **Context and design constraints**

Your documentation already lives inside Salesforce as Knowledge articles, with a schema that includes at least Title and Summary, plus your long “Documentation” field (often a custom field). The two recurring pitfalls for RAG are (a) versioning (retrieving older article versions by accident) and (b) very long, rich-text content that can’t be indexed as a single blob without destroying retrieval quality. Both issues are first-class in Salesforce Knowledge’s API model: articles have version/state fields like PublishStatus and IsLatestVersion, and Salesforce explicitly warns that query behavior differs across API versions and Knowledge configurations.

Salesforce Knowledge has two common “shapes,” and the shape determines what you query:

* In Lightning Knowledge, the article type is determined by RecordType on a concrete object like Knowledge\_\_kav.
* In Salesforce Classic Knowledge, the article type is determined by ArticleType, and concrete objects can be prefixed by the article type name (for example, FAQ\_\_kav).

Those differences matter because your ingestion job should be built to (1) discover the right object(s) and field API names once, and then (2) run stable, repeatable queries thereafter.

## **Fetching the data reliably**

### **Recommended extraction approach**

For a RAG corpus with “a lot of data and long files,” you typically want a two-lane extraction strategy:

* Lane A (initial full load + large deltas): Use Bulk API 2.0 Query (asynchronous SOQL query jobs) when you expect large result sets. Salesforce describes Bulk API 2.0 query jobs as enabling asynchronous SOQL processing for queries returning “large amounts of data (2,000 records or more).”
* Lane B (small deltas / diagnostics / spot checks): Use standard REST API Query for smaller volumes, which returns up to 2,000 records per synchronous request, with pagination via nextRecordsUrl.

This split is practical: Bulk API 2.0 gives you throughput and operational stability for big jobs, while REST Query is helpful for incremental checks, debugging, and low-volume development workflows.

### **Knowledge-specific query rules you must enforce**

The Salesforce Knowledge Developer Guide is explicit that article queries/searches in SOQL/SOSL require that you specify either PublishStatus or Id in the WHERE clause, and that you should filter on a single PublishStatus “for best results.”

Key fields to capture (minimum viable for RAG + governance):

* Stable identifiers: Id (version record), plus the “article-level” identifier if available (often KnowledgeArticleId / Knowledge\_\_ka / similar).
* Version control: PublishStatus, IsLatestVersion, VersionNumber (if available in your org/config).
* Time watermarks: LastPublishedDate (and also LastModifiedDate / SystemModstamp for robust change detection). lastPublishedDate is also shown in the Knowledge REST APIs’ responses.
* Retrieval filters: Language, plus your tags/categories fields (data categories are commonly used with Knowledge and appear in query examples).
* Content fields: Title, Summary, and your long “Documentation” field (often rich text). Title and Summary are standard Knowledge fields.

### **“Always pull the most recent version” in Salesforce terms**

IsLatestVersion indicates whether an article is the most current version, but Salesforce notes it can be true for an online/published version, a draft version (including translations), and even the latest archived version.
Therefore, “latest” for your RAG agent must be defined precisely, usually as:

* Latest published: PublishStatus='Online' (and optionally IsLatestVersion=true, since the online version is also the latest version). Salesforce explicitly notes you can’t filter (PublishState='Online') AND (IsLatestVersion=false) because the online version is the latest version.
* Draft visibility: Draft and archived visibility is permission-gated (for example, “View Draft Articles” / “View Archived Articles”).

A representative SOQL pattern for indexing only published docs (adapt field names to your org):

sql

Copy



SELECT

Id,

KnowledgeArticleId,

Title,

Summary,

Language,

PublishStatus,

IsLatestVersion,

LastPublishedDate,

LastModifiedDate,

VersionNumber,

UrlName,

Documentation\_\_c

FROM KnowledgeArticleVersion

WHERE PublishStatus = 'Online'

AND Language = 'en\_US'

AND LastPublishedDate >= 2026-01-01T00:00:00Z

The use of PublishStatus='Online' and Language='en\_US' aligns with Salesforce Knowledge SOQL samples.

### **Authentication and the integration user**

Salesforce’s REST API guide emphasizes that API access requires a user with API Enabled permission, and it explicitly mentions the Salesforce Integration user license as a way to grant system-to-system integration users full org access while limiting them to API-only operations.

For server-to-server auth, Salesforce’s own guidance for integrations strongly favors a dedicated integration user + OAuth flow. A Salesforce Developer Blog post lays out a best-practice pattern: authenticate via a dedicated app using the OAuth client credentials flow (intended for headless server-to-server connections), producing an access token that runs as the configured integration user; it notes this flow does not produce a refresh token and is designed so clients can request a new access token as needed.

One important 2026-era constraint: Salesforce’s REST API Developer Guide notes that creating connected apps is restricted as of Spring ’26; existing connected apps can continue to be used, but Salesforce recommends using external client apps instead.

Operationally, this means your “best plan” should assume:

* Use an integration user (least-privilege permissions, audited access).
* Use an OAuth flow suitable for headless services (client credentials or another server-to-server flow), implemented through an external client app / connected app as allowed in your org.
* Monitor API limits using the REST API “Limit Info Header,” which is returned on REST API requests and can be used to monitor org API limits.
* Bulk API 2.0 supports the OAuth 2.0 flows supported by Salesforce REST APIs.

## **Keeping the corpus updated without constant polling**

### **Baseline: scheduled incremental sync**

A scheduled job (weekly/monthly, as you suggested) is reasonable when the source isn’t changing continuously. The key is: “scheduled” should not mean “full re-pull.” It should mean delta replication with a stored watermark and idempotent upserts.

The Salesforce Change Data Capture guide describes data replication as (1) initial full copy and (2) continuous synchronization of new/updated data; even if you do not use CDC, that “initial + deltas” structure is still the right mental model.

Practical delta strategy:

* Persist a watermark per ingestion scope (for example, per language, per article type): last\_successful\_sync\_time in UTC.
* Each run queries for records where LastPublishedDate (for published-only indexing) or LastModifiedDate/SystemModstamp (for broader change detection) is greater than the watermark.
* For each matching article version record, compute a content fingerprint (hash of normalized text + key metadata) to decide whether to re-chunk/re-embed.
* Upsert new/changed chunks into the vector store; delete chunks for articles that are now archived or otherwise excluded.

### **When to use Bulk APIs for updates**

For large corpora, Bulk API tooling provides guardrails:

* Bulk API 2.0 query jobs are asynchronous and explicitly designed for large queries.
* Classic Bulk API query can retrieve up to 15 GB of data, split across multiple output files.
* Bulk-query execution can fail if the query doesn’t execute within the standard 2-minute timeout, returning QUERY\_TIMEOUT; Salesforce advises rewriting simpler queries or splitting results (for example, via PK chunking or similar strategies).

Even if you primarily use Bulk API 2.0, these constraints inform your query design: avoid “monster” cross-object queries for ingestion; instead, pull article records efficiently, then enrich in separate steps if needed.

### **Optional: event-driven updates via Change Data Capture**

If you eventually need lower sync latency than weekly/monthly, Change Data Capture (CDC) is Salesforce’s intended mechanism for “continuous synchronization” by publishing deltas (new/changed records) as change events.

CDC specifics that matter for architecture:

* CDC publishes deltas and supports near-real-time synchronization to external systems.
* Subscriptions can be done via CometD, the Pub/Sub API, or Apex triggers.
* Event retention is three days, enabling a subscriber to replay events after downtime.
* Pub/Sub API is based on gRPC + HTTP/2 and delivers event messages in Apache Avro format.

Because CDC coverage depends on which objects are eligible in your org, the best practice is: design your ingestion pipeline so CDC can be plugged in later as a trigger/queue, but do not make CDC a hard dependency for MVP.

## **Chunking and normalization for long, rich-text Knowledge articles**

### **Normalize “Documentation” content before chunking**

Salesforce Knowledge content commonly uses rich text. The Salesforce Lightning component lightning-formatted-rich-text describes rich text as text formatted by HTML tags (and sanitizes/whitelists tags), which is consistent with Knowledge articles storing rich text as HTML-like markup.
Salesforce also notes (in its rich text area help snippet) that rich text size includes HTML tags and that HTML markup is returned through the API.

Therefore, your ingestion pipeline should treat the “Documentation” field as semi-structured HTML and do:

* HTML → text extraction (retain headings, lists, code blocks; drop navigation junk).
* Link normalization (keep URLs as text; consider preserving link targets as metadata if important).
* Boilerplate removal (repeated headers/footers, disclaimers).
* Deduplication (exact or near-duplicate paragraphs across articles).
* Stable section path inference (for example, “Troubleshooting → Login → SSO Token Expired”) to help retrieval.

### **Chunking strategy that stays stable under version updates**

Chunk size is a trade-off: larger chunks preserve more context but reduce retrieval precision and increase cost/latency; smaller chunks improve targeting but can lose necessary surrounding context.

A robust approach for long documentation is structure-first chunking:

* First split by structural boundaries (H1/H2/H3 headings, bullet lists, code blocks, tables).
* Within each section, split into token-sized chunks with light overlap.

If you use OpenAI Vector Stores (managed), OpenAI documents a default chunking of 800 tokens with 400-token overlap, and allows setting chunking strategy with constraints (chunk size 100–4096; overlap ≤ half the chunk size).
Even if you do not use OpenAI Vector Stores, the key takeaway is that overlap should be controlled and not allowed to explode indexing volume.

A practical starting point for Salesforce Knowledge docs:

* Target chunk size: ~500–900 tokens for prose documentation; smaller for code-heavy content.
* Overlap: keep modest (enough to avoid “boundary loss,” but not 50% unless you have strong evidence it helps in your corpus).
* Chunk payload: embed Title + Summary + Section Heading + Chunk Text (concatenated) so that chunks carry enough context to match queries that mention only the article title or a feature name.

### **Metadata you should attach to each chunk**

Metadata is not optional in your situation because you already rely on status, tags, and language filtering.

Recommended minimum chunk metadata:

* article\_id (stable article identifier) + version\_id (version record ID)
* publish\_status, is\_latest\_version, language
* last\_published\_date, last\_modified\_date
* title, section\_path (hierarchical heading path)
* tags/categories (whatever your org uses)
* source\_url (link back to the Knowledge article, for auditing)

This enables strict filters like: only publish\_status=Online, language=en\_US, category constraints per user persona, etc. Salesforce’s own Knowledge REST APIs also expose article URLs and published dates for online articles, which you can store as canonical provenance.

## **Embeddings and retrieval models**

### **Embedding model recommendation**

For high-quality semantic retrieval across long documentation, a strong default is OpenAI text-embedding-3-large:

* Vector length defaults to 3072 for text-embedding-3-large (and 1536 for text-embedding-3-small).
* Max input is 8192 tokens for all OpenAI embedding models, and requests can include up to 300,000 total tokens summed across inputs (per request).
* OpenAI reports text-embedding-3-large has higher MTEB performance than text-embedding-3-small (at higher cost).
* You can reduce dimensionality via the dimensions parameter (supported in the text-embedding-3 family) when you want to trade accuracy for memory/storage.

Cost-aware alternative: text-embedding-3-small can be attractive for large corpora because it is cheaper per token while still strong, and may be “good enough” if you invest in hybrid retrieval + reranking.

### **Retrieval strategy: hybrid first-stage + optional reranking**

Documentation search benefits from *both* semantic similarity and keyword precision (product names, error codes, field API names, acronyms). Modern vector databases explicitly support hybrid retrieval:

* Weaviate hybrid search combines vector search and keyword search (BM25F) and fuses results with configurable weights.
* Pinecone’s hybrid search guidance recommends starting with a single hybrid index for simpler ops, while documenting trade-offs vs separate dense/sparse indexes.
* OpenAI’s Retrieval guide also describes hybrid tuning via weights to balance semantic embedding matches vs sparse keyword matches.

Reranking can substantially improve precision on the top-k retrieved chunks:

* Weaviate supports reranking modules that can rerank results of vector, BM25, or hybrid searches without leaving Weaviate.
* Pinecone describes integrated inference where embedding + reranking can be integrated into database endpoints to reduce orchestration complexity.
* Research comparing cross-encoders and LLM rerankers finds cross-encoders remain competitive and far more efficient, positioning LLM rerankers as a “contender” in an effectiveness–efficiency spectrum rather than a universal replacement.

A strong “best practice” stack for Knowledge docs is:

1. Hybrid retrieval with strict metadata filters.
2. Lightweight reranker on top 20–50 candidates.
3. Send only the top 5–10 reranked chunks to the generation model.

## **Vector store selection and the recommended architecture choice**

### **The capabilities you need from a vector store**

Given your constraints (status/time/version/language filtering, lots of data, long articles), the vector store must support:

* Efficient metadata filtering (status, language, tags/categories, “latest only”) at query time.
* Hybrid search (semantic + lexical), ideally without external systems glued together.
* High-throughput upserts and deletes (for version updates and archiving).
* Clear multitenancy or namespace boundaries (dev/test/prod; language partitions).

### **Primary recommendation: Weaviate for Knowledge-heavy documentation RAG**

Use Weaviate as the default vector database when you want a single system that can do:

* Hybrid retrieval (vector + BM25F fusion)
* Efficient pre-filtering for structured metadata constraints (Weaviate describes pre-filtering and explains why post-filtering can fail under restrictive filters)
* Built-in reranking modules compatible with vector/BM25/hybrid, enabling a clean multi-stage retrieval pipeline without bolting on extra services

This directly matches your “must filter correct information” requirement (status/tags/language) while still giving strong recall on natural-language questions.

### **Strong alternatives depending on deployment preferences**

* Pinecone is a strong choice if you want a fully managed platform with excellent metadata filtering (store key-value metadata and filter during search), and clear documentation around hybrid index trade-offs. It also provides an Inference API for embeddings and reranking, which can simplify ops when you want “one vendor” for indexing.
* Qdrant is compelling when you want open-source/self-host control with strong filtering mechanics: Qdrant describes payload indexes as helper structures that enable effective filtering (and notes that payload indexes extend the HNSW graph, making filtering part of the search traversal).
* OpenAI Vector Stores (managed) are attractive for a fast MVP if you want automatic chunking/embedding/indexing and optional hybrid tuning, but you should evaluate fit vs data size, pricing, and how much customization you need. OpenAI documents chunking defaults, chunking constraints, hybrid weighting controls, and storage-based pricing.

### **Recommendation summary**

* Best default for your stated needs: Weaviate (hybrid + efficient filtering + reranking in one system).
* Best “managed-first” alternative: Pinecone (managed hybrid + metadata filtering + optional integrated inference).
* Best “control/self-host” alternative: Qdrant (filter-aware indexing mechanics).

## **Proposed end-to-end architecture for the project**

The architecture below is designed to meet your requirements: fetch the right versions, keep updated asynchronously, chunk long documents well, and support an AI agent that only answers from the most relevant, properly-filtered context.

### **Core components**

Integration/auth layer

* Dedicated integration user + OAuth-based access via an external client app or connected app, aligned with Salesforce REST API guidance.

Ingestion orchestration

* Scheduler triggers ingestion (weekly/monthly).
* For large pulls, Bulk API 2.0 Query jobs; for smaller checks, REST Query with nextRecordsUrl pagination.
* Capture and log API limit headers for operational visibility.

Raw and canonical storage

* Store raw API responses (for replay/debug).
* Store canonical “article snapshot” objects (normalized text + canonical metadata) keyed by stable article ID + version.

Document processing

* HTML/rich-text normalization (since rich text is HTML-tag formatted and markup can be returned via API).
* Structural parsing to preserve headings and section boundaries.

Chunking + embedding

* Deterministic chunk IDs based on (article\_id, version\_id, section\_path, chunk\_index) so updates are idempotent.
* Embed with OpenAI text-embedding-3-large by default; consider text-embedding-3-small for cost or dimensions to reduce vector size.

Vector database

* Weaviate collections organized by environment and possibly language; store metadata for PublishStatus, Language, tags/categories, etc.

Query-time retrieval

* Enforce filters: PublishStatus=Online, Language=user\_language, plus tag/category constraints.
* Hybrid retrieval (BM25F + vector) and then rerank the candidate set.
* Provide citations/links back to Salesforce Knowledge URLs (available from Knowledge REST “Articles List/Details” patterns).

### **Update mechanics**

Implement updates as a pure function from “Salesforce truth” → “vector store truth”:

* On each sync, query the changed set by watermark.
* For each record, compute fingerprint:
  + If fingerprint unchanged: skip embedding.
  + If changed: re-chunk/re-embed and upsert.
* If article moved to Archived or otherwise excluded: delete all chunk IDs for that article/version.
* Optional future: augment scheduled sync with CDC triggers (near real-time deltas via CometD/PubSub), using event replay for reliability.

### **Implementation phases**

Phase: discovery and schema hardening

* Identify the authoritative Knowledge object(s) used in your org (Lightning: Knowledge\_\_kav; Classic: \*\_\_kav article-type objects), confirm field API names for “Documentation,” tags, categories, and language rules.
* Confirm your allowed auth method (external client app vs existing connected app) and issue integration-user credentials accordingly.

Phase: MVP RAG

* Initial full extraction via Bulk API 2.0 Query to build the first index.
* Basic chunking, embeddings, Weaviate ingestion, and filtered hybrid retrieval.

Phase: production hardening

* Add evaluation harness (golden Q/A set) to tune chunk size, hybrid weights, and reranking depth.
* Add robust monitoring: ingestion lag, chunk counts, embedding cost, retrieval hit-rate, and “no answer found” rate.
* Introduce CDC-based updates if you need fresher data than the scheduled job can provide.

Phase: governance and scaling

* Strict metadata and ACL model (if different users should only see certain categories).
* Retention policies for raw/canonical snapshots.
* Disaster recovery plan for vector index rebuild (Bulk initial load pipeline should be reproducible).

### **One key decision to finalize early**

Define what “most recent” means for your agent: latest published (PublishStatus='Online') vs “latest draft” (requires specific permissions and has different trust implications). Salesforce’s guidance about PublishStatus filtering, permissions, and version visibility makes this a product decision as much as a technical one.

If your goal is a support-grade agent that answers users reliably, “latest published” is typically the best default, and it aligns with Salesforce’s Knowledge REST APIs that explicitly target “online” articles/fields accessible to the user.

project plan- cursor

# **Salesforce Documentation RAG Agent -- Phase 1 (Standalone)**

Build and validate the full RAG pipeline **independently**, with its own config, CLI, and directory. Orchestrator wiring is deferred to Phase 2.

## **Architecture**

## ![](data:image/png;base64...)

##

##

##

##

##

##

##

##

##

##

## **Directory Structure**

All files go under src/agents/cybereason/agent\_cr\_rag/ (alongside other Cybereason agents):

src/agents/cybereason/agent\_cr\_rag/

\_dev/

README.md # Setup guide, .env vars, how to run sync + agent

rag\_config.yaml # Standalone config (Qdrant, SF, embedding, chunking)

sf\_sync.py # Salesforce sync pipeline (full + delta)

tools\_rag.py # SearchDocumentationTool, GetArticleByIdTool

agent\_rag\_react.py # create\_rag\_agent() factory + run\_rag\_react\_agent() CLI

test\_tools\_rag.py # Unit tests



## **1. Dependencies**

Add to pyproject.toml:

### Knowledge Base RAG ###

"simple-salesforce",

"langchain-qdrant",

"beautifulsoup4",



## **2. Standalone Config -- rag\_config.yaml**

Keeps all RAG settings self-contained (not touching orchestrator config yet):

rag:

vector\_store:

provider: "qdrant"

url: "http://localhost:6333"

collection\_name: "salesforce\_knowledge"

salesforce:

object\_name: "Knowledge\_\_kav"

language: "en\_US"

sync\_schedule: "weekly"

embedding:

deployment: "text-embedding-3-large"

dimensions: 3072

chunking:

strategy: "recursive"

chunk\_size: 1000

chunk\_overlap: 200

retrieval:

top\_k: 5



## **3. Qdrant Docker Service**

Add to docker-compose.yaml:

qdrant:

image: qdrant/qdrant:latest

container\_name: qdrant

ports:

- "6333:6333"

- "6334:6334"

volumes:

- qdrant\_data:/qdrant/storage

restart: unless-stopped



## **4. Salesforce Sync -- sf\_sync.py**

**Class:** SalesforceKnowledgeSync

Key methods:

* \_\_init\_\_(config) -- connects to Salesforce via simple-salesforce using .env creds
* full\_sync() -- SOQL query for all PublishStatus = 'Online' articles, clean HTML, chunk, embed, upsert to Qdrant
* delta\_sync() -- query articles modified since last\_sync\_timestamp, upsert or delete
* \_clean\_article(html) -- strip HTML via BeautifulSoup, concatenate Title + Summary + body
* \_chunk\_article(text, metadata) -- RecursiveCharacterTextSplitter with 1000/200 params
* \_init\_collection() -- create Qdrant collection if not exists

Salesforce credentials from .env:

* SALESFORCE\_USERNAME, SALESFORCE\_PASSWORD, SALESFORCE\_SECURITY\_TOKEN
* SALESFORCE\_CONSUMER\_KEY, SALESFORCE\_CONSUMER\_SECRET
* SALESFORCE\_DOMAIN

Delta sync tracks last\_sync\_timestamp in data/sf\_sync\_metadata.json.

## **5. RAG Tools -- tools\_rag.py**

Two tools inheriting from the project's Tool base class:

* \*\*SearchDocumentationTool\*\* -- takes a query string, embeds it, searches Qdrant top-k, returns formatted chunks with article title/number as source citations
* \*\*GetArticleByIdTool\*\* -- retrieves all chunks for a specific article by article\_number (Qdrant payload filter), useful for follow-up "tell me more about article X"

## **6. Standalone Agent -- agent\_rag\_react.py**

Follows the exact pattern from agent\_virustotal\_react.py:

* create\_rag\_agent(model\_id, ...) factory returning Agent\_React\_Langchain
* run\_rag\_react\_agent() CLI entry point -- can test with python -m agents.cybereason.agent\_cr\_rag.agent\_rag\_react
* System prompt focused on searching documentation, citing sources, and saying "I don't have information on that" when retrieval returns nothing relevant

## **7. Environment Variables (new)**

****# Salesforce integration user

SALESFORCE\_USERNAME=...

SALESFORCE\_PASSWORD=...

SALESFORCE\_SECURITY\_TOKEN=...

SALESFORCE\_CONSUMER\_KEY=...

SALESFORCE\_CONSUMER\_SECRET=...

SALESFORCE\_DOMAIN=login

# Azure OpenAI embedding model

AZURE\_OPENAI\_EMBEDDING\_DEPLOYMENT=text-embedding-3-large



## **8. Files Summary**

**Create:**

* src/agents/cybereason/agent\_cr\_rag/\_dev/README.md -- setup docs
* src/agents/cybereason/agent\_cr\_rag/rag\_config.yaml -- standalone RAG config
* src/agents/cybereason/agent\_cr\_rag/sf\_sync.py -- Salesforce sync pipeline
* src/agents/cybereason/agent\_cr\_rag/tools\_rag.py -- retriever tools
* src/agents/cybereason/agent\_cr\_rag/agent\_rag\_react.py -- agent factory + CLI
* src/agents/cybereason/agent\_cr\_rag/test\_tools\_rag.py -- tests

**Modify:**

* pyproject.toml -- add 3 new dependencies
* docker-build/docker-compose.yaml -- add Qdrant service

**NOT touching (Phase 2):**

* orchestrator\_config.yaml
* orchestrator.py

project steps

## **RAG project steps**

**1. Collect the data from salesforce by api**

decide:

* what is in scope
* what is not in scope
* how often the data changes

**2. Clean and normalize the data**

Before indexing, make the documents usable.

* remove duplicates
* fix encoding issues
* strip irrelevant boilerplate
* extract text from PDF / HTML / JSON
* preserve useful metadata like title, source, owner, date, section, URL

**3. Chunk the documents**

Split large documents into smaller pieces that can be retrieved well.

Common chunking strategies:

* fixed-size chunks
* paragraph-based chunks
* section-based chunks
* semantic chunking

You usually also define:

* chunk size
* chunk overlap
* whether metadata is copied into each chunk

**4. Create embeddings**

Convert each chunk into a vector representation using an embedding model.

This lets you compare user questions to document chunks by semantic similarity.

Choices here include:

* embedding model
* vector dimensions
* multilingual support
* cost vs quality tradeoff

Output:

* chunk text
* embedding vector
* Metadata

| **Model** | **Local / API** | **Embedding Size** | **Strengths** | **Notes** |
| --- | --- | --- | --- | --- |
| text-embedding-3-large | API | 3072 | Very high retrieval quality | One of the best performing embedding models for RAG |
| text-embedding-3-small | API | 1536 | Cheap and fast | Great cost/quality balance |
| Cohere embed-v3 | API | 1024 | Strong multilingual retrieval | Optimized for RAG |
| Voyage-large-2 | API | 1536 | Excellent ranking quality | Very strong for long docs |
| Voyage-2 | API | 1024 | High performance retrieval | Good balance of speed and quality |
| Jina Embeddings v3 | API / Local | 1024 | Supports long contexts | Works well for long documents |
| E5-large-v2 | Local | 1024 | Strong semantic retrieval | Good multilingual performance |
| bge-large-en-v1.5 | Local | 1024 | Excellent open-source retrieval | Very popular for RAG |
| bge-m3 | Local | 1024 | Multilingual + dense/sparse hybrid | Strong modern open model |
| Instructor-XL | Local | 768 | Instruction-based embeddings | Good for domain-specific retrieval |
| GTE-large | Local | 1024 | Strong retrieval performance | Efficient open-source model |
| all-mpnet-base-v2 | Local | 768 | Very stable baseline | Extremely widely used |

### **5. Store in a vector database**

Save the embeddings and metadata in a retrieval system.

Examples:

* Pinecone
* Weaviate
* Qdrant
* FAISS
* Chroma
* Elasticsearch / OpenSearch with vector support
* pgvector

Usually each stored record contains:

* chunk ID
* source document ID
* text
* embedding
* metadata

### **6. Build the indexing pipeline**

Create the ingestion pipeline that handles document updates.

This pipeline usually does:

* load document
* parse text
* clean text
* chunk
* embed
* upsert into vector DB
* version or delete old chunks if needed

This can run:

* manually
* on schedule
* on document change events

### **7. Build the query pipeline**

This is the runtime flow when a user asks a question.

Typical flow:

1. receive user query
2. preprocess / rewrite the query if needed
3. embed the query
4. retrieve top-k relevant chunks
5. optionally rerank the results
6. build a prompt with the retrieved context
7. send to LLM
8. return answer

### **8. Add retrieval logic**

Simple vector search is often not enough.

Useful additions:

* metadata filtering
* hybrid search (keyword + vector)
* reranking model
* multi-query retrieval
* parent-child retrieval
* query expansion
* self-query retrieval

Example:
A user asks about “password reset policy in Europe,” and retrieval can filter by:

* region = EU
* document type = policy
* latest version only

**9. Prompt engineering**

Design the prompt that tells the LLM how to use the retrieved context.

Typical rules:

* answer only from the provided context
* say when information is missing
* cite sources
* avoid guessing
* format the answer in a specific structure

Example sections:

* system instructions
* user question
* retrieved context
* answer format

**10. Add grounding and citations**

A good RAG system should show where the answer came from.

This usually means:

* document name
* chunk snippet
* source link
* page / section number if available

This improves trust and makes debugging much easier.

**11. Handle “no answer” cases**

The system should know when not enough evidence exists.

You need logic for:

* low similarity results
* conflicting retrieved chunks
* no relevant source found
* user asks something outside the knowledge base

Instead of hallucinating, it should say something like:

* “I couldn’t find this in the available sources.”

12**. Evaluate the system**

Measure whether the RAG system actually works.

Common evaluation dimensions:

* retrieval quality
* answer correctness
* faithfulness to sources
* completeness
* latency
* cost

You can evaluate with:

* manual test sets
* golden QA pairs
* LLM-as-a-judge
* retrieval metrics like recall@k, precision@k, MRR
* citations panel
* source preview
* conversation history
* admin dashboard

### **13. Maintain and refresh the index**

Documents change, so the RAG system must stay updated.

Ongoing tasks:

* reindex changed docs
* remove deleted docs
* handle versioning
* monitor stale content
* retrain evaluation sets if domain changes

## **Simple architecture summary**

A RAG project usually has **2 main pipelines**:

### **Offline pipeline**

* collect documents
* clean them
* chunk them
* create embeddings
* store in vector DB

### **Online pipeline**

* get user question
* retrieve relevant chunks
* optionally rerank
* send chunks + question to LLM
* generate grounded answer

סיכום מדדי האיוולואציה (RAG Retrieval Evaluation)

## **סיכום מדדי האיוולואציה (RAG Retrieval Evaluation)**

### **1. Hit Rate @ K (שיעור פגיעה ב-K)**

מה זה: בודק אם לפחות מסמך רלוונטי אחד מופיע ב-K התוצאות הראשונות.איך זה מחושב: לכל שאילתה, בודקים אם אחד מה-expected\_articles קיים ברשימת התוצאות עד מיקום K. מחזיר True/False לכל שאילתה, וממוצע על כל השאילתות.מה זה אומר לנו: "כמה פעמים מתוך כל השאילתות המערכת הצליחה להחזיר תוצאה נכונה בתוך K הראשונים?"

* Hit@1 = 80% -> ב-80% מהמקרים, התוצאה הראשונה הייתה נכונה
* Hit@5 = 100% -> ב-100% מהמקרים, התשובה הנכונה הופיעה ב-5 הראשונים

ערכי K שמוצגים: 1, 3, 5, 10, 20

### **2. MRR - Mean Reciprocal Rank (דירוג הדדי ממוצע)**

מה זה: מודד באיזה מיקום המסמך הרלוונטי הראשון מופיע, עם העדפה חזקה למיקומים גבוהים.איך זה מחושב: לכל שאילתה, מוצאים את המיקום הראשון שבו מופיע מסמך רלוונטי, ומחשבים 1/מיקום. ממוצע על כל השאילתות.דוגמאות:

* מסמך נכון במיקום 1 -> RR = 1/1 = 1.0
* מסמך נכון במיקום 2 -> RR = 1/2 = 0.5
* מסמך נכון במיקום 5 -> RR = 1/5 = 0.2
* לא נמצא -> RR = 0.0

מה זה אומר לנו: "כמה גבוה בממוצע המסמך הנכון מופיע בתוצאות?" ציון קרוב ל-1.0 אומר שהתשובה הנכונה כמעט תמיד ראשונה. ציון נמוך אומר שהמערכת מוצאת את המסמך אבל הוא "קבור" עמוק בתוצאות.

### **3. nDCG - Normalized Discounted Cumulative Gain (רווח מצטבר מנורמל)**

מה זה: מדד מתוחכם יותר שמעריך את כל סדר הדירוג, לא רק את המיקום הראשון. נותן "ניקוד" שיורד לוגריתמית ככל שהמיקום יורד.איך זה מחושב: עם binary relevance (רלוונטי=1, לא רלוונטי=0):

* DCG = סכום של (1 / log2(מיקום + 1)) עבור כל מסמך רלוונטי
* IDCG = מה ה-DCG היה אם הסדר היה מושלם
* nDCG = DCG / IDCG

מה זה אומר לנו: "כמה קרוב הדירוג שלנו לדירוג המושלם?" ציון 1.0 = דירוג מושלם. ציון נמוך = מסמכים רלוונטיים מופיעים מאוחר מדי בתוצאות. ההבדל מ-MRR: nDCG מתחשב בכל המסמכים הרלוונטיים, לא רק בראשון.

### **4. Context Precision (דיוק הקשר)**

מה זה: מתוך כל התוצאות שהוחזרו (top-K), כמה מהן באמת רלוונטיות?איך זה מחושב: (מספר מסמכים רלוונטיים ב-top-K) / (מספר תוצאות ב-top-K)דוגמה: אם מ-20 תוצאות רק 1 רלוונטית -> Context Precision = 1/20 = 0.05מה זה אומר לנו: "כמה 'רעש' יש בתוצאות?" ציון גבוה = רוב התוצאות רלוונטיות, מעט רעש. ציון נמוך = הרבה תוצאות לא רלוונטיות מעורבבות. חשוב במיוחד כי כל התוצאות נשלחות ל-LLM כהקשר, ורעש פוגע באיכות התשובה.

### **5. Context Recall (כיסוי הקשר)**

מה זה: מתוך כל המסמכים שהיינו צריכים למצוא, כמה באמת נמצאו?איך זה מחושב: (מספר מסמכים רלוונטיים שנמצאו) / (מספר מסמכים רלוונטיים שהיו צריכים להימצא)דוגמה: אם יש 2 מסמכים רלוונטיים ומצאנו רק 1 -> Context Recall = 0.5מה זה אומר לנו: "האם אנחנו מפספסים מסמכים חשובים?" ציון 1.0 = מצאנו את כל המסמכים שהיינו צריכים. ציון נמוך = יש מידע רלוונטי שהמערכת לא מחזירה.

### **6. Avg Top Score (ציון ממוצע של תוצאה ראשונה)**

מה זה: הציון הממוצע (similarity score) של התוצאה הראשונה בכל שאילתה.מה זה אומר לנו: רמת ה"ביטחון" הממוצעת של המערכת בתוצאה הטובה ביותר. אם זה נמוך, יכול להיות שה-embeddings לא תופסים טוב את הסמנטיקה, או שה-threshold צריך התאמה.

### **7. Avg Result Count (מספר תוצאות ממוצע)**

מה זה: כמה תוצאות בממוצע חוזרות לכל שאילתה.מה זה אומר לנו: אם זה נמוך משמעותית מה-top\_k (שמוגדר ל-20), זה אומר שה-score\_threshold (0.3) מסנן הרבה תוצאות. יכול להצביע על בעיה ב-embeddings או שהשאילתות "רחוקות" מהמסמכים.

### **טבלת סיכום מהיר**

| **מדד** | **שאלה שהוא עונה עליה** | **טווח** | **מושלם** |
| --- | --- | --- | --- |
| Hit@K | "מצאנו תוצאה נכונה ב-K הראשונים?" | 0%-100% | 100% |
| MRR | "כמה גבוה התוצאה הנכונה?" | 0-1 | 1.0 |
| nDCG | "כמה טוב סדר הדירוג?" | 0-1 | 1.0 |
| Context Precision | "כמה רעש יש בתוצאות?" | 0-1 | 1.0 |
| Context Recall | "מצאנו את כל המסמכים?" | 0-1 | 1.0 |
| Avg Top Score | "כמה בטוחה המערכת?" | 0-1 | קרוב ל-1 |
| Avg Result Count | "כמה תוצאות חוזרות?" | 0-20 | תלוי |

Full Filtering Pipeline (in order)

## **Full Filtering Pipeline (in order)**

### **Filter 1: SOQL Query (Salesforce-side)**

Where: \_build\_soql() -- line 301What it does: Only fetches articles that are:

* PublishStatus = 'Online' -- published and visible to customers
* IsLatestVersion = true -- latest Salesforce version of each record
* Language = 'en\_US' -- English only

What it filters out: Draft articles, archived articles, non-English articles, superseded Salesforce revisions

### **Filter 2: UrlName Dedup (Stage 1)**

Where: \_deduplicate\_by\_url\_name() -- line 405What it does: If multiple articles share the exact same UrlName, keeps only the one with the most recent LastPublishedDate

What it filters out: Salesforce API artefacts where the same UrlName slug appears more than once in query results

### **Filter 3: Version Dedup (Stage 2) -- NEW**

Where: \_deduplicate\_by\_version() -- line 419What it does: Groups articles that have a numeric Version\_\_c (like 23.1, 24.1) by their Title. For each group, keeps only the one with the highest version number.

What it filters out: Old product versions (e.g., drops 23.1 and 23.2 when 24.1 exists)What it keeps untouched:

| **Article type** | **Version*c | Passes through? | |---|---|---| | Documentation (versioned) | 23.1, 23.2, 24.1 | Only 24.1 kept | | API Documentation |* (empty)\*** | **Yes** |
| --- | --- | --- |
| Future Phoenix docs | Phoenix | Yes |
| All other Types (FAQ, troubleshooting, etc.) | *(any)* | Yes |

### **Filter 4: Empty Article Skip**

Where: Inside full\_sync() / delta\_sync() -- line 680What it does: Skips articles where the cleaned text content is less than 50 characters

### **Summary Flow**

Salesforce (all articles)

│

▼

Filter 1: SOQL (Online + LatestVersion + English)

│

▼

Filter 2: UrlName dedup (exact slug duplicates)

│

▼

Filter 3: Version dedup (keep highest numeric version per Title) ← NEW

│

▼

Filter 4: Skip empty articles (<50 chars)

│

▼

Qdrant (clean, deduplicated, current-version-only)
