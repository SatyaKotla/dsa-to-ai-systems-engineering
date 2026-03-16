####################################################
# --------- TESTS FOR ROUTE SEGMENT COMPONENT -------- ####
####################################################
from system_design.route_optimizer.engine.router import Router
from core_dsa.graphs.adjacency_list import Graph
from system_design.route_optimizer.engine.spatial_index_factory import (
    create_spatial_index,
)


def build_test_graph():

    g = Graph(directed=True)

    g.add_edge("A", "B", 1)
    g.add_edge("B", "C", 1)

    g.coords["A"] = (0, 0)
    g.coords["B"] = (1, 0)
    g.coords["C"] = (2, 0)

    return g


def test_route_segments():

    g = build_test_graph()

    index = create_spatial_index(graph=g, method="kdtree")

    router = Router(graph=g, spatial_index=index)

    start = (0, 0)
    goal = (2, 0)

    result = router.compute_route(start, goal)

    assert len(result.segments) > 0

    first = result.segments[0]

    assert first.start_node is not None
    assert first.end_node is not None
