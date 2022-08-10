import sys
from pprint import pprint
input = sys.stdin.readline

N, M = map(int, input().split())
N += 1

graph = [[0] * N for _ in range(N)]
edge = [[] for _ in range(N)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1][v2] = 1
    edge[v1].append(v2)

pprint(graph)
print(edge)