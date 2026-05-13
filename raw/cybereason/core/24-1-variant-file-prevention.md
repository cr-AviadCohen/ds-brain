The Cybereason platform includes Variant File Prevention (VFP), a
pre-execution prevention engine which uses advanced fuzzy
hashing techniques to scan files and quickly identify indicative
similarities and patterns of known malware families.
VFP is supported on Windows machines. For details, see Endpoint
machine prevention features (/s/knowledge-base?article=24-1-
supported-features-by-operating-
system&language=en_US#endpoint-machine-prevention-
features).
In this topic:
How does VFP work?
Detection and prevention of files
How does VFP work?
Traditional execution prevention solutions, which rely on
cryptographic hashes such as MD5, SHA-1, or SHA-256 alone,
are easy to bypass. Attackers are aware that any change to the
malicious file will completely change its file hash value.
To address this challenge, VFP compares each file with fuzzy
fingerprints that are resistant to changes. Each fingerprint covers
many variants of a high-value threat. If a file is found to match the
fingerprint, VFP detects it as a MalOp.
See this example of a MalOp detected by VFP:
