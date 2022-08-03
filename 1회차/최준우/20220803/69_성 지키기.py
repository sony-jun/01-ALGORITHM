# https://www.acmicpc.net/problem/1236

N, M = map(int, input().split())
castle = [list(map(str, input().rstrip())) for _ in range(N)]
row_cnt = 0 # 행에 'X'가 없을때 카운트할 변수
col_cnt = 0 # 열에 'X'가 없을때 카운트할 변수 

for i in range(N): # 행 체크
    if 'X' not in castle[i]:
        row_cnt += 1

for j in range(M): # 열체크
    if 'X' not in [castle[i][j] for i in range(N)]:
        col_cnt += 1
print(max(row_cnt, col_cnt)) # 둘 중에 큰 값을 출력