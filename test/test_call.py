import os
import shutil
import unittest
from collections import deque

from src.shell_commands.commands_visitor import CommandsVisitor

class TestCall(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir(self.directory)

        with open(os.path.join(self.directory, 'test1.txt'), 'w') as file:
            file.write('This\nis\na\ntesting\nfile\nfor\ncall\ncommand')

    def tearDown(self) -> None:
        shutil.rmtree(self.directory)

    def test_call_no_redirections(self):
        CommandsVisitor.converter(f'cat {self.directory}/test1.txt').\
            eval(None, self.out)
        self.assertEqual(list(self.out),
                         ['This\nis\na\ntesting\nfile\nfor\ncall\ncommand'])

    def test_call_input_redirection(self):
        CommandsVisitor.converter(f'cat < {self.directory}/test1.txt').eval(
            None, self.out)
        self.assertEqual(list(self.out),
                         ['This\nis\na\ntesting\nfile\nfor\ncall\ncommand'])

    def test_call_output_redirection(self):
        CommandsVisitor.converter(
            f'cat {self.directory}/test1.txt > {self.directory}/test2.txt').\
            eval(None, self.out)
        with open(os.path.join(self.directory, 'test2.txt'), 'r') as file:
            file_content = file.read()
        self.assertEqual(file_content,
                         'This\nis\na\ntesting\nfile\nfor\ncall\ncommand')
