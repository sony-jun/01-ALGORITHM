from pprint import pprint
n, m = map(int,input().split())

graph = [[0]*(n+1) for i in range(n+1)]

for i in range(m):
    u, v = map(int,input().split())
    graph[u][v] = 1
    graph[v][u] = 0
    pprint(graph)


list_adj = [[] * (n+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] == 1 and graph[j][i] == 0:
            list_adj[i].append(j)
print(list_adj)