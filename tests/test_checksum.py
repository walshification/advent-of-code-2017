import unittest

from solutions.checksum import calculate, max_min_difference, even_divisor_difference


class CalculateTests(unittest.TestCase):
    def test_calculates_checksum_from_min_max_difference_in_rows(self):
        test_spreadsheet = [
            [5, 1, 9, 5],
            [7, 5, 3, None],
            [2, 4, 6, 8]
        ]
        solution = calculate(test_spreadsheet, max_min_difference)
        self.assertEqual(solution, 18)

    def test_calculates_checksum_from_even_divisor_difference_in_rows(self):
        test_spreadsheet = [
            [5, 9, 2, 8],
            [9, 4, 7, 3],
            [3, 8, 6, 5],
        ]
        solution = calculate(test_spreadsheet, even_divisor_difference)
        self.assertEqual(solution, 9)


class EvenDivisorTests(unittest.TestCase):
    def test_even_divisor_divides_two_digits_if_they_divide_evenly(self):
        quotient = even_divisor_difference([12, 6])
        self.assertEqual(quotient, 2)

    def test_even_divisor_skips_numbers_that_dont_evenly_divide(self):
        quotient = even_divisor_difference([18, 7, 5, 9])
        self.assertEqual(quotient, 2)
