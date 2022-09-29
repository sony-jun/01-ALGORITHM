# 성 지키기
# 문제 : 모든 행과 열에 경비원 배치하기, 최소로 배치해야 하는 경비원의 수는?

n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]  # 이차원 리스트 생성

row = [0] * n  # 행렬 리스트
col = [0] * m

for x in range(n):  # 이중 for문으로 전부 확인
    for y in range(m):
        if matrix[x][y] == 'X':  # 'X' 라면 행렬에 1로 변경
            row[x] = 1
            col[y] = 1

cnt_row = 0
cnt_col = 0

# 비어있는 행렬 찾기 (0)
for i in row:
    if i == 0:
        cnt_row += 1

for i in col:
    if i == 0:
        cnt_col += 1

print(max(cnt_row, cnt_col))  # 최소 경비원의 수
