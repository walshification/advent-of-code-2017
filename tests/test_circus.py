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
    def test_init_assigns_parents_to_programs(self):
        pyramid = Pyramid([
            'qwer (12)',
            'asdf (34) -> qwer',
        ])
        self.assertEqual(pyramid.tower['qwer'].parent, 'asdf')

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
        children = [pyramid.tower['asdf'], pyramid.tower['qwer']]
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
            pyramid.tower['asdf'],
            pyramid.tower['qwer'],
            pyramid.tower['bar'],
            pyramid.tower['uiop'],
        ]
        self.assertEqual(pyramid.descendants('foo'), children)

    def test_find_unbalanced_program_returns_off_kilter_program(self):
        pyramid = Pyramid([
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
        ])
        self.assertEqual(Pyramid.find_unbalanced_program(pyramid, pyramid.root), 'ugml')
