import os
from collections import deque
from typing import Optional, List


from src.applications.application import Application
from src.errors import ArgumentError
from src.utils import check_flag, is_stdin_available, get_lines

class Wc(Application):
    def __init__(self):
        self.flags = {'-w': False, '-c': False, '-l': False}

    # def exec(self, args: list, stdin: Optional[str], out: deque):

