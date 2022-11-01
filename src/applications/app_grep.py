import re
from typing import Optional
from collections import deque

from applications.application import Application

class Grep(Application):
    def exec(self, args: list, stdin: Optional[list], out: deque):
        if not len(args):
            raise ValueError("No arguments provided")

        pattern = args[0]

        self.call_required_function(pattern, stdin, args, out)

    def call_required_function(self, pattern, stdin, args, out):
        num_args = len(args)
        match num_args:
            case 1:
                raise ValueError("No files provided, std input can't be taken from keyboard")
            case 2:
                self.handle_grep_stdin(pattern, stdin, out)
            case other:
                self.handle_grep_file_input(pattern, args, out)

    def handle_grep_stdin(self, pattern: str, stdin: Optional[list], out: deque):
        for input_string in stdin:
            if re.match(pattern, input_string):
                out.append(input_string+'\n')

    def handle_grep_file_input(self, pattern: str, args: list, out:deque):
        files = args[1:]
        num_files = len(files)
        for file_name in files:
            with open(file_name) as file:
                file_lines = file.readlines()
                for line in file_lines:
                    if re.match(pattern, line):
                        out.append(f"{file_name}:{line}\n") if num_files>1 else out.append(line+'\n')




