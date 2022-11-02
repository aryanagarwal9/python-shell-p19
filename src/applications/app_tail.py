from collections import deque
from typing import Optional
from applications.application import Application


class Tail(Application):
    def __init__(self):
        pass

    def exec(self, args: list[str], stdin: Optional[list], out: deque):
        if not len(args):
            raise ValueError("No arguments given")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list[str], stdin: Optional[list], out: deque):
        num_args = len(args)

        match num_args:
            case 1:
                self.handle_only_file_input(args, out)
            case 2:
                self.handle_stdin(args, stdin, out)
            case 3:
                self.handle_num_of_lines_and_file(args, out)
            case other:
                raise ValueError("wrong number of command line arguments")

    def handle_only_file_input(self, args: list[str], out: deque):
        num_lines = 10
        file = args[0]

        self.output_lines_from_file(num_lines, file, out)

    def handle_stdin(self, args: list[str], stdin: Optional[list], out: deque):
        if stdin is None:
            raise ValueError("no input given")
        if args[0] != "-n":
            raise ValueError("wrong flags")

        num_lines = int(args[1])
        display_length = min(len(stdin), num_lines)

        for i in range(len(stdin) - display_length, len(stdin)):
            out.append(stdin[i])

    def handle_num_of_lines_and_file(self, args: list[str], out: deque):
        if args[0] != "-n":
            raise ValueError("wrong flags")
        else:
            num_lines = int(args[1])
            file = args[2]

        self.output_lines_from_file(num_lines, file, out)

    def output_lines_from_file(self, num_lines: int, file: str, out: deque):
        with open(file) as f:
            lines = f.readlines()
            display_length = min(len(lines), num_lines)

            for i in range(len(lines) - display_length, len(lines)):
                out.append(lines[i])
