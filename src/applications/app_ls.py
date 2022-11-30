import os
from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError


class Ls(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque) -> None:
        # Call required handler
        if not len(args):
            self.handle_no_arguments(out=out)
        elif len(args) == 1:
            self.handle_one_argument(args=args, out=out)
        else:
            raise ArgumentError("Cannot accept more than one argument")

    def handle_no_arguments(self, out: deque) -> None:
        """Output contents of current directory
        """
        contents = self.get_directory_contents(os.getcwd())
        out.append("\t".join(contents) + '\n')

    def handle_one_argument(self, args: list, out: deque) -> None:
        """Output contents of given argument
        """
        contents = self.get_directory_contents(args[0])
        out.append("\t".join(contents) + '\n')

    @staticmethod
    def get_directory_contents(directory_name: str) -> List[str]:
        return [content for content in os.listdir(directory_name) if
                not content.startswith('.')]
