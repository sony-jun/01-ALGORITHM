import sys
from pprint import pprint
sys.stdin = open("0_유방향그래프표현하기.txt", 'r')

N, M = map(int, sys.stdin.readline().split())

adjacent_list = []
adjacent_matrix = []

for _ in range(N + 1):
    adjacent_matrix.append([0] * (N + 1))
    adjacent_list.append([])

edges = []

for _ in range(M):
    edges.append([*map(int, sys.stdin.readline().split())])

for v1, v2 in edges:
    adjacent_matrix[v1][v2] = 1

for i in edges:
    adjacent_list[i[0]].append(i[1]) # 인접 리스트의 i[0] 번째 공간에 i[1] 의 값을 추가

pprint(adjacent_list)
pprint(adjacent_matrix)