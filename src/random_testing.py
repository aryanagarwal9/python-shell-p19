import os
import sys

# from applications.application_factory import ApplicationFactory

# command = ApplicationFactory().app_by_name('pwd')
# command.exec()

print(os.getcwd())
contents = [content for content in os.listdir(os.getcwd())]
print(contents)
print("\t".join(contents) + '\n')