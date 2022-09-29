'''
XX...
.XX..
...XX

'''

import sys
sys.stdin = open('1236.txt')

N,M = map(int, I().split())
a=[list(sys.stdin.readline()) for i in range(N)]
r,c=0,0

for i in range(N): # row
    if 'X' not in a[i]:
        r += 1
for j in range(M): # column
    if 'X' not in [a[i][j] for i in range(N)]:
        c += 1

print(max(r,c))