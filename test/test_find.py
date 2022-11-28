import os
import shutil
import unittest
from collections import deque

from parameterized import parameterized

from src.applications.app_find import Find
from src.errors import FlagError


class TestFind(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        os.mkdir('resources')
        os.chdir(self.directory)

        sub_dirs = {
            'resources1': ['app1.txt', 'test1.txt', 'src', 'inner_resource'],
            'resources2': ['app2.txt', 'test2.txt', 'src', 'inner_resource']
        }

        for sub_dir in sub_dirs:
            os.mkdir(sub_dir)
            for file_name in sub_dirs[sub_dir]:
                if not file_name.endswith('.txt'):
                    os.mkdir(os.path.join(sub_dir, file_name))
                    continue

                with open(os.path.join(sub_dir, file_name), 'w') as file:
                    file.write('I am a file')

    def tearDown(self) -> None:
        os.chdir('..')
        shutil.rmtree(self.directory)

    @parameterized.expand([
        ['inside_single_directory', ['resources1', '-name', '*rc*'],
         ['resources1\n', 'resources1/inner_resource\n',
          'resources1/src\n']],
        ['inside_directory_tree', ['resources2', '-name', '*es*'],
         ['resources2\n', 'resources2/inner_resource\n',
          'resources2/test2.txt\n']]
    ])
    def test_find_when_path_provided(self, name, args, result):
        Find().exec(args, None, self.out)
        self.assertEqual(sorted(self.out), result)

    def test_find_when_path_not_provided(self):
        Find().exec(['-name', '*txt'], None, self.out)
        self.assertEqual(sorted(self.out), ['./resources1/app1.txt\n',
                                            './resources1/test1.txt\n',
                                            './resources2/app2.txt\n',
                                            './resources2/test2.txt\n'])

    def test_find_flag_not_provided(self):
        app = Find()
        self.assertRaises(FlagError, app.exec, args=['resources1', '*.txt'],
                          stdin=None, out=self.out)

    @parameterized.expand([
        ['argument_length_is_2', ['*txt', '-name'], FlagError],
        ['argument_length_is_3', ['-name', 'resources1', '*txt'], FlagError]
    ])
    def test_find_flag_not_on_correct_index(self, name, args, result):
        app = Find()
        self.assertRaises(result, app.exec, args=args, stdin=None,
                          out=self.out)

    @parameterized.expand([
        ['less than 2 arguments', ['-name'], ValueError],
        ['more than 3 arguments',
         ['resources1', 'resources2', '-name', '*.txt'], ValueError]
    ])
    def test_find_wrong_number_of_arguments(self, name, args, result):
        app = Find()
        self.assertRaises(result, app.exec, args=args, stdin=None,
                          out=self.out)
