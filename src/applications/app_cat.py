from collections import deque
from typing import Optional

from applications.application import Application


class Cat(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
        if len(args):
            self.handle_file_arguments(args, out)
        else:
            self.handle_stdin_argument(stdin, out)

    def handle_stdin_argument(self, stdin: Optional[str], out: deque):
        out.append(stdin)

    def handle_file_arguments(self, args: list, out: deque):
        concatenated_output = ''
        for file_name in args:
            with open(file_name, 'r') as file:
                concatenated_output += file.read()
        out.append(concatenated_output)

# out = deque()
# Cat().exec(['/Users/adityaparashar/UCL/Year2/COMP0010/CW/h1.txt', '/Users/adityaparashar/UCL/Year2/COMP0010/CW/h2.txt'], 'hello', out)
# print(out.popleft())