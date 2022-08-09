# 유방향 인접 행렬/ 리스트 출력하기

""" 
6 5
1 2
2 5
5 1
3 4
4 6

"""
from pprint import pprint
import sys
sys.stdin = open("그래프.txt")

N, M = map(int, input().split())
# N, M = 6, 5
# numbers = [list(map(int, input().split())) for _ in range(N-1)]
# print(numbers)
numbers = [
    [1, 2], 
    [2, 5], 
    [5, 1], 
    [3, 4], 
    [4, 6]
    ]

# print(N, M, numbers)
# pprint(numbers)

# 0으로 초기화(출력값을 맞추기 위해서)
matrix = [[0] * 7 for _ in range(7)]
# # pprint(matrix)

for idx in range(len(numbers)):
    v1, v2 = map(int, numbers[idx])
    matrix[v1][v2] = 1
    # print(v1, v2)
pprint(matrix)

N, M = map(int, input().split())
graph = [[] * 7 for _ in range(7)]
# pprint(graph)
for idx in range(len(numbers)):
    v1, v2 = map(int, numbers[idx])
    graph[v1].append(v2)
print(graph)