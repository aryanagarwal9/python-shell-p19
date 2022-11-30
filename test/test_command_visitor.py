import os
import shutil
import unittest
from collections import deque

from src.errors import ParseError
from src.shell_commands.commands.call import Call
from src.shell_commands.commands.pipe import Pipe
from src.shell_commands.commands.seq import Seq
from src.shell_commands.commands_visitor import CommandsVisitor


class TestCommandVisitor(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        self.original_directory = os.getcwd()
        os.mkdir(self.directory)
        os.chdir(self.directory)

        self.files = {
            'test1.txt': 'This\nis\na\ntesting\nfile\nfor\ncommand\nvisitor\n',
            'test2.txt': 'This\nis\ntesting\nfile2\nfor\ncommand\nvisitor\n'
        }

        for file_name in self.files:
            with open(file_name, 'w') as file:
                file.write(self.files[file_name])

    def tearDown(self) -> None:
        os.chdir(self.original_directory)
        shutil.rmtree(self.directory)

    def test_visitor_one_pipe_command(self):
        cmdline = 'find -name test | grep is'
        shell_command = CommandsVisitor().converter(cmdline)
        expected_output = Pipe(Call('find', ['-name', 'test'], None, None),
                               Call('grep', ['is'], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_nested_pipe_command(self):
        cmdline = 'find -name test | grep is | echo'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Pipe(
            Pipe(Call('find', ['-name', 'test'], None, None),
                 Call('grep', ['is'], None, None)),
            Call('echo', [], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_seq_command(self):
        cmdline = 'echo hello;echo bye'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Seq(Call('echo', ['hello'], None, None),
                              Call('echo', ['bye'], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_call_command(self):
        cmdline = 'grep test test1.txt'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('grep', ['test', 'test1.txt'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_nested_seq_command(self):
        cmdline = 'sort test1.txt ; cat test1.txt'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Seq(Call('sort', ['test1.txt'], None, None),
                              Call('cat', ['test1.txt'], None, None))
        self.assertEqual(shell_command, expected_output)

    def test_visitor_single_quoted(self):
        cmdline = "echo 'hello world'"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('echo', ['hello world'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_back_quote_in_single_quote(self):
        cmdline = "echo 'Hello `cat test1.txt`'"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('echo', ['Hello `cat test1.txt`'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_single_quote_disabled_globbing(self):
        cmdline = "echo 'tes*'"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call("echo", ['tes*'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_double_quoted(self):
        cmdline = 'grep test "text1.txt"'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('grep', ['test', "text1.txt"], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_back_quote_in_double_quote(self):
        cmdline = 'echo "Hello `cat test1.txt`"'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('echo',
                               ['Hello This is a testing file for command visitor '],
                               None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_unquoted(self):
        cmdline = "cat test1.txt"
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('cat', ['test1.txt'], None, None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_input_redirection(self):
        cmdline = 'cat < test1.txt'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('cat', [], 'test1.txt', None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_globbing(self):
        cmdline = 'cat ./*'
        shell_command = CommandsVisitor.converter(cmdline)
        expected_output = Call('cat', ['./test1.txt', './test2.txt'], None,
                               None)
        self.assertEqual(shell_command, expected_output)

    def test_visitor_many_inputs_parse_error(self):
        cmdline = 'cat hello > test1.txt > test2.txt '
        with self.assertRaises(ParseError):
            CommandsVisitor.converter(cmdline)
