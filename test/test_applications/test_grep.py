import os
import shutil
import unittest
from collections import deque

from parameterized import parameterized

from src.applications.app_grep import Grep
from src.errors import ArgumentError


class TestGrep(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        self.files = {
            'test1.txt': 'hello the app name is grep\n'
                         'grep is used to search for a pattern\nUsed in shell',
            'test2.txt': 'this coursework is about implementing a shell\n'
                         'I enjoyed the experience',
            'test3.txt': 'class for testing grep\n'
                         'making unit tests to test app',
        }

        for file_name in self.files:
            with open(os.path.join(self.directory, file_name), 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['one_file_input', ['hel', 'resources/test1.txt'],
         ['hello the app name is grep\n', 'Used in shell\n']],
        ['multiple_file_input',
         ['gre', 'resources/test1.txt', 'resources/test2.txt',
          'resources/test3.txt'], [
             'resources/test1.txt:hello the app name is grep\n',
             'resources/test1.txt:grep is used to search for a pattern\n',
             'resources/test3.txt:class for testing grep\n']]
    ])
    def test_grep_file_input(self, name, args, result):
        Grep().exec(args, None, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['one_file_input', ['-v', 'app', 'resources/test1.txt'],
         ['grep is used to search for a pattern\n', 'Used in shell\n']],
        ['multiple_file_input',
         ['-v', 'is', 'resources/test1.txt', 'resources/test2.txt',
          'resources/test3.txt'], [
             'resources/test1.txt:Used in shell\n',
             'resources/test2.txt:I enjoyed the experience\n',
             'resources/test3.txt:class for testing grep\n',
             'resources/test3.txt:making unit tests to test app\n']]
    ])
    def test_grep_invert_match_file_input(self, name, args, result):
        Grep().exec(args, None, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['no_match_present', ['hel'], 'hi\nI hope you have a good day', []],
        ['matches_present', ['hel'],
         'hello\nI am glad to see you\nLets work on shell\n',
         ['hello\n', 'Lets work on shell\n']]
    ])
    def test_grep_stdin(self, name, args, stdin, result):
        Grep().exec(args, stdin, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['one_file_input', ['-v', 'grep'], 'Use grep\nUsed in shell\n',
         ['Used in shell\n']],
        ['multiple_file_input', ['-v', 'is'], 'Grep is good\nUsed in shell\n',
         ['Used in shell\n']]
    ])
    def test_grep_invert_match_stdin(self, name, args, stdin, result):
        Grep().exec(args, stdin, self.out)
        self.assertEqual(list(self.out), result)

    def test_grep_no_files_no_stdin(self):
        app = Grep()
        self.assertRaises(ArgumentError, app.exec, ['pattern'], None, self.out)

    def test_grep_no_pattern_provided(self):
        app = Grep()
        self.assertRaises(ArgumentError, app.exec, [], None, self.out)

    def test_grep_no_pattern_provided_but_stdin_given(self):
        app = Grep()
        self.assertRaises(ArgumentError, app.exec, [], 'hello', self.out)
