import sys
sys.stdin = open('11945.txt')

N, M = map(int, input().split())

matrix = [list(input()) for i in range(N)]

for i in range(N):
    for j in range(len(matrix[0]) -1, -1, -1):
        print(matrix[i][j], end='')
    print()

# for i in range(N):
#     matrix = input()
#     print(matrix[::-1])