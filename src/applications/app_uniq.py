from collections import deque
from typing import Optional, List, Tuple

from src.applications.application import Application
from src.errors import ArgumentError
from src.utils import get_lines


class Uniq(Application):
    def __init__(self):
        self.flags = {'-i': False}

    def exec(self, args: list, stdin: Optional[str], out: deque) -> None:
        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: List[str], stdin: Optional[str],
                               out: deque) -> None:
        """check the number of args given and handle each case
        """
        self.validate_args(args, stdin)

        # Check for flag
        self.flags['-i'] = len(args) and args[0] == '-i'

        # Call required handler
        if (len(args) > 1 and self.flags['-i']) or (
                len(args) and not self.flags['-i']):
            self.handle_file_input(args, out)
        else:
            self.handle_stdin_input(stdin, out)

    @staticmethod
    def validate_args(args: list, stdin: Optional[str]) -> None:
        if len(args) > 2:
            raise ArgumentError("Invalid number of arguments")
        if not len(args) and stdin is None:
            raise ArgumentError('No arguments or stdin')
        if len(args) == 1 and args[0] == '-i' and stdin is None:
            raise ArgumentError('No arguments or stdin')

    def handle_file_input(self, args: list, out: deque) -> None:
        """Update out from file input
        """
        # Get lines from file
        file_name = args[0] if not self.flags['-i'] else args[1]
        lines = get_lines(src='file', file=file_name)

        # Iterate and compare adjacent lines
        for line in lines:
            temp_line, prev_line = self.get_required_lines(line, out)
            if prev_line is None or prev_line != temp_line:
                out.append(line)

    def handle_stdin_input(self, stdin: Optional[str], out: deque) -> None:
        """Update out from stdin
        """
        # Get lines from stdin
        stdin_input = stdin.splitlines()

        # Iterate and compare adjacent lines
        for line in stdin_input:
            temp_line, prev_line = self.get_required_lines(line, out)
            if prev_line is None or prev_line.rstrip('\n') != temp_line:
                out.append(line + '\n')

    def get_required_lines(self, line: str, out: deque) -> Tuple[str, str]:
        """Returns adjacent lines"""
        temp_line = line.lower() if self.flags['-i'] else line
        prev_line = None

        if not len(out):
            return temp_line, prev_line

        prev_line = out[-1].lower() if self.flags['-i'] else out[-1]

        return temp_line, prev_line
