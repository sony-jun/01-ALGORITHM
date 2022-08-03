# n x m
from pprint import pprint
n, m = map(int,input().split())
matrix = [list(input()) for _ in range(n)]
cnt_m = 0
cnt_n = 0
for idx1 in range(m):
    cap = False
    for idx2 in range(n):
        if matrix[idx2][idx1] == 'X':
            cap = True
    if cap == False:
        cnt_m += 1

for idx1 in range(n):
    cap = False
    for idx2 in range(m):
        if matrix[idx1][idx2] == 'X':
            cap = True
    if cap == False:
        cnt_n += 1
print(max(cnt_n,cnt_m))