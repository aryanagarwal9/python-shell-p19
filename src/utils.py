from typing import Optional

from src.errors import FlagError, StandardInputError


def check_flag(arg: str, flag: str):
    if arg != flag:
        raise FlagError("Invalid flags given")

    return True


def is_stdin_available(stdin: Optional[str]):
    if stdin is None:
        raise StandardInputError("No input given")

    return True


def get_lines(src, file=None, stdin=None) -> list:
    """Return a list of lines based on the source"""
    if src == 'file':
        with open(file) as f:
            lines = f.readlines()
    else:
        is_stdin_available(stdin)
        lines = stdin.splitlines(True)

    return lines
