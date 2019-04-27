import unittest
from unittest import TestCase
from CombinationalSearch.SearchDfs import Subsets


class TestSubsets(TestCase):

    @unittest.skip
    def test_is_solution(self):
        self.fail()

    def test_run(self):
        f = Subsets(4)
        f._run(0)