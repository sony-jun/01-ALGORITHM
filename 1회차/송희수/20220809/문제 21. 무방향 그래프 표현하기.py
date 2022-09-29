import sys
from pprint import pprint

sys.stdin = open("문제 21. 무방향 그래프 표현하기.txt")

N, M = map(int, input().split())

graph1 = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph1[u][v] = 1
    graph1[v][u] = 1

import sys

sys.stdin = open("문제 21. 무방향 그래프 표현하기.txt")

N, M = map(int, input().split())

graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph2[u].append(v)
    graph2[v].append(u)


pprint(graph1)
print(graph2)