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
        cmdline = f'find {self.directory} -name test | grep is'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Pipe(Call('find', [self.directory, '-name', 'test'], None, None),
                               Call('grep', ['is'], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_nested_pipe_command(self):
        cmdline = f'find {self.directory} -name test | grep is | echo'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Pipe(
            Pipe(Call('find', [self.directory, '-name', 'test'], None, None), Call('grep', ['is'], None, None)),
            Call('echo', [], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_seq_command(self):
        cmdline = 'echo hello;echo bye'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Seq(Call('echo', ['hello'], None, None), Call('echo', ['bye'], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_call_command(self):
        cmdline = f'grep test {self.directory}/test1.txt'
        shell_command= CommandsVisitor.converter(cmdline)
        expected_output = Call('grep', ['test', 'resources/test1.txt'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_single_quote(self):
        cmdline = "echo 'hello world'"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('echo', ['hello world'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_back_quote_in_double_quote(self):
        cmdline = f"echo `cat {self.directory}/test1.txt`"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('echo', ['This', 'is', 'a', 'testing', 'file', 'for', 'command', 'visitor'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_nested_seq_command(self):
        cmdline = "sort test1.txt ; cat test1.txt"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Seq(Call('sort', ['test1.txt'], None, None), Call('cat',['test1.txt'], None, None))
        self.assertEqual(shell_command, expected_output)







    