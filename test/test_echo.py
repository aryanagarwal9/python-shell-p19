import unittest
from collections import deque
from applications.app_echo import Echo


class TestEcho(unittest.TestCase):
    def setUp(self) -> None:
        self.out = deque()

    def no_argument_provided(self):
        self.assertEqual()


