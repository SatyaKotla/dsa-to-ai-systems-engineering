####################################################
# --------- TESTS FOR KRUSKAL ALGORITHM --------- #
####################################################
from core_dsa.algorithms.kruskal import kruskal


# Basic MST Test
def test_kruskal_basic():
    vertices = ["A", "B", "C", "D"]

    edges = [("A", "B", 4), ("A", "C", 2), ("B", "C", 5), ("B", "D", 10), ("C", "D", 3)]

    mst, total_weight = kruskal(vertices=vertices, edges=edges)

    assert total_weight == 9
    assert len(mst) == 3


# Already Minimum Graph
def test_kruskal_tree_graph():

    vertices = ["A", "B", "C"]

    edges = [("A", "B", 1), ("B", "C", 2)]

    mst, total_weight = kruskal(vertices=vertices, edges=edges)

    assert total_weight == 3
    assert len(mst) == 2


# Cycle Detection Test
def test_kruskal_cycle_detection():

    vertices = ["A", "B", "C"]

    edges = [("A", "B", 1), ("B", "C", 2), ("A", "C", 3)]

    mst, total_weight = kruskal(vertices=vertices, edges=edges)

    assert total_weight == 3
    assert len(mst) == 2


# Diconnected Graph (Forest Case)


def test_kruskal_disconnected():

    vertices = ["A", "B", "C", "D"]

    edges = [("A", "B", 1), ("C", "D", 2)]

    mst, total_weight = kruskal(vertices=vertices, edges=edges)

    assert total_weight == 3
    assert len(mst) == 2


# Edge Order Independence Test
def test_kruskal_unsorted_edges():
    vertices = ["A", "B", "C", "D"]

    edges = [("B", "D", 10), ("B", "C", 5), ("A", "B", 4), ("C", "D", 3), ("A", "C", 2)]

    _, total_weight = kruskal(vertices=vertices, edges=edges)

    assert total_weight == 9
