from unittest import TestCase
from unittest.mock import patch

from solutions.knot_hash import Knot


class InitTests(TestCase):
    def test_adds_default_length_bytes_to_the_end_of_the_lengths(self):
        knot = Knot(lengths=[])
        self.assertEqual(knot.lengths, [17, 31, 73, 47, 23])


class TwistTests(TestCase):
    def test_reverses_a_chunk_of_the_hash_by_the_length_provided(self):
        knot = Knot([3], [0, 1, 2, 3, 4])
        twisted_numbers = knot.twist(lengths=[3])
        self.assertEqual(list(twisted_numbers), [2, 1, 0, 3, 4])

    def test_sets_current_position_to_length_just_processed_plus_skip_size(self):
        knot = Knot([3], [0, 1, 2, 3, 4])
        knot.twist(lengths=[3])
        self.assertEqual(knot.current_position, 3)

    def test_skip_size_increases_by_1_after_a_twist(self):
        knot = Knot([3], [0, 1, 2, 3, 4])
        knot.twist(lengths=[3])
        self.assertEqual(knot.skip_size, 1)

    def test_wraps_around_the_end_of_the_string(self):
        knot = Knot([3, 4], [0, 1, 2, 3, 4])
        twisted_numbers = knot.twist(lengths=[3, 4])
        self.assertEqual(list(twisted_numbers), [4, 3, 0, 1, 2])

    def test_passes_the_example(self):
        knot = Knot([3, 4, 1, 5], [0, 1, 2, 3, 4])
        twisted_numbers = knot.twist(lengths=[3, 4, 1, 5])
        self.assertEqual(list(twisted_numbers), [3, 4, 2, 1, 0])
        self.assertEqual(knot.skip_size, 4)
        self.assertEqual(knot.current_position, 4)


class HashTests(TestCase):
    @patch('solutions.knot_hash.Knot.twist')
    def test_calls_twist_64_times(self, mock_twist):
        knot = Knot([])
        knot.create_sparse_hash()
        self.assertEqual(mock_twist.call_count, 64)

    @patch('solutions.knot_hash.Knot.twist')
    def test_calls_twist_with_lengths(self, mock_twist):
        knot = Knot([])
        knot.create_sparse_hash()
        mock_twist.assert_called_with(knot.lengths)

    def test_compacts_lengths_of_16_digits_into_1_by_xor_operations(self):
        knot = Knot([])
        sparse_hash = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
        dense_hash = knot.create_dense_hash(sparse_hash)
        self.assertEqual(dense_hash, [64])

    def test_converts_lists_of_digits_into_hex_string(self):
        knot = Knot([])
        hex_string = knot.hexadecimalize([0, 1, 10, 15, 16, 17, 26, 31])
        self.assertEqual(hex_string, '00010a0f10111a1f')

    def test_empty_string_becomes_valid_hash(self):
        knot = Knot([])
        self.assertEqual(knot.hash, 'a2582a3a0e66e6e86e3812dcb672a272')
