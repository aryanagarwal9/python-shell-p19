from collections import deque
from typing import Optional, List

from src.applications.application_factory import ApplicationFactory
from src.shell_commands.commands.command import Command


class Call(Command):
    def __init__(self, app: str, args: List[str], input_file: Optional[str],
                 output_file: Optional[str]):
        self.app = app
        self.args = args
        self.input_file = input_file
        self.output_file = output_file

    def __eq__(self, other):
        return self.app == other.app and \
               self.args == other.args and \
               self.input_file == other.input_file and \
               self.output_file == other.output_file

    def eval(self, input_cmd: Optional[str], out: deque):
        std_input = input_cmd
        temp_output = out

        # temp_output and out will no longer refer to the same object
        if self.output_file is not None:
            temp_output = deque()

        # input from file assigned to standard input
        if self.input_file is not None:
            with open(self.input_file, 'r') as file:
                std_input = ''.join(file.readlines())

        # No output printed on stdout if output file is present
        ApplicationFactory().app_by_name(self.app).exec(self.args, std_input,
                                                        temp_output)

        # Write output to the output file
        if self.output_file is not None:
            with open(self.output_file, 'w') as file:
                file.write(''.join(temp_output))
