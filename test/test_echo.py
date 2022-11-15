import unittest
from collections import deque

from applications.application import Echo

class TestEcho(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.out = deque()

    def test_argument_without_quotes(self):
        eval("echo hello", self.out)
        self.assertEqual(self.out.popleft(), "hello\n")

    def test_argument_joined_with_double_quotes(self):
        eval('echo "hello world"', self.out)
        self.assertEqual(self.out.popleft(), "hello world\n")

    def test_argument_joined_with_single_quotes(self):
        eval("echo 'hello world'", self.out)
        self.assertEqual(self.out.popleft(), "hello world\n")
