# IRCA - Incident Response & Automated Remediation Platform

**IRCA** is an intelligent cybersecurity platform that automates incident response workflows by integrating with Cybereason's detection platform, leveraging AI for threat analysis, and providing automated remediation capabilities.

## 🎯 Project Overview

The IRCA platform streamlines the incident response process through four main components:

1. **Data Collection**: Automated gathering of security events and malops from Cybereason
2. **AI Analysis**: GPT-4o powered threat assessment and incident narrative generation  
3. **Report Generation**: Professional PDF reports with MITRE ATT&CK mapping
4. **Automated Remediation**: LangGraph-based agent for executing remediation actions

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐    ┌──────────────┐
│   Cybereason    │───▶│ Data         │───▶│ AI Analysis     │───▶│ PDF Report   │
│   Platform      │    │ Collector    │    │ (GPT-4o)        │    │ Generator    │
└─────────────────┘    └──────────────┘    └─────────────────┘    └──────────────┘
                                                    │
                                                    ▼
┌─────────────────┐    ┌──────────────┐    ┌─────────────────┐
│   Cybereason    │◀───│ Remediation  │◀───│ Remediation     │
│   API           │    │ Execution    │    │ Agent           │
└─────────────────┘    └──────────────┘    └─────────────────┘
```

## ⚡ Quick Start

**Ready to run? Here's the fastest way to get started:**

```bash
# 1. Navigate to the IRCA directory
cd IRCA

# 2. Install dependencies (creates venv automatically)
uv sync

# 3. Activate virtual environment (CRITICAL!)
source .venv/bin/activate    # On Windows: .venv\Scripts\activate

# 4. Run the POC Demo (recommended for testing)
streamlit run streamlit_ui_poc.py --server.port=8503

# 5. Open your browser to: http://localhost:8503
```

---

## 🚀 Installation

### Prerequisites
- Python 3.11+ 
- Azure OpenAI API key
- Cybereason platform credentials

### Setup

1. **Clone the repository:**
```bash
git clone --branch IRCA git@github.com:cybereason-labs/research_notebooks.git IRCA
cd IRCA/IRCA
```

2. **Install dependencies:**
```bash
# Using uv (recommended) - this will automatically create venv and install everything
uv sync

# To activate the virtual environment:
source .venv/bin/activate  # On Linux/macOS
# or
.venv\Scripts\activate     # On Windows

# Alternative: Traditional pip method (still supported)
python3 -m venv .venv
source .venv/bin/activate  
pip install -r requirements.txt
```

**Note**: The project now uses `uv.lock` for reproducible dependency management. The `uv sync` command will:
- Create a virtual environment with the exact Python version specified (3.11)
- Install all dependencies with exact versions from `uv.lock`
- Ensure 100% reproducible builds across different machines and environments
- Resolve dependency conflicts automatically
- Install packages 10-100x faster than traditional pip


### 🔧 Managing Dependencies

```bash
# Add a new dependency
uv add package-name

# Add development dependency  
uv add --dev pytest

# Update dependencies and regenerate lock file
uv lock --upgrade

# Remove a dependency
uv remove package-name

# Export to requirements.txt (for compatibility)
uv pip freeze > requirements.txt
```

3. **Configure environment variables:**
```bash
# Navigate to IRCA directory
cd IRCA

# Create .env file with your credentials:
# AZURE_API_KEY=your_azure_openai_api_key
# AZURE_ENDPOINT=https://your-resource.openai.azure.com/
# AZURE_OPENAI_API_VERSION=your_api_version
# AZURE_MODEL_TYPE="remote"
# AZURE_OPENAI_TYPE="azure"
# CYBEREASON_USERNAME=your_username
# CYBEREASON_PASSWORD=your_password
# CYBEREASON_SERVER=your-server.cybereason.net
# CYBEREASON_PORT=443
```

4. **Google Cloud Storage Setup:**
Upload your Google service account JSON file to `IRCA/service_account.json`

## 💻 User Interfaces

IRCA provides two Streamlit-based web interfaces for different use cases:

### 🔬 POC Streamlit UI (`streamlit_ui_poc.py`)

**Purpose**: Demonstration and testing environment with fallback capabilities.

**Key Features**:
- ✅ **Fallback Data Handling**: Automatically uses sample data when live APIs fail
- ✅ **Demo Mode**: Perfect for presentations and testing
- ✅ **Content Filter Bypass**: Handles Azure OpenAI content filtering automatically
- ✅ **Real-time Report Generation**: Creates new PDFs using static LLM responses
- ✅ **Interactive Remediation**: Step-by-step remediation workflow

**When to Use**: 
- Demonstrations and POCs
- Testing without live Cybereason access
- Development and debugging

**Run Command**:
```bash
# Navigate to the parent directory (research_notebooks/)
cd research_notebooks

# Run POC Streamlit UI
streamlit run IRCA/streamlit_ui_poc.py --server.port=8503
```

**Access URL**: http://localhost:8503

### 🏭 Streamlit UI (`streamlit_ui.py`)

**Purpose**: interface for live incident response operations.

**Key Features**:
- ✅ **Live Data Collection**: Direct integration with Cybereason platform
- ✅ **Real-time AI Analysis**: Dynamic GPT-4o threat assessment
- ✅ **Production Remediation**: Full API integration for live remediation
- ✅ **Session Management**: Complete workflow state tracking
- ✅ **Comprehensive Logging**: Detailed audit trails

**When to Use**:
- Live incident response operations
- Production security workflows  
- Real threat remediation

**Run Command**:
```bash
# Navigate to the parent directory (research_notebooks/)
cd research_notebooks

# Run Production Streamlit UI
streamlit run IRCA/streamlit_ui.py --server.port=8501
```

**Access URL**: http://localhost:8501

## 🔄 Complete Workflow

### Phase 1A: Data Collection
1. **Initialize Data Collector** - Connect to Cybereason platform
2. **Collect Incident Data** - Gather malops, processes, and detection events
3. **Arrange Data** - Structure and normalize collected information

### Phase 1B: Report Generation  
1. **AI Analysis** - GPT-4o analyzes collected data and generates insights
2. **Create Narrative** - Build chronological attack timeline
3. **Generate PDF** - Professional report with MITRE ATT&CK mapping

### Phase 2: Automated Remediation
1. **Initialize Agent** - Setup LangGraph remediation agent
2. **Parse Instructions** - Extract remediation targets using AI/regex
3. **Execute Actions** - Perform kill process, quarantine file, etc.
4. **Validate Results** - Confirm successful remediation

## 📁 Output Directory Structure

All pipeline results are saved to `IRCA/outputs/` with timestamped directories:

```
IRCA/outputs/
├── bb-win11-23h2_1754341200000_2025-08-26_11-52-08/    # Latest pipeline run
│   ├── bb-win11-23h2_1754341200000_data.json       # Raw collected data
│   ├── bb-win11-23h2_1754341200000_arranged_data.json  # Processed data
│   ├── bb-win11-23h2_1754341200000_report_*.pdf    # Generated PDF reports
│   ├── bb-win11-23h2_1754341200000_llm_response_*.json  # AI analysis
│   ├── bb-win11-23h2_1754341200000_remediation_*.json  # Remediation actions
│   └── pipeline.log                                 # Execution logs
└── 
```

**🔍 File Types:**
- **`_data.json`**: Raw malops and detection events from Cybereason
- **`_arranged_data.json`**: Processed and organized incident data  
- **`_report_*.pdf`**: AI-generated incident response reports
- **`_llm_response_*.json`**: Raw AI analysis and recommendations
- **`_remediation_*.json`**: Extracted remediation action lists
- **`pipeline.log`**: Detailed execution logs and debugging info

## 🛠️ Core Components

### Data Collector (`data_collector.py` , `json_arranger.py`)
- Cybereason API integration
- Malop and detection event collection
- Data enrichment and processing

### AI Analysis (`prompt_builder.py`, `utils/llms/azure_api.py`)  
- GPT-4o powered threat analysis
- Incident narrative generation
- MITRE ATT&CK technique mapping

### Report Generator (`report_generator_figma.py`)
- Professional PDF report creation
- Figma-style design system
- Logo integration and branding

### Remediation Agent (`agent.py`)
- LangGraph-based decision engine
- Natural language instruction parsing
- Cybereason API remediation execution

## 📋 Configuration Options

### Machine and Time Settings (`configuration.py`)
```python
MACHINE_NAME = "bb-win11-23h2"           # Target machine
START_TIME = 1754341200000               # Investigation start (epoch ms)
END_TIME = 1754514000000                 # Investigation end (epoch ms)
AZURE_MODEL_NAME = "gpt-4o"               # AI model selection
```
You can control the parameters of the api request on the config.py

### Environment Variables (`.env`)
```bash
# Azure OpenAI
AZURE_API_KEY=your_azure_api_key
AZURE_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_VERSION=your_api_version
AZURE_MODEL_TYPE="remote"
AZURE_OPENAI_TYPE="azure"


# Cybereason Platform  
CYBEREASON_USERNAME=your_username
CYBEREASON_PASSWORD=your_password
CYBEREASON_SERVER=your_server.cybereason.net
CYBEREASON_PORT=443
```

## 🔧 Development & Debugging

### Logging
All components generate detailed logs in `outputs/*/pipeline.log`:
```bash
# View latest logs
tail -f src/outputs/*/pipeline.log
```

### Session Reset
Both UIs include session reset functionality:
- Look for "⚡ Quick Actions" in the sidebar
- Click "🔄 Reset Session" button


## 🚨 Troubleshooting

### Common Issues

**1. Azure OpenAI Content Filter Errors**
- The POC UI automatically handles content filtering
- Problematic filenames (e.g., Pokemon names) are sanitized automatically

**2. Empty API Responses**  
- Check Cybereason credentials in `.env`
- Verify network connectivity to Cybereason server
- Use POC UI for fallback data when APIs are unavailable

**3. Import/Module Errors**
```bash
# CRITICAL: Always run from research_notebooks/ directory, NOT from IRCA/
cd research_notebooks
streamlit run IRCA/streamlit_ui_poc.py --server.port=8503

# If you see "ModuleNotFoundError: No module named 'src'":
# - Make sure you're in research_notebooks/ directory
# - Use IRCA/ prefix in the command

# Install missing dependencies if needed
pip install reportlab langchain streamlit
```

**4. Environment Variable Issues**
```bash
# .env file must be in IRCA/ directory
# Verify file exists and has correct content:
ls -la IRCA/.env
cat IRCA/.env
```

**5. Port Conflicts**
```bash
# Kill existing processes
pkill -f "streamlit run"

# Run on different ports
streamlit run IRCA/streamlit_ui.py --server.port=8502
streamlit run IRCA/streamlit_ui_poc.py --server.port=8503
```

## 📚 API Reference

### Supported Remediation Actions
- `KILL_PROCESS` - Terminate running processes
- `QUARANTINE_FILE` - Isolate malicious files  
- `DELETE_REGISTRY_KEY` - Remove registry entries
- `ISOLATE_MACHINE` - Network isolation
- `UNQUARANTINE_FILE` - Restore quarantined files

### Data Collection Endpoints
- `/rest/detection/inbox` - Malop collection
- `/rest/detection/details` - Malop enrichment
- `/rest/crimes/unified` - EDR data
- `/rest/visualsearch/query/simple` - Process details

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make changes and test thoroughly
4. Submit a pull request with detailed description

## 📄 License

This project is proprietary to Cybereason Labs.

## 🆘 Support

For questions or issues:
- Contact the Data Science Team
- Check logs in `outputs/*/pipeline.log`