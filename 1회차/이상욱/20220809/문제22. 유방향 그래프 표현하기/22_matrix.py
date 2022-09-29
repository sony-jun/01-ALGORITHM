from pprint import pprint
import sys
sys.stdin = open ('22.txt')

n, m = map(int, input().split())
edges = []
matrix = [[0] *(n+1) for _ in range(n+1)]

for i in range(m):
    edges.append(list(map(int, input().split())))

for edge in edges:
    v1, v2 = edge[0], edge[1]
    matrix[v1][v2] = 1

pprint(matrix)