from unittest import TestCase

from WeightedGraph.Sort.quicksort import swap, partition, quicksort


class TestPartition(TestCase):
    def test_partition(self):
        l = [5, 4, 3, 2, 1]
        partition(l, 0, 4)
        self.assertEqual([2, 1, 3, 5, 4], l)
        # self.assertEqual([1, 3, 4, 5, 7, 6],
        #                  partition([1, 3,5, 4, 7, 6], 0, 2, 5))

    def test_swap(self):
        l = [1, 3, 2]
        swap(l, 1, 2)
        self.assertEqual([1, 2, 3], l)

    def test_quicksort(self):
        l = [1, 3, 2]
        quicksort(l, 0, 2)
        self.assertEqual([1, 2, 3], l)
        l = [1, 4, 3, 5, 3, 6, 1, 2, 4]
        tl = l[::]
        tl.sort()
        quicksort(l, 0, len(l)-1)

        self.assertEqual(l, tl)
