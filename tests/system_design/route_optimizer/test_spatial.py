####################################################
# --------- TESTS FOR SPATIAL COMPONENT -------- #
####################################################
from system_design.route_optimizer.engine.spatial import find_nearest_node
from core_dsa.graphs.adjacency_list import Graph


# Test: Basic Nearest Node
def test_find_nearest_node_basic():

    g = Graph(directed=True)

    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")

    g.set_coord("A", (0, 0))
    g.set_coord("B", (3, 4))
    g.set_coord("C", (7, 2))

    node = find_nearest_node(g, 2, 1)

    assert node == "A"


# Test: Exact Coordinate Match
def test_find_nearest_node_exact_match():

    g = Graph(directed=True)

    g.add_vertex("A")
    g.set_coord("A", (5, 5))

    node = find_nearest_node(g, 5, 5)

    assert node == "A"


# Test: Skip Nodes Without Coordinates
def test_find_nearest_node_skip_missing_coords():
    g = Graph(directed=True)

    g.add_vertex("A")
    g.add_vertex("B")

    g.set_coord("B", (10, 10))

    node = find_nearest_node(g, 9, 9)

    assert node == "B"


# Test: Single Node Graph
def test_find_nearest_node_single():

    g = Graph(directed=True)

    g.add_vertex("A")
    g.set_coord("A", (1, 1))

    node = find_nearest_node(g, 10, 10)

    assert node == "A"
