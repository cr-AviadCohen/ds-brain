# Project Assembly LLM.docx

**🏁 Main**

Project
Assembly LLM

# General

* **Description:**
  + Disassembling the executable into Assembly blocks, then into functions, and generating pseudocode for those functions.
  + Tagging each function with a description of its purpose (e.g., reading the *hosts file* or accessing cookie files).
  + Identifying security-related implementations, such as attack methods or capabilities.
  + Ultimately, using the function call flow to construct the **complete story** (הסיפור השלם) of the executable.
* **Owner:** Noa Perach Novogroder
* **Code:** <https://github.com/cybereason-labs/assembly-llm/tree/dev>
* **Jira:**
  + [ENG-3927: Assembly LLM | Architecture & Code Refactor](https://cybereason.atlassian.net/browse/ENG-3927?atlOrigin=eyJpIjoiZmQwYzU4ZGFkODRlNGUxN2I1Nzc4MmI4ZTFhZDUyNjMiLCJwIjoiaiJ9)
* [**NotebookLM**](https://notebooklm.google.com/notebook/f6aa29e5-616e-4f3a-9bcb-92748f456255)
* [**Architecture**](https://app.diagrams.net/?splash=0#G16U9p1Lu0BKq--hF3DGD-i0OpWYzyNhVZ#%7B%22pageId%22%3A%22Izcry1lMWkYkDwGesbCa%22%7D)
* [**#Slack Channel**](https://cybereason.enterprise.slack.com/archives/C09H4MRMBB2)
* **More:**
  + <http://ghidra.net/>

# Tasks

* Code:
  + Create a git repository under cybereason for the code in the format that Aviad provided.
  + Code architecture with classes.
  + Add samples for code analysis into data directory (will be used for testing)
* Work on a remote GPU machine
  + Connect to OCI Server: *ssh -i /Users/aviad.cohen/Downloads/oci\_gpu\_machine.key opc@161.153.18.227 -L 8888:localhost:8888*
  + Clone the git repository.
  + Install Ollama
    - ollama run gemma3n:e4b
  + Install Ghidra
  + Use HuggingFace Transformers package to work with Language Models locally. Use Cursor to write the integration.
* Work locally on Mac:
  + Apply LLM using [Ollama](https://python.langchain.com/docs/integrations/llms/ollama/)
  + Apply LLM using [LMStudio](https://lmstudio.ai/docs/python)
* Models:
  + [Google-gemma3-270m](https://medium.com/data-science-in-your-pocket/google-gemma3-270m-the-best-smallest-llm-for-everything-efcf927a74be) | [google/gemma-3n-e4b](https://huggingface.co/google/gemma-3n-E4B) | [unsloth/gemma-3-270m-it-GGUF](https://huggingface.co/unsloth/gemma-3-270m-it-GGUF)
  + [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b)
  + …

## Explorations

### Deep research on open-source LLMs for Code Analysis

**🤝 Meetings**

Meetings

# 2025.10.16

* [NotebookLM](https://notebooklm.google.com/notebook/f6aa29e5-616e-4f3a-9bcb-92748f456255)

The meeting focused on the progress, architecture, required organization, and deployment strategy for the **Assembly LLM project**.

### Project Architecture and Components

The discussion covered several key technical elements:

1. **Packing/Unpacking Capability:** A component related to **packing** was requested by Ophir. The speaker (Noa) confirmed she would implement this feature. This is critical because many malware samples utilize packing. While they acknowledged that packing is complex, with issues occurring only at runtime, the aim is to use known methods to add unpacking capability to the product. They will also attempt to add this capability for scripts, often involving **obfuscations** or various forms of compression.
2. **Ghidra Integration and Decomposition:** The unpacking process relies on using **Ghidra** to deconstruct (open and disassemble) the executable file.
   * Ghidra is treated as an **agent**. The system runs a script within the Ghidra environment (the agent) with the context of the executable.
   * The current implementation, while only handling one or two tasks, was designed to be **generic**. This allows users to request various outputs from Ghidra and generate the corresponding script to run **headlessly** inside Ghidra.
3. **Data Extraction and Processing:** Once Ghidra finishes execution, the resulting data is extracted.
   * The system can request items like all **functions and API calls**.
   * The extracted data is sent in the form of **C code**, which is then broken down and forwarded to other agents.
4. **Current Code Status:** The current code base contains the Ghidra integration, as well as a **splitter**, **prompts**, and a **writer/reporter** component. These components are already separated into different classes/modules. However, the **reporter** component is **not yet complete**.

### Project Organization and Refactoring

The male speaker (Aviad) emphasized the need to organize the code and improve standards:

* **Code Standard Improvement:** He noted issues in the current code and suggested improving the **code standard**. This can be easily achieved using **Cursor**.
* **Access and Organization:** He requested access to the Git repository to help organize the code base.
* **Standard Directory Structure:** They agreed on a required project structure:
  + A **README** file (which both parties noted had been started).
  + A **requirements** file.
  + An **.env** file (kept locally, not in Git) for tokens and configuration (like the Azure token).
  + An **SRC directory** containing the source code.
  + A **Utils directory** within SRC for external utilities (e.g., helpers for Ghidra).
  + A **VN (virtual environment)** (already created).
  + An **output directory** for results.
  + A **data directory** for file examples used in testing.

### Deployment and LLM Integration

They discussed how to integrate and run the LLM components:

* **Server Use:** They must use the **server** (for LLM Studio integration) as requested by Ophir until the male speaker receives a dedicated computer.
* **Git and Server Workflow:** The server workflow involves connecting to the server, performing a git clone initially, and then using git pull to fetch local changes made by the programmer.
* **Local Model Loading:** The male speaker will provide code to load models locally and run them on CUDA, but this functionality must be run **only on the server**.

### Repository Setup and Naming

* **Git Creation:** Since the female speaker was unsure if the project was in Git, they decided to create a **new repository**. The male speaker created the repository under "Data Science".
* **Collaborator Access:** The male speaker added the female speaker as a collaborator.
* **Immediate Git Tasks:** The immediate plan was for the male speaker to create the repo, send the link, add a README and a .gitignore. The male speaker would then zip the existing code and push it, organizing the directory structure.
* **Project Naming:** They acknowledged that the current name, **"Assembly LLM,"** was confusing and disliked by many people. They agreed to stick with it temporarily while the female speaker looked for a better name, potentially using ChatGPT.

*(Note: The discussion was constrained by time, as the female speaker had to leave by 10:30 AM (half past the hour), which prompted them to expedite the Git repository setup.)*

# 2025.09.30

* Attendees: Aviad Cohen, Noa Perach Novogroder
* Connect to OCI server
  + *ssh -i /Users/aviad.cohen/Downloads/oci\_gpu\_machine.key opc@161.153.18.227 -L 8888:localhost:8888*
  + Install Ollama
  + Install Ghidra

# 2025.09.25

* Attendees: Aviad Cohen, Noa Perach Novogroder
* [Meeting recordings](https://drive.google.com/drive/u/0/folders/1YjKxB2yVAABnlHZnd8yIm4EfftAJBQl4)
* [NotebookLM](https://notebooklm.google.com/notebook/f6aa29e5-616e-4f3a-9bcb-92748f456255)

The meeting between Aviad (Data Science Team Lead) and Noa (Security research team member) covered project structure, architecture, necessary tools, and team collaboration regarding the Assembly LLM project.

### Project Structure and Tools

* **Standardization:** Aviad provided guidance on adopting standard project structure. Noa agreed to implement this structure.
* **Directory Layout:** Structure should include directories for data (samples and outputs) and source code.
* **Configuration:** All configurations (API endpoints, API keys, etc.) should be stored in a separate configuration file (or as system variables).
* **Package Management (UV):** Aviad strongly recommended using **UV** (a package manager written in Rust, similar to pip/conda) to manage dependencies and versions, as it is fast and addresses dependency conflicts better than the older requirements.txt method.
* **Requirements:** Noa still needs to use a requirements file to specify the exact version and location of **Ghidra** for running it headless. The current project structure was messy because she initially had to run Ghidra directly until she figured out how to run it headless.
* **Code Organization:** Code should be structured using classes within the SRC folder, rather than scripts.
* **Documentation:** A structured **README.md** file is required to detail the project architecture, data flow, installation instructions (including UV usage), and how to start working.
* **Language Choice:** Python is deemed suitable for LLM projects, even in production, countering any concerns about needing to use C++.
* **UI/Reports:** Aviad suggested using **Cursor** (an AI tool) to write the README.md and generate professional PDF reports and UI elements (like graphs and flowcharts), referencing a successful example from a colleague.

### Architectural Discussion and Hydra Integration

* **Hydra Concerns:** Noa expressed concern and resistance regarding the integration of the Assembly LLM project under the existing **Hydra** architecture, viewing them as unrelated projects. She felt uncomfortable having her new work put under someone else’s umbrella.
* **Hydra Explanation:** Aviad explained that Hydra is a generic, multi-agent architecture designed to solve complex problems from different angles. He believes the Assembly LLM work easily fits under Hydra's architecture, potentially as another agent or branch.
* **Project Goal:** Noa emphasized that her goal is to allow the user to open the executable like an open book, functioning as a user interface (UI) for a reverser, not just summarizing assembly.
* **High-Level Flow:** The general process involves a PE input file, which undergoes decompilation via Ghidra, followed by function extraction, and ultimately results in a PDF output.

### Collaboration and Next Steps

* **Current Status:** The Assembly LLM project is currently a **POC (Proof of Concept)** and is scheduled to be presented soon to the Japanese team.
* **Action for Noa:** Noa will start reorganizing the code and structure immediately.
* **Collaboration:** Aviad requested to be added as a contributor to the Git repository so he can assist with structure changes via a separate branch.
* **Architecture Diagram:** They postponed creating a detailed architecture diagram (using Draw.io/Draw) until the next meeting, giving Noa time to prepare her own version.
* **Hardware:** Aviad advised Noa to request a Mac with 32GB of RAM.
* **Meeting Conclusion:** The meeting ended positively, with plans to meet again early the following week (Sunday or Monday) to review the reorganized project structure.

# 2025.09.21

* Attendees: Aviad Cohen, Noa Perach Novogroder
* [Meeting recordings](https://drive.google.com/drive/u/0/folders/1uQTUMJ4fkG3_AZ4lmXM8pw0sjPsHS1Ut)
* [NotebookLM](https://notebooklm.google.com/notebook/f6aa29e5-616e-4f3a-9bcb-92748f456255)

The meeting between Aviad and Noa focused on advancing the **Assembly LLM project** by identifying and testing suitable **local, open-source Large Language Models (LLMs)** to replace the current reliance on GPT-4/O for cost efficiency.

### Project Definition and Goals

The Assembly LLM project aims to analyze executables by:

1. Disassembling the executable into Assembly blocks, then into functions, and generating pseudocode for those functions.
2. Tagging each function with a description of its purpose (e.g., reading the hosts file or accessing cookie files).
3. Identifying security-related implementations, such as attack methods or capabilities, including recognizing techniques like traversing the **PB (Process Environment Block)** structure to resolve APIs.
4. Ultimately, using the function call flow to construct the **complete story** (הסיפור השלם) of the executable.

Noa noted that while the current process works (likely using GPT-4/O), they need to build or fine-tune their own model to save costs associated with querying a commercial API for every executable.

### LLM Testing and Tool Discussion

The core of the discussion involved Aviad demonstrating the performance of various local LLMs using the **LLM Studio** application, which provides a Graphical User Interface (GUI) for easily managing and testing open-source models.

**Models Tested:**

* **Gemma 3 (7 Billion Parameters):** This 4GB model (specifically the version published by 'Unstable') was highly favored due to its popularity and strong performance.
  + It provided a very detailed analysis of a complex C++ function, generating a lengthy, well-structured response in about 20 seconds.
  + Noa was significantly impressed that such performance was achieved locally and for free.
  + When prompted to analyze a snippet as a "malware analysis specialist," it successfully identified that the code used the **PB** (Process Environment Block) for API resolving.
* **Code Llama 7B Instruct:** This model was tested and provided a much shorter response compared to Gemma 3.
* **Open AI (Open Source, 20 Billion Parameters):** This larger, 11GB model also performed well, displaying **reasoning** capabilities by showing its thought process before generating the answer.
* **Failed Model Test:** An unnamed model failed because it was not **instruction-tuned** (instctt). Instead of analyzing the code, it attempted to continue the script.

Aviad also mentioned [**Ollama**](https://ollama.com/download), which works via the terminal and is better suited for API integration and server use compared to [**LLM Studio**](https://lmstudio.ai/).

### Hardware and Next Steps

The team recognized that running these models locally requires specific hardware.

**Action Items for Noa:**

* **Acquire Better Hardware:** Noa currently uses an older Intel i7 Windows machine, but needs a machine with a GPU. Aviad advised requesting a **MacBook Pro M1 (or Max) with 32GB RAM** to ensure adequate local performance.
* **Set up Tools:** Noa plans to download LLM Studio and start experimenting. She may consider using Ollama if API integration is required.

**Action Items for Aviad:**

* **Malware Specialist Model Research:** Aviad will use ChatGPT to perform deep research to find specialized, small language models (under 8B parameters) dedicated to **malware analysis** tasks, such as detecting malicious functions. The goal is potentially to use multiple "agents"—one for function analysis (like Gemma) and one for malware tagging.
* **Project Documentation:** Aviad created a Slack channel and a project document template for Assembly LLM to centralize all discussions, links, and findings.
* **Code Refactoring:** Aviad offered to help Noa transition the code to a modular structure using tools like LangChain, which would simplify swapping and experimenting with different LLMs.

**✅ Tasks**

Tasks

* Task 1
* Task 2

**Deep Research on Open-Source LLMs**

# <https://chatgpt.com/share/68cfe204-622c-8003-8a34-de09ff788f65>

# Transformer Models for C++ Malware Analysis

## Code Vulnerability Detection Models (C/C++ Focused)

* **mahdin70/codebert-devign-code-vulnerability-detector** – A fine-tuned version of Microsoft’s CodeBERT (RoBERTa-based, ~125M parameters ) for detecting vulnerabilities in C/C++ source code . It classifies a code snippet or function as **safe (0)** or **vulnerable (1)**, using the Devign (DetectVul) dataset for training . This encoder-based model supports static code analysis to flag potentially malicious or insecure functions, with example usage provided via the Hugging Face Transformers API .
* **mahdin70/graphcodebert-devign-code-vulnerability-detector** – A 125M-parameter GraphCodeBERT model (RoBERTa with code data-flow encoding) fine-tuned on the same C/C++ Devign vulnerability dataset . It performs binary classification of code functions as vulnerable vs. safe . The architecture considers code structure (data flow) to improve detection of unsafe C/C++ code patterns. Like the CodeBERT variant, it’s used for static analysis (e.g. CI pipelines or IDE plugins) to catch dangerous functions .
* **mahdin70/unixcoder-code-vulnerability-detector** – A model fine-tuned from Microsoft’s UniXcoder (a transformer-based code encoder-decoder) for C/C++ vulnerability detection . It has ~126M parameters and was trained on Devign, achieving ~68% accuracy (F1 ~62%) in classifying C/C++ functions as vulnerable or not . This open-source model (MIT-licensed) is similarly aimed at **malicious function detection** in source code, limited to C/C++ analysis and usable via the Hugging Face AutoModelForSequenceClassification interface (with the UniXcoder tokenizer) .
* **mahdin70/GraphCodeBERT-VulnCWE** – A GraphCodeBERT-based model (~125M params) fine-tuned for both vulnerability **detection** and **CWE classification** . It not only predicts if a code snippet is vulnerable, but also outputs the likely CWE ID (Common Weakness Enumeration) if a vulnerability is present . For example, it can identify an out-of-bounds memory write in C/C++ and label it as CWE-787 (Out-of-bounds Write) . This provides a form of **behavior prediction** by categorizing the type of security flaw. Usage involves obtaining two outputs – a binary vulnerability logit and a multi-class CWE logit – from the model’s forward pass.

## Large Language Models for Code Security Analysis

* **rootxhacker/CodeAstra-7B** – An **instruction-tuned** code *LLM* (7 billion parameters, Mistral-7B architecture) specializing in security analysis and vulnerability detection . Fine-tuned on a custom multi-language security dataset, CodeAstra-7B supports C/C++ along with many other languages (Go, Python, Java, etc.) . It achieves state-of-the-art performance (~83% accuracy on vulnerability detection) while substantially outperforming smaller code models like CodeBERT . As a generative model, it can be prompted to review raw C++ source code and explain or predict potentially malicious behavior in functions. For example, given a snippet it can enumerate security issues or dangerous calls (via natural language output). The model is open-source (Apache-2.0) and uses a **Transformer decoder** architecture with LoRA fine-tuning; it’s loaded with HuggingFace Transformers + PEFT as shown in its documentation .
* **whywhywhywhy/security-qwen2.5-3b-coder-instruct** – A smaller (≈3.1B parameters ) transformer **coder LLM** based on Alibaba’s Qwen2.5-Code model, fine-tuned for finding vulnerabilities in code. It was trained on the ReposVul dataset (6k+ real vulnerabilities) covering C, C++, Java, and Python, using Low-Rank Adaptation (LoRA) . This model is designed to assist in identifying security issues in source code – e.g. buffer overflows in C/C++ or unsafe functions – by either classifying code or generating an explanation. Being an instruct model, it can take a prompt like *“Analyze the following C++ function for malicious behavior or vulnerabilities”* and then output an analysis. It uses the Qwen 2.5 (3B) architecture (Transformer decoder) and is open-source (Apache-2.0 license) . Developers can load it via AutoModelForCausalLM and prompt it for code analysis tasks .

## Other Security-Focused Code Models

* **schirrmacher/malwi** – Although targeting Python rather than C++, *Malwi* is an open-source tool that showcases a transformer-based approach to malware *source code* detection . It uses a lightweight DistilBERT-derived model (~11.2M parameters , distilled from BERT) to scan code for malicious patterns. The pipeline compiles source code into an abstract syntax tree and **transpiles it to a “dummy bytecode”** annotated with security-relevant tokens (e.g. markers for file I/O, process execution) . This sequence is then fed into the pre-trained DistilBERT model (fine-tuned on a malware code dataset) to predict a maliciousness score . In practice, Malwi can flag suspicious functions and even enumerate their potential malicious behaviors (such as **process spawning, deserialization, or filesystem access**) in Python code . It demonstrates the viability of transformer models for static malware analysis in code. *(While Malwi currently supports Python/JavaScript, its methodology could be extended to C++ source with appropriate training data.)*

**Sources:** The information above is drawn from the models’ Hugging Face pages and documentation, including model cards and research papers (e.g. the *Zero Day Malware Detection with Alpha* approach that inspired Malwi ). Each model name links to its Hugging Face repository for further details and usage examples.
