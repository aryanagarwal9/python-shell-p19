import os
import shutil
import unittest
from collections import deque

from parameterized import parameterized

from src.applications.app_mkdir import Mkdir
from src.errors import DirectoryCreationError, ArgumentError


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
        ['single directory', ['dir1'], ['dir1']],
        ['multiple directories', ['dir1', 'dir2', 'dir3'],
         ['dir1', 'dir2', 'dir3']]
    ])
    def test_mkdir_final_directory(self, name, args, result):
        Mkdir().exec(args, None, self.out)
        expected_output = sorted(os.listdir())
        self.assertEqual(expected_output, result)

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

    @parameterized.expand([
        ['single directory', ['-v', 'dir1'], ['created directory: dir1\n']],
        ['multiple directories', ['-v', 'dir1', 'dir2', 'dir3'],
         ['created directory: dir1\n', 'created directory: dir2\n',
          'created directory: dir3\n']]
    ])
    def test_mkdir_verbose_flag(self, name, args, result):
        Mkdir().exec(args, None, self.out)
        expected_output = sorted(list(self.out))
        self.assertEqual(expected_output, result)

    @parameterized.expand([
        ['single directory', ['-p', '-v', 'dir1/dir2'],
         ['./dir1', './dir1/dir2'],
         ['created directory: dir1/dir2\n']],
        ['multiple directories',
         ['-v', '-p', 'dir1/dir2', 'dir2/dir3/dir4', 'dir1/dir5/dir7/dir2'],
         ['./dir1', './dir1/dir2', './dir1/dir5', './dir1/dir5/dir7',
          './dir1/dir5/dir7/dir2', './dir2', './dir2/dir3',
          './dir2/dir3/dir4'],
         ['created directory: dir1/dir2\n',
          'created directory: dir1/dir5/dir7/dir2\n',
          'created directory: dir2/dir3/dir4\n']]
    ])
    def test_mkdir_parent_and_verbose_flag(self, name, args, result_parent,
                                           result_verbose):
        Mkdir().exec(args, None, self.out)
        expected_output_parent = sorted([elem[0] for elem in os.walk('.')])
        expected_output_parent.remove('.')
        expected_output_verbose = sorted(list(self.out))
        self.assertEqual(expected_output_parent, result_parent)
        self.assertEqual(expected_output_verbose, result_verbose)

    def test_mkdir_file_not_found(self):
        app = Mkdir()
        self.assertRaises(DirectoryCreationError, app.exec, ['dir/dir2'], None,
                          self.out)

    def test_mkdir_file_already_exists(self):
        app = Mkdir()
        os.mkdir('dir1')
        self.assertRaises(DirectoryCreationError, app.exec, ['dir1'], None,
                          self.out)

    def test_mkdir_files_exist_and_not_found_and_created(self):
        app = Mkdir()
        os.mkdir('dir1')
        self.assertRaises(DirectoryCreationError, app.exec,
                          ['dir1', 'dir2/dir3', 'dir2'], None, self.out)
        self.assertEqual(sorted(os.listdir()), ['dir1', 'dir2'])

    @parameterized.expand([
        ['no arguments', []],
        ['one flag only', ['-p']],
        ['two flags only', ['-p', '-v']]
    ])
    def test_mkdir_no_directory_name_provided(self, name, args):
        app = Mkdir()
        self.assertRaises(ArgumentError, app.exec, args, None, self.out)

