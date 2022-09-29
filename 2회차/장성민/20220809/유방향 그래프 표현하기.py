from pprint import pprint

N, M = map(int, input().split())

all = 7
matrix = [[0] * all for _ in range(all)]
list = [[] for _ in range(all)]

for _ in range(M):
    u, v = map(int, input().split())
    matrix[u][v] = 1
    list[u].append(v)

pprint(matrix)
print(list)
