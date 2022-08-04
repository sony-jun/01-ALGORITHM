# https://www.acmicpc.net/problem/1652

import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')
input = sys.stdin.readline

N = int(input())
room = [list(map(str, input().rstrip()))for _ in range(N)]
row_cnt = 0

for i in range(N): # 가로 체크
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':
            cnt += 1
        else:
            if cnt > 1:
                row_cnt += 1
            cnt = 0
    else:
        if cnt > 1:
            row_cnt += 1
            cnt = 0

col_cnt = 0
for i in range(N): # 세로 체크
    cnt = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt += 1
        else:
            if cnt > 1:
                col_cnt += 1
            cnt = 0
    else:
        if cnt > 1:
            col_cnt += 1
            cnt = 0
print(row_cnt, col_cnt)