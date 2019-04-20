from bfs import Graph


class Dfs:
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
        if not self.discovered[v]:
            pass
            # visiting for the first time

        elif self.parents[u] != v:
            # found a back edge
            print("{}-{}".format(u, v), end="")
            path = self.find_path(v, u)
            print(path)

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
    dfs = Dfs(graph)
    # dfs.dfs(1, True)
    # print(dfs.parents)
    # print(dfs.entry)
    # print(dfs.exit)
    dfs.dfs(1, True)