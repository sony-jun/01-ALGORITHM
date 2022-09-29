import sys
sys.stdin = open("2_크로아티아_알파벳.txt", 'r') # dz=ak

s = input()

cro_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for alpha in cro_alpha:
    if alpha in s:
        s = s.replace(alpha, '*')

print(len(s))