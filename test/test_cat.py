import os
import shutil
import unittest
from collections import deque

from hypothesis import given, strategies

from src.applications.app_cat import Cat
from src.errors import ArgumentError


class TestCat(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        self.files = {
            'test1.txt': 'hello\nnice\nto\nmeet\nyou',
            'test2.txt': 'pleasure\nto\nmeet\nyou',
            'test3.txt': 'how\nare\nyou\ndoing'
        }

        os.chdir(self.directory)
        for file_name in self.files:
            with open(file_name, 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        os.chdir(self.original_directory)
        shutil.rmtree(self.directory)

    def test_cat_with_one_file(self):
        Cat().exec(['/test1.txt'], None, self.out)

        self.assertEqual(self.out.popleft(), self.files['test1.txt'])
        self.assertEqual(len(self.out), 0)

    def test_cat_with_single_file_and_number_flag(self):
        Cat().exec(['-n', '/test1.txt'], None, self.out)

        result = '\t1 hello\n\t2 nice\n\t3 to\n\t4 meet\n\t5 you'

        self.assertEqual(list(self.out), result)

    def test_cat_with_multiple_files(self):
        Cat().exec(['/test1.txt', '/test2.txt'], None, self.out)

        self.assertEqual(list(self.out),
                         [self.files['test1.txt'], self.files['test2.txt']])

    def test_cat_with_multiple_files_and_number_flag(self):
        Cat().exec(['-n', '/test1.txt', '/test2.txt'], None, self.out)

        result = ['\t1 hello\n\t2 nice\n\t3 to\n\t4 meet\n\t5 you',
                  '\t1 pleasure\n\t2 to\n\t3 meet\n\t4 you']

        self.assertEqual(list(self.out), result)

    @given(strategies.text())
    def test_cat_with_stdin(self, stdin):
        Cat().exec([], stdin, self.out)

        self.assertEqual(self.out.popleft(), stdin)
        self.assertEqual(len(self.out), 0)

    def test_cat_with_stdin_and_number_flag(self):
        Cat().exec(['-n'], 'how\nare\nyou\ndoing', self.out)

        self.assertEqual(self.out.popleft(),
                         '\t1 how\n\t2 are\n\t3 you\n\t4 doing')
        self.assertEqual(len(self.out), 0)

    def test_cat_without_stdin(self):
        app = Cat()

        self.assertRaises(ArgumentError, app.exec, [], None, self.out)
