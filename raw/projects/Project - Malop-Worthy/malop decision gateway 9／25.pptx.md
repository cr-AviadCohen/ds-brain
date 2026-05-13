# malop decision gateway 9／25.pptx

<!-- Slide number: 1 -->
#

### Notes:

<!-- Slide number: 2 -->
# 1_year_classifier_round4.ipynb

🎯 Target Variable Analysis:
========================================
Label distribution:
False    3877
True     1756
Name: label, dtype: int64

Class balance:
Benign (False): 68.8%
Malicious (True): 31.2%

![](GoogleShape62p14.jpg)

### Notes:

<!-- Slide number: 3 -->
# Define classifiers to test
classifiers = {
    'Random Forest': RandomForestClassifier(random_state=42, n_jobs=-1),
    'Gradient Boosting': GradientBoostingClassifier(random_state=42),
    'Extra Trees': ExtraTreesClassifier(random_state=42, n_jobs=-1),
    'Logistic Regression': LogisticRegression(random_state=42, max_iter=1000),
    'SVM': SVC(random_state=42, probability=True),
    'AdaBoost': AdaBoostClassifier(random_state=42),
    'Decision Tree': DecisionTreeClassifier(random_state=42),
    'KNN': KNeighborsClassifier(),
    'Naive Bayes': GaussianNB(),
    'Linear Discriminant Analysis': LinearDiscriminantAnalysis()
}

# Define hyperparameter grids for tuning
# Custom scoring function for recall optimization with precision constraint
def recall_with_precision_constraint(y_true, y_pred_proba, min_precision=0.85):
    """
    Calculate maximum recall while maintaining minimum precision threshold.
    Returns 0 if no threshold achieves the minimum precision.
    """
🏆 BEST MODEL: Extra Trees
   Recall: 0.3150
   Precision: 0.8513

### Notes:

<!-- Slide number: 4 -->
# 1_year_classifier_round4_clean.ipynb
drop all geolocation features
🏆 BEST MODEL: reduced_features
   Recall: 0.3947
   Precision: 0.8525
(yes, better)

### Notes:

<!-- Slide number: 5 -->
#

![](GoogleShape81p17.jpg)

### Notes:

<!-- Slide number: 6 -->
#

![](GoogleShape88p18.jpg)

| Metric | Value |
| --- | --- |
| Total Samples | 1690 |
| Total False Positives (FP) | 1163 |
| Number of FP Cleaned | 781 |
| Number of TP Ignored | 39 |
| % FP Cleaned (of Total Samples) | 46% |
| % FP Cleaned (of Total FP) | 67% |
| % TP Ignored (of Total TP) | 7% |

### Notes:

<!-- Slide number: 7 -->
#

![](GoogleShape97p19.jpg)

|  | Metric | Value |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total True Positives (TP) | 527 |
| 2 | Number of TP Marked | 268 |
| 3 | % TP Marked (of Total TP) | 51% |
| 4 | % TP Marked (of Total Marked Samples) | 78% |
| 5 | % FP Marked (of Total Marked Samples) | 22% |

### Notes:

<!-- Slide number: 8 -->
# 📋 Oversampled models summary:

|  | precision | recall | f1\_score | accuracy | auc\_roc | threshold |
| --- | --- | --- | --- | --- | --- | --- |
| reduced\_features\_ROS\_1to1 | 0.850202 | 0.398482 | 0.542636 | 0.790533 | 0.889476 | 0.769113 |
| reduced\_features\_SMOTE\_1to2 | 0.850877 | 0.368121 | 0.513907 | 0.78284 | 0.890293 | 0.670087 |
| reduced\_features\_ROS\_1to2 | 0.851351 | 0.358634 | 0.504673 | 0.780473 | 0.891665 | 0.669445 |
| reduced\_features\_ROS\_2to1 | 0.85 | 0.290323 | 0.432815 | 0.762722 | 0.889542 | 0.879596 |
| reduced\_features\_SMOTE\_1to1 | 0.85 | 0.290323 | 0.432815 | 0.762722 | 0.890253 | 0.810005 |
| reduced\_features\_SMOTE\_2to1 | 0.850299 | 0.26945 | 0.409222 | 0.757396 | 0.886691 | 0.8824 |

### Notes:

<!-- Slide number: 9 -->
#

|  | Metric | Reduced features | ROS 1:1 |
| --- | --- | --- | --- |
| 0 | Total Samples | 1690 | 1690 |
| 1 | Total False Positives (FP) | 1163 | 1163 |
| 2 | Number of FP Cleaned | 820 | 662 |
| 3 | % FP Cleaned (of Total Samples) | 49% | 39% |
| 4 | % FP Cleaned (of Total FP) | 71% | 57% |
| 5 | % TP Ignored (of Total TP) | 7% | 4% |

### Notes:

<!-- Slide number: 10 -->
#
Prompt: i want to inquire why i have malicious samples that have probability of less than 0.2
Perfect! I've completed a comprehensive analysis of why you have malicious samples with probability less than 0.2. Let me summarize my findings and recommendations:
🚨 Key Findings from Your Current Model:
Based on your classifier results, you have 361 false negatives out of 527 total malicious samples in your test set, which means approximately 68.5% of malicious samples are being misclassified. Some of these are getting probabilities below 0.2, which are essentially being treated as very confident benign samples.

### Notes:

<!-- Slide number: 11 -->
#
Prompt: all these statistics i already know, i'm interestd in the root cause.
Malicious samples by number of tactics:
 1 tactic(s): 523 samples (99.2%)
 2 tactic(s): 4 samples (0.8%)

2. TIME-BASED PATTERNS:
Span time = 0 (instant): 247 (46.9%)
Span time <= 60s: 312 (59.2%)
Span time <= 1hr: 358 (67.9%)

3. EVENT FREQUENCY PATTERNS:
Very low event frequency (<=0.01): 111 (21.1%)

4. RULES-TO-EVENTS RATIO:
Perfect rules_events_ratio (1.0): 0 (0.0%)

5. COMPARING SIMPLE vs COMPLEX MALICIOUS SAMPLES:
Simple attacks (1 rule, 1 tactic, <=60s): 276 (52.4%)
Complex attacks (>=3 rules OR >=2 tactics OR >1hr): 173 (32.8%)
=== ROOT CAUSE ANALYSIS: LOW-PROBABILITY MALICIOUS SAMPLES ===
Malicious test samples: 527

1. ATTACK COMPLEXITY ANALYSIS:
Malicious samples by number of rules:
 1 rule(s): 370 samples (70.2%)
 2 rule(s): 140 samples (26.6%)
 3 rule(s): 8 samples (1.5%)
 4 rule(s): 4 samples (0.8%)
 5 rule(s): 1 samples (0.2%)
 7 rule(s): 1 samples (0.2%)
 43 rule(s): 1 samples (0.2%)
 50 rule(s): 1 samples (0.2%)
 52 rule(s): 1 samples (0.2%)

### Notes:

<!-- Slide number: 12 -->
Top Alert Types in Simple Attacks:
1. TCP NULL flags Attack suspicion: 393 (38.0%)
2. Malware detection: 149 (14.4%)
3. Password Spray: 127 (12.3%)
4. Azure AD Audit: User Modified 2FA: 62 (6.0%)
5. Sideloaded App(s): 48 (4.6%)
6. Manual Envelope Rejection: 16 (1.5%)
7. Cryptomining: 14 (1.4%)
8. Azure AD Audit: Brute-force from 'Agressive IP known malicious on AbuseIPDB': 12 (1.2%)
9. Azure AD Audit: Update policy: 11 (1.1%)
10. Unfamiliar sign-in properties: 10 (1.0%)
11. Azure AD Audit: Login after Brute Force on User Account from Multiple IP - ALLOW: 9 (0.9%)
12. AWS CloudTrail: RevokeSecurityGroupIngress: 8 (0.8%)
13. SharePoint: Mass Folder Delete: 8 (0.8%)
14. SharePoint: Object Shared with Guest: 7 (0.7%)
15. Outbound vertical port scan: 7 (0.7%)
=== ROOT CAUSE IDENTIFIED ===
🚨 276 out of 527 malicious samples (52.4%) are SIMPLE ATTACKS:
  • Single rule detection
  • Single tactic
  • Duration ≤ 60 seconds
  • These look like benign false positives to the model!

=== WHAT TYPES OF SIMPLE ATTACKS GET LOW PROBABILITIES? ===
Found 1035 raw alerts for simple attacks

Severity Distribution in Simple Attacks:
   HIGH: 406 (39.2%)
   MEDIUM: 374 (36.1%)

=== THE FUNDAMENTAL PROBLEM ===
🎯 Your model was trained to distinguish between:
  • Complex multi-stage attacks (what we expect from "malicious")
  • Normal benign activity

🚨 But 276 malicious samples are actually:
  • Single-alert incidents
  • Instantaneous events
  • Look exactly like false positives or low-confidence alerts

💡 These simple attacks have the SAME FEATURE PROFILE as benign noise!

### Notes:

<!-- Slide number: 13 -->
#

🚨 SPECIFIC ISSUE:
The model learned that malicious = complex multi-stage attacks
But 943 samples are single-alert detections that:
  1. TCP NULL flags Attack (38%) - Network anomaly detection
  2. Malware detection (14%) - AV hits
  3. Password Spray (12%) - Authentication attacks
  4. Azure AD changes (6%) - Single policy modifications

These are LEGITIMATE threats but have benign-like feature patterns!

💡 WHY PROBABILITIES < 0.2:
To the model, these samples look like:
  • False positive alerts (single rule fired)
  • Noise/low-confidence detections
  • Isolated events (not attack campaigns)
  • Same statistical profile as benign activity

### Notes:

<!-- Slide number: 14 -->
🎯 ROOT CAUSE IDENTIFIED - FINAL RESULTS
📊 The Problem Scale:
276 out of 527 malicious samples (52.4%) are "simple attacks" that get low probabilities
These represent legitimate threats but have benign-like feature patterns
🔍 Root Cause - Feature Pattern Analysis:
Simple Malicious Attacks vs Benign Samples are nearly IDENTICAL:
Number of rules: Simple Malicious = 1.0, Benign = 1.21
Number of tactics: Simple Malicious = 1.0, Benign = 1.01
Span time: Simple Malicious ≈ 0 seconds, Benign ≈ 1,452,823 seconds
Attack duration: 59.2% of malicious samples last ≤60 seconds
🚨 What's Getting Low Probabilities (<0.2):
Top Alert Types in Simple Attacks:
TCP NULL flags Attack (38%) - Network anomaly detection
Malware detection (14%) - Antivirus hits
Password Spray (12%) - Authentication attacks
Azure AD Audit: User Modified 2FA (6%) - Policy changes
Sideloaded App(s) (5%) - Application security

#

### Notes:

<!-- Slide number: 15 -->
💡 Why Your Model Fails on These:
The Fundamental Issue:
Your model learned: "Malicious = Complex Multi-Stage Attacks"
But 52.4% of your malicious samples are single-alert detections
To the classifier, these look like:
False positive alerts (single rule fired)
Noise/low-confidence detections
Isolated events (not attack campaigns)
🎯 ACTIONABLE SOLUTIONS:
1. Immediate Fix - Feature Engineering:
Add alert-type specific features (TCP flags, malware family, auth patterns)
Create severity-weighted features (HIGH/MEDIUM severity boost)
Add alert reputation scores based on historical true positive rates
2. Data Strategy:
Separate models for simple vs complex attacks
Alert-type specific thresholds
Ensemble approach: One model for campaigns, one for single alerts
3. Training Improvements:
Cost-sensitive learning - penalize missing these simple attacks more heavily
Stratified sampling - ensure simple attacks are well-represented
SMOTE focused on underrepresented simple attack patterns
The core issue is your ground truth labels don't match your feature engineering - you're trying to distinguish complex campaigns from benign activity, but half your "malicious" samples are isolated security events that legitimately look benign in aggregate statistics! 🔥

Would you like me to implement any of these specific solutions? 🚀
#

yes, try to solve that

### Notes:

<!-- Slide number: 16 -->
# improved_classifier_solution_nogeo.ipynb

New features:
Is_simple_attack: 1 rule, 1 tactic, less than 60s span
Is_instant_attack: span_time == 0
Is_single_rule: 1 rule
Severity_weighted_complexity: #rules*#tactics*severity_weights
High_confidence_simple_alert: 'TCP NULL flags Attack suspicion', 'Malware detection', 'Password Spray', 'Cryptomining')
Legitimate_instant_event: High_confidence_simple_alert & Is_instant_attack
Rule_efficiency: rules_events_ratio
Perfect_efficiency_simple: rules_events_ratio >= 0.8 & Is_simple_attack

Ensemble use separate models for simple and complex attacks
|  | Model | KS\_Statistic | Recall | Precision | Low\_Prob\_Malicious | Low\_Prob\_Percentage |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | Enhanced Ensemble | 0.612 | 0.239 | 0.851 | 41 | 7.780 |
| 1 | Enhanced Single | 0.626 | 0.271 | 0.851 | 13 | 2.467 |
| 2 | Original | 0.646 | 0.395 | 0.852 | 39 | 7.400 |

### Notes:

<!-- Slide number: 17 -->
# Prompt: explain high_confidence_simple_alert and legitimate_instant_event

⚡ legitimate_instant_event
Purpose:
Identifies legitimate malicious events that happen instantly but are high-confidence.

Key insight:
Solves the "instant = benign" bias problem:
❌ Traditional thinking: Instant events are likely false positives
✅ Enhanced thinking: Instant malware detection is still malware!

🚨 high_confidence_simple_alert
Purpose:
Identifies alerts that are inherently suspicious even when they appear simple/fast.

Key insight:
Some alert types are always suspicious regardless of timing/complexity:
If you see "Malware detection" → Immediately suspicious! ⚠️
Even if it's just 1 rule, 1 tactic, instant timing
Traditional models might undervalue these due to simplicity

Better name would be: instant_high_confidence_threat or legitimate_instant_malware

Solution approach:
high_confidence_simple_alert: "Some alert types are ALWAYS suspicious"
legitimate_instant_event: "Instant high-confidence alerts are ESPECIALLY suspicious"

### Notes:

<!-- Slide number: 18 -->
# The Irony

![](GoogleShape180p30.jpg)

![](GoogleShape181p30.jpg)

### Notes:

<!-- Slide number: 19 -->
#

![](GoogleShape188p31.jpg)

![](GoogleShape189p31.jpg)

### Notes:

<!-- Slide number: 20 -->
#

![](GoogleShape196p32.jpg)

### Notes:

<!-- Slide number: 21 -->
#

![](GoogleShape203p33.jpg)
| Metric | Baseline | Enhanced single |
| --- | --- | --- |
| Total Samples | 1690 | 1690 |
| Total False Positives (FP) | 1163 | 1163 |
| Number of FP Cleaned | 781 | 554 |
| Number of TP Ignored | 39 | 13 |
| % FP Cleaned (of Total Samples) | 46% | 33% |
| % FP Cleaned (of Total FP) | 67% | 48% |
| % TP Ignored (of Total TP) | 7% | 2% |

### Notes:

<!-- Slide number: 22 -->
# Feature generation
Implement high confidence attacks with this prompt:
are there more high confidence attacks (alert_name) to add to high_confidence_simple_alerts?

Then, explicitly inject list of attacks:
use this as the list of attacks:
array(["

As a result, 2 lists of alerts:
high_confidence_simple_alerts
high_suspicious_simple_alerts

### Notes:

<!-- Slide number: 23 -->
#
Prompt: make a new notebook 1_year_classifier_round5 in which you will try hyperparameter tuning for binary classifiers in order to classify malops_05_2024_06_2025_round5.parquet the metrics is ks value and you will present visualizations like plot_model_distributions_and_stats i want to check also feature selection in the process and perhaps an ensemble of several different classifiers. the ultimate goal is high recall where precision >= 0.85 otherwise i want to get as less malicious samples when prediction probability <= 0.2

![](GoogleShape217p35.jpg)

### Notes:

<!-- Slide number: 24 -->
# 1_year_classifier_round5_grid.ipynb
📊 FEATURE SELECTION SUMMARY:
============================================================
• Full: 206 features - All original features
• Correlation: 179 features - Eliminated 27 highly correlated features
• L1_Lasso: 126 features - L1 regularization selected 126 features
• TreeImportance: 144 features - Random Forest selected top 144 important features
• MutualInfo: 100 features - Mutual information selected top 100 features
• PCA: 104 features - PCA reduced to 104 components (95.1% variance)
• omit_suspicious_alerts: 204 features - Omit high suspicious alerts (only high confidence alerts)
• Previous: 205 features - Previous feature engineer

✅ FEATURE SELECTION METHODS READY!
   • 8 different feature sets prepared
   • Each classifier will be trained on all feature sets
============================================================

### Notes:

<!-- Slide number: 25 -->
# Best models by precision, low probability malicious, KS/recall
| Model Type | Feature Method | #Features | KS Statistic | Threshold | Recall | Precision | Low Prob Malicious | Low Prob Percentage |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SVM | Full | 206 | 0.626 | 0.745 | 0.002 | 1.000 | 66 | 12.524 |
| ExtraTrees | PCA | 104 | 0.617 | 0.739 | 0.290 | 0.850 | 6 | 1.139 |
| ExtraTrees | Tree Importance | 144 | 0.655 | 0.813 | 0.336 | 0.851 | 21 | 3.985 |

### Notes:

<!-- Slide number: 26 -->
#

![](GoogleShape236p38.jpg)

### Notes:

<!-- Slide number: 27 -->
#

![](GoogleShape243p39.jpg)

### Notes:

<!-- Slide number: 28 -->
#

![](GoogleShape250p40.jpg)
|  | Metric | Value |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total False Positives (FP) | 1163 |
| 2 | Number of FP Cleaned | 394 |
| 3 | Number of TP Ignored | 6 |
| 4 | % FP Cleaned (of Total Samples) | 23% |
| 5 | % FP Cleaned (of Total FP) | 34% |
| 6 | % TP Ignored (of Total TP) | 1% |

### Notes:

<!-- Slide number: 29 -->

![](GoogleShape258p41.jpg)
#

### Notes:

<!-- Slide number: 30 -->
#

![](GoogleShape265p42.jpg)
|  | Metric | Value |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total False Positives (FP) | 1163 |
| 2 | Number of FP Cleaned | 631 |
| 3 | Number of TP Ignored | 21 |
| 4 | % FP Cleaned (of Total Samples) | 37% |
| 5 | % FP Cleaned (of Total FP) | 54% |
| 6 | % TP Ignored (of Total TP) | 4% |

### Notes:

<!-- Slide number: 31 -->
# stacked_svm_extratrees_classifier.ipynb

![](GoogleShape273p43.jpg)
🏆 TOP 20 MOST IMPORTANT FEATURES:
 1. 🎯 svm_prediction                 				0.187128
 2.    data_source_category_SSO       				0.039040
 3.    rule_Multiple anomalous sign-in properties 		0.032320
 4.    internal_ips_normalized_entropy 				0.027080
 5.    data_source_category_Secure Web Gateway 			0.018752

### Notes:

<!-- Slide number: 32 -->
# Stats are different, no hyperparameter tuning

| Model | KS\_Statistic | AUC | Recall | Precision | Low\_Prob\_Malicious | Low\_Prob\_Percentage |
| --- | --- | --- | --- | --- | --- | --- |
| ExtraTrees\_Full\_Baseline | 0.6301 | 0.8860 | 0.2713 | 0.8512 | 15 | 2.8463 |
| SVM\_Full | 0.6260 | 0.8705 | 0.0019 | 1.0000 | 66 | 12.5237 |
| ExtraTrees\_Stacked | 0.6505 | 0.8888 | 0.2884 | 0.8539 | 17 | 3.2258 |

### Notes:

<!-- Slide number: 33 -->
#
| Metric | Reduced features (baseline) | ROS 1:1 | Enhanced single (with is\_single\_rule) | ExtraTrees PCA | EXtraTrees (top 144 (70%) important features) | ExtraTree (prior to svm) | ExtraTree + SVM |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total Samples | 1690 | 1690 | 1690 | 1690 | 1690 | 1690 | 1690 |
| Total False Positives (FP) | 1163 | 1163 | 1163 | 1163 | 1163 | 1163 | 1163 |
| Number of FP Cleaned | 781 | 662 | 554 | 394 | 631 | 582 | 625 |
| Number of TP Ignored | 39 |  | 13 | 6 | 21 | 15 | 17 |
| % FP Cleaned (of Total Samples) | 46% | 39% | 33% | 23% | 37% | 34% | 37% |
| % FP Cleaned (of Total FP) | 67% | 57% | 48% | 34% | 54% | 50% | 54% |
| % TP Ignored (of Total TP) | 7% | 4% | 2% | 1% | 4% | 3% | 3% |

### Notes:

<!-- Slide number: 34 -->
# fp_cleaned_optimizer_grid_search.ipynb

![](GoogleShape293p46.jpg)

### Notes:

<!-- Slide number: 35 -->
# Models optimized to maximum class 0 recall @98% precision
| Metric | Enhanced single (with is\_single\_rule) | ExtraTrees PCA | ExtraTrees\_Full/omit\_suspicious\_alerts |  |  |
| --- | --- | --- | --- | --- | --- |
| Total Samples | 1690 | 1690 | 1690 |  |  |
| Total False Positives (FP) | 1163 | 1163 | 1163 |  |  |
| Number of FP Cleaned | 554 | 394 | 498 |  |  |
| Number of TP Ignored | 13 | 6 | 11 |  |  |
| % FP Cleaned (of Total Samples) | 33% | 23% | 29% |  |  |
| % FP Cleaned (of Total FP) | 48% | 34% | 43% |  |  |
| % TP Ignored (of Total TP) | 2% | 1% | 2% |  |  |

### Notes:

<!-- Slide number: 36 -->
# SVM and KNN classifiers can be used to enrich features

![](GoogleShape306p48.jpg)

### Notes:

<!-- Slide number: 37 -->
# KNN and SVM classifiers can be used to enrich features

![](GoogleShape313p49.jpg)

### Notes:

<!-- Slide number: 38 -->
# Svm + knn (advanced ml pipeline)
| Metric | Random Forest enhanced features | Gradient Boosting pca features | Gradient Boosting enhanced features | Random Forest pca features | Extra Trees pca features | Logistic Regression enhanced features | Logistic Regression pca features | Extra Trees enhanced features |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total Samples | 1690 | 1690 | 1690 | 1690 | 1690 | 1690 | 1690 | 1690 |
| Total False Positives (FP) | 1163 | 1163 | 1163 | 1163 | 1163 | 1163 | 1163 | 1163 |
| Number of FP Cleaned | 423 | 416 | 406 | 340 | 326 | 234 | 177 | 776 |
| Number of TP Ignored | 11 | 11 | 11 | 11 | 11 | 11 | 11 | 67 |
| % FP Cleaned (of Total Samples) | 25% | 25% | 24% | 20% | 19% | 14% | 10% | 46% |
| % FP Cleaned (of Total FP) | 36% | 36% | 35% | 29% | 28% | 20% | 15% | 67% |
| % TP Ignored (of Total TP) | 2% | 2% | 2% | 2% | 2% | 2% | 2% | 13% |
|  | 77/23 | 75/25 | 76/24 | 76/24 | 75/25 | 76/24 | 75/25 | 72/28 |

### Notes:

<!-- Slide number: 39 -->
#
I tried to inspect the original feature transformation upon round4 feature extraction (perhaps there is a slight variance between it an round5) and also knn+svm (enhaced) features and pca feature reduction, i did it in notebook advanced_ml_pipeline_with_transformed_feats4.ipynb but discovered that there are significant differences between cv scores and test scores. This is probably due to underrepresented samples in folds, combining with different thresholds for 0.98 precision (as required by scorer function). I tried to overcome it with Repeated Stratified K-Fold

### Notes:

<!-- Slide number: 40 -->
# ExtraTrees_basic_features (hyperparameter tuning)
ExtraTrees_fixed_enhanced_features
🎯 Clean Efficiency Score: 0.3166
🎯 CV Score: 0.2774
🎯 FPs Threshold (98% recall): 0.0730
🎯 Clean Efficiency Score: 0.3249
🎯 CV Score: 0.5076
🎯 FPs Threshold (98% recall): 0.0481
|  | Metric | Value |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total False Positives (FP) | 1163 |
| 2 | Number of FP Cleaned | 535 |
| 3 | Number of TP Ignored | 11 |
| 4 | % FP Cleaned (of Total Samples) | 32% |
| 5 | % FP Cleaned (of Total FP) | 46% |
| 6 | % TP Ignored (of Total TP) | 2% |
|  | Metric | Value |
| --- | --- | --- |
| 0 | Total Samples | 1690 |
| 1 | Total False Positives (FP) | 1163 |
| 2 | Number of FP Cleaned | 549 |
| 3 | Number of TP Ignored | 11 |
| 4 | % FP Cleaned (of Total Samples) | 32% |
| 5 | % FP Cleaned (of Total FP) | 47% |
| 6 | % TP Ignored (of Total TP) | 2% |
bootstrap: False
ccp_alpha: 0.0
class_weight: balanced
criterion: gini
max_depth: 12
max_features: sqrt
max_leaf_nodes: None
max_samples: None
min_impurity_decrease: 0.0
min_samples_leaf: 1
min_samples_split: 2
min_weight_fraction_leaf: 0.0
n_estimators: 200
n_jobs: None
oob_score: False
random_state: 42
verbose: 0
warm_start: False

### Notes:

<!-- Slide number: 41 -->

![](GoogleShape343p53.jpg)
#

### Notes:

<!-- Slide number: 42 -->

![](GoogleShape350p54.jpg)
#
| Metric | Value |
| --- | --- |
| Total Samples | 1690 |
| Total True Positives (TP) | 527 |
| Number of TP Marked | 264 |
| Number of FP Marked | 83 |
| % TP Marked (of Total TP) | 50% |
| % TP Marked (of Total Marked Samples) | 76% |
| % FP Marked (of Total Marked Samples) | 24% |

### Notes:

<!-- Slide number: 43 -->

![](GoogleShape358p55.jpg)
#
| Metric | Value |
| --- | --- |
| Total Samples | 1690 |
| Total False Positives (FP) | 1163 |
| Number of FP Cleaned | 549 |
| Number of TP Ignored | 11 |
| % FP Cleaned (of Total Samples) | 32% |
| % FP Cleaned (of Total FP) | 47% |
| % TP Ignored (of Total TP) | 2% |

### Notes:

<!-- Slide number: 44 -->
# features
1_year_feats-round5.ipynb excluding high_suspicious_simple_alert and instant_high_suspicious_threat. Over this svm (C=1.0, gamma='auto') and knn (n_neighbors=3, weights='uniform', metric='euclidean') classifiers where knn probabilities are binned [0.2,0.5,0.8,1]

### Notes:
