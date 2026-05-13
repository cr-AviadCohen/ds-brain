---
title: MCP
type: project
tags: [project, wiki]
status: active
started: 2026-05-11
systems: []
related_decisions: []
raw_path: raw/projects/Project - MCP/
last_updated: 2026-05-11
---

# MCP

> Model Context Protocol server for Cybereason — routing logic and per-API tool implementations exposed so MCP clients (Claude Desktop, Cursor, etc.) can drive Cybereason APIs through standard MCP.

## Goal

Build an MCP server that exposes Cybereason APIs in a standards-compliant way, with each tool responsible for a single API call. Support consumption by standard MCP clients, validate against Phoenix feature parity, and explore the right division of routing logic between client AI and the MCP server.

## Approach

POC-grade implementation (not production). Two implementation styles explored: (1) "smart MCP server" + "dumb client" with custom tools tailored for product chat — accuracy may be higher but all API costs incurred by Cybereason; (2) richer MCP client connecting multiple MCP servers, configured via host:port. Need to authenticate (OAuth?), optimise heavy responses (some APIs return 81K+ tokens, hitting Azure OpenAI GPT-4o's 450K-tokens-per-minute limit), and software-engineer the code (clean classes, LangChain & LangGraph). Future: Docker support, NPX publishing, MCP resources/prompts/sampling, Streamlit-backed user-feedback infrastructure.

## Status

active — seeded from raw 2026-05-11.

## Decisions

(populated by /ingest as decisions are taken)

## Risks

- Many Cybereason APIs return very large responses, easily exhausting LLM rate limits.
- API was not designed for LLM consumption.

## Mentions

(populated by /ingest)

## Open questions

- Where does routing live: client-side AI or MCP server-side agent?
- Can MCP access the database directly rather than via API?
- How is action success (e.g., process kill) verified end-to-end?
