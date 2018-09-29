from unittest import TestCase
from algorithms.ex1_karatsuba import multiply, split, number_of_digits, combine, calculate_right_digits


class TestMultiply(TestCase):

    def test_multiply_small(self):
        x = 4
        y = 5
        expected_result = 20
        result = multiply(x, y)
        self.assertEqual(expected_result, result)

    def test_multiply_medium(self):
        x = 44
        y = 55
        expected_result = 2420
        result = multiply(x, y)
        self.assertEqual(expected_result, result)

    def test_multiply_large(self):
        x = 4444
        y = 5555
        expected_result = 24686420
        result = multiply(x, y)
        self.assertEqual(expected_result, result)

    def test_split(self):
        x = 1234
        m = 2
        expected_a = 12
        expected_b = 34
        a, b = split(x, m)
        self.assertEqual(expected_a, a)
        self.assertEqual(expected_b, b)

    def test_split_small(self):
        x = 2
        m = 1
        expected_a = 0
        expected_b = 2
        a, b = split(x, m)
        self.assertEqual(expected_a, a)
        self.assertEqual(expected_b, b)

    def test_number_of_digits(self):
        x = 12
        expected_result = 2
        result = number_of_digits(x)
        self.assertEqual(expected_result, result)

    def test_number_of_digits(self):
        x = 2
        expected_result = 1
        result = number_of_digits(x)
        self.assertEqual(expected_result, result)

    def test_number_of_digits(self):
        x = -1
        self.assertRaises(ValueError, number_of_digits, x)

    def test_combine(self):
        a = 1
        b = 2
        c = 3
        d = 4
        expected_result = 408
        result = combine(a, b, c, d, 1)
        self.assertEqual(expected_result, result)

    def test_combine_uneven_digits(self):
        a = 0
        b = 2
        c = 3
        d = 4
        expected_result = 68
        result = combine(a, b, c, d, 1)
        self.assertEqual(expected_result, result)

    def test_combine_medium(self):
        a = 10
        b = 12
        c = 65
        d = 69
        expected_result = 6647828
        result = combine(a, b, c, d, 2)
        self.assertEqual(expected_result, result)

    def test_combine_large(self):
        a = 100
        b = 122
        c = 654
        d = 696
        expected_result = 65549472912
        result = combine(a, b, c, d, 3)
        self.assertEqual(expected_result, result)

    def test_right_digits(self):
        x = 134
        y = 24
        expected_right_digits = 1
        right_digits = calculate_right_digits(x, y)
        self.assertEqual(expected_right_digits, right_digits)

    def test_right_digits_medium(self):
        x = 1340
        y = 24222
        expected_right_digits = 2
        right_digits = calculate_right_digits(x, y)
        self.assertEqual(expected_right_digits, right_digits)



