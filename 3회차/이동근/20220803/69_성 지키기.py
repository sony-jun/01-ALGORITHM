N, M = map(int, input().split())

castle = [input() for _ in range(N)]

row_count, col_count = 0, 0

# X 없는 행, 열 개수 구하기
for i in range(N):
    if 'X' not in castle[i]:
        row_count += 1

for i in range(M):
    if 'X' not in [castle[j][i] for j in range(N)]:
        col_count += 1

# 둘 중 큰 값이 결국 문제 조건을 충족시키는 값이다.
# 작은 값을 고를 경우 문제 조건을 충족하지 못한다.
# https://tturbo0824.tistory.com/27
print(max(row_count, col_count))