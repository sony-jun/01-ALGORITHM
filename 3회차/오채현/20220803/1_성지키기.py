from pprint import pprint
# n, m = map(int, input().split())

# matrix = [list(map(str, input().split())) for _ in range(n)]

# testcase = [
#     ['X', 'X', '.', '.', '.'],
#     ['.', 'X', 'X', '.', '.'],
#     ['.','.', '.', 'X', 'X']
# ]
# cnt = 0
# for i in range(len(testcase)):
#     if 'X' not in testcase[i]:
#         cnt += 1

# print(cnt)

# pprint(matrix)

n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]

cntrow = 0
cntcol = 0

for i in range(n):
    #각 행에서 경비가 있는지 없는지 확인
    if 'X' not in matrix[i]:
        cntrow += 1

for j in range(m):
    # 각 열에서 경비가 있는지 없는지 확인
    if 'X' not in [matrix[i][j] for i in range(n)]:
        cntcol += 1

print(max(cntrow, cntcol))