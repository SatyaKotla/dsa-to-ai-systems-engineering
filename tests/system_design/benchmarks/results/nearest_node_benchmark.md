# Nearest Node Benchmark

## Testing linear nearest node search.

**Hardware:** Windows 10

**Language:** Python 3.13

### Dataset Results:

|Sr. No.  |     Dataset    |  Search Time (in seconds) |
|----------:|:-------------|:------:|
| 1 |  Grid 10 nodes | 0.000036 |
|2 |    Grid 50 nodes   |   0.000747 |
|3 |Grid 100 nodes |    0.004330 |
|4 | Grid 1000 nodes |    0.611789 |

### Observation:
Search time increases linearly with number of nodes.

### Conclusion:
Current algorithm is O(N)

### Next Step:
Implement KD-tree spatial index to reduce complexity to O(log N).
