n, m = map(int, input().split())

matrix = [[0] * (n + 1) for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for i in range(m):
    u, v = map(int, input().split())
    matrix[u][v] = 1

    graph[u].append(v)

print(matrix)
print(graph)
