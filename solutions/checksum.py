import yaml


def calculate(rows):
    return sum([max_min_difference(row) for row in rows])


def max_min_difference(row):
    digits = [digit for digit in row if digit is not None]
    return max(digits) - min(digits)


if __name__ == '__main__':
    with open('solutions/problem_inputs/checksum.yaml', 'r') as spreadsheet:
        test_input = yaml.load(spreadsheet)
    print('Part One: ', calculate(test_input))
