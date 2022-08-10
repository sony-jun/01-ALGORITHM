from pprint import pprint

N, M = map(int, input().split())
# 인접 행렬 
matrix = [[0] * 7 for _ in range(7)]
# 인접 리스트 
adj_list = [[] for _ in range(7)]
edges = []

for i in range(M):
    u, v = map(int, input().split())
    edges.append([u, v]) # [1, 2], [2, 5], [5, 1], [3, 4], [4, 6]
    # 인접 리스트
    adj_list[u].append(v)
    adj_list[v].append(u)

# 인접행렬
for edge in edges:
    v1, v2 = edge[0], edge[1] # edge 요소의 첫번째와 두번째  1, 2
    matrix[v1][v2] = 1
    matrix[v2][v1] = 1

pprint(matrix)
print(adj_list)

