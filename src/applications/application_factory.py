import applications.application as application


class ApplicationFactory:
    def __init__(self):
        self.app_types = {'pwd': application.Pwd,
                          'echo': application.Echo
                          }

    def app_by_name(self, name: str) -> application.Application:
        return self.app_types[name]()
