# Command Line Classification.pptx

<!-- Slide number: 1 -->
# Command Line Classification
Aviad Cohen, Ph.D.Data Science Team
Slack channel: cmd_classification

### Notes:

<!-- Slide number: 2 -->
# Title
TEXT…
bullet1
bullet2
‹#›

### Notes:
Integrating AI into our cybersecurity operations significantly enhances the capabilities of SOC analysts by automating routine tasks such as threat detection, log analysis, and incident triage. This not only reduces response time and human error but also lowers operational costs by minimizing the need for large manual teams. AI-driven tools offer real-time insights and pattern recognition that accelerate decision-making, while intuitive, user-friendly interfaces simplify complex processes, enabling even less-experienced analysts to act effectively. Ultimately, AI transforms the SOC into a more efficient, cost-effective, and agile environment capable of keeping pace with today’s evolving threat landscape.

<!-- Slide number: 3 -->
# Problem Domain
Modern cyberattacks increasingly leverage command-line interfaces (CLI) for stealthy operations, often bypassing traditional security solutions.
Attackers use obfuscated, encoded, and multi-stage CLI commands to evade detection, making static rule-based approaches insufficient.
Early and accurate CLI classification accelerates incident investigations, reduces response time, and improves threat containment.

![HD wallpaper: problem, solution, decision, think, choose ...](GoogleShape90p18.jpg)

### Notes:

<!-- Slide number: 4 -->
# Project Goal
Classifying process command lines as Benign / Malicious, at end-point machine, using ML/AI.
It is considered a difficult task, as the command line itself can be malicious OR NOT, depends on context, which is not always available.

![3d White people with dart and target. Success in business. (Provided by Getty Images)](GoogleShape97p19.jpg)

### Notes:

<!-- Slide number: 5 -->
# Intro
Literature review
Found few articles related to this topic:
Command-line Risk Classification using Transformer-based Neural Architectures (2024)
Detection of Malicious Remote Shell Sessions (2019)
Detecting Malicious PowerShell Commands using Deep Neural Networks (2018)
Obfuscated Command Line Detection Using Machine Learning (2018)
Deep Research using various AI tools:
GenSpark, ChatGPT, Gemini, Grok.

![Stack of books,reading,literature,education,library,home office concept, large copy space (Provided by Getty Images)](GoogleShape103p20.jpg)

### Notes:

<!-- Slide number: 6 -->
# Types of Command Lines
Process command lines: commands used to initiate a new process. currently collected from customers.
Interactive shell command: executed via terminal (cmd / powershell / Bash)currently NOT collected

![Program console solid icon. Application command input window symbol, glyph style pictogram on white background. Browser item sign for mobile concept and web design. Vector graphics. (Provided by Getty Images)](GoogleShape111p21.jpg)

### Notes:

<!-- Slide number: 7 -->
# Command Line Interface (CLI) by OS
Microsoft Windows: CMD / Powershell. To begin with..
MacOS: Terminal. Most beneficial for the product

![Program console solid icon. Application command input window symbol, glyph style pictogram on white background. Browser item sign for mobile concept and web design. Vector graphics. (Provided by Getty Images)](GoogleShape118p22.jpg)

### Notes:

<!-- Slide number: 8 -->
# Example of Commands
Microsoft Windows: CMD / Powershell. To begin with..
MacOS: Terminal. Most beneficial for the product

![Program console solid icon. Application command input window symbol, glyph style pictogram on white background. Browser item sign for mobile concept and web design. Vector graphics. (Provided by Getty Images)](GoogleShape125p23.jpg)

### Notes:

<!-- Slide number: 9 -->
# Data Collection
GitHub: Malicious Powershell Scripts
VirusTotal: Malicious *.bat files | Filtered ~9,500 unique commands (LINK)
Customers:
Observe
Transparency
Production environment
DI – Elasticsearch
Production environment
Contains both benign & malop
F5 UI:
Customers production UI
Google BigQuery
~95,000 unique commands only from 17-3-2025, malops (LINK)
** Context is not always available.

![the database is an icon vector. Isolated contour symbol illustration (Provided by Getty Images)](GoogleShape132p24.jpg)

### Notes:

<!-- Slide number: 10 -->
# Example of CLI Commands
…

![the database is an icon vector. Isolated contour symbol illustration (Provided by Getty Images)](GoogleShape139p25.jpg)

### Notes:

<!-- Slide number: 11 -->
# Challenges
Obtaining enough data of Malicious * Benign samples for training.
Labeling
In order to train a ML classifier, we must have a verified labeled dataset of both benign and malicious.
Even Malop records are not 100% malicious.
Maliciousness is depend on context, which is not always available.

![Business challenge Businessmen use ladders to climb over gaps (Provided by Getty Images)](GoogleShape147p26.jpg)

![Businessman pushing boulder up to hill and hard work challenge. Concept illustration vector. (Provided by Getty Images)](GoogleShape146p26.jpg)

### Notes:

<!-- Slide number: 12 -->
# Utilizing OpenAI GPT4o to label commands
In order to label large amount of samples, we utilized OpenAI’s most advanced LLM, the GPT4o. We asked the model to provide:
Malicious ness score
Short explanation – why the command got the particular score
Detailed explanation
Prompt:

![](GoogleShape154p27.jpg)

### Notes:

<!-- Slide number: 13 -->
# Command lines from VirusTotal – label by LLM Maliciousness Score Distribution

![](GoogleShape160p28.jpg)

### Notes:

<!-- Slide number: 14 -->
# Utilizing Sigma Rules to label commands
Conducted by Security Research Team…

### Notes:

<!-- Slide number: 15 -->
# Feature Engineering
Deep Research using various AI tools: GenSpark, ChatGPT, Gemini, Grok.
Feature Extraction in Python with detailed YAML configuration file
Exploratory Analysis of the dataset
Removing bad features (zero variance), duplicates
Rank the features
Some informative charts

### Notes:

<!-- Slide number: 16 -->
# Feature Correlation Heat-Map (VirusTotal)

![](GoogleShape180p31.jpg)

### Notes:

<!-- Slide number: 17 -->
# Feature Correlation Heat-Map (GBQ)

![](GoogleShape186p32.jpg)

### Notes:

<!-- Slide number: 18 -->
# Feature Importance: InfoGain (VirusTotal)

![](GoogleShape192p33.jpg)

### Notes:

<!-- Slide number: 19 -->
# Feature Importance: InfoGain (GBQ)

![](GoogleShape198p34.jpg)

### Notes:

<!-- Slide number: 20 -->
# T-SNE (VirusTotal)

![](GoogleShape204p35.jpg)

### Notes:

<!-- Slide number: 21 -->
# T-SNE (GBQ)

![](GoogleShape210p36.jpg)

### Notes:

<!-- Slide number: 22 -->
# Solution
Not yet chosen
Classic ML-based model
LLM-based:
LLM / Fine-Tuned LLM
RAG

### Notes:

<!-- Slide number: 23 -->
# ML Experiment (VirusTotal)

![](GoogleShape222p38.jpg)

### Notes:

<!-- Slide number: 24 -->
# ML Experiment (GBQ)

![](GoogleShape228p39.jpg)

### Notes:

<!-- Slide number: 25 -->
# Classifiers Best Threshold (VirusTotal)

![](GoogleShape234p40.jpg)

### Notes:

<!-- Slide number: 26 -->
# Classifiers Best Threshold (GBQ)

![](GoogleShape240p41.jpg)

![](GoogleShape241p41.jpg)

### Notes:

<!-- Slide number: 27 -->
# Best Classifier TPR, FPR, IDR (TPR*TNR) (VirusTotal)

![](GoogleShape247p42.jpg)

### Notes:

<!-- Slide number: 28 -->
# Best Classifier TPR, FPR, IDR (TPR*TNR) (GBQ)

![](GoogleShape253p43.jpg)

### Notes:

<!-- Slide number: 29 -->

### Notes:
