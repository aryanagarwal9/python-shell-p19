from abc import abstractmethod, ABC
from collections import deque
from typing import Optional


class Application(ABC):
    @abstractmethod
    def exec(self, args: list, stdin: Optional[str], out: deque):
        pass

