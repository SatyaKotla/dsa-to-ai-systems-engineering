# Graphs

This module contains graph data structure implementations.

## Implementations:

### 1. Adjacency List 

A flexible graph implementation supporting:

- Directed and undirected graphs
- Weighted edges
- Dynamic vertex creation
- Efficient neighbor lookup
- Suitability for sparse graphs

#### Design

The graph is internally stored as :
vertex -> list of(neighbor, weight)

This representation provides:
- Space Complexity: O(V + E)
- Efficient traversal of neighbors
- Suitability for sparse graphs

#### Core Methods

- `add_vertex(vertex)`
- `add_edge(u, v, weight)`
- `neighbors(vertex)`
- `vertices()`

#### Intended Usage

This graph implementation is designed to support:

- Dijkstra's Algorithm
- BFS/DFS
- Topological Sorting
- Future graph-based algorithms
