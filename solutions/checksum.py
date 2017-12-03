import yaml


def calculate(rows, difference_func):
    return sum([difference_func(row) for row in rows])


def max_min_difference(row):
    digits = [digit for digit in row if digit is not None]
    return max(digits) - min(digits)


def even_divisor_difference(row):
    divisors = [digit for digit in row if _divides_evenly(digit, row)]
    return int(max(divisors) / min(divisors))


def _divides_evenly(number, digits):
    for digit in digits:
        if number != digit and (number % digit == 0 or digit % number == 0):
            return True
    return False


if __name__ == '__main__':
    with open('solutions/problem_inputs/checksum.yaml', 'r') as spreadsheet:
        test_input = yaml.load(spreadsheet)
    print('Part One: ', calculate(test_input, max_min_difference))
    print('Part Two: ', calculate(test_input, even_divisor_difference))
