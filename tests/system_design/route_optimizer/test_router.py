####################################################
# --------- TESTS FOR ROUTER COMPONENT -------- ####
####################################################
from system_design.route_optimizer.engine.router import Router
from core_dsa.graphs.adjacency_list import Graph
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)

# Test the basic route


def build_test_graph():

    g = Graph(directed=True)

    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 1)

    g.coords["A"] = (0, 0)
    g.coords["B"] = (1, 0)
    g.coords["C"] = (2, 0)

    return g


def test_compute_route_basic():

    g = build_test_graph()

    index = create_spatial_index(graph=g, method="kdtree")

    router = Router(graph=g, spatial_index=index)

    start = (0.1, 0)
    goal = (1.9, 0)

    result = router.compute_route(start, goal)

    assert result.nodes == ["A", "B", "C"]
    assert result.distance == 2


# Test: Unreachable Node
def test_compute_route_unreachable():

    g = Graph(directed=True)

    g.add_edge("A", "B", 1)
    g.add_vertex("C")

    g.coords["A"] = (0, 0)
    g.coords["B"] = (1, 0)
    g.coords["C"] = (5, 5)

    start = (0, 0)
    goal = (5, 5)

    index = create_spatial_index(graph=g, method="kdtree")

    router = Router(graph=g, spatial_index=index)

    result = router.compute_route(start, goal)

    assert result.nodes == []
    assert result.distance == float("inf")


# Test for Same Start and Goal


def test_compute_route_same_node():

    g = build_test_graph()

    start = (0.1, 0)
    goal = (0.2, 0)

    index = create_spatial_index(graph=g, method="kdtree")

    router = Router(graph=g, spatial_index=index)

    result = router.compute_route(start, goal)

    assert result.nodes == ["A"]
    assert result.distance == 0
