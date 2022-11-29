import re
from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError
from src.utils import check_flag, check_stdin


class Cut(Application):
    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: List[str], stdin: Optional[str],
                               out: deque):
        """check the number of args given and handle each case
        """

        num_args = len(args)

        if num_args == 2:
            self.handle_cut_str(args, out, stdin=stdin, src='stdin')
        elif num_args == 3:
            self.handle_cut_str(args, out, src='file')
        else:
            raise ArgumentError("Invalid number of arguments")

    def handle_cut_str(self, args: List[str], out: deque, src: str,
                       stdin: Optional[str] = None):
        """Validate the arguments and output the specified number of lines
        """

        # Validate arguments
        check_flag(args[0], '-b')
        if self.is_byte_order_valid(args):
            byte_order = args[1].split(',')
            byte_order.sort()

        lines = self.get_lines(args, src, stdin)

        for line in lines:
            cut_str = self.get_cut_str(line, byte_order)
            out.append(cut_str + '\n')

    @staticmethod
    def is_byte_order_valid(args: List[str]) -> bool:
        """Validates byte order"""
        byte_order = args[1]
        if byte_order is None:
            raise ArgumentError('byte order not given')

        for b in byte_order:
            if b not in '0123456789,-':
                raise ArgumentError('illegal list value')

        match = re.search(',,|--', byte_order)
        if match is not None:
            raise ArgumentError('illegal list value')

        return True

    @staticmethod
    def get_lines(args, src, stdin=None) -> list:
        """Return the lines to be cut based on the source"""
        if src == 'file':
            file = args[2]
            with open(file) as f:
                lines = f.readlines()
        elif src == 'stdin':
            check_stdin(stdin)
            lines = stdin.rstrip('\n').split('\n')

        return lines

    def get_cut_str(self, line, byte_order) -> str:
        """Generic function for getting cut string from
        single byte, open interval, or closed interval"""
        cut_str = ''
        used_bytes = []
        for byte in byte_order:
            if byte.isdigit():
                cut_str = self.cut_single_byte(byte, line, cut_str, used_bytes)
            elif re.match('[0-9]-[0-9]', byte) is not None:
                cut_str = self.cut_byte_interval(line, cut_str, used_bytes,
                                                 start=int(byte[0]),
                                                 end=int(byte[2]))
            elif re.match('[0-9]-', byte) is not None:
                cut_str = self.cut_byte_interval(line, cut_str, used_bytes,
                                                 start=int(byte[0]),
                                                 end=len(line))
            elif re.match('-[0-9]', byte) is not None:
                cut_str = self.cut_byte_interval(line, cut_str, used_bytes,
                                                 start=1, end=int(byte[1]))
        return cut_str

    @staticmethod
    def cut_single_byte(byte, line, cut_str, used_bytes) -> str:
        """Returns the cut string for a single byte"""
        byte = int(byte)
        if byte <= len(line) and line[byte] != '\n' and byte not in used_bytes:
            cut_str += line[byte - 1]
            used_bytes.append(byte)

        return cut_str

    @staticmethod
    def cut_byte_interval(line, cut_str, used_bytes, start, end) -> str:
        """Returns cut string for closed or open byte intervals"""
        for i in range(start, end + 1):
            if i <= len(line) and line[i - 1] != '\n' and i not in used_bytes:
                cut_str += line[i - 1]
                used_bytes.append(i)
        return cut_str
