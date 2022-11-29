from collections import deque
from typing import Optional

from src.applications.application import Application
from src.errors import ArgumentError
from src.utils import check_flag


class Sort(Application):
    def __init__(self):
        self.flags = {'-r': False}

    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args) > 2:
            raise ArgumentError('Wrong number of arguments')

        self.flags['-r'] = len(args) and args[0] == '-r'

        if self.is_file_input_available(args):
            self.handle_file_input(args, out)
        elif self.is_stdin_available(stdin):
            self.handle_stdin(stdin, out)
        else:
            raise ArgumentError('No arguments or stdin')

    def handle_file_input(self, args: list, out: deque):
        file_name = args[0] if len(args) == 1 else args[1]
        with open(file_name, 'r') as file:
            for line in sorted(file.readlines(), reverse=self.flags['-r']):
                out.append(line) if line.endswith('\n') else out.append(
                    line + '\n')

    def handle_stdin(self, stdin: Optional[str], out: deque):
        for line in sorted(stdin.splitlines(), reverse=self.flags['-r']):
            out.append(line + '\n')

    def is_file_input_available(self, args: list):
        if len(args) > 1:
            check_flag(args[0], '-r')
            return True
        return len(args) and not self.flags['-r']

    @staticmethod
    def is_stdin_available(stdin: Optional[str]):
        return stdin is not None
