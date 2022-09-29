N, M = map(int, input().split())

# 인접 행렬
matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1

pprint(matrix)

# 인접 리스트
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

print(graph)
