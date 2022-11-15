import os
import unittest
from collections import deque

from applications.application import Pwd

class TestPwd(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.out = deque()

    def pwd_command(self):
        eval("pwd", out)
        self.assertEqual(self.out.popleft(), os.getcwd())


