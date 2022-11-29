from collections import deque
from typing import Optional

from src.applications.application import Application


class Echo(Application):
    def __init__(self):
        self.flags = {'-n': False}

    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args) and args[0] == '-n':
            self.flags['-n'] = True

        out.append(" ".join(args[1:])) if self.flags['-n'] else out.append(
            " ".join(args) + '\n')
