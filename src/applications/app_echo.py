from typing import Optional
from collections import deque

from src.applications.application import Application

class Echo(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        out.append(" ".join(args)+"\n")



