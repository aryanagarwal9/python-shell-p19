from collections import deque
from typing import Optional

from src.applications.application import Application


class Echo(Application):
    def __init__(self):
        self.flags = {'-n': False}

    def exec(self, args: list, stdin: Optional[str], out: deque) -> None:
        """
        -n flag: do not output the trailing newline
        """

        # Check for flag
        self.flags['-n'] = len(args) and args[0] == '-n'

        if self.flags['-n']:
            out.append(" ".join(args[1:]))
        else:
            out.append(" ".join(args) + '\n')
