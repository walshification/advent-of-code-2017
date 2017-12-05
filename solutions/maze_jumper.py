import yaml


class MazeJumper:
    def __init__(self, instructions):
        self.instructions = instructions
        self._index = 0
        self.total_jump_count = 0

    @property
    def location(self):
        return self._index

    def jump(self):
        jump_amount = self.instructions[self._index]
        self.instructions[self._index] += 1
        self._index += jump_amount
        self.total_jump_count += 1

    def jump_out(self):
        while self._index < len(self.instructions):
            self.jump()
        return self.total_jump_count


if __name__ == '__main__':
    with open('solutions/problem_inputs/maze_jumper.yaml', 'r') as instructions:
        test_input = yaml.load(instructions)
    print('Part One:', MazeJumper(test_input).jump_out())
