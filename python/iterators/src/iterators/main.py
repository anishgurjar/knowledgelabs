class CountUpTo:

    def __init__(self, limit: int):
        self.curr = 0
        self.limit = limit
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curr < self.limit:
            self.curr += 1
            return self.curr
        else:
            raise StopIteration

mycounter = CountUpTo(10)

print(next(mycounter))
print(next(mycounter))
print(next(mycounter))
print(next(mycounter))
print(next(mycounter))
