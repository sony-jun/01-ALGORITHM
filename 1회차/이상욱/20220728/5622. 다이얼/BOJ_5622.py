import sys
sys.stdin = open ('5622.txt')
list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
num = 0


for i in list:
    for j in word:
        if j in i:
            num = num + list.index(i) + 3
print(num)