# https://www.acmicpc.net/problem/1652
import sys

sys.stdin = open("0_누울 자리를 찾아라.txt")

N = int(input())
metrix = []
row_count = 0
col_count = 0

for i in range(N):
    metrix.append(list(input()))

for j in range(N):
    cnt_1 , cnt_2 = 0, 0
    for i in range(N):
        if 'X' not in metrix[j][i]:
            cnt_1 += 1
        else:
            cnt_1 = 0
        if cnt_1 == 2:
            row_count += 1


for j in range(N):
    cnt_1 , cnt_2 = 0, 0
    for i in range(N):
        if 'X' not in metrix[i][j]:
            cnt_2 += 1
        else:
            cnt_2 = 0
        if cnt_2 == 2 :
            col_count += 1


print(row_count, col_count)




    
# # https://www.acmicpc.net/problem/1652
# import sys

# sys.stdin = open("0_누울 자리를 찾아라.txt")

# N = int(input())
# metrix = []
# cnt = 0
# cnt_1 = 0
# cnt_2 = 0
# row_list = []
# col_list = []

# for i in range(N):
#     metrix.append(list(input()))

# for j in range(N):
#     for i in range(N-1):
#         if 'X' not in metrix[j][i:i+2]:
#             cnt += 1
#     row_list.append(cnt)
#     cnt = 0
# # print(row_list)

# for j in range(N):
#     for i in range(N-1):
#         if 'X' not in metrix[i][j] and 'X' not in metrix[i+1][j]:
#             cnt += 1
#     col_list.append(cnt)
#     cnt = 0
# # print(col_list)

# for i in row_list:
#     if i > 0:
#         cnt_1 += 1

# for i in col_list:
#     if i > 0:
#         cnt_2 += 1

# print(cnt_1, cnt_2)




    
