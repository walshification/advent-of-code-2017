import re
from itertools import chain

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

    def __repr__(self):
        return "<Program: name={} weight={} children={} parent={}>".format(
            self.name,
            self.weight,
            self.children,
            self.parent,
        )


class Pyramid:
    def __init__(self, programs):
        self.programs = {program.name: program for program in programs}
        self._root = None
        self._tree = None

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
    def tree(self):
        if self._tree is None:
            self._tree = {}
            for name, program in self.programs.items():
                self._tree[name] = {
                    'weight': program.weight,
                    'children': program.children,
                    'supported_weight': self._supported_weight([program])
                }
        return self._tree

    @property
    def unbalanced_program(self):
        return self._find_unbalanced_program(self.root)

    def is_balanced(self, program_name):
        program = self.tree[program_name]
        if not program['children']:
            return True
        descendants = set()
        for child in program['children']:
            descendants.add(
                sum(self.tree[child]['weight'] for child in self._get_descendants([self.programs[child]])
                )
            )
        # supported_weights = set(
        #     self.tree[child]['weight'] for child in descendants
        # )
        return len(descendants) < 2

    def _dig_up_root(self, arbitrary_program):
        if not arbitrary_program.parent:
            return arbitrary_program
        return self._dig_up_root(self.programs[arbitrary_program.parent])

    def _supported_weight(self, programs):
        descendants = self._get_descendants(programs)
        if programs:
            print('descendants for {}'.format(programs[0].name), descendants)
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
            program for program in root.children if not self.is_balanced(program)
        ]
        if unbalanced:
            unbalanced_branches = [
                child for child in root.children if not self.is_balanced(child)
            ]
            if unbalanced_branches:
                return self._find_unbalanced_program(self.programs[unbalanced[0]])
            return unbalanced[0]
        return root.name


if __name__ == '__main__':
    with open('solutions/problem_inputs/circus.yaml', 'r') as programs:
        test_input = yaml.load(programs)
    pyramid = Pyramid(test_input)
    print('Part One:', pyramid.root.name)
    print('Part Two:', Pyramid.find_unbalanced_program(pyramid, pyramid.root))
