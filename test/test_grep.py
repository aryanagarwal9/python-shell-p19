import os
import shutil
import unittest
from collections import deque
from parameterized import parameterized

from src.applications.app_grep import Grep


class TestGrep(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        self.files = {
            'test1.txt': 'hello the app name is grep\ngrep is used to search for a pattern\nUsed in shell',
            'test2.txt': 'this coursework is about implementing a shell\nI enjoyed the experience',
            'test3.txt': 'class for testing grep\nmaking unit tests to test app',
        }

        for file_name in self.files:
            with open(os.path.join(self.directory, file_name), 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['one_file_input', ['hel', 'resources/test1.txt'], ['hello the app name is grep\n', 'Used in shell\n']],
        ['multiple_file_input', ['gre', 'resources/test1.txt', 'resources/test2.txt', 'resources/test3.txt'], [
            'resources/test1.txt:hello the app name is grep\n',
            'resources/test1.txt:grep is used to search for a pattern\n',
            'resources/test3.txt:class for testing grep\n']]
    ])
    def test_grep_file_input(self, name, args, result):
        Grep().exec(args, None, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['no_match_present', ['hel'], 'hi\nI hope you have a good day', []],
        ['matches_present', ['hel'], 'hello\nI am glad to see you\nLets work on shell\n', ['hello\n'
                                                                                           , 'Lets work on shell\n']]
    ])
    def test_grep_stdin(self, name, args, stdin, result):
        Grep().exec(args, stdin, self.out)
        self.assertEqual(list(self.out), result)

    def test_grep_no_files_no_stdin(self):
        app = Grep()
        self.assertRaises(ValueError, app.exec, ['pattern'], None, self.out)

    def test_grep_no_pattern_provided(self):
        app = Grep()
        self.assertRaises(ValueError, app.exec, [], None, self.out)

    def test_grep_no_pattern_provided_but_stdin_given(self):
        app = Grep()
        self.assertRaises(ValueError, app.exec, [], 'hello', self.out)
