import unittest

from solutions import captcha


class CaptchaTests(unittest.TestCase):
    def test_sums_repeating_number_pairs(self):
        solution = captcha.solve(1122)
        self.assertEqual(solution, 3)

    def test_sums_overlapping_repeating_pairs(self):
        solution = captcha.solve(1111)
        self.assertEqual(solution, 4)

    def test_skips_pairs_that_do_not_match(self):
        solution = captcha.solve(1234)
        self.assertEqual(solution, 0)

    def test_counts_last_digit_if_it_matches_the_first(self):
        solution = captcha.solve(91212129)
        self.assertEqual(solution, 9)
