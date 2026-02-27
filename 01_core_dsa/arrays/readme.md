# Array Data Structures (Built from Scratch)

This folder contains implementation of a dynamic array in Python, built from first principles withou using Python's built in list features for resizing logic.

The goal is to understand:
- Memory management
- Amortized analysis
- In-place algorithms
- API Design
- Encapsulation

## Implementated Features

### Core Operations
    - append (amortized O(1))
    - insert (O(n))
    - delete (O(n))
    - pop 
    - resize (double capacity)
    - shrink (half capacity)

### In-Place Algorithms
    - reverse() 
    - rotate(k, right=True) -- O(n), reversal algorithm
    - remove_duplicates_sorted(sorted arrays only) -- O(n), two-pointers technique

### Python Protocol Support
    - __getitem__ for indexing
    - __setitem__ for assignment
    - __iter__ for iteration support
    - __len__ for length support
    - to_list() for safe data exposure

## Concepts covered

- Amortized time complexity
- Capacity vs Size distinction 
- Two-pointer technique
- In-place algorithms
- Reversal algorithm 
- Modular arithmetic (rotation logic)
- Encapsulation and abstraction
- Iterator protocol
- Defensive programming

## Usage Example

```python
from dynamic_array import DynamicArray

# Append example
a = DynamicArray()
a.append(1)
a.append(2)
print(a.to_list()) # [1, 2]

# Reversing an array example
a.reverse()
print(a.to_list()) # [2, 1]
```

## Why this project?
This implementation focuses on low-level array behavior and algorithmic efficiency rather than relying on Python's built-in list.