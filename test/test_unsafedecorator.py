import unittest
import os
from collections import deque

from src.applications.app_tail import Tail
from src.applications.unsafe_decorator import UnsafeDecorator
from src.applications.app_head import Head
from src.applications.app_cut import Cut
from src.applications.app_uniq import Uniq
from src.applications.app_cd import Cd


class TestUnsafeDecorator(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    def test_unsafe_tail_call_required_function_with_extra_args(self):
        UnsafeDecorator(Tail()).exec(['1', '2', '3', '4'], None, self.out)
        self.assertEqual(self.out.popleft(), 'Invalid number of arguments\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_tail_with_num_of_files_and_stdin_without_stdin(self):
        UnsafeDecorator(Tail()).exec([], None, self.out)
        self.assertEqual(self.out.popleft(), 'No input given\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_tail_with_num_of_lines_and_stdin_without_num_lines(self):
        UnsafeDecorator(Tail()).exec(['not -n', 5], 'random text', self.out)
        self.assertEqual(self.out.popleft(), 'Invalid flags given\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_head_with_num_of_files_and_stdin_without_stdin(self):  # head
        UnsafeDecorator(Head()).exec([], None, self.out)
        self.assertEqual(self.out.popleft(), 'No input given\n')
        self.assertEqual(len(self.out), 0)

    def test_head_with_num_of_lines_and_stdin_without_num_lines(self):
        UnsafeDecorator(Head()).exec(['not -n', 5], 'random text', self.out)
        self.assertEqual(self.out.popleft(), 'Invalid flags given\n')
        self.assertEqual(len(self.out), 0)

    def test_head_call_required_function_with_extra_args(self):
        UnsafeDecorator(Head()).exec(['1', '2', '3', '4'], None, self.out)
        self.assertEqual(self.out.popleft(), 'Invalid number of arguments\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_cut_without_stdin(self):
        UnsafeDecorator(Cut()).exec(['-b', '0'], None, self.out)
        self.assertEqual(self.out.popleft(), 'No input given\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_cut_without_num_bytes(self):
        UnsafeDecorator(Cut()).exec(['not -n', 5], 'random text', self.out)
        self.assertEqual(self.out.popleft(), 'Invalid flags given\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_call_required_function_with_extra_args(self):
        UnsafeDecorator(Cut()).exec(['1', '2', '3', '4'], None, self.out)
        self.assertEqual(self.out.popleft(), 'Invalid number of arguments\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_call_required_function_with_no_args(self):
        UnsafeDecorator(Cut()).exec([], None, self.out)
        self.assertEqual(self.out.popleft(), 'Invalid number of arguments\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_uniq_no_arguments_no_stdin(self):
        UnsafeDecorator(Uniq()).exec([], None, self.out)
        self.assertEqual(self.out.popleft(), 'no arguments or stdin\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_uniq_flag_given_but_no_stdin(self):
        UnsafeDecorator(Uniq()).exec(['-i'], None, self.out)
        self.assertEqual(self.out.popleft(), 'no arguments or stdin\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_uniq_wrong_number_of_arguments(self):
        UnsafeDecorator(Uniq()).exec(['-i', 'test_uniq1.txt', 'test_uniq2.txt'], None, self.out)
        self.assertEqual(self.out.popleft(), 'wrong number of arguments\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_uniq_flag_at_incorrect_index(self):
        UnsafeDecorator(Uniq()).exec([os.path.join('resources', 'test_uniq1.txt'), '-i'], None, self.out)
        self.assertEqual(self.out.popleft(), 'Invalid flags given\n')
        self.assertEqual(len(self.out), 0)

    def test_unsafe_cd_multiple_arguments(self):
        UnsafeDecorator(Cd()).exec([os.path.join('resources', 'test_uniq1.txt'), '-i'], None, self.out)
        self.assertEqual(self.out.popleft(), 'Maximum of one argument expected\n')
        self.assertEqual(len(self.out), 0)

    def test_find_flag_not_provided(self):
        UnsafeDecorator(Cd()).exec([os.path.join('resources', 'test_uniq1.txt'), '-i'], None, self.out)
        self.assertEqual(self.out.popleft(), 'Maximum of one argument expected\n')
        self.assertEqual(len(self.out), 0)