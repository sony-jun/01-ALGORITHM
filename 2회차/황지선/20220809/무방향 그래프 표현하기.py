# 무방향 그래프 표현하기
# 인접 행렬

# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하세요.
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

# 입력
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 출력
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 1, 0],
#  [0, 1, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 1, 0, 0, 1],
#  [0, 1, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 1, 0, 0]]
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

# 정점의 개수를 일치시키기 위해 어떻게 입력을 받으면 좋을지 고민해봐라!
# 실제로 이런 형태로 입력을 주는 문제가 많다!

from pprint import pprint

# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
N, M = map(int, input().split())
# pprint(graph)
# v1, v2를 담을 리스트
list_ = []
max_n = 0

# u, v를 리스트 형태로 담기
for _ in range(M):
    u, v = map(int, input().split())
    list_.append([u, v])
# list_ = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]

# 리스트의 길이만큼 for문을 돌려서 간선의 양끝의 값들 중 가장 큰 값들 만을 구한다.
# 그 값이 곧 그래프의 길이가 될 것임.
for i in range(M):
    for j in range(2):
        if list_[i][j] > max_n:
            max_n = list_[i][j]

graph1 = [[0] * (max_n+1) for _ in range(max_n+1)]
graph2 = [[] for _ in range(max_n+1)]

# 큰 리스트 인덱스
for x in range(M):
    # a = u, b = v
    a = list_[x][0]
    b = list_[x][1]
    graph1[a][b] = 1
    graph1[b][a] = 1
    graph2[a].append(b)
    graph2[b].append(a)

pprint(graph1)  # 인접 행렬
pprint(graph2)  # 인접 리스트