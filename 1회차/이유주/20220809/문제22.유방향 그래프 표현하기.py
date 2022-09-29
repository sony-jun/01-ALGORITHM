N, M = map(int,input().split()) #정점 개수,간선 개수

#인접 행렬
graph1 = [[0]*(N+1) for _ in range(N+1)]

#인접리스트
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph1[u][v] = 1
    graph[u].append(v)

print(graph1)
print(graph)