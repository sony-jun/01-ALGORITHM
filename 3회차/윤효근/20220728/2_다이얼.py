import sys


sys.stdin = open("2_다이얼.txt")


dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
w=input()
result=0
for j in range(len(w)):
    for i in dial:
        if w[j] in i:
            result += dial.index(i)+3
print(result)