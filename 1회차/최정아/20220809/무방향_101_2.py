# 인접 리스트
N, M = map(int, input().split())

list_adj = [[] * (N + 1) for i in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == 1:
            list_adj[i].append(j)
print(list_adj)