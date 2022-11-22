from typing import Optional, List
from collections import deque
from src.errors import FlagError
from src.utils import check_flag
from src.applications.application import Application


class Uniq(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args) > 2:
            raise ValueError("wrong number of arguments")

        if not len(args) and stdin is None:
            raise ValueError('no arguments or stdin')

        if len(args) == 1 and args[0] == '-i' and stdin is None:
            raise ValueError('no arguments or stdin')

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: List[str], stdin: Optional[str], out: deque):
        flag = True if len(args) and args[0] == '-i' else False
        if len(args) > 1 or (len(args) and not flag):
            if len(args)>1:
                check_flag(args[0], '-i')
            self.handle_file_input(args, out, flag)
        else:
            self.handle_stdin_input(stdin, out, flag)

    def handle_file_input(self, args: list, out: deque, flag: bool):
        file_name = args[0] if not flag else args[1]
        with open(file_name, 'r') as file:
            for line in file.readlines():
                temp_line, prev_line = self.get_required_lines(line, flag, out)
                if prev_line is None or prev_line != temp_line:
                    out.append(line)

    def handle_stdin_input(self, stdin: Optional[str], out: deque, flag: bool):
        stdin_input = stdin.split('\n')
        for line in stdin_input:
            if line=='':
                continue
            temp_line, prev_line = self.get_required_lines(line, flag, out)
            if prev_line is None or prev_line.rstrip('\n') != temp_line:
                out.append(line+'\n')

    def get_required_lines(self, line, flag, out):
        return line.lower() if flag else line, None if not len(out) else out[-1].lower() if flag else out[-1]