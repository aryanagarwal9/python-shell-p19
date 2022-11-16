from abc import abstractmethod, ABC
from collections import deque
from typing import Optional

class Application(ABC):
    @abstractmethod
    def exec(self, args: list[str], stdin: Optional[str], out: deque):
        pass



