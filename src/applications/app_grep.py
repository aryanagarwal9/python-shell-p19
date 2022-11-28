import re
from collections import deque
from typing import Optional

from src.applications.application import Application


class Grep(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if not len(args):
            raise ValueError("No arguments provided")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list, stdin: Optional[str],
                               out: deque):
        pattern = args[0]
        num_args = len(args)
        if num_args > 1:
            self.handle_file_input(pattern, args, out)
        elif stdin is None:
            raise ValueError('no arguments or stdin')
        else:
            self.handle_stdin(pattern, stdin, out)

    def handle_stdin(self, pattern: str, stdin: Optional[str], out: deque):
        for input_string in stdin.split('\n'):
            if re.search(pattern, input_string) is not None:
                out.append(input_string.rstrip() + '\n')

    def handle_file_input(self, pattern: str, args: list, out: deque):
        files = args[1:]
        num_files = len(files)
        for file_name in files:
            with open(file_name) as file:
                file_lines = file.readlines()
                for line in file_lines:
                    if re.search(pattern, line) is not None:
                        if num_files > 1:
                            out.append(f"{file_name}:{line.rstrip()}\n")
                        else:
                            out.append(line.rstrip() + '\n')
