from pprint import pprint

N, M = map(int, input().split())
# N 크기만큼의 인접행렬을 생성
matrix = [[0] * N for _ in range(N)]
edges = [] # 간선의 시작점, 끝점을 담을 리스트

for _ in range(M):
    # 간선의 시작점, 끝점
    u, v = map(int, input().split())
    edges.append([u, v]) # [1, 2] [2, 5] [5, 1] [3, 4] [4, 6]

for edge in edges:
    # v1 = 1 / v2 = 2
    v1, v2 = edge[0], edge[1] # 리스트에 담긴 간선의 시작점[0], 간선의 끝점[1]을 각각 담는다
    # 좌우 대칭으로 입력
    matrix[v2][v1] = 1 # matrix[2][1]
    matrix[v1][v2] = 1 # matrix[1][2]

pprint(matrix)
#[[0, 0, 0, 0, 0, 0, 0],
# [0, 0, 1, 0, 0, 1, 0],
# [0, 1, 0, 0, 0, 1, 0],
# [0, 0, 0, 0, 1, 0, 0],
# [0, 0, 0, 1, 0, 0, 1],
# [0, 1, 1, 0, 0, 0, 0],
# [0, 0, 0, 0, 1, 0, 0]]
