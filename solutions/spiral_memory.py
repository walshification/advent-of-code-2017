import itertools
import math


class Cell:
    def __init__(self, coordinates, value=0):
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
        self._forward = itertools.cycle([
            self.move_right,
            self.move_up,
            self.move_left,
            self.move_down
        ])
        self._backward = itertools.cycle([
            self.move_left,
            self.move_up,
            self.move_right,
            self.move_down
        ])

    def advance(self, number_of_cells):
        n = 1
        layer_length = 1
        position = 0, 0
        layers_for_cells = math.ceil(math.sqrt(number_of_cells))

        for _ in range(layers_for_cells):
            for _ in range(2):
                move = next(self._forward)
                for _ in range(layer_length):
                    n += 1
                    if n > number_of_cells:
                        return
                    position = move(*position)
                    yield(position)
            layer_length += 1

    def backtrack(self, endpoint):
        n = 1
        layer = math.ceil((math.sqrt(endpoint) / 2)) - 1
        layer_length = layer * 2  # -x to x
        position = (layer, -layer)
        distance_from_corner = int(math.pow(((layer * 2) + 1), 2) - endpoint + 1)

        for _ in range(distance_from_corner):
            for _ in range(2):
                move = next(self._backward)
                for _ in range(layer_length):
                    n += 1
                    if n > distance_from_corner:
                        return
                    position = move(*position)
                    yield(position)
            layer_length -= 1

    def move_right(self, x, y):
        return x+1, y

    def move_down(self, x, y):
        return x, y-1

    def move_left(self, x, y):
        return x-1, y

    def move_up(self, x, y):
        return x, y+1


class MemoryBank:
    adjacent_positions = [
        (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)
    ]

    def __init__(self, worker=None, disable_progress_bar=False):
        self._cells = {(0, 0): Cell((0, 0), value=1)}  # origin
        self._cells_by_value = {1: self._cells[(0, 0)]}
        self._highest_value = 1
        self.worker = worker or SpiralWorker()
        self.disable_progress_bar = disable_progress_bar

    @property
    def cells(self):
        return list(self._cells.values())

    def allocate(self, number_of_cells):
        for position in self.worker.advance(number_of_cells):
            current_cell = Cell(position)
            current_cell.value = sum(self._calculate_adjacent_values(current_cell))
            self._cells[position] = current_cell
            self._cells_by_value[current_cell.value] = current_cell
            self._highest_value = current_cell.value

    def get_cell(self, x, y):
        return self._cells[x, y]

    def distance_from_origin(self, other):
        for position in self.worker.backtrack(other):
            target_cell = self._cells.get(position)
            if target_cell and target_cell.id == other:
                return target_cell.distance_from(self.get_cell(0, 0))

    def value_higher_than_target(self, value):
        return self._get_cell_by_value_or_higher(value)

    def _calculate_adjacent_values(self, current_cell):
        return [
            self._get_adjacent_value(current_cell, *adjacent_position)
            for adjacent_position in self.adjacent_positions
        ]

    def _get_adjacent_value(self, current_cell, adjacent_x, adjacent_y):
        adjacent_x = current_cell.x + adjacent_x
        adjacent_y = current_cell.y + adjacent_y
        if (adjacent_x, adjacent_y) in self._cells:
            return self._cells[adjacent_x, adjacent_y].value
        return 0

    def _get_cell_by_value_or_higher(self, value):
        if value > self._highest_value:
            return None

        target = None
        while not target:
            target = self._cells_by_value.get(value)
            value += 1
        return target


if __name__ == '__main__':
    bank = MemoryBank()
    bank.allocate(312051)
    print('Part One:', bank.distance_from_origin(312051))
    print('Part Two:', bank.value_higher_than_target(312051))
