# Owl Bot

### Overview

Owl Bot is an MCP (Model Context Protocol) server that transforms Notion into an AI-friendly knowledge base for the LevelBlue organization. It bridges IDE environments (Cursor, Claude Code) with the Notion workspace, enabling AI agents and developers to seamlessly search, query, synthesize, and manage knowledge.

Download -

owl-bot.zip
91.7 KiB

---

### What Owl Bot Does

> 💡 Search & Discover — Semantic search across the entire Notion workspace and connected sources

> 💡 Fetch & Read — Retrieve full page content with automatic markdown conversion

> 💡 Synthesize & Answer — Multi-source knowledge synthesis with citations

> 💡 Query Databases — Natural language database queries with filter parsing

> 💡 Manage Tasks — Agent-tracked task lifecycle with live Notion status updates

> 💡 Create & Document — Structured knowledge capture and documentation workflows

---

### Key Numbers

Metric
	
Value

MCP Tools
	
6 registered tools

MCP Resources
	
2 dynamic resources

System Prompts
	
3 context modes

Slash Commands
	
10 workspace commands

Notion Block Types
	
25+ supported

Codebase Size
	
~1,900 lines TypeScript

---

### Tech Stack

Runtime
Node.js 18+ (ES2022 modules)
TypeScript 6.0.2 (strict mode)
Stdio transport MCP server
Dependencies
@modelcontextprotocol/sdk v1.29.0
@notionhq/client v5.16.0
zod v4.3.6
Integrations
Cursor IDE (via MCP)
Claude Code (via MCP)
Notion API

---

### Documentation Index

See the child pages below for full documentation on every aspect of Owl Bot.
- 📄 [Architecture & Project Structure](https://www.notion.so/Architecture-Project-Structure-339ae23bae1d81b99238db3b869ae783?pvs=25)
- 📄 [MCP Tools Reference](https://www.notion.so/MCP-Tools-Reference-339ae23bae1d818f9f81dd5b9a0b6335?pvs=25)
- 📄 [MCP Resources & System Prompts](https://www.notion.so/MCP-Resources-System-Prompts-339ae23bae1d8186941dde1aa6ba122c?pvs=25)
- 📄 [Core Modules Deep Dive](https://www.notion.so/Core-Modules-Deep-Dive-339ae23bae1d8105a7d0feac75468d5f?pvs=25)
- 📄 [Slash Commands Reference](https://www.notion.so/Slash-Commands-Reference-339ae23bae1d812aaf76ebb41ccb2623?pvs=25)
- 📄 [Knowledge Workflows](https://www.notion.so/Knowledge-Workflows-339ae23bae1d81e7966fdb517a2b2216?pvs=25)
- 📄 [Configuration & Setup Guide](https://www.notion.so/Configuration-Setup-Guide-339ae23bae1d81ce8a7dc7fa7285ae88?pvs=25)
- 📄 [Database Operations Guide](https://www.notion.so/Database-Operations-Guide-339ae23bae1d8185b16cc3d9c13ea63a?pvs=25)
- 📄 [Agent Behavior & Auto-Activation](https://www.notion.so/Agent-Behavior-Auto-Activation-339ae23bae1d81f79a11c0a3ff903165?pvs=25)

---

# Subpages Content

---

## Architecture & Project Structure

#### System Architecture

```
graph TD
    A["Cursor / Claude Code"] -->|MCP Protocol| B["Owl Bot MCP Server"]
    B -->|Notion API| C["Notion Workspace"]
    B --> D["Cache Layer"]
    B --> E["Rate Limiter"]
    C --> F["Pages & Databases"]
    C --> G["Connected Sources"]

Cursor / Claude Code

Owl Bot MCP Server

Notion Workspace

Cache Layer

Rate Limiter

Pages & Databases

Connected Sources

MCP Protocol

Notion API

​
```

---

#### How It Works

Owl Bot runs as a stdio-transport MCP server. It is spawned on demand by the IDE (Cursor or Claude Code) and communicates over stdin/stdout using the Model Context Protocol.

> 💡 The server registers 6 tools, 2 resources, and 3 system prompts with the MCP host, which the AI agent can then invoke to interact with Notion.

---

#### Directory Structure

```
owl-bot/
├── src/
│   ├── index.ts                   # Entry point
│   ├── server.ts                  # MCP server initialization
│   ├── notion/                    # Notion API interaction layer
│   │   ├── client.ts              # Singleton client, rate limiting, caching
│   │   ├── search.ts              # Workspace search implementation
│   │   ├── fetch.ts               # Page fetching with recursive blocks
│   │   ├── query.ts               # Database querying with NL parsing
│   │   └── types.ts               # TypeScript type definitions
│   ├── tools/                     # MCP tool implementations
│   │   ├── search-docs.ts         # search_docs tool
│   │   ├── get-page.ts            # get_page tool
│   │   ├── ask-knowledge.ts       # ask_knowledge tool
│   │   ├── query-database.ts      # query_database tool
│   │   ├── list-projects.ts       # list_projects tool
│   │   └── get-aidra-docs.ts      # get_aidra_docs tool
│   ├── prompts/                   # System prompt contexts
│   │   ├── engineering.ts         # Cybereason engineer mode
│   │   ├── aidra-expert.ts        # AIDRA malware analysis mode
│   │   └── knowledge-qa.ts        # General Q&A mode
│   ├── resources/                 # MCP resource providers
│   │   ├── workspace-index.ts     # workspace://index
│   │   └── project-list.ts        # workspace://projects
│   └── utils/                     # Utility modules
│       ├── markdown.ts            # Block-to-markdown conversion
│       ├── cache.ts               # TTL-based LRU cache
│       ├── chunker.ts             # Content chunking for token limits
│       └── errors.ts              # Error handling utilities
├── dist/                          # Compiled JavaScript output
├── .cursor/                       # Cursor IDE integration
│   ├── rules/owl-bot.mdc          # Auto-activation rules
│   └── skills/owl-bot/SKILL.md     # Operational playbook
├── package.json                   # Dependencies & scripts
├── tsconfig.json                  # TypeScript config (ES2022)
├── setup.sh                       # Automated setup script
└── README.md                      # User-facing docs

​
```

---

#### Module Dependency Flow

```
graph LR
    index["index.ts"] --> server["server.ts"]
    server --> tools["tools/*"]
    server --> prompts["prompts/*"]
    server --> resources["resources/*"]
    tools --> notion["notion/*"]
    resources --> notion
    notion --> utils["utils/*"]

index.ts

server.ts

tools/*

prompts/*

resources/*

notion/*

utils/*

​
```

---

#### Component Responsibilities

Layer
	
Module
	
Responsibility

Entry
	
index.ts / server.ts
	
Bootstrap MCP server, register tools/resources/prompts

Tools
	
tools/*.ts
	
Define MCP tool schemas and orchestrate Notion calls

Notion
	
notion/*.ts
	
API client, search, fetch, query logic

Prompts
	
prompts/*.ts
	
Context-specific system prompts for the AI agent

Resources
	
resources/*.ts
	
Read-only MCP resources (workspace index, project list)

Utils
	
utils/*.ts
	
Markdown conversion, caching, chunking, error handling

---

## MCP Tools Reference

All six MCP tools registered by Owl Bot, with full input/output specifications.

---

#### 1. search_docs

> 💡 Semantic search across the entire Notion workspace

Inputs:

Parameter
	
Type
	
Required
	
Description

query
	
string
	
Yes
	
Full-text search query

limit
	
number (1–25)
	
No
	
Max results to return

content_type
	
"pages" | "databases" | "all"
	
No
	
Filter by content type

Output: Formatted list of results with titles, types, URLs, and content previews.

Use when: Finding documentation, locating pages, general discovery.

---

#### 2. get_page

> 💡 Fetch a single Notion page with full content

Inputs:

Parameter
	
Type
	
Required
	
Description

page
	
string
	
Yes
	
Page title, URL, or ID

include_children
	
boolean
	
No
	
Recursively include child blocks

Output: Full page content converted to markdown, including metadata (title, URL, last edited, parent), child page listing.

Use when: Reading full page content, deep-diving into a known page.

---

#### 3. ask_knowledge

> 💡 Multi-source knowledge synthesis with citations

Inputs:

Parameter
	
Type
	
Required
	
Description

question
	
string
	
Yes
	
Natural language question

How it works:
1. Decomposes the question into multiple search queries
1. Runs parallel searches across the workspace
1. Ranks results by relevance scoring (word overlap + rank bumps)
1. Fetches the top 3 most relevant pages
1. Synthesizes a coherent answer with source citations

Output: Synthesized answer with inline citations pointing to source pages.

Use when: Complex questions that span multiple pages, need for cited answers.

---

#### 4. query_database

> 💡 Natural language database queries

Inputs:

Parameter
	
Type
	
Required
	
Description

database
	
string
	
Yes
	
Database name or ID

filter
	
string
	
No
	
Natural language filter (e.g. "status is Done")

sort
	
string
	
No
	
Sort spec (e.g. "created desc")

Filter operators: is, contains, empty, not empty

Property types: select, checkbox, rich_text, title, number, date

Sort options: Property-based or timestamp-based (created, last edited)

Output: Formatted table with up to 100 rows and direct links.

Use when: Querying task boards, finding records by criteria, reporting.

---

#### 5. list_projects

> 💡 Discover all project and documentation pages

Inputs:

Parameter
	
Type
	
Required
	
Description

category
	
string
	
No
	
Optional category filter

Output: Grouped list of pages vs databases with titles and links.

Use when: Discovering what projects exist, exploring the workspace.

---

#### 6. get_aidra_docs

> 💡 Fast-path access to AIDRA project documentation

Inputs:

Parameter
	
Type
	
Required
	
Description

topic
	
string
	
No
	
AIDRA-specific topic filter

Output: Full AIDRA page content plus listing of related AIDRA pages.

Use when: AIDRA malware analysis questions, multi-agent architecture details.

---

## MCP Resources & System Prompts

#### MCP Resources

Resources are read-only data endpoints that the AI agent can query for workspace context.

---

##### workspace://index

> 💡 Dynamic index of the top 25 recent and notable pages/databases in the workspace
- Returns page titles, types, last-edited timestamps, and direct Notion links
- Updated dynamically on each request
- Useful for getting a quick overview of workspace activity

---

##### workspace://projects

> 💡 Complete list of all project pages with descriptions
- Returns all project-tagged pages
- Includes page descriptions where available
- Dynamically refreshed from workspace content

---

#### System Prompts

System prompts set the AI agent's context and expertise for different interaction modes.

---

##### cybereason-engineer

> 💡 General engineering assistant with Notion workspace access
- Sets up the AI as a Cybereason/LevelBlue engineer
- Teaches source citation patterns
- Broad engineering context for code, infrastructure, and project questions

Best for: General development questions, code context, project overview

---

##### aidra-expert

> 💡 AIDRA malware analysis specialist mode
- Deep AIDRA project knowledge and multi-agent architecture context
- Evidence-first analysis guidance
- Malware deobfuscation and detection engineering expertise

Best for: AIDRA-specific questions, malware analysis, Sigma rules, detection engineering

---

##### knowledge-qa

> 💡 General Q&A mode with parametrized questions
- Accepts a user question as parameter
- Teaches multi-step search → fetch → synthesize pattern
- General-purpose knowledge retrieval

Best for: Ad-hoc questions, knowledge lookups, research tasks

---

## Core Modules Deep Dive

Detailed documentation of every core module in the Owl Bot codebase.

---

#### Notion Client (src/notion/client.ts)

> 💡 Singleton Notion API client with built-in rate limiting, retry logic, and caching

##### Methods

Method
	
Cache TTL
	
Description

searchPages(query, filter)
	
60s
	
Search workspace with optional type filter

getPage(id)
	
2 min
	
Retrieve page by ID

getBlocks(pageId)
	
2 min
	
Fetch child blocks with pagination

queryDataSource(dbId, filter, sort)
	
—
	
Query database with filters/sorts

getDataSource(dbId)
	
5 min
	
Get database schema

parseNotionId(input)
	
—
	
UUID parser/normalizer

##### Rate Limiting
- 350ms minimum between API calls
- Automatic exponential backoff on 429/5xx responses
- Max 3 retries with configurable backoff

---

#### Search Module (src/notion/search.ts)

> 💡 Converts raw Notion API search results into standardized, formatted items
- Rich text snippet extraction from result highlights
- Page classification (page vs database)
- Formatted markdown output with titles, types, and URLs

---

#### Fetch Module (src/notion/fetch.ts)

> 💡 Recursive page fetching with depth control and content processing
- Recursive block fetching with configurable depth
- Automatic block-to-markdown conversion (25+ block types)
- Child page extraction and listing
- Content chunking for large pages (token-aware)
- Metadata formatting: title, URL, last edited, parent type

---

#### Query Module (src/notion/query.ts)

> 💡 Natural language filter parsing for database queries

##### Filter Parsing
- Operators: is, contains, empty, not empty
- Property types: select, checkbox, rich_text, title, number, date
- Automatic property name matching (fuzzy, case-insensitive)

##### Sort Parsing
- Property-based: "name asc", "status desc"
- Timestamp-based: "created desc", "last edited asc"

##### Output
- Table-formatted results with property extraction
- Up to 100 rows per query
- Direct Notion links for each row

---

#### Markdown Utilities (src/utils/markdown.ts)

> 💡 Bidirectional conversion between Notion blocks and Markdown

##### Rich Text Handling
- Bold, italic, code, strikethrough, underline
- Links, colors, inline math
- Mention resolution

##### Block Type Support (25+)

<details><summary>Full list of supported block types</summary>

</details>

##### Property Extraction (20+ types)

Handles: title, rich_text, number, select, multi_select, date, checkbox, people, files, formula, rollup, relation, created_time, last_edited_time, created_by, last_edited_by, url, email, phone_number, status

---

#### Cache System (src/utils/cache.ts)

> 💡 TTL-based LRU cache for reducing API calls

Setting
	
Value

Default TTL
	
5 minutes

Max entries
	
200

Eviction
	
LRU (least recently used)

Cleanup
	
Automatic expired entry removal

Cache key patterns:
- search:query:filter — search results (60s)
- page:id — page content (2min)
- blocks:id — block children (2min)
- datasource:id — database schemas (5min)

---

#### Content Chunker (src/utils/chunker.ts)

> 💡 Token-aware content splitting for large pages
- Splits by paragraphs respecting token limits
- Token estimation: 1 token ≈ 4 characters
- Summarization mode: headings + first 15 body lines
- Smart truncation preserving document structure

---

#### Error Handling (src/utils/errors.ts)
- Sanitized error messages (no token/credential exposure)
- Graceful fallbacks (empty results instead of crashes)
- User-friendly "not found" messages
- Structured error types for different failure modes

---

## Slash Commands Reference

Complete reference for all 10 Notion slash commands available in Claude Code.

---

#### Search & Discovery

##### /notion:search

> 💡 Workspace-wide semantic search across all pages and databases

Usage: /notion:search <query>

Example: /notion:search AIDRA pipeline architecture

---

##### /notion:find

> 💡 Quick title-based search — faster than full semantic search

Usage: /notion:find <title>

Example: /notion:find Sprint Board

---

#### Page & Content Creation

##### /notion:create-page

> 💡 Smart page creation with auto-template selection

Usage: /notion:create-page <title> [parent]

Example: /notion:create-page "API Design Doc" "Engineering Wiki"

Features:
- Auto-selects template based on content type
- Optional parent page placement
- Notion-flavored Markdown content

---

#### Database Operations

##### /notion:database-query

> 💡 Query databases using natural language filters and sorts

Usage: /notion:database-query <db name>; <filters>

Example: /notion:database-query Tasks; status is In Progress, assignee contains Itamar

---

##### /notion:create-task

> 💡 Add a task to the Tasks database with properties

Usage: /notion:create-task <title>; <details>

Example: /notion:create-task Fix auth bug; priority=High, status=To Do

---

##### /notion:create-database-row

> 💡 Insert a row into any database using natural-language values

Usage: /notion:create-database-row <db>; key=value

Example: /notion:create-database-row Bugs; title=Memory leak, severity=Critical

Notes:
- Auto-fetches schema to match property names
- Flexible property name matching (case-insensitive)
- Special formats: __YES__/__NO__ for checkboxes, date:Prop:start for dates

---

#### Task Management Workflows

##### /notion:tasks:setup

> 💡 Initialize a task board for project management

Usage: /notion:tasks:setup [url]

Creates or configures a task board with:
- Status tracking (To Do, In Progress, Done)
- Agent status fields for automation
- Blocking signal checkbox

---

##### /notion:tasks:build

> 💡 Implement a task with live Notion status tracking

Usage: /notion:tasks:build <url>

Workflow:
1. Fetches task details from Notion
1. Sets status to "In Progress"
1. Implements the task
1. Updates status to "Done" on completion
1. Reports blockers via "Agent Blocked" checkbox

---

##### /notion:tasks:plan

> 💡 Generate implementation plans from specs

Usage: /notion:tasks:plan <url>

Workflow:
1. Fetches and analyzes the spec page
1. Identifies functional and non-functional requirements
1. Develops phased implementation strategy
1. Creates a plan document linked back to the spec
1. Optionally generates task items in the task board

---

##### /notion:tasks:explain-diff

> 💡 Document code changes as a Notion page

Usage: /notion:tasks:explain-diff [ref]

Creates a documentation page explaining:
- What changed and why
- Files modified
- Before/after comparisons
- Impact analysis

---

## Knowledge Workflows

Structured workflows for capturing, researching, and organizing knowledge in Notion.

---

#### Knowledge Capture Workflow

> 💡 Capture knowledge from conversations, code reviews, debugging sessions, and meetings

##### Steps
1. Extract — Identify key concepts, decisions, procedures, and insights
1. Classify — Categorize the knowledge type:

Type
	
When to Use
	
Example

Concept
	
Explaining an idea or technology
	
"What is MCP?"

How-To
	
Step-by-step procedures
	
"How to deploy Owl Bot"

Decision Record
	
Recording a technical decision
	
"Why we chose Zod over Joi"

FAQ
	
Frequently asked questions
	
"How do I reset the cache?"

Meeting Summary
	
Post-meeting notes
	
"Sprint planning outcomes"

Learning
	
Post-incident or retro
	
"Rate limit incident learnings"

Reference
	
Quick-lookup material
	
"Notion API property types"
1. Structure using the appropriate template:

<details><summary>Concept Template</summary>

</details>

<details><summary>How-To Template</summary>

</details>

<details><summary>Decision Record Template</summary>

</details>

<details><summary>FAQ Template</summary>

</details>

<details><summary>Learning Template</summary>

</details>
1. Place in the right location (wiki, project page, documentation DB, decision log)
1. Link to related pages using <mention-page> for discoverability

---

#### Research & Documentation Workflow

> 💡 Research across the workspace and produce structured findings
1. Search broadly with search_docs to locate relevant content
1. Fetch full page details for promising results using get_page
1. Synthesize patterns, themes, and connections across sources
1. Document findings as a structured page with <mention-page> citations

---

#### Meeting Intelligence Workflow

> 💡 Prepare comprehensive meeting materials from workspace knowledge
1. Gather meeting details (topic, attendees, purpose)
1. Search Notion for related project pages, previous meeting notes, specs
1. Fetch and analyze for current status, open decisions, blockers, knowledge gaps
1. Create structured pre-read or agenda with:

---

#### Spec to Implementation Workflow

> 💡 Convert specifications into tracked, implementable task plans
1. Fetch and analyze the spec for functional and non-functional requirements
1. Develop implementation strategy with phased milestones
1. Generate plan document linked back to original spec
1. Create tasks in the Tasks database with proper properties:
1. Track progress with date-based status updates and agent status fields

---

## Configuration & Setup Guide

Complete guide for installing, configuring, and running Owl Bot.

---

#### Prerequisites
- Node.js 18+
- Notion API token (read-only access)
- Cursor or Claude Code as IDE

---

#### Installation

##### Step 1: Install Dependencies

```
cd owl-bot
npm install --production

​
```

##### Step 2: Build TypeScript

```
npm run build

​
```

##### Step 3: Configure MCP Server

<details><summary>Option A: Automated Setup (Cursor)</summary>

</details>

<details><summary>Option B: Manual MCP Configuration</summary>

</details>

<details><summary>Option C: Claude Code HTTP Transport</summary>

</details>

##### Step 4: Restart IDE

Restart Cursor or Claude Code to activate the MCP server and load commands.

---

#### Environment Variables

Variable
	
Required
	
Description

NOTION_API_TOKEN
	
Optional
	
Override embedded token for Notion API access

---

#### Configuration Files

File
	
Purpose

~/.cursor/mcp.json
	
MCP server registration for Cursor

.cursor/rules/owl-bot.mdc
	
Auto-activation triggers for Cursor agent

.cursor/skills/owl-bot/SKILL.md
	
Operational playbook for agent behavior

package.json
	
Dependencies and npm scripts

tsconfig.json
	
TypeScript ES2022 strict config

CLAUDE.md
	
Project-level Notion workspace guidelines

---

#### Auto-Activation Triggers

Owl Bot automatically activates in Cursor when it detects:
- Project names: AIDRA, AIDRA-LOCAL, VOWL, OwlHub, Owlint Sigma, Pixel Agents, Detection Engineering Hub
- Topics: Sigma rules, malware analysis, deobfuscation, multi-agent orchestration
- Keywords: "search Notion", "check the docs", "owl-bot"

---

#### Verification

After setup, verify Owl Bot is running:
1. Open Cursor or Claude Code
1. Type /notion:search test
1. You should see formatted search results from your Notion workspace

If no results appear, check:
- MCP server is registered in config
- Notion API token has workspace access
- Node.js 18+ is installed
- TypeScript build completed (dist/ directory exists)

---

## Database Operations Guide

Guidelines and best practices for working with Notion databases through Owl Bot.

---

#### Core Rules

> 💡 Always fetch the database schema first before creating or updating rows. This ensures you use correct property names and types.

---

#### Property Type Formats

Property Type
	
Format
	
Example

Title
	
Plain text
	
title=Fix auth bug

Rich Text
	
Plain text
	
description=Detailed explanation

Select
	
Option name
	
status=In Progress

Multi-Select
	
Comma-separated
	
tags=bug,frontend

Number
	
JavaScript number
	
priority=1 (not "1")

Checkbox
	
__YES__ or __NO__
	
blocked=__YES__

Date (start)
	
date:PropName:start
	
date:Due:start=2026-04-10

Date (end)
	
date:PropName:end
	
date:Due:end=2026-04-15

URL
	
userDefined: prefix
	
userDefined:url=https://...

ID
	
userDefined: prefix
	
userDefined:id=ABC-123

---

#### Natural Language Filters

When querying databases, you can use natural language:

##### Filter Operators

Operator
	
Usage
	
Example

is
	
Exact match
	
status is Done

contains
	
Substring match
	
name contains auth

empty
	
No value set
	
assignee is empty

not empty
	
Has a value
	
due date is not empty

##### Sort Specifications
- By property: "name asc", "priority desc"
- By timestamp: "created desc", "last edited asc"

---

#### Property Name Matching

> 💡 Owl Bot matches property names flexibly — minor capitalization differences are tolerated. "Status", "status", and "STATUS" all match the same property.

---

#### Best Practices
1. Fetch schema first — Use get_page or query_database on the database before mutations
1. Use exact option names — For select/multi-select, match the defined options
1. Numbers not strings — Pass priority=1 not priority="1"
1. Prefix reserved names — Properties named id or url need userDefined: prefix
1. Date format — Always use ISO 8601 format (YYYY-MM-DD)

---

## Agent Behavior & Auto-Activation

How Owl Bot behaves as an intelligent agent within the IDE.

---

#### Query Classification

When a user sends a message, Owl Bot classifies the intent and routes to the optimal tool:

User Intent
	
Tool Used
	
Example Query

General question
	
ask_knowledge
	
"How does the AIDRA pipeline work?"

Search request
	
search_docs
	
"Find all pages about Sigma rules"

Read a specific page
	
get_page
	
"Show me the VOWL architecture page"

Database query
	
query_database
	
"What tasks are in progress?"

Explore projects
	
list_projects
	
"What projects do we have?"

AIDRA topic
	
get_aidra_docs
	
"Tell me about AIDRA deobfuscation"

---

#### Execution Patterns

##### Direct Answer

Single tool call → formatted response.

##### Discovery + Deep Dive

search_docs → identify best result → get_page for full content.

##### Multi-Source Synthesis

ask_knowledge internally runs: decompose → multi-search → rank → fetch top 3 → synthesize.

##### Tool Chaining

Multiple dependent tool calls for complex workflows (e.g., find database → query it → fetch related pages).

---

#### Error Recovery

> 💡 Owl Bot automatically recovers from common failures

Scenario
	
Recovery Action

Empty search results
	
Broadens query, removes specific terms

No exact match
	
Retries with synonym substitution

Page not found
	
Explicit "not found" message with suggestions

Rate limited (429)
	
Exponential backoff, up to 3 retries

Server error (5xx)
	
Exponential backoff retry

Token exposure risk
	
Error messages are sanitized

---

#### Auto-Activation (Cursor)

In Cursor, Owl Bot activates automatically based on .cursor/rules/owl-bot.mdc:

##### Trigger: Project Names
- AIDRA, AIDRA-LOCAL
- VOWL (Vulnerability Owl)
- OwlHub
- Owlint Sigma
- Pixel Agents
- Detection Engineering Hub

##### Trigger: Topics
- Sigma rules and detection engineering
- Malware analysis and deobfuscation
- Multi-agent orchestration

##### Trigger: Keywords
- "search Notion"
- "check the docs"
- "owl-bot"

---

#### Agent Identity

> 💡 Owl Bot is a Notion knowledge assistant for the LevelBlue/Cybereason organization. It serves developers and AI agents working on projects including AIDRA, VOWL, OwlHub, Owlint Sigma, and Pixel Agents.

The agent operates in three contextual modes:
1. Cybereason Engineer — General engineering with Notion access
1. AIDRA Expert — Deep malware analysis and detection engineering
1. Knowledge Q&A — General-purpose question answering with synthesis
