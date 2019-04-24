from unittest import TestCase

from bfs import Graph
from dfs import *
from graphs import *


class TestDfsDirected(TestCase):
    def test_topo_sort(self):
        t = TopoSort(Graph(gTopoSort, 7))
        self.assertEqual([7, 1, 2, 3, 6, 5, 4], t.topo_sort(), "Sorting is incorrect")

    def test_classification(self):
        self.fail()