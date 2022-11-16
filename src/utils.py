import errors
from typing import Optional


def check_flag(arg: str, flag: str):
    if arg != flag:
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
        if start >= len(stdin):
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
