import sys
import unittest

import src.shell as shell
from src.errors import ArgumentError, FlagError


class TestShell(unittest.TestCase):

    def test_shell_non_interactive_mode(self):
        sys.argv = ['/comp0010/sh', '-c', 'echo foo']


    def test_shell_non_interactive_extra_args(self):
        sys.argv = ['/comp0010/sh', '-c', 'echo foo', 'echo bar']
        args = sys.argv

        self.assertRaises(ArgumentError, shell.run)

    def test_shell_non_interactive_invalid_flag(self):
        sys.argv = ['/comp0010/sh', '-x', 'echo foo']
        args = sys.argv

        self.assertRaises(FlagError, shell.run)


if __name__ == "__main__":
    unittest.main()
