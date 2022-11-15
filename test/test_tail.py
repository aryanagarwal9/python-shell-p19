import os
import unittest
from collections import deque
from parameterized import parameterized
from applications.app_tail import Tail


class TestTail(unittest.TestCase):


    def setUp(self) -> None:
        self.out = deque()
        self.test_file_name = 'test.txt'
        test_str = "Line 1\nLine 2\nLine 3"
        with open(self.test_file_name, 'w') as f:
            f.write(test_str)

    def tearDown(self) -> None:
        os.remove(self.test_file_name)


    def test_call_required_function_with_invalid_args(self):

    @parameterized.expand([
        ['zero_lines', ['-n', '0', 'test.txt'], None, []],
        ['one_line', ['-n', '1', 'test.txt'], None, ['Line 3']],
        ['two_lines', ['-n', '2', 'test.txt'], None, ['Line 2\n', 'Line 3']]
    ])
    def test_tail_command_with_3_args(self, name, args, stdin, result):
        Tail().exec(args=args, stdin=None, out=self.out)
        self.assertEqual(list(self.out), result)

    # def test_tail_command_with_2_args(self):
    #     args = ['-n', '2']
    #
    #     Tail().exec(args=args, stdin=None, out=self.out)
    #     result = ['Line 2\n', 'Line 3']
    #
    #     self.assertEqual(self.out, result)

if __name__ == '__main__':
    unittest.main()
