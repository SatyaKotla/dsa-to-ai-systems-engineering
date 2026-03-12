####################################################
# --------- TESTS FOR TOPOLOGICAL SORT ALGORITHM - #
####################################################

# Kahn's Algorithm
from core_dsa.algorithms.topological_sort import topological_sort_kahn
from core_dsa.graphs.adjacency_list import Graph
import pytest


# test for valid DAG
def test_kahn_topological_sort():
    g = Graph(directed=True)

    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")

    order = topological_sort_kahn(g)

    assert order[0] == "A"
    assert order[-1] == "D"


# Cycle Detection
def test_kahn_cycle_detection():
    g = Graph(directed=True)

    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "A")

    with pytest.raises(ValueError):
        topological_sort_kahn(g)
