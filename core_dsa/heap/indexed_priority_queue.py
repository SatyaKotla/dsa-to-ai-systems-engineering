class IndexedPriorityQueue():
    """
    Index Priority Queue supporting O(log(n)) insert, update, and removal.

    - Keys must be unique.
    - Supports min-heap or max-heap behavior.
    """

    def __init__(self, is_min_heap: bool = True):
        self._heap = []              # list of keys (unique element)
        self._priorities = {}        # key -> priority (score)
        self._position = {}          # key -> index in heap (rank)
        self._is_min_heap = is_min_heap
    
    # -----------------------------------------------
    # Public API
    # -----------------------------------------------

    def insert(self, key, priority):
        """
        Insert a new key with given priority.
        Raises KeyError if key already exists.
        """
        if key in self._position:
            raise ValueError("Key already exists.")
        
        self._priorities[key] = priority
        self._heap.append(key)

        index = len(self._heap) - 1
        self._position[key] = index 

        self._heapify_up(index)

    def update(self, key, new_priority):
        """
        Update an existing key with the new priority.
        Raises KeyError if key does not exist.
        """
        if key not in self._position:
            raise ValueError("Key does not exist.")
        
        # update the new priority
        self._priorities[key] = new_priority
        
        index = self._position[key]
        parent_index = self._parent(index)

        # If not root and violates the heap property with parent
        # go up
        if index > 0 and self._compare(self._heap[index],
                                        self._heap[parent_index]):
            self._heapify_up(index)
        else:
            self._heapify_down(index)


    def remove(self, key):
        """
        Removes a key from the queue.
        Raises KeyError if key does not exist.
        """
        if key not in self._position:
            raise ValueError("Key does not exist")
        
        index = self._position[key]
        last_index = len(self._heap) - 1

        # If Removing last element
        if index == last_index:
            self._heap.pop()
            del self._position[key]
            del self._priorities[key]
            return
        
        # swap with the last element
        self._swap(index, last_index)

        # remove the last element (given key shifted to last)
        self._heap.pop()

        del self._position[key]
        del self._priorities[key]
    
        # Restore heap property (previous last shifted to index)
        if index > 0 and self._compare(self._heap[index], 
                                       self._heap[self._parent(index)]):
            self._heapify_up(index)
        else:
            self._heapify_down(index)



    def pop(self):
        """
        Remove and return (key, priority) of the top element.
        """
        if not self._heap:
            raise IndexError("Heap is empty")
        
        root_key = self._heap[0]
        root_priority = self._priorities[root_key]

        last_index = len(self._heap) - 1

        # swap the root and the last element
        self._swap(0, last_index)

        # removes the last element(original root)
        self._heap.pop()

        # remove the root's reference from position and priorities
        del self._position[root_key]
        del self._priorities[root_key]

        # heapify down with new root
        if self._heap:
            self._heapify_down(0)
        
        return (root_key, root_priority)


    def peek(self):
        """
        Return the top-priority (key, priority) without removing it.
        """
        if not self._heap:
            raise IndexError("Heap is empty")
        key = self._heap[0]
        return (key, self._priorities[key])

    def contains(self, key) -> bool:
        """
        Return True if key exists in the queue.
        """
        return key in self._position

    def size(self) -> int:
        """
        Return the number of elements.
        """
        return len(self._heap)

    def is_empty(self) -> bool:
        """
        Return True if queue is empty.
        """
        return not self._heap
    
    def __len__(self):
        return len(self._heap)
    
    def __contains__(self, key):
        return key in self._position
    
    def __bool__(self):
        return bool(self._heap)
    
    def clear(self):
        self._heap.clear()
        self._position.clear()
        self._priorities.clear()

    # -----------------------------------------------
    # Internal Helpers
    # -----------------------------------------------

    def _heapify_up(self, index):
        
        while index > 0:
            parent = self._parent(index)
            
            if self._compare(self._heap[index], self._heap[parent]):
                self._swap(index, parent)
                index = parent
            else:
                break

    def _heapify_down(self, index):
        
        size = len(self._heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2 
            current_best = index

            # check left child
            if left < size and self._compare(self._heap[left], 
                                             self._heap[current_best]):
                current_best = left 
           
            # check right child
            if right < size and self._compare(self._heap[right], 
                                             self._heap[current_best]):
                current_best = right 
            
            # If no better child found, stop
            if current_best == index:
                break 

            # Otherwise swap and continue
            self._swap(index, current_best)
            index = current_best

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = (self._heap[j],
                                        self._heap[i])
        # update position to reflect the change in heap
        self._position[self._heap[i]] = i 
        self._position[self._heap[j]] = j

    def _compare(self, key1, key2) -> bool:
        """
        Return True if key1 should come before key2. 
        """
        if self._is_min_heap:
            return self._priorities[key1] < self._priorities[key2]
        else:
            return self._priorities[key1] > self._priorities[key2]

    def _parent(self, index):
        parent_index = (index - 1) // 2 
        return parent_index

    def _left(self, index):
        left_index = 2 * index + 1
        return left_index

    def _right(self, index):
        right_index = 2 * index + 2
        return right_index

def main() -> None:
    pass 

if __name__ == "__main__":
    main()