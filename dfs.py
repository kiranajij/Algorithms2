from bfs import Graph
from graphs import *


class Dfs:
    PARENT_EDGE = 2
    BACK_EDGE = 1
    TREE_EDGE = 0

    def __init__(self, graph: Graph):
        self.processed = {}
        self.graph = graph
        self.n_vertices = graph.n_vertices
        self.parents = {}
        self.discovered = {}
        self.entry = {}
        self.exit = {}
        self.time = 0
        self.finished = False

    def initialize_search(self):
        for i in range(1, self.n_vertices + 1):
            self.parents[i] = None
            self.discovered[i] = False
            self.processed[i] = False
            self.entry[i] = None
            self.exit[i] = None
        self.finished = False

    def dfs(self, start, restart=False):
        if self.finished:
            return
        if restart:
            self.initialize_search()
        self.discovered[start] = True
        self.process_vertex_early(start)
        self.time += 1
        self.entry[start] = self.time
        # self.time += 1
        for n_v in self.graph.get_neighbours(start):
            if not self.discovered[n_v]:
                self.parents[n_v] = start
                self.process_edge(start, n_v)
                self.dfs(n_v)
            elif not self.processed[n_v]:
                self.process_edge(start, n_v)
                if self.finished:
                    return
        self.processed[start] = True
        self.process_vertex_late(start)
        self.time += 1
        self.exit[start] = self.time
        # self.time += 1

    def process_vertex_early(self, start):
        # print("{}->".format(start), end="")
        pass

    def process_edge(self, u, v):
        pass

    def find_path(self, start, end) -> list:
        # self.dfs(start)
        c_v = end
        p = self.parents[c_v]
        path = [c_v]
        while c_v != start and p is not None:
            c_v = p
            p = self.parents[c_v]
            path.append(c_v)
        path.reverse()
        return path

    def process_vertex_late(self, v):
        pass

    def classify_edge(self, x, y):
        if not self.discovered[y]:
            return self.TREE_EDGE
        elif self.parents[x] != y:
            return self.BACK_EDGE
        else:
            return self.PARENT_EDGE


class DfsCycle(Dfs):
    def process_edge(self, u, v):
        if not self.discovered[v]:
            # Visiting first time
            pass
        elif self.parents[u] != v:
            # Found Cycle
            path = self.find_path(v, u)
            print(path)

    def process_vertex_early(self, start):
        pass

    def process_vertex_late(self, v):
        pass


class DfsArticulation(Dfs):

    def __init__(self, *args, **kwargs):
        super(DfsArticulation, self).__init__(*args, **kwargs)
        self.reachable_vertex = {}
        self.tree_outdegree = {}  # Number of edges coming out of a node

    def initialize_search(self):
        super(DfsArticulation, self).initialize_search()
        self.reachable_vertex = {}
        self.tree_outdegree = {}

    def process_edge(self, u, v):
        edge_class = self.classify_edge(u, v)
        if edge_class == self.TREE_EDGE:
            # print("{}-{}: TREE".format(u, v))
            self.tree_outdegree[u] += 1
        elif edge_class == self.BACK_EDGE:
            # print("{}-{}: BACK".format(u, v))
            if self.entry[v] < self.entry[self.reachable_vertex[u]]:
                self.reachable_vertex[u] = v

    def process_vertex_early(self, v):
        self.reachable_vertex[v] = v
        self.tree_outdegree[v] = 0

    def process_vertex_late(self, v):
        if self.parents[v] is None:
            # Root of our tree
            if self.tree_outdegree[v] > 1:
                # has more than two children
                print("root cut node: ", v)
            return
        is_root = self.parents[self.parents[v]] is None
        if self.reachable_vertex[v] == self.parents[v] and not is_root:
            print("Parent cut Node", self.parents[v])

        if self.reachable_vertex[v] == v:
            print("bridge articulation node(p): ", self.parents[v])

            if self.tree_outdegree[v] > 0:
                print("bridge articulation node(v): ", v)

        time_v = self.entry[self.reachable_vertex[v]]
        time_p = self.entry[self.reachable_vertex[self.parents[v]]]

        if time_v < time_p:
            self.reachable_vertex[self.parents[v]] = self.reachable_vertex[v]


class DfsDirected(Dfs):
    FORWARD_EDGE = 3
    CROSS_EDGE = 4

    def classify_edge(self, x, y):
        if self.parents[y] == x:
            return self.TREE_EDGE
        if (not self.processed[y]) and self.discovered[y]:
            return self.BACK_EDGE
        if self.processed[y] and self.entry[y] > self.entry[x]:
            return self.FORWARD_EDGE
        if self.processed[y] and self.entry[y] < self.entry[x]:
            return self.CROSS_EDGE
        print("Warning: unclassified edge ({}, {})".format(x, y))

    def process_edge(self, u, v):
        pass


class TopoSort(DfsDirected):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toposort = []

    def process_vertex_late(self, v):
        self.toposort.append(v)

    def process_edge(self, u, v):
        cls = self.classify_edge(u, v)
        print("class({}, {}) = {}".format(u, v, cls))
        if cls == self.BACK_EDGE:
            print("Warning: Back edge ({}, {}), not a DAG".format(u, v))

    def initialize_search(self):
        super().initialize_search()
        self.toposort = []

    def topo_sort(self):
        self.initialize_search()
        for key in self.graph.keys():
            if not self.discovered[key]:
                self.dfs(key)

        self.toposort.reverse()
        return self.toposort

