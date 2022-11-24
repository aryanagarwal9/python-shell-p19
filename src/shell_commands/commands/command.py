from abc import abstractmethod, ABC
from collections import deque
from typing import Optional, List

class Command(ABC):
    @abstractmethod
    def eval(self, input_cmd: Optional[str], out: deque):
        pass
