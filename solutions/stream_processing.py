def valuate(stream):
    cleaned_stream = clean(stream)
    pure_stream = remove_garbage(cleaned_stream)
    return assess(pure_stream)


def clean(stream):
    cleaned_stream = []
    i = 0
    while i < len(stream):
        if stream[i] == '!':
            i += 1
        else:
            cleaned_stream.append(stream[i])
        i += 1
    return ''.join(cleaned_stream)


def remove_garbage(stream):
    cleaned_stream = []
    i = 0
    while i < len(stream):
        if stream[i] == '<':
            while stream[i] != '>':
                i += 1
        else:
            cleaned_stream.append(stream[i])
        i += 1
    return ''.join(cleaned_stream)


def assess(stream, generation=1):
    if stream == '{}':
        return generation
    if stream[:2] == '{{':
        return generation + assess(stream[1:-1], generation+1)
    return sum(
        assess(group, generation) for group in stream.split(',')
    )
