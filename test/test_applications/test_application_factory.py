import unittest

from parameterized import parameterized

from src.applications.app_cat import Cat
from src.applications.app_cd import Cd
from src.applications.app_echo import Echo
from src.applications.app_find import Find
from src.applications.app_grep import Grep
from src.applications.app_head import Head
from src.applications.app_ls import Ls
from src.applications.app_pwd import Pwd
from src.applications.app_tail import Tail
from src.applications.application_factory import ApplicationFactory
from src.applications.unsafe_decorator import UnsafeDecorator
from src.errors import ApplicationNotSupportedError


class TestApplicationFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.app_types = {'pwd': Pwd,
                          'echo': Echo,
                          'cd': Cd,
                          'ls': Ls,
                          'cat': Cat,
                          'grep': Grep,
                          'head': Head,
                          'tail': Tail,
                          'find': Find,
                          }

    def test_application_factory(self):
        af = ApplicationFactory()
        for name, app in self.app_types.items():
            received_app = af.app_by_name(name)
            self.assertIsInstance(received_app, app)

    def test_application_factory_unsafe_command(self):
        af = ApplicationFactory()
        for name in self.app_types:
            received_app = af.app_by_name('_' + name)
            self.assertIsInstance(received_app, UnsafeDecorator)

    @parameterized.expand([
        ['unsupported app', 'xyz'],
        ['unsupported unsafe app', '_xyz']
    ])
    def test_application_factory_unsupported_application(self, name, app):
        af = ApplicationFactory()
        self.assertRaises(ApplicationNotSupportedError, af.app_by_name, app)
