import sys
from pprint import pprint 

sys.stdin = open('21.txt')

N, M = map(int, input().split())

graph_1 =  [[0]* (N + 1) for _ in range(N + 1)]
graph_2 = [[] for _ in range(N + 1)]

for i in range(M):
    x, y = map(int, input().split())
    graph_1[x][y] = 1
    graph_1[y][x] = 1
    graph_2[x].append(y)
    graph_2[y].append(x)
pprint(graph_1)
print(graph_2)