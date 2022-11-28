import glob
import os
import re
from collections import deque
from typing import Optional

from src.applications.application import Application
from src.utils import check_flag


class Find(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args) < 2 or len(args) > 3:
            raise ValueError("wrong number of arguments")

        if len(args) == 2:
            check_flag(args[0], '-name')

        elif len(args) == 3:
            check_flag(args[1], '-name')

        self.find_files(args, out)

    def find_files(self, args: list, out: deque):
        path = '.' if args[0] == '-name' else args[0]
        pattern = args[1] if args[0] == '-name' else args[2]

        self.match_current_dir(path, pattern, out)

        for filename in glob.iglob(os.path.join(path, "**", pattern),
                                   recursive=True):
            out.append(filename + '\n')

    def match_current_dir(self, path, pattern, out):
        pattern = pattern.lstrip('*')
        if re.search(pattern, path) is not None:
            out.append(path + '\n')
