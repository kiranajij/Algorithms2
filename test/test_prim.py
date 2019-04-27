from unittest import TestCase

from WeightedGraph import *

g = {
    1: [(2, 5), (3, 7), (4, 12)],
    2: [(1, 5), (3, 9), (5, 7)],
    3: [(1, 7), (2, 9), (4, 4), (5, 4), (6, 3)],
    4: [(1, 12), (3, 4), (6, 7)],
    5: [(2, 7), (3, 4), (6, 2), (7, 5)],
    6: [(3, 3), (4, 7), (5, 2), (7, 2)],
    7: [(5, 5), (6, 2)]
}

wg = WeightedGraph(g)


class TestPrim(TestCase):
    def test_prim(self):
        pr = Prim(wg)
        pr.initialize()
        pr.prim(1)
        self.assertEqual(6, pr.parents[7],
                         "Parent of 7 is not 6")

