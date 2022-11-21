from abc import abstractmethod, ABC
from collections import deque
from typing import Optional


class Application(ABC):
    @abstractmethod
    def exec(self, args: List[str], stdin: Optional[str], out: deque):
        pass
