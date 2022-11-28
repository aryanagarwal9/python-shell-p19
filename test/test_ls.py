import os
import shutil
import unittest
from collections import deque

from src.applications.app_ls import Ls


class TestLs(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.given_directory = os.path.join(os.getcwd(), 'resources')
        os.mkdir(self.given_directory)

        for num_file in range(10):
            with open(
                    os.path.join(self.given_directory, f'file{str(num_file)}'),
                    'w') as file:
                file.write('Hello')

    def tearDown(self) -> None:
        shutil.rmtree(self.given_directory)

    def test_ls_current_directory(self):
        Ls().exec([], None, self.out)
        directory_content = '\t'.join(
            [file for file in (os.listdir(os.getcwd())) if
             not file.startswith('.')]) + '\n'
        self.assertEqual(self.out.popleft(), directory_content)

    def test_ls_given_directory(self):
        Ls().exec([self.given_directory], None, self.out)
        directory_content = '\t'.join(
            [file for file in (os.listdir(self.given_directory)) if
             not file.startswith('.')]) + '\n'
        self.assertEqual(self.out.popleft(), directory_content)

    def test_ls_multiple_arguments(self):
        app = Ls()
        self.assertRaises(ValueError, app.exec,
                          args=['directory1', 'directory2'], stdin=None,
                          out=self.out)
