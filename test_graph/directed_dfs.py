from graph import *
from dfs import *


class EdgeClassification(DFS):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def classify_edge(self, x, y):
        if self.parents[y] == x or not self.discovered[y]:
            return "TREE"

        if self.discovered[y] and not self.processed[y]:
            return "BACK"

        if self.processed[y] and self.entry[x] < self.entry[y]:
            return "FORWARD"

        if self.processed[y] and self.entry[y] < self.entry[x]:
            return "CROSS"

        return "UNCLASSIFIED"

    def process_edge(self, x, y):
        edge_class = self.classify_edge(x, y)
        print(f"{x}-{y}\t{edge_class}")


class TopologicalSort(EdgeClassification):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.toposort_stack = []

    def process_edge(self, x, y):
        edge_class = self.classify_edge(x, y)
        if edge_class == "BACK":
            raise TypeError("No cycles allowed in DAS")

    def process_vertex_late(self, v):
        self.toposort_stack.append(v)

    def toposort(self):
        for i in range(self.n):
            if not self.discovered[i]:
                name = i
                if isinstance(self.graph, MappedGraph):
                    name = self.graph.get_node_name(i)
                self.dfs(name)

        return self.toposort_stack[::-1]

class StronglyConnectedComponent(EdgeClassification):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    


if __name__ == '__main__':
    
    members = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    dgraph = MappedGraph(len(members),
        members,
        is_directed=True)


    dgraph.add_edges_from_touple(
        ('a', ['b', 'c']),
        ('b', ['c', 'd']),
        ('c', ['e', 'f']),
        ('e', 'd'),
        ('f', 'e'),
        ('g', ['a', 'f'])
    )

    graph = dgraph.get_simplified_graph()
    print(dgraph)

    ddfs = TopologicalSort(graph)
    toposort = ddfs.toposort()
    print(list( dgraph.map_ids_to_names(toposort) ))

