import os
import shutil
import unittest
from collections import deque
from hypothesis import given, strategies
from parameterized import parameterized
from applications.app_sort import Sort

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
        self.file_path = self.directory+'/test_sort.txt'

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_sort_for_file_input(self):
        Sort().exec([self.file_path], None, self.out)
        sorted_list_of_lines = sorted([line+'\n' for line in self.files['test_sort.txt'].split('\n')])
        self.assertEqual(list(self.out), sorted_list_of_lines)

    def test_sort_for_file_input_reverse(self):
        Sort().exec(['-r', self.file_path], None, self.out)
        sorted_list_of_lines_reverse = sorted([line+'\n' for line in self.files['test_sort.txt'].split('\n')], reverse=True)
        self.assertEqual(list(self.out), sorted_list_of_lines_reverse)

    @parameterized.expand()
    def test_sort_for_stdin(self):
        # stdin = 'java\npython\nc++\nc\nhaskell\nruby\nocaml'
        Sort().exec([], stdin, self.out)
        print(stdin)
        sorted_list_of_lines = sorted([line+'\n' for line in stdin.split('\n')])
        self.assertEqual(list(self.out), sorted_list_of_lines)

    def test_sort_for_stdin_reverse(self, stdin: str):
        Sort().exec(['-r'], stdin, self.out)
        sorted_list_of_lines_reverse = sorted([line+'\n' for line in stdin.split('\n')], reverse=True)
        self.assertEqual(list(self.out), sorted_list_of_lines_reverse)


if __name__=='__main__':
    unittest.main()