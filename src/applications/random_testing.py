import subprocess

s = "line1 word1 word2\nline2 word3 word4\nline3 word5 word6\n"
print(s.splitlines(True))
print(s.split())

print(subprocess.check_output(['wc', '-c', '/Users/adityaparashar/UCL/Year2/COMP0010/CW/h1.txt']).decode('utf8').split()[0])
