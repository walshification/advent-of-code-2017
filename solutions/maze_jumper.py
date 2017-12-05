import yaml


class MazeJumper:
    def __init__(self, instructions):
        self.instructions = instructions
        self._index = 0
        self.total_jump_count = 0

    @property
    def location(self):
        return self._index

    def jump(self, jump_type=''):
        jump_amount = self.instructions[self._index]
        self._change_instruction(jump_type)
        self._index += jump_amount
        self.total_jump_count += 1

    def jump_out(self, jump_type=''):
        while self._index < len(self.instructions):
            self.jump(jump_type=jump_type)
        return self.total_jump_count

    def _change_instruction(self, jump_type):
        if jump_type == 'wacky' and self._is_big_jump(self.instructions[self._index]):
            self.instructions[self._index] -= 1
        else:
            self.instructions[self._index] += 1

    def _is_big_jump(self, jump_amount):
        return jump_amount > 2


if __name__ == '__main__':
    with open('solutions/problem_inputs/maze_jumper.yaml', 'r') as instructions:
        part_one_input = yaml.load(instructions)

    part_two_input = part_one_input[:]
    print('Part One:', MazeJumper(part_one_input).jump_out())
    print('Part Two:', MazeJumper(part_two_input).jump_out(jump_type='wacky'))
