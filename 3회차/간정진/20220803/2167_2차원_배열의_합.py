import sys

sys.stdin = open("2167.txt", "r")

# N, M = map(int, input().split())
# temp = 0

# matrix = [list(map(int, input().split())) for _ in range(N)]

# K = int(input())
# sum = 0

# for _ in range(K):
#     i, j, x, y = map(int, input().split())

#     for k in range(i-1, x):
#         for q in range(j-1, y):
#             sum += matrix[k][q]
#     print(sum)
#     sum = 0


N, M = map(int, input().split())
temp = 0

matrix = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = matrix[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
    
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])