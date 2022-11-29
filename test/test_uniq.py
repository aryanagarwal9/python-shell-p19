import os
import shutil
import unittest
from collections import deque

from parameterized import parameterized

from src.applications.app_uniq import Uniq
from src.errors import FlagError, ArgumentError


class TestUniq(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir('resources')

        self.files = {
            'test_uniq1.txt': 'java\njava\npython\nPython\nc++\nc\nhaskell\n'
                              'haskell\nruby\nOcaml\nocaml\nhaskell',
            'test_uniq2.txt': 'java\npython\nc++\nc\nhaskell\nruby\nOcaml'
                              '\nhaskell\n'
        }
        for file_name in self.files:
            with open(os.path.join(self.directory, file_name), 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['duplicate_adjacent_lines_available', ['resources/test_uniq1.txt'],
         ['java\n', 'python\n', 'Python\n', 'c++\n',
          'c\n', 'haskell\n', 'ruby\n', 'Ocaml\n', 'ocaml\n', 'haskell']],
        ['no_duplicate_adjacent_lines', ['resources/test_uniq2.txt'],
         ['java\n', 'python\n', 'c++\n',
          'c\n', 'haskell\n', 'ruby\n', 'Ocaml\n', 'haskell\n']]
    ])
    def test_uniq_without_flag_file_input(self, name, args, result):
        Uniq().exec(args, None, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['duplicate_adjacent_lines_available',
         ['-i', 'resources/test_uniq1.txt'],
         ['java\n', 'python\n', 'c++\n', 'c\n',
          'haskell\n', 'ruby\n', 'Ocaml\n', 'haskell']],
        ['no_duplicate_adjacent_lines', ['-i', 'resources/test_uniq2.txt'],
         ['java\n', 'python\n', 'c++\n', 'c\n',
          'haskell\n', 'ruby\n', 'Ocaml\n', 'haskell\n']]
    ])
    def test_uniq_with_flag_file_input(self, name, args, result):
        Uniq().exec(args, None, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['single_line_input', 'London', ['London\n']],
        ['multiple_line_input',
         'London\nlondon\nParis\ndelhi\nDelhi\nBerlin\nBerlin\n',
         ['London\n', 'london\n', 'Paris\n', 'delhi\n', 'Delhi\n', 'Berlin\n']]
    ])
    def test_uniq_without_flag_stdin(self, name, stdin, result):
        Uniq().exec([], stdin, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['single_line_input', 'London', ['London\n']],
        ['multiple_line_input',
         'London\nlondon\nParis\ndelhi\nDelhi\nBerlin\nBerlin\n',
         ['London\n', 'Paris\n', 'delhi\n', 'Berlin\n']]
    ])
    def test_uniq_with_flag_stdin(self, name, stdin, result):
        Uniq().exec(['-i'], stdin, self.out)
        self.assertEqual(list(self.out), result)

    def test_uniq_no_arguments_no_stdin(self):
        app = Uniq()
        self.assertRaises(ArgumentError, app.exec, args=[], stdin=None,
                          out=self.out)

    def test_uniq_flag_given_but_no_stdin(self):
        app = Uniq()
        self.assertRaises(ArgumentError, app.exec, args=['-i'], stdin=None,
                          out=self.out)

    def test_uniq_wrong_number_of_arguments(self):
        app = Uniq()
        self.assertRaises(ArgumentError, app.exec,
                          args=['-i', 'test_uniq1.txt', 'test_uniq2.txt'],
                          stdin=None, out=self.out)
