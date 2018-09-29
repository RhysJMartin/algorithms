from unittest import TestCase
from algorithms.graph_search_iterative import create_graph, dfs, dfs_loop, find_scc


class TestGraphSearchIterative(TestCase):

    def test_create_graph(self):
        graph_definition = [[1, 2], [2, 3], [3, 1]]
        num_vertices = 3
        direction = 'forward'
        expected_graph = [[1], [2], [0]]
        graph = create_graph(graph_definition, num_vertices, direction)
        self.assertListEqual(expected_graph, graph)

    def test_create_graph(self):
        graph_definition = [[1, 2], [2, 3], [3, 1]]
        num_vertices = 3
        direction = 'reverse'
        expected_graph = [[2], [0], [1]]
        graph = create_graph(graph_definition, num_vertices, direction)
        self.assertListEqual(expected_graph, graph)

    def test_finish_order(self):
        graph_definition = [[1, 2], [2, 3], [2, 4], [3, 1], [4, 5], [5, 1]]
        num_vertices = 5
        direction = 'forward'
        graph = create_graph(graph_definition, num_vertices, direction)
        expected_finish_order = [4, 3, 2, 1, 0]
        visited, finish_order, visited_together = dfs(graph, 0)
        self.assertListEqual(expected_finish_order, finish_order)

    def test_finish_order_reversed(self):
        graph_definition = [[1, 2], [2, 3], [2, 4], [3, 1], [4, 5], [5, 1]]
        num_vertices = 5
        direction = 'reverse'
        graph = create_graph(graph_definition, num_vertices, direction)
        expected_finish_order = [1, 3, 4, 2, 0]
        visited, finish_order, visited_together = dfs(graph, 0)
        self.assertListEqual(expected_finish_order, finish_order)

    def test_dfs_loop(self):
        graph_definition = [[1, 2], [2, 3], [3, 1], [2, 4], [4, 5], [5, 6], [6, 4]]
        num_vertices = 6
        direction = 'forward'
        graph = create_graph(graph_definition, num_vertices, direction)
        finish_order, component_sizes = dfs_loop(graph, range(num_vertices))
        expected_finish_order = [5, 4, 3, 2, 1, 0]
        expected_component_sizes = [6, 0, 0, 0, 0, 0]
        self.assertListEqual(expected_finish_order, finish_order)
        self.assertListEqual(expected_component_sizes, component_sizes)

    def test_dfs_loop(self):
        graph_definition = [[1, 2], [2, 3], [3, 1], [2, 4], [4, 5], [5, 6], [6, 4]]
        num_vertices = 6
        direction = 'forward'
        graph = create_graph(graph_definition, num_vertices, direction)
        finish_order, component_sizes = dfs_loop(graph, [4, 3, 2, 1, 0, 5])
        expected_finish_order = [3, 5, 4, 1, 0, 2]
        expected_component_sizes = [3, 0, 3, 0, 0, 0]
        self.assertListEqual(expected_finish_order, finish_order)
        self.assertListEqual(expected_component_sizes, component_sizes)

    def test_find_scc(self):
        graph_definition = [[1, 2], [2, 3], [3, 1], [2, 4], [4, 5], [5, 6], [6, 4]]
        num_vertices = 6
        scc_sizes = find_scc(graph_definition, num_vertices)
        expected_scc_sizes = [3, 3, 0, 0, 0]
        self.assertListEqual(expected_scc_sizes, scc_sizes)
