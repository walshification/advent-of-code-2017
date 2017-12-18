import yaml


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

    further_cleaned_stream = []
    i = 0
    cleaned_stream = ''.join(cleaned_stream)
    while i < len(cleaned_stream):
        if cleaned_stream[i] in ['{', '}']:
            further_cleaned_stream.append(cleaned_stream[i])
            while cleaned_stream[i+1:i+2] not in ['', '}', '{']:
                i += 1
        else:
            further_cleaned_stream.append(cleaned_stream[i])
        i += 1
    return ''.join(further_cleaned_stream)


def assess(stream, generation=1):
    total = 0
    i = 0
    while i < len(stream):
        if stream[i+1:i+2] == '{':
            generation += 1
        if stream[i+1:i+2] == '}':
            total += generation
            generation -= 1
        i += 1
    return total

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(10000)

    with open('solutions/problem_inputs/stream_processing.yaml') as stream:
        test_input = yaml.safe_load(stream)
    print('Part One:', valuate(test_input))
