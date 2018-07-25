from unittest import TestCase
from algorithms.maintaining_median import Median


class TestMedian(TestCase):
    def test_median(self):
        sequence = [5, 20, 10, 9]
        expected_medians = [5, 5, 10, 9]
        median = Median()
        medians = [median.add(x) for x in sequence]
        self.assertListEqual(expected_medians, medians)

    def test_median_increasing(self):
        # test rebalance from high to low
        sequence = [1, 2, 3, 4]
        expected_medians = [1, 1, 2, 2]
        median = Median()
        medians = [median.add(x) for x in sequence]
        self.assertListEqual(expected_medians, medians)

    def test_median_decreasing(self):
        # test rebalance low to high
        sequence = [4, 3, 2, 1]
        expected_medians = [4, 3, 3, 2]
        median = Median()
        medians = [median.add(x) for x in sequence]
        self.assertListEqual(expected_medians, medians)
