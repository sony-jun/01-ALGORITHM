#77
import sys
sys.stdin = open("무방향그래프표현하기.txt")
from pprint import pprint

N, M = map(int,input().split())
uv = [list(map(int,input().split())) for _ in range(M) ]

graph = [[0]*(N+1) for _ in range(N+1)]
pprint(graph)
print(uv)
for a in range(M):
    graph[uv[a][0]][uv[a][1]] = 1
    graph[uv[a][1]][uv[a][0]] = 1
pprint(graph)

graph_list = [[] for _ in range(N+1)]
for a in range(M):
    graph_list[uv[a][0]].append(uv[a][1])
    graph_list[uv[a][1]].append(uv[a][0])

pprint(graph_list)