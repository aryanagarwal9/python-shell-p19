import unittest
from collections import deque

from applications.app_echo import Echo

# class EchoTest(unittest.TestCase):
#     def __init__(self):
#         super().__init__()

d = {3:2, 1:1, 10:1,2:2, 4:5, 6:5}
print(sorted(sorted(list(d.items())), key=lambda x:x[1], reverse=True))