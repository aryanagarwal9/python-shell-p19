import os
import unittest
from collections import deque

from applications.app_tail import Tail


class TestTail(unittest.TestCase):
    # def __init__(self):
    #     super().__init__()
    #     self.test_file_name = 'test.txt'

    def setUp(self) -> None:
        self.out = deque()
        self.test_file_name = 'test.txt'
        test_str = "Line 1 \n Line 2 \n Line 3"
        with open(self.test_file_name, 'w') as f:
            f.write(test_str)

    def tearDown(self) -> None:
        os.remove(self.test_file_name)

    def test_tail_command(self):
        args = ['-n', '2', 'test.txt']
        Tail().exec(args=args, stdin=None, out=self.out)
        print(self.out)

if __name__ == '__main__':
    unittest.main()
