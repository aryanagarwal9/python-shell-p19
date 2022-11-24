import os
import shutil

from src.shell_commands.commands_visitor import CommandsVisitor
from src.shell_commands.commands.pipe import Pipe
from src.shell_commands.commands.call import Call
from src.shell_commands.commands.seq import Seq

import unittest
from collections import deque


class TestCommandVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        self.files = {
            'test1.txt': 'This\nis\na\ntesting\nfile\nfor\ncommand\nvisitor\n'
        }

        for file_name in self.files:
            with open(os.path.join(self.directory, file_name), 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_visitor_one_pipe_command(self):
        cmdline = f'find {self.directory} -name test* | grep is'
        shell_command = CommandsVisitor().converter(cmdline)
        expected_output = Pipe(Call('find', [self.directory, '-name', 'test*'], None, None),
                               Call('grep', ['is'], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_nested_pipe_command(self):
        cmdline = f'find {self.directory} -name test* | grep is | echo'
        shell_command = CommandsVisitor().converter(cmdline)
        expected_output = Pipe(
            Pipe(Call('find', [self.directory, '-name', 'test*'], None, None), Call('grep', ['is'], None, None)),
            Call('echo', [], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_seq_command(self):
        cmdline = 'echo hello;echo bye'
        shell_command = CommandsVisitor().converter(cmdline)
        expected_output = Seq(Call('echo', ['hello'], None, None), Call('echo', ['hello'], None, None))
        self.assertEqual(shell_command, expected_output)

    