import itertools
import math


class Cell:
    def __init__(self, cell_id, coordinates, value=0):
        self.id = cell_id
        self.coordinates = coordinates
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.value = value

    def distance_from(self, other):
        return sum([abs(self.x - other.x), abs(self.y - other.y)])

    def is_adjacent(self, other):
        return self.distance_from(other) == 1 or self.is_diagonal_from(other)

    def is_diagonal_from(self, other):
        return abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1


class SpiralWorker:
    def __init__(self):
        self._moves = itertools.cycle([
            self.move_right,
            self.move_up,
            self.move_left,
            self.move_down
        ])

    def advance(self, number_of_cells):
        n = 1
        layer_length = 1
        position = 0, 0
        layers_for_cells = range(math.ceil(math.sqrt(number_of_cells)))

        for _ in layers_for_cells:
            for _ in range(2):
                move = next(self._moves)
                for _ in range(layer_length):
                    n += 1
                    position = move(*position)
                    yield(n, position)
            layer_length += 1

    def move_right(self, x, y):
        return x+1, y

    def move_down(self, x, y):
        return x, y-1

    def move_left(self, x, y):
        return x-1, y

    def move_up(self, x, y):
        return x, y+1


class MemoryBank:
    def __init__(self, worker=None):
        self._cells = {1: Cell(1, (0, 0))}  # origin
        self.worker = worker or SpiralWorker()

    def allocate(self, number_of_cells):
        for step, position in self.worker.advance(number_of_cells):
            current_cell = self.get_cell_by_position(position)
            # adjacent_values = self._calculate_adjacent_values(current_cell)
            self._cells[step] = Cell(step, position)

    def get_coordinates(self, cell_id):
        return self._cells[cell_id].coordinates

    def distance_from_points(self, cell_id_a, cell_id_b=1):
        cell_a = self._cells[cell_id_a]
        cell_b = self._cells[cell_id_b]
        return cell_a.distance_from(cell_b)

    def get_cell_by_position(self, position):
        for cell in self._cells.values():
            if cell.coordinates == position:
                return cell

    def _calculate_adjacent_values(self, current_cell):
        return [
            cell.value for cell in self._cells.values()
            if cell.is_adjacent(current_cell)
        ]


if __name__ == '__main__':
    bank = MemoryBank()
    bank.allocate(312051)
    print('Part One:', bank.distance_from_origin(312051))
