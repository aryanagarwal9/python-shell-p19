from typing import Optional
from collections import deque

from applications.application import Application

class Echo(Application):
    def exec(self, args: list, stdin: Optional[list], out: deque):
        out.append(" ".join(args)+"\n")



