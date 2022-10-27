from abc import abstractmethod, ABC


class Application(ABC):
    @abstractmethod
    def exec(self):
        pass



