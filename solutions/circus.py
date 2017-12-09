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


class Tower:
    def __init__(self, root, descendants):
        self.root = root
        self.descendants = descendants
        self.line = [root] + descendants
        self.supported_weight = sum(program.weight for program in descendants)
        self._branches = None
        self._branch_weights = None

    @classmethod
    def build(cls, root, programs):
        descendants = [program for program in programs if program.name in root.children]
        return cls(root, descendants)

    @property
    def branches(self):
        if self._branches is None:
            children = [
                descendant for descendant in self.descendants
                for child_name in self.root.children
                if descendant.name == child_name
            ]
            self._branches = [Tower.build(child, self.descendants) for child in children]
        return self._branches

    @property
    def is_balanced(self):
        if self._branch_weights is None:
            self._branch_weights = {branch.supported_weight for branch in self.branches}
        return len(self._branch_weights) == 1


class Pyramid:
    def __init__(self, programs):
        self.tree = self._build_tree(programs)

    @property
    def root(self):
        any_key = next(iter(self.tree))
        return self._find_root(self.tree[any_key])

    def descendants(self, program):
        if not self.tree[program].children:
            return []

        children = [
            [self.tree[child]] + self.descendants(child)
            for child in self.tree[program].children
        ]
        return list(chain.from_iterable(children))  # flatten the lists

    def _build_tree(self, programs):
        tree = self._construct_programs(programs)
        return self._assign_parents(tree)

    def _construct_programs(self, programs):
        tree = {}
        for program in programs:
            program = Program(program)
            tree[program.name] = program
        return tree

    def _assign_parents(self, tree):
        for program in tree.keys():
            for other in tree.values():
                if program in other.children:
                    tree[program].parent = other.name
        return tree

    def _find_root(self, program):
        if not program.parent:
            return program
        return self._find_root(self.tree[program.parent])


if __name__ == '__main__':
    with open('solutions/problem_inputs/circus.yaml', 'r') as programs:
        test_input = yaml.load(programs)
    pyramid = Pyramid(test_input)
    print('Part One:', pyramid.root.name)
    print('Part Two:', Pyramid.find_unbalanced_program(pyramid, pyramid.root))
