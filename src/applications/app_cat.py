from collections import deque
from typing import Optional

from applications.application import Application

class Cat(Application):
    def exec(self, args: list, stdin: Optional[str], out: deque):
<<<<<<< HEAD
        print("hi i am echo")
=======
        if len(args):
            self.handle_file_arguments(args, out)
        else:
            self.handle_stdin_argument(stdin, out)


    def handle_stdin_argument(self, stdin: Optional[str], out: deque):
        stdin_input= stdin.split('\n')
        for line in stdin_input:
            out.append(line+'\n')


    def handle_file_arguments(self,args: list, out: deque):
        concatenated_output = ''
        for file_name in args:
            with open(file_name,'r') as file:
                concatenated_output+=file.read()
        out.append(concatenated_output+'\n')
>>>>>>> c9ca63865e53ae700f368b615b0bc086ec52acbc
