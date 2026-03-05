####################################################
# -------- TESTS FOR GRAPH (Adjacency list) ------ #
####################################################
from core_dsa.graphs.adjacency_list import Graph


# Directed Graph Behavior
def test_directed_graph_add_edge():
    g = Graph(directed=True)
    g.add_edge(0, 1, 5)

    assert (1, 5) in g._adj[0]
    assert 0 not in [v for v, _ in g._adj.get(1, [])]


# Undirected Graph Behavior
def test_undirected_graph_add_edge():
    g = Graph(directed=False)
    g.add_edge(0, 1, 5)

    assert (1, 5) in g._adj[0]
    assert (0, 5) in g._adj[1]


# Negative Weight Tracking
def test_graph_negative_weight_tracking():
    g = Graph(directed=True)
    g.add_edge(0, 1, -5)

    assert g.negative_edge_count == 1
