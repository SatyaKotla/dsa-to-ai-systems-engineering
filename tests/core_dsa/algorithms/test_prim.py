####################################################
# --------- TESTS FOR PRIM'S ALGORITHM --------- #
####################################################
from core_dsa.algorithms.prim import prim
from core_dsa.graphs.adjacency_list import Graph


# Simple Graph Test
def test_prim_basic_graph():
    g = Graph()

    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("C", "A", 4)
    g.add_edge("C", "D", 2)
    g.add_edge("D", "B", 3)
    g.add_edge("D", "C", 2)
    g.add_edge("B", "A", 1)
    g.add_edge("B", "D", 3)

    mst, weight = prim(graph=g, source="A")

    assert weight == 6
    assert len(mst) == 3


# Single Node Graph
def test_prim_single_node():
    g = Graph()

    g.add_vertex("A")

    mst, weight = prim(graph=g, source="A")

    assert mst == []
    assert weight == 0


# Two Node Graph
def test_prim_two_nodes():
    g = Graph()

    g.add_edge("A", "B", 5)
    g.add_edge("B", "A", 5)

    mst, weight = prim(graph=g, source="A")

    assert weight == 5
    assert len(mst) == 1


# Larger Graph Test
def test_prim_larger_graph():
    g = Graph()

    g.add_edge("A", "B", 2)
    g.add_edge("A", "C", 6)
    g.add_edge("A", "D", 3)
    g.add_edge("B", "A", 2)
    g.add_edge("B", "E", 5)
    g.add_edge("C", "A", 6)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "A", 3)
    g.add_edge("D", "C", 1)
    g.add_edge("D", "E", 4)
    g.add_edge("E", "B", 5)
    g.add_edge("E", "D", 4)

    mst, weight = prim(graph=g, source="A")

    assert weight == 10
    assert len(mst) == 4


# Disconnnected Graph
def test_prim_disconnected_graph():
    g = Graph()

    g.add_edge("A", "B", 1)
    g.add_edge("B", "A", 1)
    g.add_vertex("C")

    mst, weight = prim(graph=g, source="A")

    assert weight == 1
    assert len(mst) == 1


# Edge Validation
def test_prim_edges():
    g = Graph()

    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "A", 1)
    g.add_edge("B", "D", 3)
    g.add_edge("C", "A", 4)
    g.add_edge("C", "D", 2)
    g.add_edge("D", "B", 3)
    g.add_edge("D", "C", 2)

    mst, weight = prim(graph=g, source="A")

    edges = {(u, v) for u, v, w in mst}

    assert ("A", "B") in edges or ("B", "A") in edges


# Test Decrese Key Behavior
def test_prim_decrease_key_behavior():
    g = Graph(directed=False)

    g.add_edge("A", "B", 10)
    g.add_edge("A", "C", 6)
    g.add_edge("A", "D", 5)
    g.add_edge("C", "D", 4)
    g.add_edge("D", "E", 2)
    g.add_edge("B", "E", 15)

    mst, weight = prim(graph=g, source="A")

    assert weight == 21
    assert len(mst) == 4
