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

    def test_call_required_function_with_invalid_args(self):
        app = Tail()
        self.assertRaises(ArgumentError, app.exec, args=[], stdin=None, out=self.out)
        self.assertRaises(ArgumentError, app.exec, args=[1, 2, 3, 4], stdin=None, out=self.out)


    @parameterized.expand([
        ['zero_lines', ['-n', '0', 'test.txt'], None, []],
        ['one_line', ['-n', '1', 'test.txt'], None, ['Line 3']],
        ['two_lines', ['-n', '2', 'test.txt'], None, ['Line 2\n', 'Line 3']]
    ])
    def test_tail_command_with_3_args(self, name, args, stdin, result):
        Tail().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['lessLinesInArgs', ['-n', '0'], 'Line 2\nLine 3', []],
        ['moreLinesInArgs', ['-n', '3'], 'Line 2\nLine 3', ['Line 2\n', 'Line 3']],
        ['equalLinesInArgs', ['-n', '2'], 'Line 2\nLine 3', ['Line 2\n', 'Line 3']],
        ['newLineAtEndOfStr', ['-n', '2'], 'Line 2\nLine 3\n', ['Line 2\n', 'Line 3\n']]
    ])
    def test_tail_command_with_2_args(self, name, args, stdin, result):

        Tail().exec(args=args, stdin=stdin, out=self.out)

        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['fileWithMoreThan10Lines', ['test_with_more_lines.txt'], None, ['Line 2\n', 'Line 3\n', 'Line 4\n', 'Line 5\n',
                                                                         'Line 6\n', 'Line 7\n', 'Line 8\n', 'Line 9\n',
                                                                         'Line 10\n', 'Line 11']],
        ['fileWithLessThan10Lines', ['test.txt'], None, ['Line 1\n', 'Line 2\n', 'Line 3']]
    ])
    def test_tail_command_with_1_arg(self, name, args, stdin, result):
        Tail().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))


if __name__ == '__main__':
    unittest.main()
