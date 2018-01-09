import yaml


class Walker:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.furthest_distance = 0

    @property
    def coordinates(self):
        return (self.x, self.y, self.z)

    @property
    def distance_from_origin(self):
        distance = 0
        if self.x > 0:
            distance += self.x
        if self.y > 0:
            distance += self.y
        if self.z > 0:
            distance += self.z
        return distance

    def advance(self, moves):
        for move in moves.split(','):
            self.move(move)
            if self.distance_from_origin > self.furthest_distance:
                self.furthest_distance = self.distance_from_origin
        return self

    def move(self, direction):
        direction_to_coordinate_delta_map = {
            'n': (0, 1, -1),
            'nw': (-1, 1, 0),
            'sw': (-1, 0, 1),
            's': (0, -1, 1),
            'se': (1, -1, 0),
            'ne': (1, 0, -1),
        }
        self.__change_coordinates(*direction_to_coordinate_delta_map[direction])

    def __change_coordinates(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz


if __name__ == '__main__':
    with open('problem_inputs/hex_ed.yaml', 'r') as moves:
        test_input = yaml.safe_load(moves)
    walker = Walker()
    walker.advance(test_input)
    print('Part One:', walker.distance_from_origin)
    print('Part Two:', walker.furthest_distance)
