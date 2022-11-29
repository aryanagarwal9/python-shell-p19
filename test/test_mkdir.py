import os
import shutil
import unittest
from collections import deque

from parameterized import parameterized

from src.applications.app_mkdir import Mkdir


class TestMkdir(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        self.original_directory = os.getcwd()
        os.mkdir(self.directory)
        os.chdir(self.directory)

    def tearDown(self) -> None:
        os.chdir(self.original_directory)
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['single directory', ['dir1']],
        ['multiple directories', ['dir1', 'dir2', 'dir3']]
    ])
    def test_mkdir_final_directory(self, name, args):
        Mkdir().exec(args, None, self.out)
        expected_output = sorted(os.listdir())
        self.assertEqual(expected_output, sorted(args))

    @parameterized.expand([
        ['single directory', ['dir1/dir2'], ['dir1/dir2']],
        ['multiple directories', ['dir1/dir2', 'dir1/dir2/dir3'],
         ['dir1/dir2', 'dir1/dir2/dir3']]
    ])
    def test_mkdir_sub_directories(self, name, args, result):
        os.mkdir('dir1')
        Mkdir().exec(args, None, self.out)
        expected_output = sorted([elem[0] for elem in os.walk('dir1')])
        expected_output.remove('dir1')
        self.assertEqual(expected_output, sorted(result))

    @parameterized.expand([
        ['single directory', ['-p', 'dir1/dir2'], ['./dir1', './dir1/dir2']],
        ['multiple directories',
         ['-p', 'dir1/dir2', 'dir2/dir3/dir4', 'dir1/dir5/dir7/dir2'],
         ['./dir1', './dir1/dir2', './dir1/dir5', './dir1/dir5/dir7',
          './dir1/dir5/dir7/dir2', './dir2', './dir2/dir3',
          './dir2/dir3/dir4']]
    ])
    def test_mkdir_parent_flag(self, name, args, result):
        Mkdir().exec(args, None, self.out)
        expected_output = sorted([elem[0] for elem in os.walk('.')])
        expected_output.remove('.')
        self.assertEqual(expected_output, sorted(result))

