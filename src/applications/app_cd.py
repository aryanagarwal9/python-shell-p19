import os
from collections import deque
from typing import Optional

from src.applications.application import Application
from src.errors import ArgumentError


class Cd(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque) -> None:
        if len(args) > 1:
            raise ArgumentError("Maximum of one argument expected")

        # If path provided, go there else go to home directory
        os.chdir(args[0]) if len(args) else os.chdir(os.path.expanduser("~"))
