from typing import Optional

from src.errors import FlagError, StandardInputError


def check_flag(arg: str, flag: str):
    if arg != flag:
        raise FlagError(f"Invalid flags given: {arg}")

    return True


def is_stdin_available(stdin: Optional[list]):
    if stdin is None:
        raise StandardInputError("No input given")

    return True


def get_lines(src, file=None, stdin=None) -> list:
    """Return a list of lines based on the source"""
    if src == 'file':
        with open(file) as f:
            lines = f.readlines()
    elif src == 'stdin':
        is_stdin_available(stdin)
        lines = stdin.rstrip('\n').split('\n')

    return lines