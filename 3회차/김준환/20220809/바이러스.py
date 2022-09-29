# # from pprint import pprint
# import sys
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# matrix = [[0]*(n+1) for _ in range(n+1)]
# for _ in range(m):
#     x, y = map(int,input().split())
#     matrix[x][y] = 1
# # pprint(matrix)
# lst = set()
# storage_lst = set({1})
# cnt = 0
# while cnt < n+1:
#     cnt += 1
#     for x in lst:
#         for y in range(n+1):
#             if matrix[x][y] == 1:
#                 storage_lst.add(y)
#     for num in storage_lst:
#         lst.add(num)
#     # print(storage_lst)
# # print(lst)
# print(len(lst)-1)

import sys
input = sys.stdin.readline

n = int(input())         # 컴퓨터 대수
m = int(input())         # 관계 개수
input_lst = []           
for _ in range(m):
    input_lst.append(list(map(int,input().split())))
print(input_lst)
num_set = set({1})
cnt = 0
while cnt < m+1:
    print(num_set)
    cnt += 1
    for case in input_lst:
        if case[0] in num_set:
            num_set.add(case[1])
        if case[1] in num_set:
            num_set.add(case[0])
print(len(num_set)-1)