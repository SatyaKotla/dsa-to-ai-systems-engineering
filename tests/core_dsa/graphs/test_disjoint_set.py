####################################################
# - TESTS FOR GRAPHS (DISJOINT SET (UNION-FIND)) - #
####################################################
from core_dsa.graphs.disjoint_set import DijointSet


# Test: make_set initialization
def test_make_set_initialization():
    ds = DijointSet()

    ds.make_set("A")
    ds.make_set("B")

    assert ds.parent["A"] == "A"
    assert ds.parent["B"] == "B"


# Test: find Returns Self Initially
def test_find_initial_root():
    ds = DijointSet()

    ds.make_set("A")

    assert ds.find("A") == "A"


# Test: Simple Union
def test_union_chain():
    ds = DijointSet()

    for v in ["A", "B", "C"]:
        ds.make_set(v)

    ds.union("A", "B")
    ds.union("B", "C")

    assert ds.find("A") == ds.find("C")


# Test: Separate Components
def test_separate_components():
    ds = DijointSet()

    for v in ["A", "B", "C", "D"]:
        ds.make_set(v)

    ds.union("A", "B")
    ds.union("C", "D")

    assert ds.find("A") != ds.find("C")


# Test: Union Same Set
def test_union_same_set():
    ds = DijointSet()

    for v in ["A", "B"]:
        ds.make_set(v)

    ds.union("A", "B")
    ds.union("A", "B")

    assert ds.find("A") == ds.find("B")


# Test: Larger Set
def test_multiple_unions():
    ds = DijointSet()

    for v in ["A", "B", "C", "D", "E"]:
        ds.make_set(v)

    ds.union("A", "B")
    ds.union("B", "C")
    ds.union("C", "D")

    assert ds.find("A") == ds.find("D")
    assert ds.find("A") != ds.find("E")
