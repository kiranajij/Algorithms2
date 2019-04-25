class WeightedGraph:
    """
    This is a data structure to hold a graph.
    """

    def __init__(self, graph: dict):
        """
        :param graph: graph is of type dict. The graph must be in format
                {
                    vertex: [(edge_vertex, weight)]
                }
                where vertex is a vertex of the graph
                edge_vertex is a edge. for a graph G = (V, E)
                if (u, v) belongs to E and weight of (u, v) is w then
                (v, w) belongs to graph[u].
        """
        self.graph = graph

    def get_neighbors(self, v):
        """
        :param v: the vertex whose neighbors are desired
        :return: returns the neighbors of v
        """
        neighbors = [i[0] for i in self.graph[v]]
        return neighbors

    def get_weight(self, u, v):
        for key in self.graph[u]:
            if key[0] == v:
                return key[1]
        return None

    def get_weights(self, v):
        weights = [i[1] for i in self.graph[v]]
        return weights

    def get_min_weighted_pair(self, v):
        """
        This function returns the minimum weighted pair from the neighbor of v
        :param v: vertex
        :return: tuple
        """
        tmp: list = self.graph[v]
        if not tmp:  # if
            return None
        min_pair = min(tmp, key=lambda x: x[1])  # getting the minimum
        return min_pair

    def get_vertices(self):
        return self.graph.keys()

    def get_edges(self, v):
        return self.graph[v]

    def make_edge_list(self):
        edges = []
        for k in self.get_vertices():
            for v, w in self.get_edges(k):
                if v < k: continue
                edge = Edge(k, v, w)
                edges.append(edge)
        return edges

    def get_length(self):
        return len(self.get_vertices())

    def __str__(self) -> str:
        return self.graph.__str__()

    def __repr__(self) -> str:
        return "WeightedGraph()"


class Edge:
    def __init__(self, x: object, y: object, weight: float):
        self.x = x
        self.y = y
        self.weight = weight

    def __eq__(self, other):
        if self.x == other.y:
            if self.y == other.x and self.weight == other.weight:
                return True
        if self.x == other.x:
            if self.y == other.y and self.weight == other.weight: return True

        return False
