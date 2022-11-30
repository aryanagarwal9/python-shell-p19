import glob
import os
import re
from collections import deque
from typing import Optional

from src.applications.application import Application
from src.utils import check_flag
from src.errors import ArgumentError


class Find(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque) -> None:
        # If no path is provided
        if len(args) == 2:
            check_flag(args[0], '-name')

        # First element will be path
        elif len(args) == 3:
            check_flag(args[1], '-name')

        else:
            raise ArgumentError("Wrong number of arguments")

        self.find_files(args, out)

    def find_files(self, args: list, out: deque) -> None:
        """Output the files inside the directory whose name matches the pattern
        """
        path = '.' if args[0] == '-name' else args[0]
        pattern = args[1] if args[0] == '-name' else args[2]

        self.match_current_dir(path, pattern, out)

        # Recursively check for files inside all sub-directories
        for filename in glob.iglob(os.path.join(path, "**", pattern),
                                   recursive=True):
            out.append(filename + '\n')

    @staticmethod
    def match_current_dir(path: str, pattern: str, out: deque) -> None:
        """Check if the current directory matches the given pattern
        """
        pattern = pattern.lstrip('*')
        if re.search(pattern, path) is not None:
            out.append(path + '\n')
