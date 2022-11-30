from collections import deque
from typing import Optional

from src.shell_commands.commands.command import Command


class Pipe(Command):
    def __init__(self, left: Command, right: Command):
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.left == other.left and \
               self.right == other.right

    def eval(self, input_cmd: Optional[str], out: deque):
        temp_deque = deque()

        # Output from the left becomes input for the right
        self.left.eval(input_cmd, temp_deque)
        self.right.eval("".join(temp_deque), out)
