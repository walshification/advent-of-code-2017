import unittest

from solutions.stream_processing import assess, clean


class CleanTests(unittest.TestCase):
    def test_removes_a_negated_character_from_the_stream(self):
        self.assertEqual(clean('{!y}'), '{}')

    def test_removes_does_not_double_remove_double_bangs(self):
        self.assertEqual(clean('{!!}'), '{}')


class AssessTests(unittest.TestCase):
    def test_values_a_top_level_group_at_one(self):
        self.assertEqual(assess('{}'), 1)

    def test_adds_one_to_nested_groups(self):
        self.assertEqual(assess('{{}}'), 3)

    def test_asseses_sibling_groups_at_same_generation_rate(self):
        self.assertEqual(assess('{},{}'), 2)

    def test_iterates_over_nested_sibling_groups(self):
        self.assertEqual(assess('{{},{}}'), 5)

    def test_assesses_multigenerational_streams(self):
        self.assertEqual(assess('{{{},{},{{}}}}'), 16)
