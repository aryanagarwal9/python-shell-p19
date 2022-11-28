from collections import deque
from typing import Optional, List

from src.shell_commands.commands.command import Command
from src.applications.application_factory import ApplicationFactory


class Call(Command):
    def __init__(self, app: str, args: List[str], input_file: Optional[str], output_file: Optional[str]):
        self.app = app
        self.args = args
        self.input_file = input_file
        self.output_file = output_file

    def eval(self, input_cmd: Optional[str], out: deque):
        std_input = input_cmd
        temp_output = out

        if self.output_file is not None:
            temp_output = deque()

        if self.input_file is not None:
            with open(self.input_file, 'r') as file:
                std_input = ''.join(file.readlines())

        ApplicationFactory().app_by_name(self.app).exec(self.args, std_input, temp_output)

        if self.output_file is not None:
            with open(self.output_file, 'w') as file:
                file.write(''.join(temp_output))



