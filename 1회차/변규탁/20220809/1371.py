import sys


N = sys.stdin.read()
M = N.replace('\n', '').replace(' ', '')
list_ = [0]*26

for i in M:
    list_[ord(i)-97] += 1

for i in range(len(list_)):
    if list_[i] == max(list_):
        print(chr(97+i), end="")