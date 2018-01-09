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
        if direction == 'n':
            self.__change_coordinates(0, 1, -1)
        if direction == 'nw':
            self.__change_coordinates(-1, 1, 0)
        if direction == 'sw':
            self.__change_coordinates(-1, 0, 1)
        if direction == 's':
            self.__change_coordinates(0, -1, 1)
        if direction == 'se':
            self.__change_coordinates(1, -1, 0)
        if direction == 'ne':
            self.__change_coordinates(1, 0, -1)

    def __on_the_axis(self):
        return 0 in [self.x, self.y, self.z]

    def __follow_the_axis(self):
        absolute_x = abs(self.x)
        absolute_y = abs(self.y)
        absolute_z = abs(self.z)
        if absolute_x > 0:
            return absolute_x
        if absolute_y > 0:
            return absolute_y
        if absolute_z > 0:
            return absolute_z

    def __change_coordinates(self, dx, dy, dz):
        self.x += dx
        self.y += dy
        self.z += dz


if __name__ == '__main__':
    with open('problem_inputs/hex_ed.yaml', 'r') as moves:
        test_input = yaml.safe_load(moves)
    print('Part One:', Walker().advance(test_input).distance_from_origin)
