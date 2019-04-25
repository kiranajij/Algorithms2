from WeightedGraph.UnionFind import UnionFind
from WeightedGraph.WeightedGraph import *


class Kruskal:
    def __init__(self, graph: WeightedGraph):
        self.graph = graph
        self.parents = {}

    def kruskal(self):
        edges = self.graph.make_edge_list()
        edges.sort(key=lambda x: x.weight)
        uf = UnionFind(self.graph.get_length())

        while edges:
            edge = edges.pop(0)
            if not uf.is_same_component(edge.x, edge.y):
                uf.union_sets(edge.x, edge.y)
                print("Edge: {0.x}-{0.y}".format(edge))
                self.parents[edge.y] = edge.x

        return self.parents

    def process_uf(self, uf: UnionFind):
        pass