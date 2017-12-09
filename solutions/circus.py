import re
from itertools import chain

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

    @classmethod
    def find_unbalanced_program(cls, pyramid, root):
        child_lineages = cls.__map_children_to_lineages(pyramid, root)
        lineage_weights = cls.__map_children_to_total_weights(child_lineages)
        weight_names = cls.__map_weights_to_names(lineage_weights)

        if pyramid.is_unbalanced(weight_names):
            off_balance_program = cls.__find_off_balance_program(weight_names.values())
            return cls.find_unbalanced_program(pyramid, pyramid.tower[off_balance_program])
        else:
            return root.name

    @classmethod
    def __map_children_to_lineages(cls, pyramid, root):
        return {
            child: [pyramid.tower[child]] + pyramid.descendants(child)
            for child in root.children
        }

    @classmethod
    def __map_children_to_total_weights(cls, child_lineages):
        return {
            child: sum(child.weight for child in lineage)
            for child, lineage in child_lineages.items()
        }

    @classmethod
    def __map_weights_to_names(cls, lineage_weights):
        weight_names = {}
        for name, weight in lineage_weights.items():
            if weight_names.get(weight):
                weight_names[weight].append(name)
            else:
                weight_names[weight] = [name]
        return weight_names

    @classmethod
    def __find_off_balance_program(cls, names):
        for name_list in names:
            if len(name_list) == 1:
                return name_list[0]

    @property
    def root(self):
        any_key = next(iter(self.tower))
        return self._find_root(self.tower[any_key])

    def descendants(self, program):
        if not self.tower[program].children:
            return []

        children = [
            [self.tower[child]] + self.descendants(child)
            for child in self.tower[program].children
        ]
        return list(chain.from_iterable(children))  # flatten the lists

    def is_unbalanced(self, weight_names):
        return len(weight_names) > 1

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
            return program
        return self._find_root(self.tower[program.parent])


if __name__ == '__main__':
    with open('solutions/problem_inputs/circus.yaml', 'r') as programs:
        test_input = yaml.load(programs)
    print('Part One:', Pyramid(test_input).root)
