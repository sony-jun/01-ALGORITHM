import sys
sys.stdin = open('4396_지뢰찾기.txt')

from pprint import pprint

N = int(input())

matrix = [list(input()) for _ in range(N)]
matrix1 = [list(input()) for _ in range(N)]

for row in matrix:
    for col in matrix1:
        if matrix[row][col] == '.' and matrix[row][col] == 'x':
            for i in range(8):
                matrix[row][col] = i

print(matrix)