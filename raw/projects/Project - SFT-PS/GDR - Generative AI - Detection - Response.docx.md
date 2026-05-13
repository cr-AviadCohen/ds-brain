# GDR - Generative AI - Detection - Response.docx

PowerShell classification+code analisys+remediatio

**Tasks – PowerShell Classification finetuning**

implementation steps:

* **Collection Acquisition:**
  + Benign:
    - Download Benign Powershell scripts from VirusTotal
    - <https://github.com/das-lab/mpsd/tree/main/powershell_benign_dataset>
  + Malicious:
    - Download Malicious Powershell scripts from VirusTotal
    - <https://github.com/das-lab/mpsd/tree/main/malicious_pure>
    - <https://github.com/Fa2y/Malicious-PowerShell-Dataset/tree/main/malicious_samples>
* **Label Dataset:**
  + Tag the dataset using GPT4o.
* **Dataset Creation:**
  + Create a JSON dataset for model experiments and Fine-Tuning.
  + Split the dataset into Training & Evaluation
* **Initial Experiment:**
  + Search for the most suitable LLM models for this task.
  + [PARALLEL] Apply various suitable LLMs on the dataset.
  + Compare the detection results of all models: *TPR,FPR*
* **Supervised Fine-Tuning:**
  + Search for the most suitable models for SFT on this task.
  + [PARALLEL] Develop an SFT (Supervised Fine-Tuning) script for each of the chosen LLMs. Train the model to a satisfactory level.
  + Compare the detection results of all models: *TPR,FPR*

hybrid llm solution #1

question #1:

product wize, do we want all powershells runing in the memory (or any other GDR project) to get code-analysis and remediation? will even benign be sent as requests?

assuming only malicious ones (makes more sense),

hybrid solution suggestion:

1. powershell scripts classification using a fine-tuned llm, served on our resources

costs will be training the model on a strong machine resource (OCI has the relevant machines, already paying them).

model options are tiny-bert / lamma / phi-2 / mistral,

* tiny-bert -

very small, least strong open source model metrics:

(on a 50-50 malicious benign dataset!? - we’ll see better results when testing on real world numbers)

FPR (benign classified as malicious): ±0.1

TPR (recall, malicious classified as malicious): ±0.87

TNR (benign classified as benign): ±0.91

precision: ±0.9

1. then, only powershells classified as malicious (1%-5%), are sent to a higher complexity model (gpt / gemini / claude),

for classification (verification- we already assume the powershell is malicious),

code-analysis,

and remediation steps suggestions

1. only powershells that were classified as malicious also by gpt will trigger an alert, showcase the code analysis and remediation steps.

this solution will ensure:

* lowest FPR possible, calling 2 different models on malicious suspects.
* a high quality analysis, as the large models are way better at reasoning then any open source model (even if fine tuned).
* relatively low costs, as 95%-99% of the powershells will be sent to an internal resource
