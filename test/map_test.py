import unittest

from core.map import Map


class MyTestCase(unittest.TestCase):
    def test_empty_map(self):
        edges = {}

        map = Map(edges)
        next = map.next("A")

        self.assertIsNone(next)

    def test_no_route(self):
        edges = {
            "A": []
        }

        map = Map(edges)
        next = map.next("A", "no end")

        self.assertIsNone(next)

    def test_short_route(self):
        edges = {
            "A": ["B"],
            "B": []
        }

        map = Map(edges)
        next = map.next("A", "B")

        self.assertEqual("B", next)

    def test_long_route(self):
        edges = {
            "A": ["B"],
            "B": ["C"],
            "C": []
        }

        map = Map(edges)
        next = map.next("A", "C")

        self.assertEqual("B", next)

    def test_multiple_routes(self):
        edges = {
            "A": ["B","C"],
            "B": ["D"],
            "C": ["D"],
            "D": []
        }

        map = Map(edges)
        next = map.next("A", "D")

        self.assertEqual("B", next)

    def test_circle(self):
        edges = {
            "A": ["B"],
            "B": ["A"]
        }

        map = Map(edges)
        next = map.next("A", "B")

        self.assertEqual("B", next)


if __name__ == '__main__':
    unittest.main()
