import unittest
from unittest import TestCase
from CombinationalSearch.SearchDfs import Subsets, Permutations


class TestSubsets(TestCase):

    @unittest.skip
    def test_is_solution(self):
        self.fail()

    def test_run(self):
        f = Subsets(4)
        f.run()


class TestPermutations(TestCase):
    def test_run(self):
        tr = Permutations(3)
        tr.run()