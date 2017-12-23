import yaml


def solve(sequence, pair_step='next'):
    return sum(_digits_with_a_following_pair(sequence, pair_step))


def _digits_with_a_following_pair(sequence, pair_step):
    sequence_str = str(sequence)
    return [
        _digit_with_pair(i, sequence_str, pair_step)
        for i in range(len(sequence_str))
    ]


def _digit_with_pair(i, sequence_str, pair_step):
    next_i = _determine_next(i, sequence_str, pair_step)
    if sequence_str[i] == sequence_str[next_i]:
        return int(sequence_str[i])
    return 0


def _determine_next(i, sequence_str, pair_step):
    return {
        'half': _half_step_index(i, sequence_str),
        'next': (i + 1 if i + 1 != len(sequence_str) else 0),
    }[pair_step]


def _half_step_index(i, sequence_str):
    return int((i + (len(sequence_str) / 2)) % len(sequence_str))


if __name__ == '__main__':
    with open('problem_inputs/captcha.yaml', 'r') as captcha:
        test_input = yaml.safe_load(captcha)
    print('Part One: ', solve(test_input))
    print('Part Two: ', solve(test_input, pair_step='half'))
