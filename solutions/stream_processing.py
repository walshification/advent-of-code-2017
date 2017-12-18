def valuate(stream):
    # clean garbage
    # remove garbage
    # assess the groups
    return assess(stream)


def assess(stream, generation=1):
    if stream == '{}':
        return generation
    if stream[:2] == '{{':
        return generation + assess(stream[1:-1], generation+1)
    return sum(
        assess(group, generation) for group in stream.split(',')
    )
