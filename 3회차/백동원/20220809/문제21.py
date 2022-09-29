# 무방향 그래프 표현하기
from pprint import pprint

N, M = map(int, input().split())
matrix = [[0] * (N + 1) for _ in range(N + 1)]
list_ = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    matrix[v][u] = 1
    list_[u].append(v)
    list_[v].append(u)
pprint(matrix)
pprint(list_)