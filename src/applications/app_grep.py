import re
from typing import Optional
from collections import deque

from applications.application import Application


class Grep(Application):
    def exec(self, args: list, stdin: Optional[list], out: deque):
        if not len(args):
            raise ValueError("No arguments provided")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list, stdin: Optional[list], out: deque):
        pattern = args[0]
        num_args = len(args)
        if num_args > 1:
            self.handle_file_input(pattern, args, out)
        else:
            self.handle_stdin(pattern, stdin, out)

    def handle_stdin(self, pattern: str, stdin: Optional[list], out: deque):
        for input_string in stdin:
            if re.match(pattern, input_string):
                out.append(input_string + '\n')

    def handle_file_input(self, pattern: str, args: list, out: deque):
        files = args[1:]
        num_files = len(files)
        for file_name in files:
            with open(file_name) as file:
                file_lines = file.readlines()
                for line in file_lines:
                    if re.match(pattern, line):
                        out.append(f"{file_name}:{line}\n") if num_files > 1 else out.append(line + '\n')
