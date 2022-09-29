import sys
input = sys.stdin.readline
T = int(input())
matrix = [list(input().rstrip()) for _ in range(T)]
row = 0
for i in matrix:
    cnt = 0
    for j in i:
        if j == '.':
            cnt += 1
        else:
            if cnt > 1:
                row += 1
            cnt = 0
    if cnt > 1:
        row += 1
col = 0
for i in range(len(matrix)):
    cnt = 0
    for j in range(T):
        if matrix[j][i] == '.':
            cnt += 1
        else:
            if cnt > 1:
                col += 1
            cnt = 0
    if cnt > 1:
        col += 1
print(row, col)