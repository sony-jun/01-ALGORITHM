import sys
sys.stdin = open ('21.txt')

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m): # _가 0일때
    v1, v2 = map(int, input().split()) # v1, v2 = 6, 5
    graph[v1].append(v2) #graph[6].append(5)
    graph[v2].append(v1) #graph[5].append(6)
print(graph)