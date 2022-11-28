from collections import deque
from typing import Optional, List

from src.applications.application import Application


class UnsafeDecorator(Application):
    def __init__(self, app: Application):
        self.unsafe_app = app

    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        try:
            self.unsafe_app.exec(args, stdin, out)
        except Exception as exception:
            out.append(f'{exception}')
