from typing import Optional
from collections import deque

from applications.application import Application


class Uniq(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args) > 2:
            raise ValueError("wrong number of arguments")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list[str], stdin: Optional[str], out: deque):
        flag = True if len(args) and args[0] == '-i' else False
        if len(args) > 1 or (len(args) and not flag):
            self.handle_file_input(args, out, flag)
        else:
            self.handle_stdin_input(stdin, out, flag)

    def handle_file_input(self, args: list, out: deque, flag: bool):
        file_name = args[0] if not flag else args[1]
        with open(file_name, 'r') as file:
            for line in file.readlines():
                line = line.lower() if flag else line
                if not out or out[-1] != line:
                    out.append(line)

    def handle_stdin_input(self, stdin: Optional[str], out: deque, flag: bool):
        stdin_input = stdin.split('\n')
        for line in stdin_input:
            line = line.lower() if flag else line
            if not out or out[-1] != line:
                out.append(line)