from applications.application import Application
from applications.app_pwd import Pwd
from applications.app_echo import Echo
from applications.app_cd import Cd
from applications.app_ls import Ls
from applications.app_cat import Cat
from applications.app_grep import Grep
from applications.app_head import Head
from applications.app_tail import Tail
from applications.app_find import Find


class ApplicationFactory:
    def __init__(self):
        self.app_types = {'pwd': Pwd,
                          'echo': Echo
                          }

    def app_by_name(self, name: str) -> Application:
        return self.app_types[name]()

