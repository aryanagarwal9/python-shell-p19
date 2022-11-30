import os
import shutil
import unittest
from collections import deque

from src.shell_commands.commands_visitor import CommandsVisitor


class TestPipe(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        with open(os.path.join(self.directory, 'test1.txt'), 'w') as file:
            file.write('line1\nline2\nline3')

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_pipe_command(self):
        CommandsVisitor.converter(f'echo {self.directory}/test* | cat').eval(
            None, self.out)
        self.assertEqual(list(self.out), ['resources/test1.txt\n'])
