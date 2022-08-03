# 2차원 배열의 합

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

K = int(input())

for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for a in range(i - 1, x):
        for b in range(j - 1, y):
            result += matrix[a][b]
    print(result)