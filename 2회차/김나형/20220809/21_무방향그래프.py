
import sys
from pprint import pprint
sys. stdin = open ("21_무방향그래프.txt")

N, M = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N+1)]
graph1 = [[] for _ in range(N+1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph [v1][v2] = 1
    graph [v2][v1] = 1

    graph1[v1].append(v2)
    graph1[v2].append(v1)
pprint(graph)
pprint(graph1)