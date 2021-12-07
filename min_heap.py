class MinHeap:
    def __init__(self, heap_size):
        #Complete a complete binary tree using an array
        #Then use the binary tree to construct a Heap
        self.heap_size = heap_size
        #The number of elements is needed when instantiating an array
        #heap_size records the size of the array
        self.min_heap = [0] * (heap_size + 1)
        #real_size stores the number of elements in the heap
        self.real_size = 0 
    
    # Function to add an element
    def add(self, element):
        self.real_size += 1
        if self.real_size > self.heap_size:
            print("You're trying to add too many elements")
            self.real_size -= 1
            return
        #Add the element into the array
        self.min_heap[self.real_size] = element
        #Index of the newly added element
        index = self.real_size
        print(f" Index = {index}")
        print(self.min_heap)
        #Parent node of newly added element. If we use an array to 
        #represent the complete binary tree and store the root at index
        #1 index of the parent node of any node is [index_of_the_node /2]
        #Index of the left child node is [index_of_the_node *2]
        #Index of the right child node is [index_of_the_node *2 + 1]
        parent = index // 2
        print(f"Parent = {parent}")
        #Check if the newly added element is smaller than its parent
        while(self.min_heap[index] < self.min_heap[parent] and index > 1):
            self.min_heap[parent], self.min_heap[index] = self.min_heap[index], self.min_heap[parent]
            index = parent
            parent = index //2

    def peek(self):
        return self.min_heap[1]


if __name__ == "__main__":
    min_heap1 = MinHeap(5)
    min_heap1.add(3)
    min_heap1.add(1)
    min_heap1.add(4)
    min_heap1.add(6)
    print(f"The smallest value is {min_heap1.peek()}")
