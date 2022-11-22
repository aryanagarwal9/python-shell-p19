from src.applications.application import Application
from src.applications.app_pwd import Pwd
from src.applications.app_echo import Echo
from src.applications.app_cd import Cd
from src.applications.app_ls import Ls
from src.applications.app_cat import Cat
from src.applications.app_grep import Grep
from src.applications.app_head import Head
from src.applications.app_tail import Tail
from src.applications.app_find import Find


class ApplicationFactory:
    def __init__(self):

        self.app_types = {'pwd': Pwd,
                          'echo': Echo,
                          'cd': Cd,
                          'ls': Ls,
                          'cat': Cat,
                          'grep': Grep,
                          'head': Head,
                          'tail': Tail,
                          'find': Find
                          }

    def app_by_name(self, name: str) -> Application:
        return self.app_types[name]()

