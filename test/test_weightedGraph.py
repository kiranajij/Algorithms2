from unittest import TestCase
from WeightedGraph.WeightedGraph import *

g = {
    1: [(2, 1), (3, 2)],
    2: [(1, 1)],
    3: [(1, 2)]
}
wg = WeightedGraph(g)


class TestWeightedGraph(TestCase):
    def test_get_neighbors(self):
        self.assertEqual([2, 3], wg.get_neighbors(1),
                         "Get Neighbors failed")

    def test_get_weights(self):
        self.assertEqual([1, 2], wg.get_weights(1),
                         "get weights failed")

    def test_get_weight(self):
        self.assertEqual(2, wg.get_weight(1, 3),
                         "get weight failed")

    def test_get_min_weighted_pair(self):
        self.assertEqual((2, 1), wg.get_min_weighted_pair(1),
                         "get min weighted pair failed")

    def test_make_edges(self):
        edges = wg.make_edge_list()
        self.assertIn(Edge(1, 2, 1), edges)
        # self.assertNotIn(Edge(2, 1, 1), edges)
