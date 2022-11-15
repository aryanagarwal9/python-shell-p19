from applications.application_factory import ApplicationFactory

command = ApplicationFactory().app_by_name('pwd')
command.exec()


