import unittest

from solutions.circus import Program, Pyramid


class ProgramTests(unittest.TestCase):
    def test_creates_a_program_with_attributes_from_a_string(self):
        program = Program('asdf (34)')
        self.assertEqual(program.name, 'asdf')
        self.assertEqual(program.weight, 34)

    def test_registers_programs_on_the_program_supporting_them(self):
        program = Program('asdf (34) -> qwer')
        self.assertEqual(program.children, ['qwer'])


class ParentTests(unittest.TestCase):
    def test_root_returns_the_bottom_of_the_pyramid(self):
        schemas = ['qwer (34)', 'foo (17) -> asdf', 'asdf (34) -> qwer']
        pyramid = Pyramid.build(schemas)
        self.assertEqual(pyramid.root.name, 'foo')

    def test_programs_are_updated_with_weight_supported_by_program(self):
        schemas = ['qwer (34)', 'asdf (42) -> qwer']
        pyramid = Pyramid.build(schemas)
        self.assertEqual(pyramid.programs['asdf'].total_weight, 76)

    def test_is_balanced_returns_true_if_children_all_weigh_the_same(self):
        schemas = [
            'qwer (34)',
            'asdf (42) -> qwer, foo',
            'foo (34)',
        ]
        pyramid = Pyramid.build(schemas)
        self.assertTrue(pyramid.is_balanced('asdf'))

    def test_is_balanced_returns_false_if_children_have_different_weights(self):
        schemas = [
            'qwer (34)',
            'asdf (42) -> qwer, foo',
            'foo (35)',
        ]
        pyramid = Pyramid.build(schemas)
        self.assertFalse(pyramid.is_balanced('asdf'))

    def test_unbalanced_program_returns_root_if_root_is_unbalanced(self):
        schemas = [
            'qwer (34)',
            'asdf (42) -> qwer, foo',
            'foo (35)',
        ]
        pyramid = Pyramid.build(schemas)
        self.assertEqual(pyramid.unbalanced_program.name, 'asdf')

    def test_unbalanced_program_returns_root_child_if_unbalanced(self):
        schemas = [
            'qwer (34) -> baz, bar',
            'asdf (42) -> qwer, foo',
            'foo (47)',
            'baz (14)',
            'bar (13)'
        ]
        pyramid = Pyramid.build(schemas)
        self.assertEqual(pyramid.unbalanced_program.name, 'qwer')

    def test_find_unbalanced_program_returns_off_kilter_program(self):
        schemas = [
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)',
        ]
        pyramid = Pyramid.build(schemas)
        self.assertEqual(pyramid.unbalanced_program.name, 'ugml')

    def test_weight_to_balance_returns_weight_corrected_for_children(self):
        schemas = [
            'pbga (66)',
            'xhth (57)',
            'ebii (61)',
            'havc (66)',
            'ktlj (57)',
            'fwft (72) -> ktlj, cntj, xhth',
            'qoyq (66)',
            'padx (45) -> pbga, havc, qoyq',
            'tknk (41) -> ugml, padx, fwft',
            'jptl (61)',
            'ugml (68) -> gyxo, ebii, jptl',
            'gyxo (61)',
            'cntj (57)',
        ]
        pyramid = Pyramid.build(schemas)
        self.assertEqual(pyramid.weight_to_balance, 60)
