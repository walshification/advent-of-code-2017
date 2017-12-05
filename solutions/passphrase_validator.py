import yaml


def valid_count(passphrases, validation):
    return len([passphrase for passphrase in passphrases if validation(passphrase)])


def is_unique(passphrase):
    passwords = passphrase.split(' ')
    return len(passwords) == len(set(passwords))


def has_no_anagrams(passphrase):
    passwords = passphrase.split(' ')
    for i in range(len(passwords)):
        print('for', passwords)
        for other in passwords[i+1:]:
            print('checking', passwords[i], other, not is_anagram(passwords[i], other))
            if is_anagram(passwords[i], other):
                return False
    return True


def is_anagram(word, other):
    word_letters = list(word)
    other_letters = list(other)
    return len(word_letters) == len(set(word_letters + other_letters))


if __name__ == '__main__':
    with open('solutions/problem_inputs/passphrase_validator.yaml', 'r') as passwords:
        test_input = yaml.load(passwords)
    print('Part One:', valid_count(test_input, is_unique))
    print('Part Two:', valid_count(test_input, has_no_anagrams))
