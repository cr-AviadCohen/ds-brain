# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

AI Assistant for Cybereason - A multi-agent AI system with 36 specialized agents for security operations, covering Cybereason platform APIs, MITRE frameworks (ATT&CK, D3FEND, CAPEC, CWE), and threat intelligence sources (VirusTotal, Shodan, CVE, etc.).

## Commands

### Development Setup
```bash
# Install dependencies (using uv - recommended)
uv sync

# Or manual setup
uv venv --python 3.12
source .venv/bin/activate
uv pip install -e .
```

### Running the Application
```bash
# Orchestrator CLI
uv run python -m orchestrator.orchestrator

# Streamlit Web UI
uv run streamlit run src/orchestrator/orchestrator_streamlit.py

# Individual agents (examples)
uv run python -m agents.mitre.agent_mitre_attack.agent_mitre_attack_react
uv run python -m agents.threat_intelligence.agent_virustotal.agent_virustotal_react
uv run python -m agents.cybereason.agent_cr_api.agent_cr_api_ALL_react
```

### Testing
```bash
# Run all tests
uv run pytest

# Run tests for a specific agent
uv run pytest src/agents/threat_intelligence/agent_virustotal/test_tools_virustotal.py

# Run all tier-1 tests
uv run python -m agents._dev.run_all_tier1_tests

# Guardrails benchmark
uv run python -m utils.guardrails.run_guardrails_benchmark
```

### Docker
```bash
# Build and run
docker-compose -f docker-build/docker-compose.yaml up --build
```

## Architecture

### Core Components

- **`src/orchestrator/`**: LangGraph-based orchestrator that routes requests to appropriate agents
  - `orchestrator.py`: Main orchestration logic with agent routing
  - `orchestrator_config.yaml`: Centralized configuration for agents, guardrails, LLM settings
  - `orchestrator_CLI.py`: Command-line interface with `/` commands
  - `orchestrator_streamlit.py`: Web UI
  - `orchestrator_benchmark.py`: Benchmarking harness with JSON config files in `benchmark_configs/`

- **`src/utils/agents/agent.py`**: Base `Agent` class all agents inherit from (Pydantic-based with guardrails support)

- **`src/utils/tools/tool.py`**: Base `Tool` class with conversion support for LangGraph, Agno, and FastMCP formats

- **`src/utils/llm.py`**: LLM factory — centralized creation of Azure OpenAI and LMStudio instances

- **`src/utils/rag/`**: RAG (Retrieval-Augmented Generation) utilities for knowledge-grounded agents

- **`src/utils/guardrails/`**: Input/output validation using semantic similarity (99.58% accuracy)
  - `guardrails.py`: Main guardrails implementation
  - `guardrails_config.yaml`: Blocklist/allowlist patterns

### Agent Structure

All agents follow this pattern:
```
src/agents/<category>/agent_<name>/
├── _dev/                              # Development files, README, changelogs
│   └── README.md
├── agent_<name>_react.py              # Agent implementation with create_<name>_agent() factory
├── tools_<name>.py                    # Tool implementations
└── test_tools_<name>.py               # Tests
```

Agent categories:
- `cybereason/`: 15 Cybereason platform agents (API, UI, investigation, custom rules)
- `mitre/`: 4 MITRE framework agents (ATT&CK, D3FEND, CAPEC, CWE)
- `threat_intelligence/`: 17 external threat intel agents (VirusTotal, Shodan, etc.)

### Creating New Agents

1. Create directory under appropriate category in `src/agents/`
2. Implement `tools_<name>.py` with tool classes inheriting from `Tool`
3. Create `agent_<name>_react.py` with `create_<name>_agent()` factory function
4. Add test file `test_tools_<name>.py`
5. Place documentation in `_dev/` subdirectory

### Tool Permissions and Versioning

Cybereason API tools support permission-based filtering and server version compatibility:
```python
from utils.tools.tool_cr_api import PERMISSION, MIN_VERSION
from agents.cybereason.agent_cr_api.tools_cr_api import available_tools_by_permission_and_version

# Filter tools by user permissions AND server version
filtered_tools = available_tools_by_permission_and_version(
    username="analyst@company.com",
    tools_list=ALL_CR_TOOLS
)
```

### Imports

The project uses `uv sync` with `src/` as the package root. Import from package root:
```python
from utils.agents.agent import Agent
from utils.tools.tool import Tool
from orchestrator.orchestrator import create_orchestrator
from agents.mitre.agent_mitre_attack.agent_mitre_attack_react import create_mitre_agent
```

## Code Style

- Follow PEP 8
- Use type hints for function signatures and class attributes
- Use docstrings (Google style)
- Use dataclasses for simple data containers
- Keep methods under 20 lines when possible

## Environment Variables

Required for core functionality:
```bash
AZURE_OPENAI_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_API_VERSION=...
```

For Cybereason agents:
```bash
CYBEREASON_SERVER=...
CYBEREASON_USERNAME=...
CYBEREASON_PASSWORD=...
```

See README.md for full list of threat intelligence API keys.

## Workflow Orchestration

### 1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don't keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

### 2. Subagent Strategy
- Use subagents liberally to keep main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

### 3. Self-Improvement Loop
- After ANY correction from the user: update `tasks/lessons.md` with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until mistake rate drops
- Review lessons at session start for relevant project

### 4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: "Would a staff engineer approve this?"
- Run tests, check logs, demonstrate correctness

### 5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask "is there a more elegant way?"
- If a fix feels hacky: "Knowing everything I know now, implement the elegant solution"
- Skip this for simple, obvious fixes — don't over-engineer
- Challenge your own work before presenting it

### 6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don't ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching required from the user
- Go fix failing CI tests without being told how

## Task Management

1. **Plan First**: Write plan to `tasks/todo.md` with checkable items
2. **Verify Plan**: Check in before starting implementation
3. **Track Progress**: Mark items complete as you go
4. **Explain Changes**: High-level summary at each step
5. **Document Results**: Add review section to `tasks/todo.md`
6. **Capture Lessons**: Update `tasks/lessons.md` after corrections

## Core Principles

- **Simplicity First**: Make every change as simple as possible. Impact minimal code.
- **No Laziness**: Find root causes. No temporary fixes. Senior developer standards.
- **Minimal Impact**: Changes should only touch what's necessary. Avoid introducing bugs.

## Babysitter Integration

This project is onboarded to babysitter for orchestrated workflows, security scanning, and code quality.

### Project Profile

- Profile: `.a5c/project-profile.json`
- Run history: `.a5c/runs/`

### Key Commands

```bash
# Orchestrate a workflow
/babysitter:call

# Plan without executing
/babysitter:plan

# Resume a paused run
/babysitter:resume

# Diagnose run health
/babysitter:doctor
```

### Recommended Skills

| Skill | Purpose |
|---|---|
| `agent-inspector:scan` | OWASP LLM Top 10 security scanning |
| `agent-inspector:fix` | Remediate security vulnerabilities |
| `langchain` | LangGraph/LangChain development |
| `simplify` | Code quality review |
| `code-review:code-review` | PR review |
| `council-orchestration` | Multi-agent deliberation |