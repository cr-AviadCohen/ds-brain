# Lunch & Learn 2／2026.pptx

<!-- Slide number: 1 -->

![](GoogleShape255p35.jpg)
# Lunch & Learn
MalOps Classification Using Machine Learning

### Notes:

<!-- Slide number: 2 -->

![Beautify this slide](GoogleShape261p36.jpg)

### Notes:

<!-- Slide number: 3 -->
# Samples         &            Features

![lot of different cats, and other objects - such as dogs, bats, mice, briefcase, table. no background. figures are not connected thematically or in any other way.](GoogleShape266p37.jpg)
Tail length
Whisker length
Number of legs
Made of wood
Has wings
Color

### Notes:

<!-- Slide number: 4 -->

![emphasis difference in classification of "cat" in deterministic programming vs. machine learning. use tabular data as input, not image. structure the deterministic approach as a conditional statement not as a decision tree.](GoogleShape273p38.jpg)

### Notes:

<!-- Slide number: 5 -->
# Problem: High FP ratio of suspicious MalOps
A MalOp (Malicious Operation) is a group of correlated security events that has been verified and classified as a genuine malicious threat
US
Europe
ASIA

![](GoogleShape283p39.jpg)

![](GoogleShape282p39.jpg)

![](GoogleShape281p39.jpg)
Total: 1,886 TP / 5,054 suspected MalOps = 0.37 precision = 0.63 FDR
‹#›

### Notes:

<!-- Slide number: 6 -->
# Machine Learning Approach

Feature extraction of suspected MalOps
Comparison of wide range of algorithms to distinguish between real MalOps and non malicious groups of events
Requirement: FDR (False Discovery Rate) less than 15%
Results were suboptimal as the TPR (sensitivity) was only about 30%

![](GoogleShape295p40.jpg)
‹#›

### Notes:

<!-- Slide number: 7 -->
# Poor distinction between populations

![](GoogleShape302p41.jpg)
‹#›

### Notes:

<!-- Slide number: 8 -->
# New approach:
Using model to omit obvious false MalOps

This approach seemed valuable, but required to decrease the %TP omitted in this method

![](GoogleShape311p42.jpg)
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

<!-- Slide number: 9 -->
# Root Cause Analysis of Model Performance with LLM
Prompt: i want to inquire why i have malicious samples that have probability of less than 0.2
Perfect! I've completed a comprehensive analysis of why you have malicious samples with probability less than 0.2. Let me summarize my findings and recommendations:
🚨 Key Findings from Your Current Model:
Based on your classifier results, you have 361 false negatives out of 527 total malicious samples in your test set, which means approximately 68.5% of malicious samples are being misclassified. Some of these are getting probabilities below 0.2, which are essentially being treated as very confident benign samples.

### Notes:

<!-- Slide number: 10 -->
# I Insisted
Prompt: all these statistics i already know, i'm interestd in the root cause.
1. ATTACK COMPLEXITY ANALYSIS:
2. TIME-BASED PATTERNS:
3. EVENT FREQUENCY PATTERNS:
4. RULES-TO-EVENTS RATIO:
5. COMPARING SIMPLE vs COMPLEX MALICIOUS SAMPLES:
New features:
Is_simple_attack: 1 rule, 1 tactic, less than 60s span
Is_instant_attack: span_time == 0
Is_single_rule: 1 rule
Severity_weighted_complexity: #rules*#tactics*severity_weights
High_confidence_simple_alert: 'TCP NULL flags Attack suspicion', 'Malware detection', 'Password Spray', 'Cryptomining')
Legitimate_instant_event: High_confidence_simple_alert & Is_instant_attack
Rule_efficiency: rules_events_ratio
Perfect_efficiency_simple: rules_events_ratio >= 0.8 & Is_simple_attack
=== THE FUNDAMENTAL PROBLEM ===
🎯 Your model was trained to distinguish between:
  • Complex multi-stage attacks (what we expect from "malicious")
  • Normal benign activity
🚨 SPECIFIC ISSUE:
The model learned that malicious = complex multi-stage attacks
But 943 samples are single-alert detections that are threats but have benign-like feature patterns!

### Notes:

<!-- Slide number: 11 -->

![Beautify this slide](GoogleShape333p45.jpg)

### Notes:

<!-- Slide number: 12 -->

![](GoogleShape338p46.jpg)

### Notes:

<!-- Slide number: 13 -->
# Better separation of populations

![](GoogleShape345p47.jpg)
‹#›

### Notes:

<!-- Slide number: 14 -->
# Better separation of populations

![](GoogleShape352p48.jpg)
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

<!-- Slide number: 15 -->
# Extensive research of feature selection and models tuning uncovered that SVM and KNN classifiers can be used to enrich features

![](GoogleShape359p49.jpg)

![](GoogleShape360p49.jpg)

### Notes:

<!-- Slide number: 16 -->
# Final Model

![](GoogleShape367p50.jpg)
‹#›

### Notes:

<!-- Slide number: 17 -->
# Baseline Vs Final Model

![](GoogleShape375p51.jpg)

![](GoogleShape374p51.jpg)
‹#›

### Notes:

<!-- Slide number: 18 -->
# False Positives Removal in the Final Model

![](GoogleShape382p52.jpg)
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

<!-- Slide number: 19 -->
# Prioritizing MalOps analysis with model

![](GoogleShape390p53.jpg)
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

<!-- Slide number: 20 -->
# Questions?

![](GoogleShape398p54.jpg)

### Notes:
