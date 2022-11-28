from typing import Optional

from src.errors import FlagError, StandardInputError


def check_flag(arg: str, flag: str):
    if arg != flag:
        raise FlagError("Invalid flags given")

    return True


def check_stdin(stdin: Optional[list]):
    if stdin is None:
        raise StandardInputError("No input given")

    return True
