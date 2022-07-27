import sys
sys.stdin = open('B2941.txt')

word = input()
c_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in c_alph:
    count = word.replace(i, '!')
    word = count

print(len(word))