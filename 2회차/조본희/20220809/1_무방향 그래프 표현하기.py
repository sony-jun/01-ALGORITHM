import sys
from pprint import pprint
input = sys.stdin.readline
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
N, M = map(int, input().split())
N += 1
graph = [[0] * N for _ in range(N)]
adj = [[] for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    graph[v2][v1] = 1
    adj[v1].append(v2)
    adj[v2].append(v1)


pprint(graph)
print(adj)