import os
import shutil
import unittest
from collections import deque

from applications.app_cd import Cd

class TestCd(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.sub_directory = 'resource1/resource2'
        self.test_directory = os.getcwd()
        os.makedirs(os.path.join(self.test_directory, self.sub_directory))

    def tearDown(self) -> None:
        os.chdir(self.test_directory)
        shutil.rmtree('resource1')

    def test_cd_home_directory(self):
        Cd().exec([], None, self.out)
        self.assertEqual(os.getcwd(), os.path.expanduser('~'))

    def test_cd_directory_provided(self):
        Cd().exec([self.sub_directory], None, self.out)
        self.assertEqual(os.getcwd(), os.path.join(self.test_directory,self.sub_directory))

    def test_cd_multiple_arguments(self):
        app = Cd()
        self.assertRaises(ValueError, app.exec, args=['directory1', 'directory2'], stdin=None, out=self.out)

