from pprint import pprint

N, M = map(int, input().split())

adjacency_matrix = [[0] * (N+1) for _ in range(N+1)]
adjacency_list = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    adjacency_matrix[u][v] = 1
    adjacency_matrix[v][u] = 1
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)
pprint(adjacency_matrix)
print(adjacency_list)