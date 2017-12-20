import unittest

from solutions.spiral_memory import Cell, MemoryBank


class CellTests(unittest.TestCase):
    def setUp(self):
        self.cell = Cell((1, 1))

    def test_remembers_coordinates(self):
        self.assertEqual(self.cell.coordinates, (1, 1))

    def test_distance_from_returns_number_of_steps_between_cells_along_x_axis(self):
        other = Cell((4, 1))
        self.assertEqual(self.cell.distance_from(other), 3)

    def test_distance_from_returns_number_of_steps_between_cells_along_y_axis(self):
        other = Cell((1, 4))
        self.assertEqual(self.cell.distance_from(other), 3)

    def test_distance_from_returns_number_of_steps_between_cells_along_diagonal(self):
        other = Cell((4, -1))
        self.assertEqual(self.cell.distance_from(other), 5)

    def test_is_adjacent_returns_true_if_next_to_other(self):
        other = Cell((2, 1))
        self.assertTrue(self.cell.is_adjacent(other))

    def test_is_adjacent_returns_false_if_other_is_two_or_more_steps_way(self):
        other = Cell((3, 1))
        self.assertFalse(self.cell.is_adjacent(other))

    def test_is_diagonal_from_returns_true_if_diagonal_from_other(self):
        other = Cell((0, 0))
        self.assertTrue(self.cell.is_diagonal_from(other))

    def test_is_diagonal_from_returns_false_if_diagonal_from_other(self):
        other = Cell((-1, 0))
        self.assertFalse(self.cell.is_diagonal_from(other))


class MemoryBankTests(unittest.TestCase):
    def setUp(self):
        self.bank = MemoryBank(disable_progress_bar=True)

    def test_allocates_memory_cells_in_a_spiral_pattern(self):
        self.bank.allocate(3)
        self.assertTrue(self.bank.get_cell(0, 0))
        self.assertTrue(self.bank.get_cell(1, 0))
        self.assertTrue(self.bank.get_cell(1, 1))

    def test_continues_the_spiral_with_layers(self):
        self.bank.allocate(10)
        self.assertTrue(self.bank.get_cell(-1, 1))
        self.assertTrue(self.bank.get_cell(-1, -1))
        self.assertTrue(self.bank.get_cell(2, -1))

    def test_sets_cumulative_adjacent_values_on_new_cells(self):
        self.bank.allocate(6)
        self.assertEqual(self.bank.get_cell(0, 0).value, 1)
        self.assertEqual(self.bank.get_cell(1, 0).value, 1)
        self.assertEqual(self.bank.get_cell(1, 1).value, 2)
        self.assertEqual(self.bank.get_cell(0, 1).value, 4)
        self.assertEqual(self.bank.get_cell(-1, 1).value, 5)
        self.assertEqual(self.bank.get_cell(-1, 0).value, 10)

    def test_value_higher_than_target_returns_cell_with_next_highest_value(self):
        self.bank.allocate(6)
        higher = self.bank.value_higher_than_target(9)
        self.assertEqual(higher.value, 10)

    def test_value_higher_than_target_returns_None_if_no_higher_value(self):
        self.bank.allocate(6)
        higher = self.bank.value_higher_than_target(11)
        self.assertEqual(higher, None)

    def test_allocate_does_not_go_beyond_desired_number_of_cells(self):
        self.bank.allocate(10)
        self.assertEqual(len(self.bank.cells), 10)
