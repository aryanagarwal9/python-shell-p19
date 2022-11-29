import os
import shutil
import unittest
from collections import deque
from parameterized import parameterized

from src.applications.app_mkdir import Mkdir
from src.applications.unsafe_decorator import UnsafeDecorator
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
        ['single directory', ['dir1/dir2']],
        ['multiple directories', ['dir1/dir2', 'dir1/dir2/dir3']]
    ])
    def test_mkdir_sub_directories(self, name, args):
        os.mkdir('dir1')
        Mkdir().exec(args, None, self.out)
        expected_output = sorted([elem[0] for elem in os.walk('dir1')])
        self.assertEqual(expected_output, sorted(['dir1']+args))

    def test_mkdir_flag_final_directory(self):
        Mkdir().exec(['-p','dir1/dir2'], None, self.out)
        expected_output = os.listdir('dir1')
        self.assertEqual(expected_output, ['dir2'])

    def test_mkdir_unsafe_create_new_directories_even_if_some_arguments_exist(self):
        os.mkdir('dir1')
        self.assertEqual(UnsafeDecorator(Mkdir()).exec(['dir1','dir2','dir3'], None, self.out), 'FileExistsError\n')
        expected_output = sorted(os.listdir('dir1'))
        self.assertEqual(expected_output, ['dir2','dir3'])
