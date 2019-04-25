from unittest import TestCase

from WeightedGraph import *
from test.test_prim import wg


class TestKruskal(TestCase):
    def test_kruskal(self):
        kr = Kruskal(wg)
        uf = kr.kruskal()

        print(uf)
        # self.assertIsInstance(uf, UnionFind)
