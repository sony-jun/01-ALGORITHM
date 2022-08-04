# 백준 누울 자리를 찾아라 1652 https://www.acmicpc.net/problem/1652

matrix_ = []
N = int(input())
M = N
count = 0
plus = 0
h = 0
total = 0
for i in range(N):
    matrix_.append(list(input()))
    for idx in range(M):
        if matrix_[i][idx] != 'X':
            plus += 1
        elif matrix_[i][idx] == 'X':
            plus = 0
        if plus == 2:
            count += 1
    plus = 0

for i in range(N):
    for idx in range(M):
        if matrix_[idx][i] != 'X':
            h += 1
        elif matrix_[idx][i] == 'X':
            h = 0
        if h == 2:
            total += 1
    h = 0
print(count, total)
            