class Node:

    def __init__(self):
        self.value = None
        self.next = None

    def set_value(self, new_value):
        self.value = new_value
    
    def get_value(self):
        return self.value

    def set_next(self, node):
        self.next = node
