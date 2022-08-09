from pprint import pprint

N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1

graph1 = [[] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph1[u].append(v)
    graph1[v].append(u)

pprint(graph)
pprint(graph1)