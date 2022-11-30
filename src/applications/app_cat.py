from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError


class Cat(Application):
    def __init__(self):
        self.flags = {'-n': False}

    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        """
        -n flag: number all the output lines
        """

        # Check for flag
        self.flags['-n'] = len(args) and args[0] == '-n'

        # Call required handler
        if len(args) > 1 or (len(args) == 1 and args[0] not in self.flags):
            self.handle_file_arguments(args, out)
        else:
            self.handle_stdin_argument(stdin, out)

    def handle_file_arguments(self, args: List[str], out: deque):
        """If file name is given, concatenate all the files and output
        """

        # First element can be a flag
        file_names = args[list(self.flags.values()).count(True):]

        for file_name in file_names:
            with open(file_name, 'r') as file:
                # choosing content based on flag
                file_content = [
                    f'\t{line_count} {line}' if self.flags['-n'] else line for
                    line_count, line in enumerate(file.readlines(), start=1)]
            out.append("".join(file_content))

    def handle_stdin_argument(self, stdin: Optional[str], out: deque):
        """If file not given then read from stdin and
        output the lines
        """

        if stdin is None:
            raise ArgumentError('No arguments or stdin provided')

        stdin = stdin.splitlines(True)

        # choosing content based on flag
        temp_output = [f'\t{line_count} {line}' if self.flags['-n'] else line
                       for line_count, line in enumerate(stdin, start=1)]
        out.append("".join(temp_output))
