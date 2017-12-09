import unittest

from solutions.circus import Program, Pyramid, Tower


class ProgramTests(unittest.TestCase):
    def test_creates_a_program_with_attributes_from_a_string(self):
        program = Program('asdf (34)')
        self.assertEqual(program.name, 'asdf')
        self.assertEqual(program.weight, 34)

    def test_registers_programs_on_the_program_supporting_them(self):
        program = Program('asdf (34) -> qwer')
        self.assertEqual(program.children, ['qwer'])


class TowerTests(unittest.TestCase):
    def test_build_organizes_programs_into_their_line_by_the_root(self):
        root = Program('asdf (17) -> qwer')
        children = [Program('qwer (12)')]

        tower = Tower.build(root, children)

        expected_line = [root] + children
        self.assertEqual(tower.line, expected_line)

    def test_build_excludes_programs_that_are_not_children_of_the_root(self):
        root = Program('asdf (17) -> qwer')
        child = Program('qwer (12)')
        outsider = Program('foo (12)')

        tower = Tower.build(root, [child, outsider])
        self.assertTrue(outsider not in tower.line)

    def test_supported_weight_sums_the_weight_of_the_tower_above_the_root(self):
        root = Program('asdf (17) -> qwer, foo')
        other_programs = [Program('qwer (12)'), Program('foo (12)')]

        tower = Tower.build(root, other_programs)
        self.assertEqual(tower.supported_weight, 24)

    def test_branches_returns_a_list_of_towers_for_the_root_descendants(self):
        root = Program('asdf (17) -> qwer')
        child = Program('qwer (12)')

        tower = Tower.build(root, [child])
        self.assertEqual(type(tower.branches[0]), Tower)
        self.assertEqual(tower.branches[0].root.name, 'qwer')

    def test_is_balanced_returns_true_if_all_branches_have_the_same_weight(self):
        root = Program('asdf (17) -> qwer, foo')
        children = [Program('qwer (12)'), Program('foo (12)')]

        tower = Tower.build(root, children)
        self.assertTrue(tower.is_balanced)

    def test_is_balanced_returns_false_if_tower_branches_have_different_weights(self):
        root = Program('asdf (17) -> qwer, foo')
        children = [Program('qwer (12)'), Program('foo (13)')]

        tower = Tower.build(root, children)
        self.assertTrue(tower.is_balanced)


class ParentTests(unittest.TestCase):
    def test_init_assigns_parents_to_programs(self):
        pyramid = Pyramid([
            'qwer (12)',
            'asdf (34) -> qwer',
        ])
        self.assertEqual(pyramid.tree['qwer'].parent, 'asdf')

    def test_root_returns_the_bottom_of_the_pyramid(self):
        pyramid = Pyramid([
            'qwer (12)',
            'foo (17) -> asdf',
            'asdf (34) -> qwer',
        ])
        self.assertEqual(pyramid.root.name, 'foo')

    def test_descendants_returns_list_of_child_programs_of_program(self):
        pyramid = Pyramid([
            'qwer (12)',
            'foo (17) -> asdf',
            'asdf (34) -> qwer',
        ])
        children = [pyramid.tree['asdf'], pyramid.tree['qwer']]
        self.assertEqual(pyramid.descendants('foo'), children)

    def test_descendants_returns_list_with_siblings_of_program(self):
        pyramid = Pyramid([
            'qwer (12)',
            'uiop (43)',
            'foo (17) -> asdf, bar',
            'bar (57) -> uiop',
            'asdf (34) -> qwer',
        ])
        children = [
            pyramid.tree['asdf'],
            pyramid.tree['qwer'],
            pyramid.tree['bar'],
            pyramid.tree['uiop'],
        ]
        self.assertEqual(pyramid.descendants('foo'), children)

    # def test_find_unbalanced_program_returns_off_kilter_program(self):
    #     pyramid = Pyramid([
    #         'pbga (66)',
    #         'xhth (57)',
    #         'ebii (61)',
    #         'havc (66)',
    #         'ktlj (57)',
    #         'fwft (72) -> ktlj, cntj, xhth',
    #         'qoyq (66)',
    #         'padx (45) -> pbga, havc, qoyq',
    #         'tknk (41) -> ugml, padx, fwft',
    #         'jptl (61)',
    #         'ugml (68) -> gyxo, ebii, jptl',
    #         'gyxo (61)',
    #         'cntj (57)',
    #     ])
    #     self.assertEqual(Pyramid.find_unbalanced_program(pyramid, pyramid.root), 'ugml')
