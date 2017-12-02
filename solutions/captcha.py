def solve(sequence):
    sequence = str(sequence)
    pairs = []
    sequence_end = len(sequence)
    for i in range(sequence_end):
        next_i = i + 1 if i + 1 is not (sequence_end) else 0
        if sequence[i] == sequence[next_i]:
            pairs.append(int(sequence[i]))
    return sum(pairs)
