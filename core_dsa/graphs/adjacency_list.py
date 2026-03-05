class Graph:
    """
    Adjacency List Graph representation.

    Supports:
    - Directed or undirected graphs
    - Weighted edges
    """

    def __init__(self, directed: bool = True):
        self._adj = {}
        self._directed = directed
        self.negative_edge_count = 0

    def add_vertex(self, vertex):
        """Add a vertex to a graph."""
        if vertex not in self._adj:
            self._adj[vertex] = []

    def add_edge(self, u, v, weight: float = 1):
        """
        Add an edge from u to v with given weight.
        If graph is undirected, also adds edge from v to u.
        """
        self.add_vertex(u)
        self.add_vertex(v)

        if weight < 0:
            self.negative_edge_count += 1

        self._adj[u].append((v, weight))

        if not self._directed:
            self._adj[v].append((u, weight))

    def neighbors(self, vertex):
        """
        Return list (neighbor, weight).
        """
        return self._adj.get(vertex, [])

    def vertices(self):
        """
        Return all vertices.
        """
        return self._adj.keys()

    def __contains__(self, vertex):
        return vertex in self._adj

    def __len__(self):
        return len(self._adj)

    def __repr__(self):
        return f"Graph(directed={self._directed})," f"vertices={len(self._adj)}"


def main():
    graph = Graph(directed=True)

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 2)
    graph.add_edge("B", "D", 1)
    graph.add_edge("C", "D", 4)

    print(graph.neighbors("A"))


if __name__ == "__main__":
    main()
