import os
import unittest
from collections import deque
from parameterized import parameterized
from applications.app_tail import Tail
from errors import ArgumentError


class TestTail(unittest.TestCase):


    def setUp(self) -> None:
        self.out = deque()
        self.test_file = 'test.txt'
        test_str = "Line 1\nLine 2\nLine 3"
        with open(self.test_file, 'w') as f:
            f.write(test_str)

        self.test_file_with_more_lines = 'test_with_more_lines.txt'
        test_str = 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10\nLine 11'
        with open(self.test_file_with_more_lines, 'w') as f:
            f.write(test_str)

    def tearDown(self) -> None:
        os.remove(self.test_file)
        os.remove(self.test_file_with_more_lines)

    def test_call_required_function_with_extra_args(self):
        app = Tail()
        self.assertRaises(ArgumentError, app.exec, args=[1, 2, 3, 4], stdin=None, out=self.out)


    @parameterized.expand([
        ['zero_lines', ['-n', '0', 'test.txt'], []],
        ['one_line', ['-n', '1', 'test.txt'], ['Line 3']],
        ['two_lines', ['-n', '2', 'test.txt'], ['Line 2\n', 'Line 3']]
    ])
    def test_tail_with_num_of_lines_and_file_input(self, name, args, result):
        Tail().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['zeroLinesInArgs', ['-n', '0'], 'Line 2\nLine 3', []],
        ['lessLinesInArgs', ['-n', '0'], 'Line 2\nLine 3', []],
        ['moreLinesInArgs', ['-n', '3'], 'Line 2\nLine 3', ['Line 2\n', 'Line 3']],
        ['equalLinesInArgs', ['-n', '2'], 'Line 2\nLine 3', ['Line 2\n', 'Line 3']],
        ['newLineAtEndOfStr', ['-n', '2'], 'Line 2\nLine 3\n', ['Line 2\n', 'Line 3\n']]
    ])
    def test_tail_with_num_of_lines_and_stdin(self, name, args, stdin, result):

        Tail().exec(args=args, stdin=stdin, out=self.out)

        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['fileWithMoreThan10Lines', ['test_with_more_lines.txt'], ['Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n',
                                                                         'Line 6\n', 'Line 7\n', 'Line 8\n', 'Line 9\n',
                                                                         'Line 10\n', 'Line 11']],
        ['fileWithLessThan10Lines', ['test.txt'], ['Line 1\n', 'Line 2\n', 'Line 3']]
    ])
    def test_tail_with_only_file_input(self, name, args, result):
        Tail().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['fileWithMoreThan10Lines', '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11', ['2\n', '3\n', '4\n', '5\n', '6\n',
                                                                          '7\n', '8\n', '9\n', '10\n', '11']],
        ['fileWithLessThan10Lines', '1\n2\n3', ['1\n', '2\n', '3']]
    ])
    def test_tail_with_only_stdin_input(self, name, stdin, result):
        Tail().exec(args=[], stdin=stdin, out=self.out)
        self.assertEqual(result, list(self.out))

