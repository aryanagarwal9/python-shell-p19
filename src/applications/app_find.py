import glob
import os
from collections import deque
from typing import Optional

from applications.application import Application


class Find(Application):
    def exec(self, args: list, stdin: Optional[list], out: deque):
        if len(args) < 2 or len(args) > 3:
            raise ValueError("wrong number of arguments")

        self.find_files(args, out)

    def find_files(self, args: list, out: deque):
        path = '.' if args[0] == '-name' else args[0]
        pattern = args[1] if args[0] == '-name' else args[2]

        for filename in glob.iglob(os.path.join(path, "**", pattern), recursive=True):
            out.append(filename)

