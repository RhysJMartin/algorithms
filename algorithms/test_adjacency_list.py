from unittest import TestCase
from algorithms.ex_4_random_contraction import AdjacencyList


class TestAdjacencyList(TestCase):

    def test_init_adjacency_list(self):
        simple_data = [[1, 2, 3, 4], [2, 1, 4], [3, 1, 4], [4, 1, 2, 3]]
        expected_vertices = [{0, 1, 2}, {0, 3}, {1, 4}, {2, 3, 4}]
        expected_edges = [[1, 2], [1, 3], [1, 4], [2, 4], [3, 4]]
        vertices, edges = AdjacencyList.init_adjacency_list(simple_data)
        self.assertListEqual(expected_vertices, vertices)
        self.assertListEqual(expected_edges, edges)

    def test_random_selection(self):
        simple_data = [[1, 2, 3, 4], [2, 1, 4], [3, 1, 4], [4, 1, 2, 3]]
        expected_edge = 3
        al = AdjacencyList(simple_data, 0)
        edge = al.select_edge()
        self.assertEqual(expected_edge, edge)

    def test_contraction(self):
        simple_data = [[1, 2, 3, 4], [2, 1, 4], [3, 1, 4], [4, 1, 2, 3]]
        # Random seed 5 results in random.randint(0,5) = 4
        expected_vertices = [{0, 1, 2}, {0, 3}, {1, 2, 3}, set([])]
        expected_edges = [[1, 2], [1, 3], [1, 3], [2, 3], []]
        al = AdjacencyList(simple_data, 5)
        al.contraction()
        self.assertListEqual(expected_vertices, al.vertices)
        self.assertListEqual(expected_edges, al.edges)

    def test_contraction_second_step(self):
        simple_data = [[1, 2, 3, 4], [2, 1, 4], [3, 1, 4], [4, 1, 2, 3]]
        # Random seed = 5 results in random.randint(0,5) = 4 -> random.randint(0,4) = 2
        expected_vertices = [{0, 3}, {0, 3}, set([]), set([])]
        expected_edges = [[1, 2], [], [], [2, 1], []]
        al = AdjacencyList(simple_data, 5)
        al.contraction()
        al.contraction()
        self.assertListEqual(expected_vertices, al.vertices)
        self.assertListEqual(expected_edges, al.edges)

    def test_run(self):
        simple_data = [[1, 2, 3, 4], [2, 1, 4], [3, 1, 4], [4, 1, 2, 3]]
        expected_min_cut = 2
        al = AdjacencyList(simple_data, 5)
        min_cut = al.estimate_min_cut()
        self.assertEqual(expected_min_cut, min_cut)




