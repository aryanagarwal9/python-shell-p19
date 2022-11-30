import os
import shutil
import unittest
from collections import deque

from parameterized import parameterized

from src.applications.app_cut import Cut
from src.errors import ArgumentError, FlagError, StandardInputError


class TestHead(unittest.TestCase):

    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        self.files = {
            'test1.txt': '1234\n5678\n'
        }

        for file_name in self.files:
            with open(os.path.join(self.directory, file_name), 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['single_byte', ['-b', '1', 'resources/test1.txt'], ['1\n', '5\n']],
        ['multiple_single_bytes', ['-b', '1,2', 'resources/test1.txt'],
         ['12\n', '56\n']],
        ['out_of_range_bytes', ['-b', '1,2,8', 'resources/test1.txt'],
         ['12\n', '56\n']],
        ['single_byte_interval', ['-b', '1-3', 'resources/test1.txt'],
         ['123\n', '567\n']],
        ['multiple_byte_intervals', ['-b', '1-1,2-3', 'resources/test1.txt'],
         ['123\n', '567\n']],
        ['mixed_byte_intervals', ['-b', '-2,3-', 'resources/test1.txt'],
         ['1234\n', '5678\n']],
        ['overlapping_byte_intervals', ['-b', '1-,2-', 'resources/test1.txt'],
         ['1234\n', '5678\n']],
        ['out_of_range_byte_interval', ['-b', '1-9', 'resources/test1.txt'],
         ['1234\n', '5678\n']],
        ['unsorted_single_bytes', ['-b', '3,1,2', 'resources/test1.txt'],
         ['123\n', '567\n']],
        ['unsorted_byte_intervals', ['-b', '2-3,1-2', 'resources/test1.txt'],
         ['123\n', '567\n']],
        ['reversed_byte_interval', ['-b', '3-1', 'resources/test1.txt'],
         ['\n', '\n']],
        ['bytes_and_interval', ['-b', '1,2-3', 'resources/test1.txt'],
         ['123\n', '567\n']]
    ])
    def test_cut_with_file_input(self, name, args, result):
        Cut().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(result, list(self.out))

    @parameterized.expand([
        ['single_byte', ['-b', '1'], '1234\n5678\n', ['1\n', '5\n']],
        ['multiple_single_bytes', ['-b', '1,2'], '1234\n5678\n',
         ['12\n', '56\n']],
        ['out_of_range_bytes', ['-b', '1,2,8'], '1234\n5678\n',
         ['12\n', '56\n']],
        ['single_byte_interval', ['-b', '1-3'], '1234\n5678\n',
         ['123\n', '567\n']],
        ['multiple_byte_intervals', ['-b', '1-2,2-4'], '1234\n5678\n',
         ['1234\n', '5678\n']],
        ['out_of_range_byte_interval', ['-b', '1-9'], '1234\n5678\n',
         ['1234\n', '5678\n']],
        ['unsorted_single_bytes', ['-b', '3,1,2'], '1234\n5678\n',
         ['123\n', '567\n']],
        ['unsorted_byte_intervals', ['-b', '2-3,1-2'], '1234\n5678\n',
         ['123\n', '567\n']],
        ['reversed_byte_interval', ['-b', '3-1'], '1234\n5678\n',
         ['\n', '\n']],
        ['bytes_and_interval', ['-b', '1,2-3'], '1234\n5678\n',
         ['123\n', '567\n']]
    ])
    def test_cut_with_stdin(self, name, args, stdin, result):
        Cut().exec(args=args, stdin=stdin, out=self.out)

        self.assertEqual(result, list(self.out))

    def test_cut_without_stdin(self):
        app = Cut()
        self.assertRaises(StandardInputError, app.exec, args=['-b', '1'],
                          stdin=None, out=self.out)

    def test_cut_without_num_bytes(self):
        app = Cut()
        self.assertRaises(FlagError, app.exec, args=['not -n', 5],
                          stdin='random text', out=self.out)

    def test_call_required_function_with_extra_args(self):
        app = Cut()
        self.assertRaises(ArgumentError, app.exec, args=[1, 2, 3, 4],
                          stdin=None, out=self.out)

    def test_call_required_function_with_no_args(self):
        app = Cut()
        self.assertRaises(ArgumentError, app.exec, args=[], stdin=None,
                          out=self.out)

    @parameterized.expand([
        ['no_byte_order', ['-b', None, 'resources/test1.txt']],
        ['char_a_in_byte_order', ['-b', '1,a', 'resources/test1.txt']],
        ['double_comma', ['-b', '1,,2', 'resources/test1.txt']]
    ])
    def test_call_required_function_with_invalid_byte_order(self, name, args):
        app = Cut()
        self.assertRaises(ArgumentError, app.exec, args=args, stdin=None,
                          out=self.out)

    def test_get_cut_str(self):
        app = Cut()
        self.assertRaises(ArgumentError, app.get_cut_str, line='foo',
                          byte_order='1,,2')
