# 2167.
"""
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3

"""
# 배열 크기
import sys
sys.stdin = open("2차원.txt")

N, M = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
K = int(input())
sum_num = 0
# print(matrix)
for count in range(K):
    sum_num = 0
    i, j, x, y = map(int, input().split())
    for row in range(i-1, x):
        for line in range(j-1, y):
            sum_num += matrix[row][line]
    print(sum_num)