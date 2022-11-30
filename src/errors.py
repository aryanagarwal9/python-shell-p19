from typing import Optional


class ShellErrors(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        if Optional is not None:
            self.message = message
            super().__init__(self.message)


class FlagError(ShellErrors):
    pass


class ArgumentError(ShellErrors):
    pass


class StandardInputError(ShellErrors):
    pass


class ParseError(ShellErrors):
    pass


class DirectoryCreationError(ShellErrors):
    pass

class ApplicationNotSupportedError(ShellErrors):
    pass