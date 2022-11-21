import os
from collections import deque
from typing import Optional

from applications.application import Application

class Cd(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args)>1:
            raise ValueError("Maximum of one argument expected")
        os.chdir(args[0]) if len(args) else os.chdir(os.path.expanduser("~"))