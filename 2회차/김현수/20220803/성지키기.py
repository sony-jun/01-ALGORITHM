import sys
sys.stdin = open('성지키기.txt','r')
from pprint import pprint

N, M = map(int,input().split())

matrix = [list(input()) for _ in range(N)]

pprint(matrix)
cnt_n = 0
cnt_m = 0

for n in range(N): 
    for m in range(M):
        if matrix[n][m] == 'X':
            break
    else:
        cnt_n += 1
    # if 'X' in matrix[n]

for m in range(M):
    for n in range(N):
        if matrix[n][m] == 'X':
            break
    else:
        cnt_m += 1

print(max(cnt_n,cnt_m))