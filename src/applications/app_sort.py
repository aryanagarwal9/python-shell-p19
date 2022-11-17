from collections import deque
from typing import Optional
from utils import check_flag
from errors import FlagError
from applications.application import Application


class Sort(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        reverse = len(args) and args[0] == '-r'
        if self.is_file_input_available(args):
            self.handle_file_input(args, out, reverse=reverse)

        elif self.is_stdin_available(stdin):
            self.handle_stdin(stdin, out, reverse=reverse)

        else:
            raise ValueError('no arguments or stdin')

    def is_file_input_available(self, args: list):
        if len(args) > 1:
            check_flag(args[0], '-r')
            return True
        return len(args) and args[0] != '-r'

    def is_stdin_available(self, stdin: Optional[str]):
        return stdin is not None

    def handle_file_input(self, args: list, out: deque, reverse: bool):
        file_name = args[0] if len(args) == 1 else args[1]
        with open(file_name,'r') as file:
            for line in sorted(file.readlines(), reverse=reverse):
                out.append(line) if line.endswith('\n') else out.append(line+'\n')

    def handle_stdin(self, stdin: Optional[str], out: deque, reverse: bool):
        for line in sorted(stdin.split('\n'), reverse=reverse):
            out.append(line + '\n')
