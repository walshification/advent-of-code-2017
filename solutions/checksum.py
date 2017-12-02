def calculate(rows):
    return sum([max_min_difference(row) for row in rows])


def max_min_difference(row):
    digits = [digit for digit in row if digit is not None]
    return max(digits) - min(digits)
