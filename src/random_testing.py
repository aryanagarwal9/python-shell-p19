from applications.application_factory import ApplicationFactory as af

command = af().app_by_name('pwd')
command.exec()