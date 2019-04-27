import unittest
from unittest import TestCase

from WeightedGraph.UnionFind import UnionFind


class TestUnionFind(TestCase):

    def setUp(self) -> None:
        self.uf = UnionFind(10)

    def test_find(self):
        self.assertEqual(3, self.uf.find(3),
                         "find")
        self.uf.union_sets(1, 2)
        self.uf.union_sets(4, 2)
        self.assertEqual(1, self.uf.find(4),
                         "union_set")
        self.assertEqual(True, self.uf.is_same_component(2, 4),
                         "same component")

    @unittest.skip
    def test_union_sets(self):
        self.fail()

    @unittest.skip
    def test_is_same_component(self):
        self.fail()