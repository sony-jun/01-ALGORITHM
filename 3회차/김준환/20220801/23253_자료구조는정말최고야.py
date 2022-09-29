# import sys
# input = sys.stdin.readline

# n, m = map(int,input().split())
# dummy_lst = []
# for i in range(m):
#     l = int(input())
#     dummy_lst.append(list(map(int,input().split())))

# idx = 0
# num = 1
# answer = 'No'

# while idx < len(dummy_lst):
#     if len(dummy_lst[idx]) > 0 and dummy_lst[idx][-1] == num:
#         dummy_lst[idx].pop(-1)
#         idx=-1
#         if num == n:
#             answer='Yes'
#             break
#         num += 1
#         idx == 0
#     idx += 1
    
# print(answer)


import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dummy_lst = []
for i in range(m):
    l = int(input())
    dummy_lst.append(list(map(int,input().split())))
answer = 'Yes'
for i in range(m):
    if dummy_lst[i] != sorted(dummy_lst[i], reverse=True):
        answer = 'No'
print(answer)






# 처음 코드

# n, m = map(int,input().split())
# dummy_lst = []
# for i in range(m):
#     l = int(input())
#     dummy_lst.append(list(map(int,input().split())))

# answer='Yes'
# breaker=False
# for num in range(1,n+1):
#     cnt= 0
#     for i in range(len(dummy_lst)):
#         if len(dummy_lst[i])>=1 and num == dummy_lst[i][-1]:
#             dummy_lst[i].pop(-1)
#             break
#         cnt += 1

#         if cnt == len(dummy_lst):
#             answer = 'No'
#             breaker = True
#             break
#     if breaker == True:
#         break
# print(answer)