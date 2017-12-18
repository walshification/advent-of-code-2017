import unittest

from solutions.stream_processing import assess, clean, remove_garbage, valuate


class CleanTests(unittest.TestCase):
    def test_removes_a_negated_character_from_the_stream(self):
        self.assertEqual(clean('{!y}'), '{}')

    def test_removes_does_not_double_remove_double_bangs(self):
        self.assertEqual(clean('{!!}'), '{}')


class RemovegarbageTests(unittest.TestCase):
    def test_removes_empty_garbage_from_stream(self):
        self.assertEqual(remove_garbage('{<>}'), '{}')

    def test_removes_garbage_that_has_all_kinds_of_characters_in_it(self):
        self.assertEqual(remove_garbage('{<asdfawefawefawe>}'), '{}')

    def test_removes_garbage_that_had_curly_brackets_in_it(self):
        self.assertEqual(remove_garbage('{<{}{}{}}{}{}{{{{}}}>}'), '{}')

    def test_removes_garbage_that_is_next_to_other_garbage(self):
        self.assertEqual(remove_garbage('{<><>}'), '{}')


class AssessTests(unittest.TestCase):
    def test_values_a_top_level_group_at_one(self):
        self.assertEqual(assess('{}'), 1)

    def test_adds_one_to_nested_groups(self):
        self.assertEqual(assess('{{}}'), 3)

    def test_asseses_sibling_groups_at_same_generation_rate(self):
        self.assertEqual(assess('{}{}'), 2)

    def test_iterates_over_nested_sibling_groups(self):
        self.assertEqual(assess('{{}{}}'), 5)

    def test_assesses_multigenerational_streams(self):
        self.assertEqual(assess('{{{}{}{{}}}}'), 16)


class ValuateTests(unittest.TestCase):
    def test_survives_some_feature_level_tests(self):
        self.assertEqual(valuate('{{{}}}'), 6)
        self.assertEqual(valuate('{{},{}}'), 5)
        self.assertEqual(valuate('{<a>,<a>,<a>,<a>}'), 1)
        self.assertEqual(valuate('{{<ab>},{<ab>},{<ab>},{<ab>}}'), 9)
        self.assertEqual(valuate('{{<!!>},{<!!>},{<!!>},{<!!>}}'), 9)
        self.assertEqual(valuate('{{<a!>},{<a!>},{<a!>},{<ab>}}'), 3)
