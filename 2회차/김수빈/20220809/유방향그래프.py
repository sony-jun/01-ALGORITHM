from pprint import pprint
N, M = map(int, input().split())

graph = []
for i in range(N + 1):
    graph.append([0] * (N + 1))

list_ = []
for i in range(N + 1):
    list_.append([])

for j in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    list_[u].append(v)

pprint(graph)
print(list_)