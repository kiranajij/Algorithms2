from graph import WeightedGraph
import numpy as np
import pdb


def minimum_spanning_tree(graph, start):
    
    if not isinstance(graph, WeightedGraph):
        raise TypeError("Must be of type WeightedGraph")

    n = graph.n

    # Initialize the requried attributes
    parents = np.full((n, ), -1)
    is_in_tree = np.full((n, ), False)
    cost_in_adding = np.full((n, ), np.inf)

    # Add the start element
    is_in_tree[start] = True
    for node, weight in graph.get_neighbors(start):
        cost_in_adding[node] = weight
        parents[node] = start

    # pdb.set_trace()

    while True:

        min_cost = np.inf
        next_node = None

        # Find the next minimum cost
        for node, weight in enumerate(cost_in_adding):
            if weight < min_cost and not is_in_tree[node]:
                next_node = node
                min_cost = weight
        if next_node is None:
            break

        # add the node to the spanning tree
        parent = parents[next_node]
        print((parent, next_node))

        # update the costs of adding it to the tree
        for node, weight in graph.get_neighbors(next_node):
            if weight < cost_in_adding[node] and not is_in_tree[node]:
                cost_in_adding[node] = weight
                parents[node] = next_node

        is_in_tree[next_node] = True
    return parents


if __name__ == '__main__':
    graph = WeightedGraph(7)
    graph.add_edges(0, [1, 6, 5], [5, 7, 12])
    graph.add_edges(1, [2, 6], [7, 9])
    graph.add_edges(2, [3, 4, 6], [5, 2, 4])
    graph.add_edge(3, 4, 2)
    graph.add_edges(4, [6, 5], [3, 7])
    graph.add_edge(5, 6, 4)
    print(graph)

    parents  = minimum_spanning_tree(graph, 0)
    print(parents)