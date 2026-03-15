# Spatial Benchmark

## Objective

Compare brute-force (Linear Scan) nearest node search with KD-tree spatial indexing.

## Methodology

- Datasets: grid graphs (10, 50, 100, 1000)
- Queries: 100 random coordinate searches
- Metric: average query time
- Hardware: Local machine

## Results

|Dataset |     Nodes    |  Linear Scan (Brute Force) | KD Tree | Speedup |
|:----------|-------------:|:------:|:------:|------:|
| Grid_10 | 100  |0.00002793s |0.00004336s|0.64x|
|Grid_50   |   2500   |  0.00067760s  |0.00005639s|12.02x|
|Grid_100  |10000 |  0.00289105s  |0.00001810s|159.76x|
|Grid_1000  | 1000000 |  0.59763321s   |0.00008579s|6966.08x|

## Conclusion:
KD-tree dramatically improves nearest node lookup performance as dataset size increases.
Brute-force search scales linearly O(N), while KD-tree provides approximately O(log N) search time.
