# 성의 세로, 가로 크기의 개수
N, M = map(int,input().split())

matrix = []
for _ in range(N):
    matrix.append(input())

# [0] 으로 초기화
row = [0] * N
col = [0] * M

# 'X' 있으면 해당 행렬의 요소 1로 변경
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'X':
            row[i] = 1
            col[j] = 1

# 'X' 없는 행과 열의 개수를 세서, 큰 값 출력
row_cnt = 0
for i in range(N):
    if row[i] == 0:
        row_cnt += 1

col_cnt = 0
for j in range(M):
    if col[j] == 0:
        col_cnt += 1

print(max(row_cnt, col_cnt))