from core_dsa.arrays.dynamic_array import DynamicArray

def test_constructor_with_iterable():
    a = DynamicArray([1, 2, 3])
    assert a.to_list() == [1, 2, 3]
    

def test_append():
    a = DynamicArray()
    a.append(10)
    assert a.to_list() == [10]
   


