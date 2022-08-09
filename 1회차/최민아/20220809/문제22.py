import sys
sys.stdin = open("20220809/문제22.txt")

import pprint                                       # 유방향 그래프

N, M = map(int, input().split())                    # 정점 개수, 간선 개수

graph_matrix = [[0] * (N+1) for i in range(N+1)]    # 인접 행렬
graph_list = [[] for i in range(N+1)]               # 인접 리스트

for i in range(M):                                  # 간선 개수 만큼
    u, v = map(int, input().split())                # 간선 양 끝점 u, v
    graph_matrix[u][v] = 1                          # 간선 있으면 1
    graph_list[u].append(v)                         # 인접 정점 추가

pprint.pprint(graph_matrix)                         # 인접 행렬 출력
print(graph_list)                                   # 인접 리스트 출력