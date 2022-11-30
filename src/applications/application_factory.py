from src.applications.app_cat import Cat
from src.applications.app_cd import Cd
from src.applications.app_cut import Cut
from src.applications.app_echo import Echo
from src.applications.app_find import Find
from src.applications.app_grep import Grep
from src.applications.app_head import Head
from src.applications.app_ls import Ls
from src.applications.app_mkdir import Mkdir
from src.applications.app_pwd import Pwd
from src.applications.app_sort import Sort
from src.applications.app_tail import Tail
from src.applications.app_uniq import Uniq
from src.applications.application import Application
from src.applications.app_wc import Wc
from src.applications.unsafe_decorator import UnsafeDecorator
from src.errors import ApplicationNotSupportedError


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
                          'find': Find,
                          'sort': Sort,
                          'uniq': Uniq,
                          'cut': Cut,
                          'mkdir': Mkdir,
                          'wc': Wc
                          }

    def app_by_name(self, name: str) -> Application:
        if (name.startswith('_') and name[1:] not in self.app_types) or (
                not name.startswith('_') and name not in self.app_types):
            raise ApplicationNotSupportedError(
                'Application currently not supported by the shell')

        if name.startswith('_'):
            return self.get_unsafe_app_object(name)
        return self.app_types[name]()

    def get_unsafe_app_object(self, name: str) -> Application:
        return UnsafeDecorator(self.app_types[name[1:]]())
