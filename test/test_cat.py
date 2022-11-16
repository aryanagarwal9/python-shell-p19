import os
import shutil
import unittest
from collections import deque

from hypothesis import given, strategies

from applications.app_cat import Cat

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

        for file_name in self.files:
            with open(os.path.join(self.directory, file_name),'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_cat_with_one_file(self):
        Cat().exec([self.directory+'/test1.txt'], None, self.out)
        self.assertEqual(self.out.popleft(), self.files['test1.txt'])
        self.assertEqual(len(self.out), 0)

    def test_cat_with_multiple_files(self):
        Cat().exec([self.directory+'/test1.txt', self.directory+'/test2.txt'], None, self.out)
        self.assertEqual(self.out.popleft(), self.files['test1.txt']+self.files['test2.txt'])
        self.assertEqual(len(self.out), 0)

    @given(strategies.text())
    def test_cat_with_stdin(self, stdin):
        Cat().exec([], stdin, self.out)
        self.assertEqual(self.out.popleft(), stdin)
        self.assertEqual(len(self.out), 0)
        