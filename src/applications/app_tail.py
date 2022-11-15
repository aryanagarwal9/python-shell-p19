from typing import Optional
from collections import deque
from collections import deque
from typing import Optional

import errors
from applications.application import Application

from applications.application import Application

class Tail(Application):
    def exec(self, args: list[str], stdin: Optional[str], out: deque):
        if not len(args):
            raise errors.ArgumentError("No arguments given")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list[str], stdin: Optional[str], out: deque):
        """check the number of args given and handle each case

        :param args: list of arguments
        :param stdin: standard input
        :param out: output stored in a deque
        :return: None
        """

        num_args = len(args)

        if num_args == 1:
            self.handle_only_file_input(args, out)
        elif num_args == 2:
            self.handle_stdin(args, stdin, out)
        elif num_args == 3:
            self.handle_num_of_lines_and_file(args, out)
        else:
            raise errors.ArgumentError("Invalid number of arguments")

    def handle_only_file_input(self, args: list[str], out: deque):
        """output the first 10 lines if only file name is given

        :param args: list of arguments
        :param out: output stored in a deque
        :return: None
        """

        num_lines = 10
        file = args[0]

        self.output_lines_from_file(num_lines, file, out)

    def handle_stdin(self, args: list[str], stdin: Optional[str], out: deque):
        """If file not given then read from stdin and
        output the specified number of lines

        :param args: list of arguments
        :param stdin: standard input
        :param out: output stored in a deque
        :return: None
        """

        # validate parameters
        if stdin is None:
            raise errors.StandardInputError("No input given")
        if args[0] != "-n":
            raise errors.FlagError("Invalid flags given")

        # add lines to output
        num_lines = int(args[1])
        display_length = min(len(stdin), num_lines)

        for i in range(len(stdin) - display_length, len(stdin)):
            out.append(stdin[i])

    def handle_num_of_lines_and_file(self, args: list[str], out: deque):
        """If file not given then read from stdin and
        output the specified number of lines

        :param args: list of arguments
        :param out: output stored in a deque
        :return: None
        """

        # validate parameter
        if args[0] != "-n":
            raise errors.FlagError("Invalid flags given")
        else:
            num_lines = int(args[1])
            file = args[2]

        self.output_lines_from_file(num_lines, file, out)

    def output_lines_from_file(self, num_lines: int, file: str, out: deque):
        """Read the text file and add the specified number of lines to output

        :param num_lines: number of lines to add to output
        :param file: text file to read lines from
        :param out: output stored in a deque
        :return: None
        """

        with open(file) as f:
            lines = f.readlines()
            display_length = min(len(lines), num_lines)

            for i in range(len(lines) - display_length, len(lines)):
                out.append(lines[i])

    def get_lines(self, args: list[str], file: str = None, stdin: Optional[str] = None) -> int:
        if file is not None:
            with open(file) as f:
                num_lines = int(args[1])
                lines = f.readlines()
                display_length = min(len(lines), num_lines)
                return lines[]
        elif stdin:
            num_lines = int(args[1])
