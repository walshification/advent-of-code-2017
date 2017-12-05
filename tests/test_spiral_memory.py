import unittest

from solutions.spiral_memory import Cell, MemoryBank


class CellTests(unittest.TestCase):
    def setUp(self):
        self.cell = Cell(1, (1, 1))

    def test_remembers_cell_id_and_coordinates(self):
        self.assertEqual(self.cell.id, 1)
        self.assertEqual(self.cell.coordinates, (1, 1))

    def test_distance_from_returns_number_of_steps_between_cells_along_x_axis(self):
        other = Cell(2, (4, 1))
        self.assertEqual(self.cell.distance_from(other), 3)

    def test_distance_from_returns_number_of_steps_between_cells_along_y_axis(self):
        other = Cell(2, (1, 4))
        self.assertEqual(self.cell.distance_from(other), 3)

    def test_distance_from_returns_number_of_steps_between_cells_along_diagonal(self):
        other = Cell(2, (4, -1))
        self.assertEqual(self.cell.distance_from(other), 5)

    def test_is_adjacent_returns_true_if_next_to_other(self):
        other = Cell(2, (2, 1))
        self.assertTrue(self.cell.is_adjacent(other))

    def test_is_adjacent_returns_false_if_other_is_two_or_more_steps_way(self):
        other = Cell(2, (3, 1))
        self.assertFalse(self.cell.is_adjacent(other))

    def test_is_diagonal_from_returns_true_if_diagonal_from_other(self):
        other = Cell(2, (0, 0))
        self.assertTrue(self.cell.is_diagonal_from(other))

    def test_is_diagonal_from_returns_false_if_diagonal_from_other(self):
        other = Cell(2, (-1, 0))
        self.assertFalse(self.cell.is_diagonal_from(other))


class MemoryBankTests(unittest.TestCase):
    def setUp(self):
        self.bank = MemoryBank()

    def test_allocates_memory_cells_in_a_spiral_pattern(self):
        self.bank.allocate(3)
        self.assertEqual(self.bank.get_coordinates(1), (0, 0))
        self.assertEqual(self.bank.get_coordinates(2), (1, 0))
        self.assertEqual(self.bank.get_coordinates(3), (1, 1))

    def test_continues_the_spiral_with_layers(self):
        self.bank.allocate(10)
        self.assertEqual(self.bank.get_coordinates(5), (-1, 1))
        self.assertEqual(self.bank.get_coordinates(7), (-1, -1))
        self.assertEqual(self.bank.get_coordinates(10), (2, -1))
