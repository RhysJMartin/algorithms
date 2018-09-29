from unittest import TestCase
from algorithms.find_sums import count_2_sums


class TestCount2Sums(TestCase):
    def test_count_2_sums(self):
        data = [20, -17, 1, -2, 5, 100, 200]
        interval = [-3, 3]
        expected_sums = 2
        sums = count_2_sums(data, interval)
        self.assertEqual(expected_sums, sums)

    def test_count_2_sums_mentor_example(self):
        data = [-3, -1, 1, 2, 9, 11, 7, 6, 2]
        interval = [3, 10]
        expected_sums = 8
        sums = count_2_sums(data, interval)
        self.assertEqual(expected_sums, sums)

    def test_count_2_sums_mentor_example_2(self):
        data = [-2, 0, 0, 4]
        interval = [0, 4]
        expected_sums = 2
        sums = count_2_sums(data, interval)
        self.assertEqual(expected_sums, sums)

    def test_count_2_sums_mentor_example_3(self):
        data = [1, 2, 3, 4, 5, 6]
        interval = [3, 4]
        expected_sums = 2
        sums = count_2_sums(data, interval)
        self.assertEqual(expected_sums, sums)

    def test_count_2_sums_mentor_example_4(self):
        data = [1, 2, 3, 4, 5, 6]
        interval = [30, 40]
        expected_sums = 0
        sums = count_2_sums(data, interval)
        self.assertEqual(expected_sums, sums)

