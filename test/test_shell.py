import sys
import unittest
from collections import deque
import contextlib
from io import StringIO

import src.shell as shell
from src.errors import ArgumentError, FlagError


class TestShell(unittest.TestCase):

    def test_shell_non_interactive_mode(self):
        sys.argv = ['/comp0010/sh', '-c', 'echo foo']

        out = StringIO()
        with contextlib.redirect_stdout(out):
            shell.run()

        self.assertEqual('foo\n', out.getvalue())

    def test_shell_non_interactive_extra_args(self):
        sys.argv = ['/comp0010/sh', '-c', 'echo foo', 'echo bar']
        self.assertRaises(ArgumentError, shell.run)

    def test_shell_non_interactive_invalid_flag(self):
        sys.argv = ['/comp0010/sh', '-x', 'echo foo']
        self.assertRaises(FlagError, shell.run)

    def test_shell_eval(self):
        out = deque()
        shell.eval('echo foo', out)
        
        self.assertEqual(out.popleft(), 'foo\n')
