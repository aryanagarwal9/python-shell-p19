import os
import shutil
import unittest
from collections import deque
from parameterized import parameterized
from src.applications.app_head import Head
from src.errors import ArgumentError, FlagError, StandardInputError


class TestHead(unittest.TestCase):

    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        self.files = {
            'test1.txt': 'Line 1\nLine 2\nLine 3',
            'test2.txt': 'Line 1\nLine 2\nLine 3\nLine 4\nLine 5\nLine 6\nLine 7\nLine 8\nLine 9\nLine 10\nLine 11',
        }

        for file_name in self.files:
            with open(os.path.join(self.directory, file_name), 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['zero_lines', ['-n', '0', 'resources/test1.txt'], []],
        ['one_line', ['-n', '1', 'resources/test1.txt'], ['Line 1\n']],
        ['two_lines', ['-n', '2', 'resources/test1.txt'], ['Line 1\n', 'Line 2\n']]
    ])
    def test_head_with_num_of_lines_and_file_input(self, name, args, result):
        Head().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['fileWithMoreThan10Lines', ['resources/test2.txt'], ['Line 1\n', 'Line 2\n', 'Line 3\n', 'Line 4\n',
                                                              'Line 5\n', 'Line 6\n', 'Line 7\n', 'Line 8\n',
                                                              'Line 9\n', 'Line 10\n']],
        ['fileWithLessThan10Lines', ['resources/test1.txt'], ['Line 1\n', 'Line 2\n', 'Line 3\n']]
    ])
    def test_head_with_only_file_input(self, name, args, result):
        Head().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['zeroLinesInArgs', ['-n', '0'], 'Line 2\nLine 3', []],
        ['lessLinesInArgs', ['-n', '1'], 'Line 2\nLine 3', ['Line 2\n']],
        ['moreLinesInArgs', ['-n', '3'], 'Line 2\nLine 3', ['Line 2\n', 'Line 3\n']],
        ['equalLinesInArgs', ['-n', '2'], 'Line 2\nLine 3', ['Line 2\n', 'Line 3\n']],
        ['newLineAtEndOfStr', ['-n', '2'], 'Line 2\nLine 3\n', ['Line 2\n', 'Line 3\n']]
    ])
    def test_head_with_num_of_lines_and_stdin(self, name, args, stdin, result):
        Head().exec(args=args, stdin=stdin, out=self.out)

        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['fileWithMoreThan10Lines', '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11', ['1\n', '2\n', '3\n', '4\n', '5\n', '6\n',
                                                                          '7\n', '8\n', '9\n', '10\n']],
        ['fileWithLessThan10Lines', '1\n2\n3', ['1\n', '2\n', '3\n']]
    ])
    def test_head_with_only_stdin(self, name, stdin, result):
        Head().exec(args=[], stdin=stdin, out=self.out)
        self.assertEqual(result, list(self.out))

    def test_head_with_num_of_files_and_stdin_without_stdin(self):
        app = Head()
        self.assertRaises(StandardInputError, app.exec, args=[], stdin=None, out=self.out)

    def test_head_with_num_of_lines_and_stdin_without_num_lines(self):
        app = Head()
        self.assertRaises(FlagError, app.exec, args=['not -n', '5'], stdin='random text', out=self.out)

    def test_call_required_function_with_extra_args(self):
        app = Head()
        self.assertRaises(ArgumentError, app.exec, args=['1', '2', '3', '4'], stdin=None, out=self.out)


