import os
from collections import deque
from typing import Optional

from src.applications.application import Application


class Pwd(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        out.append(os.getcwd()+'\n')
