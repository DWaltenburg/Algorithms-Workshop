class DisJSet:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        if self.parent[x] == self.parent[y]:
            return
        else:
            self.link(self.find(x), self.find(y))

    def link(self, x, y):
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] = self.rank[x] + 1


def sequence(n):
    forrest = DisJSet(n)

    for i in range(n-1):
        forrest.union(i+1, i)
        print(i+1,"union", i+1, "with", i)
    
    for i in range(n):
        parent = forrest.find(i)
        print(i, "parent is", parent)

sequence(5)