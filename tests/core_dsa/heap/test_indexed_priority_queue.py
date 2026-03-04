####################################################
########## TESTS FOR INDEXED PRIORITY QUEUE#########
####################################################
from core_dsa.heap.indexed_priority_queue import IndexedPriorityQueue
import pytest

# Basic ordering property
def test_ipq_pop_returns_sorted_order():
    ipq = IndexedPriorityQueue()

    data = {
        "a": 5,
        "b": 1,
        "c": 3,
        "d": 2

    }
    
    for key, priority in data.items():
        ipq.insert(key, priority)
    
    result = []
    
    while not ipq.is_empty():
        result.append(ipq.pop()[1])
    
    assert result == sorted(data.values())

# Decrease-Key Behavior
def test_ipq_decrease_priority_moves_up():
    ipq = IndexedPriorityQueue()

    ipq.insert("a", 10)
    ipq.insert("b", 20)
    ipq.insert("c", 30)

    ipq.update("c", 1)

    # c should be at the root
    assert ipq._heap[0] == "c"

# Increase-Key Behvaior
def test_ipq_increase_priority_moves_down():
    ipq = IndexedPriorityQueue()

    ipq.insert("a", 1)
    ipq.insert("b", 2)
    ipq.insert("c", 10)

    # increase priority of root
    ipq.update("a", 100)

    # a should not be at the root
    assert ipq._heap[0] != "a"

# Remove Key
def test_ipq_remove_key():
    ipq = IndexedPriorityQueue()

    ipq.insert("a", 1)
    ipq.insert("b", 2)

    ipq.remove("a")

    assert not ipq.contains("a")
    assert ipq.size() == 1

# Empty Pop Error
def test_ipq_pop_empty_raises():
    ipq = IndexedPriorityQueue()

    with pytest.raises(IndexError):
        ipq.pop()

# Internal Consistency Invariance Test
def test_ipq_internal_consistency():
    ipq = IndexedPriorityQueue()

    ipq.insert("a", 10)
    ipq.insert("b", 5)
    ipq.insert("c", 20)

    # Check position map matches heap structure
    for index, key in enumerate(ipq._heap):
        assert ipq._position[key] == index
    
    # Check all keys in position map exists in heap
    for key in ipq._position:
        assert key in ipq._heap
    
    # Check priorities exist for all Keys
    for key in ipq._heap:
        assert key in ipq._priorities