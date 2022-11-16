from collections import deque
from typing import Optional

from applications.application import Application

class Cut(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        print("hi i am echo")