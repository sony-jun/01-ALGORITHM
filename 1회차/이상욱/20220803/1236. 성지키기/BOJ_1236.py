import sys
sys.stdin = open('1236.txt')

N, M = map(int, input().split())
row = 0
col = 0
matrix = [list(input()) for i in range(N)]

for i in range(N):
    if 'X' not in matrix[i]:
        row += 1

# for j in range(M):
#     for i in range(N):
#         # print([matrix[i][j]])
#         if 'X' not in [matrix[i][j]]:
#             col += 1

for j in range(M):
    # print([matrix[i][j] for i in range(N)])
    if 'X' not in [matrix[i][j] for i in range(N)]:
        col += 1
print(max(row, col))