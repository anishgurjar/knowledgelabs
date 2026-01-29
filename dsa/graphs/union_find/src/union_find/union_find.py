class UnionFind:

    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)
    
    def union(self,x,y):

        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False #already connected
        
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_y] < self.rank[root_x]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        
        return True
    