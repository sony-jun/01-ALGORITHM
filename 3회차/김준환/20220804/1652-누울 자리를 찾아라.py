# # from pprint import pprint

# k = int(input())

# matrix = [list(input()) for _ in range(5)]

# # 가로로
# s_r = 0
# for n in range(k):
#     x_set = set()
#     if 'X' not in matrix[n]:
#         x_set.add(k)
#     for m in range(k):
#         # print(f'mat = {matrix[n][m]}')
#         if matrix[n][m] == 'X':
#             # print(matrix[n][m])
#             if m > 1 and matrix[n][m-2] == '.' and matrix[n][m-1] == '.':
#                 x_set.add(m-2)
#             elif m < k-2 and matrix[n][m+2] == '.' and matrix[n][m+1] == '.':
#                 x_set.add(m+1)
#     s_r += len(x_set)

# s_c = 0
# for m in range(k):
#     x_set = set()
#     cnt = 0
#     for n in range(k):
#         if 'X' not in matrix[n][m]:
#             cnt += 1
#             if cnt == k:
#                 x_set.add(k)
#         # print(f'mat = {matrix[n][m]}')
#         if matrix[n][m] == 'X':
#             # print(matrix[n][m])
#             if n > 1 and matrix[n-2][m] == '.' and matrix[n-1][m] == '.':
#                 x_set.add(n-2)
#             elif n < k-2 and matrix[n+2][m] == '.' and matrix[n+1][m] == '.':
#                 x_set.add(n+1)
#     s_c += len(x_set)

# print(s_r , s_c)




# from pprint import pprint

k = int(input())

matrix = [list(input()) for _ in range(k)]

# 가로 탐색
long = 0
cnt = 0
for col in range(k):
    for row in range(k):
        if matrix[col][row] == '.':
            long += 1
        else:
            if long > 1:
                cnt += 1
            long = 0
    if long > 1:
        cnt += 1
    long=0
print(cnt,end=' ')

# 세로 탐색
long = 0
cnt = 0
for row in range(k):
    for col in range(k):
        if matrix[col][row] == '.':
            long += 1
        else:
            if long > 1:
                cnt += 1
            long = 0
    if long > 1:
        cnt += 1
    long=0
print(cnt)