# Pixel Agents Council: Visualization and Multi-Agent Execution

### What Are Pixel Agents

Pixel Agents is an autonomous multi-agent framework that replaces single-agent Claude Code with a council of six specialized AI agents working together. Instead of one model handling all tasks, each agent brings distinct expertise and they deliberate, challenge each other, and reach consensus before executing. The system includes a real-time pixel art office visualization that shows the agents working, communicating, and collaborating.

The system is located at /root/.claude/Pixel_Agents/ and runs as a Node.js Express server on port 3333, proxied through nginx at /_proxy/3333/.

---

### The Six Council Agents

#### Scout (Green, wears goggles)

Role: Explorer and context gatherer

The Scout is always the first agent to run in a full council session. It maps the codebase structure, discovers relevant files, traces dependencies, identifies entry points, and reports verified file paths to all downstream agents. This prevents hallucination by ensuring every agent works from a verified file map rather than guessing at file locations.

Tools available: Read, Glob, Grep (search-only, no write access)

#### Architect (Blue, wears glasses)

Role: Solution designer and technical visionary

The Architect designs solutions with exact file paths and code structure. It defines APIs, data structures, and contracts between components. It plans implementation order, evaluates trade-offs with justification, and produces actionable specs for the Implementer. The Architect must respond to every challenge from the Critic with evidence-based arguments or revisions.

Tools available: Read, Glob, Grep

#### Critic (Red, wears red scarf)

Role: Adversarial reviewer and skeptic

The Critic challenges assumptions, finds weak points in designs, identifies edge cases and security issues, and verifies completeness. It issues formal challenges with evidence and rates issues as CRITICAL, HIGH, MEDIUM, or LOW. Critically, the Critic never manufactures problems -- if a design is sound, it says so. It produces NEEDS_REVISION or BLOCKED verdicts only when genuinely warranted.

Tools available: Read, Glob, Grep

#### Implementer (Orange, wears hoodie)

Role: Code executor and builder

The Implementer writes production code based on the Architect's design. It follows specifications faithfully without redesigning on the fly, handles errors properly at system boundaries, and flags blockers immediately if the design is unclear. It can spawn up to four parallel worker clones via a SPLIT_TASKS directive for large implementations. All error handling follows fail-secure principles (deny by default, never fail-open).

Tools available: Read, Glob, Grep, Write, Edit

#### Tester (Purple, wears lab coat)

Role: Test writer and validator

The Tester writes unit, integration, and edge-case tests. It validates that implementations meet the original specification, tests boundary conditions and error paths, and reports PASS, GAPS, or FAIL verdicts. The focus is on behavior testing rather than testing implementation details.

Tools available: Read, Glob, Grep, Write (test files)

#### Debugger (Yellow, wears detective hat)

Role: Root cause analyst

The Debugger uses a structured hypothesis-driven debugging methodology. It forms two to three explicit hypotheses about each bug, designs experiments to distinguish between them, collects structured evidence, updates confidence based on results, and produces a root cause recommendation. It never guesses -- it always verifies by reading actual code and testing actual fixes.

Tools available: Read, Glob, Grep

---

### Execution Modes

The council engine automatically routes tasks based on natural language analysis:

Mode
	
Trigger Example
	
What Happens
	
Solo
	
"only scout, list files"
	
One agent runs alone, no follow-ups. Fastest mode.

Direct
	
"architect, plan the API"
	
Lead agent runs and can output HANDOFF: to pass to next agent.
	
Team
	
"scout and critic, review auth"
	
Two agents run in parallel on the same task.

Debug
	
"why won't the app start?"
	
Scout investigates first, then Debugger analyzes with Critic review.
	
Full Council
	
"build a REST API"
	
Complete deliberation pipeline through all phases.

---

### Full Council Pipeline

#### Phase 1: Exploration (Scout-First)

The Scout runs alone, mapping all relevant files with verified paths. Its output is parsed into a DISCOVERED FILES map that all downstream agents receive. This grounding step prevents the common failure mode where agents reference files that do not exist.

#### Phase 2: Parallel Deliberation

The Architect and Critic run in parallel, both grounded in the Scout's file map. The Architect proposes a solution while the Critic independently identifies potential issues. If the Critic issues a NEEDS_REVISION or BLOCKED verdict, the Architect must respond with evidence-based rebuttals or revisions.

#### Phase 3: Implementation

The Implementer builds the converged plan into code. For large tasks, it can spawn two to four worker clones via the SPLIT_TASKS directive, each receiving a portion of the work with 60% of the parent's token budget.

#### Phase 4: Verification

The Tester and Debugger verify the implementation independently. Both receive sandbox validation hints indicating which files were modified. If verification reveals failures or gaps, a fix loop sends issues back to the Implementer for up to two additional passes.

---

### Mission Control System

Every council run is tracked as a persistent mission with defined lifecycle stages:

INTAKE - ROUTING - SCOPING - PLANNING - DELIBERATION - IMPLEMENTATION - VALIDATION - FINALIZATION

Missions are stored in /root/.claude/Pixel_Agents/missions/{mission_id}/ with:
- mission.json containing metadata, stage, status, and aggregated results
- events.jsonl containing timestamped events for the complete mission timeline

Broad tasks with three or more items are automatically decomposed into child missions, with the parent aggregating usage and findings from all children.

---

### Real-Time Visualization

The pixel art office visualization runs in the browser and connects via WebSocket to receive real-time updates:

#### Visual Elements
- Each agent has a unique color, accessory, and animation set
- Agents move around a pixel art office with furniture, desks, and a conference table
- Speech bubbles show what each agent is currently working on
- The conference table area is used during deliberation phases
- Status indicators show idle, working, or blocked states

#### Hook-Driven Updates

When running inside Claude Code, the council-hook.js script maps Claude's tool calls to agent activity:
- Read, Glob, Grep, WebFetch, WebSearch map to Scout
- Write, Edit map to Implementer
- Skill, EnterPlanMode map to Architect
- Agent and Task spawns map to numbered Worker clones

#### JSONL Watcher Mode

When started with the --jsonl-watch flag, the server watches Claude Code's JSONL transcript files in ~/.claude/projects/ and reflects activity in real-time without running a council task.

---

### Core Technical Files

File
	
Size
	
Purpose
	
server.js
	
25 KB
	
Express and WebSocket server, broadcasts council state

council-engine.js
	
294 KB
	
Complete multi-agent routing and execution logic
	
council-hook.js
	
5.3 KB
	
CLI tool for visualization updates from Claude hooks

mission-control.js
	
105 KB
	
Mission lifecycle, stage tracking, task decomposition
	
jsonl-watcher.js
	
8 KB
	
Real-time Claude cursor activity monitoring

public/simulation.js
	
50 KB
	
Agent movement, pathfinding, speech bubbles
	
public/office.js
	
17.5 KB
	
Pixel office rendering and animation

public/agents.js
	
49 KB
	
Agent sprite definitions and animation frames
	
public/tilemap.js
	
28.8 KB
	
Room layout, furniture, conference table

#### Dependencies
- express (4.18.2) for the web framework
- ws (8.14.2) for WebSocket communication
- langfuse (3.38.6) for optional LLM observability and analytics
