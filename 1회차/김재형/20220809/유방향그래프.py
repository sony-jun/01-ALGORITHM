import sys
sys.stdin = open('유방향그래프_input.txt')
from pprint import pprint

# 인접 행렬
n, m = map(int, input().split())

matrix = [[0] * 7 for _ in range(7)]
graph = [[] for _ in range(7)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    matrix[v1][v2] = 1

    graph[v1].append(v2)

    
    
pprint(matrix)
pprint(graph)
