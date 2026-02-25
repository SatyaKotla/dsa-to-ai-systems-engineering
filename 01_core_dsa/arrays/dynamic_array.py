#dynamic array 
class DynamicArray():
    def __init__(self):
        self.max_len = 1
        self.size = 0
        self.array = [None] * self.max_len

    def append(self, item):
        if self.size == self.max_len:
            self._resize()

        self.array[self.size] = item 
        self.size += 1
    
    def _resize(self):
        self.max_len = self.max_len * 2 
        new_array = [None] * self.max_len
        
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array

    def __len__(self):
        return self.size
    
    def __getitem__(self, index):
        if index < 0:
            index = self.size + index 
        
        if index < 0 or index >= self.size:
            raise IndexError("Index is out of range")
        
        return self.array[index]
    
    def insert(self, index,value):
        # Handling negative index
        if index < 0:
            index = self.size + index

        # Allowing insertion at the end (index == self.size)
        if index < 0 or index > self.size:
            raise IndexError("Index is out of range")
        
        #Resize if full
        if self.size == self.max_len:
                self._resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]

        #Insertion
        self.array[index] = value
        self.size = self.size + 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Popping from an empty array.")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None 
        self.size = self.size - 1

        # shrink the capacity of the array if size is less than 
        # 1/4th of the capacity
        if self.size > 0 and self.size <= self.max_len //4:
            self._shrink()
        return value 
    
    
    def _shrink(self):
        self.max_len = self.max_len // 2
        new_array = [None] * self.max_len 

        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array =  new_array 
    
    def delete(self, index):
        if index < 0:
            index = self.size + index
        
        if index < 0 and index >= self.size:
            raise IndexError("Index is out of range.")
        
        value = self.array[index]

        #shift left
        for i in range(index, self.size-1):
            self.array[i] = self.array[i + 1]
        
        self.array[self.size -1] = None 
        self.size = self.size - 1

        if self.size > 0 and self.size <= self.max_len//4 :
            self._shrink()
        
        return (value)



if __name__ == "__main__":
    a = DynamicArray()
    print(f"Initial array {a.array}")
    a.append(10)
    a.append(20)
    a.append(30)
    print(f"array after appending 10, 20 , 30 : {a.array[:a.size]}")
    a.insert(1, 40)
    print(f"array after inserting an element at index 1 :{a.array[:a.size]}")
    popped_value = a.pop()
    print(f"popped value is :{popped_value} ; array after popping is : {a.array[:a.size]}")
    deleted_value = a.delete(0)
    print(f"deleted value is : {deleted_value}; array after deleting an element at 0th index : {a.array[:a.size]}")