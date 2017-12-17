import yaml


class Registry:
    def __init__(self, instructions=None):
        self.registers = {}
        self._operator_map = {
            'inc': '+',
            'dec': '-',
        }
        self.largest_value_ever = 0
        self.prepare_registry(instructions)

    @property
    def largest_value(self):
        largest = 0
        for value in self.registers.values():
            if value > largest:
                largest = value
        return largest

    def prepare_registry(self, instructions):
        if instructions is None:
            return
        [self._parse_instruction(instruction) for instruction in instructions]

    def _parse_instruction(self, instruction):
        register, operator, value, _, other, comparator, difference = instruction.split()
        if register not in self.registers:
            self.registers[register] = 0
        if other not in self.registers:
            self.registers[other] = 0
        if eval('{} {} {}'.format(self.registers[other], comparator, difference)):
            self.registers[register] = eval(
                '{} {} {}'.format(
                    self.registers[register],
                    self._operator_map[operator],
                    value
                )
            )
        if self.registers[register] > self.largest_value_ever:
            self.largest_value_ever = self.registers[register]


if __name__ == '__main__':
    with open('solutions/problem_inputs/registry.yaml', 'r') as instructions:
        test_input = yaml.safe_load(instructions)
    print('Part One:', Registry(test_input).largest_value)
