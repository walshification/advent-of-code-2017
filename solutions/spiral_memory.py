import itertools
import math


class Cell:
    def __init__(self, cell_id, coordinates):
        self.id = cell_id
        self.coordinates = coordinates
        self.x = coordinates[0]
        self.y = coordinates[1]


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
            self._cells[step] = Cell(step, position)

    def get_coordinates(self, cell_id):
        return self._cells[cell_id].coordinates

    def distance_from_origin(self, cell_id):
        cell = self._cells[cell_id]
        return sum([abs(cell.x), abs(cell.y)])
