import unittest

from solutions.stream_processing import valuate


class AssessTests(unittest.TestCase):
    def test_values_a_top_level_group_at_one(self):
        self.assertEqual(valuate('{}'), 1)

    def test_adds_one_to_nested_groups(self):
        self.assertEqual(valuate('{{}}'), 3)

    def test_asseses_sibling_groups_at_same_generation_rate(self):
        self.assertEqual(valuate('{},{}'), 2)

    def test_iterates_over_nested_sibling_groups(self):
        self.assertEqual(valuate('{{},{}}'), 5)

    def test_assesses_multigenerational_streams(self):
        self.assertEqual(valuate('{{{},{},{{}}}}'), 16)
