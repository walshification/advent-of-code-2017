import unittest

from solutions.passphrase_validator import (has_no_anagrams,
                                            is_anagram,
                                            is_unique,
                                            valid_count)


class PassphraseValidatorTests(unittest.TestCase):
    def test_is_unique_returns_true_for_passphrase_with_no_repeating_words(self):
        self.assertTrue(is_unique('aa bb cc'))

    def test_is_unique_returns_false_for_passphrases_with_repeat_words(self):
        self.assertFalse(is_unique('aa bb aa'))

    def test_is_anagram_returns_true_if_any_password_is_anagram_for_other(self):
        self.assertTrue(is_anagram('asdf', 'fdsa'))

    def test_has_no_anagrams_returns_true_if_passphrase_contains_no_anagrams(self):
        self.assertTrue(has_no_anagrams('iiii oiii ooii oooi oooo'))

    def test_has_no_anagrams_returns_false_if_passphrase_has_anagram(self):
        self.assertFalse(has_no_anagrams('abcde xyz ecdab'))

    # bug regression
    def test_has_no_anagrams_isnt_fooled_by_consecutive_letter_pairs(self):
        self.assertTrue(has_no_anagrams('aa bb'))

    def test_valid_count_returns_number_of_valid_passphrases_per_validator_function(self):
        passphrases = [
            'aa bb cc',
            'aa bb aa',
            'asdf qwer fdas'
        ]
        self.assertEqual(valid_count(passphrases, has_no_anagrams), 1)
