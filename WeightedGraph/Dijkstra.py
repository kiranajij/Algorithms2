import sys

from WeightedGraph import WeightedGraph


class Dijkstra:
    def __init__(self, graph: WeightedGraph):
        self.graph = graph
        self.parents = {}

    def initialize(self):
        for k in self.graph.get_vertices():
            self.parents[k] = None

    def dijkstra(self, start, end):
        dist = {}
        in_tree = {}
        self.parents = {}

        for k in self.graph.get_vertices():
            dist[k] = sys.maxsize
            in_tree[k] = False
            self.parents[k] = None

        c_v = start
        dist[c_v] = 0

        while not in_tree[c_v]:
            in_tree[c_v] = True
            for n_v, w in self.graph.get_edges(c_v):
                if (not in_tree[n_v]) and (dist[n_v] > dist[c_v] + w):
                    self.parents[n_v] = c_v
                    dist[n_v] = dist[c_v] + w

            c_v = start
            d = sys.maxsize

            for k in self.graph.get_vertices():
                if (not in_tree[k]) and (dist[k] < d):
                    c_v = k
                    d = dist[k]

        return self.backtrace(start, end)

    def backtrace(self, start, end) -> list:
        c_v = end
        p = self.parents[c_v]
        path = [c_v]
        while p is not None:
            c_v = p
            p = self.parents[c_v]
            path.append(c_v)
        path.reverse()
        return path