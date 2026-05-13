# Malop decision gateway - Sep.pptx

<!-- Slide number: 1 -->

![](GoogleShape254p34.jpg)
# XDR - MalOp
Decision gate
September 2025

### Notes:

<!-- Slide number: 2 -->
# Problem: High FP ratio of suspicious MalOps
US
Europe
ASIA

![](GoogleShape266p35.jpg)

![](GoogleShape265p35.jpg)

![](GoogleShape264p35.jpg)
Total: 1,886 TP / 5,054 suspected MalOps = 0.37 precision = 0.63 FDR
‹#›

### Notes:

<!-- Slide number: 3 -->
# Machine Learning Approach

Feature extraction of suspected MalOps
Comparison of wide range of algorithms to distinguish between real MalOps and non malicious groups of events
Requirement: FDR (False Discovery Rate) less than 15%
Results were suboptimal as the TPR was only about 30%

![](GoogleShape277p36.jpg)
‹#›

### Notes:

<!-- Slide number: 4 -->
# Poor distinction between populations

![](GoogleShape284p37.jpg)
‹#›

### Notes:

<!-- Slide number: 5 -->
# New approach:
Using model to omit obvious false MalOps

This approach seemed valuable, but required to decrease the %TP omitted in this method

![](GoogleShape293p38.jpg)
| Metric | Value |
| --- | --- |
| Total Samples | 1690 |
| Total False Positives (FP) | 1163 |
| Number of FP Cleaned | 820 |
| % FP Cleaned (of Total Samples) | 49% |
| % FP Cleaned (of Total FP) | 71% |
| % TP Ignored (of Total TP) | 7% |
‹#›

### Notes:

<!-- Slide number: 6 -->
# New features

A comprehensive inquiry, made in the assistance of an LLM revealed that model had troubles distinguishing between simple attacks and legitimate events, new features were generated in order to increase its ability to correctly classify the events.
2 more models were developed, one that separates simple and complex events (the ensemble model) and one was trained on all events (the single model).
|  | Model | KS\_Statistic | Recall | Precision | Low\_Prob\_Malicious | Low\_Prob\_Percentage |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Enhanced Ensemble | 0.612 | 0.239 | 0.851 | 41 | 7.780 |
| 1 | Enhanced Single | 0.626 | 0.271 | 0.851 | 13 | 2.467 |
| 2 | Original | 0.646 | 0.395 | 0.852 | 39 | 7.400 |
‹#›

### Notes:

<!-- Slide number: 7 -->
# Comprehensive Inquiry
Prompt: i want to inquire why i have malicious samples that have probability of less than 0.2
💡 Why Your Model Fails on These:
The Fundamental Issue:
Your model learned: "Malicious = Complex Multi-Stage Attacks"
But 52.4% of your malicious samples are single-alert detections
To the classifier, these look like:
False positive alerts (single rule fired)
Noise/low-confidence detections
Isolated events (not attack campaigns)

### Notes:

<!-- Slide number: 8 -->
# Add more features to target and differentiate simple attacks

New features:
Is_simple: 1 rule, 1 tactic, less than 60s span
Is_instant: span_time == 0
Is_single_rule: 1 rule
Severity_weighted_complexity: #rules*#tactics*severity_weights
High_confidence_simple_alert: 'TCP NULL flags Attack suspicion', 'Malware detection', 'Password Spray', 'Cryptomining')
instant_event: High_confidence_simple_alert & Is_instant_attack
Rule_efficiency: rules_events_ratio
Perfect_efficiency_simple: rules_events_ratio >= 0.8 & Is_simple_attack
Ensemble use separate models for simple and complex attacks
|  | Model | KS\_Statistic | Recall | Precision | Low\_Prob\_Malicious | Low\_Prob\_Percentage |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Enhanced Ensemble | 0.612 | 0.239 | 0.851 | 41 | 7.780 |
| 1 | Enhanced Single | 0.626 | 0.271 | 0.851 | 13 | 2.467 |
| 2 | Original | 0.646 | 0.395 | 0.852 | 39 | 7.400 |

### Notes:

<!-- Slide number: 9 -->
# Better separation of populations

![](GoogleShape322p42.jpg)
‹#›

### Notes:

<!-- Slide number: 10 -->
# Better separation of populations

![](GoogleShape329p43.jpg)
‹#›

### Notes:

<!-- Slide number: 11 -->
# Better separation of populations

![](GoogleShape336p44.jpg)
| Metric | Baseline | Enhanced single |
| --- | --- | --- |
| Total Samples | 1690 | 1690 |
| Total False Positives (FP) | 1163 | 1163 |
| Number of FP Cleaned | 781 | 554 |
| Number of TP Ignored | 39 | 13 |
| % FP Cleaned (of Total Samples) | 46% | 33% |
| % FP Cleaned (of Total FP) | 67% | 48% |
| % TP Ignored (of Total TP) | 7% | 2% |
‹#›

### Notes:

<!-- Slide number: 12 -->
# Extensive research of feature selection and models tuning uncovered that SVM and KNN classifiers can be used to enrich features

![](GoogleShape343p45.jpg)

![](GoogleShape344p45.jpg)

### Notes:

<!-- Slide number: 13 -->
# Final Model

![](GoogleShape351p46.jpg)
‹#›

### Notes:

<!-- Slide number: 14 -->
# Baseline Vs Final Model

![](GoogleShape359p47.jpg)

![](GoogleShape358p47.jpg)
‹#›

### Notes:

<!-- Slide number: 15 -->
# Prioritizing MalOps analysis with model

![](GoogleShape366p48.jpg)
| Metric | Value |
| --- | --- |
| Total Samples | 1690 |
| Total True Positives (TP) | 527 |
| Number of TP Marked | 264 |
| Number of FP Marked | 83 |
| % TP Marked (of Total TP) | 50% |
| % TP Marked (of Total Marked Samples) | 76% |
| % FP Marked (of Total Marked Samples) | 24% |
‹#›

### Notes:

<!-- Slide number: 16 -->
# False Positives Removal in the Final Model

![](GoogleShape374p49.jpg)
| Metric | Final model | Baseline |
| --- | --- | --- |
| Total Samples | 1690 | 1690 |
| Total False Positives (FP) | 1163 | 1163 |
| Number of FP Cleaned | 549 | 781 |
| Number of TP Ignored | 11 | 39 |
| % FP Cleaned (of Total Samples) | 32% | 46% |
| % FP Cleaned (of Total FP) | 47% | 67% |
| % TP Ignored (of Total TP) | 2% | 7% |
‹#›

### Notes:
