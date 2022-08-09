#인접행렬
n, m = map(int, input().split())

graph = [[0] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u][v] = 1

print(graph)


#인접리스트

n, m = map(int, input().split())

graph = [[] * (n + 1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

print(graph)