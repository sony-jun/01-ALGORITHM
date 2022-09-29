# 인접 행렬 
N, M = map(int, input().split())

graph = []
for i in range(N + 1):
    graph.append([0]* (N+1))
for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
print(graph)
