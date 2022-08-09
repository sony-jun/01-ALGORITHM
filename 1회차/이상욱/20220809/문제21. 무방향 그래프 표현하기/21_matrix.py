from pprint import pprint
import sys
sys.stdin = open ('21.txt')

n, m = map(int, input().split())

matrix = [[0] * 7 for _ in range(n+1)]
edges=[]
for i in range(m):
    edges.append(list(map(int, input().split())))

for edge in edges:
    v1, v2 = edge[0], edge[1]
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

pprint(matrix)
