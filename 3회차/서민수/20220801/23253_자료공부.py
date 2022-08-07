# 1.  교과서 권 수 n, 교과서 더미 m
# i 더미에 쌓인 교과서는  k 두번째는 k 개의 정수
# 내림차순

import sys


sys.stdin = open("_자료공부.txt")
# input() :
# sys.stdin.readline() : 빠르다

answer = "No"
#stack = [11, 10, 8, 5]
stack_list = [[5,4,3,2,1],[6,2], [9,3]]
# 비교값을 pop 통해서 스택에서 꺼내온다
# 5

for stack in stack_list:
    comparison = stack.pop() 
# top comparison 비교
    while len(stack) != 0:
        if stack[-1] > comparison:
        # pop을 사용해서 comparison 값을 갱신
            comparison = stack.pop()
        else:
            answer = "No"
            break
    
print(answer)