from applications.application import Application, Pwd


class ApplicationFactory:
    def __init__(self):
        self.app_types = {'pwd': Pwd
                          }

    def app_by_name(self, name: str) -> Application:
        return self.app_types[name]()
