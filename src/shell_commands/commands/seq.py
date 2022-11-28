from collections import deque
from typing import Optional

from src.shell_commands.commands.command import Command

class Seq(Command):
    def __init__(self, left: Command, right: Command):
        self.left = left
        self.right = right

    def eval(self, input_cmd: Optional[str], out: deque):
        self.left.eval(input_cmd, out)
        self.right.eval(None, out)