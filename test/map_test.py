import unittest

from sandbox.location.map import Map


class MyTestCase(unittest.TestCase):
    def test_empty_map(self):
        edges = {}

        world_map = Map(edges)
        next_node = world_map.next("A", "B")

        self.assertIsNone(next_node)

    def test_no_route(self):
        edges = {"A": []}

        world_map = Map(edges)
        next_node = world_map.next("A", "no end")

        self.assertIsNone(next_node)

    def test_short_route(self):
        edges = {"A": ["B"], "B": []}

        world_map = Map(edges)
        next_node = world_map.next("A", "B")

        self.assertEqual("B", next_node)

    def test_long_route(self):
        edges = {"A": ["B"], "B": ["C"], "C": []}

        world_map = Map(edges)
        next_node = world_map.next("A", "C")

        self.assertEqual("B", next_node)

    def test_multiple_equal_routes(self):
        edges = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": []}

        world_map = Map(edges)
        next_node = world_map.next("A", "D")

        self.assertEqual("C", next_node)

    def test_multiple_different_length_routes(self):
        edges = {"A": ["B", "C"], "B": ["E"], "C": ["D"], "D": ["E"], "E": []}

        world_map = Map(edges)

        next_node = world_map.next("A", "E")

        self.assertEqual("B", next_node)

    def test_circle(self):
        edges = {"A": ["B"], "B": ["A"]}

        world_map = Map(edges)
        next_node = world_map.next("A", "B")

        self.assertEqual("B", next_node)


if __name__ == "__main__":
    unittest.main()
