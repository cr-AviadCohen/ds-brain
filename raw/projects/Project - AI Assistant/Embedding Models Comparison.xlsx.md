# Embedding Models Comparison.xlsx

## Sheet1
| Feature | all-mpnet-base-v2 (Your Current) | bge-small-en-v1.5 (Local Speed) | potion-base-8M (Static/Instant) | voyage-3-lite (Managed API) |
| --- | --- | --- | --- | --- |
| Type | Dense Transformer | Dense Transformer | Static (Model2Vec) | API (Matryoshka) |
| Dimensions | 768 | 384 | 256 | 512 (Flexible) |
| Model Size | ~420 MB | ~133 MB | ~30 MB | N/A (Cloud) |
| Parameters | ~110M | ~33M | ~8M | Unknown |
| Est. Latency | ~25ms | ~10ms | < 1ms | ~11ms (+ network) |
| Accuracy (MTEB) | High (Top ~60) | Very High (Top ~20) | Moderate | Best (Top 5) |
| Context | 384 tokens | 512 tokens | 512 tokens | 32,000 tokens |
| Verdict | Too Heavy / Slow | The Best Balance | The Speed King | The Quality King |
