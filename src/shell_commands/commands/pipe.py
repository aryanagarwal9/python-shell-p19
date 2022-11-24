from collections import deque
from typing import Optional

from src.shell_commands.commands.command import Command
# from src.shell_commands.commands.call import Call

class Pipe(Command):
    def __init__(self, left: Command, right: Command):
        self.left = left
        self.right = right

    def eval(self, input_cmd: Optional[str], out: deque):
        temp_deque = deque()
        self.left.eval(input_cmd, temp_deque)
        self.right.eval("".join(temp_deque), out)
