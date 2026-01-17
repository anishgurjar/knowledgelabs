class Stack:

    def __init__(self,val=None):
        self._stack = []
        self._length = 0
        if val:
            self._stack.append(val)
            self._length += 1
    
    def push(self,val):
        self._stack.append(val)
        self._length += 1

    def pop(self):
        if self._length == 0:
            return None
        item = self._stack[self._length - 1]
        self._length -= 1
        del self._stack[self._length - 1]
        return item
    
    def isEmpty(self, x):
        if self._length > 0:
            return False
        else:
            return True
    
    def size(self):
        return self._length

    def peek(self):
        return self._stack[0]