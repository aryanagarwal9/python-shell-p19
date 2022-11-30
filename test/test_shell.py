import unittest
from collections import deque

from src.shell import eval


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        eval("echo foo", out)
        self.assertEqual(out.popleft(), "foo\n")
        self.assertEqual(len(out), 0)


if __name__ == "__main__":
    unittest.main()