class Graph:
    def __init__(self, relation: dict,
                 n_vertices: int,
                 directed: bool = False):
        self.directed = directed
        self.n_vertices = n_vertices
        self.relation = relation

    def get_neighbours(self, v):
        return self.relation[v]


class Bfs:
    def __init__(self, graph: Graph):
        self.parent = {}
        self.discovered = []
        self.processed = []
        self.graph = graph

    def initialize_search(self):
        self.parent = {i: None for i in range(1, self.graph.n_vertices + 1)}
        self.discovered = {i: False for i in range(1, self.graph.n_vertices + 1)}
        self.processed = {i: False for i in range(1, self.graph.n_vertices + 1)}

    def bfs(self, start, restart: bool = True):
        if restart:
            self.initialize_search()
        queue = [start]  # Queue to store vertices to process
        self.discovered[start] = True
        self.parent[start] = None

        while queue:
            c_v = queue.pop(0)
            self.process_vertex_early(c_v)
            for n_v in self.graph.get_neighbours(c_v):
                if self.graph.directed or not self.processed[n_v]:
                    self.process_edge(c_v, n_v)
                if not self.discovered[n_v]:
                    queue.append(n_v)
                    self.discovered[n_v] = True
                    self.parent[n_v] = c_v
                self.process_vertex_late(n_v)
            self.processed[c_v] = True

    def find_path(self, start, end) -> list:
        self.bfs(start)
        c_v = end
        p = self.parent[c_v]
        path = [c_v]
        while p is not None:
            c_v = p
            p = self.parent[c_v]
            path.append(c_v)
        path.reverse()
        return path

    def connected_components(self):
        n = self.graph.n_vertices
        self.components = {}
        self.c = 0
        self.initialize_search()
        for i in range(1, n):
            if not self.discovered[i]:
                self.c += 1

                self.bfs(i, restart=False)
        return self.components

    def two_color(self):
        self.color = {i: None for i in range(1, self.graph.n_vertices + 1)}
        self.bipartable = True
        self.initialize_search()

        for i in range(1, graph.n_vertices + 1):
            if not self.discovered[i]:
                self.color[i] = True
                self.bfs(i)
        return self.bipartable

    def process_vertex_early(self, v):
        # self.components[v] = self.c
        pass

    def process_edge(self, c_v, n_v):
        # self.n_vertex += 1
        if self.color[c_v] == self.color[n_v]:
            self.bipartable = False
        else:
            self.color[n_v] = self.complement(self.color[c_v])

    def process_vertex_late(self, n_v):
        pass

    def complement(self, color):
        if color is None:
            return None
        if color:
            return False
        return True


if __name__ == '__main__':
    g = {
        1: [2, 3, 4],
        2: [1, 5, 6],
        3: [1, 5, 7],
        4: [1, 6],
        5: [2, 3, 7],
        6: [2, 4],
        7: [3, 5],
        8: [9, 10],
        9: [8],
        10: [8]
    }

    graph = Graph(g, 10, False)
    bfs = Bfs(graph)
    c = bfs.two_color()
    print(c)
