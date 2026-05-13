# Pretrained Models Results.docx

Pre-trained Models Evaluation Results

| **Model name** | **prompt** | **results** |
| --- | --- | --- |
| meta-llama/Llama-3.2-1B-Instruct | prompt = (  "Classify the following PowerShell script as 'malicious' or 'benign'. "  "Respond with only one word: malicious or benign.\n\n"  f"Script:\n{example['text']}\n\nClassification:"  ) | ![](data:image/png;base64...) |
| teknium/OpenHermes-2.5-Mistral-7B  #(Quantized to ~1B with LoRA/QLoRA) | prompt = (  "Classify the following PowerShell script as 'malicious' or 'benign'. "  "Respond with only one word: malicious or benign.\n\n"  f"Script:\n{example['text']}\n\nClassification:"  ) |  |
| tiiuae/falcon-rw-1b |  |  |
