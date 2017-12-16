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
    # def test_root_returns_the_bottom_of_the_pyramid(self):
    #     schemas = ['qwer (34)', 'foo (17) -> asdf', 'asdf (34) -> qwer']
    #     pyramid = Pyramid.build(schemas)
    #     self.assertEqual(pyramid.root.name, 'foo')

    # def test_tree_returns_dict_with_stats_of_programs_mapped_to_name(self):
    #     schemas = ['qwer (34)']
    #     pyramid = Pyramid.build(schemas)
    #     self.assertEqual(pyramid.tree['qwer']['weight'], 34)
    #     self.assertEqual(pyramid.tree['qwer']['children'], [])

    # def test_tree_contains_weight_supported_by_program(self):
    #     schemas = ['qwer (34)', 'asdf (42) -> qwer']
    #     pyramid = Pyramid.build(schemas)
    #     self.assertEqual(pyramid.tree['asdf']['supported_weight'], 34)

    # def test_is_balanced_returns_true_if_children_all_weight_the_same(self):
    #     schemas = [
    #         'qwer (34)',
    #         'asdf (42) -> qwer, foo',
    #         'foo (34)',
    #     ]
    #     pyramid = Pyramid.build(schemas)
    #     self.assertTrue(pyramid.is_balanced('asdf'))

    # def test_is_balanced_returns_false_if_children_have_different_weights(self):
    #     schemas = [
    #         'qwer (34)',
    #         'asdf (42) -> qwer, foo',
    #         'foo (35)',
    #     ]
    #     pyramid = Pyramid.build(schemas)
    #     self.assertFalse(pyramid.is_balanced('asdf'))

    # def test_unbalanced_program_returns_root_if_root_is_unbalanced(self):
    #     schemas = [
    #         'qwer (34)',
    #         'asdf (42) -> qwer, foo',
    #         'foo (35)',
    #     ]
    #     pyramid = Pyramid.build(schemas)
    #     self.assertEqual(pyramid.unbalanced_program, 'asdf')

    # def test_unbalanced_program_returns_root_child_if_unbalanced(self):
    #     schemas = [
    #         'qwer (34) -> baz, bar',
    #         'asdf (42) -> qwer, foo',
    #         'foo (34)',
    #         'baz (14)',
    #         'bar (13)'
    #     ]
    #     pyramid = Pyramid.build(schemas)
    #     self.assertEqual(pyramid.unbalanced_program, 'qwer')

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
        self.assertEqual(pyramid.unbalanced_program, 'ugml')
