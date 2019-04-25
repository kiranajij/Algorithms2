from unittest import TestCase

from bfs import Graph
from dfs import *
from graphs import *


class TestDfsDirected(TestCase):
    def test_topo_sort(self):
        t = TopoSort(Graph(gTopoSort, 7))
        self.assertEqual([7, 1, 2, 3, 6, 5, 4], t.topo_sort(), "Sorting is incorrect")

    def test_classification(self):
        g = Graph(gTopoSort, 7)
        dg = TopoSort(g)
        dg.initialize_search()
        dg.topo_sort()
        self.assertEqual(dg.classify_edge(1, 2), dg.TREE_EDGE,
                         "Not a tree edge (1, 2)")
        self.assertEqual(dg.FORWARD_EDGE, dg.classify_edge(1, 3))
        self.assertEqual(dg.classify_edge(7, 1), dg.CROSS_EDGE,
                         "Not a tree edge (7, 1)")

    def test_topo_sort_2(self):
        g = Graph(gProblem_topo, 9)
        dg = TopoSort(g)
        dg.initialize_search()
        r = dg.topo_sort()
        print(r)
        self.assertIsNotNone(r)
