from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError


class Cat(Application):
    def __init__(self):
        self.flags = {'-n': False}

    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        if len(args) and args[0] in self.flags:
            self.flags[args[0]] = True

        if len(args) > 1 or (len(args) == 1 and args[0] not in self.flags):
            self.handle_file_arguments(args, out, self.flags['-n'])
        else:
            self.handle_stdin_argument(stdin, out, self.flags['-n'])

    @staticmethod
    def handle_file_arguments(args: List[str], out: deque, flag: bool):
        if flag:
            args.pop(0)

        for file_name in args:
            with open(file_name, 'r') as file:
                file_content = [f'\t{line_counter} {line}' if flag else line
                                for line_counter, line in
                                enumerate(file.readlines(), start=1)]
            out.append("".join(file_content))

    @staticmethod
    def handle_stdin_argument(stdin: Optional[str], out: deque, flag: bool):
        if stdin is None:
            raise ArgumentError('no arguments or stdin provided')
        stdin = stdin.rstrip('\n').split('\n')
        for line_count, line in enumerate(stdin, start=1):
            out.append(f'{line_count} {line}') if flag else out.append(line)
