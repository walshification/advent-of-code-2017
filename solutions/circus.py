import re
import yaml


class Pyramid:
    def __init__(self, programs):
        self.tower = {}
        self._build_tower(programs)

    @property
    def root(self):
        return self._find_root(self.tower[next(iter(self.tower))])

    def get(self, name):
        return self.tower.get(name)

    def parent(self, child):
        for parent, attributes in self.tower.items():
            if child in attributes['supports']:
                return self.tower[parent]
        return None

    def _build_tower(self, programs):
        supports = None
        for program in programs:
            if '->' in program:
                program, supports = program.split(' -> ')
                supports = supports.split(', ')

            name = re.search('\w+|$', program).group()
            weight = re.search('\d+|$', program).group()
            self.tower[name] = {
                'name': name,
                'weight': int(weight),
                'supports': supports or [],
            }

    def _find_root(self, node):
        if not self.parent(node['name']):
            return node['name']
        return self._find_root(self.parent(node['name']))


if __name__ == '__main__':
    with open('solutions/problem_inputs/circus.yaml', 'r') as programs:
        test_input = yaml.load(programs)
    print('Part One:', Pyramid(test_input).root)
