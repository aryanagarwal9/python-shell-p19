from abc import abstractmethod, ABC
from collections import deque
from typing import Optional
<<<<<<< HEAD

class Application(ABC):
    @abstractmethod
    def exec(self, args: list, stdin: Optional[list], out: deque):
=======


class Application(ABC):
    @abstractmethod
    def exec(self, args: list[str], stdin: Optional[list], out: deque):
>>>>>>> 9d530b0b1e0e7447b3aa0ec0c6887327625ecb4e
        pass



