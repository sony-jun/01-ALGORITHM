import sys
sys.stdin = open("3_2차원배열의합.txt")

N, M = map(int, input().split())
list_ = []
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matrix =[[0]*(M+1) for _ in range(N+1)]

# [[1, 2, 4], [8, 16, 32]]
for _ in range(N):
    list_.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, M+1):
        # 본래 값 + 왼쪽 + 위쪽 - 대각선
        matrix[i][j] = list_[i-1][j-1] + matrix[i][j-1] + matrix[i-1][j] - matrix[i-1][j-1]

# (g, h)에서 (a, b)까지의 합을 구하는 공식
# (0, 0) ~ (a, b)까지의 합 - (0, 0) ~ (c, d)까지의 합 - (0, 0) ~ (e, f)까지의 합 + (0, 0) ~ (g, h)까지의 합
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(matrix[x][y]-matrix[x][j-1]-matrix[i-1][y]+matrix[i-1][j-1])


#더 공부해 볼 것