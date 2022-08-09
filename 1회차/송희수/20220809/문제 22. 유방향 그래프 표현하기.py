import sys
from pprint import pprint

sys.stdin = open("문제 22. 유방향 그래프 표현하기.txt")

N, M = map(int, input().split())

graph1 = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph1[u][v] = 1
    
pprint(graph1)

import sys

sys.stdin = open("문제 22. 유방향 그래프 표현하기.txt")

N, M = map(int, input().split())

graph2 = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph2[u].append(v)

print(graph2)