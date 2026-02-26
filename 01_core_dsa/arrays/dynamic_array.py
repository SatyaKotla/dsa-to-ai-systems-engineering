#dynamic array 
class DynamicArray():
    def __init__(self):
        self._max_len = 1 # capacity of the array
        self._size = 0 # actual size of the array
        self._array = [None] * self._max_len # array

    def append(self, item):
        if self._size == self._max_len:
            self._resize()

        self._array[self._size] = item 
        self._size += 1
    
    def _resize(self):
        self._max_len = self._max_len * 2 
        new_array = [None] * self._max_len
        
        for i in range(self._size):
            new_array[i] = self._array[i]
        
        self._array = new_array

    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        if index < 0:
            index = self._size + index 
        
        if index < 0 or index >= self._size:
            raise IndexError("Index is out of range")
        
        return self._array[index]
    
    # to access the element to set value to at the index position
    def __setitem__(self, index, value):
        if index < 0:
            index = self._size + index

        if index < 0 or index >= self._size:
            raise IndexError("Index is out of range")
        
        self._array[index] = value
    
    # for looping the elements directly
    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]
    
    # to get the array without the other memory values
    def to_list(self):
        return self._array[:self._size]
    
    def insert(self, index,value):
        # Handling negative index
        if index < 0:
            index = self._size + index

        # Allowing insertion at the end (index == self.size)
        if index < 0 or index > self._size:
            raise IndexError("Index is out of range")
        
        #Resize if full
        if self._size == self._max_len:
                self._resize()
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]

        #Insertion
        self._array[index] = value
        self._size = self._size + 1

    def pop(self):
        if self._size == 0:
            raise IndexError("Popping from an empty array.")
        value = self._array[self._size - 1]
        self._array[self._size - 1] = None 
        self._size = self._size - 1

        # shrink the capacity of the array if size is less than 
        # 1/4th of the capacity
        if self._size > 0 and self._size <= self._max_len //4:
            self._shrink()
        return value 
    
    
    def _shrink(self):
        self._max_len = self._max_len // 2
        new_array = [None] * self._max_len 

        for i in range(self._size):
            new_array[i] = self._array[i]
        
        self._array =  new_array 
    
    def delete(self, index):
        if index < 0:
            index = self._size + index
        
        if index < 0 and index >= self._size:
            raise IndexError("Index is out of range.")
        
        value = self._array[index]

        #shift left
        for i in range(index, self._size-1):
            self._array[i] = self._array[i + 1]
        
        self._array[self._size -1] = None 
        self._size = self._size - 1

        if self._size > 0 and self._size <= self._max_len//4 :
            self._shrink()
        
        return (value)
    
    # Reverse an Array (In - Place)
    """
    Reverse elements without creating a new array.
    For example:
    Input: [1, 2, 3, 4]
    Output: [4, 3, 2, 1]

    """
    def reverse(self):
        i = 0
        while i < self._size // 2:
            (self._array[i], self._array[self._size-1]) = (self._array[self._size-1], 
                                                self._array[i])
            i = i+1
        return self._array 

    # Finding the maximum element in the array
    def max(self):
        if self._size == 0:
            raise ValueError("The array is empty.")
        
        max_value = self._array[0]
        
        for i in range(1, self._size):
            if self._array[i] > max_value:
                max_value = self._array[i]
        
        return max_value


if __name__ == "__main__":
    a = DynamicArray()
    print(f"Initial array {a.to_list()}")
    a.append(10)
    a.append(20)
    a.append(30)
    print(f"\nArray after appending 10, 20 , 30 : {a.to_list()}")
    a.insert(1, 40)
    print(f"\nArray after inserting an element at index 1 :{a.to_list()}")
    popped_value = a.pop()
    print(f"\nPopped value is :{popped_value}; array after popping is : {a.to_list()}")
    deleted_value = a.delete(0)
    print(f"\nDeleted value is : {deleted_value}; array after deleting an element at 0th index : {a.to_list()}")
    a.reverse()
    print(f"\nArray after reversing it in place: {a.to_list()}")
    max_value = a.max()
    print(f"\nMaximum value in the array: {max_value}")
