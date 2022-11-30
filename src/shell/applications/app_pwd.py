import os
from collections import deque
from typing import Optional, List

from shell.applications.application import Application


class Pwd(Application):
    def exec(self, args: List[str], stdin: Optional[str], out: deque) -> None:
        out.append(os.getcwd()+'\n')
