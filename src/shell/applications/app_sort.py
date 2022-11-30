from collections import deque
from typing import Optional, List

from shell.applications.application import Application
from shell.errors import ArgumentError
from shell.utils import check_flag


class Sort(Application):
    def __init__(self):
        self.flags = {'-r': False}

    def exec(self, args: List[str], stdin: Optional[str], out: deque) -> None:
        """
        -r flag: reverse the result of comparisons
        """
        if len(args) > 2:
            raise ArgumentError('Wrong number of arguments')

        # Check for flag
        self.flags['-r'] = len(args) and args[0] == '-r'

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: List[str], stdin: Optional[str],
                               out: deque):
        if self.is_file_input_available(args):
            self.handle_file_input(args, out)
        elif self.is_stdin_available(stdin):
            self.handle_stdin(stdin, out)
        else:
            raise ArgumentError('No arguments or stdin')

    def handle_file_input(self, args: List[str], out: deque) -> None:
        file_name = args[0] if len(args) == 1 else args[1]

        with open(file_name, 'r') as file:
            for line in sorted(file.readlines(), reverse=self.flags['-r']):
                out.append(line) if line.endswith('\n') else out.append(
                    line + '\n')

    def handle_stdin(self, stdin: Optional[str], out: deque) -> None:
        for line in sorted(stdin.splitlines(), reverse=self.flags['-r']):
            out.append(line + '\n')

    def is_file_input_available(self, args: List[str]) -> bool:
        # Flag should be at the right position
        if len(args) > 1:
            check_flag(args[0], '-r')
            return True

        return len(args) and not self.flags['-r']

    @staticmethod
    def is_stdin_available(stdin: Optional[str]) -> bool:
        return stdin is not None
