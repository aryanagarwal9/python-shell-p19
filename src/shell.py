import os
import sys
from collections import deque

from src.shell_commands.commands_visitor import CommandsVisitor
from src.errors import ArgumentError


def eval(cmdline, out):
    CommandsVisitor().converter(cmdline).eval(None, out)


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ArgumentError("Wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ArgumentError(f"Unexpected command line argument {sys.argv[1]}")
        out = deque()
        eval(sys.argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            out = deque()
            eval(cmdline, out)
            while len(out) > 0:
                print(out.popleft(), end="")
