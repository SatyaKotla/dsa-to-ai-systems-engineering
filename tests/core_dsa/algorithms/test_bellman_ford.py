####################################################
# --------- TESTS FOR BELLMAN-FORD ALGORITHM --------- #
####################################################
from core_dsa.algorithms.bellman_ford import bellman_ford, reconstruct_path
from core_dsa.algorithms.dijkstra import dijkstra
from core_dsa.graphs.adjacency_list import Graph
import pytest

# Basic Shortest Path


def test_bellman_ford_basic():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, -3)
    g.add_edge(2, 3, 4)

    distance, _ = bellman_ford(g, source=0)

    assert distance[0] == 0
    assert distance[1] == 4
    assert distance[2] == 1
    assert distance[3] == 5


# Test with Negative Edge


def test_negative_edges():
    g = Graph()
    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 3, -1)
    g.add_edge(3, 4, 1)

    distance, _ = bellman_ford(g, source=0)

    assert distance[0] == 0
    assert distance[1] == 1
    assert distance[2] == 0
    assert distance[3] == -1
    assert distance[4] == 0


# Negative Cycle Detection Test
def test_negative_cycle_detection():
    g = Graph()
    g.add_edge(0, 1, -1)
    g.add_edge(1, 2, -1)
    g.add_edge(2, 0, -1)

    with pytest.raises(ValueError):
        bellman_ford(g, 0)


# Test to verify Bellman_ford with Dijkstra
def test_bellman_ford_dijkstra_correctness():
    g = Graph(directed=True)

    g.add_edge(0, 1, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(0, 2, 4)

    distance1, _ = dijkstra(g, 0)
    distance2, _ = bellman_ford(g, 0)

    assert distance1[0] == distance2[0]
    assert distance1[1] == distance2[1]
    assert distance1[2] == distance2[2]


# Path reconstruction
def test_bellman_ford_path_reconstruction():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 5)
    g.add_edge(1, 2, -3)
    g.add_edge(2, 3, 4)

    _, previous = bellman_ford(g, source=0)

    path = reconstruct_path(previous, 3)

    assert path == [0, 1, 2, 3]


# Destination is unreachable
def test_bellman_ford_unreachable():
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(2, 3, 1)

    _, previous = bellman_ford(g, 0)

    path = reconstruct_path(previous, 3)

    assert path is None
