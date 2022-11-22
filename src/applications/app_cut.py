import errors
import re
from typing import Optional
from collections import deque
from applications.application import Application
from utils import check_flag, check_stdin, split_stdin_to_lines


class Cut(Application):
    def exec(self, args: list, stdin: Optional[list], out: deque):
        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list, stdin: Optional[list], out: deque):
        """check the number of args given and handle each case
        """

        num_args = len(args)

        if num_args == 2:
            self.handle_cut_str(args, out, stdin=stdin, src='stdin')
        elif num_args == 3:
            self.handle_cut_str(args, out, src='file')
        else:
            raise errors.ArgumentError("Invalid number of arguments")

    def handle_cut_str(self, args: list, out: deque, src: str, stdin: Optional[str] = None):
        """If file and num_lines is given then read from file and
        output the specified number of lines
        """

        # validate parameter
        check_flag(args[0], '-b')

        self.check_byte_order(args)
        byte_order = args[1].split(',')
        byte_order.sort()

        lines = self.get_lines(args, src, stdin)

        for line in lines:
            cut_str = self.get_cut_str(line, byte_order)
            out.append(cut_str + '\n')

    def check_byte_order(self, args: list):
        byte_order = args[1]
        if byte_order is None:
            raise errors.ArgumentError('byte order not given')

        match = re.match('(?![0-9]|,|-)', byte_order)
        if match is not None:
            raise errors.ArgumentError('illegal list value')

        match = re.match(',,|--|,-|-,|-[0-9]-', byte_order)
        if match is not None:
            raise errors.ArgumentError('illegal list value')

    def get_lines(self, args, src, stdin=None):
        if src == 'file':
            file = args[2]
            with open(file) as f:
                lines = f.readlines()
        elif src == 'stdin':
            check_stdin(stdin)
            lines = split_stdin_to_lines(stdin)

        return lines

    def get_cut_str(self, line, byte_order):
        cut_str = ''
        used_bytes = []
        for byte in byte_order:
            if byte.isdigit():
                cut_str = self.cut_single_byte(byte, line, cut_str, used_bytes)
            else:
                cut_str = self.cut_byte_range(byte, line, cut_str, used_bytes)
        return cut_str

    def cut_single_byte(self, byte, line, cut_str, used_bytes):
        byte = int(byte)
        if byte < len(line) and line[byte] != '\n' and byte not in used_bytes:
            cut_str += line[byte]
            used_bytes.append(byte)

        return cut_str

    def cut_byte_range(self, byte, line, cut_str, used_bytes):
        start = int(byte[0])
        end = int(byte[2])
        match = re.match('[0-9]-[0-9]', byte)
        if match is not None:
            for i in range(start, end + 1):
                if i < len(line) and line[i] != '\n' and i not in used_bytes:
                    cut_str += line[i]
                    used_bytes.append(i)
            return cut_str
