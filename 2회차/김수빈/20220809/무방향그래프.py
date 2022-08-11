# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현

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
    graph[v][u] = 1
    list_[u].append(v)
    list_[v].append(u)

pprint(graph)
print(list_)