from typing import Optional
from collections import deque
from collections import deque
from typing import Optional

import errors
from applications.application import Application

from applications.application import Application

class Tail(Application):
    def exec(self, args: list[str], stdin: Optional[list], out: deque):
        if not len(args):
            raise errors.ArgumentError("No arguments given")

        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: list[str], stdin: Optional[list], out: deque):
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

        out.extend(self.output_lines_from_file(num_lines, file))

    def handle_stdin(self, args: list[str], stdin: Optional[list], out: deque):
        """If file not given then read from stdin and
        output the specified number of lines

        :param args: list of arguments
        :param stdin: standard input
        :param out: output stored in a deque
        :return: None
        """

        # validate parameters
        check_stdin(stdin)
        check_flag(args[0], '-n')

        # add lines to output
        num_lines = int(args[1])
        stdin_lines = split_stdin_to_lines(stdin)

        display_length = min(len(stdin_lines), num_lines)

        for i in range(len(stdin_lines) - display_length, len(stdin_lines)):
            out.append(stdin_lines[i])

    def handle_num_of_lines_and_file(self, args: list[str], out: deque):
        """If file and num_lines is given then read from file and
        output the specified number of lines

        :param args: list of arguments
        :param out: output stored in a deque
        :return: None
        """

        # validate parameter
        check_flag(args[0], '-n')

        num_lines = int(args[1])
        file = args[2]

        out.extend(self.output_lines_from_file(num_lines, file))

    def output_lines_from_file(self, num_lines: int, file: str):
        """Read the text file and add the specified number of lines to output

        :param num_lines: number of lines to add to output
        :param file: text file to read lines from
        :param out: output stored in a deque
        :return: None
        """

        res = []

        with open(file) as f:
            lines = f.readlines()
            display_length = min(len(lines), num_lines)

            for i in range(len(lines) - display_length, len(lines)):
                res.append(lines[i])

        return res


def check_flag(arg: str, flag: str):
    if arg != "-n":
        raise errors.FlagError("Invalid flags given")

    return True


def check_stdin(stdin: Optional[list]):
    if stdin is None:
        raise errors.StandardInputError("No input given")

    return True


def split_stdin_to_lines(stdin):
    lines = []
    start = 0
    while True:
        if start >= len(stdin) - 1:
            break

        i = stdin.find('\n', start)
        if i == -1:
            lines.append(stdin[start:])
            break
        else:
            end = i + 1
            lines.append(stdin[start: end])
            start = end

    return lines
