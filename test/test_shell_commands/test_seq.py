import os
import shutil
import unittest
from collections import deque

from src.shell_commands.commands_visitor import CommandsVisitor


class TestSeq(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        with open(os.path.join(self.directory, 'test1.txt'), 'w') as file:
            file.write('line1\nline2\nline3')

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_seq_command(self):
        CommandsVisitor.converter(
            f'echo hello;cat {self.directory}/test1.txt').eval(None, self.out)
        self.assertEqual(list(self.out), ['hello\n', 'line1\nline2\nline3'])
