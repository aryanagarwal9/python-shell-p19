import os
import shutil
import unittest
from collections import deque
from parameterized import parameterized
from applications.app_sort import Sort
from errors import FlagError

class TestSort(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir('resources')

        self.files = {
            'test_sort.txt': 'java\npython\nc++\nc\nhaskell\nruby\nocaml'
        }

        with open(os.path.join(self.directory, 'test_sort.txt'), 'w') as file:
            file.write(self.files['test_sort.txt'])
        self.file_path = self.directory + '/test_sort.txt'

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_sort_for_file_input(self):
        Sort().exec([self.file_path], None, self.out)
        sorted_list_of_lines = sorted([line + '\n' for line in self.files['test_sort.txt'].split('\n')])
        self.assertEqual(list(self.out), sorted_list_of_lines)

    def test_sort_for_file_input_reverse(self):
        Sort().exec(['-r', self.file_path], None, self.out)
        sorted_list_of_lines_reverse = sorted([line + '\n' for line in self.files['test_sort.txt'].split('\n')],
                                              reverse=True)
        self.assertEqual(list(self.out), sorted_list_of_lines_reverse)

    @parameterized.expand([
        ['single_line_input', 'Hello I am Python', ['Hello I am Python\n']],
        ['multiple_line_input', 'Banana\nNetflix\nPython\nJava\nApple\nGoogle\nAmazon',
         sorted([line + '\n' for line in 'Banana\nNetflix\nPython\nJava\nApple\nGoogle\nAmazon'.split('\n')])]
    ])
    def test_sort_for_stdin(self, name, stdin, result):
        Sort().exec([], stdin, self.out)
        self.assertEqual(list(self.out), result)

    @parameterized.expand([
        ['single_line_input', 'Hello I am Python', ['Hello I am Python\n']],
        ['multiple_line_input', 'Banana\nNetflix\nPython\nJava\nApple\nGoogle\nAmazon',
         sorted([line + '\n' for line in 'Banana\nNetflix\nPython\nJava\nApple\nGoogle\nAmazon'.split('\n')], reverse=True)]
    ])
    def test_sort_for_stdin_reverse(self, name, stdin, result):
        Sort().exec(['-r'], stdin, self.out)
        self.assertEqual(list(self.out), result)

    def test_sort_with_no_arguments_no_stdin(self):
        app = Sort()
        self.assertRaises(ValueError, app.exec, args=[], stdin=None, out=self.out)

    def test_sort_only_flag_present_no_stdin(self):
        app = Sort()
        self.assertRaises(ValueError, app.exec, args=['-r'], stdin=None, out=self.out)

    def test_sort_flag_not_present_on_correct_index(self):
        app = Sort()
        self.assertRaises(FlagError, app.exec, args=[self.file_path, '-r'], stdin=None, out=self.out)