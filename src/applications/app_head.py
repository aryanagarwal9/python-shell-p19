from collections import deque
from typing import Optional, List

from src.applications.application import Application
from src.errors import ArgumentError
from src.utils import check_flag, is_stdin_available, get_lines


class Head(Application):
    def exec(self, args: List[str], stdin: Optional[str], out: deque) -> None:
        self.call_required_function(args, stdin, out)

    def call_required_function(self, args: List[str], stdin: Optional[str],
                               out: deque) -> None:
        """Checks the number of args given and handles each case
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
            raise ArgumentError("Invalid number of arguments")

    def handle_only_stdin(self, stdin: Optional[str], out) -> None:
        """If only stdin is given, output the first 10 lines
         """
        # Validate parameters
        is_stdin_available(stdin)

        # Add head to output
        out.extend(self.get_head(stdin=stdin, src='stdin'))

    def handle_only_file_input(self, args: List[str], out: deque) -> None:
        """If only file name is given, output the first 10 lines
        """

        # Get file
        file = args[0]

        # Add head to output
        out.extend(self.get_head(file=file, src='file'))

    def handle_num_of_lines_and_stdin(self, args: List[str],
                                      stdin: Optional[str],
                                      out: deque) -> None:
        """If file not given then read from stdin and
        output the specified number of lines
        """

        # Validate parameters
        check_flag(args[0], '-n')
        is_stdin_available(stdin)

        # Get number of lines
        num_lines = int(args[1])

        # Add head to output
        out.extend(
            self.get_head(num_lines=num_lines, stdin=stdin, src='stdin'))

    def handle_num_of_lines_and_file(self, args: List[str],
                                     out: deque) -> None:
        """If file and num_lines is given then read from file and
        output the specified number of lines
        """

        # Validate parameter
        check_flag(args[0], '-n')

        # Get number of lines and file
        num_lines = int(args[1])
        file = args[2]

        # Add head to output
        out.extend(self.get_head(num_lines=num_lines, file=file, src='file'))

    @staticmethod
    def get_head(num_lines: int = 10, file: str = None,
                 stdin: Optional[str] = None, src: str = 'file') -> List[str]:
        """Returns head based on src and number of lines"""

        res = []

        if src == 'file':
            lines = get_lines(src, file=file)
        else:
            lines = get_lines(src, stdin=stdin)

        display_length = min(len(lines), num_lines)
        for i in range(display_length):
            res.append(lines[i])

        return res
