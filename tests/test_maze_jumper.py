import unittest

from solutions.maze_jumper import MazeJumper


class TestSetup(unittest.TestCase):
    def setUp(self):
        self.instructions = [1, 3, 0, 1, -3]
        self.jumper = MazeJumper(self.instructions)


class InitTests(TestSetup):
    def test_maze_jumper_registers_a_list_of_jump_instructions(self):
        self.assertEqual(self.jumper.instructions, self.instructions)

    def test_maze_jumper_starts_at_the_beginning_of_the_instructions(self):
        self.assertEqual(self.jumper.location, 0)

    def test_maze_jumper_starts_with_zero_jumps(self):
        self.assertEqual(self.jumper.total_jump_count, 0)


class JumpTests(TestSetup):
    def test_jump_advances_the_jumper_by_the_instruction_amount(self):
        self.jumper.jump()
        self.assertEqual(self.jumper.location, 1)

    def test_jump_increments_the_instruction_that_it_executes(self):
        self.jumper.jump()
        self.assertEqual(self.jumper.instructions[0], 2)

    def test_jump_increments_total_jump_count(self):
        self.jumper.jump()
        self.assertEqual(self.jumper.total_jump_count, 1)

    def test_wacky_jump_decreases_instruction_by_one_if_jump_is_three_or_more(self):
        self.jumper.jump('wacky')
        self.jumper.jump('wacky')
        self.assertEqual(self.jumper.instructions[1], 2)

    def test_wacky_jump_still_increments_by_one_for_small_jumps(self):
        self.jumper.jump('wacky')
        self.assertEqual(self.jumper.instructions[0], 2)


class JumpOutTests(TestSetup):
    def test_jump_out_runs_until_jumper_is_out_of_the_list_and_returns_jump_count(self):
        self.jumper.jump_out()
        self.assertEqual(self.jumper.total_jump_count, 4)

    def test_wacky_jump_out_runs_longer(self):
        self.jumper.jump_out(jump_type='wacky')
        self.assertEqual(self.jumper.total_jump_count, 9)
