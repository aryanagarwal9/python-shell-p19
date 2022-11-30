from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError, FlagError


class Wc(Application):
    def __init__(self):
        self.flags = {'-w': False, '-c': False, '-l': False}
        self.flag_connect = {'-w': self.get_word_count,
                             '-c': self.get_byte_count,
                             '-l': self.get_line_count}

    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        """
        -w flag: return the word count
        -c flag: return the byte count
        -l flag: return the newline count
        """

        # Flag should be provided
        if args[0] in self.flags:
            self.flags[args[0]] = True
        else:
            raise FlagError('No flag provided')

        # First few elements can be flags
        file_names = args[list(self.flags.values()).count(True):]

        # Get the flag being used
        flag_name = [flag for flag in self.flags if self.flags[flag]][0]

        # Call required handler
        if len(file_names):
            self.handle_file_input(file_names, flag_name, out)
        elif stdin is not None:
            self.handle_stdin(stdin, flag_name, out)
        else:
            raise ArgumentError('No arguments or stdin')

    def handle_file_input(self, file_names: List[str], flag_name: str,
                          out: deque):
        """Update out from file input.
        Takes care to include total count for multiple files
        """
        num_files = len(file_names)
        total_count = 0

        for file_name in file_names:
            with open(file_name, 'r') as file:
                file_data_count = self.flag_connect[flag_name](file.read())
                total_count += file_data_count
                out.append(
                    f'\t{file_data_count} {file_name}\n')

        if num_files > 1:
            out.append(f'\t{total_count} total\n')

    def handle_stdin(self, stdin: Optional[str], flag_name: str, out: deque):
        out.append(f'\t{self.flag_connect[flag_name](stdin)}\n')

    @staticmethod
    def get_line_count(src_content: str):
        return src_content.count('\n')

    @staticmethod
    def get_word_count(src_content: str):
        return len(src_content.split())

    @staticmethod
    def get_byte_count(src_content: str):
        return len(src_content.encode('utf-8'))
