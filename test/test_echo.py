import unittest
from collections import deque

from hypothesis import given, strategies

from src.applications.app_echo import Echo


class TestEcho(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    def test_echo_no_argument_provided(self):
        Echo().exec([], None, self.out)
        self.assertEqual(self.out.popleft(), '\n')
        self.assertEqual(len(self.out), 0)

    @given(strategies.text())
    def test_echo_arguments_provided(self, text):
        Echo().exec([text], None, self.out)
        self.assertEqual(self.out.popleft(), text + '\n')
        self.assertEqual(len(self.out), 0)

    def test_echo_flag_no_argument_provided(self):
        Echo().exec(['-n'], None, self.out)
        self.assertEqual(self.out.popleft(), "")
        self.assertEqual(len(self.out), 0)

    @given(strategies.text())
    def test_echo_flag_arguments_provided(self, text):
        Echo().exec(['-n', text], None, self.out)
        self.assertEqual(self.out.popleft(), text)
        self.assertEqual(len(self.out), 0)
