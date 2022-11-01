import os

from applications.application import Application

class Pwd(Application):
    def __init__(self):
        pass

    def exec(self):
        return os.getcwd()