import unittest

from solutions.memory_reallocation import Reallocator


class MemoryReallocationSetup(unittest.TestCase):
    def setUp(self):
        self.reallocator = Reallocator([0, 2, 7, 0])


class MemoryReallocationTests(MemoryReallocationSetup):
    def test_reallocator_keeps_track_of_a_number_of_banks(self):
        self.assertEqual(len(self.reallocator.banks), 4)

    def test_reallocate_distributes_the_largest_bank_across_others(self):
        reallocator = Reallocator([1, 0, 0])
        reallocator.reallocate()
        self.assertEqual(reallocator.banks, [0, 1, 0])

    def test_reallocate_distributes_banks_larger_than_one_across_all_banks(self):
        reallocator = Reallocator([2, 0, 0])
        reallocator.reallocate()
        self.assertEqual(reallocator.banks, [0, 1, 1])

    def test_reallocate_cycles_back_to_beginning_of_banks_as_it_redistributes(self):
        reallocator = Reallocator([0, 3, 0])
        reallocator.reallocate()
        self.assertEqual(reallocator.banks, [1, 1, 1])

    def test_history_tracks_bank_states_after_redistribution(self):
        reallocator = Reallocator([1, 0, 0])
        reallocator.reallocate()
        self.assertEqual(reallocator.history, [[0, 1, 0]])

    def test_actively_reallocation_returns_number_of_steps_needed_to_repeat_a_state(self):
        reallocator = Reallocator([1, 0, 0])
        steps = reallocator.actively_reallocate()
        self.assertEqual(steps, 4)

    def test_integration_example(self):
        self.assertEqual(self.reallocator.actively_reallocate(), 5)

    def test_target_loop_size_finds_cycle_length_between_repeated_state(self):
        self.assertEqual(self.reallocator.actively_reallocate(target='loop-size'), 4)
