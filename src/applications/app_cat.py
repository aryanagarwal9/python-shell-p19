from collections import deque
from typing import Optional

from src.applications.application import Application


class Cat(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args):
            self.handle_file_arguments(args, out)
        else:
            self.handle_stdin_argument(stdin, out)

    @staticmethod
    def handle_stdin_argument(stdin: Optional[str], out: deque):
        out.append(stdin)

    @staticmethod
    def handle_file_arguments(args: list, out: deque):
        concatenated_output = ''
        for file_name in args:
            with open(file_name, 'r') as file:
                concatenated_output += file.read()
        out.append(concatenated_output)
