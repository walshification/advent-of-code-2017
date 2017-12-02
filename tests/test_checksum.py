import unittest

from solutions import checksum


class ChecksumTests(unittest.TestCase):
    def test_sums_repeating_number_pairs(self):
        test_spreadsheet = [
            [5, 1, 9, 5],
            [7, 5, 3, None],
            [2, 4, 6, 8]
        ]
        solution = checksum.calculate(test_spreadsheet)
        self.assertEqual(solution, 18)
