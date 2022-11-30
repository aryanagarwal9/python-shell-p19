import os
import shutil
import unittest
from collections import deque
from subprocess import check_output

from shell.applications.app_wc import Wc
from shell.errors import FlagError, ArgumentError


class TestWc(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()
        self.directory = 'resources'
        self.original_directory = os.getcwd()
        os.mkdir(self.directory)
        os.chdir(self.directory)

        self.files = {
            'test1.txt': 'Hello\nI\nam\ntesting\nfile\nfor\napplication\nwc\n',
            'test2.txt': 'We\nhave\nimplemented\nthree\nflags',
            'test3.txt': 'This\nis\nCOMP0010\nshell\nin\npython\n'
        }

        for file_name in self.files:
            with open(file_name, 'w') as file:
                file.write(self.files[file_name])

        self.stdin = 'Hello\nI\nam\ntesting\ninput\nfor\napplication\nwc\n'

    def tearDown(self) -> None:
        os.chdir(self.original_directory)
        shutil.rmtree(self.directory)

    def test_wc_number_of_lines_in_single_file(self):
        Wc().exec(['-l', 'test1.txt'], None, self.out)
        result = ['\t{} test1.txt\n'.format(
            check_output(["wc", "-l", "test1.txt"]).decode("utf8").split()[0])]
        self.assertEqual(list(self.out), result)

    def test_wc_number_of_lines_in_multiple_files(self):
        Wc().exec(['-l', 'test1.txt', 'test2.txt', 'test3.txt'], None,
                  self.out)
        total = int(
            check_output(["wc", "-l", "test1.txt"]).decode("utf8").split()[
                0]) + int(
            check_output(["wc", "-l", "test2.txt"]).decode("utf8").split()[
                0]) + int(
            check_output(["wc", "-l", "test3.txt"]).decode("utf8").split()[0])

        result = [
            '\t{} test1.txt\n'.format(
                check_output(["wc", "-l", "test1.txt"]).decode("utf8").split()[
                    0]),
            '\t{} test2.txt\n'.format(
                check_output(["wc", "-l", "test2.txt"]).decode("utf8").split()[
                    0]),
            '\t{} test3.txt\n'.format(
                check_output(["wc", "-l", "test3.txt"]).decode("utf8").split()[
                    0]),
            '\t{} total\n'.format(total)]
        self.assertEqual(list(self.out), result)

    def test_wc_number_of_words_in_single_file(self):
        Wc().exec(['-w', 'test1.txt'], None, self.out)
        result = [
            '\t{} test1.txt\n'.format(
                check_output(["wc", "-w", "test1.txt"]).decode("utf8").split()[
                    0])]
        self.assertEqual(list(self.out), result)

    def test_wc_number_of_words_in_multiple_files(self):
        Wc().exec(['-w', 'test1.txt', 'test2.txt', 'test3.txt'], None,
                  self.out)
        total = int(
            check_output(["wc", "-w", "test1.txt"]).decode("utf8").split()[
                0]) + int(
            check_output(["wc", "-w", "test2.txt"]).decode("utf8").split()[
                0]) + int(
            check_output(["wc", "-w", "test3.txt"]).decode("utf8").split()[0])

        result = [
            '\t{} test1.txt\n'.format(
                check_output(["wc", "-w", "test1.txt"]).decode("utf8").split()[
                    0]),
            '\t{} test2.txt\n'.format(
                check_output(["wc", "-w", "test2.txt"]).decode("utf8").split()[
                    0]),
            '\t{} test3.txt\n'.format(
                check_output(["wc", "-w", "test3.txt"]).decode("utf8").split()[
                    0]),
            '\t{} total\n'.format(total)]
        self.assertEqual(list(self.out), result)

    def test_wc_number_of_bytes_in_single_file(self):
        Wc().exec(['-w', 'test1.txt'], None, self.out)
        result = [
            '\t{} test1.txt\n'.format(
                check_output(["wc", "-w", "test1.txt"]).decode("utf8").split()[
                    0])]
        self.assertEqual(list(self.out), result)

    def test_wc_number_of_bytes_in_multiple_files(self):
        Wc().exec(['-c', 'test1.txt', 'test2.txt', 'test3.txt'], None,
                  self.out)
        total = int(
            check_output(["wc", "-c", "test1.txt"]).decode("utf8").split()[
                0]) + int(
            check_output(["wc", "-c", "test2.txt"]).decode("utf8").split()[
                0]) + int(
            check_output(["wc", "-c", "test3.txt"]).decode("utf8").split()[0])

        result = [
            '\t{} test1.txt\n'.format(
                check_output(["wc", "-c", "test1.txt"]).decode("utf8").split()[
                    0]),
            '\t{} test2.txt\n'.format(
                check_output(["wc", "-c", "test2.txt"]).decode("utf8").split()[
                    0]),
            '\t{} test3.txt\n'.format(
                check_output(["wc", "-c", "test3.txt"]).decode("utf8").split()[
                    0]),
            '\t{} total\n'.format(total)]
        self.assertEqual(list(self.out), result)

    def test_wc_number_of_lines_stdin(self):
        Wc().exec(['-l'], self.stdin, self.out)
        self.assertEqual(list(self.out), ['\t8\n'])

    def test_wc_number_of_words_stdin(self):
        Wc().exec(['-w'], self.stdin, self.out)
        self.assertEqual(list(self.out), [f'\t{len(self.stdin.split())}\n'])

    def test_wc_number_of_bytes_stdin(self):
        Wc().exec(['-c'], self.stdin, self.out)
        self.assertEqual(list(self.out),
                         [f'\t{len(self.stdin.encode("utf-8"))}\n'])

    def test_wc_no_flag_provided(self):
        app = Wc()
        self.assertRaises(FlagError, app.exec, ['test1.txt', 'test2.txt'],
                          None, self.out)

    def test_wc_no_arguments_no_stdin(self):
        app = Wc()
        self.assertRaises(ArgumentError, app.exec, ['-c'], None, self.out)
