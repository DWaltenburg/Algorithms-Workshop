class DisJSet:
    def __init__(self, n):
        self.value = [i for i in range(n)]
        self.size = [-1] * n

    def find(self, x):
        if self.size[x] > 0:
            self.size[x] = self.find(self.size[x])
        return self.size[x]

    def weighted_union(self, x, y):
        if self.size[x] and self.size[y] < 0:
            temp = self.size[x] + self.size[y]

            if  self.size[x] > self.size[y]:
                self.size[x] = y
                self.size[y] = temp

            else:
                self.size[y] = x
                self.size[x] = temp

def sequence(n):
    #time start
    forrest = DisJSet(n)

    for i in range(n-1):
        forrest.weighted_union(i+1,i)

    for i in range(n):
        forrest.find(i)

#sequence(100)
tree = DisJSet(10)
tree.weighted_union(1,2)
tree.weighted_union(1,3)
tree.weighted_union(1,4)

tree.weighted_union(5,6)
tree.weighted_union(5,7)

tree.weighted_union(1,5)

for i in range(10):
    print(tree.value[i], ":", tree.size[i], ":", tree.find(i))