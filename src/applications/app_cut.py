import errors
from collections import deque
from typing import Optional
from applications.application import Application
from utils import check_flag, check_stdin, split_stdin_to_lines


class Cut(Application):

    def exec(self, args: list, stdin: Optional[str], out: deque):
        print("hi i am echo")

