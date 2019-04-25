from WeightedGraph import WeightedGraph
import sys

class Prim:
    """
    This is the implementation of Prim's algorithm of finding 
    minimum spanning tree of a weighted graph.
    """
    def __init__(self, graph: WeightedGraph):
        """
        """
        self.graph = graph
        self.parents = {}

    def initialize(self):
        for key in self.graph.get_vertices():
            self.parents[key] = None
    
    def prim(self, start):
        dist = {}
        in_tree = {}

        # Initializing variables
        for key in self.graph.get_vertices():
            in_tree[key] = False
            dist[key] = sys.maxsize

        v = start
        dist[v] = 0

        while not in_tree[v]:
            in_tree[v] = True
            for vert, weight in self.graph.get_edges(v):
                if (dist[vert] > weight) and (not in_tree[vert]):
                    dist[vert] = weight
                    self.parents[vert] = v

            v = start
            d = sys.maxsize

            for vert in self.graph.get_vertices():
                if (not in_tree[vert]) and (dist[vert] < d):
                    v = vert
                    d = dist[vert]
