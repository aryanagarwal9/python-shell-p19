import os
from typing import Optional
from collections import deque

from src.applications.application import Application


class Ls(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if not len(args):
            self.handle_no_arguments(out=out)
        elif len(args) == 1:
            self.handle_one_argument(args=args, out=out)
        else:
            raise ValueError("Cannot accept more than one argument")

    def get_directory_contents(self, directory_name: str):
        return [content for content in os.listdir(directory_name) if not content.startswith('.')]

    def handle_no_arguments(self, out: deque):
        contents = self.get_directory_contents(os.getcwd())
        out.append("\t".join(contents) + '\n')

    def handle_one_argument(self, args: list, out: deque):
        contents = self.get_directory_contents(args[0])
        out.append("\t".join(contents) + '\n')

