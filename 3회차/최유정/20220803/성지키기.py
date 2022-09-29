# https://www.acmicpc.net/problem/1236

N, M = map(int, input().split())
matrix = [list(input()) for n in range(N)]
row_cnt = 0
col_cnt = 0
for n in range(N):
    if 'X' not in matrix[n]:
        row_cnt += 1
for i in range(M):
    col_list = []
    for j in range(N):
        col_list.append(matrix[j][i]) #열 요소 담는 리스트
        if 'X' not in col_list:
            col_cnt += 1
print(col_list)
print(row_cnt, col_cnt)