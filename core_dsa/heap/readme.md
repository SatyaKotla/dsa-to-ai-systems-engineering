# Heap Module

This module contains heap-based data structure implementations.

## Implementations

### 1. Indexed Priority Queue 

A binary heap with O(1) key lookup using a position map.

**Features:**
- O(log n) insert
- O(log n) update (change priority)
- O(log n) remove by key
- O(1) peek

**Use cases:**
- Dijkstra's Algorithm
- A* search
- Scheduling systems