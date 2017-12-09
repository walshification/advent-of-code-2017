import unittest

from solutions.circus import Pyramid


class PyramidTests(unittest.TestCase):
    def test_creates_a_dictionary_structure_out_of_input(self):
        pyramid = Pyramid(['asdf (34)'])
        self.assertEqual(pyramid.get('asdf')['name'], 'asdf')
        self.assertEqual(pyramid.get('asdf')['weight'], 34)

    def test_registers_programs_on_the_program_supporting_them(self):
        pyramid = Pyramid([
            'qwer (12)',
            'asdf (34) -> qwer',
        ])
        self.assertEqual(pyramid.get('asdf')['supports'], ['qwer'])


class ParentTests(unittest.TestCase):
    def test_parent_returns_the_list_of_parent_of_a_program(self):
        pyramid = Pyramid([
            'qwer (12)',
            'asdf (34) -> qwer',
        ])
        self.assertEqual(pyramid.parent('qwer')['name'], 'asdf')

    def test_root_returns_the_bottom_of_the_pyramid(self):
        pyramid = Pyramid([
            'qwer (12)',
            'foo (17) -> asdf',
            'asdf (34) -> qwer',
        ])
        self.assertEqual(pyramid.root, 'foo')
