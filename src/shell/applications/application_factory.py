from shell.applications.app_cat import Cat
from shell.applications.app_cd import Cd
from shell.applications.app_cut import Cut
from shell.applications.app_echo import Echo
from shell.applications.app_find import Find
from shell.applications.app_grep import Grep
from shell.applications.app_head import Head
from shell.applications.app_ls import Ls
from shell.applications.app_mkdir import Mkdir
from shell.applications.app_pwd import Pwd
from shell.applications.app_sort import Sort
from shell.applications.app_tail import Tail
from shell.applications.app_uniq import Uniq
from shell.applications.application import Application
from shell.applications.app_wc import Wc
from shell.applications.unsafe_decorator import UnsafeDecorator
from shell.errors import ApplicationNotSupportedError


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
        """Returns the corresponding object using application name
        """

        # Check if name is a supported application
        if (name.startswith('_') and name[1:] not in self.app_types) or (
                not name.startswith('_') and name not in self.app_types):
            raise ApplicationNotSupportedError(
                'Application currently not supported by the shell')

        # Unsafe application version
        if name.startswith('_'):
            return self.get_unsafe_app_object(name)
        return self.app_types[name]()

    def get_unsafe_app_object(self, name: str) -> Application:
        return UnsafeDecorator(self.app_types[name[1:]]())
