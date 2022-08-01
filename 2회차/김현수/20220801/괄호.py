import sys
sys.stdin = open('괄호.txt','r')

from collections import deque

T = int(input()) #테스트케이스 넘버
#1
for k in range(T):
    check_ = 0
    str_ = deque(input())
    for i in str_:
        if check_ < 0: # ')'가 더 많으므로 바로 NO
            break
        elif i == '(':
            check_ += 1
        elif i == ')':
            check_ -= 1
    
    if check_ == 0: #'('')' 갯수가 같다.
        print('YES')
    else :
        print('NO')

#2

# for k in range(T):
#     answer = []
#     str_ = input()
#     for i in str_:
#         if i == '(':
#             answer.append(i)
#         elif i == ')':
#             if answer: #리스트에 무언가 있으면
#                 answer.pop()
#             else:
#                 print('NO')
#                 break
#     else:
#         if answer: #리스트에 무언가 잇으면
#             print('NO')
#         else:
#             print('YES')