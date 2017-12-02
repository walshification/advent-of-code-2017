def solve(sequence):
    return sum(_digits_with_a_following_pair(sequence))


def _digits_with_a_following_pair(sequence):
    sequence_str = str(sequence)
    return [digit_with_pair(i, sequence_str) for i in range(len(sequence_str))]


def digit_with_pair(i, sequence_str):
    next_i = i + 1 if i + 1 is not len(sequence_str) else 0
    if sequence_str[i] == sequence_str[next_i]:
        return int(sequence_str[i])
    return 0
