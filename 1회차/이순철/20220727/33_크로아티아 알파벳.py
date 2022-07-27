
import sys

sys.stdin = open("33_크로아티아 알파벳.txt")


cro = input()
# print(cro)
cro_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in cro_a:
    cro = cro.replace(i, '*')
    # print(cro)
print(len(cro))