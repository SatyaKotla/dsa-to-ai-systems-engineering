from core_dsa.arrays.dynamic_array import DynamicArray
import pytest

# Constructor edge cases
def test_constructor_with_iterable():
    a = DynamicArray([1, 2, 3])
    assert a.to_list() == [1, 2, 3]

def test_constructor_empty():
    a = DynamicArray()
    assert a.to_list() == []

# Append behavior
def test_append():
    a = DynamicArray()
    a.append(10)
    assert a.to_list() == [10]

def test_append_mutliple():
    a = DynamicArray()
    for i in range(6):
        a.append(i)
    assert a.to_list() == [0, 1, 2, 3, 4, 5]

# Resize behavior
def test_resize_behavior():
    a = DynamicArray()
    for i in range(100):
        a.append(i)
    
    assert len(a.to_list()) == 100 
    assert a.to_list()[0] == 0 
    assert a.to_list()[-1] == 99

# Reverse edge cases
@pytest.mark.parametrize("input_data, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4], [4, 3, 2, 1]),
]) 
def test_reverse(input_data, expected):
    a = DynamicArray(input_data)
    a.reverse()
    assert a.to_list() == expected

# Indexing
def test_index_access():
    a = DynamicArray([10, 20, 30])
    assert a[0] == 10
    assert a[2] == 30

# Index out of bounds
def test_index_out_of_bounds():
    a = DynamicArray([1, 2, 3])
    with pytest.raises(IndexError):
        _ = a[5]

# Length validation test
def test_length_updates_correctly():
    a = DynamicArray()
    assert len(a) == 0
    a.append(1)
    assert len(a) == 1

# Large scale stress test for correctness
def test_large_input():
    a = DynamicArray()
    for i in range(10000):
        a.append(i)
    assert a.to_list()[0] == 0 
    assert a.to_list()[-1] == 9999

# Mutation safety
def test_to_list_returns_copy():
    a = DynamicArray([1, 2, 3])
    _list = a.to_list()
    _list.append(100)
    assert a.to_list() == [1, 2, 3]