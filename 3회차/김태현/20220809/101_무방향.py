from pprint import pprint

import sys
sys.stdin = open("101_무방향.txt", "r")

N, M = map(int, input().split()) # N: 노드 개수, M: 엣지 개수

# 인접 행렬
matrix = []
for _ in range(7):
    matrix.append([0 for _ in range(7)]) # 출력 양식에 맞추기 위해 7개

# 인접 리스트
adj = [[] for _ in range(7)] # 출력 양식에 맞추기 위해 7개

# input() 값 순회하며, 행렬과 리스트에 각각 추가
for i in range(M):
    u, v = map(int, input().split())
    
    # 행렬에 값 추가
    matrix[u][v] += 1
    matrix[v][u] += 1
    
    # 리스트에 값 추가
    adj[u].append(v)
    adj[v].append(u)

pprint(matrix)
pprint(adj)