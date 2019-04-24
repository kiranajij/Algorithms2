class WeightedGraph:
    def __init__(self, graph: dict):
        self.graph = graph

    def get_neighbors(self, v):
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

    def __str__(self) -> str:
        return super().__str__()

    def __repr__(self) -> str:
        return super().__repr__()

