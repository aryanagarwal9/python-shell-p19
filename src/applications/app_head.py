import errors
from typing import Optional
from collections import deque
from applications.application import Application
from utils import check_flag, check_stdin, split_stdin_to_lines


class Head(Application):
    def exec(self, args: list[str], stdin: Optional[list], out: deque):
        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list[str], stdin: Optional[list], out: deque):
        """check the number of args given and handle each case
        """

        num_args = len(args)

        if num_args == 0:
            self.handle_only_stdin(stdin, out)
        elif num_args == 1:
            self.handle_only_file_input(args, out)
        elif num_args == 2:
            self.handle_num_of_lines_and_stdin(args, stdin, out)
        elif num_args == 3:
            self.handle_num_of_lines_and_file(args, out)
        else:
            raise errors.ArgumentError("Invalid number of arguments")

    def handle_only_stdin(self, stdin: str, out):
        """output the first 10 lines if only stdin is given
         """
        # validate parameters
        check_stdin(stdin)

        # add lines to output
        out.extend(self.get_lines(stdin=stdin, src='stdin'))

    def handle_only_file_input(self, args: list[str], out: deque):
        """output the first 10 lines if only file name is given
        """

        file = args[0]
        out.extend(self.get_lines(file=file, src='file'))

    def handle_num_of_lines_and_stdin(self, args: list[str], stdin: Optional[list], out: deque):
        """If file not given then read from stdin and
        output the specified number of lines
        """

        # validate parameters
        check_stdin(stdin)
        check_flag(args[0], '-n')

        num_lines = int(args[1])

        # add lines to output
        out.extend(self.get_lines(num_lines=num_lines, stdin=stdin, src='stdin'))

    def handle_num_of_lines_and_file(self, args: list[str], out: deque):
        """If file and num_lines is given then read from file and
        output the specified number of lines
        """

        # validate parameter
        check_flag(args[0], '-n')

        num_lines = int(args[1])
        file = args[2]

        out.extend(self.get_lines(num_lines=num_lines, file=file, src='file'))


    def get_lines(self, num_lines: int = 10, file: str = None, stdin: str = None, src: str = 'file') -> list[str]:
        res = []

        if src == 'file':
            with open(file) as f:
                lines = f.readlines()
                display_length = min(len(lines), num_lines)

        elif src == 'stdin':
            lines = split_stdin_to_lines(stdin)
            display_length = min(len(lines), num_lines)

        for i in range(display_length):
            res.append(lines[i])

        return res
