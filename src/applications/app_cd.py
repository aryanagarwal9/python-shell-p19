import os
from collections import deque
from typing import Optional

from applications.application import Application

class Cd(Application):
<<<<<<< HEAD
    def exec(self, args: list, stdin: Optional[str], out: deque):
        print("hi i am echo")
=======
    def exec(self, args: list, stdin: Optional[list], out: deque):
        if len(args)>1:
            raise ValueError("Maximum of one argument expected")
        os.chdir(args[0]) if len(args) else os.chdir(os.path.expanduser("~"))


 
>>>>>>> c9ca63865e53ae700f368b615b0bc086ec52acbc
