import unittest

from solutions import captcha


class CaptchaTests(unittest.TestCase):
    def test_sums_repeating_number_pairs(self):
        solution = captcha.solve(1122)
        self.assertEqual(solution, 3)
