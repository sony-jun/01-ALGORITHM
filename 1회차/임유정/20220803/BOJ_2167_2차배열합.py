# script
from pprint import pprint

import sys

sys.stdin = open('2167.txt')

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for i in range(n)]
#pprint(matrix)

k = int(input())
point = [list(map(int, input().split())) for i in range(k)]
#pprint(point)

for k in range(k):
    sum = 0
    for i in range((point[k][0] - 1), (point[k][2])):
        for j in range((point[k][1] - 1), (point[k][3])):
            sum += matrix[i][j]
    print(sum)