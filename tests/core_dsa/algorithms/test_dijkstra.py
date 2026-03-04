####################################################
########## TESTS FOR DIJKSTRA ALGORITHM ############
####################################################
from core_dsa.algorithms.dijkstra import dijkstra, reconstruct_path
from core_dsa.graphs.adjacency_list import Graph
import pytest

# Basic Shortest Path
def test_dijkstra_basic():
    g = Graph(directed=True)

    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(0, 2, 4)

    distance, _ = dijkstra(g, 0)

    assert distance[0] == 0
    assert distance[1] == 1
    assert distance[2] == 3

# Disconnected Graph
def test_dijkstra_disconnected():
    g = Graph(directed=True)
    g.add_edge(0, 1, 5)

    distance, _ = dijkstra(g, 0)

    assert distance.get(2, float("inf")) == float("inf")

# Negative Weight Validation
def test_dijkstra_reject_negative_weights():
    g = Graph(directed=True)
    g.add_edge(0, 1, -1)

    with pytest.raises(ValueError):
        dijkstra(g, 0)

# Path Reconstruction
def test_dijkstra_path_reconstruction():
    g = Graph(directed=True)

    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)

    _, previous = dijkstra(g, 0)

    path = reconstruct_path(previous, 2)
    
    assert path == [0, 1, 2]