N, M = 6, 5
edges = [
    [1, 2],
    [2, 5],
    [5, 1],
    [3, 4],
    [4, 6]
]
edges_set = set()
for i,j in edges:
    edges_set.add(i)
    edges_set.add(j)
if 0 in edges_set:
    N = len(edges_set)
else:
    N = len(edges_set) + 1
matrix = [[0] * N for _ in range(N)]
matrix_list = [[] for _ in range(N)]
for v1, v2 in edges:
    matrix[v1][v2] = 1
    matrix_list[v1].append(v2)
print(matrix)
print(matrix_list)