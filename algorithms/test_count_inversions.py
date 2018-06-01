from unittest import TestCase
from algorithms.ex2_inversions import sort_and_count, merge_and_count_split_inv, split


class TestCountInversions(TestCase):

    def test_sort_and_count_base(self):
        x = [3]
        expected_sorted_x = [3]
        exptected_inverstions = 0
        sorted_x, inversions = sort_and_count(x)
        self.assertListEqual(expected_sorted_x, sorted_x)
        self.assertEqual(exptected_inverstions, inversions)

    def test_merge_and_count_split_inv(self):
        a = [1, 3, 5]
        b = [2, 4, 6]
        expected_list = [1, 2, 3, 4, 5, 6]
        expected_inversions = 3
        sorted_list, inversions = merge_and_count_split_inv(a, b)
        self.assertListEqual(expected_list, sorted_list)
        self.assertEqual(expected_inversions, inversions)

    def test_split(self):
        input = [1,2,3]
        expected_a = [1]
        expected_b = [2,3]
        a, b = split(input)
        self.assertListEqual(expected_a, a)
        self.assertListEqual(expected_b, b)

    def test_sort_and_count_small_inverted(self):
        x = [6, 5, 4, 3, 2, 1]
        expeected_sorted_x = [1, 2, 3, 4, 5, 6]
        expected_count = 15
        sorted_x, count = sort_and_count(x)
        self.assertListEqual(expeected_sorted_x, sorted_x)
        self.assertEqual(expected_count, count)

    def test_sort_and_count_medium(self):
        x = [1, 2, 3, 4, 12, 11, 5, 6, 7, 8, 10, 9]
        expeected_sorted_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        expected_count = 14
        sorted_x, count = sort_and_count(x)
        self.assertListEqual(expeected_sorted_x, sorted_x)
        self.assertEqual(expected_count, count)


