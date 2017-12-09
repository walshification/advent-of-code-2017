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
        self.assertEqual(pyramid.root, 'foo')
