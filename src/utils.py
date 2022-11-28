from src.errors import FlagError, StandardInputError
from typing import Optional


def check_flag(arg: str, flag: str):
    if arg != flag:
        raise FlagError("Invalid flags given")

    return True


def check_stdin(stdin: Optional[str]):
    if stdin is None:
        raise StandardInputError("No input given")

    return True
