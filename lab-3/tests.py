import unittest

from main import get_cycle


class TestGetCycle(unittest.TestCase):
    def test_non_cycle_graph(self):
        graph = {1: [2, 3], 2: [3], 3: []}
        self.assertFalse(get_cycle(graph))

    def test_cycle_graph(self):
        graph = {1: [2, 3], 2: [3], 3: [1]}
        self.assertEqual([3, 1, 2], get_cycle(graph))

