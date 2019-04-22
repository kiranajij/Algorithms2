def scan_graph():
    n = int(input())
    graph = {}
    for i in range(n):
        e1, e2 = list(input().split())
        if e1 not in graph:
            graph[e1] = []
        if e2 not in graph:
            graph[e2] = []
        graph[e1].append(e2)
        graph[e2].append(e1)

    return graph


class Graph:
    def __init__(self, graph):
        self.graph = graph

    def get_neighbours(self, item):
        return self.graph[item]

    def keys(self):
        return self.graph.keys()

class Bfs:
    def __init__(self, graph):
        self.discovered = {}
        self.graph = graph
        self.parents = {}
        self.colors = {}
        self.partable = True
        self.processed = {}

    def initialize_search(self):
        for k in self.graph.keys():
            self.parents[k] = None
            self.colors[k] = None
            self.discovered[k] = False
            self.processed[k] = False
        self.partable = True

    def compliment(self, c):
        if c == 0:
            return 1
        elif c == 1:
            return 0
        else:
            return None

    def process_vertex(self, u, v):
        if self.colors[v] is None:
            self.colors[v] = self.compliment(self.colors[u])
        if self.colors[v] == self.colors[u]:
            self.partable = False

    def bfs(self, start):
        queue = [start]
        self.discovered[start] = True
        while queue:
            c_v = queue.pop(0)
            self.discovered[c_v] = True
            for n_v in self.graph.get_neighbours(c_v):
                if not self.discovered[n_v]:
                    queue.append(n_v)
                    self.discovered[n_v] = True
                self.process_vertex(c_v, n_v)
                self.processed[c_v] = True

    def run(self):
        self.initialize_search()
        for i in self.graph.keys():
            if not self.discovered[i]:
                self.colors[i] = 1
                self.bfs(i)
        return self.partable


if __name__ == '__main__':
    tc = int(input())
    for i in range(tc):
        graph = scan_graph()
        g = Graph(graph)
        bfs = Bfs(g)
        res = bfs.run()
        if res:
            print('Yes')
        else:
            print('No')