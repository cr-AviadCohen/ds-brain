# NGAV Analysis.docx

![](data:image/png;base64...)

NGAV Analysis with VirusTotal

Introduction

VirusTotal is the ideal resource for performing accurate and unbiased analyses of Anti-virus (AV) tools because it hosts the largest database of malicious samples and details how security vendors classify them. This is important because it is possible for AV vendors to skew results in their favor by removing certain samples that do not fit into their model, or by strategically selecting a group of samples that fit particularly well. Cybereason has statistically demonstrated the effectiveness of the Cybereason NGAV solution by querying VirusTotal for transparent and unbiased comparisons against other AV vendors using a random selection of over 10,000 malicious and benign samples. The following provides details on how we used VirusTotal data to demonstrate a vendor’s effectiveness in key three key areas. These are:

1. A vendor’s ability to identify malicious samples that were never-before-seen.
2. A vendor’s ability to accurately identify known malware.
3. A vendor’s false positive rate.

Analysis #1: How Well Does Cybereason Block Unknown Malware?

The first analysis is designed to demonstrate how well the Cybereason NGAV solution blocks unknown malware. This will show how often vendors are able to catch malware that, upon first appearance, would defy standard AV techniques. Quality machine learning algorithms are required to perform well in this analysis. Here is how we performed this analysis:

1. Looking at a specific set of dates two months in the past, we took a random selection of first-ever-scans where ten or fewer vendors convicted the sample as malicious. This effectively provided a set of threats that did not have a clear signature (unknown malware).
2. From that set, we took the samples that were flagged by more than twenty vendors two months later. This removed any false positives from the initial list.
3. This left us with a set of definitively malicious samples that were not easily detected by traditional AV methods. We ran this set against a list of vendors and noted the percent of samples that each vendor flagged as malicious initially. These are all malicious so the closer to 100%, the better.

The results for the top three vendors are as follows:

1. Cybereason: 74.4%
2. Cylance: 54.4%
3. CrowdStrike: 52.6%

*Note:* In this test, we only utilized the machine learning layer of the Cybereason NGAV solution to demonstrate the effectiveness of the machine learning engine alone. We would score higher with the addition of our signature-based and behavioral layers, which are in the actual product.

Analysis #2: How Well Does Cybereason Block Known Malware?

The second analysis is designed to show how well AV vendors block known malware. Specifically, it is designed to see how machine learning based detection compares to traditional signature-based detection. Here is how we to performed this analysis:

1. First, we determined a list of 8 leading traditional AV vendors. We chose AVG, BitDefender, ESET, Kaspersky, McAfee, Microsoft, Sophos, and Symantec.
2. Looking at a specific set of dates, we took valid PE-EXE samples whose first scans were detected by at least 6 of the chosen leading vendors.
3. From this list, we took only the badware (malware and ransomware but no PUPs).
4. We were left with set of actual malware that contained signatures caught by most traditional AV methods. We ran these samples against our list of AV vendors and NGAV vendors and noted the percent of samples that each vendor flagged as malicious. These are all malicious, so the closer to 100%, the better.

The results for the top three vendors are as follows:

1. Symantec: 99.7%
2. Cybereason: 99.5%
3. McAfee: 99.4%

*Note:* In this test, we only utilized the machine learning layer of our NGAV to demonstrate the effectiveness of our machine learning alone. We would score higher with the addition of our signature-based and behavioral layers, which are in the actual product.

Analysis #3: How Well Does Cybereason Avoid False Positives?

The final analysis is designed to show how often an AV vendor will block benign samples. Here is how we performed this analysis:

1. We picked a vendor to test for their false positive rate.
2. We took a selection of random samples that *all* *other* vendors did not flag as malicious upon their first scan.
3. We tested those samples against the vendor chosen in step 1 and counted the percentage of samples that were flagged as malicious. Since none of the samples were malicious, the closer to 0 the better.
4. We repeated steps 1-3 for each vendor.

The results for the top three machine learning vendors are as follows:

1. Cybereason: 2.2%
2. CrowdStrike: 2.6%
3. Cylance: 6.6%
