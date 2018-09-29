from unittest import TestCase
from algorithms.dijkstra import shortest_path


class TestShortestPath(TestCase):
    def test_shortest_path(self):
        graph = [[(2, 10), (3, 30), (5, 60)],
                 [(1, 10), (4, 20)],
                 [(1, 30), (4, 40)],
                 [(3, 40), (2, 20), (5, 50)],
                 [(1, 60), (4, 50)]]
        start_vertex = 1
        expected_spath = [0, 10, 30, 30, 60]
        spath = shortest_path(graph, start_vertex)
        self.assertListEqual(expected_spath, spath)
