# Owlint_Sigma

> 💡 Owlint-Sigma Tipper is an AI-powered Sigma detection rule generation and bidirectional SIEM translation platform built by LevelBlue. It transforms DFIR reports, threat intelligence, and raw SIEM queries into production-ready Sigma detection rules — and translates them across six major SIEM platforms.

Platform Overview
Supported SIEM Platforms
Processing Tracks
Quality & Validation Pipeline
Documentation
System & Architecture
Usage, Quality & Audit
Research & Methodology

---

## Platform Overview

Git - https://github.com/cybereason-labs/itamar-h/tree/dev-owlint

Owlint-Sigma v5.0 (Python 3.10+) solves three critical detection engineering challenges:

📄
Threat Intel → Detection Rules
Automatically converts DFIR reports, IOC lists, and detection logic narratives into validated, multi-logsource Sigma rules using tiered LLM generation, self-healing validation, and red-team review.
🔄
Cross-SIEM Translation
Bidirectional translation between Sigma and six SIEM query languages with field mapping, validation, and repair loops.
📚
Detection Library
Semantic deduplication and persistent rule storage via ChromaDB vector embeddings. Never generate a duplicate rule again.

---

## Supported SIEM Platforms

Platform
	
Module
	
Sigma → SIEM
	
SIEM → Sigma
	
Auto-Detect

Splunk
	
splunk.py
	
Yes
	
Yes
	
Yes

Microsoft Sentinel
	
sentinel.py
	
Yes
	
Yes
	
Yes

Elastic Security
	
elastic.py
	
Yes
	
Yes
	
Yes

CrowdStrike Falcon
	
crowdstrike.py
	
Yes
	
Yes
	
Yes

Google Chronicle
	
chronicle.py
	
Yes
	
Yes
	
Yes

IBM QRadar
	
qradar.py
	
Yes
	
Yes
	
Yes

Each platform module inherits from BasePlatform and provides syntax patterns, field mapping dictionaries, platform-specific validation rules, and translation templates.

---

## Processing Tracks

<details><summary>Track 1: Threat Intelligence → Sigma → SIEM</summary>

</details>

<details><summary>Track 2: Sigma → SIEM Query</summary>

</details>

<details><summary>Track 3: SIEM Query → Sigma</summary>

</details>

---

## Quality & Validation Pipeline

Owlint-Sigma implements six layers of validation to ensure production-grade rule quality:
1. Sigma Structural Validation — YAML structure, required fields, logsource format
1. Field Allowlist Validation — Fields checked against field_logsource_map.yaml per category
1. Red-Team Review — LLM-powered adversarial review of generated rules
1. Self-Healing Loops — Automatic repair attempts when validation fails
1. Query Validation — Post-translation structural checks against field maps
1. Fitness Assessment — Pre-generation suitability scoring of input content

---

## Documentation

### System & Architecture
- 📄 [Architecture & Data Flow](https://www.notion.so/Architecture-Data-Flow-339ae23bae1d8164b437faeaff1197ed?pvs=25)
- 📄 [Core Modules Reference](https://www.notion.so/Core-Modules-Reference-339ae23bae1d81a38be4f1d11159c355?pvs=25)
- 📄 [Platforms Reference](https://www.notion.so/Platforms-Reference-339ae23bae1d81158698ceba4d0db8b7?pvs=25)
- 📄 [Field & Logsource Reference](https://www.notion.so/Field-Logsource-Reference-339ae23bae1d817caa3ec663f99f9498?pvs=25)
- 📄 [Configuration System](https://www.notion.so/Configuration-System-339ae23bae1d811988a0d5632d725e26?pvs=25)
- 📄 [Project Structure & Dependencies](https://www.notion.so/Project-Structure-Dependencies-339ae23bae1d817798f6efc22500e941?pvs=25)

### Usage, Quality & Audit
- 📄 [Testing & Quality Assurance](https://www.notion.so/Testing-Quality-Assurance-339ae23bae1d81f6961adcc7053febd7?pvs=25)
- 📄 [CLI Usage & Output Formats](https://www.notion.so/CLI-Usage-Output-Formats-339ae23bae1d810fb3b4dfd0fe179752?pvs=25)
- 📄 [Audit Engine Reference](https://www.notion.so/Audit-Engine-Reference-339ae23bae1d8103bce9f366b546479d?pvs=25)

### Research & Methodology
- 📄 [Step-Based Detection Logic: Improving Sigma Rule Quality Through Structured TTP Coverage](https://www.notion.so/Step-Based-Detection-Logic-Improving-Sigma-Rule-Quality-Through-Structured-TTP-Coverage-339ae23bae1d8134bfd9e05399d0d4c1?pvs=25)

---

> 💡 Last updated: April 5, 2026 | Version: 5.0 | Maintainer: LevelBlue

---

# Subpages Content

---

## Architecture & Data Flow

Owlint-Sigma follows a pipeline architecture with three distinct processing tracks, all centered around Sigma as the universal detection format.

---

#### System Architecture Diagram

```
flowchart TB
    subgraph INFRA["SHARED INFRASTRUCTURE"]
        direction TB
        KB["Knowledge Base<br>14 field sets, 21 logsource categories<br>11+ generation profiles<br>detection_knowledge.yaml<br>mitre_attack_reference.yaml<br>field_logsource_map.yaml"]
        LLM["LLM Layer<br>gpt-5.4 via Azure OpenAI<br>text-embedding-3-large 3072-dim<br>Pluggable: extend BaseLLM"]
        SIEM6["6 SIEM Platforms<br>Splunk SPL - Sentinel KQL<br>Elastic EQL - CrowdStrike CQL<br>Chronicle YARA-L - QRadar AQL"]
        OBS["Observability<br>LangFuse tracing for all LLM calls<br>Structured pipeline logging"]
    end

    subgraph TRACKA["TRACK A: Threat Intel --> Sigma --> SIEM"]
        A1["Input<br>DFIR Report / Detection Logic / TTPs"] --> A2["Preprocess<br>Format analysis + kill-chain hints"]
        A2 --> A2b["Decompose - LLM<br>Atomic DetectionUnits<br>Platform inference + dedup"]
        A2b --> A2c["Library Dedup<br>Embedding similarity > 0.55<br>skips existing rules"]
        A2c --> A3["Classify Logsources<br>7 profiles, keyword scoring<br>threshold > 0.15"]
        A3 --> A4["Generate Sigma - Tiered LLM<br>Call 1: Structure Draft<br>Call 2: Quality Enhancement<br>Fallback strategies"]
        A4 --> A5["Validate + Self-Heal<br>15+ checks, 3 retries<br>Red-team review"]
        A5 --> A5b["Store in Library<br>ChromaDB embed + metadata<br>Upsert on source + step"]
        A5 --> A6["Sigma Output<br>Rules + Coverage Report<br>Companion rules"]
        A5b --> A6
        A6 --> A6b["Format Report<br>Text / JSON / Markdown"]
        A6 --> A7["Translate to SIEM - LLM<br>Field mapping + syntax ref<br>Platform validator + self-heal"]
        A7 --> A8["SIEM Queries<br>Production-ready native queries"]
    end

    subgraph TRACKB["TRACK B: SIEM Query --> Sigma"]
        B1["Input<br>Native SIEM Query"] --> B2["Detect Platform<br>Regex patterns, 6 platforms<br>No LLM needed"]
        B2 --> B3["Reverse Translate - LLM<br>Reverse field mapping<br>Few-shot examples"]
        B3 --> B4["Validate<br>Same SigmaValidator<br>Up to 3 retries"]
        B4 --> B5["Sigma Rule<br>Portable YAML"]
        B5 --> B6["Store in Library<br>track_origin=track_b"]
    end

    subgraph TRACKC["TRACK C: SIEM A --> SIEM B (Cross-Platform)"]
        C1["Input<br>Query from any SIEM"] --> C2["To Sigma - LLM Call 1<br>Runs Track B internally"]
        C2 --> C3["Sigma Pivot<br>Universal bridge"]
        C3 --> C4["From Sigma - LLM Call 2<br>Runs Track A7 internally"]
        C4 --> C5["Output<br>Native query in target SIEM<br>2 LLM calls total"]
    end

    INFRA -.-> TRACKA
    INFRA -.-> TRACKB
    INFRA -.-> TRACKC

    style INFRA fill:#e8e8ff,stroke:#666,color:#333
    style TRACKA fill:#fff3e0,stroke:#e65100,color:#333
    style TRACKB fill:#e8f5e9,stroke:#2e7d32,color:#333
    style TRACKC fill:#e3f2fd,stroke:#1565c0,color:#333

TRACK C: SIEM A --> SIEM B (Cross-Platform)

TRACK B: SIEM Query --> Sigma

TRACK A: Threat Intel --> Sigma --> SIEM

SHARED INFRASTRUCTURE

Input
Query from any SIEM

To Sigma - LLM Call 1
Runs Track B internally

Sigma Pivot
Universal bridge

From Sigma - LLM Call 2
Runs Track A7 internally

Output
Native query in target SIEM
2 LLM calls total

Input
Native SIEM Query

Detect Platform
Regex patterns, 6 platforms
No LLM needed

Reverse Translate - LLM
Reverse field mapping
Few-shot examples

Validate
Same SigmaValidator
Up to 3 retries

Sigma Rule
Portable YAML

Store in Library
track_origin=track_b

Input
DFIR Report / Detection Logic / TTPs

Preprocess
Format analysis + kill-chain hints

Decompose - LLM
Atomic DetectionUnits
Platform inference + dedup

Library Dedup
Embedding similarity > 0.55
skips existing rules

Classify Logsources
7 profiles, keyword scoring
threshold > 0.15

Generate Sigma - Tiered LLM
Call 1: Structure Draft
Call 2: Quality Enhancement
Fallback strategies

Validate + Self-Heal
15+ checks, 3 retries
Red-team review

Store in Library
ChromaDB embed + metadata
Upsert on source + step

Sigma Output
Rules + Coverage Report
Companion rules

Format Report
Text / JSON / Markdown

Translate to SIEM - LLM
Field mapping + syntax ref
Platform validator + self-heal

SIEM Queries
Production-ready native queries

Knowledge Base
14 field sets, 21 logsource categories
11+ generation profiles
detection_knowledge.yaml
mitre_attack_reference.yaml
field_logsource_map.yaml

LLM Layer
gpt-5.4 via Azure OpenAI
text-embedding-3-large 3072-dim
Pluggable: extend BaseLLM

6 SIEM Platforms
Splunk SPL - Sentinel KQL
Elastic EQL - CrowdStrike CQL
Chronicle YARA-L - QRadar AQL

Observability
LangFuse tracing for all LLM calls
Structured pipeline logging

​
```

---

#### Track A: Detailed Pipeline Flow

```
flowchart LR
    subgraph INPUT["Step 1"]
        I["Threat Intel Text<br>DFIR / Detection Logic / TTPs"]
    end
    subgraph PREP["Step 2"]
        P["Preprocess<br>content_preprocessor.py<br>Format: NARRATIVE / STRUCTURED / MIXED"]
    end
    subgraph DECOMP["Step 2.5"]
        D["Decompose - LLM<br>detection_decomposer.py<br>Atomic DetectionUnits"]
    end
    subgraph DEDUP["Step 2.7"]
        DD["Library Dedup<br>rule_library.py<br>Cosine similarity > 0.55"]
    end
    subgraph CLASS["Step 3"]
        C["Classify Logsources<br>logsource_profiles.py<br>7 profiles, weighted scoring"]
    end
    subgraph GEN["Step 4"]
        G["Generate Sigma<br>generator.py<br>Two-call tiered LLM"]
    end
    subgraph VAL["Step 5"]
        V["Validate + Self-Heal<br>validator.py<br>15+ checks, red-team review"]
    end
    subgraph STORE["Step 5.5"]
        S["Store in Library<br>rule_library.py<br>ChromaDB + metadata"]
    end
    subgraph OUT["Step 6"]
        O["Sigma Output<br>sigma_rules.yml<br>audit.csv, coverage_report.yml"]
    end
    subgraph RPT["Step 6.5"]
        R["Format Report<br>report_formatter.py<br>Text / JSON / Markdown"]
    end
    subgraph TRANS["Step 7"]
        T["Translate to SIEM<br>translator.py<br>Field maps + validator"]
    end
    subgraph SIEM["Step 8"]
        SQ["SIEM Queries<br>SPL / KQL / EQL<br>CQL / YARA-L / AQL"]
    end

    I --> P --> D --> DD --> C --> G --> V --> S
    V --> O --> R
    O --> T --> SQ

Step 8

Step 7

Step 6.5

Step 6

Step 5.5

Step 5

Step 4

Step 3

Step 2.7

Step 2.5

Step 2

Step 1

SIEM Queries
SPL / KQL / EQL
CQL / YARA-L / AQL

Translate to SIEM
translator.py
Field maps + validator

Format Report
report_formatter.py
Text / JSON / Markdown

Sigma Output
sigma_rules.yml
audit.csv, coverage_report.yml

Store in Library
rule_library.py
ChromaDB + metadata

Validate + Self-Heal
validator.py
15+ checks, red-team review

Generate Sigma
generator.py
Two-call tiered LLM

Classify Logsources
logsource_profiles.py
7 profiles, weighted scoring

Library Dedup
rule_library.py
Cosine similarity > 0.55

Decompose - LLM
detection_decomposer.py
Atomic DetectionUnits

Preprocess
content_preprocessor.py
Format: NARRATIVE / STRUCTURED / MIXED

Threat Intel Text
DFIR / Detection Logic / TTPs

​
```

---

#### High-Level Data Flow

Track A (Threat Intel to Sigma to SIEM):

Input file → optional multi-source split → SmartSigmaGenerator.generate_ruleset → ContentPreprocessor / fitness inside pipeline → DetectionDecomposer → per unit: classify platform/type/category → tiered LLM generation + SigmaValidator + red-team + retries → behavioral companions for IOC/hybrid → RuleLibrary embed/dedup/store → write sigma_rules.yml, audit.csv, coverage_report.yml → optional SigmaTranslator.from_sigma for SIEM queries

Track B (Sigma to SIEM):

YAML load → SigmaTranslator.from_sigma (field maps from YAML, QueryValidator, review, fallback)

Track C (SIEM to Sigma):

Raw query + platform → SigmaTranslator.to_sigma (reverse mapping + validation) → sigma_rule.yml

Cross-platform:

translate() = to Sigma then from Sigma

---

#### Validation Layers

Owlint-Sigma implements multiple validation layers to ensure rule quality:
1. Sigma Structural Validation — YAML structure, required fields, logsource format
1. Field Allowlist Validation — Fields checked against field_logsource_map.yaml per category
1. Red-Team Review — LLM-powered adversarial review of generated rules
1. Self-Healing Loops — Automatic repair attempts when validation fails
1. Query Validation — Post-translation structural checks against field maps
1. Fitness Assessment — Pre-generation suitability scoring of input content

---

#### Key Design Patterns

##### Tiered LLM Generation

The generator uses a tiered prompt strategy:
1. Primary generation with full context (knowledge, RAG, field maps)
1. Validation against Sigma schema and field allowlists
1. Self-healing — automatic repair attempts on validation failures
1. Red-team review — adversarial LLM pass to catch logic flaws
1. Companion generation — additional rules for IOC and hybrid detections

##### Multi-Source Processing

Input files with ## Source: headers are automatically split and processed independently, enabling batch processing of multi-source threat intel documents.

##### Platform Detection

PlatformDetector uses syntax pattern matching to automatically identify the source SIEM platform from raw query text, enabling seamless SIEM to Sigma conversion without explicit platform specification.

##### Field Map Architecture

Each SIEM platform has a dedicated YAML field map (config/siem_field_maps/) containing:
- Table/index mappings per Sigma logsource category
- Bidirectional field name mappings
- Modifier translations (contains, startswith, endswith, etc.)
- Condition templates
- Platform-specific notes and caveats

---

#### Observability

Optional Langfuse tracing is available via observability.py — traces LLM calls and embedding operations when Langfuse keys are configured.

---

## Core Modules Reference

Definitive API reference for every module, class, function, and constant in the owlint_sigma package.

---

#### Generator (generator.py)

> ⚡ The SmartSigmaGenerator (aliased as SigmaGenerator) is the heart of the pipeline. It orchestrates tiered LLM prompts, self-healing validation loops, red-team review, companion rule generation, and ruleset assembly.

##### SmartSigmaGenerator

Constructor Param
	
Description
	
llm
	
LLM provider instance (BaseLLM)

max_retries
	
Max self-healing validation retries
	
skip_red_team
	
Boolean; skip adversarial review pass

max_content_chars
	
Truncation limit for input content
	
rule_library
	
Optional RuleLibrary for dedup and storage

Methods:
- generate_ruleset(content, source_url) -> RulesetGenerationResult — Full pipeline: preprocess, decompose, generate, validate, heal, store
- generate_single(content, category, platform, source_url) -> SingleRuleResult — Generate one rule for a specific category/platform
- _render_system_prompt(category, platform) -> str — Build system prompt with RAG context, logsource profile, and field allowlists

##### Dataclasses

<details><summary>SingleRuleResult</summary>

</details>

<details><summary>RulesetGenerationResult</summary>

</details>

<details><summary>CompanionFailure</summary>

</details>

---

#### Detection Decomposer (detection_decomposer.py)

> 🔬 DetectionDecomposer uses LLM-powered decomposition to split threat intelligence into atomic detection units, each mapped to a Sigma logsource category and platform.

##### DetectionDecomposer

Methods:
- decompose(content, source_url) -> Tuple[List[DetectionUnit], CoverageReport] — Decompose content into detection units with coverage tracking

Coverable categories: process_creation, network_connection, registry_event, image_load, file_event, process_access, dns_query, syslog

##### Dataclasses

<details><summary>DetectionUnit</summary>

</details>

<details><summary>PlatformQueryHint</summary>

</details>

<details><summary>CoverageReport</summary>

</details>

---

#### Translator (translator.py)

> 🔄 SigmaTranslator provides bidirectional translation between Sigma rules and SIEM queries, plus cross-SIEM translation using Sigma as a pivot format.

##### SigmaTranslator

Constants:
- MAX_INPUT_CHARS = 15,000 — Maximum input size for translation

Methods:
- to_sigma(query, source_platform, auto_detect) -> Dict — SIEM query to Sigma rule
- from_sigma(sigma_rule, target_platform) -> Dict — Sigma rule to SIEM query
- translate(query, source_platform, target_platform) -> Dict — Cross-SIEM via Sigma pivot

Self-healing loop: Draft -> Validate -> Review -> Fix (up to max_retries)

Dependencies: Uses QueryValidator, PlatformDetector, RuleLibrary

---

#### Validator (validator.py)

> 🛡️ SigmaValidator is the multi-pass validation engine that checks syntax, schema, field usage, and quality of Sigma rules.

##### SigmaValidator

Constants:

Constant
	
Value
	
REQUIRED_FIELDS
	
{title, id, description, logsource, detection, level}

REQUIRED_LOGSOURCE
	
{category, product}
	
AMBIGUOUS_SHORT_FILTERS
	
APT, RPM, YUM, DNF, etc.

Methods:
- validate_full(rule_yaml, logsource, target_platform) -> SigmaValidationResult — Complete multi-pass validation
- validate_syntax(rule_yaml) -> SigmaValidationResult — YAML parse and structure check
- validate_schema(parsed_dict, logsource) -> SigmaValidationResult — Schema conformance
- validate_quality(parsed_dict) -> SigmaValidationResult — Quality heuristics
- validate_modifiers(detection_dict) -> List[str] — Check modifier validity

##### SigmaValidationResult

Field
	
Type
	
Description

errors
	
List[str]
	
Blocking errors

rule_title
	
Optional[str]
	
Extracted rule title

suggestions
	
List[str]
	
Improvement suggestions

Properties: error_message, has_issues

Method: to_dict()

##### Standalone Functions and Constants
- sanitize_sigma_yaml(raw_yaml) -> str — Fix common YAML issues (quoting, indentation, encoding)
- KNOWN_GENERIC_INDICATORS — Set of overly generic indicator strings
- SIGMA_VALID_MODIFIERS — contains, endswith, startswith, base64, base64offset, re, cidr, all, gt, gte, lt, lte, wide, windash, utf16le, utf16be, utf16
- SIGMA_VALID_LEVELS — high, medium, low
- SIGMA_VALID_MODES — report, prevent

---

#### Query Validator (query_validator.py)

> ✅ QueryValidator performs post-translation structural checks, comparing translated queries against the source Sigma rule and platform field maps.

##### QueryValidator

Methods:
- validate(query, platform, sigma_rule, sigma_category) -> QueryValidationResult — Full post-translation validation
- _check_table(query, platform, category, table_schema) -> List[str] — Verify correct table/index usage
- _check_field_coverage(query, platform, category, sigma_rule, table_schema) -> List[str] — Check field mapping completeness
- _check_logic_preservation(query, sigma_rule) -> List[str] — Verify detection logic preserved

##### QueryValidationResult

Field
	
Type
	
Description
	
is_valid
	
bool
	
Overall pass/fail

errors
	
List[str]
	
Blocking errors
	
warnings
	
List[str]
	
Non-blocking warnings

Properties: error_message, all_issues

---

#### Content Preprocessor (content_preprocessor.py)

> 📥 ContentPreprocessor handles deterministic preprocessing of threat intelligence input, normalizing text and classifying it into logsource categories.

##### ContentPreprocessor

Methods:
- preprocess(content) -> Tuple[NormalizedIntelInput, ClassificationResult] — Normalize and classify input

##### IntelInputKind (Enum)

NARRATIVE | STRUCTURED | MIXED

##### Dataclasses

<details><summary>NormalizedIntelInput</summary>

</details>

<details><summary>ClassificationResult</summary>

</details>

##### Standalone Functions and Constants
- normalize_intel_input(text) -> NormalizedIntelInput — Standalone normalization
- classify_logsources(text, min_score) -> ClassificationResult — Standalone classification
- PLATFORM_KEYWORDS — Maps platform (windows / linux / ci_platform) to keyword tuples

---

#### Fitness Assessor (fitness.py)

> 🎯 ContentFitnessAssessor uses heuristic scoring to determine whether input content is suitable for Sigma rule generation.

##### ContentFitnessAssessor

Constants:

Constant
	
Description
	
SIGMA_PROCESS_NAMES
	
~40 known process names for detection

SIGMA_KEYWORDS
	
Sigma-relevant keywords
	
CHAIN_KEYWORDS
	
Attack chain indicators

NETWORK_INDICATORS
	
Network-based detection signals
	
REGISTRY_INDICATORS
	
Registry-based detection signals

FILE_INDICATORS
	
File-based detection signals
	
DNS_INDICATORS
	
DNS-based detection signals

IMAGE_LOAD_INDICATORS
	
Image load detection signals
	
SIGMA_MIN_SCORE
	
0.15 — Minimum score threshold

Methods:
- assess(content) -> FitnessResult — Evaluate content suitability

##### FitnessResult

Field
	
Type
	
Description

sigma_reason
	
str
	
Explanation of assessment

sigma_indicators
	
list
	
Detected indicator types

Method: to_dict()

---

#### SIEM Schemas (siem_schemas.py)

> 🗄️ Loads and formats SIEM platform YAML schemas for use in LLM prompts and query validation. Supports category alias resolution and cached loading.

##### Functions

Function
	
Returns
	
Description
	
_load_platform_schema(platform)
	
Dict
	
Cached YAML schema loading

get_supported_platforms()
	
List[str]
	
All supported SIEM platforms
	
get_schema_for_platform(platform, sigma_category)
	
Optional[Dict]
	
Schema for platform + category

get_query_language(platform)
	
str
	
Query language name (SPL, KQL, etc.)
	
format_field_map_for_prompt(platform, category)
	
str
	
Field map formatted for LLM prompts

format_review_field_map(platform, category)
	
str
	
Compact field map for review prompts
	
extract_category_from_sigma(sigma_yaml)
	
str
	
Extract logsource category from YAML

get_expected_table(platform, category)
	
str
	
Expected table/index name
	
get_all_siem_fields(platform, category)
	
List[str]
	
All fields for platform + category

Category aliases: Maps 15+ variant names to canonical categories (e.g., proc_creation -> process_creation)

---

#### Platform Detector (platform_detector.py)

> 🔍 PlatformDetector auto-detects the SIEM query language from raw query text using syntax pattern matching.

##### PlatformDetector

Methods:
- detect(query) -> Optional[DetectionCandidate] — Best match with highest confidence
- detect_all(query) -> List[DetectionCandidate] — All candidates sorted by confidence descending

##### DetectionCandidate

Field
	
Type
	
Description
	
platform
	
str
	
Detected platform name

confidence
	
float
	
Detection confidence (0.0 - 1.0)
	
matched_patterns
	
list
	
Patterns that triggered the match

---

#### Sigma Logsources (sigma_logsources.py)

> 📋 Field allowlists per logsource category, loaded from field_logsource_map.yaml. Provides the authoritative set of valid fields for each Sigma logsource.

##### Field Registries (frozensets)

Registry
	
Field Count

NETWORK_CONNECTION_FIELDS
	
12

REGISTRY_EVENT_FIELDS
	
7

IMAGE_LOAD_FIELDS
	
10

PIPE_CREATED_FIELDS
	
4

FIREWALL_FIELDS
	
9

WEBSERVER_FIELDS
	
10

CLOUD_FIELDS
	
14

##### Functions
- LOGSOURCE_FIELDS — Dict mapping 25+ categories to their field frozensets
- EXCLUSIVE_FIELD_MAP — Loaded from field_logsource_map.yaml
- get_fields_for_logsource(category) -> FrozenSet[str] — Return allowed fields
- list_categories() -> List[str] — All known logsource categories
- format_exclusive_field_map(category) -> str — Formatted for prompt injection

---

#### Logsource Profiles (logsource_profiles.py)

> 📐 Generation profiles that customize LLM prompts, field allowlists, and classifier weights per logsource category.

##### LogsourceGenerationProfile (frozen dataclass)

Field
	
Type
	
Description
	
category
	
str
	
Sigma logsource category

product
	
str
	
Sigma product (e.g., windows)
	
telemetry_summary
	
str
	
What telemetry this logsource provides

extract_guidance
	
str
	
What to extract from threat intel
	
fp_prevention
	
str
	
False positive prevention guidance

red_team_focus
	
str
	
Red team review focus areas
	
classifier_keywords
	
tuple
	
Keywords for classification scoring

classifier_regexes
	
tuple
	
Regex patterns for classification
	
keyword_weight
	
float
	
0.12 default — keyword scoring weight

regex_weight
	
float
	
0.15 default — regex scoring weight
	
priority
	
int
	
100 default — generation priority (lower = higher)

##### LOGSOURCE_PROFILES

Dict containing 12+ profiles: process_creation (priority 10), network_connection, file_event, registry_event, dns_query, image_load, process_access, driver_load, pipe_created, file_delete, file_rename, and more.

##### Functions
- get_profile(category, platform) -> LogsourceGenerationProfile — Retrieve profile for category
- list_generation_categories() -> List[str] — All categories with profiles
- format_allowed_fields(category) -> str — Formatted field allowlist for prompts

---

#### Sigma RAG (sigma_rag.py)

> 📚 SimpleSigmaRAG provides retrieval-augmented generation context for Sigma rule creation, including templates, best practices, and category-specific examples.

##### SimpleSigmaRAG

Methods:
- get_sigma_template() -> str — Base Sigma rule YAML template
- get_sigma_best_practices() -> str — 150+ lines of best practices
- get_sigma_examples(category) -> str — Category-specific rule examples
- get_sigma_generation_context(category) -> str — Full context combining template + practices + examples

##### Constants
- SIGMA_RULE_TEMPLATE — Base YAML template
- SIGMA_BEST_PRACTICES — 150+ line best practices document
- SIGMA_VALID_MODIFIERS — Valid Sigma detection modifiers
- SIGMA_VALID_LEVELS — Valid Sigma rule severity levels
- SIGMA_VALID_MODES — Valid Sigma rule modes

---

#### Report Formatter (report_formatter.py)

> 📊 Output formatting for pipeline results in multiple formats. Assembles individual rule results and coverage data into structured reports.

##### ReportRenderer

Methods:
- render_text(report) -> str — Jose-style human-readable text report
- render_json(report) -> str — JSON output
- render_markdown(report) -> str — Markdown output

##### Dataclasses

<details><summary>FormattedRule</summary>

</details>

<details><summary>SourceReport</summary>

</details>

<details><summary>PipelineReport</summary>

</details>

##### Standalone Functions and Constants
- build_source_report(results, coverage) -> SourceReport — Assemble source report
- build_pipeline_report(sources, track) -> PipelineReport — Assemble full pipeline report
- PIPELINE_VERSION = "owlint_sigma v3.0"

---

#### Rule Library (rule_library.py)

> 🗃️ RuleLibrary provides ChromaDB-backed persistent storage, semantic similarity search, and near-duplicate detection for generated Sigma rules.

##### RuleLibrary

Constructor: persist_dir (from settings), embedding_provider

Storage: ChromaDB collection "sigma_rules" with cosine distance

Methods:
- store(rule) -> str — Store rule; checks near-duplicates (>0.90 similarity threshold)
- search_similar(query_text, top_k, threshold, filters) -> List[Tuple[StoredRule, float]] — Semantic similarity search
- coverage_analysis(source_url) -> Dict — Coverage analysis for a source
- get_rule(rule_id) -> Optional[StoredRule] — Retrieve by ID
- retire_rule(rule_id, reason) — Mark rule as retired

##### StoredRule

<details><summary>StoredRule — Full field reference</summary>

</details>

---

#### Embeddings (embeddings.py)

> 🧮 EmbeddingProvider generates Azure OpenAI embeddings for semantic similarity, rule deduplication, and RAG retrieval.

##### EmbeddingProvider

Constructor: model, api_key, endpoint, api_version

Methods:

Method
	
Returns
	
Description

embed_batch(texts, batch_size)
	
List[List[float]]
	
Batch embed multiple texts

embed_detection_description(description)
	
List[float]
	
Embed detection description text

_flatten_selection(value)
	
str
	
Flatten selection dict to string

Properties: client, is_available()

---

#### Detection Knowledge (detection_knowledge.py)

> 🧠 Loads YAML-based detection engineering knowledge and MITRE ATT&CK references for prompt injection. Source: config/detection_knowledge.yaml.

##### Functions
- get_knowledge_for_category(category) -> str — Full detection engineering knowledge for a category
- get_mitre_for_category(category) -> str — MITRE ATT&CK technique references
- get_redteam_knowledge(category) -> str — Condensed knowledge for red team verification prompts

##### Internal Helpers
- _format_granted_access() — Format GrantedAccess bitmask reference
- _format_calltrace() — Format CallTrace pattern reference
- _format_commandline() — Format CommandLine detection patterns
- _format_network_ports() — Format network port reference

---

#### Logger (logger.py)

> 📝 Centralized logging configuration for the pipeline with structured stage and LLM call logging.

##### Functions
- get_logger(name) -> logging.Logger — Get configured logger with optional name suffix
- log_pipeline_stage(stage, status, duration_ms, **extra) — Log pipeline stage events with structured data
- log_llm_call(agent, model, prompt_tokens, completion_tokens, duration_ms, success, error) — Log LLM call metrics

---

#### Observability (observability.py)

> 📡 Optional Langfuse integration for tracing LLM and embedding calls across the pipeline.

##### Functions
- _init_langfuse() -> bool — Lazy Langfuse client initialization
- trace_llm(name, model, input_text, output_text, input_tokens, output_tokens, metadata) — Record an LLM call trace
- trace_embedding(name, model, input_text, embedding_dimensions, duration_ms, prompt_tokens, total_tokens, embedding_vector, metadata) — Record an embedding call trace
- flush() -> None — Flush all pending Langfuse events

---

#### Platforms Base (platforms/base.py)

> 🏗️ Abstract base classes and shared types for all SIEM platform implementations.

##### PlatformType (Enum)

SPLUNK | SENTINEL | ELASTIC | CROWDSTRIKE | CHRONICLE | QRADAR

##### BasePlatform (ABC)

Abstract properties: platform_type, display_name, query_language

Abstract methods:
- get_syntax_reference() — Platform syntax documentation
- get_field_mapping() — Sigma-to-platform field mapping
- get_translation_examples() — Example translations
- validate_query(query) — Platform-specific query validation
- get_detection_patterns() — Common detection patterns

Concrete methods:
- get_reverse_field_mapping() — Inverted field mapping
- format_field_mapping_for_prompt() — Field map formatted for LLM prompts
- format_examples_for_prompt(direction) — Examples formatted for prompts

##### Dataclasses

Dataclass
	
Fields
	
Description

PlatformValidationResult
	
is_valid, errors, warnings
	
Query validation result (property: error_message)

---

#### Platform Registry (platforms/__init__.py)

> 🔌 Registry with lazy loading for all 6 SIEM platform implementations.

##### Functions
- get_platform(platform) -> BasePlatform — Get platform instance by name
- list_platforms() -> List[str] — List all registered platform names
- get_all_platforms() -> List[BasePlatform] — Get all platform instances
- register_platform(platform: BasePlatform) — Register a custom platform

Built-in platforms: Splunk, Sentinel, Elastic, CrowdStrike, Chronicle, QRadar

---

#### LLM Base (llm/base.py)

> 🤖 Abstract base and shared types for the LLM provider abstraction layer.

##### ProviderType (Enum)

AZURE_OPENAI | OPENAI | HUGGINGFACE | OLLAMA | CUSTOM

##### Dataclasses

<details><summary>ModelCapabilities</summary>

</details>

<details><summary>LLMResponse</summary>

</details>

##### BaseLLM (ABC)

Abstract: provider_type, complete(), is_available()

Concrete methods:
- complete_text() — Simple text completion
- classify() — Classification via LLM
- get_info() — Provider/model info

Property: capabilities

---

#### LLM Factory (llm/factory.py)

> 🏭 Factory pattern for creating LLM provider instances with per-agent model configuration.

##### LLMFactory

Methods:
- create(agent_name, provider, model, **kwargs) -> BaseLLM — Create LLM instance
- register_provider(provider_type, provider_class) — Register custom provider
- set_agent_model(agent_name, model) — Override model for specific agent
- list_available_providers() -> list — List registered providers

##### Convenience Function
- get_llm(agent_name, provider, model, **kwargs) -> BaseLLM — Shorthand factory call

---

#### LLM Registry (llm/registry.py)

> 📒 Central model registry with capability metadata, aliases, and task-based recommendations.

##### ModelInfo (dataclass)

Field
	
Type
	
Description

display_name
	
str
	
Human-readable name

capabilities
	
ModelCapabilities
	
Model capabilities

recommended_for
	
list
	
Recommended task types

##### ModelRegistry

Built-in models: gpt-5-mini, gpt-5, gpt-4o, gpt-4o-mini, llama-3.1-70b, mistral-7b, mixtral-8x7b, phi-3-medium, llama-3.1-8b

Methods:
- register(model) — Register a model
- get(model_id) — Get model info by ID or alias
- list_all() — List all registered models
- list_by_provider(provider) — Filter by provider
- list_free() — List free/open models
- recommend_for(task) — Get recommendations for a task type

##### Convenience Functions
- get_model_info(model_id) — Shorthand registry lookup
- list_models() — Shorthand list all

---

#### LLM Providers

##### AzureOpenAIProvider (llm/azure_openai.py)

Extends BaseLLM. Handles reasoning models specially (o1, o3, gpt-5 prefixes).

Methods:
- complete() — Chat completion with reasoning model support
- is_available() — Check endpoint/key availability
- _calculate_cost() — Token-based cost estimation
- _is_reasoning_model() — Detect reasoning model from name

##### OpenAIProvider (llm/openai_provider.py)

Extends BaseLLM. Direct OpenAI API integration.

Methods:
- complete() — Chat completion
- is_available() — Check API key availability
- _calculate_cost() — Token-based cost estimation

---

## Platforms Reference

> 💡 Platforms Reference documents the platform abstraction layer that powers Owlint-Sigma's bidirectional SIEM translation. All 6 SIEM platform implementations inherit from a common abstract base class, providing consistent field mapping, query validation, and translation examples across Splunk, Sentinel, Elastic, CrowdStrike, Chronicle, and QRadar.

Platform Architecture
PlatformType Enum
Abstract Properties
Abstract Methods
Concrete (Inherited) Methods
Data Classes
Platform Registry
Platform Implementations
Platform Detection
PlatformDetector Methods
DetectionCandidate Dataclass
Custom Platform Registration

---

### Platform Architecture

The platform layer lives in platforms/ and is built around a single abstract base class that every SIEM module must implement.

> 💡 BasePlatform(ABC) in platforms/base.py is the abstract base for all SIEM modules. Every platform must implement a fixed contract of properties and methods.

#### PlatformType Enum

Six supported SIEM targets:

SPLUNK | SENTINEL | ELASTIC | CROWDSTRIKE | CHRONICLE | QRADAR

#### Abstract Properties

Property
	
Return Type
	
Description
	
platform_type
	
PlatformType
	
Enum value identifying this platform

display_name
	
str
	
Human-readable platform name
	
query_language
	
str
	
Name of the query language (e.g. SPL, KQL, EQL)

#### Abstract Methods

Method
	
Signature
	
Description
	
get_syntax_reference
	
() -> str
	
Returns platform query syntax reference text

get_field_mapping
	
() -> Dict
	
Sigma field name → platform field name mapping
	
get_translation_examples
	
() -> List[TranslationExample]
	
Example Sigma ↔ platform query pairs

validate_query
	
(query) -> PlatformValidationResult
	
Validate a translated query for structural correctness
	
get_detection_patterns
	
() -> List[str]
	
Regex patterns characteristic of this platform's queries

#### Concrete (Inherited) Methods
- get_reverse_field_mapping() — Inverts the field mapping dict (platform → Sigma)
- format_field_mapping_for_prompt() — Renders field mapping as formatted text for LLM prompts
- format_examples_for_prompt(direction) — Renders translation examples filtered by direction (to_sigma / from_sigma)

#### Data Classes

> 💡 TranslationExample dataclass: sigma_rule (str), platform_query (str), description (str) — pairs a Sigma rule with its platform query equivalent for few-shot prompting.

> 💡 PlatformValidationResult dataclass: is_valid (bool), errors (List[str]), warnings (List[str]), plus an error_message property that joins all errors into a single string.

---

### Platform Registry

platforms/__init__.py provides a central registry with lazy loading.

Function
	
Signature
	
Description

list_platforms
	
() -> List[str]
	
Return names of all registered platforms

register_platform
	
(platform: BasePlatform) -> None
	
Register a custom platform at runtime

> 💡 Lazy Loading: Platform modules are imported on first call to any registry function. This avoids importing all six platform modules at startup and keeps CLI response time fast.

---

### Platform Implementations

Each of the six platforms is implemented as a single-file module in platforms/. Click to expand details.

<details><summary>Splunk (splunk.py) — SplunkPlatform</summary>

</details>

<details><summary>Microsoft Sentinel (sentinel.py) — SentinelPlatform</summary>

</details>

<details><summary>Elastic Security (elastic.py) — ElasticPlatform</summary>

</details>

<details><summary>CrowdStrike Falcon (crowdstrike.py) — CrowdStrikePlatform</summary>

</details>

<details><summary>Google Chronicle (chronicle.py) — ChroniclePlatform</summary>

</details>

<details><summary>IBM QRadar (qradar.py) — QRadarPlatform</summary>

</details>

---

### Platform Detection

platform_detector.py provides automatic SIEM identification from raw query text.

> 💡 PlatformDetector analyzes query text against each platform's regex detection patterns, counts matches, and scores confidence to identify the source SIEM.

#### PlatformDetector Methods

Method
	
Signature
	
Description

detect_all
	
(query: str) -> List[DetectionCandidate]
	
Returns all candidates sorted by confidence (descending)

#### DetectionCandidate Dataclass

Field
	
Type
	
Description
	
platform
	
BasePlatform
	
The matched platform instance

confidence
	
float
	
Score from 0.0 to 1.0
	
matched_patterns
	
List[str]
	
Which regex patterns matched in the query

Mechanism: Each platform provides a list of regex patterns via get_detection_patterns(). The detector runs all patterns against the query text, counts matches per platform, and normalizes scores to produce a confidence ranking.

---

### Custom Platform Registration

To add a new SIEM platform to Owlint-Sigma:
1. Create a new module in platforms/ (e.g. platforms/my_siem.py)
1. Define a class inheriting from BasePlatform:

```
from platforms.base import BasePlatform, PlatformType

class MySiemPlatform(BasePlatform):
    @property
    def platform_type(self) -> PlatformType:
        return PlatformType.MY_SIEM  # add to enum first

    @property
    def display_name(self) -> str:
        return "My SIEM"

    @property
    def query_language(self) -> str:
        return "MSQL"

    def get_syntax_reference(self) -> str:
        return "SELECT ... FROM events WHERE ..."

    def get_field_mapping(self) -> dict:
        return {"Image": "process_path", ...}

    def get_translation_examples(self):
        return [TranslationExample(...)]

    def validate_query(self, query):
        return PlatformValidationResult(is_valid=True, errors=[], warnings=[])

    def get_detection_patterns(self):
        return [r"my_siem_keyword", r"FROM my_table"]

​
```
1. Register at runtime:

```
from platforms import register_platform
from platforms.my_siem import MySiemPlatform

register_platform(MySiemPlatform())

​
```

Once registered, the new platform is available for translation, detection, and all registry functions.

---

> 💡 Last updated: April 5, 2026 | Version: 5.0 | Maintainer: LevelBlue

---

## Field & Logsource Reference

> 💡 Field & Logsource Reference — Authoritative mappings between Sigma logsource categories, allowed detection fields, and generation profiles used by Owlint-Sigma for validation and LLM-guided rule generation.

Overview
Logsource Categories & Field Counts
Generation Profiles (LOGSOURCE_PROFILES)
Key Profiles
Field Placement Validation
Classification Process
MITRE ATT&CK Integration

---

### Overview

Owlint-Sigma maintains authoritative mappings between Sigma logsource categories and allowed detection fields. These are used for validation (rejecting misplaced fields) and generation (guiding LLM prompts).

The system enforces that each detection field appears only in categories where it is semantically valid. This prevents common mistakes like using CommandLine in a dns_query rule or QueryName in a process_creation rule.

---

### Logsource Categories & Field Counts

The following table documents all primary logsource categories, their field counts, and key fields:

Category
	
Field Count
	
Key Fields

process_creation
	
33
	
Image, CommandLine, ParentImage, OriginalFileName, md5, sha256, User, IntegrityLevel

network_connection
	
12
	
DestinationIp, DestinationPort, Protocol, SourceIp, SourcePort, Initiated

file_event
	
9
	
TargetFilename, CreationUtcTime, Hashes, Image

registry_event
	
7
	
TargetObject, Details, EventType, NewName

dns_query
	
6
	
QueryName, QueryStatus, QueryResults

image_load
	
10
	
ImageLoaded, Signed, SignatureStatus, Hashes, Image

driver_load
	
8
	
ImageLoaded, Signed, Signature, Hashes

pipe_created
	
4
	
PipeName, Image, User

process_access
	
6
	
SourceImage, TargetImage, GrantedAccess, CallTrace

firewall
	
9
	
Action, Protocol, SourceIp, DestinationIp, Direction

proxy
	
12
	
c-uri, c-useragent, cs-host, r-dns, sc-status

webserver
	
10
	
c-uri, cs-method, cs-referrer, sc-status, c-ip

syslog
	
9
	
EventID, RuleName, facility, severity

cloud
	
14
	
eventSource, eventName, sourceIPAddress, errorCode, userIdentity

> 💡 Category Aliases — The following categories share their parent's field allowlists:
> registry_add, registry_delete, registry_set → inherit from registry_event
> file_creation, file_change, file_delete, file_rename → inherit from file_event

---

### Generation Profiles (LOGSOURCE_PROFILES)

12+ profiles, each a LogsourceGenerationProfile dataclass containing:
- category — the Sigma logsource category
- product — target product (e.g., windows, linux)
- telemetry_summary — description of what telemetry this category captures
- extract_guidance — instructions for extracting detection logic
- fp_prevention — false positive prevention guidance
- red_team_focus — adversary simulation perspective
- classifier_keywords — keyword list for automatic input classification
- classifier_regexes — regex patterns for classification
- keyword_weight (default 0.12) — scoring weight for keyword matches
- regex_weight (default 0.15) — scoring weight for regex matches
- priority — profile priority for tie-breaking

#### Key Profiles

<details><summary><strong>process_creation</strong> (Priority 10 — Highest)</summary>

</details>

<details><summary><strong>network_connection</strong></summary>

</details>

<details><summary><strong>file_event</strong></summary>

</details>

<details><summary><strong>registry_event</strong></summary>

</details>

<details><summary><strong>dns_query</strong></summary>

</details>

<details><summary><strong>image_load</strong></summary>

</details>

<details><summary><strong>process_access</strong></summary>

</details>

<details><summary><strong>driver_load</strong></summary>

</details>

<details><summary><strong>pipe_created</strong></summary>

</details>

<details><summary><strong>file_delete / file_rename</strong></summary>

</details>

---

### Field Placement Validation

> 💡 Strict Enforcement — Any detection field not present in the category's allowlist triggers a validation error. This is a hard failure, not a warning.
- field_logsource_map.yaml maps 40+ fields to their allowed categories
- During validation, each field in the detection block is checked against the active category's allowlist
- format_exclusive_field_map(category) -> str — formats the allowlist as guidance text injected into LLM prompts, ensuring the model only uses valid fields

---

### Classification Process

The classification pipeline determines which logsource categories are appropriate for a given input:

```
classify_logsources(text, min_score=0.15) -> ClassificationResult

​
```

Scoring mechanism:
1. Each profile's classifier_keywords are matched against the input text
1. Each profile's classifier_regexes are evaluated against the input text
1. Keyword matches are weighted by keyword_weight (default 0.12)
1. Regex matches are weighted by regex_weight (default 0.15)
1. Scores are summed per category

> 💡 Key Thresholds:
> classification_min_score = 0.15 — categories scoring below this are discarded
> ruleset_max_categories = 6 — maximum categories selected per generation run

---

### MITRE ATT&CK Integration
- config/mitre_attack_reference.yaml provides per-category tactics and techniques
- Full sub-technique support (e.g., T1059.001 — PowerShell under Command and Scripting Interpreter)
- Integrated into rule generation for accurate tags: field population
- Each logsource category maps to its most commonly associated ATT&CK techniques

---

> 💡 Last updated: April 5, 2026 | Source: field_logsource_map.yaml, logsource_profiles.py, mitre_attack_reference.yaml

---

## Configuration System

Owlint-Sigma uses pydantic-settings for configuration management via the SigmaSettings class in config.py with .env file support. Configuration is loaded once via get_settings() (cached with @lru_cache).

> 💡 Property: use_azure -> bool (auto-detected from credentials)
> Singleton: get_settings() -> SigmaSettings (cached via @lru_cache)

---

### Environment Variables (SigmaSettings)

#### Azure OpenAI

#### Embeddings

#### Rule Library

#### Sigma Generation

#### Translation

#### Logging / Output

#### LangFuse Observability

---

### YAML Knowledge Configs

> 💡 Four YAML configuration files provide domain knowledge injected into LLM prompts and used for validation. These are not environment variables -- they are loaded at runtime from the config/ directory.

File
	
Purpose
	
Key Contents

config/detection_knowledge.yaml
	
Per-category detection engineering reference injected into LLM prompts
	
granted_access patterns, network_ports (high/medium/low noise), commandline_patterns, calltrace_patterns, process_signatures, field_semantics. ~400+ lines.

config/mitre_attack_reference.yaml
	
MITRE ATT&CK sub-technique hints per logsource category
	
Per-category tactics and techniques with indicators of compromise.

config/field_logsource_map.yaml
	
Authoritative Sigma field-to-logsource mapping
	
Maps 40+ fields to allowed logsource categories (e.g., SignatureStatus: [image_load, driver_load]).

config/siem_field_maps/*.yaml
	
Per-platform SIEM translation definitions
	
query_language, tables, field_map, modifier_map, condition_template, notes.

---

### SIEM Field Maps

> 💡 Each platform YAML in config/siem_field_maps/ defines the translation layer between Sigma and a target SIEM. Add a new file to support a new platform.

Key
	
Type
	
Description

query_language
	
str
	
The native query language name (e.g., SPL, KQL, YARA-L).

tables
	
dict
	
Per sigma_category table/index mappings for the platform.

field_map
	
dict
	
Bidirectional field name mappings (Sigma field <-> platform field).

modifier_map
	
dict
	
Modifier translations: contains, startswith, endswith, re, etc.

condition_template
	
str
	
Native query template pattern used for rule output.

notes
	
str
	
Platform-specific caveats, limitations, and behavioral differences.

---

### LLM Integration

> 💡 The llm/ subpackage provides a pluggable LLM abstraction layer. Provider is auto-detected from available credentials via get_llm().

#### Architecture

#### Supported Providers

#### Built-in Model Registry

---

## Project Structure & Dependencies

### Project Structure

> 💡 The installable product is owlint-sigma (package name) / owlint_sigma (import name) located under the owlint_sigma/ directory.

---

#### Directory Layout

Path
	
Purpose

owlint_sigma/owlint_sigma/
	
Main Python package (generator, translator, validator, LLM, platforms)

owlint_sigma/owlint_sigma/llm/
	
LLM abstractions, factory, registry, Azure OpenAI + OpenAI providers

owlint_sigma/owlint_sigma/platforms/
	
Per-SIEM modules (Splunk, Sentinel, Elastic, CrowdStrike, Chronicle, QRadar)

owlint_sigma/config/
	
YAML knowledge: detection engineering, MITRE, field-logsource map

owlint_sigma/config/siem_field_maps/
	
Per-platform, per-logsource-category field maps for translation prompts

owlint_sigma/tests/
	
Pytest test suites

owlint_sigma/architecture/
	
System diagram (owlint_sigma.drawio)

output/
	
Generated artifacts from pipeline runs

---

#### Module Map

Module
	
Role

init.py
	
Public exports: generators, translator, validator, decomposer, reports, RAG, platforms

main.py
	
CLI: interactive menu + argparse subcommands

config.py
	
SigmaSettings (pydantic-settings): all configuration

generator.py
	
SmartSigmaGenerator: tiered prompts, self-healing, red-team, companions

detection_decomposer.py
	
DetectionDecomposer, DetectionUnit, CoverageReport

translator.py
	
SigmaTranslator: to_sigma, from_sigma, translate

validator.py
	
SigmaValidator: multi-pass validation

query_validator.py
	
QueryValidator: post-translation structural checks

fitness.py
	
ContentFitnessAssessor: suitability scoring

content_preprocessor.py
	
ContentPreprocessor: normalization, classification

platform_detector.py
	
PlatformDetector: infer SIEM from query text

sigma_logsources.py
	
Field allowlists per logsource

siem_schemas.py
	
Load/format SIEM YAML schemas

sigma_rag.py
	
SimpleSigmaRAG: templates, best practices, examples

report_formatter.py
	
ReportRenderer, PipelineReport

rule_library.py
	
RuleLibrary: ChromaDB persistence, dedup, search

embeddings.py
	
EmbeddingProvider for rule similarity

observability.py
	
Optional Langfuse tracing

logger.py
	
Structured logging helpers

detection_knowledge.py
	
Loads YAML knowledge for prompt injection (get_knowledge_for_category, get_mitre_for_category, get_redteam_knowledge)

platforms/base.py
	
BasePlatform ABC, PlatformType enum, TranslationExample, PlatformValidationResult

platforms/init.py
	
Platform registry: get_platform, list_platforms, register_platform, get_all_platforms

platforms/splunk.py
	
SplunkPlatform (SPL)

platforms/sentinel.py
	
SentinelPlatform (KQL)

platforms/elastic.py
	
ElasticPlatform (EQL)

platforms/crowdstrike.py
	
CrowdStrikePlatform (CQL)

platforms/chronicle.py
	
ChroniclePlatform (YARA-L)

platforms/qradar.py
	
QRadarPlatform (AQL)

---

#### Standalone Scripts
- audit_rules.py — Parse text/JSON reports into CSV-style findings
- run_live_pipeline.py — End-to-end live run with real LLM (uses TIPPER_LOG_DIR)

---

### Dependencies

Package
	
Version
	
Purpose

openai
	
>= 1.0.0, < 2.0.0
	
LLM API client (OpenAI + Azure)

pyyaml
	
>= 6.0.0, < 7.0.0
	
YAML parsing for Sigma rules and configs

pydantic
	
>= 2.0.0, < 3.0.0
	
Data validation and settings management

pydantic-settings
	
>= 2.0.0, < 3.0.0
	
Environment-based configuration

python-dotenv
	
>= 1.0.0, < 2.0.0
	
.env file loading

langfuse
	
>= 2.0.0, < 3.0.0
	
LLM observability and tracing

chromadb
	
>= 0.4.0
	
Vector database for rule library

numpy
	
>= 1.24.0
	
Numerical operations for embeddings

PyMuPDF (optional)
	
—
	
PDF input parsing

Packaging is via setup.py (no pyproject.toml). Install with pip install -e . from the owlint_sigma/ directory.

---

#### __init__.py Public Exports (49 symbols)

The package's __init__.py exposes 49 public symbols organized by domain:

Category
	
Exports

Generation
	
SmartSigmaGenerator, SigmaGenerator, SingleRuleResult, RulesetGenerationResult, CompanionFailure

Reporting
	
FormattedRule, SourceReport, PipelineReport, ReportRenderer, build_source_report, build_pipeline_report

Decomposition
	
DetectionDecomposer, DetectionUnit, PlatformQueryHint, CoverageReport

Translation
	
SigmaTranslator, PlatformDetector

Validation
	
SigmaValidator, SigmaValidationResult, sanitize_sigma_yaml

Fitness
	
ContentFitnessAssessor, FitnessResult

Logsource Profiles
	
LogsourceGenerationProfile, LOGSOURCE_PROFILES, get_profile, list_generation_categories, format_allowed_fields

Content Preprocessing
	
ContentPreprocessor, NormalizedIntelInput, ClassificationResult, IntelInputKind, normalize_intel_input, classify_logsources

RAG / Knowledge
	
SimpleSigmaRAG, get_sigma_template, get_sigma_best_practices, get_sigma_examples, get_sigma_generation_context

Log Sources
	
get_fields_for_logsource, list_categories

Platforms
	
get_platform, list_platforms, register_platform

LLM
	
BaseLLM, LLMResponse, get_llm

Embeddings
	
EmbeddingProvider

Rule Library
	
RuleLibrary, StoredRule

---

## Testing & Quality Assurance

### Testing

Run the test suite from the owlint_sigma/ directory:

> cd owlint_sigma && pip install -e . && python -m pytest tests/ -v

---

#### Test Suites

Test Suite

test_audit.py

test_audit.py classes: TestDeadFiltersJoseExamples (tests 1-5, Jose's specific dead filter cases), TestDeadFiltersUniversal (tests 6-10, additional dead filter cases), TestValidFilterPatterns (tests 11-14, should NOT trigger errors), TestFieldPlacementJoseExamples (tests 15-21, field placement error cases), TestFieldPlacementUniversal (tests 22-28, additional field placement), TestCorrectFieldPlacement (tests 29-34, should NOT trigger errors), TestCounterproductiveFilters, TestPlatformConsistency, TestDetectionQualityOverhaul

test_cli.py

test_cli.py classes: TestHelpOutput (--help on root and subcommands), TestArgParsing (argument parser correctness for all 3 tracks), TestInputValidation (path/platform/output dir validation), TestLoadSigmaRules (load from file/directory/multi-doc), TestMainDispatch (routes to correct track or exits), TestSourceSplitting (multi-source document segmentation)

test_universality_proofs.py

test_universality_proofs.py classes: TestUniversalDeadFilters (proves dead filter detection works for any field/category combination, not just hard-coded cases), TestUniversalFieldPlacement (proves field placement checks are universal across all field/category combinations)

---

### Quality Assurance Layers

Owlint-Sigma implements six layers of validation to ensure rule quality:
1. Sigma Structural Validation — YAML structure, required fields, logsource format
1. Field Allowlist Validation — Fields checked against field_logsource_map.yaml per category
1. Red-Team Review — LLM-powered adversarial review of generated rules
1. Self-Healing Loops — Automatic repair attempts when validation fails
1. Query Validation — Post-translation structural checks against field maps
1. Fitness Assessment — Pre-generation suitability scoring of input content

---

### Live Pipeline Testing

run_live_pipeline.py — Standalone script for end-to-end live pipeline execution with real LLM calls. Uses TIPPER_LOG_DIR environment variable for output directory. Exercises the full generation/translation/validation pipeline against actual LLM providers to verify integration beyond unit tests.

---

### Audit Pipeline

The standalone audit script (audit_rules.py) provides:
- Parsing of text and JSON pipeline reports
- CSV-style findings output
- Rule-by-rule status, title, and error details
- Integration with SigmaValidator for deep validation

---

### Coverage Reporting

The coverage_report.yml output tracks per-source detection coverage with these statuses:
- covered — Detection unit has a corresponding Sigma rule
- not_coverable — Detection unit cannot be expressed in Sigma
- uncovered — Detection unit could be covered but was not
- covered_by_existing — Matched by an existing rule in the library
- partial — Partially covered detection

---

## CLI Usage & Output Formats

#### Interactive Mode

Run without arguments for an interactive menu:

python -m owlint_sigma

Presents three options:
- 1 DFIR to Sigma to SIEM
- 2 Sigma to SIEM
- 3 SIEM to Sigma

---

#### Subcommands

##### Track 1: dfir-to-sigma

python -m owlint_sigma dfir-to-sigma -i report.md -s splunk -o ./output

Arguments:
- -i / --input: Input file (.txt, .md, .pdf, .json, .html)
- -s / --siem: Target SIEM platform (optional)
- -o / --output: Output directory (default: ./output)

##### Track 2: sigma-to-siem

python -m owlint_sigma sigma-to-siem -i rules/ -s sentinel -o ./output

Arguments:
- -i: Sigma YAML file or directory of files
- -s: Target SIEM platform (required)
- -o: Output directory

##### Track 3: siem-to-sigma

python -m owlint_sigma siem-to-sigma -i query.txt -s splunk -o ./output

Arguments:
- -i: File containing SIEM query
- -s: Source SIEM platform (required)
- -o: Output directory

##### Standalone Audit

python audit_rules.py /path/to/report.txt

Parses text/JSON pipeline reports and produces CSV-style findings.

---

### Output Formats

File
	
Format
	
Description

sigma_rules.yml
	
YAML (multi-doc)
	
Separated Sigma YAML documents for all passing rules

queries_{platform}.txt
	
Text
	
Commented blocks per rule with native SIEM queries

audit.csv
	
CSV
	
rule number, title, status, errors from SigmaValidator

coverage_report.yml
	
YAML
	
Per-source coverage: step IDs, categories, statuses, reasons, metrics

Coverage statuses: covered, not_coverable, uncovered, covered_by_existing, partial

Reporting API: ReportRenderer and build_pipeline_report() support Text, JSON, and Markdown output formats.

---

### Python API Examples

#### Generate Rules from Threat Intel

from owlint_sigma import SigmaGenerator

generator = SigmaGenerator()

result = generator.generate_ruleset(threat_intel_text)

#### Translate Sigma to SIEM

from owlint_sigma import SigmaTranslator

translator = SigmaTranslator()

query = translator.from_sigma(sigma_yaml, target_platform="splunk")

#### Translate SIEM to Sigma

from owlint_sigma import SigmaTranslator

translator = SigmaTranslator()

sigma_rule = translator.to_sigma(siem_query, source_platform="sentinel")

---

## Audit Engine Reference

#### Overview

> 💡 The audit engine (audit_rules.py) provides deep rule-quality analysis beyond what SigmaValidator checks. It parses pipeline output reports and runs heuristic checks that catch logic errors, field misuse, and cross-rule inconsistencies. At 700+ lines, it is the standalone audit and quality checking engine for the project.

---

#### Report Parsing Functions

> 💡 These two entry-point parsers convert raw pipeline output into structured rule dictionaries for downstream checks.
- extract_rules_from_text(content: str) -> List[Dict] — Parse text-format pipeline reports into structured rule dictionaries
- extract_rules_from_json(content: str) -> List[Dict] — Parse JSON-format pipeline reports into structured rule dictionaries

---

#### Single-Rule Checks

Each function accepts a parsed rule dictionary and returns a List[str] of findings. An empty list means the rule passed that check.

#
	
Check Function
	
Description
	
Example Finding
	
1
	
check_dead_filters(parsed)
	
Detects filter-selection value mismatches — contradictory values on the same field
	
Filter says Image contains cmd.exe but selection also checks for Image containing powershell.exe

2
	
check_field_placement(parsed, category)
	
Verifies fields belong to the declared logsource category using field_logsource_map.yaml
	
Field TargetFilename used in a process_creation rule (belongs to file_event)
	
3
	
check_duplicate_fields(parsed)
	
Finds duplicate field specifications in detection logic
	
Field CommandLine appears twice in the same selection block

4
	
check_counterproductive_filters(parsed)
	
Heuristic check: filter values that contradict the detection intent
	
Rule detects mimikatz but filter excludes lsass.exe — counterproductive
	
5
	
check_platform_consistency(parsed)
	
Windows/Linux path mismatches in rules
	
Windows paths like C:\Windows\ found in a rule declared for Linux

6
	
check_detection_specificity(parsed)
	
Warns if detection is too broad (insufficient specificity)
	
Rule only checks a single generic field value with no additional conditions
	
7
	
check_private_ip_filter(parsed)
	
Network rules need private IP exclusion filters
	
Network connection rule missing RFC1918 private IP range exclusions

---

#### Cross-Rule Analysis

> 💡 check_cross_rule_coherence(rules: list) -> List[dict] analyzes multiple rules together for systemic issues:
1. Filter inconsistency — Different filtering approaches across rules targeting the same logsource category
1. Redundancy detection — Rules covering overlapping detections that could be consolidated
1. Logic contradictions — Rules whose detection and filtering logic conflict with each other

---

#### Full Audit Pipeline

audit_report(report_path: str) -> List[Dict] — Runs all checks end-to-end and outputs CSV-style findings.

> 💡 Each finding record includes:
> Rule number and title for identification
> Status: pass, fail, or warning
> Error details per check type
> Integrates with SigmaValidator for deep validation

---

#### CLI Usage

```
python audit_rules.py /path/to/report.txt

​
```

---

#### Constants

Constant
	
Purpose
	
_STOP_WORDS
	
Common words filtered out during intent analysis to improve heuristic accuracy

_LINUX_INDICATORS
	
Regex patterns for Linux-specific paths and processes (e.g., /usr/bin/, /etc/)
	
_WINDOWS_INDICATORS
	
Regex patterns for Windows-specific paths and processes (e.g., C:\Windows\, .exe)

---

## Step-Based Detection Logic: Improving Sigma Rule Quality Through Structured TTP Coverage

#### Overview

This page documents a detection engineering methodology observed in LevelBlue's threat intelligence workflow — structuring detection logic as multi-step, sequenced detection chains rather than isolated, single-event Sigma rules. Each step targets a distinct phase of an attacker's TTP (Tactics, Techniques, and Procedures), creating layered coverage that mirrors the actual kill chain.

This approach significantly improves the depth, accuracy, and resilience of Sigma-based detection.

---

#### The Core Idea

> 💡 Instead of writing one Sigma rule per threat report, decompose each threat into sequential detection steps — each targeting a specific phase of the attack lifecycle. This produces multiple focused rules per threat, with clear logical ordering.

Traditional approach:
- Read threat report → write 1-2 Sigma rules → done

Step-based approach:
- Read threat report → identify each attack phase → write a detection step per phase → link them as a chain

---

#### Why This Improves Sigma Rule Quality

##### 1. Kill Chain Alignment

Each step maps to a real phase of the attack. This means rules are grounded in attacker behavior, not just IOCs. When one step fires, analysts know exactly where in the attack chain the activity sits.

##### 2. Granular, Testable Rules

Single-step rules are easier to test, tune, and maintain. A noisy alert can be isolated to one step without breaking the entire detection. Each rule has a narrow, well-defined scope.

##### 3. Defense-in-Depth Coverage

If an attacker evades Step 1 (e.g., supply chain entry), Step 2 (execution abuse) or Step 3 (C2 connections) can still catch them. Multiple independent detection opportunities per threat.

##### 4. Improved Analyst Context

When a Step 3 alert fires, the analyst immediately knows:
- What came before (Steps 1-2)
- What to look for next (Steps 4+)
- Where in the kill chain this sits

This dramatically reduces mean time to understand (MTTU).

##### 5. Correlation Potential

Step-based rules naturally feed into correlation rules. If Step 1 + Step 3 fire on the same host within a time window, that's a high-confidence compound detection that single rules can't achieve.

---

#### Real-World Examples

<details><summary>Example 1: Supply Chain Poisoning via Malicious AI Skills (OpenClaw)</summary>

</details>

<details><summary>Example 2: VoidStealer Browser Credential Theft (ABE Bypass)</summary>

</details>

<details><summary>Example 3: TeamPCP Supply Chain Attack (Checkmarx/GitHub Actions)</summary>

</details>

---

#### Mapping to Sigma Rule Design

> 💡 Each Step in the detection logic maps to one or more Sigma rules. The step description provides the rule's detection logic, while the step number provides ordering and correlation context.

##### Recommended Sigma Rule Naming Convention

```
<threat_name>_step<N>_<detection_focus>

​
```

Examples:
- voidstealer_step1_suspicious_browser_spawn
- voidstealer_step2_debugger_attachment
- teampcp_step3_ci_credential_harvesting

##### Sigma Rule Enrichment

Each rule generated from a step should include:
- tags: MITRE ATT&CK technique IDs for that specific step
- related: references to other rules in the same chain
- description: explicit step number and what phase it covers
- level: escalating severity as steps progress (low → medium → high → critical)

---

#### How to Apply This Methodology
1. Ingest a threat intelligence report or blog post
1. Decompose the attack into sequential phases (entry → execution → persistence → lateral movement → exfiltration)
1. Write detection logic for each phase as a numbered step
1. Convert each step into one or more Sigma rules
1. Link the rules with correlation metadata
1. Test each step independently, then test the chain as a whole

---

#### Impact Assessment

Metric
	
Traditional (Single Rule)
	
Step-Based (Chained)

Kill chain coverage
	
Partial (usually one phase)
	
Full (all phases)

Correlation capability
	
None
	
Built-in (step ordering)

Evasion resistance
	
Low (single point of failure)
	
High (multiple detection layers)
