import yaml


def calculate(rows, difference_func):
    return sum([difference_func(row) for row in rows])


def max_min_difference(row):
    digits = [digit for digit in row if digit is not None]
    return max(digits) - min(digits)


def even_divisor_difference(row):
    for i in range(len(row)):
        divisors = _dig_for_divisors(row[i], row[i+1:])
        if divisors:
            return int(max(divisors) / min(divisors))


def _dig_for_divisors(number, row):
    for digit in row:
        if number % digit == 0 or digit % number == 0:
            return number, digit


if __name__ == '__main__':
    with open('solutions/problem_inputs/checksum.yaml', 'r') as spreadsheet:
        test_input = yaml.load(spreadsheet)
    print('Part One: ', calculate(test_input, max_min_difference))
    print('Part Two: ', calculate(test_input, even_divisor_difference))
