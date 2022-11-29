import os
from typing import Optional, List
from collections import deque

from src.applications.application import Application
from src.errors import ArgumentError, DirectoryCreationError

class Mkdir(Application):
    def __init__(self):
        self.flags = {'-p': False, '-v': False}

    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        if not len(args) or all(arg in self.flags for arg in args):
            raise ArgumentError('No directory names provided')

        self.flags['-p'] = '-p' in args[:2]
        self.flags['-v'] = '-v' in args[:2]

        self.handle_directory_creation(args, out)

    def handle_directory_creation(self, args: List[str], out: deque):
        dir_exists, parent_dirs_nonexistent = list(), list()
        make_dir = self.get_makedir(args)
        new_dirs = args[list(self.flags.values()).count(True):]
        for new_dir in new_dirs:
            if not os.path.isdir(new_dir):
                try:
                    make_dir(new_dir)
                    if self.flags['-v']:
                        out.append(f'created directory: {new_dir}\n')
                except FileNotFoundError:
                    parent_dirs_nonexistent.append(new_dir)
            else:
                dir_exists.append(new_dir)

        if len(dir_exists) or len(parent_dirs_nonexistent):
            self.handle_errors(dir_exists, parent_dirs_nonexistent)

    @staticmethod
    def get_makedir(args: List[str]):
        if args[0] == '-p':
            args.pop(0)
            return os.makedirs
        return os.mkdir

    @staticmethod
    def handle_errors(dir_exists, parent_dirs_non_existent):
        error_message = ''
        for directory in dir_exists:
            error_message += f'{directory}: Directory already exists\n'

        for directory in parent_dirs_non_existent:
            error_message += f'{directory}: Parent directories not found\n'

        raise DirectoryCreationError(error_message)

