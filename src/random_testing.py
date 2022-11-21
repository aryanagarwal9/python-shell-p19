

from applications.application_factory import ApplicationFactory
import os
import sys

command = ApplicationFactory().app_by_name('pwd')
command.exec()

print('**abc\n')

a,b,c = (1,2,3)
print(a,b,c)
# Hello
# Hello
# Hi
# Hello
# Hello
# Hello
# Hey
#
# curr_word = None
# for line in file:
#     if curr_word is None:
#         curr_word=line
#     elif line!=curr_word:
#         out.append(curr_word+'\n')
#         curr_word=line
# out.append(curr_word)

