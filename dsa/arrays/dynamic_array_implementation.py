class DynamicArray:

    def __init__(self):
        self.capacity = 1
        self.items = [None] * self.capacity
        self.size = 0 #num items are 0
    
    def append(self,item):

        if self.capacity == self.size:
            self.resize()
        self.items[self.size] = item
        self.size+=1
    
    def resize(self):
        self.capacity = self.capacity * 2
        new_array = [None] * (self.capacity) #create a new array with twice the size
        for i in range(self.size):
            new_array[i] = self.items[i]
        self.items = new_array
