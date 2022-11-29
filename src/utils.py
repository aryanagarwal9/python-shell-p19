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
