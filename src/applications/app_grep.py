import re
from collections import deque
from typing import Optional

from src.applications.application import Application
from src.errors import ArgumentError
from src.utils import get_lines


class Grep(Application):
    def __init__(self):
        self.flags = {'-v': False}

    def exec(self, args: list, stdin: Optional[str], out: deque) -> None:
        """
        -v flag: Invert the sense of matching, to select non-matching lines.
        """
        if not len(args):
            raise ArgumentError("No arguments provided")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list, stdin: Optional[str],
                               out: deque) -> None:
        """check the number of args given and handle each case
        """

        # Check for flag
        self.flags['-v'] = args[0] == '-v'
        pattern = args[1] if self.flags['-v'] else args[0]

        # Call required handler
        if len(args) > 2 or (len(args) == 2 and not self.flags['-v']):
            self.handle_file_input(pattern, args, out)
        elif stdin is not None:
            self.handle_stdin(pattern, stdin, out)
        else:
            raise ArgumentError('No arguments or stdin')

    def handle_stdin(self, pattern: str, stdin: Optional[str],
                     out: deque) -> None:
        """If file not given then read from stdin and
        output the lines matching the pattern
        """
        for input_string in stdin.rstrip('\n').split('\n'):
            if self.should_append_line(pattern, input_string):
                out.append(input_string + '\n')

    def handle_file_input(self, pattern: str, args: list, out: deque) -> None:
        """If file given, then output lines matching the pattern grouped by
        files
        """
        files = args[2:] if self.flags['-v'] else args[1:]
        num_files = len(files)
        for file_name in files:
            for line in get_lines(src='file', file=file_name):
                if self.should_append_line(pattern, line):
                    if num_files > 1:
                        out.append(f"{file_name}:{line.rstrip()}\n")
                    else:
                        out.append(line.rstrip() + '\n')

    def should_append_line(self, pattern: str, line: str) -> None:
        # Choose content based on flag
        return (not self.flags['-v'] and re.search(pattern, line) is not None)\
               or (self.flags['-v'] and re.search(pattern, line) is None)
