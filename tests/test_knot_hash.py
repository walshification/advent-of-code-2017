import unittest

from solutions.knot_hash import KnotHash


class InitTests(unittest.TestCase):
    def test_defaults_to_deque_of_integers_from_0_to_255(self):
        knot = KnotHash([])
        self.assertEqual(len(knot.string), 256)

    def test_sets_a_current_position_that_starts_at_0(self):
        knot = KnotHash([])
        self.assertEqual(knot.current_position, 0)

    def test_sets_a_skip_size_that_starts_at_0(self):
        knot = KnotHash([])
        self.assertEqual(knot.skip_size, 0)

    def test_remembers_a_series_of_lengths_to_use_for_hashing(self):
        lengths = [2, 5, 4, 3]
        knot = KnotHash(lengths)
        self.assertEqual(knot.lengths, lengths)


class TwistTests(unittest.TestCase):
    def test_reverses_a_chunk_of_the_hash_by_the_length_provided(self):
        knot = KnotHash([3], [0, 1, 2, 3, 4])
        knot.twist()
        self.assertEqual(knot.string, [2, 1, 0, 3, 4])

    def test_sets_current_position_to_length_just_processed_plus_skip_size(self):
        knot = KnotHash([3], [0, 1, 2, 3, 4])
        knot.twist()
        self.assertEqual(knot.current_position, 3)

    def test_skip_size_increases_by_1_after_a_twist(self):
        knot = KnotHash([3], [0, 1, 2, 3, 4])
        knot.twist()
        self.assertEqual(knot.skip_size, 1)

    def test_wraps_around_the_end_of_the_string(self):
        knot = KnotHash([3, 4], [0, 1, 2, 3, 4])
        knot.twist()
        self.assertEqual(knot.string, [4, 3, 0, 1, 2])

    def test_passes_the_example(self):
        knot = KnotHash([3, 4, 1, 5], [0, 1, 2, 3, 4])
        knot.twist()
        self.assertEqual(knot.string, [3, 4, 2, 1, 0])
        self.assertEqual(knot.skip_size, 4)
        self.assertEqual(knot.current_position, 4)
