####################################################
# --------- TESTS FOR A STAR(*) ALGORITHM --------- #
####################################################
from core_dsa.algorithms.astar import astar, reconstruct_path
from core_dsa.algorithms.dijkstra import dijkstra
from core_dsa.graphs.adjacency_list import Graph


# Basic shortest path
def test_astart_basic_path():

    edges = [("A", "B", 1), ("A", "C", 4), ("B", "C", 2), ("B", "D", 5), ("C", "D", 1)]

    g = Graph.from_edges(edges=edges)

    g.coords = {"A": (0, 0), "B": (1, 0), "C": (1, 1), "D": (2, 1)}

    distance, previous = astar(g, "A", "D")

    path = reconstruct_path(previous, "A", "D")

    assert path == ["A", "B", "C", "D"]
    assert distance["D"] == 4


# Goal Unreachable
def test_astar_unreachable():
    g = Graph()

    g.add_edge("A", "B", 1)
    g.add_edge("C", "D", 1)

    g.coords = {"A": (0, 0), "B": (1, 0), "C": (2, 0), "D": (3, 0)}

    distance, previous = astar(g, "A", "D")

    assert distance["D"] == float("inf")


# Zero Heuristic = Dijkstra
def zero_heuristic(graph, node, goal):
    return 0


def test_astar_equals_dijkstra():

    edges = [("A", "B", 2), ("A", "C", 5), ("B", "C", 1), ("C", "D", 3)]

    g = Graph.from_edges(edges)

    g.coords = {"A": (0, 0), "B": (1, 0), "C": (1, 1), "D": (2, 1)}

    distance_astar, _ = astar(g, "A", "D", heuristic=zero_heuristic)
    distance_dijkstra, _ = dijkstra(g, "A")

    assert distance_astar["D"] == distance_dijkstra["D"]
