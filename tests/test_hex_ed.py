import unittest

from solutions.hex_ed import Walker


class WalkerTests(unittest.TestCase):
    def test_starts_at_the_origin(self):
        walker = Walker()
        self.assertEqual(walker.coordinates, (0, 0, 0))

    def test_moves_north(self):
        walker = Walker()
        walker.move('n')
        self.assertEqual(walker.coordinates, (0, 1, -1))

    def test_moves_northwest(self):
        walker = Walker()
        walker.move('nw')
        self.assertEqual(walker.coordinates, (-1, 1, 0))

    def test_moves_southwest(self):
        walker = Walker()
        walker.move('sw')
        self.assertEqual(walker.coordinates, (-1, 0, 1))

    def test_moves_south(self):
        walker = Walker()
        walker.move('s')
        self.assertEqual(walker.coordinates, (0, -1, 1))

    def test_moves_southeast(self):
        walker = Walker()
        walker.move('se')
        self.assertEqual(walker.coordinates, (1, -1, 0))

    def test_moves_northeast(self):
        walker = Walker()
        walker.move('ne')
        self.assertEqual(walker.coordinates, (1, 0, -1))

    def test_advances_with_a_list_of_moves(self):
        walker = Walker()
        walker.advance(['s', 's'])
        self.assertEqual(walker.coordinates, (0, -2, 2))

    def test_knows_how_far_from_the_origin_it_is(self):
        walker = Walker()
        walker.advance(['s', 's'])
        self.assertEqual(walker.distance_from_origin, 2)

    def test_knows_how_far_on_a_diagonal(self):
        walker = Walker()
        walker.advance(['se', 'se'])
        self.assertEqual(walker.distance_from_origin, 2)

    def test_knows_how_far_when_its_all_jagged(self):
        walker = Walker()
        walker.advance(['nw', 'sw', 'sw'])
        self.assertEqual(walker.distance_from_origin, 3)
