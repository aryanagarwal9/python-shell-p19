from abc import abstractmethod, ABC


class Application(ABC):
    @abstractmethod
    def exec(self):
        self.exec()


class Pwd(Application):
    def __init__(self):
        pass

    def exec(self):
        print("hi i am pwd")