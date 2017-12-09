import re
import yaml


class Program:
    def __init__(self, program):
        supports = None
        if '->' in program:
            program, supports = program.split(' -> ')
            supports = supports.split(', ')
        name = re.search('\w+|$', program).group()
        weight = re.search('\d+|$', program).group()

        self.name = name
        self.weight = int(weight)
        self.children = supports or []
        self.parent = None


class Pyramid:
    def __init__(self, programs):
        self.tower = self._build_tower(programs)

    @property
    def root(self):
        any_key = next(iter(self.tower))
        return self._find_root(self.tower[any_key])

    def _build_tower(self, programs):
        tower = self._construct_programs(programs)
        return self._assign_parents(tower)

    def _construct_programs(self, programs):
        tower = {}
        for program in programs:
            program = Program(program)
            tower[program.name] = program
        return tower

    def _assign_parents(self, tower):
        for program in tower.keys():
            for other in tower.values():
                if program in other.children:
                    tower[program].parent = other.name
        return tower

    def _find_root(self, program):
        if not program.parent:
            return program.name
        return self._find_root(self.tower[program.parent])


if __name__ == '__main__':
    with open('solutions/problem_inputs/circus.yaml', 'r') as programs:
        test_input = yaml.load(programs)
    print('Part One:', Pyramid(test_input).root)
