class DisJSet:
    def __init__(self, n):
        self.value = [i for i in range(n)]
        self.size = [-1] * n

    def find(self, x):
        if self.size[x] > 0:
            x = self.find(self.size[x])
        return x

    def weighted_union(self, x, y):
        if self.find(x) == self.find(y) or ((self.size[x] or self.size[y]) > 0):
            return

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

sequence(100)