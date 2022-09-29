import sys
sys.stdin = open('22.txt')

n, m = map(int, input().split())

graph = [[] * 7 for _ in range(7)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)

print(graph)