import sys

sys.stdin = open('괄호_input.txt')

# 맨 앞이 ')'이면 안됨 / 맨 뒤가 '('이면 안됨

T = int(input())

for i in range(T):
    ps = input()
    ps_ls = []
    cnt = 0
    for j in ps:
        ps_ls.append(j)
    if ps_ls[0] == ')':
        print('NO')
    elif ps_ls[-1] == '(':
        print('NO')
    else:
        for p in ps_ls:
            if p == '(':
                cnt += 1
            if p == ')':
                cnt -= 1
    if cnt == 0:
        print('YES')
    else:
        print('NO')
        
#======================================
# n = int(input())
# left = '('
# right = ')'

# for i in range(n):
#     ps = input()
#     left_stack = []
#     right_stack = []
#     for j in ps:
#         if j == left:
#             left_stack.append(j)
#         if j == right:
#             if len(left_stack) != 0:
#                 left_stack.pop()
#             else:
#                 right_stack.append(j)
#     if len(left_stack) == 0 and len(right_stack) == 0:
#         print('YES')
#     else:
#         print('NO')