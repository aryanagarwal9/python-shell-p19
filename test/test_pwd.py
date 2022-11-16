import os
import unittest
from collections import deque

from applications.app_pwd import Pwd

class TestPwd(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    def test_pwd_command(self):
        Pwd().exec([], None, self.out)
        self.assertEqual(self.out.popleft(), os.getcwd())
        self.assertEqual(len(self.out), 0)


if __name__ == '__main__':
    unittest.main()


