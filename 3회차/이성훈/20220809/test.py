from pprint import pprint
import sys

sys.stdin = open("1_문제 22. 유방향 그래프 표현하기.txt")


N, M = map(int, input().split())

matrix1 = [[] for _ in range(N + 1)] 
matrix2 = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    matrix1[v1].append(v2)
    matrix2[v1][v2] = 1

pprint(matrix2)
print(matrix1)
