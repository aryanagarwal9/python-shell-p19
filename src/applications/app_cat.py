from collections import deque
from typing import Optional

from applications.application import Application

class Cat(Application):
    def exec(self, args: list, stdin: Optional[list], out: deque):
        print("hi i am echo")