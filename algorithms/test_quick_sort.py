from unittest import TestCase
from algorithms.ex3_quick_sort import partition, quick_sort, swap_pivot, find_median_pivot


class TestQuickSort(TestCase):
    def test_partition(self):
        A = [2,3,5,1,4,6]
        expected_result = [1, 2, 5, 3, 4, 6]
        expected_pi = 1
        result, pi = partition(A, 0, 6)
        self.assertListEqual(expected_result, result)
        self.assertEqual(expected_pi, pi)

    def test_partition_2(self):
        A = [4, 5, 2, 1, 6, 3]
        expected_result = [3, 2, 1, 4, 6, 5]
        expected_pi = 3
        result, pi = partition(A, 0, 6)
        self.assertListEqual(expected_result, result)
        self.assertEqual(expected_pi, pi)

    def test_quick_sort_base(self):
        A = [1]
        expected_sorted_A = [1]
        expected_evaluations = 0
        sorted_A, evaluations = quick_sort(A)
        self.assertListEqual(expected_sorted_A, sorted_A)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort_empty(self):
        A = []
        expected_sorted_A = []
        expected_evaluations = 0
        sorted_A, evaluations = quick_sort(A)
        self.assertListEqual(expected_sorted_A, sorted_A)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort_small_selection(self):
        A = [4, 5, 2, 1, 6, 3]
        expected_part_sorted_A = [4, 5, 2, 1, 6, 3]
        expected_evaluations = 0
        part_sorted_A, evaluations = quick_sort(A, 0, 1)
        self.assertListEqual(expected_part_sorted_A, part_sorted_A)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort_partial_sort(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_part_sorted_a = [2, 4, 5, 1, 6, 3]
        expected_evaluations = 2
        part_sorted_A, evaluations = quick_sort(a, 0, 3)
        self.assertListEqual(expected_part_sorted_a, part_sorted_A)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort_partial_sort_2(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_part_sorted_a = [4, 1, 2, 5, 6, 3]
        expected_evaluations = 3
        part_sorted_A, evaluations = quick_sort(a, 1, 4)
        self.assertListEqual(expected_part_sorted_a, part_sorted_A)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort_partial_sort_3(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_part_sorted_a = [4, 5, 2, 1, 3, 6]
        part_sorted_a, evaluations = quick_sort(a, 3, 6)
        expected_evaluations = 3
        self.assertListEqual(expected_part_sorted_a, part_sorted_a)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_part_sorted_a = [1, 2, 3, 4, 5, 6]
        expected_evaluations = 9
        part_sorted_a, evaluations = quick_sort(a)
        self.assertListEqual(expected_part_sorted_a, part_sorted_a)
        self.assertEqual(expected_evaluations, evaluations)

    def test_quick_sort_medium(self):
        A = [4, 5, 2, 1, 6, 3, 12, 11, 10, 9, 7, 8]
        expected_part_sorted_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        expected_evaluations = 32
        part_sorted_a, evaluations = quick_sort(A)
        self.assertListEqual(expected_part_sorted_a, part_sorted_a)
        self.assertEqual(expected_evaluations, evaluations)

    def test_swap_pivot(self):
        a = [4, 5, 2, 1, 6, 3]
        l = 0
        r = 6
        mode = 'last'
        expected_a = [3, 5, 2, 1, 6, 4]
        new_a = swap_pivot(a, l, r, mode)
        self.assertListEqual(expected_a, new_a)

    def test_swap_pivot_2(self):
        a = [4, 5, 2, 1, 6, 3]
        l = 1
        r = 5
        mode = 'last'
        expected_a = [4, 6, 2, 1, 5, 3]
        new_a = swap_pivot(a, l, r, mode)
        self.assertListEqual(expected_a, new_a)

    def test_swap_pivot_first(self):
        a = [4, 5, 2, 1, 6, 3]
        l = 1
        r = 5
        mode = 'first'
        expected_a = [4, 5, 2, 1, 6, 3]
        new_a = swap_pivot(a, l, r, mode)
        self.assertListEqual(expected_a, new_a)

    def test_swap_pivot_exception(self):
        a = [4, 5, 2, 1, 6, 3]
        l = 1
        r = 5
        mode = 'rand'
        with self.assertRaises(ValueError):
            swap_pivot(a, l, r, mode)

    def test_quick_sort_last(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_part_sorted_a = [1, 2, 3, 4, 5, 6]
        expected_evaluations = 9
        part_sorted_a, evaluations = quick_sort(a, pivot_mode='last')
        self.assertListEqual(expected_part_sorted_a, part_sorted_a)
        self.assertEqual(expected_evaluations, evaluations)

    def test_find_median_pivot(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_pivot = 3
        expected_index = 6
        pivot, index = find_median_pivot(a)
        self.assertEqual(expected_pivot, pivot)
        self.assertEqual(expected_index, index)

    def test_find_median_pivot(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_pivot = 3
        expected_index = 5
        pivot, index = find_median_pivot(a, 0, 6)
        self.assertEqual(expected_pivot, pivot)
        self.assertEqual(expected_index, index)

    def test_find_median_pivot_2(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_pivot = 2
        expected_index = 2
        pivot, index = find_median_pivot(a, 1, 4)
        self.assertEqual(expected_pivot, pivot)
        self.assertEqual(expected_index, index)

    def test_find_median_pivot_3(self):
        a = [4, 5, 2, 1, 6, 3, 7]
        expected_pivot = 4
        expected_index = 0
        pivot, index = find_median_pivot(a, 0, 7)
        self.assertEqual(expected_pivot, pivot)
        self.assertEqual(expected_index, index)

    def test_swap_pivot(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_a = [3, 5, 2, 1, 6, 4]
        swapped_a = swap_pivot(a, 0, 6, mode='median')
        self.assertListEqual(expected_a, swapped_a)

    def test_swap_pivot_2(self):
        a = [4, 5, 2, 1, 6, 3]
        expected_a = [4, 2, 5, 1, 6, 3]
        swapped_a = swap_pivot(a, 1, 4, mode='median')
        self.assertListEqual(expected_a, swapped_a)

    def test_swap_pivot_3(self):
        a = [4, 5, 2, 1, 6, 3, 7]
        expected_a = [4, 5, 2, 1, 6, 3, 7]
        swapped_a = swap_pivot(a, 0, 7, mode='median')
        self.assertListEqual(expected_a, swapped_a)


