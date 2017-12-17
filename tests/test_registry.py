import unittest

from solutions.registry import Registry


class RegisterTests(unittest.TestCase):
    def test_creates_an_initial_registry_with_no_entries(self):
        registry = Registry()
        self.assertEqual(registry.registers, {})

    def test_adds_registers_to_the_registry_when_introduced(self):
        registry = Registry(['b inc 5 if a > 1'])
        self.assertTrue('b' in registry.registers)

    def test_adds_rgisters_for_comparing_if_not_previously_registered(self):
        registry = Registry(['b inc 5 if a > 1'])
        self.assertTrue('a' in registry.registers)

    def test_increases_register_by_value(self):
        registry = Registry(['b inc 5 if a == 0'])
        self.assertEqual(registry.registers['b'], 5)

    def test_decreases_register_by_value(self):
        registry = Registry(['b dec 5 if a == 0'])
        self.assertEqual(registry.registers['b'], -5)

    def test_does_not_change_register_if_condition_is_false_by_less_than(self):
        registry = Registry(['b dec 5 if a < 0'])
        self.assertEqual(registry.registers['b'], 0)

    def test_largest_value_returns_largest_value_in_registry(self):
        registry = Registry(['b inc 5 if a == 0'])
        self.assertEqual(registry.largest_value, 5)

    def test_processes_a_series_of_instructions(self):
        instructions = [
            'b inc 5 if a > 1',
            'a inc 1 if b < 5',
            'c dec -10 if a >= 1',
            'c inc -20 if c == 10',
        ]
        registry = Registry(instructions)
        self.assertEqual(registry.largest_value, 1)
