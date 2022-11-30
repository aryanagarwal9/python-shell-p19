from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError


class Uniq(Application):
    def __init__(self):
        self.flags = {'-i': False}

    def exec(self, args: List[str], stdin: Optional[str], out: deque) -> None:
        if len(args) > 2:
            raise ArgumentError("Invalid number of arguments")

        if not len(args) and stdin is None:
            raise ArgumentError('No arguments or stdin')

        if len(args) == 1 and args[0] == '-i' and stdin is None:
            raise ArgumentError('No arguments or stdin')

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: List[str], stdin: Optional[str],
                               out: deque) -> None:
        self.flags['-i'] = len(args) and args[0] == '-i'
        if (len(args) > 1 and self.flags['-i']) or (
                len(args) and not self.flags['-i']):
            self.handle_file_input(args, out)
        else:
            self.handle_stdin_input(stdin, out)

    def handle_file_input(self, args: List[str], out: deque) -> None:
        file_name = args[0] if not self.flags['-i'] else args[1]
        with open(file_name, 'r') as file:
            for line in file.readlines():
                temp_line, prev_line = self.get_required_lines(line, out)
                if prev_line is None or prev_line != temp_line:
                    out.append(line)

    def handle_stdin_input(self, stdin: Optional[str], out: deque) -> None:
        stdin_input = stdin.splitlines()
        for line in stdin_input:
            temp_line, prev_line = self.get_required_lines(line, out)
            if prev_line is None or prev_line.rstrip('\n') != temp_line:
                out.append(line + '\n')

    def get_required_lines(self, line, out):
        return line.lower() if self.flags['-i'] else line, None if not \
            len(out) else out[-1].lower() if self.flags['-i'] else out[-1]
