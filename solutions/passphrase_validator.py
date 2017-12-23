import yaml


def valid_count(passphrases, validate):
    return len([passphrase for passphrase in passphrases if validate(passphrase)])


def is_unique(passphrase):
    passwords = passphrase.split(' ')
    return len(passwords) == len(set(passwords))


def has_no_anagrams(passphrase):
    passwords = passphrase.split(' ')
    for i in range(len(passwords)):
        for other in passwords[i+1:]:
            if is_anagram(passwords[i], other):
                return False
    return True


def is_anagram(word, other):
    return sorted(list(word)) == sorted(list(other))


if __name__ == '__main__':
    with open('problem_inputs/passphrase_validator.yaml', 'r') as passwords:
        test_input = yaml.load(passwords)
    print('Part One:', valid_count(test_input, is_unique))
    print('Part Two:', valid_count(test_input, has_no_anagrams))
