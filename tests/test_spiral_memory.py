import unittest

from solutions.spiral_memory import Cell, MemoryBank


class CellTests(unittest.TestCase):
    def test_remembers_cell_id_and_coordinates(self):
        cell = Cell(1, (0, 0))
        self.assertEqual(cell.id, 1)
        self.assertEqual(cell.coordinates, (0, 0))


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

    def test_calculates_manhattan_distance_from_origin_to_point_along_the_x_axis(self):
        self.bank.allocate(11)
        self.assertEqual(self.bank.distance_from_origin(11), 2)

    def test_calculates_manhattan_distance_from_origin_to_point_along_the_y_axis(self):
        self.bank.allocate(15)
        self.assertEqual(self.bank.distance_from_origin(15), 2)

    def test_calculates_manhattan_distance_from_origin_to_point_along_the_diagonal(self):
        self.bank.allocate(12)
        self.assertEqual(self.bank.distance_from_origin(12), 3)
