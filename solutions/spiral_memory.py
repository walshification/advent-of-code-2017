import itertools
import math


class Cell:
    def __init__(self, cell_id, coordinates, value=0):
        self.id = cell_id
        self.coordinates = coordinates
        self.x = coordinates[0]
        self.y = coordinates[1]
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

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
        self._cells = {1: Cell(1, (0, 0), value=1)}  # origin
        self.worker = worker or SpiralWorker()

    def allocate(self, number_of_cells):
        for step, position in self.worker.advance(number_of_cells):
            current_cell = Cell(step, position)
            current_cell.value = sum(self._calculate_adjacent_values(current_cell))
            self._cells[step] = current_cell

    def get_cell(self, cell_id):
        return self._cells[cell_id]

    def get_coordinates(self, cell_id):
        return self._cells[cell_id].coordinates

    def _calculate_adjacent_values(self, current_cell):
        return [
            cell.value for cell in self._cells.values()
            if cell.is_adjacent(current_cell)
        ]


if __name__ == '__main__':
    bank = MemoryBank()
    bank.allocate(312051)
    print('Part One:', bank.distance_from_origin(312051))
