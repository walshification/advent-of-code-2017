import itertools
import math

from tqdm import tqdm


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
                    if n > number_of_cells:
                        return
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
    def __init__(self, worker=None, disable_progress_bar=False):
        self._cells = {1: Cell(1, (0, 0), value=1)}  # origin
        self._cells_by_value = {1: self._cells[1]}
        self._highest_value = 1
        self.worker = worker or SpiralWorker()
        self.disable_progress_bar = disable_progress_bar

    @property
    def cells(self):
        return list(self._cells.values())

    def allocate(self, number_of_cells):
        for step, position in tqdm(
            self.worker.advance(number_of_cells),
            total=number_of_cells,
            disable=self.disable_progress_bar
        ):
            current_cell = Cell(step, position)
            # current_cell.value = sum(self._calculate_adjacent_values(current_cell))
            self._cells[step] = current_cell
            self._cells_by_value[current_cell.value] = current_cell
            self._highest_value = current_cell.value

    def get_cell(self, cell_id):
        return self._cells[cell_id]

    def get_coordinates(self, cell_id):
        return self._cells[cell_id].coordinates

    def distance_from_origin(self, other):
        return self.get_cell(other).distance_from(self.get_cell(1))

    def value_higher_than_target(self, value):
        return self._get_cell_by_value_or_higher(value)

    def _calculate_adjacent_values(self, current_cell):
        return [
            cell.value for cell in self._cells.values()
            if cell.is_adjacent(current_cell)
        ]

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
    # print('Part Two:', bank.value_higher_than_target(312051))
