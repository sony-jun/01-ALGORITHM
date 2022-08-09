from pprint import pprint

N = int(input())
M = int(input())

matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

pprint(matrix)


