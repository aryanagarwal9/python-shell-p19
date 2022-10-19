from abc import abstractmethod, ABC


class Application(ABC):
    @abstractmethod
    def exec(self):
        pass


class Pwd(Application):
    def __init__(self):
        pass

    def exec(self):
        print("hi i am pwd")

class Echo(Application):
    def __init__(self):
        pass

    def exec(self):
        print("hi i am echo")