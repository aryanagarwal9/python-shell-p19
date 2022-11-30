import os
import sys
from collections import deque

from src.errors import ArgumentError, FlagError
from src.shell_commands.commands_visitor import CommandsVisitor


def eval(cmdline, out):
    CommandsVisitor().converter(cmdline).eval(None, out)

def run_non_interactive_mode(args_num):
    if args_num != 2:
        raise ArgumentError("Wrong number of command line arguments")
    if sys.argv[1] != "-c":
        raise FlagError(f"Invalid Flag: {sys.argv[1]}")
    out = deque()
    eval(sys.argv[2], out)
    while len(out) > 0:
        print(out.popleft(), end="")

def run_interactive_mode():
    while True:
        print(os.getcwd() + "> ", end="")
        cmdline = input()
        out = deque()
        eval(cmdline, out)
        while len(out) > 0:
            print(out.popleft(), end="")

def run():
    args_num = len(sys.argv) - 1
    if args_num > 0:
        run_non_interactive_mode(args_num)
    else:
        run_interactive_mode()

if __name__ == "__main__":
    run()
