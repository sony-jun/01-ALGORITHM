from pprint import pprint

N, M = map(int, input().split())

matrix_ = [[0] * (N+1) for _ in range(N+1)]
list_ = [[] for _ in range(N+1)]

print(list_)

for _ in range(M):
    u, v = map(int, input().split())
    matrix_[u][v] = 1
    matrix_[v][u] = 1

    list_[u].append(v)
    list_[v].append(u)

pprint(matrix_)
print(list_)