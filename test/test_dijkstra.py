from unittest import TestCase
from test.test_prim import wg
from WeightedGraph.Dijkstra import Dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra(self):
        dj = Dijkstra(wg)
        self.assertEqual([1, 3, 6, 7],
                         dj.dijkstra(1, 7),
                         "1-7 failed")
        self.assertEqual([4, 6, 7],
                         dj.dijkstra(4, 7),
                         "So it doesn't work")
        self.assertEqual([2, 5, 6],
                         dj.dijkstra(2, 6),
                         "2-6 failed")
        self.assertEqual([4, 3, 5],
                         dj.dijkstra(4, 5),
                         "4-5 failed")
