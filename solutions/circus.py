import re
from collections import defaultdict

import yaml


class Program:
    def __init__(self, program):
        children = []
        if '->' in program:
            program, supports = program.split(' -> ')
            children.extend(supports.split(', '))
        name = re.search('\w+|$', program).group()
        weight = re.search('\d+|$', program).group()

        self.name = name
        self.weight = int(weight)
        self.children = children
        self.parent = None
        self.total_weight = int(weight)


class Pyramid:
    def __init__(self, programs):
        self.programs = {program.name: program for program in programs}
        for name, program in self.programs.items():
            program.total_weight += sum(
                self.programs[child].weight for child in program.children
            )
        self._root = None
        self._unbalanced_program = None

    @classmethod
    def build(cls, schemas):
        programs = [Program(schema) for schema in schemas]
        for program in programs:
            for other in programs:
                if program.name in other.children:
                    program.parent = other.name
        return cls(programs)

    @property
    def root(self):
        if self._root is None:
            self._root = self._dig_up_root(self.programs[next(iter(self.programs))])
        return self._root

    @property
    def unbalanced_program(self):
        if self._unbalanced_program is None:
            self._unbalanced_program = self._find_unbalanced_program(self.root)
        return self._unbalanced_program

    @property
    def weight_to_balance(self):
        sibling = [
            self.programs[child]
            for child in self.programs[self.unbalanced_program.parent].children
            if child != self.unbalanced_program.name
        ][0]
        difference = sibling.total_weight - self.unbalanced_program.total_weight
        return self.unbalanced_program.weight + difference

    def is_balanced(self, program_name):
        program = self.programs[program_name]
        if not program.children:
            return True
        children_weights = set(
            self.programs[child].total_weight for child in program.children
        )
        return len(children_weights) < 2

    def _dig_up_root(self, arbitrary_program):
        if not arbitrary_program.parent:
            return arbitrary_program
        return self._dig_up_root(self.programs[arbitrary_program.parent])

    def _supported_weight(self, programs):
        descendants = self._get_descendants(programs)
        return sum(descendant.weight for descendant in descendants)

    def _get_descendants(self, programs):
        if not programs:
            return []
        children = [
            self.programs[child]
            for program in programs
            for child in program.children
        ]
        return children + self._get_descendants(children)

    def _find_unbalanced_program(self, root):
        unbalanced = [
            program.name for program in [root] if not self.is_balanced(program.name)
        ]
        if unbalanced:
            child_to_weights_mapping = {
                child: self.programs[child].total_weight
                for child in self.programs[unbalanced[0]].children
            }
            weight_count = defaultdict(int)
            for weight in child_to_weights_mapping.values():
                weight_count[weight] += 1
            oddball = [
                child
                for child, weight in child_to_weights_mapping.items()
                if weight_count[weight] == 1 and self.programs[child].children
            ]
            if oddball:
                return self._find_unbalanced_program(self.programs[oddball[0]])
            else:
                return root
        return root


if __name__ == '__main__':
    with open('problem_inputs/circus.yaml', 'r') as programs:
        test_input = yaml.safe_load(programs)
    pyramid = Pyramid.build(test_input)
    print('Part One:', pyramid.root.name)
    print('Part Two:', pyramid.weight_to_balance, '1072')
