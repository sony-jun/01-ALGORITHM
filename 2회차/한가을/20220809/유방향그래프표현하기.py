# 그래프 입력이 주어질때 유방향 그래프를
# 인접 행렬과 인접 리스트로 표현

# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다

# 인접 행렬을 출력하고 인접 리스트를 출력

# 출력 예시
# [[0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0]]
# [[], [2], [5], [4], [6], [1], []]

from pprint import pprint
import sys
sys.stdin = open('유방향그래프표현하기.txt')

N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]
graphList = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())

    graph[u][v] = 1
    graph[u][v] = 1

    graphList[u].append(v)

pprint(graph)
print(graphList)