
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]


for k in range(int(input())):
    sum = 0
    i, j, x, y = map(int, input().split())

    for a in range(i-1, x):
        for b in range(j-1, y):
            sum += matrix[a][b]
    print(sum)



# N, M = map(int, input().split())

# numbers = [list(map(int, input().split())) for _ in range(N)]

# sum_arr = [[0 for _ in range(M+1)] for _ in range(N+1)]
# for i in range(1, N + 1):
#     for j in range(1, M +1):
#         sum_arr[i][j] = numbers[i-1][j-1] + (sum_arr[i-1][j]) \
#             + (sum_arr[i][j-1]) - (sum_arr[i-1][j-1])

# K = int(input())
# for _ in range(K):
#     i, j, x, y = map(int, input().split())
#     print(sum_arr[x][y] - sum_arr[x][j-1] \
#         - sum_arr[i-1][y] + sum_arr[i-1][j-1])