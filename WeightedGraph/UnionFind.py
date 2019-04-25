"""
This Module contains the union set data structure.
"""


class UnionFind(object):
    def __init__(self, size: int):
        self.size = size
        self.sizes = []
        self.parents = []
        self.initialize_union_find()

    def initialize_union_find(self) -> None:
        for i in range(self.size+1):
            self.parents.append(i)
            self.sizes.append(1)

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        return self.find(self.parents[x])

    def union_sets(self, x: int, y: int) -> None:
        r1 = self.find(x)
        r2 = self.find(y)

        if r1 == r2: return

        if self.sizes[r1] >= self.sizes[r2]:
            self.sizes[r1] += self.sizes[r2]
            self.parents[r2] = r1
        else:
            self.sizes[r2] += self.sizes[r1]
            self.parents[r1] = r2

    def is_same_component(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def __str__(self):
        return self.parents.__str__()